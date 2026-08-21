# -*- coding: utf-8 -*-
"""A4 · Trois dollars soixante-quinze.
Bloc A « Je découvre » · couleur ambre · 75 min. Dire et écrire un prix.
Source : exercice `prPrix` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre='Trois dollars soixante-quinze',
        chapeau="Un prix se dit en deux morceaux et s'écrit avec une virgule. "
                "Tout le module en dépend : les prix se donnent à l'oral, "
                "une seule fois.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle ferme la découverte et ouvre le "
                  "défi 1, qui est une séance d'écoute de prix. Commencer en écrivant "
                  "3,75 $ au tableau et en demandant à trois élèves de le lire à voix "
                  "haute. Les trois lectures seront différentes.")

    d.objectifs([
        "lire un prix à voix haute : les dollars, puis les cents ;",
        "reconnaître la forme courte employée au comptoir ;",
        "écrire un prix avec une virgule et le signe de dollar après le nombre ;",
        "demander le prix de quatre façons.",
    ])

    d.regle("Un prix a deux parties",
            "« 3,75 $ » se dit trois dollars soixante-quinze",
            precision="D'abord les dollars, ensuite les cents. On ne dit pas "
                      "« cents » à la fin : on s'arrête au nombre. Au comptoir, "
                      "on entend surtout la forme courte, « trois "
                      "soixante-quinze », où le mot « dollars » saute. Ce n'est "
                      "pas du mauvais français : c'est du français parlé normal.",
            notes="Diapositive à photographier. Faire dire les deux formes par tout le "
                  "groupe. La forme courte est celle qu'ils entendront réellement, donc "
                  "celle qu'il faut savoir reconnaître.")

    d.tableau('Analyse', "La virgule, pas le point",
              ["On écrit", "On n'écrit pas"],
              [["3,75 $", "3.75 $"],
               ["110 $", "$110"],
               ["33,25 $", "33.25$"]],
              cle=0,
              note="La virgule sépare les dollars des cents, et le signe se met après.",
              notes="Diapositive à photographier. Beaucoup d'élèves viennent de pays où "
                    "le point sépare les décimales et où le signe se met devant. Ce "
                    "n'est pas une faute d'orthographe : c'est une convention "
                    "différente, à réapprendre.")

    d.tableau('Analyse', "Les trois dizaines qui piègent",
              ["Le nombre", "Comment il se construit"],
              [["70 · soixante-dix", "soixante, plus dix"],
               ["75 · soixante-quinze", "soixante, plus quinze"],
               ["80 · quatre-vingts", "quatre fois vingt"],
               ["90 · quatre-vingt-dix", "quatre fois vingt, plus dix"]],
              cle=0,
              note="« Soixante-quinze » revient dans presque tous les prix du transport.",
              notes="Diapositive à photographier. Ne pas s'excuser du système de "
                    "numération : l'expliquer comme une construction, ce qu'il est. "
                    "Faire compter de 60 à 100 en chœur, deux fois.")

    d.tableau('Analyse', "Les quatre façons de demander le prix",
              ["La question", "Quand on l'emploie"],
              [["C'est combien ?", "la plus courte, entre gens pressés"],
               ["Ça coûte combien ?", "la plus fréquente"],
               ["Combien coûte le mensuel ?", "quand on nomme le titre"],
               ["Combien est-ce que je vous dois ?", "au moment de payer"]],
              cle=0,
              note="Les quatre sont polies. La dernière sert à confirmer un prix déjà dit.",
              notes="Diapositive à photographier. Faire choisir à chacun celle qu'il "
                    "adoptera : une seule, apprise par cœur, vaut mieux que quatre "
                    "hésitantes.")

    d.pratique('Écriture', "Écrivez le prix en chiffres",
               "Écoutez, puis écrivez avec une virgule et le signe de dollar.", [
        ("Trois dollars soixante-quinze", "3,75 $"),
        ("Trente-cinq dollars", "35,00 $"),
        ("Trente-trois vingt-cinq", "33,25 $"),
        ("Cent dix dollars", "110,00 $"),
        ("Six dollars soixante-quinze", "6,75 $"),
        ("Dix-sept dollars", "17,00 $"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 4 du module. Dicter les prix soi-même, à voix normale, "
             "sans ralentir : c'est ainsi qu'ils seront dits au comptoir. Ne répéter "
             "que si un élève le demande — et le féliciter de l'avoir demandé.")

    d.pratique('Répétition', "Six prix de la grille",
               "Écoutez, puis répétez chaque prix deux fois.", [
        ("Trois dollars soixante-quinze.", "un passage"),
        ("Deux dollars soixante-quinze.", "un passage à tarif réduit"),
        ("Trente-cinq dollars.", "dix passages"),
        ("Trente-trois dollars vingt-cinq.", "l'hebdo"),
        ("Cent dix dollars.", "le mensuel"),
        ("Soixante-six dollars.", "le mensuel à tarif réduit"),
    ], corrige=True,
       notes="Ce sont les vrais prix de la zone A. Les élèves les reverront au bloc D, "
             "dans la grille. Ne pas encore expliquer les titres : on travaille les "
             "nombres, pas les tarifs.")

    d.piege('Prononciation',
            "« trois dollars soixante-quinze cents »",
            "« trois dollars soixante-quinze »",
            "On ne dit pas « cents » à la fin d'un prix en français. On s'arrête "
            "au nombre. Ajouter « cents » est immédiatement reconnaissable comme "
            "une traduction de l'anglais.",
            notes="Piège très fréquent chez les élèves qui ont appris l'anglais avant "
                  "le français. Le corriger une fois clairement, puis passer à autre "
                  "chose.")

    d.billet(
        "Écrivez en chiffres les trois prix que vous avez entendus aujourd'hui.",
        exemples=[
            "Un passage coûte ___ .",
            "Un mensuel coûte ___ .",
        ],
        notes="Devoir court. Vérifier la virgule et la position du signe de dollar : "
              "c'est là que se voit ce qui reste de la séance.")

    return d.save(dossier)
