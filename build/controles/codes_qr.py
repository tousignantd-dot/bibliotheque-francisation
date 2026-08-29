#!/usr/bin/env python3
"""Contrôle de l'encodeur de codes QR.

Un code QR faux ne se voit pas : il ressemble à un code QR. Le contrôle ne
regarde donc pas le carré, il le **fait relire** — par deux chemins
indépendants, et sur ce que chacun peut réellement prouver :

  1. **La matrice, à masque égal, contre `segno`.** Pour les dix versions et
     les huit masques, module par module. C'est la preuve de l'encodage :
     découpage en blocs, correction d'erreurs, entrelacement, parcours en
     zigzag, bits de format et de version. Rien de tout ça n'est vérifiable à
     l'œil, et tout se trompe en silence.

     Le *choix* du masque, lui, n'est pas comparé : les huit sont valides, la
     pénalité n'est qu'une heuristique de lisibilité, et deux implémentations
     conformes en choisissent parfois deux différents.

  2. **Le carré rendu, décodé par OpenCV**, comme le ferait un téléphone —
     à taille réduite et sur une image dégradée, parce que cette feuille sera
     photocopiée avant d'arriver dans les mains d'un élève.

Les deux bibliothèques ne servent qu'ici. Le serveur n'importe que `qr.py`,
en bibliothèque standard — c'est la règle du dépôt.

    python3 -m pip install segno opencv-python-headless numpy

Le fichier ne s'appelle **pas** `qr.py` : il masquerait le module de la racine
pour tout script lancé depuis ce dossier — le contrôle des organisations est
tombé dessus, avec un « circular import » qui ne disait rien de la cause.
"""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RACINE))
import qr                                                     # noqa: E402

ECHECS = []


def verifie(nom, condition, detail=""):
    if condition:
        print("  ok   %s" % nom)
    else:
        print("  RATÉ %s %s" % (nom, detail))
        ECHECS.append(nom)


def avec_masque(texte, masque):
    """La matrice de ce texte sous un masque imposé."""
    version = qr._version_pour(len(texte.encode()))
    codets = qr._codets_finaux(texte, version)
    base, reserve = qr._motifs_fixes(version)
    m = [ligne[:] for ligne in base]
    qr._poser_donnees(m, reserve, codets)
    for y in range(len(m)):
        for x in range(len(m)):
            if not reserve[y][x] and qr._MASQUES[masque](y, x):
                m[y][x] ^= 1
    qr._poser_format(m, masque)
    qr._poser_version(m, version)
    return m


ADRESSES = [
    "https://francis.quebec/s/KRB482",
    "http://127.0.0.1:5199/s/CJ363C",
    "https://bibliotheque-francisation-production.up.railway.app/s/KRB482",
    "https://francis.quebec/s/A",
    "É",                                    # UTF-8 sur deux octets
]

print("\n— La matrice, contre segno, à masque égal —")
try:
    import segno
except ImportError:
    segno = None
    print("  segno absent : `python3 -m pip install segno` pour ce contrôle")
    ECHECS.append("segno absent")

if segno:
    for version in range(1, 11):
        # Un texte qui remplit la version **exactement** : aucun octet de
        # remplissage ne vient masquer une erreur dans les derniers blocs.
        capacite = qr.TABLE_Q[version][0] - (2 if version <= 9 else 3)
        tete = "v%d-" % version
        texte = tete + "A" * (capacite - len(tete))
        assert len(texte.encode()) == capacite
        assert qr._version_pour(len(texte.encode())) == version
        ecarts = 0
        for masque in range(8):
            ref = segno.make_qr(texte, error="Q", mode="byte",
                                boost_error=False, mask=masque)
            attendue = [[int(v) for v in ligne] for ligne in ref.matrix]
            obtenue = avec_masque(texte, masque)
            if len(attendue) != len(obtenue):
                ecarts += 10_000
                continue
            ecarts += sum(1 for y in range(len(attendue))
                          for x in range(len(attendue))
                          if attendue[y][x] != obtenue[y][x])
        verifie("version %2d, les 8 masques (%d octets)" % (version, capacite),
                ecarts == 0, "%d module(s) différent(s)" % ecarts)

