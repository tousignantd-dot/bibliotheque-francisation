#!/usr/bin/env python3
"""Les extraits du bloc 3 de la démonstration entreprise (Aliments Belrive).

    python3 build/audio_belrive.py            # ce qui manque seulement
    python3 build/audio_belrive.py --refaire  # tout, de nouveau

Le contraste de débit EST la leçon : Jean-Guy parle au débit normal d'Azure —
c'est-à-dire vite — et Nadia comme Marie-Ève sont ralenties d'un palier. On n'a
donc pas à écrire que le superviseur parle trop vite : on le fait entendre.

Sortie : assets/interactive/entreprise-belrive/
"""
import argparse
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / 'build'))
import azure_voix

SORTIE = RACINE / 'assets' / 'interactive' / 'entreprise-belrive'

# (fichier, rôle, palier, texte)
EXTRAITS = [
    # A — ce qui se passe vraiment
    ('a1.mp3', 'masculin_1', None,
     "Nadia ! La deux est pleine, tu la vides pis tu m'apportes les étiquettes "
     "du lot d'hier avant la pause."),
    ('a2.mp3', 'feminin_2', 'lent', "Oui, oui."),
    ('a3.mp3', 'enseignante', 'lent',
     "Nadia… ce ne sont pas les étiquettes d'hier, ça. Et la palette est encore pleine."),

    # B — la reprise, avec les quatre gestes
    ('b1.mp3', 'masculin_1', None,
     "Nadia ! La deux est pleine, tu la vides pis tu m'apportes les étiquettes "
     "du lot d'hier avant la pause."),
    ('b2.mp3', 'feminin_2', 'lent',
     "Attendez, s'il vous plaît. Vous parlez trop vite pour moi. Répétez lentement ?"),
    ('b3.mp3', 'masculin_1', None, "OK. La palette numéro deux. Tu la vides."),
    ('b4.mp3', 'feminin_2', 'lent', "Je vide la palette deux. Après ?"),
    ('b5.mp3', 'masculin_1', None,
     "Après, tu m'apportes les étiquettes du lot d'hier. Avant la pause."),
    ('b6.mp3', 'feminin_2', 'lent', "Les étiquettes… Montrez-moi, s'il vous plaît."),
    ('b7.mp3', 'masculin_1', None, "Celles-là. Dans la chemise jaune."),
    ('b8.mp3', 'feminin_2', 'lent',
     "Je vide la palette deux, et j'apporte les étiquettes jaunes avant la pause."),
    ('b9.mp3', 'masculin_1', None, "C'est ça. Parfait."),

    # C — dire qu'on n'y arrivera pas
    ('c1.mp3', 'feminin_2', 'lent',
     "Jean-Guy, je n'aurai pas le temps avant la pause. "
     "Je peux vous apporter les étiquettes après ?"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--refaire', action='store_true',
                    help="régénère même les extraits déjà sur le disque")
    a = ap.parse_args()

    SORTIE.mkdir(parents=True, exist_ok=True)
    faits = passes = 0
    for nom, role, palier, texte in EXTRAITS:
        dest = SORTIE / nom
        if dest.exists() and not a.refaire:
            passes += 1
            continue
        d = azure_voix.parle(texte, role, dest, palier=palier)
        faits += 1
        print('  %-8s %-12s %-5s %5.2f s  %s'
              % (nom, role, palier or 'normal', d, texte[:46]))
    print('%d extrait(s) produit(s), %d déjà là → %s'
          % (faits, passes, SORTIE.relative_to(RACINE)))


if __name__ == '__main__':
    main()
