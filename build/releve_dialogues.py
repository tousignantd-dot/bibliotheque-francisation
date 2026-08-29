#!/usr/bin/env python3
"""Le relevé de toutes les répliques enregistrées, pour les réécouter d'affilée.

    python3 build/releve_dialogues.py

Produit `assets/presentations/revision-dialogues.html` : chaque MP3 de dialogue
du dépôt, rangé par niveau → module → défi, avec son texte, sa durée, son débit
mesuré, et quatre boutons de verdict (trop rapide · trop lent · glitch · pauses).
Les verdicts restent dans le navigateur (localStorage) et s'exportent en JSON.

Le texte lu vit à deux endroits selon l'âge du module — voir la note
`sources-du-texte-lu` : `build/contenu/<slug>/dialogues.js` pour les 77 modules
récents, la constante `DIALOGUES` des vieux `generer_audio_*.py` pour le reste.
Un MP3 sans texte retrouvé est tout de même listé : l'oreille passe avant.
"""
import ast
import json
import pathlib
import re
import subprocess
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
INTER = RACINE / 'assets' / 'interactive'
CONTENU = RACINE / 'build' / 'contenu'
SORTIE = RACINE / 'assets' / 'presentations' / 'revision-dialogues.html'

sys.path.insert(0, str(RACINE / 'build' / 'powerpoints'))
from modules import MODULES                                      # noqa: E402


def slug_perso(nom):
    """La règle de charSlug() du HTML — le trait d'union survit."""
    s = unicodedata.normalize('NFD', nom.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace("'", '').replace(' ', '_')


def dialogues_du_contenu(slug):
    """Les blocs de `build/contenu/<slug>/dialogues.js`, lus au motif."""
    f = CONTENU / slug / 'dialogues.js'
    if not f.exists():
        return {}
    src = f.read_text(encoding='utf-8')
    blocs = list(re.finditer(r'^  (\w+): \{', src, re.M))
    out = {}
    for i, m in enumerate(blocs):
        debut, fin = m.end(), (blocs[i + 1].start() if i + 1 < len(blocs) else len(src))
        corps = src[debut:fin]
        label = re.search(r'label:\s*"((?:[^"\\]|\\.)*)"', corps)
        lignes = re.findall(r'\["([^"]+)",\s*"((?:[^"\\]|\\.)*)"\]', corps)
        out[m.group(1)] = {
            'label': (label.group(1).replace('\\"', '"') if label else ''),
            'lines': [(p, t.replace('\\"', '"')) for p, t in lignes],
        }
    return out


def dialogues_hérités():
    """Les `DIALOGUES = {...}` des vieux scripts, clés « module/bloc »."""
    out = {}
    for f in sorted(RACINE.glob('generer_audio_*.py')):
        try:
            arbre = ast.parse(f.read_text(encoding='utf-8'))
        except SyntaxError:
            continue
        for n in arbre.body:
            if not isinstance(n, ast.Assign):
                continue
            if not any(getattr(c, 'id', '') == 'DIALOGUES' for c in n.targets):
                continue
            try:
                v = ast.literal_eval(n.value)
            except ValueError:
                continue
            for cle, bloc in v.items():
                if '/' not in cle or not isinstance(bloc, dict):
                    continue
                mod, sous = cle.split('/', 1)
                out.setdefault(mod, {})[sous] = {
                    'label': bloc.get('title', ''),
                    'lines': [tuple(l) for l in bloc.get('lines', [])],
                }
    return out


def duree(chemin):
    try:
        r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                            'format=duration', '-of', 'csv=p=0', str(chemin)],
                           capture_output=True, text=True, timeout=20)
        return round(float(r.stdout.strip()), 3)
    except (ValueError, OSError, subprocess.SubprocessError):
        return None


def main():
    hérités = dialogues_hérités()
    fiches = []
    for dossier in sorted(p for p in INTER.iterdir() if p.is_dir()):
        mp3s = sorted(dossier.glob('*/line_*.mp3'))
        if not mp3s:
            continue
        slug = dossier.name
        meta = MODULES.get(slug, {})
        blocs = dialogues_du_contenu(slug) or hérités.get(slug, {})
        # index (bloc, rang) → (personnage, texte)
        textes = {}
        for nom_bloc, bloc in blocs.items():
            for rang, (perso, texte) in enumerate(bloc['lines'], 1):
                textes[(nom_bloc, rang)] = (perso, texte)
        for mp3 in mp3s:
            bloc = mp3.parent.name
            m = re.match(r'line_(\d+)_(.+)\.mp3$', mp3.name)
            if not m:
                continue
            rang = int(m.group(1))
            perso, texte = textes.get((bloc, rang), ('', ''))
            if not texte:                       # nommage du personnage divergent
                perso = m.group(2).replace('_', ' ')
            fiches.append({
                'module': slug,
                'titre': meta.get('titre', slug),
                'niveau': meta.get('niveau', 0),
                'numero': meta.get('numero', 0),
                'bloc': bloc,
                'label': (blocs.get(bloc, {}) or {}).get('label', ''),
                'rang': rang,
                'perso': perso,
                'texte': texte,
                'src': '../interactive/%s/%s/%s' % (slug, bloc, mp3.name),
                'chemin': str(mp3),
            })

    with ThreadPoolExecutor(max_workers=12) as pool:
        for f, d in zip(fiches, pool.map(lambda f: duree(f['chemin']), fiches)):
            f['duree'] = d
            f['cps'] = round(len(f['texte']) / d, 1) if (d and f['texte']) else None
            del f['chemin']

    fiches.sort(key=lambda f: (f['niveau'] or 99, f['numero'] or 99,
                               f['module'], f['bloc'], f['rang']))
    page(fiches)
    manquants = sum(1 for f in fiches if not f['texte'])
    print('✅ %d répliques · %d modules · %d sans texte retrouvé\n   %s'
          % (len(fiches), len({f['module'] for f in fiches}), manquants, SORTIE))


def page(fiches):
    gabarit = pathlib.Path(__file__).with_name('revision_dialogues.html')
    SORTIE.write_text(
        gabarit.read_text(encoding='utf-8').replace(
            '/*%%DONNEES%%*/[]', json.dumps(fiches, ensure_ascii=False)),
        encoding='utf-8')


if __name__ == '__main__':
    main()
