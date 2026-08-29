#!/usr/bin/env python3
"""Le « glitch » de fin : mesurer comment chaque MP3 de dialogue se termine.

    python3 build/fin_de_fichier.py            # tout le dépôt
    python3 build/fin_de_fichier.py module-n1  # les modules dont le slug commence ainsi

Un fichier propre s'éteint : ses vingt dernières millisecondes sont 60 à 80 dB
sous sa crête. Un fichier coupé s'arrête en plein son — l'onde tombe d'un coup
à zéro, et l'oreille entend un clic. C'est le défaut relevé à l'écoute le
29 août 2026.

Deux formes, qui ne se réparent pas de la même façon :

- `amorce`  — le silence, puis l'attaque d'un son voisé (souvent ~250 Hz : une
  inspiration, ou le début d'un mot de trop) tranchée net. Le son en trop peut
  être retiré sans rien perdre de la réplique.
- `tronque` — la parole va jusqu'au dernier échantillon : la syllabe finale
  manque. Là, il faut refaire le MP3.

Sortie : un JSON sur la sortie standard, une ligne de bilan sur l'erreur
standard. Rien n'est modifié.
"""
import json
import pathlib
import subprocess
import sys

import numpy as np

RACINE = pathlib.Path(__file__).resolve().parent.parent
INTER = RACINE / 'assets' / 'interactive'
SR = 24000
TRAME = 0.010                 # 10 ms
SEUIL_FIN = -30.0             # dB sous la crête : au-delà, la fin n'est pas éteinte
SILENCE = -55.0               # dB sous la crête : en deçà, c'est du silence


def pcm(f):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(f), '-f', 's16le',
                        '-acodec', 'pcm_s16le', '-ac', '1', '-ar', str(SR), '-'],
                       capture_output=True)
    return np.frombuffer(r.stdout, '<i2').astype(np.float32) / 32768.0


def examine(f):
    x = pcm(f)
    n = int(SR * TRAME)
    if len(x) < 20 * n:
        return None
    k = len(x) // n
    db = 20 * np.log10(np.sqrt(np.maximum(
        (x[:k * n].reshape(k, n) ** 2).mean(1), 1e-12)))
    pic = float(db.max())
    fin = float(db[-2:].max()) - pic          # niveau des 20 dernières ms
    if fin <= SEUIL_FIN:
        return None                            # le fichier s'éteint : rien à signaler
    # combien de temps le son court-il sans interruption avant la fin ?
    rel = db - pic
    i = len(rel) - 1
    while i >= 0 and rel[i] > SILENCE:
        i -= 1
    duree_son_ms = int((len(rel) - 1 - i) * TRAME * 1000)
    return {
        'f': str(f.relative_to(INTER)),
        'pic_dB': round(pic, 1),
        'fin_dB_sous_pic': round(fin, 1),
        'son_final_ms': duree_son_ms,
        'forme': 'amorce' if duree_son_ms <= 120 else 'tronque',
    }


def main():
    filtre = sys.argv[1] if len(sys.argv) > 1 else ''
    fichiers = sorted(f for f in INTER.glob('*/*/line_*.mp3')
                      if f.relative_to(INTER).parts[0].startswith(filtre))
    trouves = []
    for i, f in enumerate(fichiers, 1):
        r = examine(f)
        if r:
            trouves.append(r)
        if i % 500 == 0:
            print('  %d / %d…' % (i, len(fichiers)), file=sys.stderr)
    print(json.dumps(trouves, ensure_ascii=False, indent=1))
    amorces = sum(1 for r in trouves if r['forme'] == 'amorce')
    print('\n%d fichiers sur %d finissent en plein son — %d amorces coupées, '
          '%d répliques tronquées'
          % (len(trouves), len(fichiers), amorces, len(trouves) - amorces),
          file=sys.stderr)


if __name__ == '__main__':
    main()
