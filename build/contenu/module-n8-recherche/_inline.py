"""Extrait le plus long <script> en ligne du module produit, pour node --check.

Le contrôle que `CLAUDE.md` réclame après chaque `build/module.py` : le build
assemble du JavaScript qu'il ne lit jamais, et une apostrophe non échappée
produit un HTML de la bonne taille dont le script entier meurt.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parents[3]
SLUG = 'module-n8-recherche'
html = (RACINE / f'assets/interactive/{SLUG}/{SLUG}-activite-interactive.html').read_text(encoding='utf-8')
bloc = max(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', html, re.S), key=len)
sortie = pathlib.Path(sys.argv[1])
sortie.write_text(bloc, encoding='utf-8')
print(f'{len(bloc)} octets → {sortie}')
