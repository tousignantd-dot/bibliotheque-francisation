"""
Contrôle automatique des épreuves.

`apercu.py` encadre en magenta pur tout texte qui sort de sa boîte. Ce
script relit les PNG produits et signale ces encadrés : on n'a donc pas à
regarder 270 diapositives une par une pour savoir laquelle est cassée.

Un débordement n'est jamais acceptable — c'est le seul défaut qui rend une
diapo inutilisable en classe. Le build échoue s'il en reste un.
"""
import glob
import os
import sys
from PIL import Image

MAGENTA = (255, 0, 255)


def controler(dossier):
    fautifs = []
    for f in sorted(glob.glob(os.path.join(dossier, '*', '*.png'))
                    or glob.glob(os.path.join(dossier, '*.png'))):
        im = Image.open(f).convert('RGB')
        n = sum(c for c, p in im.getcolors(maxcolors=1 << 24) if p == MAGENTA)
        if n:
            fautifs.append((f, n))
    return fautifs


if __name__ == '__main__':
    base = sys.argv[1] if len(sys.argv) > 1 else '_apercu'
    mauvais = controler(base)
    for f, n in mauvais:
        print(f'DÉBORDEMENT  {f}  ({n} pixels de repère)')
    print(f'{len(mauvais)} diapositive(s) en débordement.')
    sys.exit(1 if mauvais else 0)
