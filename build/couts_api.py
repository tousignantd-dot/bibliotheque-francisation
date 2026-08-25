#!/usr/bin/env python3
"""Le relevé du registre des appels d'API, à l'écran.

    python3 build/couts_api.py                    # tout le registre
    python3 build/couts_api.py --depuis 2026-08-25
    python3 build/couts_api.py --par-route         # par route plutôt que par élève
    python3 build/couts_api.py --fichier chemin.jsonl

Le registre vit sur le volume (`data/appels_api.jsonl`) : en local, c'est
celui du poste ; en production, il se lit par `GET /api/admin/appels`, qui
rend le même calcul filtré au groupe. Ce script n'écrit rien et n'appelle
aucune API — il ne coûte rien de le lancer.

Il répond à la question que la page « Le prix d'un module » posait sans
pouvoir la trancher : combien d'appels un élève fait-il vraiment ? Tant que
la colonne « élèves » reste à zéro, les 36 $ de cette page restent une
hypothèse.
"""

import argparse
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))

import journal_api  # noqa: E402


def sous(montant):
    return "%8.4f $" % montant


def pluriel(n, mot, pluriel_=None):
    """Un compteur qui écrit « 1 appels » se lit comme un défaut de calcul."""
    return "%d %s" % (n, mot if n <= 1 else (pluriel_ or mot + "s"))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--depuis", help="date ISO ; les lignes antérieures sont sautées")
    ap.add_argument("--par-route", action="store_true",
                    help="grouper par route plutôt que par élève")
    ap.add_argument("--fichier", help="un autre registre que celui du poste")
    args = ap.parse_args()

    fichier = Path(args.fichier) if args.fichier else RACINE / "data" / "appels_api.jsonl"
    lignes = journal_api.lire(depuis=args.depuis, fichier=fichier)
    if not lignes:
        print("Registre vide ou absent : %s" % fichier)
        print("Rien n'a encore été compté — les appels d'API du serveur "
              "n'ont pas eu lieu, ou le serveur tournait sans registre.")
        return 0

    releve = journal_api.par_eleve(lignes)
    total = releve["total"]
    print("Registre : %s" % fichier)
    print("%d lignes%s" % (len(lignes), " depuis %s" % args.depuis if args.depuis else ""))
    print()

    if args.par_route:
        print("%-22s %7s %12s %10s %10s" % (
            "route", "appels", "coût", "jetons e.", "jetons s."))
        print("-" * 66)
        par = {}
        for d in lignes:
            seau = par.setdefault(d.get("route") or "?", journal_api._vide())
            journal_api._ajouter(seau, d)
        for route, seau in sorted(par.items(), key=lambda kv: -kv[1]["cout_usd"]):
            print("%-22s %7d %12s %10d %10d" % (
                route, seau["appels"], sous(seau["cout_usd"]),
                seau["jetons_entree"], seau["jetons_sortie"]))
    else:
        print("%-12s %7s %7s %7s %12s" % (
            "élève", "appels", "cache", "échecs", "coût"))
        print("-" * 50)
        for eid, seau in sorted(releve["parEleve"].items(),
                                key=lambda kv: -kv[1]["cout_usd"]):
            print("%-12s %7d %7d %7d %12s" % (
                eid, seau["appels"], seau["cache"], seau["echecs"],
                sous(seau["cout_usd"])))

    print("-" * 66)
    print("total   %s · %s"
          % (pluriel(total["appels"], "appel"), sous(total["cout_usd"])))
    if total["cache"]:
        print("cache   %s servi%s sans rien payer · %s épargnés"
              % (pluriel(total["cache"], "appel"),
                 "" if total["cache"] <= 1 else "s",
                 sous(total["economie_cache_usd"])))
    if total["echecs"]:
        print("échecs  %s sans réponse utilisable"
              % pluriel(total["echecs"], "appel"))

    eleves = [e for e in releve["parEleve"] if e != "sansEleve"]
    if eleves:
        impute = sum(releve["parEleve"][e]["cout_usd"] for e in eleves)
        print("moyenne %s par élève, sur %s ayant appelé"
              % (sous(impute / len(eleves)), pluriel(len(eleves), "élève")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
