#!/usr/bin/env python3
"""Retirer le cran « très lent » du bouton de débit, partout.

    python3 build/vitesse_deux_crans.py --essai
    python3 build/vitesse_deux_crans.py --appliquer

Décidé le 29 août 2026 : à 0,65, `playbackRate` rend un son franchement mauvais
— l'étirement s'entend plus que le ralentissement n'aide. Le bouton garde deux
crans, normal et lent (0,8), et rien d'autre.

Trois retouches, dans le gabarit **et** dans les modules déjà construits :
le cran lui-même, le garde-fou qui relit le choix stocké — un élève resté sur
« très lent » doit retomber sur « lent », pas planter sur un cran absent — et
l'infobulle qui annonçait trois crans.

Chaque fichier est vérifié pièce par pièce : un fichier qui n'a pas les trois
morceaux est **laissé tel quel et nommé**. C'est la leçon du retrait de greffe
qui avait échoué en silence sur 77 modules.
"""
import glob
import io
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent

RETOUCHES = [
    ("  {v:0.65, lbl:'Débit très lent'},\n", ""),
    ("Math.min(2, Math.max(0, parseInt(localStorage.getItem('saaf-vitesse')",
     "Math.min(1, Math.max(0, parseInt(localStorage.getItem('saaf-vitesse')"),
    ("Trois crans : normal, lent, très lent.", "Deux crans : normal et lent."),
]


def fichiers():
    return (sorted(glob.glob(str(RACINE / 'assets/interactive/*/*-activite-interactive.html')))
            + [str(RACINE / 'build/gabarit/module.html')])


def traite(chemin, appliquer):
    s = io.open(chemin, encoding='utf-8').read()
    nom = pathlib.Path(chemin).parent.name
    presents = [a for a, _ in RETOUCHES if a in s]
    if not presents:
        return nom, 'sans bouton'
    if len(presents) != len(RETOUCHES):
        manquants = [a[:32] for a, _ in RETOUCHES if a not in s]
        return nom, 'INCOMPLET — manque %s' % ' / '.join(manquants)
    for avant, apres in RETOUCHES:
        s = s.replace(avant, apres)
    if appliquer:
        io.open(chemin, 'w', encoding='utf-8').write(s)
    return nom, 'à deux crans'


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('--essai', '--appliquer'):
        sys.exit('usage : vitesse_deux_crans.py --essai|--appliquer')
    appliquer = sys.argv[1] == '--appliquer'
    bilan = {}
    for f in fichiers():
        nom, etat = traite(f, appliquer)
        bilan.setdefault(etat, []).append(nom)
    for etat, noms in sorted(bilan.items()):
        print('%-14s %3d' % (etat[:14], len(noms)))
        if etat.startswith('INCOMPLET'):
            for n in noms:
                print('     !! %s' % n)
    verbe = 'ramenés' if appliquer else 'seraient ramenés'
    print('\n%d fichiers %s à deux crans' % (len(bilan.get('à deux crans', [])), verbe))


if __name__ == '__main__':
    main()
