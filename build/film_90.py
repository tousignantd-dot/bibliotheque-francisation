#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le film de 90 secondes : voix off, images, montage.

    python3 build/film_90.py --voix      # synthétise les 14 répliques (Azure)
    python3 build/film_90.py --minutage  # mesure et confronte au découpage
    python3 build/film_90.py --montage   # assemble le .mp4

Le storyboard est `assets/presentations/film-90-secondes.html` ; ce script en
est l'exécution. **Les durées ci-dessous sont celles du storyboard** : le
`--minutage` dit si la voix y entre, et c'est lui qui commande, pas l'inverse.
Une voix off se compte, elle ne s'estime pas — le premier jet du texte montait
à 4,5 mots par seconde sur le plan 01, ce qui est indisable.

LE PIÈGE DU MONTAGE, déjà payé une fois sur l'animatique du teaser de 48 s :
`xfade` **raccourcit la sortie de la durée du fondu**. Chaque segment doit donc
être allongé d'autant, et le décalage de chaque fondu vaut la somme des durées
*voulues* — jamais des durées réelles des fichiers. Sans ça la voix off dérive
par rapport à l'image, et ça ne se voit qu'à la fin.
"""

import argparse
import json
import os
import pathlib
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "film-90-secondes"
sys.path.insert(0, str(RACINE))

# Le débit de la voix off. Au débit par défaut d'Azure, les quatorze
# répliques ne font que 52,8 s dans un film de 90 : 41 % de silence, ce qui
# n'est plus de la respiration mais du vide. Mesuré sur la réplique la plus
# longue : défaut 9,33 s · -6 % 11,41 s · -12 % 12,19 s · -18 % 13,07 s. On
# retient -8 %, qui pose la voix sans la traîner et laisse environ 1,7 s de
# souffle par plan.
REFERENCE = "-8%"
FONDU = 0.5          # durée d'un fondu enchaîné
LARGEUR, HAUTEUR, IPS = 1920, 1080, 25

# num, début, fin, titre, voix off, provenance de l'image
#   "creee"   → image à générer (build/film_90_images.py)
#   "capture" → capture réelle de l'application
PLANS = [
    ("01", 0, 5,  "Le point qui ne sort pas",
     "Il y a un moment où l'on décide de ne rien dire.", "creee"),
    ("02", 5, 12, "Le comptoir",
     "Au comptoir. Au téléphone. Devant un propriétaire.", "creee"),
    ("03", 12, 18, "Trois fois rien",
     "On comprend. On connaît les mots. Mais on ne se lance pas.", "creee"),
    ("04", 18, 24, "Le comptoir se replie",
     "francis met cette conversation-là dans un endroit où se tromper ne coûte rien.",
     "creee"),
    ("05", 24, 29, "Il choisit, et il parle",
     "L'élève choisit une situation. Et il parle.", "capture"),
    ("06", 29, 34, "Quelqu'un répond",
     "En face, quelqu'un répond — et s'ajuste à ce qu'il vient de dire.", "capture"),
    ("07", 34, 42, "Écrit ici",
     "Les situations ne sont pas génériques. Elles ont été écrites ici, pour ce qui se passe ici.",
     "creee"),
    ("08", 42, 48, "Ce qu'il a dit, et comment",
     "À la fin, une rétroaction sur sa grammaire et sur la clarté de ce qu'il a dit.",
     "capture"),
    ("09", 48, 55, "Et elle s'efface",
     "Elle est à lui. Elle ne se conserve pas, et personne d'autre ne la lit.", "creee"),
    ("10", 55, 59, "Quinze pupitres",
     "Et pendant ce temps, l'enseignante voit son groupe.", "creee"),
    ("11", 59, 65, "C'est elle qui décide",
     "Ce n'est pas la machine qui décide de la suite. C'est elle.", "capture"),
    ("12", 65, 71, "Quatre interrupteurs",
     "Un centre n'a pas à nous faire confiance. Il coche.", "creee"),
    ("13", 71, 84, "Ce qui ne sort plus",
     "Aucun vrai nom. Aucun courriel. Les productions s'effacent après trente jours. "
     "Et si la direction refuse l'assistance, plus rien ne quitte le serveur.", "creee"),
    ("14", 84, 90, "La phrase sort",
     "Et un jour, au comptoir, la phrase sort.", "creee"),
]


def vo(num):
    return SORTIE / ("vo-%s.mp3" % num)


def image(num):
    return SORTIE / ("plan-%s.jpg" % num)


def duree(chemin):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(chemin)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


# ── La voix ────────────────────────────────────────────────────────────────
def faire_voix():
    """Sylvie, la voix de l'enseignante — la même que l'animatique de 48 s.

    On ROGNE les silences de tête et de queue : Azure en pose de longs, et un
    film montré à la seconde près ne peut pas se permettre une demi-seconde
    de vide au début de chaque plan. Les silences internes ne sont jamais
    touchés — les pauses de ponctuation sont voulues.
    """
    from build import azure_voix
    SORTIE.mkdir(parents=True, exist_ok=True)
    total = 0.0
    print(" plan  voulu  réel   marge   verdict")
    for num, d, f, titre, texte, _ in PLANS:
        dest = vo(num)
        azure_voix.parle(texte, "enseignante", dest, reference=REFERENCE)
        azure_voix.rogner_silences(dest, marge=0.12)
        reel = duree(dest)
        voulu = f - d
        marge = voulu - reel
        total += reel
        etat = "DÉBORDE" if marge < 0.25 else ("large" if marge > 2.5 else "bon")
        print("  %s   %4.1f  %5.2f  %+5.2f   %s" % (num, voulu, reel, marge, etat))
    print("\n  parole : %.1f s · film : %d s" % (total, PLANS[-1][2]))


def minutage():
    print(" plan  voulu  réel   marge   verdict")
    manque = 0
    for num, d, f, titre, texte, _ in PLANS:
        if not vo(num).exists():
            print("  %s   — pas encore synthétisé" % num); manque += 1; continue
        reel, voulu = duree(vo(num)), f - d
        marge = voulu - reel
        etat = "DÉBORDE" if marge < 0.25 else ("large" if marge > 2.5 else "bon")
        print("  %s   %4.1f  %5.2f  %+5.2f   %s" % (num, voulu, reel, marge, etat))
        manque += marge < 0.25
    return 1 if manque else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--voix", action="store_true")
    ap.add_argument("--minutage", action="store_true")
    ap.add_argument("--montage", action="store_true")
    a = ap.parse_args()
    if a.voix:
        faire_voix()
    if a.minutage:
        return minutage()
    if a.montage:
        from build.film_90_montage import monter
        monter(PLANS, SORTIE, FONDU, LARGEUR, HAUTEUR, IPS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
