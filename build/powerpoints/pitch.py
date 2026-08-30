#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Les diaporamas de présentation — ceux qu'on projette à une direction.

Trois séances de la trousse deviennent des diaporamas, avec le même socle
visuel que les 1 264 diaporamas de cours : ce n'est pas un habillage de plus,
c'est le produit qui se présente lui-même.

    python3 build/powerpoints/pitch.py            # les trois
    python3 build/powerpoints/pitch.py p2         # un seul
    python3 build/powerpoints/pitch.py --apercu   # + le rendu d'épreuve PNG

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
DECKS = ['p1', 'p2', 'p3', 'p4']


def preparer():
    modules.MODULES[SLUG] = {
        'numero': 0, 'activite': 0, 'niveau': 0,
        'titre': 'francis · présentation',
        'chapeau': 'Les diaporamas de la trousse de présentation.',
        'seances': DECKS, 'blocs': {},
    }
    modules.choisir(SLUG)


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
    construire(args or DECKS, apercu='--apercu' in sys.argv)
