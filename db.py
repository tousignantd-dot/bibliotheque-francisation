#!/usr/bin/env python3
"""Stockage Postgres — la migration du chantier « Le réseau des centres ».

**Le repli est la règle, pas l'exception.** Sans `DATABASE_URL`, ou sans le
pilote, ce module se déclare indisponible et `server.py` continue d'écrire
dans les fichiers du volume, exactement comme avant. C'est ce qui permet de
livrer la migration sans que le poste local ait besoin d'une base, et de
revenir en arrière en retirant une variable d'environnement.

Deux formes de rangement, et la différence n'est pas cosmétique :

- **Les collections tenues en document** — comptes, groupes, arbre, accès,
  planification, invitations… Petites, bornées, modifiées par une personne à
  la fois. Une ligne de `documents`, la liste entière en JSONB. On y gagne
  l'atomicité et l'indépendance du volume, pas la concurrence fine ; le verrou
  de `server.py` s'en charge.
- **Les journaux d'élèves** — progression, accès, signaux d'aide, vocabulaire.
  Une **ligne par enregistrement**, avec l'index unique qui porte la règle
  métier (« un enregistrement par élève, activité et événement »). L'écriture
  devient un `INSERT … ON CONFLICT DO UPDATE` : on ne relit plus la liste
  entière pour y ajouter une ligne. C'est là qu'était le mur — 128
  enregistrements pesaient déjà 42 Ko, et une classe de trente en produit des
  milliers par session.
"""
import json
import os
import threading

try:
    import psycopg
    from psycopg.rows import dict_row
    from psycopg_pool import ConnectionPool
    _PILOTE = True
except ImportError:                                    # pragma: no cover
    try:
        import psycopg
        from psycopg.rows import dict_row
        ConnectionPool = None
        _PILOTE = True
    except ImportError:
        psycopg = None
        dict_row = None
        ConnectionPool = None
        _PILOTE = False

_POOL = None
_VERROU = threading.Lock()

# **Une liste explicite, jamais « tout ce qui traîne dans data/ ».** Certains
# fichiers de `data/` sont du **code versionné** — `materiel.json` et
# `sections.json` sont produits par le build et décrivent ce que le dépôt
# livre. Les faire passer en base créerait une deuxième vérité, et c'est le
# défaut que ce dépôt connaît déjà. Ce qui n'est pas nommé ici reste sur le
# volume, et c'est le comportement sûr.
DOCUMENTS = {
    "teachers.json", "groups.json", "students.json", "schedule.json",
    "organisations.json", "acces.json", "invitations.json", "audit.json",
    "documents.json", "prof_sessions.json", "depots.json", "promotions.json",
    "corrige_moi.json", "oral_submissions.json", "written_submissions.json",
    "signalements.json", "analyses_erreurs.json", "traductions.json",
}

# Les journaux d'élèves, rangés en lignes. La clé est le nom du fichier JSON
# qu'ils remplacent : `server.py` continue de raisonner en fichiers, et c'est
# ce module qui sait où ça vit vraiment.
JOURNAUX = {
    "progress.json": {
        "table": "progression",
        "cle": ("studentId", "activityId", "event"),
    },
    "access_log.json": {
        "table": "journal_acces",
        "cle": None,                                   # ajout pur
    },
    "signaux_aide.json": {
        "table": "signaux_aide",
        "cle": ("studentId", "activityId", "exercice"),
    },
    "vocab_progress.json": {
        "table": "vocab_progression",
        "cle": ("studentId", "wordId"),
    },
}


def url():
    return os.environ.get("DATABASE_URL", "").strip()


def disponible():
    """Postgres est-il utilisable ? Le silence vaut « non », et « non » est sûr."""
    return bool(_PILOTE and url())


def _pool():
    global _POOL
    if _POOL is None:
        with _VERROU:
            if _POOL is None:
                if ConnectionPool is not None:
                    _POOL = ConnectionPool(url(), min_size=1, max_size=8,
                                           kwargs={"row_factory": dict_row})
                else:
                    _POOL = None
    return _POOL


