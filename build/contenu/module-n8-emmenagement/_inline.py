# Extrait le plus long <script> en ligne du HTML produit, pour `node --check`.
# Voir CLAUDE.md : « Le build assemble du JavaScript qu'il ne lit jamais. »
#     python3 build/contenu/module-n8-emmenagement/_inline.py
#     node --check /tmp/inline_n8_emmenagement.js
import re
import pathlib

HTML = pathlib.Path('assets/interactive/module-n8-emmenagement/'
                    'module-n8-emmenagement-activite-interactive.html')
SORTIE = pathlib.Path('/tmp/inline_n8_emmenagement.js')

h = HTML.read_text(encoding='utf-8')
scripts = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', h, re.S)
SORTIE.write_text(max(scripts, key=len), encoding='utf-8')
print(SORTIE, len(SORTIE.read_text(encoding='utf-8')), 'octets')
