#!/usr/bin/env python3
"""Rogner les fins de fichier sales relevées par `build/fin_de_fichier.py`.

    python3 build/rogner_fins.py --essai      # ne touche à rien, dit ce qui serait fait
    python3 build/rogner_fins.py --appliquer

Le relevé du 29 août 2026 : 131 des 5 962 répliques finissent en plein son au
lieu de s'éteindre — l'onde tombe d'un coup à zéro, et l'oreille entend un clic.
Ce sont des modules produits avant que `rogner_silences()` entre dans
`azure_voix.py` ; il reste 300 à 500 ms de non-parole après la dernière syllabe.

Le geste est le **même** que celui de la chaîne de production actuelle : on
retire du silence de queue en gardant 40 ms de marge. Aucune voix n'est
touchée, aucun ré-échantillonnage — ce n'est pas le post-étirement qui a
échoué deux fois cette semaine.

Prudence : chaque fichier est rogné **sur copie** puis remesuré, et l'original
n'est remplacé que si la fin est effectivement retombée sous le seuil. Les
fichiers dont la syllabe finale manque vraiment sont laissés intacts — le
rognage ne rend pas ce qui n'a pas été synthétisé, il faut les régénérer.
"""
import shutil
import subprocess
import sys
import pathlib
import tempfile

import numpy as np

RACINE = pathlib.Path(__file__).resolve().parent.parent
INTER = RACINE / 'assets' / 'interactive'
SEUIL = -30.0                       # dB sous la crête : au-delà, la fin n'est pas éteinte

sys.path.insert(0, str(RACINE / 'build'))
from azure_voix import rogner_silences, duree                    # noqa: E402
from fin_de_fichier import examine                               # noqa: E402


def fin_dB(f):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(f), '-f', 's16le',
                        '-acodec', 'pcm_s16le', '-ac', '1', '-ar', '24000', '-'],
                       capture_output=True)
    x = np.frombuffer(r.stdout, '<i2').astype(np.float32) / 32768.0
    n, k = 240, len(x) // 240
    if k < 3:
        return 0.0
    db = 20 * np.log10(np.sqrt(np.maximum((x[:k * n].reshape(k, n) ** 2).mean(1), 1e-12)))
    return float(db[-2:].max() - db.max())


def main():
    appliquer = '--appliquer' in sys.argv
    if not appliquer and '--essai' not in sys.argv:
        sys.exit('précisez --essai ou --appliquer')

    fichiers = sorted(INTER.glob('*/*/line_*.mp3'))
    print('%d répliques à examiner…' % len(fichiers))
    sales = [f for f in fichiers if examine(f)]
    print('%d finissent en plein son\n' % len(sales))

    rognes, laisses = [], []
    with tempfile.TemporaryDirectory() as tmp:
        for f in sales:
            copie = pathlib.Path(tmp) / f.name
            shutil.copy(f, copie)
            avant = duree(copie)
            rogner_silences(copie)
            if fin_dB(copie) <= SEUIL:
                rognes.append((f, avant, duree(copie)))
                if appliquer:
                    shutil.copy(copie, f)
            else:
                laisses.append(f)

    for f, a, b in rognes:
        print('  %-58s %.2f → %.2f s' % (f.relative_to(INTER), a, b))
    verbe = 'rognés' if appliquer else 'seraient rognés'
    print('\n✅ %d %s · %d laissés intacts (syllabe finale manquante, à régénérer)'
          % (len(rognes), verbe, len(laisses)))
    if laisses:
        print('\nÀ régénérer :')
        for f in laisses:
            print('  %s' % f.relative_to(INTER))


if __name__ == '__main__':
    main()
