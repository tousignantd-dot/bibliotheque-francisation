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

# Le débit. Sur la voix ordinaire, `<prosody rate>` agit franchement. **Sur
# DragonHD, presque pas** — mesuré sur la réplique la plus longue : défaut
# 9,38 s, -8 % 9,36 s (soit rien, dans le bruit de la synthèse), -15 % 9,92 s,
# c'est-à-dire 6 % de plus pour 15 % demandés. La prosodie HD se calcule sur la
# phrase entière et ne se laisse pas étirer. On garde -15 %, le maximum utile,
# et ce sont les DURÉES DE PLAN qui s'ajustent à la voix, jamais l'inverse.
# La voix : Sylvie en DragonHD — la même comédienne que la version
# précédente, mais la prosodie se calcule sur la phrase entière au lieu
# d'être plate. C'est celle du jeu de rôle.
ROLE = "hd_feminin"
REFERENCE = "-15%"
FONDU = 0.5          # durée d'un fondu enchaîné
LARGEUR, HAUTEUR, IPS = 1920, 1080, 25

# num, début, fin, titre, voix off, provenance de l'image
#   "creee"   → image à générer (build/film_90_images.py)
#   "capture" → capture réelle de l'application
PLANS = [
    ("01", 0, 5.0,  "Le point qui ne sort pas",
     "Elle sait quoi dire. Elle ne le dit pas.", "creee"),
    ("02", 5.0, 12.0, "Le comptoir",
     "Elle est au comptoir. L'employée attend. Elle a préparé sa phrase, "
     "mais elle ne sort pas.", "creee"),
    ("03", 12.0, 17.5, "Trois fois rien",
     "Ça arrive au téléphone. À la pharmacie. Devant un propriétaire.", "creee"),
    ("04", 17.5, 25.5, "Le comptoir se replie",
     "Le soir, chez elle, elle recommence la scène. Sur francis, se tromper "
     "ne coûte rien.", "creee"),
    ("05", 25.5, 31.5, "Elle choisit, et elle parle",
     "Elle choisit une situation. Elle touche le micro. Elle parle.", "capture"),
    ("06", 31.5, 37.0, "Quelqu'un répond",
     "Quelqu'un répond. Et la réponse dépend de ce qu'elle vient de dire.", "capture"),
    ("07", 37.0, 45.5, "Écrit ici",
     "La clinique, le bail, l'autobus, le bureau de poste. Ces situations-là, "
     "on les a écrites ici.", "creee"),
    ("08", 45.5, 51.0, "Ce qu'elle a dit, et comment",
     "À la fin, elle voit ce qu'elle a dit, et ce qui se dit autrement.", "capture"),
    ("09", 51.0, 57.5, "Et elle s'efface",
     "La correction est pour elle seule. Son enseignante ne la lit pas. "
     "Rien n'en reste.", "creee"),
    ("10", 57.5, 61.5, "Quinze pupitres",
     "Ce que son enseignante voit, c'est la classe.", "creee"),
    ("11", 61.5, 68.0, "C'est elle qui décide",
     "Qui avance, qui bloque, qui n'a pas ouvert. La suite, ce n'est pas "
     "la machine.", "capture"),
    ("12", 68.0, 73.0, "Quatre interrupteurs",
     "Un centre n'a pas à nous croire sur parole. Il coche.", "creee"),
    ("13", 73.0, 85.0, "Ce qui ne sort plus",
     "Pas de vrai nom. Pas de courriel. Ce qu'elle écrit s'efface après "
     "trente jours. Et si la direction ne veut pas de l'assistance, plus rien "
     "ne sort du serveur.", "creee"),
    ("14", 85.0, 90.0, "La phrase sort",
     "Et puis un matin, au comptoir, la phrase sort.", "creee"),
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
        azure_voix.parle(texte, ROLE, dest, reference=REFERENCE)
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
