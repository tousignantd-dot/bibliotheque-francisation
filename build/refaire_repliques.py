#!/usr/bin/env python3
"""Refaire une liste précise de répliques, sans toucher au reste du module.

    python3 build/refaire_repliques.py liste.json --essai
    python3 build/refaire_repliques.py liste.json --lancer

`liste.json` porte des chemins relatifs à `assets/interactive/`, de la forme
`module-n2-guichet/t1/line_01_ecran.mp3`. Le script les regroupe par module et
appelle le générateur du module avec `--only`, qui régénère l'extrait nommé et
lui seul — les soixante autres répliques ne sont ni retirées ni facturées.

Deux raisons de refaire une réplique, et le script ne les distingue pas :
elle sort tronquée (la voix a mal tiré), ou son texte passe désormais par le
lexique de prononciation de `azure_voix.py` et doit être resynthétisé pour en
profiter. Dans les deux cas, le geste est le même.
"""
import collections
import json
import pathlib
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / 'build'))
from fournisseur import protege                                  # noqa: E402


def generateur(slug):
    """Le script qui sait produire l'audio de ce module."""
    f = RACINE / ('generer_audio_%s.py' % slug.replace('module-', 'module_').replace('-', '_'))
    return f if f.exists() else None


def main():
    if len(sys.argv) < 3 or sys.argv[2] not in ('--essai', '--lancer'):
        sys.exit('usage : refaire_repliques.py liste.json --essai|--lancer')
    liste = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
    lancer = sys.argv[2] == '--lancer'

    par_module = collections.defaultdict(list)
    for rel in liste:
        slug, bloc, nom = rel.split('/')
        par_module[slug].append('%s/%s' % (bloc, nom))

    sans = [m for m in par_module if not generateur(m)]
    if sans:
        sys.exit('!! aucun générateur pour : %s' % ', '.join(sans))

    print('%d répliques · %d modules\n' % (len(liste), len(par_module)))
    ok = echec = 0
    for slug in sorted(par_module):
        cibles = sorted(par_module[slug])
        print('── %-26s %2d répliques' % (slug, len(cibles)))
        if not lancer:
            for c in cibles:
                print('     %s' % c)
            continue
        # `--force` est indispensable : les générateurs récents lisent
        # `--only` comme « ne regarde que ceux-là » et sautent quand même les
        # fichiers déjà présents, tandis que les anciens refont d'office. Sans
        # lui, 14 des 95 répliques du 29 août 2026 ont été sautées **en
        # silence**, avec un « ✅ 0 générés · 2 déjà présents » qui ressemblait
        # à un succès. `--only` borne déjà le travail : forcer ne coûte rien.
        r = subprocess.run([sys.executable, str(generateur(slug)),
                            '--force', '--only', ','.join(cibles)],
                           cwd=RACINE, capture_output=True, text=True)
        for l in r.stdout.splitlines():
            if '→' in l or '❌' in l or '✅' in l:
                print('   ', l.strip())
        if r.returncode:
            echec += 1
            print('    !! échec (%s)' % (r.stderr.strip().splitlines() or ['?'])[-1])
        else:
            ok += 1
    if lancer:
        print('\n%d modules traités · %d en échec' % (ok, echec))


if __name__ == '__main__':
    main()
