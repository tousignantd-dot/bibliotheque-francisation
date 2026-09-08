#!/usr/bin/env python3
"""Les images du courriel de présentation, tirées des captures du portail.

Les captures d'origine (`captures-cas`, `captures-telephone`) sont hautes :
posées telles quelles dans un courriel, elles poussent le texte sous la ligne
de flottaison. On en tire ici des versions **cadrées pour le courriel** —
largeur de 560 px pour l'ordinateur, planche de deux téléphones côte à côte —
et on les écrit dans `captures-courriel/`.

    python3 build/captures_courriel.py
"""
from pathlib import Path
from PIL import Image, ImageDraw

ICI = Path(__file__).resolve().parent.parent
SRC = ICI / "assets" / "presentations"
OUT = SRC / "captures-courriel"

LARGE = 560          # une image d'ordinateur dans un courriel de 640 px
FOND = (247, 246, 243)
TRAIT = (214, 210, 202)


def bande(nom, source, haut=0.0, bas=1.0, large=LARGE):
    """Découpe une bande horizontale de la capture, puis met à l'échelle."""
    im = Image.open(SRC / source).convert("RGB")
    y0, y1 = int(im.height * haut), int(im.height * bas)
    im = im.crop((0, y0, im.width, y1))
    im = im.resize((large, max(1, round(im.height * large / im.width))), Image.LANCZOS)
    ecrire(nom, im)
    return im


def planche_telephones(nom, sources, hauteur=520, ecart=22, marge=18):
    """Deux écrans de téléphone sur un même fond : une seule image à charger."""
    ims = []
    for s in sources:
        im = Image.open(SRC / s).convert("RGB")
        ims.append(im.resize((round(im.width * hauteur / im.height), hauteur), Image.LANCZOS))
    l = sum(i.width for i in ims) + ecart * (len(ims) - 1) + marge * 2
    planche = Image.new("RGB", (l, hauteur + marge * 2), FOND)
    d = ImageDraw.Draw(planche)
    x = marge
    for i in ims:
        planche.paste(i, (x, marge))
        d.rectangle([x - 1, marge - 1, x + i.width, marge + hauteur], outline=TRAIT)
        x += i.width + ecart
    ecrire(nom, planche)
    return planche


def ecrire(nom, im):
    OUT.mkdir(parents=True, exist_ok=True)
    f = OUT / nom
    im.save(f, quality=84, optimize=True, progressive=True)
    print(f"{f.relative_to(ICI)}  {im.width}×{im.height}  {f.stat().st_size // 1024} Ko")


def main():
    # Ordinateur — la bande qui porte l'argument, pas l'écran entier.
    bande("ordi-cours.jpg", "captures-cas/07-module-avec-ia.jpg", 0.035, 0.63)
    bande("ordi-classe.jpg", "captures-cas/01-suivi-comptes.jpg", 0.02, 0.52)
    bande("ordi-minilecon.jpg", "captures-cas/14-minilecon.jpg", 0.0, 0.62)
    bande("ordi-seance.jpg", "captures-cas/05-feuille-seance.jpg", 0.0, 0.66)
    # Téléphone — le panneau d'enregistrement, déjà cadré, remis à la taille du courriel.
    bande("tel-oral.jpg", "captures-courriel/production-orale.jpg", large=300)
    # Téléphone — deux écrans par image.
    planche_telephones("tel-cours.jpg", ["captures-telephone/05-dialogue.jpg",
                                         "captures-telephone/16-seance.jpg"])
    planche_telephones("tel-outils.jpg", ["captures-telephone/07-vrai-faux.jpg",
                                          "captures-telephone/14-outils.jpg"])


if __name__ == "__main__":
    main()
