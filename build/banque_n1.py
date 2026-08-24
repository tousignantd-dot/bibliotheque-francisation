#!/usr/bin/env python3
"""Renvoi vers `build/banque.py --niveau 1`.

La banque n'est plus celle d'un seul niveau depuis le 24 août 2026 : le
registre, les contrôles et l'état vivent dans `build/banque.py`, qui compte
les huit niveaux. Ce fichier reste parce que son nom est écrit dans
`CLAUDE.md`, dans `docs/plan-exercices-niveau-1.md` et dans les habitudes ;
il ne fait plus rien d'autre que passer la main.
"""
import pathlib
import subprocess
import sys

BANQUE = pathlib.Path(__file__).resolve().parent / 'banque.py'

if __name__ == '__main__':
    args = sys.argv[1:]
    if '--niveau' not in args:
        args += ['--niveau', '1']
    print('(banque_n1.py → banque.py %s)' % ' '.join(args))
    sys.exit(subprocess.run([sys.executable, str(BANQUE)] + args).returncode)
