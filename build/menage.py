#!/usr/bin/env python3
"""Vider l'installation avant la mise en service.

    DATABASE_URL=… python3 build/menage.py --etat     # ce qui partirait
    DATABASE_URL=… python3 build/menage.py --forcer   # le fait

**Sans `DATABASE_URL`, il ne nettoie que le volume local.** La production est
sur Postgres, et un script lancé d'un poste ne voit que le disque de ce poste —
c'est déjà vrai de `build/controles/organisations.py` et de
`build/couts_api.py`. Le dire est la moitié de l'outil : un ménage qu'on croit
fait est pire qu'un ménage pas fait.

Ce qu'il fait, et dans cet ordre :

1. **Les CSS et les centres partent en cascade** — avec leurs groupes, leurs
   élèves, et tout ce que ces élèves ont laissé : progression, journal d'accès,
   signaux d'aide, vocabulaire, direct de la classe, « Corrige-moi ! »,
   analyses d'erreurs, productions orales (fichiers audio compris) et écrites,
   fichiers partagés au groupe, planification, relevé quotidien, registre des
   appels d'API.
2. **Les comptes s'éteignent, ils ne s'effacent pas** (`actif: false`). Leur
   historique reste lisible, et c'est le comportement que le dépôt tient déjà
   pour les accès. Leurs sessions ouvertes, elles, sont fermées : un jeton
   d'essai qui survit au ménage rouvrirait une porte qu'on croit fermée.
3. **Deux choses ne bougent jamais** : le nœud **réseau**, racine de l'arbre,
   et le **compte fondateur** avec son accès. Sans eux, la console ne se
   rouvre plus et l'installation est morte — c'est le seul geste que
   l'interface elle-même ne pourrait pas réparer.

Ce qu'il ne touche pas, et pourquoi : le **catalogue** d'activités et le
**matériel** (ils décrivent le code livré, pas une classe), les **dépôts de
matériel** des enseignants (des documents, pas des traces d'élèves), le
**journal d'audit** (append-only, et il porte la trace du ménage lui-même), et
les **caches** de traduction et de voix, qui se regénèrent et ne nomment
personne.
"""

import argparse
import json
import os
import pathlib
import shutil
import sys

RACINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE))

import server  # noqa: E402  — on réemploie ses load_*/save_*, qui savent déjà
               # lire et écrire en base comme en fichiers. Une seconde
               # implémentation du stockage finirait par diverger de la
               # première, et c'est le défaut que ce dépôt paie ailleurs.


# ── Les journaux d'élèves : on les vide en entier ───────────────────────────
# (nom lisible, chargeur, sauveur)
JOURNAUX = [
    ("progression",            server.load_progress,           server.save_progress),
    ("journal d'accès",        server.load_access_log,         server.save_access_log),
    ("signaux d'aide",         server.load_signaux_aide,        server.save_signaux_aide),
    ("vocabulaire",            server.load_vocab_progress,      server.save_vocab_progress),
    ("direct de la classe",    server.load_direct,              server.save_direct),
    ("« Corrige-moi ! »",      server.load_corrige_moi,         server.save_corrige_moi),
    ("analyses d'erreurs",     server.load_analyses_erreurs,    server.save_analyses_erreurs),
    ("productions orales",     server.load_oral_submissions,    server.save_oral_submissions),
    ("productions écrites",    server.load_written_submissions, server.save_written_submissions),
    ("fichiers de groupe",     server.load_documents,           server.save_documents),
    ("planification",          server.load_schedule,            server.save_schedule),
    ("signalements",           server.load_signalements,        server.save_signalements),
]

# Les dossiers de fichiers déposés par les élèves. Effacer la fiche sans
# effacer l'audio laisserait des enregistrements de personnes réelles sur le
# volume, sans plus rien pour dire à qui ils appartiennent.
DOSSIERS = ["assets/oral-submissions", "assets/documents-groupe"]

# Le relevé quotidien et le registre des appels ne passent pas par un
# load_/save_ : ce sont des fichiers à part.
FICHIERS = ["data/stats_jour.json", "data/appels_api.jsonl"]


def dossier_donnees():
    return pathlib.Path(os.environ.get("STORAGE_DIR", str(RACINE)))


def stockage():
    """« postgres » ou « fichiers » — la même question que `/api/health`."""
    try:
        return "postgres" if server._db and server._db.disponible() else "fichiers"
    except Exception:
        return "fichiers"


def releve():
    """Ce qu'il y a, sans rien écrire."""
    orgs = server.load_organisations()
    reseau = next((o for o in orgs if o.get("type") == "reseau"), None)
    teachers = server.load_teachers()
    fondateur_id = server.founder_id(teachers)

    a_supprimer = [o for o in orgs if o is not reseau]
    a_eteindre = [t for t in teachers if t["id"] != fondateur_id
                  and t.get("actif") is not False]

    etat = {
        "stockage": stockage(),
        "reseau": reseau,
        "fondateur": next((t for t in teachers if t["id"] == fondateur_id), None),
        "orgs": a_supprimer,
        "groupes": server.load_groups(),
        "eleves": server.load_students(),
        "comptes": a_eteindre,
        "acces": [a for a in server.load_acces()
                  if not (a.get("teacherId") == fondateur_id
                          and reseau and a.get("orgId") == reseau["id"])],
        "journaux": [],
        "fichiers": [],
    }
    for nom, charger, _ in JOURNAUX:
        try:
            etat["journaux"].append((nom, len(charger())))
        except Exception as e:
            etat["journaux"].append((nom, "illisible : %s" % e))
    base = dossier_donnees()
    for rel in DOSSIERS:
        d = base / rel
        n = sum(1 for _ in d.rglob("*") if _.is_file()) if d.exists() else 0
        etat["fichiers"].append((rel, n))
    for rel in FICHIERS:
        f = base / rel
        etat["fichiers"].append((rel, 1 if f.exists() else 0))
    return etat