class _ConnexionSimple:
    """Repli quand `psycopg_pool` manque : une connexion par geste.

    Moins efficace, mais le module doit marcher avec le seul `psycopg`
    installé — c'est ce qui arrive quand on épingle une dépendance de moins.
    """
    def __enter__(self):
        self._c = psycopg.connect(url(), row_factory=dict_row)
        return self._c

    def __exit__(self, *e):
        self._c.close()
        return False


def connexion():
    p = _pool()
    return p.connection() if p is not None else _ConnexionSimple()


SCHEMA = """
CREATE TABLE IF NOT EXISTS documents (
    nom        text PRIMARY KEY,
    donnees    jsonb NOT NULL,
    modifie_le timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS progression (
    id          bigserial PRIMARY KEY,
    student_id  integer NOT NULL,
    activity_id integer,
    evenement   text    NOT NULL,
    doc         jsonb   NOT NULL,
    horodatage  text    NOT NULL DEFAULT ''
);
-- La règle métier « un enregistrement par (élève, activité, événement) »
-- devient une contrainte de la base. Elle était jusqu'ici tenue par une
-- recherche en Python dans la liste entière, donc perdue dès que deux
-- requêtes se croisaient.
CREATE UNIQUE INDEX IF NOT EXISTS progression_cle
    ON progression (student_id, activity_id, evenement);
CREATE INDEX IF NOT EXISTS progression_jour ON progression (left(horodatage, 10));

CREATE TABLE IF NOT EXISTS journal_acces (
    id         bigserial PRIMARY KEY,
    student_id integer,
    doc        jsonb NOT NULL,
    horodatage text  NOT NULL DEFAULT ''
);
CREATE INDEX IF NOT EXISTS journal_acces_eleve ON journal_acces (student_id);

CREATE TABLE IF NOT EXISTS signaux_aide (
    id          bigserial PRIMARY KEY,
    student_id  integer NOT NULL,
    activity_id integer,
    exercice    text    NOT NULL DEFAULT '',
    doc         jsonb   NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS signaux_aide_cle
    ON signaux_aide (student_id, activity_id, exercice);

CREATE TABLE IF NOT EXISTS vocab_progression (
    id         bigserial PRIMARY KEY,
    student_id integer NOT NULL,
    word_id    text    NOT NULL,
    doc        jsonb   NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS vocab_progression_cle
    ON vocab_progression (student_id, word_id);
"""


def init_schema():
    with connexion() as c:
        with c.cursor() as cur:
            cur.execute(SCHEMA)
        c.commit()


# ── Collections tenues en document ──────────────────────────────────────────

def lire_document(nom, defaut=None):
    with connexion() as c:
        with c.cursor() as cur:
            cur.execute("SELECT donnees FROM documents WHERE nom = %s", (nom,))
            r = cur.fetchone()
    if r is None:
        return [] if defaut is None else defaut
    return r["donnees"]


def gere(fichier):
    """Ce fichier est-il rangé en base ? Le nom, pas le chemin."""
    return fichier in DOCUMENTS or fichier in JOURNAUX


def ecrire_document(nom, donnees):
    with connexion() as c:
        with c.cursor() as cur:
            cur.execute(
                "INSERT INTO documents (nom, donnees, modifie_le) "
                "VALUES (%s, %s, now()) "
                "ON CONFLICT (nom) DO UPDATE "
                "SET donnees = EXCLUDED.donnees, modifie_le = now()",
                (nom, json.dumps(donnees, ensure_ascii=False)))
        c.commit()


# ── Journaux d'élèves, ligne par ligne ──────────────────────────────────────

