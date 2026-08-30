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


def dossier_donnees():
    return pathlib.Path(os.environ.get("STORAGE_DIR", str(RACINE)))


def base_demandee():
    """`DATABASE_URL` est-elle posée ? — c'est l'intention, pas le résultat."""
    return bool(os.environ.get("DATABASE_URL", "").strip())


def base_repond():
    """La base répond-elle vraiment ? Rend (oui, motif).

    **Ce contrôle est le filet de tout l'outil, et il a été ajouté après un
    incident.** `_load_json_list` retombe sur le fichier du volume quand la
    base est injoignable — c'est **voulu** côté serveur : si la base tombe en
    pleine séance, rendre une liste vide viderait le portail et l'enseignante
    recréerait ce qu'elle croit perdu. Mais un outil de purge qui hérite de ce
    repli montre le disque du poste **en annonçant la production**, et invite
    à effacer en croyant viser ailleurs.

    On ne se fie donc pas à `db.disponible()`, qui ne regarde que la présence
    d'une adresse et d'un pilote : on ouvre la connexion et on interroge.
    """
    if not base_demandee():
        return False, "DATABASE_URL n'est pas posée"
    if not (server._db and server._db.disponible()):
        return False, "le pilote psycopg est absent du poste"
    try:
        with server._db.connexion() as c:
            with c.cursor() as cur:
                cur.execute("SELECT 1")
        return True, ""
    except Exception as e:
        return False, str(e).strip().splitlines()[0]


def stockage():
    """« postgres » ou « fichiers » — mesuré, pas déduit."""
    return "postgres" if base_repond()[0] else "fichiers"


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
    vu = server.menage_releve()
    etat["journaux"] = [(j["nom"], j["n"] if j["n"] is not None else j.get("erreur"))
                        for j in vu["journaux"]]
    etat["fichiers"] = [(f["nom"], f["n"]) for f in vu["fichiers"]]
    return etat


def afficher(etat):
    print("Stockage : %s  (vérifié par une requête, pas déduit)" % etat["stockage"])
    if etat["stockage"] == "fichiers":
        print("  ⚠ Ce ménage ne touche QUE le volume local (%s)." % dossier_donnees())
        print("    La production n'en saura rien.")
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
    """Le geste lui-même vit dans `server.menage_executer()`, qui sert aussi le
    bouton de la console. Deux implémentations d'un même effacement, ce serait
    deux façons de se tromper."""
    fait, motif = server.menage_executer(etat["fondateur"])
    if not fait:
        print("Refus : %s" % motif)
        return 1
    server.journal(etat["fondateur"], "installation.menage",
                   str((etat["reseau"] or {}).get("id", "")),
                   {"organisations": len(etat["orgs"]), "groupes": len(etat["groupes"]),
                    "eleves": len(etat["eleves"]), "comptesEteints": len(etat["comptes"])})
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__)
    ap.add_argument("--etat", action="store_true",
                    help="montrer ce qui partirait, sans rien écrire (défaut)")
    ap.add_argument("--forcer", action="store_true",
                    help="faire le ménage pour de bon")
    ap.add_argument("--local", action="store_true",
                    help="viser le volume de ce poste, et non la production")
    args = ap.parse_args()

    # Le refus vient avant le relevé : un inventaire du mauvais volume est
    # exactement ce qui fait effacer à côté.
    if base_demandee():
        ok, motif = base_repond()
        if not ok:
            print("Refus : DATABASE_URL est posée, mais la base ne répond pas.")
            print("  %s" % motif)
            print()
            print("Sans elle, chaque lecture retomberait en silence sur le volume")
            print("local (%s) et l'inventaire montrerait les données de ce poste" % dossier_donnees())
            print("en croyant montrer la production. Rien n'a été lu ni écrit.")
            print()
            print("À vérifier : l'adresse est bien celle du proxy public")
            print("(DATABASE_PUBLIC_URL, hôte en .proxy.rlwy.net), entre guillemets")
            print("simples, et collée en entier — elle commence par postgresql://")
            return 1

    etat = releve()
    afficher(etat)

    # **Le refus qui manquait, et qui a coûté un volume.** Le 29 août 2026, un
    # `--forcer` lancé sans `DATABASE_URL` — l'adresse n'avait pas été prise par
    # le shell — a vidé le disque du poste au lieu de la production. Le script
    # avertissait pourtant, en toutes lettres, deux lignes plus haut : un
    # avertissement ne retient pas la main de quelqu'un qui vient de taper la
    # commande qu'on lui a donnée. Viser son propre poste doit donc se demander,
    # et jamais être ce qui arrive par défaut quand la vraie cible manque.
    if args.forcer and not base_demandee() and not args.local:
        print()
        print("Refus : rien n'indique quelle installation vider.")
        print("  Sans DATABASE_URL, la cible serait le volume de ce poste —")
        print("  %s — et non la production." % dossier_donnees())
        print()
        print("  Pour la production : posez DATABASE_URL (DATABASE_PUBLIC_URL")
        print("  du service Postgres) et relancez.")
        print("  Pour ce poste, en connaissance de cause : ajoutez --local.")
        return 1
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
