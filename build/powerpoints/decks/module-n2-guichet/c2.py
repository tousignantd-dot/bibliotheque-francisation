# -*- coding: utf-8 -*-
"""C2 · Quarante-cinq dollars, en lettres.
Bloc C « Défi 2 · Je fais un chèque » · couleur ambre · 75 min.
Source : dialogue `t2b`, exercices `t2lettres`, `t2b`,
mini-leçon `t2lettres`.

Seconde séance du Défi 2, et la plus technique du module : écrire un nombre
en lettres, avec son trait d'union et son long trait jusqu'au bout de la
ligne. C'est la ligne que le comptoir regarde en premier, et celle qui fait
refuser un chèque.

La séance reprend les nombres de la séance A2 — treize et trente s'écrivent
maintenant, après s'être seulement entendus.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-guichet/images/')


def _photo(nom):
    """La photo si elle est sur le disque, sinon rien. Voir `a1.py`."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Quarante-cinq dollars, en lettres",
        chapeau="Écrire un montant en lettres sur la longue ligne du chèque, "
                "avec le trait d'union et le trait de fin qui protègent.",
        duree='75 minutes')

    d.titre(notes="Rendre les chèques commencés en C1 au début de la séance : le travail "
                  "d'aujourd'hui les termine. Séance d'écriture, donc beaucoup de temps "
                  "au crayon et peu de diapositives.")

    d.objectifs([
        "écrire un montant en lettres ;",
        "mettre le trait d'union au bon endroit ;",
        "tirer un trait jusqu'au bout de la ligne ;",
        "vérifier un chèque avant de le donner.",
    ])

    d.dialogue('Dialogue · 1 de 3', "Il manque une chose", [
        ("MONIQUE", "Attendez. Il manque une chose sur votre chèque.", True),
        ("AMADOU", "Ah bon ? J'ai écrit la date et le nom.", True),
        ("MONIQUE", "Oui, mais le montant en lettres n'est pas là.", True),
        ("AMADOU", "Quarante-cinq… ça s'écrit comment ?", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Demander au groupe de "
             "répondre à la dernière question avant d'écouter la suite.")

    d.dialogue('Dialogue · 2 de 3', "Avec un trait entre les deux mots", [
        ("MONIQUE", "Quarante-cinq dollars. Avec un trait entre les deux mots.", True),
        ("AMADOU", "D'accord. Et après le mot, je fais un trait ?", True),
        ("MONIQUE", "Oui, un trait jusqu'au bout de la ligne.", True),
        ("AMADOU", "Pourquoi ?", True),
    ], notes="Deux traits différents dans la même réplique : le petit, entre les deux "
             "mots, et le long, au bout de la ligne. Les dessiner tous les deux au "
             "tableau, l'un sous l'autre.")

    d.dialogue('Dialogue · 3 de 3', "Pour que personne n'ajoute rien", [
        ("MONIQUE", "Pour que personne n'ajoute un mot après.", True),
        ("AMADOU", "Ah ! Je comprends. Voilà, c'est fini.", True),
    ], notes="Montrer concrètement : écrire « quarante-cinq dollars » au tableau, laisser "
             "la ligne vide après, et ajouter « et cinquante » devant le groupe. Le "
             "silence qui suit vaut toutes les explications.")

    d.regle("Un trait entre les deux morceaux du nombre",
            "45 devient quarante-cinq. 72 devient soixante-douze.",
            precision="Le mot « dollars » vient après, écrit en lettres lui aussi — "
                      "jamais le signe de dollar sur cette ligne. Et s'il y a des cents : "
                      "quarante-cinq dollars et cinquante cents.",
            notes="Diapositive à photographier. Faire écrire trois montants au tableau "
                  "par trois élèves, et laisser le groupe placer le trait.")

    d.tableau('Analyse', "Les nombres qu'on écrit le plus",
              ["En chiffres", "En lettres, sur le chèque"],
              [["13 $", "treize dollars"],
               ["30 $", "trente dollars"],
               ["45 $", "quarante-cinq dollars"],
               ["60 $", "soixante dollars"],
               ["80 $", "quatre-vingts dollars"]],
              cle=1,
              note="Après soixante : soixante-dix, quatre-vingts, quatre-vingt-dix.",
              notes="Diapositive à photographier. Elle reprend les deux familles de "
                    "nombres de la séance A2 : ce qui s'entendait s'écrit maintenant.")

    d.piege("Le trait oublié",
            "quarante cinq dollars",
            "quarante-cinq dollars, puis un trait",
            "Deux fautes coûtent un chèque refusé : le trait d'union oublié entre les "
            "deux morceaux du nombre, et la ligne laissée vide après le mot « dollars ». "
            "Le long trait n'est pas une décoration : il empêche d'ajouter un mot.",
            notes="Faire chercher au groupe ce qu'on pourrait ajouter sur une ligne "
                  "laissée vide. Les réponses viennent vite, et elles sont justes.")

    d.pratique('Écriture', "Le montant en lettres",
               "Écrivez chaque montant comme sur la longue ligne du chèque.", [
        ("45 $ : ___ dollars", "quarante-cinq"),
        ("13 $ : ___ dollars", "treize"),
        ("30 $ : ___ dollars", "trente"),
        ("60 $ : ___ dollars", "soixante"),
        ("80 $ : ___ dollars", "quatre-vingts"),
        ("Après le dernier mot, je fais un ___ jusqu'au bout.", "trait"),
    ], corrige=True, cols=2,
       notes="Les six mêmes phrases sont dans le module en ligne, exercice `t2lettres`, "
             "avec sa mini-leçon.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Il manque le montant en lettres.", "vrai"),
        ("« Quarante-cinq » s'écrit avec un trait entre les deux mots.", "vrai"),
        ("Après le mot, on laisse la ligne vide.", "faux — on tire un trait"),
        ("Le trait empêche d'ajouter un mot après.", "vrai"),
        ("Amadou repart sans finir son chèque.", "faux — il le termine"),
    ], corrige=True, cols=1,
       notes="Les cinq mêmes énoncés sont dans le module en ligne, exercice `t2b`.")

    d.pratique('Pratique · seul puis à deux', "Terminez votre chèque",
               "Reprenez le chèque de la séance C1 et finissez-le.", [
        ("Étape 1", "Sur la longue ligne : quarante-cinq dollars, avec le trait d'union."),
        ("Étape 2", "Après le mot, tirez un trait jusqu'au bout de la ligne."),
        ("Étape 3", "En bas à droite : votre signature, en dernier."),
        ("Étape 4", "Échangez avec votre voisin et vérifiez les six lignes de la C1."),
    ], cols=1,
       notes="Vingt-cinq minutes. La vérification à deux vaut plus que la correction de "
             "l'enseignante : c'est en cherchant l'erreur d'un autre qu'on retient la "
             "liste des six lignes.")

    d.vocabulaire('Vocabulaire', "Les cinq mots du chèque et du paiement", [
        ("un chèque", "Le papier signé qui paie à la place de l'argent."),
        ("un montant", "Le nombre de dollars qu'on paie ou qu'on retire."),
        ("une signature", "Ton nom écrit de ta main, en bas du papier."),
        ("le paiement direct", "Payer avec sa carte, sur la petite machine du magasin."),
        ("le comptant", "Payer avec des billets et des pièces, pas avec une carte."),
    ], notes="Diapositive à photographier. Faire dire chaque mot avec son article. "
             "Demander pour chacun : « Où est-ce que vous avez déjà vu ça ? »")

    d.billet(
        "Écrivez trois montants en lettres, avec le mot dollars.",
        exemples=[
            "quinze dollars",
            "quarante-cinq dollars",
            "quatre-vingts dollars",
        ],
        notes="Devoir court. Une seule chose est regardée : le trait d'union. Le reste "
              "s'installera tout seul.")

    return d.save(dossier)
