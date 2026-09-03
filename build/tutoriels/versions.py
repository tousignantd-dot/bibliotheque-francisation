#!/usr/bin/env python3
"""La version du storyboard, et qui l'a bougée.

    python3 build/tutoriels/versions.py                       # l'état
    python3 build/tutoriels/versions.py 01-tour-du-portail "les quatre états montrés"
    python3 build/tutoriels/versions.py 01-tour-du-portail "captures refaites" --mineure

Sans repère de version, on ne sait pas si ce qu'on relit est ce qu'on a
demandé. La question s'est posée le 3 septembre 2026, telle quelle : « est-ce
que tu as mis à jour le storyboard ? » — et rien dans la page ne permettait
d'y répondre.

Deux rangs, et la distinction est le fond du problème :

· **majeure** — j'ai retouché le storyboard : un texte réécrit, un plan
  ajouté ou retiré, des gestes changés. C'est une nouvelle version à relire.
· **mineure** — les copies d'écran ont été reprises, le texte n'a pas bougé.
  Le bouton « Mettre à jour le guide » ne fait que ça.

Ce que l'utilisateur tape lui-même dans l'atelier **ne bouge pas la
version** : c'est son brouillon, pas une livraison. Compter ses propres
frappes comme des versions rendrait le repère inutile en une séance.

L'historique garde les dix derniers rangs — assez pour savoir ce qui s'est
passé depuis la dernière lecture, pas assez pour devenir un journal.
"""
import json
import pathlib
import sys
from datetime import datetime

ICI = pathlib.Path(__file__).resolve().parent
FICHIER = ICI / "guide" / "versions.json"

MOIS = ("janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre")


def lire():
    return json.loads(FICHIER.read_text(encoding="utf-8")) if FICHIER.exists() else {}


def horodatage(quand=None):
    q = quand or datetime.now()
    return "%d %s %d, %02d h %02d" % (q.day, MOIS[q.month - 1], q.year,
                                      q.hour, q.minute)


def etat(capsule):
    """La version d'une capsule, telle qu'elle s'affiche. Jamais None."""
    fiche = lire().get(capsule)
    if not fiche:
        return {"version": "v1.0", "quand": "", "quoi": "première écriture",
                "historique": []}
    return fiche


def poser(capsule, quoi, majeure=True):
    """Monte la version d'une capsule et note ce qui a changé."""
    tout = lire()
    fiche = tout.get(capsule, {"version": "v1.0", "historique": []})
    majeur, mineur = (int(x) for x in fiche["version"][1:].split("."))
    if majeure:
        majeur, mineur = majeur + 1, 0
    else:
        mineur += 1
    fiche["version"] = "v%d.%d" % (majeur, mineur)
    fiche["quand"] = horodatage()
    fiche["quoi"] = quoi
    fiche.setdefault("historique", []).insert(
        0, {"version": fiche["version"], "quand": fiche["quand"], "quoi": quoi})
    fiche["historique"] = fiche["historique"][:10]
    tout[capsule] = fiche
    FICHIER.parent.mkdir(parents=True, exist_ok=True)
    FICHIER.write_text(json.dumps(tout, ensure_ascii=False, indent=1),
                       encoding="utf-8")
    return fiche


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--mineure"]
    if not args:
        for capsule, fiche in sorted(lire().items()):
            print("%-24s %-6s %s — %s" % (capsule, fiche["version"],
                                          fiche.get("quand", ""), fiche.get("quoi", "")))
        if not lire():
            print("aucune version posée")
    else:
        fiche = poser(args[0], args[1] if len(args) > 1 else "mise à jour",
                      majeure="--mineure" not in sys.argv)
        print("%s → %s · %s · %s" % (args[0], fiche["version"], fiche["quand"],
                                     fiche["quoi"]))
