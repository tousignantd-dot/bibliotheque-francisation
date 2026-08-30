#!/usr/bin/env python3
"""Le débit d'articulation, par niveau, par module et par voix.

    python3 build/debit_par_voix.py

Un caractère par seconde calculé sur la durée brute du MP3 ne veut rien dire :
le silence de bord pèse lourd sur « Merci. » et presque rien sur une phrase
longue, si bien que la même articulation rend 4 c/s d'un côté et 14 de l'autre.
On mesure donc la **durée parlée** — les trames au-dessus de crête − 35 dB,
silences internes et de bord retirés — et c'est elle qui divise le nombre de
caractères. C'est la leçon du 25 août sur les voix ralenties, qu'un c/s brut
avait fait conclure n'importe quoi.

Le relevé croise trois axes, parce que la plainte peut venir de chacun :
le **niveau** (« tout le niveau 4 est trop rapide »), le **personnage**
(« Kim monte à vingt »), et la **voix Azure** qui le porte — c'est elle, au
bout du compte, qu'on peut ralentir.
"""
import collections
import json
import pathlib
import re
import subprocess
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor

import numpy as np

RACINE = pathlib.Path(__file__).resolve().parent.parent
INTER = RACINE / 'assets' / 'interactive'
SR, TRAME = 24000, 0.010
SOUS_CRETE = 35.0            # dB : en deçà, on considère que ça ne parle pas

sys.path.insert(0, str(RACINE / 'build' / 'powerpoints'))
from modules import MODULES                                      # noqa: E402


def slug(nom):
    s = unicodedata.normalize('NFD', nom.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace("'", '').replace(' ', '_')


def duree_parlee(f):
    """Les secondes où ça parle vraiment, silences retirés."""
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(f), '-f', 's16le',
                        '-acodec', 'pcm_s16le', '-ac', '1', '-ar', str(SR), '-'],
                       capture_output=True)
    x = np.frombuffer(r.stdout, '<i2').astype(np.float32) / 32768.0
    n = int(SR * TRAME)
    k = len(x) // n
    if k < 3:
        return 0.0
    db = 20 * np.log10(np.sqrt(np.maximum((x[:k * n].reshape(k, n) ** 2).mean(1), 1e-12)))
    return float((db > db.max() - SOUS_CRETE).sum() * TRAME)


def voix_des_persos(module):
    """Le personnage → rôle de voix, lu dans le générateur du module."""
    g = RACINE / 'audio' / ('generer_audio_%s.py' % module.replace('module-', 'module_').replace('-', '_'))
    if not g.exists():
        return {}
    m = re.search(r'VOIX_PERSO\s*=\s*\{(.*?)\n\}', g.read_text(encoding='utf-8'), re.S)
    if not m:
        return {}
    return dict(re.findall(r'"([^"]+)":\s*"([^"]+)"', m.group(1)))


def repliques():
    for d in sorted((RACINE / 'build' / 'contenu').glob('*/dialogues.js')):
        module = d.parent.name
        roles = voix_des_persos(module)
        src = d.read_text(encoding='utf-8')
        blocs = list(re.finditer(r'^  (\w+): \{', src, re.M))
        for i, b in enumerate(blocs):
            fin = blocs[i + 1].start() if i + 1 < len(blocs) else len(src)
            lignes = re.findall(r'\["([^"]+)",\s*"((?:[^"\\]|\\.)*)"\]', src[b.end():fin])
            for rang, (perso, texte) in enumerate(lignes, 1):
                f = INTER / module / b.group(1) / ('line_%02d_%s.mp3' % (rang, slug(perso)))
                if f.exists():
                    yield {'module': module, 'perso': perso,
                           'role': roles.get(perso, '?'),
                           'niveau': MODULES.get(module, {}).get('niveau', 0),
                           'titre': MODULES.get(module, {}).get('titre', module),
                           'texte': texte.replace('\\"', '"'), 'f': f}


def main():
    fiches = list(repliques())
    print('%d répliques…' % len(fiches), file=sys.stderr)
    with ThreadPoolExecutor(max_workers=12) as pool:
        for fi, d in zip(fiches, pool.map(lambda x: duree_parlee(x['f']), fiches)):
            fi['parle'] = round(d, 3)
            fi['cps'] = round(len(fi['texte']) / d, 1) if d > 0.2 else None
            fi['f'] = str(fi['f'].relative_to(INTER))
    bons = [f for f in fiches if f['cps']]

    def table(cle, titre, mini=15):
        groupes = collections.defaultdict(list)
        for f in bons:
            groupes[f[cle]].append(f['cps'])
        print('\n%s' % titre)
        print('  %-30s %6s %6s %6s %6s' % ('', 'n', 'méd.', 'p90', 'max'))
        for g, v in sorted(groupes.items(),
                           key=lambda kv: -float(np.median(kv[1]))):
            if len(v) < mini:
                continue
            print('  %-30s %6d %6.1f %6.1f %6.1f'
                  % (g, len(v), np.median(v), np.percentile(v, 90), max(v)))

    table('niveau', 'PAR NIVEAU (c/s d\'articulation)')
    table('role', 'PAR VOIX AZURE')
    print('\nLES 20 PERSONNAGES LES PLUS RAPIDES (médiane, ≥ 15 répliques)')
    par = collections.defaultdict(list)
    for f in bons:
        par[(f['perso'], f['module'], f['role'], f['niveau'])].append(f['cps'])
    lignes = [(k, v) for k, v in par.items() if len(v) >= 15]
    lignes.sort(key=lambda kv: -float(np.median(kv[1])))
    print('  %-14s %-24s %-12s %3s %5s %6s %6s' % ('perso', 'module', 'voix', 'niv', 'n', 'méd.', 'max'))
    for (p, m, r, niv), v in lignes[:20]:
        print('  %-14s %-24s %-12s %3s %5d %6.1f %6.1f'
              % (p[:14], m.replace('module-', '')[:24], r[:12], niv, len(v),
                 np.median(v), max(v)))
    json.dump(fiches, open(RACINE / 'build' / '.debits.json', 'w'), ensure_ascii=False)
    print('\n(détail dans build/.debits.json)')


if __name__ == '__main__':
    main()
