#!/usr/bin/env python3
"""Faire repartir les navigateurs sur l'audio neuf, pas sur celui du cache.

    python3 build/version_audio.py --essai
    python3 build/version_audio.py --poser 12

Les modules vont chercher leurs sons avec un numéro de version collé à l'URL —
`sons/xxx.mp3?v=${AUDIO_V}`. Le nom du fichier ne change jamais quand on le
régénère : sans ce numéro, un navigateur qui l'a déjà en cache continue de
servir l'ancien, et le travail de la journée reste invisible.

**À relancer après toute régénération d'audio.** Le 29 août 2026, environ
1 450 MP3 ont été remplacés — rognage des fins, lexique de prononciation,
débit des niveaux 4 et 5, accent d'insistance — sans que le numéro bouge. Il
faut donc le poser à la main, et c'est le genre d'oubli qui ne se voit pas :
tout est correct sur le disque, et faux dans le navigateur.

Le numéro vit dans le gabarit **et** dans chaque module construit : un module
reconstruit le reprend du gabarit, un module qui ne l'est pas garde le sien.
D'où les valeurs disparates trouvées ce jour-là — 79 modules à 11, trois à 9,
trois à 8, deux à 10. Le script les aligne tous.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
MOTIF = re.compile(r"const AUDIO_V = '(\d+)'")


def fichiers():
    return (sorted(RACINE.glob('assets/interactive/*/*-activite-interactive.html'))
            + [RACINE / 'build' / 'gabarit' / 'module.html'])


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('--essai', '--poser'):
        sys.exit('usage : version_audio.py --essai | --poser <numéro>')
    poser = sys.argv[1] == '--poser'
    neuf = sys.argv[2] if poser else None
    if poser and not (neuf or '').isdigit():
        sys.exit('!! --poser attend un numéro')

    avant, sans, faits = {}, [], 0
    for f in fichiers():
        s = f.read_text(encoding='utf-8')
        m = MOTIF.search(s)
        if not m:
            sans.append(f.parent.name)
            continue
        avant[m.group(1)] = avant.get(m.group(1), 0) + 1
        if poser and m.group(1) != neuf:
            f.write_text(MOTIF.sub("const AUDIO_V = '%s'" % neuf, s, count=1),
                         encoding='utf-8')
            faits += 1
    print('valeurs trouvées : %s'
          % ' · '.join('%s → %d fichiers' % (v, n) for v, n in sorted(avant.items(), key=lambda kv: int(kv[0]))))
    if sans:
        print('sans AUDIO_V (%d) : %s' % (len(sans), ' '.join(sans[:8])))
    if poser:
        print("\n%d fichiers passés à '%s'" % (faits, neuf))
    else:
        print("\n(essai : rien n'a été modifié)")


if __name__ == '__main__':
    main()