def lire_journal(fichier):
    """La liste entière, dans l'ordre d'insertion — même forme qu'avant.

    `server.py` reçoit exactement ce que `_load_json_list` lui rendait, donc
    les écrans n'ont rien à savoir de la base. Les lectures ciblées viendront
    quand un écran en aura besoin ; les rendre toutes ciblées d'un coup serait
    réécrire les tableaux de bord en même temps que le stockage, et on ne
    saurait plus lequel des deux a cassé.
    """
    table = JOURNAUX[fichier]["table"]
    with connexion() as c:
        with c.cursor() as cur:
            cur.execute(f"SELECT doc FROM {table} ORDER BY id")
            return [r["doc"] for r in cur.fetchall()]


def _colonnes(fichier, entree):
    if fichier == "progress.json":
        return {"student_id": entree.get("studentId"),
                "activity_id": entree.get("activityId"),
                "evenement": entree.get("event") or "",
                "horodatage": entree.get("timestamp") or ""}
    if fichier == "access_log.json":
        return {"student_id": entree.get("studentId"),
                "horodatage": entree.get("timestamp") or ""}
    if fichier == "signaux_aide.json":
        return {"student_id": entree.get("studentId"),
                "activity_id": entree.get("activityId"),
                "exercice": entree.get("exercice") or ""}
    return {"student_id": entree.get("studentId"),
            "word_id": str(entree.get("wordId") or "")}


def enregistrer(fichier, entree):
    """Pose ou met à jour **un** enregistrement. Ne lit jamais la liste.

    C'est tout l'objet de la migration : l'écriture ne dépend plus de la
    taille du journal. `ON CONFLICT` fait tenir la règle métier à la base,
    donc deux requêtes simultanées ne peuvent plus produire deux lignes ni
    s'effacer l'une l'autre.
    """
    spec = JOURNAUX[fichier]
    table, cle = spec["table"], spec["cle"]
    cols = _colonnes(fichier, entree)
    cols["doc"] = json.dumps(entree, ensure_ascii=False)
    noms = ", ".join(cols)
    valeurs = ", ".join(f"%({k})s" for k in cols)
    if cle:
        cles_sql = {"progress.json": "student_id, activity_id, evenement",
                    "signaux_aide.json": "student_id, activity_id, exercice",
                    "vocab_progress.json": "student_id, word_id"}[fichier]
        maj = ", ".join(f"{k} = EXCLUDED.{k}" for k in cols if k not in cles_sql)
        sql = (f"INSERT INTO {table} ({noms}) VALUES ({valeurs}) "
               f"ON CONFLICT ({cles_sql}) DO UPDATE SET {maj}")
    else:
        sql = f"INSERT INTO {table} ({noms}) VALUES ({valeurs})"
    with connexion() as c:
        with c.cursor() as cur:
            cur.execute(sql, cols)
        c.commit()


def remplacer_journal(fichier, entrees):
    """Réécrit un journal en entier. Sert à la migration et aux purges.

    Volontairement peu employé : c'est exactement le geste que la migration
    cherche à faire disparaître du chemin normal.
    """
    table = JOURNAUX[fichier]["table"]
    with connexion() as c:
        with c.cursor() as cur:
            cur.execute(f"DELETE FROM {table}")
        c.commit()
    for e in entrees:
        enregistrer(fichier, e)


def compter():
    """Un état des lieux, pour la commande de migration et le contrôle."""
    etat = {}
    with connexion() as c:
        with c.cursor() as cur:
            # `jsonb_array_length` échoue sur un objet : tous les documents ne
            # sont pas des listes, et un compteur qui plante n'aide personne.
            cur.execute("SELECT nom, CASE WHEN jsonb_typeof(donnees) = 'array' "
                        "THEN jsonb_array_length(donnees) ELSE -1 END AS n "
                        "FROM documents ORDER BY nom")
            etat["documents"] = {r["nom"]: r["n"] for r in cur.fetchall()}
            for f, spec in JOURNAUX.items():
                cur.execute(f"SELECT count(*) AS n FROM {spec['table']}")
                etat[spec["table"]] = cur.fetchone()["n"]
    return etat
