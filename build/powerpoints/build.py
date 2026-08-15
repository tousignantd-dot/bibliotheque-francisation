#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génération des présentations d'enseignement
============================================

    python3 build.py module-probleme            → les séances du module
    python3 build.py module-probleme a1 b2      → n'en reconstruit que deux
    python3 build.py module-probleme --apercu a1 → construit et rend les épreuves PNG
    python3 build.py --tous                     → tous les modules du registre

Le premier argument est le **slug** du module, celui de
`assets/interactive/<slug>/`. Les présentations sortent dans
`assets/powerpoints/<slug>/` : `A1-….pptx` n'est unique qu'à l'intérieur d'un
module, et à plat le `A1` du module 8 écraserait celui du module 9.

Chaque séance vit dans `decks/<slug>/<code>.py` et expose `build(dossier)`.
Le socle visuel est dans `theme.py` — n'y touchez pas pour changer un
contenu, et ne touchez pas à un contenu pour changer le visuel.

Dépendances : python-pptx et Pillow. Le poste n'a ni Node ni LibreOffice ;
`apercu.py` remplace le rendu LibreOffice en relisant le .pptx produit.
"""
import importlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import modules  # noqa: E402

RACINE_SORTIE = os.path.abspath(os.path.join(ICI, '..', '..', 'assets', 'powerpoints'))


def dossier_decks(slug):
    return os.path.join(ICI, 'decks', slug)


def charger(slug, code):
    """Importe `decks/<slug>/<code>.py`.

    Le chemin des decks est mis en tête de `sys.path` juste avant l'import et
    les modules déjà chargés sous ce nom sont oubliés : sans cela, produire
    deux modules dans le même processus servirait le `a1` du premier au
    second."""
    chemin = dossier_decks(slug)
    if chemin not in sys.path:
        sys.path.insert(0, chemin)
    sys.modules.pop(code, None)
    mod = importlib.import_module(code)
    if os.path.dirname(os.path.abspath(mod.__file__)) != chemin:
        raise SystemExit(f'{slug}/{code} : deck introuvable ({mod.__file__}).')
    return mod


def produire(slug, cibles=None, apercu=False):
    m = modules.choisir(slug)
    cibles = [c.lower() for c in (cibles or m['seances'])]
    sortie = os.path.join(RACINE_SORTIE, slug)
    os.makedirs(sortie, exist_ok=True)

    print(f"Module {m['numero']} · {m['titre']}  ({slug})")
    total = 0
    for code in cibles:
        mod = charger(slug, code)
        chemin, n = mod.build(sortie)
        total += n
        print(f'  {code.upper():3s}  {n:2d} diapos  {os.path.basename(chemin)}')
        if apercu:
            import apercu as ap
            dest = os.path.join(ICI, '_apercu', slug, code)
            ap.render(chemin, dest)
            print(f'       épreuves → {dest}')
    print(f'  → {len(cibles)} présentation(s) · {total} diapositives · {sortie}\n')
    return total


def main(argv):
    apercu = '--apercu' in argv
    tous = '--tous' in argv
    argv = [a for a in argv if not a.startswith('--')]

    if tous:
        cibles_mod = modules.ORDRE
        codes = None
    else:
        if not argv:
            raise SystemExit(
                'Usage : python3 build.py <module> [codes…] [--apercu]\n'
                '        python3 build.py --tous\n'
                'Modules : ' + ', '.join(modules.ORDRE))
        cibles_mod, codes = [argv[0]], (argv[1:] or None)

    total = 0
    for slug in cibles_mod:
        if not os.path.isdir(dossier_decks(slug)):
            print(f'{slug} · pas encore de decks — ignoré\n')
            continue
        total += produire(slug, codes, apercu)
    print(f'OK · {total} diapositives au total')

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