print("\n— Le carré, relu par un décodeur —")
try:
    import numpy as np
    import cv2
except ImportError:
    cv2 = None
    print("  OpenCV absent : `python3 -m pip install opencv-python-headless "
          "numpy` pour ce contrôle")
    ECHECS.append("opencv absent")


def image(matrice, echelle, marge=4):
    n = len(matrice) + 2 * marge
    img = np.full((n * echelle, n * echelle), 255, dtype=np.uint8)
    for y, ligne in enumerate(matrice):
        for x, v in enumerate(ligne):
            if v:
                y0, x0 = (y + marge) * echelle, (x + marge) * echelle
                img[y0:y0 + echelle, x0:x0 + echelle] = 0
    return img


if cv2:
    lecteur = cv2.QRCodeDetector()
    for texte in ADRESSES:
        lu, _, _ = lecteur.detectAndDecode(image(qr.matrice(texte), 8))
        verifie("relu : %s" % texte[:38], lu == texte, "lu %r" % lu[:40])

    print("\n— Et une fois photocopié —")
    # Ce que subit vraiment la feuille : une réduction, un flou, un contraste
    # qui bave, du grain. Si le carré ne survit pas à ça, il ne sert à rien —
    # et c'est précisément ce que le niveau de correction Q achète.
    for texte in ADRESSES[:3]:
        brut = image(qr.matrice(texte), 4)
        floue = cv2.GaussianBlur(brut, (3, 3), 0)
        bruit = np.random.default_rng(7).normal(0, 18, floue.shape)
        sale = np.clip(floue.astype(float) + bruit, 0, 255).astype(np.uint8)
        # Le gris d'une photocopie fatiguée : le noir n'est plus noir.
        sale = np.clip(sale.astype(float) * 0.8 + 30, 0, 255).astype(np.uint8)
        lu, _, _ = lecteur.detectAndDecode(sale)
        verifie("dégradé, relu : %s" % texte[:32], lu == texte, "lu %r" % lu[:40])

print("\n— Le SVG —")
rendu = qr.svg("https://francis.quebec/s/KRB482")
verifie("c'est un SVG", rendu.startswith("<svg") and rendu.endswith("</svg>"))
verifie("il porte un fond blanc", 'fill="#FFFFFF"' in rendu)
verifie("il garde la marge de quatre modules",
        'viewBox="0 0 37 37"' in rendu, rendu[:200])
verifie("il s'annonce aux lecteurs d'écran", 'role="img"' in rendu)
verifie("aucune requête vers l'extérieur",
        "http" not in rendu.replace('xmlns="http://www.w3.org/2000/svg"', ""))

print("\n— Le SVG rend bien la matrice —")
# Le chemin SVG est relu et retransformé en matrice. Sans ça, une erreur dans
# le tracé des rectangles donnerait un carré faux à partir d'une matrice
# juste — et rien, plus haut, ne le verrait.
import re                                                     # noqa: E402


def matrice_du_svg(rendu, marge=4):
    boite = re.search(r'viewBox="0 0 (\d+) (\d+)"', rendu)
    total = int(boite.group(1))
    n = total - 2 * marge
    m = [[0] * n for _ in range(n)]
    chemin = re.search(r'<path fill="[^"]*" d="([^"]*)"', rendu).group(1)
    for x, y, largeur in re.findall(r"M(\d+) (\d+)h(\d+)v1h-\d+z", chemin):
        for i in range(int(largeur)):
            m[int(y) - marge][int(x) - marge + i] = 1
    return m


for texte in ADRESSES:
    verifie("aller-retour SVG : %s" % texte[:34],
            matrice_du_svg(qr.svg(texte)) == qr.matrice(texte))

print("\n— Les bornes —")
try:
    qr.matrice("x" * 200)
    verifie("un texte trop long est refusé", False, "accepté")
except ValueError:
    verifie("un texte trop long est refusé", True)

print()
if ECHECS:
    print("%d contrôle(s) en échec : %s" % (len(ECHECS), ", ".join(ECHECS)))
    sys.exit(1)
print("Tous les contrôles passent.")
