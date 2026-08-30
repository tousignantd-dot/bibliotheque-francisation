# -*- coding: utf-8 -*-
"""Les chiffres des diaporamas de présentation, comptés sur le dépôt.

Écrire « 1 264 fiches » en dur dans une diapositive, c'est signer un chiffre
qui vieillira sans prévenir — et le dire faux devant une direction coûte plus
cher que de ne pas le dire.
"""
import collections
import json
import pathlib
import re
import zipfile

RACINE = pathlib.Path(__file__).resolve().parents[3]


def _mesurer():
    c = {}
    acts = json.loads((RACINE / 'data' / 'activities.json').read_text())
    cat = collections.Counter(a.get('categorie') for a in acts)
    c['cours'] = cat.get('cours', 0)
    c['ateliers'] = cat.get('atelier', 0)
    c['niveaux'] = sorted({a.get('level') for a in acts if a.get('level')})

    niv = {}
    for a in acts:
        i = a.get('interactive') or ''
        if i.startswith('assets/interactive/'):
            niv[i.split('/')[2]] = a.get('level')

    docs = list((RACINE / 'assets' / 'documents').glob('*.html'))
    c['fiches'] = len([p for p in docs if re.search(r'-[a-e][1-5]-', p.name)])

    decks = list((RACINE / 'assets' / 'powerpoints').rglob('*.pptx'))
    c['decks'] = len(decks)
    c['par_niveau'] = collections.Counter(niv.get(d.parent.name, '?') for d in decks)
    c['modules_par_niveau'] = collections.Counter(
        niv.get(d.name, '?') for d in (RACINE / 'assets' / 'powerpoints').iterdir()
        if d.is_dir())
    diapos = 0
    for d in decks:
        try:
            with zipfile.ZipFile(d) as z:
                diapos += len([n for n in z.namelist()
                               if re.match(r'ppt/slides/slide\d+\.xml$', n)])
        except Exception:
            pass
    c['diapos'] = diapos

    minutes = notes = 0
    for p in (RACINE / 'build' / 'powerpoints' / 'decks').rglob('*.py'):
        t = p.read_text(errors='ignore')
        m = re.search(r"duree='(\d+)", t)
        if m:
            minutes += int(m.group(1))
        notes += len(re.findall(r'notes=', t))
    c['heures'] = round(minutes / 60)
    c['notes'] = notes
    c['mp3'] = len(list((RACINE / 'assets' / 'interactive').rglob('*.mp3')))
    c['images'] = sum(len(list((RACINE / 'assets' / 'interactive').rglob(e)))
                      for e in ('*.jpg', '*.png', '*.webp'))
    return c


CH = _mesurer()


def n(v):
    """Espace **insécable**, pas fine : Verdana n'a pas U+2009, et le thème
    refuse le fichier plutôt que d'afficher des carrés vides."""
    return '{:,}'.format(v).replace(',', ' ')
