#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nunito, en local, pour ce qui doit fonctionner sans réseau.

    python3 build/police_nunito.py            # état des fichiers
    python3 build/police_nunito.py --recuperer # les télécharge

Tout le dépôt tire Nunito de Google Fonts par un `@import`, et c'est très bien
pour le portail : il est en ligne de toute façon. **Un diaporama projeté, non.**
On le donne dans une école dont le réseau invité tombe, ou depuis un portable
débranché — et il s'affiche alors dans une police de repli, avec des chasses
différentes, donc des retours à la ligne différents, donc des écrans qui
débordent. Le seul cas où l'on ne peut rien réparer sur place.

**Deux fichiers suffisent.** Google sert Nunito en police **variable** : un seul
`.woff2` par sous-ensemble couvre 400 à 900. Il faut le droit et l'italique, et
seulement le sous-ensemble `latin` — sa plage porte U+0152-0153 (Œ œ) et
U+0131, le « i » sans point du logotype francis. Le latin-ext, le cyrillique et
le vietnamien ne servent à rien ici et tripleraient le poids.

Les fichiers sont **versionnés** dans `assets/design-system/fonts/` : un
diaporama produit sur un poste sans réseau doit pouvoir l'être. C'est
`build/powerpoints/pitch/web.py` qui les incorpore ensuite en base64, pour que
chaque diaporama soit un fichier autonome — un `<link>` relatif casserait dès
qu'on déplace le fichier ou qu'on l'envoie par courriel.
"""

import argparse
import pathlib
import re
import urllib.request

RACINE = pathlib.Path(__file__).resolve().parent.parent
DOSSIER = RACINE / 'assets' / 'design-system' / 'fonts'

# L'API `css2` ne rend des `.woff2` qu'à un navigateur récent : sans cet
# en-tête, elle sert du TTF, quatre fois plus lourd.
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120.0 Safari/537.36')
FEUILLE = ('https://fonts.googleapis.com/css2?family=Nunito:ital,wght@'
           '0,400;0,700;0,800;0,900;1,400&display=swap')

FICHIERS = {'normal': 'nunito-latin.woff2', 'italic': 'nunito-latin-italique.woff2'}


def _lire(url, entetes=None):
    req = urllib.request.Request(url, headers=entetes or {'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def sources():
    """{style: (url, plage unicode)} pour le seul sous-ensemble latin."""
    css = _lire(FEUILLE).decode('utf-8')
    out = {}
    morceaux = re.split(r'/\* ([a-z-]+) \*/', css)
    for i in range(1, len(morceaux), 2):
        if morceaux[i] != 'latin':
            continue
        b = morceaux[i + 1]
        style = re.search(r'font-style:\s*(\w+)', b).group(1)
        out.setdefault(style, (re.search(r'url\((https://[^)]+)\)', b).group(1),
                               re.search(r'unicode-range:\s*([^;]+);', b).group(1).strip()))
    manquants = set(FICHIERS) - set(out)
    if manquants:
        raise SystemExit('!! Google Fonts ne rend plus le style : %s\n'
                         '   La feuille a changé de forme ; relire son contenu.'
                         % ', '.join(sorted(manquants)))
    return out


def etat():
    for style, nom in sorted(FICHIERS.items()):
        p = DOSSIER / nom
        print('  %-32s %s' % (nom, ('%d Ko' % (p.stat().st_size // 1024))
                              if p.exists() else 'ABSENT'))
    return all((DOSSIER / n).exists() for n in FICHIERS.values())


def recuperer():
    DOSSIER.mkdir(parents=True, exist_ok=True)
    src = sources()
    for style, nom in sorted(FICHIERS.items()):
        url, plage = src[style]
        octets = _lire(url, {'User-Agent': UA})
        (DOSSIER / nom).write_bytes(octets)
        print('  %-32s %d Ko' % (nom, len(octets) // 1024))
    # La plage est identique pour les deux styles ; on la garde à côté des
    # fichiers plutôt que de la réécrire dans web.py, où elle vieillirait sans
    # que personne ne le voie.
    (DOSSIER / 'nunito-latin.plage.txt').write_text(
        src['normal'][1] + '\n', encoding='utf-8')
    print('  %-32s %s…' % ('nunito-latin.plage.txt', src['normal'][1][:44]))


def plage():
    """La plage unicode du sous-ensemble latin, telle que Google la déclare."""
    p = DOSSIER / 'nunito-latin.plage.txt'
    return p.read_text(encoding='utf-8').strip() if p.exists() else ''


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--recuperer', action='store_true')
    a = ap.parse_args()
    if a.recuperer:
        recuperer()
    else:
        raise SystemExit(0 if etat() else 1)
