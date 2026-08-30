#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Les diaporamas de présentation — ceux qu'on projette à une direction.

Trois séances de la trousse deviennent des diaporamas, avec le même socle
visuel que les 1 264 diaporamas de cours : ce n'est pas un habillage de plus,
c'est le produit qui se présente lui-même.

    python3 build/powerpoints/pitch.py             # les neuf
    python3 build/powerpoints/pitch.py p2          # un seul
    python3 build/powerpoints/pitch.py --apercu    # + le rendu d'épreuve PNG
    python3 build/powerpoints/pitch.py --vignettes # + la première diapositive

Deux familles : **P**, le pitch, dans l'ordre où on le projette ; **A**, les
annexes, qu'on ouvre quand la salle demande à voir. La trousse les range dans
cet ordre, et c'est le seul endroit où l'on choisit lequel montrer.

Sortie : `assets/presentations/diaporamas/`. Le module actif est un
**pseudo-module** posé ici, jamais dans le registre : `modules.py` recense ce
qui s'enseigne, et une présentation de vente ne s'enseigne pas.
"""
import importlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
sys.path.insert(0, os.path.join(ICI, 'pitch'))

import modules  # noqa: E402

SLUG = 'presentation-francis'
SORTIE = os.path.abspath(os.path.join(ICI, '..', '..', 'assets', 'presentations',
                                      'diaporamas'))
# P = le pitch, dans l'ordre où on le projette.
# A = les annexes, ouvertes quand la salle demande à voir.
PITCH = ['p1', 'p2', 'p3', 'p4']
ANNEXES = ['a1', 'a2', 'a3', 'a4', 'a5']
DECKS = PITCH + ANNEXES


def preparer():
    modules.MODULES[SLUG] = {
        'numero': 0, 'activite': 0, 'niveau': 0,
        'titre': 'francis · présentation',
        'chapeau': 'Les diaporamas de la trousse de présentation.',
        'seances': DECKS, 'blocs': {},
    }
    modules.choisir(SLUG)


VIGNETTES = os.path.join(SORTIE, 'apercus')


def vignettes(codes):
    """La première diapositive de chaque diaporama, en PNG.

    Elles sont **versionnées**, à la différence des épreuves de `_apercu/` :
    la trousse les affiche, et une page en ligne ne peut pas dépendre d'un
    dossier ignoré par git. C'est ce qui permet de voir un diaporama sans le
    télécharger — la plainte qui a motivé tout ceci.
    """
    import apercu
    preparer()
    os.makedirs(VIGNETTES, exist_ok=True)
    faites = []
    for code in codes:
        mod = importlib.import_module(code)
        nom = os.path.basename(mod.build.__module__)
        chemin = _fichier(code)
        if not os.path.exists(chemin):
            continue
        tmp = os.path.join(ICI, '_apercu', '_vignette')
        os.makedirs(tmp, exist_ok=True)
        apercu.render(chemin, tmp, limite=1)
        src = os.path.join(tmp, '01.png')
        dst = os.path.join(VIGNETTES, code.upper() + '.png')
        _reduire(src, dst)
        faites.append(os.path.basename(dst))
    return faites


def _fichier(code):
    """Le .pptx d'un code, retrouvé par son préfixe : les noms portent le
    titre, qui change, alors que le code ne change pas."""
    for f in sorted(os.listdir(SORTIE)):
        if f.upper().startswith(code.upper() + '-') and f.endswith('.pptx'):
            return os.path.join(SORTIE, f)
    return ''


def _reduire(src, dst, largeur=720):
    """Une vignette de 720 px : la page en montre trois de front, et neuf
    aperçus pleine taille pèseraient plus lourd que les diaporamas eux-mêmes."""
    from PIL import Image
    with Image.open(src) as im:
        h = round(im.height * largeur / im.width)
        im.convert('RGB').resize((largeur, h), Image.LANCZOS).save(
            dst, quality=86, optimize=True)


def construire(codes, apercu=False):
    preparer()
    os.makedirs(SORTIE, exist_ok=True)
    for code in codes:
        mod = importlib.import_module(code)
        chemin, n = mod.build(SORTIE)
        print('  %-52s %2d diapositives' % (os.path.basename(chemin), n))
        if apercu:
            import apercu
            dossier = os.path.join(ICI, '_apercu', SLUG, code)
            os.makedirs(dossier, exist_ok=True)
            apercu.render(chemin, dossier)
            print('     épreuves : %s' % os.path.relpath(dossier, ICI))


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    codes = args or DECKS
    construire(codes, apercu='--apercu' in sys.argv)
    if '--vignettes' in sys.argv:
        faites = vignettes(codes)
        print('  vignettes : %d dans %s'
              % (len(faites), os.path.relpath(VIGNETTES, os.getcwd())))
