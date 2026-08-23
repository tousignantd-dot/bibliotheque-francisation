# -*- coding: utf-8 -*-
"""Extrait le plus long script en ligne du HTML produit, pour `node --check`.

Le build assemble du JavaScript qu'il ne lit jamais : une apostrophe non
échappée quelque part dans les sept fichiers de contenu produit un HTML de la
bonne taille, sans erreur, dont le script entier meurt sur une SyntaxError.

    python3 build/contenu/module-n8-habitation/_inline.py && node --check /tmp/inline_n8h.js
"""
import re
import pathlib

H = pathlib.Path('assets/interactive/module-n8-habitation/'
                 'module-n8-habitation-activite-interactive.html')
src = max(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>',
                     H.read_text(encoding='utf-8'), re.S), key=len)
pathlib.Path('/tmp/inline_n8h.js').write_text(src, encoding='utf-8')
print(f'{len(src)} octets → /tmp/inline_n8h.js')
