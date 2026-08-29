#!/usr/bin/env python3
"""Régénérer toutes les répliques du cours à l'échelle de débit par niveau.

    python3 build/refaire_tous_dialogues.py --essai
    python3 build/refaire_tous_dialogues.py --lancer
    python3 build/refaire_tous_dialogues.py --lancer --niveau 4

Chaque générateur est appelé avec `--force --only line_` : le préfixe `line_`
ne désigne que les répliques de dialogue, jamais les sons du banc de
vocabulaire — la règle de `azure_voix.famille()`. Les `sons/` gardent donc leur
taux et, pour les modules encore chez ElevenLabs, leur timbre : c'est une
question distincte, laissée ouverte.

`--force` est indispensable : sans lui, les générateurs récents lisent `--only`
comme « ne regarde que ceux-là » et sautent les fichiers déjà présents, en
affichant un « ✅ 0 générés » qui ressemble à un succès.

Trois ateliers n'ont pas de générateur — je-demenage, parler-de-sa-sante,
visite-vieux-montreal. Ils sont listés et sautés, pas oubliés en silence.
"""
import pathlib
import subprocess
import sys
import time

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / 'build'))
from fournisseur import repliques_du_module                      # noqa: E402
INTER = RACINE / 'assets' / 'interactive'


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('--essai', '--lancer'):
        sys.exit('usage : refaire_tous_dialogues.py --essai|--lancer')
    lancer = sys.argv[1] == '--lancer'

    modules = sorted({f.parts[-3] for f in INTER.glob('*/*/line_*.mp3')})
    if '--niveau' in sys.argv:
        vise = int(sys.argv[sys.argv.index('--niveau') + 1])
        sys.path.insert(0, str(RACINE / 'build' / 'powerpoints'))
        from modules import MODULES
        modules = [m for m in modules if MODULES.get(m, {}).get('niveau') == vise]
        print('— niveau %d seulement —' % vise)
    couples = []
    sans = []
    for m in modules:
        g = RACINE / ('generer_audio_%s.py' % m.replace('module-', 'module_').replace('-', '_'))
        (couples if g.exists() else sans).append((m, g))
    # La protection se décide **fichier par fichier** : les modules sont
    # mixtes, et protéger le module entier bloquait des répliques déjà passées
    # à Azure — celles de Kim dans module-n5-degat, par exemple — qui sont
    # réglables sans remplacer un seul enregistrement d'origine.
    travail, protegees = [], 0
    for m, g in couples:
        ok, bl = repliques_du_module(m)
        protegees += len(bl)
        if ok:
            travail.append((m, g, ok, len(bl)))
    couples = travail
    n = sum(len(ok) for _, _, ok, _ in couples)
    print('%d modules · %d répliques régénérables · %d protégées (ElevenLabs) '
          '· %d modules sans générateur'
          % (len(couples), n, protegees, len(sans)))
    for m, _ in sans:
        print('   sauté (aucun générateur) : %s' % m)
    if not lancer:
        for m, _, ok, bl in couples[:6]:
            print('   %-26s %3d à refaire · %3d protégées' % (m, len(ok), bl))
        return

    depart = time.time()
    ok = echec = 0
    for i, (m, g, cibles, bloquees) in enumerate(couples, 1):
        t = time.time()
        r = subprocess.run([sys.executable, str(g), '--force',
                            '--only', ','.join(cibles)],
                           cwd=RACINE, capture_output=True, text=True)
        bilan = [l for l in r.stdout.splitlines() if l.startswith('✅')]
        garde = (' · %d protégées' % bloquees) if bloquees else ''
        print('[%2d/%d] %-26s %-40s %4.0f s%s'
              % (i, len(couples), m, (bilan[-1] if bilan else '(pas de bilan)'),
                 time.time() - t, garde), flush=True)
        if r.returncode:
            echec += 1
            print('        !! %s' % (r.stderr.strip().splitlines() or ['?'])[-1])
        else:
            ok += 1
    print('\n%d modules faits · %d en échec · %.0f min'
          % (ok, echec, (time.time() - depart) / 60))


if __name__ == '__main__':
    main()