def afficher(etat):
    print("Stockage : %s" % etat["stockage"])
    if etat["stockage"] == "fichiers":
        print("  ⚠ Sans DATABASE_URL, ce ménage ne touche QUE le volume local")
        print("    (%s). La production n'en saura rien." % dossier_donnees())
    print()
    print("CE QUI RESTE")
    r, f = etat["reseau"], etat["fondateur"]
    print("  réseau     : %s" % (r.get("nom") if r else "— aucun nœud réseau !"))
    print("  fondateur  : %s (%s)" % (f.get("nom") if f else "—",
                                      (f or {}).get("code", "sans code")))
    print()
    print("CE QUI PART")
    print("  organisations      : %d" % len(etat["orgs"]))
    for o in etat["orgs"]:
        print("      %-9s %s" % (o.get("type", "?"), o.get("nom", "")))
    print("  groupes            : %d" % len(etat["groupes"]))
    print("  élèves             : %d" % len(etat["eleves"]))
    print("  accès              : %d" % len(etat["acces"]))
    for nom, n in etat["journaux"]:
        print("  %-18s : %s" % (nom, n))
    for rel, n in etat["fichiers"]:
        print("  %-18s : %s" % (rel.split("/")[-1], n))
    print()
    print("CE QUI S'ÉTEINT (le compte reste, il ne se connecte plus)")
    print("  comptes            : %d" % len(etat["comptes"]))
    for t in etat["comptes"]:
        print("      %-24s %s" % (t.get("nom", ""), t.get("code", "")))


def menage(etat):
    reseau = etat["reseau"]
    fondateur = etat["fondateur"]
    if reseau is None:
        print("Refus : aucun nœud « reseau » dans l'arbre. Sans racine, le "
              "ménage laisserait une installation sans portée.")
        return 1
    if fondateur is None:
        print("Refus : aucun compte fondateur. Le ménage fermerait la porte "
              "derrière lui.")
        return 1

    # 1. L'arbre : on ne garde que la racine.
    server.save_organisations([reseau])
    # 2. Les accès : seul celui du fondateur sur le réseau survit.
    server.save_acces([a for a in server.load_acces()
                       if a.get("teacherId") == fondateur["id"]
                       and a.get("orgId") == reseau["id"]])
    # 3. Groupes et élèves, en entier.
    server.save_groups([])
    server.save_students([])
    # 4. Tout ce que les élèves ont laissé.
    for nom, _, sauver in JOURNAUX:
        try:
            sauver([])
        except Exception as e:
            print("  ! %s : %s" % (nom, e))
    # 5. Les comptes s'éteignent, ils ne s'effacent pas.
    teachers = server.load_teachers()
    for t in teachers:
        if t["id"] != fondateur["id"]:
            t["actif"] = False
    server.save_teachers(teachers)
    # 6. Les sessions ouvertes : un jeton d'essai qui survit au ménage
    #    rouvrirait une porte qu'on croit fermée.
    sessions = server.load_sessions()
    server.save_sessions({j: s for j, s in sessions.items()
                          if s.get("teacherId") == fondateur["id"]})
    # 7. Les fichiers déposés et les deux relevés à part.
    base = dossier_donnees()
    for rel in DOSSIERS:
        d = base / rel
        if d.exists():
            shutil.rmtree(d, ignore_errors=True)
            d.mkdir(parents=True, exist_ok=True)
    for rel in FICHIERS:
        f = base / rel
        if f.exists():
            f.unlink()

    server.journal(fondateur, "installation.menage", str(reseau["id"]),
                   {"organisations": len(etat["orgs"]),
                    "groupes": len(etat["groupes"]),
                    "eleves": len(etat["eleves"]),
                    "comptesEteints": len(etat["comptes"])})
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__)
    ap.add_argument("--etat", action="store_true",
                    help="montrer ce qui partirait, sans rien écrire (défaut)")
    ap.add_argument("--forcer", action="store_true",
                    help="faire le ménage pour de bon")
    args = ap.parse_args()

    etat = releve()
    afficher(etat)
    if not args.forcer:
        print()
        print("Rien n'a été écrit. Relancez avec --forcer pour agir.")
        return 0

    print()
    print("--forcer : le ménage se fait maintenant.")
    code = menage(etat)
    if code == 0:
        print()
        print("Fait. Il reste le nœud réseau et le compte fondateur.")
        print("La suite : ouvrir les CSS et les centres depuis reseau.html,")
        print("puis les comptes de direction, qui ouvriront les leurs.")
    return code


if __name__ == "__main__":
    sys.exit(main())
