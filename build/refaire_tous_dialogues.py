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
from fournisseur import protege                                  # noqa: E402
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
    # Les modules encore chez ElevenLabs sont **protégés** : l'utilisateur a
    # retiré son autorisation de les remplacer le 29 août 2026. Les écraser
    # changerait les comédiens, pas seulement la vitesse.
    noms = [m for m, _ in couples]
    permis, bloques = protege(noms)
    couples = [(m, g) for m, g in couples if m in set(permis)]
    for b in bloques:
        print('   protégé (ElevenLabs, non autorisé) : %s' % b)
    n = len(list(INTER.glob('*/*/line_*.mp3')))
    print('%d modules · %d répliques · %d sans générateur' % (len(couples), n, len(sans)))
    for m, _ in sans:
        print('   sauté (aucun générateur) : %s' % m)
    if not lancer:
        return

    depart = time.time()
    ok = echec = 0
    for i, (m, g) in enumerate(couples, 1):
        t = time.time()
        r = subprocess.run([sys.executable, str(g), '--force', '--only', 'line_'],
                           cwd=RACINE, capture_output=True, text=True)
        bilan = [l for l in r.stdout.splitlines() if l.startswith('✅')]
        print('[%2d/%d] %-28s %-42s %4.0f s'
              % (i, len(couples), m, (bilan[-1] if bilan else '(pas de bilan)'),
                 time.time() - t), flush=True)
        if r.returncode:
            echec += 1
            print('        !! %s' % (r.stderr.strip().splitlines() or ['?'])[-1])
        else:
            ok += 1
    print('\n%d modules faits · %d en échec · %.0f min'
          % (ok, echec, (time.time() - depart) / 60))


if __name__ == '__main__':
    main()
