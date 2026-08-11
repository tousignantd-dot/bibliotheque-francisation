#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génération des présentations d'enseignement du module 9
========================================================

    python3 build.py            → construit les 16 séances
    python3 build.py a1 b2      → n'en reconstruit que deux
    python3 build.py --apercu a1 → construit et rend les épreuves PNG

Chaque séance vit dans `decks/<code>.py` et expose `build(dossier)`.
Le socle visuel est dans `theme.py` — n'y touchez pas pour changer un
contenu, et ne touchez pas à un contenu pour changer le visuel.

Dépendances : python-pptx et Pillow. Le poste n'a ni Node ni LibreOffice ;
`apercu.py` remplace le rendu LibreOffice en relisant le .pptx produit.
"""
import importlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [ICI, os.path.join(ICI, 'decks')]

SORTIE = os.path.abspath(os.path.join(
    ICI, '..', '..', 'assets', 'powerpoints'))

# L'ordre d'enseignement. Les blocs suivent les sections du module.
SEANCES = [
    # Bloc A · Je me prépare
    'a1', 'a2', 'a3', 'a4',
    # Bloc B · Tâche 1 — parler à sa propriétaire
    'b1', 'b2', 'b3', 'b4',
    # Bloc C · Tâche 2 — les parties communes
    'c1', 'c2', 'c3', 'c4',
    # Bloc D · Tâche 3 — se plaindre
    'd1', 'd2',
    # Bloc E · Application et bilan
    'e1', 'e2',
]


def main(argv):
    apercu = '--apercu' in argv
    argv = [a for a in argv if not a.startswith('--')]
    cibles = [a.lower() for a in argv] or SEANCES

    os.makedirs(SORTIE, exist_ok=True)
    total_diapos = 0
    for code in cibles:
        mod = importlib.import_module(code)
        chemin, n = mod.build(SORTIE)
        total_diapos += n
        print(f'  {code.upper():3s}  {n:2d} diapos  {os.path.basename(chemin)}')
        if apercu:
            import apercu as ap
            dest = os.path.join(ICI, '_apercu', code)
            ap.render(chemin, dest)
            print(f'       épreuves → {dest}')
    print(f'\nOK · {len(cibles)} présentation(s) · {total_diapos} diapositives')
    print(f'Sortie : {SORTIE}')

    if apercu:
        import controle
        mauvais = controle.controler(os.path.join(ICI, '_apercu'))
        for f, n in mauvais:
            print(f'DÉBORDEMENT  {f}')
        if mauvais:
            print(f'\n{len(mauvais)} diapositive(s) en débordement — à corriger.')
            sys.exit(1)
        print('Contrôle des débordements : aucun.')


if __name__ == '__main__':
    main(sys.argv[1:])
