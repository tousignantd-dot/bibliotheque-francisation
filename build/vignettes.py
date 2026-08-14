#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vignettes de première diapositive · pour le dépôt de matériel
=============================================================

    python3 build/vignettes.py                 → tous les modules
    python3 build/vignettes.py module-probleme → un seul

Le dépôt de matériel montre, à côté de chaque présentation, une vignette de
sa première diapositive : c'est ce qui permet de répondre à « est-ce le bon
fichier ? » sans télécharger douze mégaoctets.

Le poste n'a pas LibreOffice. On réutilise donc `build/powerpoints/apercu.py`,
qui relit le `.pptx` produit avec python-pptx et le repeint avec Pillow en
lisant la géométrie réelle des formes. Ce n'est pas une reconstitution : le
rendu part du fichier livré.

Sortie : `assets/vignettes/<slug>/<CODE>.png`, 16:9, largeur `LARGEUR`.
Le fichier n'est refait que si le `.pptx` est plus récent que la vignette —
relancer le script après un build ne recalcule que ce qui a bougé.
"""
import os
import shutil
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, '..'))
sys.path.insert(0, os.path.join(ICI, 'powerpoints'))

SOURCE = os.path.join(RACINE, 'assets', 'powerpoints')
SORTIE = os.path.join(RACINE, 'assets', 'vignettes')

LARGEUR = 640          # assez pour un cadre de 372 px sur écran à deux pixels
QUALITE = 82           # même réglage que les images de vocabulaire


def code_du_fichier(nom):
    """`B3-dire-depuis-quand.pptx` → `B3`. Le code de séance est tout ce qui
    précède le premier tiret ; un fichier sans code garde son nom entier."""
    base = os.path.splitext(nom)[0]
    tete = base.split('-', 1)[0]
    return tete.upper()


def vignette(pptx, dest):
    from PIL import Image
    import apercu

    tmp = tempfile.mkdtemp(prefix='vignette-')
    try:
        faits = apercu.render(pptx, tmp, limite=1)
        if not faits:
            return False
        im = Image.open(faits[0])
        h = round(im.height * LARGEUR / im.width)
        im = im.convert('RGB').resize((LARGEUR, h), Image.LANCZOS)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        im.save(dest, 'PNG', optimize=True)
        return True
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def modules(cibles):
    if not os.path.isdir(SOURCE):
        return []
    tous = sorted(d for d in os.listdir(SOURCE)
                  if os.path.isdir(os.path.join(SOURCE, d)))
    return [m for m in tous if not cibles or m in cibles]


def main(argv):
    cibles = [a for a in argv if not a.startswith('--')]
    force = '--force' in argv
    faits = passes = 0

    for slug in modules(cibles):
        dossier = os.path.join(SOURCE, slug)
        pptxs = sorted(f for f in os.listdir(dossier) if f.endswith('.pptx'))
        if not pptxs:
            continue
        print(f'{slug} · {len(pptxs)} présentation(s)')
        for nom in pptxs:
            src = os.path.join(dossier, nom)
            dest = os.path.join(SORTIE, slug, code_du_fichier(nom) + '.png')
            if (not force and os.path.exists(dest)
                    and os.path.getmtime(dest) >= os.path.getmtime(src)):
                passes += 1
                continue
            if vignette(src, dest):
                ko = os.path.getsize(dest) // 1024
                print(f'  {code_du_fichier(nom):3s}  {ko:3d} Ko  '
                      f'{os.path.relpath(dest, RACINE)}')
                faits += 1

    print(f'\nOK · {faits} vignette(s) produite(s), {passes} déjà à jour.')
    if not faits and not passes:
        print('Aucune présentation trouvée dans assets/powerpoints/<module>/.')


if __name__ == '__main__':
    main(sys.argv[1:])
