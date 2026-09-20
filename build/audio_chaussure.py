#!/usr/bin/env python3
"""Les extraits du bloc A de la démonstration détail (Chaussures Rivard).

    python3 build/audio_chaussure.py            # ce qui manque seulement
    python3 build/audio_chaussure.py --refaire  # tout, de nouveau

LE CONTRASTE DE DÉBIT EST LA LEÇON, et c'est la distribution éprouvée de
Belrive, reprise telle quelle : le CLIENT parle au débit normal d'Azure —
c'est-à-dire vite — et la vendeuse comme la gérante sont ralenties d'un palier.
On n'a donc pas à écrire que le client parle trop vite : on le fait entendre.

LE CASTING SE COMPTE AVANT D'ÉCRIRE. Il n'y a que quatre voix, deux féminines
et deux masculines, et deux personnages du même genre ne peuvent pas se
répondre dans un même extrait. Dans un magasin la tentation est exactement là
— la vendeuse, la cliente, la gérante. D'où un client MASCULIN : il libère les
deux voix féminines pour Yasmine et Chantal, qui, elles, se répondent.

Sortie : assets/interactive/entreprise-chaussure/
"""
import argparse
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / 'build'))
import azure_voix

SORTIE = RACINE / 'assets' / 'interactive' / 'entreprise-chaussure'

# (fichier, rôle, palier, texte)
EXTRAITS = [
    # A — l'accueil raté. Rien ne casse, et c'est ça le problème.
    ('a1.mp3', 'masculin_1', None,
     "Bonjour ! Écoutez, le soulier brun là, dans la vitrine, "
     "vous l'auriez-tu en trente-huit pis en large ?"),
    ('a2.mp3', 'feminin_2', 'lent', "Oui… bonjour !"),
    ('a3.mp3', 'enseignante', 'lent',
     "Yasmine ? Le monsieur est reparti. Il est allé voir en face."),

    # B — la reprise : arrêter, faire préciser, redire.
    ('b1.mp3', 'masculin_1', None,
     "Bonjour ! Écoutez, le soulier brun là, dans la vitrine, "
     "vous l'auriez-tu en trente-huit pis en large ?"),
    ('b2.mp3', 'feminin_2', 'lent',
     "Un instant, s'il vous plaît. Vous cherchez quel modèle ?"),
    ('b3.mp3', 'masculin_1', None, "Le brun, là. Dans la vitrine."),
    ('b4.mp3', 'feminin_2', 'lent', "Le brun. Et quelle pointure ?"),
    ('b5.mp3', 'masculin_1', None, "Trente-huit. En large, si vous l'avez."),
    ('b6.mp3', 'feminin_2', 'lent',
     "Trente-huit, en large. Je vais voir en réserve. Je reviens tout de suite."),
    ('b7.mp3', 'masculin_1', None, "Parfait, merci."),

    # C — passer le relais. Ce n'est pas un échec.
    ('c1.mp3', 'masculin_1', None,
     "Pis là, je voudrais savoir si je peux l'échanger si jamais ça fait pas, "
     "parce que c'est pour un cadeau, faque il faudrait que ça soit possible."),
    ('c2.mp3', 'feminin_2', 'lent',
     "Un instant, s'il vous plaît. Je vais chercher ma collègue."),
    ('c3.mp3', 'enseignante', 'lent',
     "Bonjour ! Oui, vous pouvez l'échanger. Vous avez trente jours, avec la facture."),

    # D — « je regarde ».
    ('d1.mp3', 'masculin_1', None, "Non, non, je regarde."),
    ('d2.mp3', 'feminin_2', 'lent', "Parfait. Je suis là si vous avez besoin."),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--refaire', action='store_true',
                    help="régénère même les extraits déjà sur le disque")
    ap.add_argument('--compter', action='store_true',
                    help="compte les extraits et les caractères, sans rien produire")
    a = ap.parse_args()

    if a.compter:
        n = sum(len(t) for _, _, _, t in EXTRAITS)
        print('%d extrait(s), %d caractères' % (len(EXTRAITS), n))
        return

    SORTIE.mkdir(parents=True, exist_ok=True)
    faits = passes = 0
    for nom, role, palier, texte in EXTRAITS:
        dest = SORTIE / nom
        if dest.exists() and not a.refaire:
            passes += 1
            continue
        d = azure_voix.parle(texte, role, dest, palier=palier)
        faits += 1
        print('  %-8s %-12s %-6s %5.2f s  %s'
              % (nom, role, palier or 'normal', d, texte[:44]))
    print('%d extrait(s) produit(s), %d déjà là → %s'
          % (faits, passes, SORTIE.relative_to(RACINE)))


if __name__ == '__main__':
    main()
