#!/usr/bin/env python3
"""Le « glitch » de fin : mesurer comment chaque MP3 de dialogue se termine.

    python3 build/fin_de_fichier.py            # les dialogues des modules
    python3 build/fin_de_fichier.py module-n1  # ceux dont le slug commence ainsi
    python3 build/fin_de_fichier.py --dans assets/presentations/medias/formation-dea
    python3 build/fin_de_fichier.py --dans <dossier> --epreuve   # + le contrôle du contrôle

LE RELEVÉ NE VALAIT QUE POUR `assets/interactive/*/*/line_*.mp3` (20 septembre
2026). Tout ce qui est synthétisé ailleurs — une formation, un simulateur, une
capsule — n'a jamais pu être mesuré : il n'y avait pas d'argument pour le dire.
Dix-sept fichiers de la formation DEA ont donc été servis pendant quatre jours
en finissant entre −12 et −30 dB sous leur crête, c'est-à-dire en plein son.
C'est l'utilisateur qui les a entendus.

`--epreuve` REND LE CONTRÔLE VÉRIFIABLE. Il coupe trois fichiers sains juste
après leur trame la plus forte et exige que la mesure les signale. Une mesure
qui rend « zéro défaut » sans avoir prouvé qu'elle réagit ne dit rien, et un
premier passage a failli conclure « rien à signaler » sur un témoin tronqué au
milieu — la coupe était tombée dans un silence.

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
        'f': str(f.relative_to(INTER)) if INTER in f.parents else f.name,
        'pic_dB': round(pic, 1),
        'fin_dB_sous_pic': round(fin, 1),
        'son_final_ms': duree_son_ms,
        'forme': 'amorce' if duree_son_ms <= 120 else 'tronque',
    }


def epreuve(fichiers):
    """La mesure réagit-elle ? On coupe trois fichiers sains en plein son.

    Sans ça, « 0 fichier en défaut » peut vouloir dire « la mesure ne mesure
    rien ». On coupe juste après la trame la PLUS FORTE, jamais à une fraction
    de la durée : une coupe au milieu tombe souvent dans un silence, et le
    fichier tronqué s'éteint alors proprement.
    """
    import tempfile
    temoins = fichiers[:3]
    if not temoins:
        return
    with tempfile.TemporaryDirectory() as d:
        for f in temoins:
            x = pcm(f)
            n = int(SR * TRAME)
            k = len(x) // n
            db = 20 * np.log10(np.sqrt(np.maximum(
                (x[:k * n].reshape(k, n) ** 2).mean(1), 1e-12)))
            # LA COUPE DOIT LAISSER UN FICHIER MESURABLE. `examine` rend None
            # sous 20 trames ; couper à la crête d'un clip dont l'attaque est
            # forte rendait un témoin de 15 trames, et l'épreuve accusait la
            # mesure d'un défaut qui était le sien. On ne retient donc que les
            # crêtes situées au-delà de la 25e trame.
            garde = db.copy()
            garde[:25] = -999
            if garde.max() == -999:
                continue
            c = pathlib.Path(d) / 'temoin.wav'
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(f), '-t',
                            '%.3f' % ((int(garde.argmax()) + 1) * TRAME), str(c)],
                           check=True)
            if examine(c) is None:
                raise SystemExit('  ÉPREUVE ÉCHOUÉE sur %s : un fichier coupé '
                                 'en plein son n\'est pas signalé. Le relevé '
                                 'qui suivrait ne voudrait rien dire.' % f.name)
        print('  épreuve : %d témoins coupés net, %d signalés'
              % (len(temoins), len(temoins)), file=sys.stderr)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if '--dans' in sys.argv:
        dossier = pathlib.Path(sys.argv[sys.argv.index('--dans') + 1]).resolve()
        fichiers = sorted(dossier.rglob('*.mp3'))
        globals()['INTER'] = dossier.parent
    else:
        filtre = args[0] if args else ''
        fichiers = sorted(f for f in INTER.glob('*/*/line_*.mp3')
                          if f.relative_to(INTER).parts[0].startswith(filtre))
    if '--epreuve' in sys.argv:
        epreuve(fichiers)
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
