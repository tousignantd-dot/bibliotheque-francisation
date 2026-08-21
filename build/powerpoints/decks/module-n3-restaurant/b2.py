# -*- coding: utf-8 -*-
"""B2 · Où regarder sur le tableau.
Bloc B « Défi 1 · Lire le menu » · couleur teal · 75 min.
Source : exercices `t1colonnes` et `t1tableau`, mini-leçon `t1colonnes`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre='Où regarder sur le tableau',
        chapeau="Cinq endroits, et le panneau entier devient lisible : le "
                "titre du bloc, le nom du plat, ce qui vient après le nom, le "
                "prix à droite, et les petites lignes du bas.",
        duree='75 minutes')

    d.titre(notes="Séance de stratégie de lecture. Projeter le tableau du menu du module "
                  "interactif (exercice 5 du défi 1) pendant toute la séance : les élèves "
                  "y cherchent chaque information au fur et à mesure.")

    d.objectifs([
        "trouver une information précise sur un tableau de menu ;",
        "distinguer un prix unique de trois prix de formats ;",
        "lire les petites lignes du bas de l'affiche ;",
        "poser une question quand le tableau ne dit pas tout.",
    ])

    d.tableau('Analyse', "Où est quoi ?",
              ['Tu cherches', 'Regarde'],
              [["ce qu'il y a dans le plat", "après le nom : au poulet, aux légumes"],
               ["le prix", "au bout de la ligne, à droite"],
               ["les formats", "trois prix côte à côte sur la même ligne"],
               ["ce qui vient avec", "sous le titre du bloc, en petit"]],
              cle=1,
              note="Les conditions, elles, sont tout en bas de l'affiche.",
              notes="Diapo à photographier. C'est la diapositive la plus utile du bloc : "
                    "elle tient toute la stratégie de lecture en quatre lignes.")

    d.regle("Trois prix ne font pas trois plats",
            "Soupe aux légumes   3,25  4,25  5,25",
            precision="C'est la même soupe. Ce qui change, c'est la portion — "
                      "la quantité dans le bol. Les prix sont toujours dans le "
                      "même ordre : du plus petit au plus grand, de gauche à "
                      "droite.",
            notes="Diapo à photographier. Les montants sont un exemple de classe : ce "
                  "qui compte est l'ordre des trois, pas les chiffres.")

    d.tableau('Analyse', "Le tableau de chez Marcel",
              ['Bloc', 'Ce qui y est écrit'],
              [["Sandwichs", "au poulet, aux œufs, au jambon — servis avec salade ou frites"],
               ["Soupes", "aux légumes, au poulet et nouilles — petit, moyen, grand"],
               ["Breuvages", "jus de pomme, jus d'orange, lait, café, eau"],
               ["Trios", "sandwich, accompagnement et breuvage — un seul prix"]],
              cle=1,
              note="Le bloc « Extras » ajoute le fromage, le bacon, une seconde portion.",
              notes="Diapo à photographier. C'est le menu de référence du module : il "
                    "revient dans le jeu de rôle et dans la production écrite.")

    d.tableau('Analyse', "Les petites lignes du bas",
              ['Ce qui est écrit', 'Ce que ça veut dire'],
              [["Taxes en sus", "le montant de la caisse sera un peu plus haut"],
               ["Comptant et débit seulement", "la carte de crédit n'est pas acceptée"],
               ["Le dessin d'une feuille", "le plat est sans viande"]],
              cle=1,
              note="Trois lignes de rien du tout, et ce sont elles qui décident.",
              notes="Diapo à photographier. Faire raconter une fois où quelqu'un est "
                    "arrivé à la caisse sans le bon moyen de paiement.")

    d.pratique('Compréhension écrite', "Vrai ou faux ?",
               "Répondez d'après le tableau de chez Marcel.", [
        ("Il y a trois sortes de sandwichs.", "vrai"),
        ("La salade et les frites sont des accompagnements.", "vrai"),
        ("La soupe existe en trois formats.", "vrai"),
        ("On peut payer avec une carte de crédit.", "faux — comptant et débit"),
        ("Le fromage est compris dans le prix du sandwich.", "faux — c'est un extra"),
    ], corrige=True,
       notes="Exercice central de la séance. Faire montrer du doigt, sur le tableau "
             "projeté, la ligne qui justifie chaque réponse.")

    d.cartes("Quand le tableau ne dit pas tout", "Quatre questions", [
        ("Qu'est-ce qu'il y a dans ce sandwich ?",
         "Quand le nom ne suffit pas, ou quand un mot est inconnu. C'est la question la "
         "plus fréquente au comptoir."),
        ("Ça vient avec quoi ?",
         "Quand la ligne « servi avec » n'est pas visible de là où on est. Le préposé "
         "répond en deux mots."),
        ("Quelle est la soupe du jour ?",
         "Elle change tous les jours et elle est souvent écrite à la craie, en petit, "
         "sur un tableau à part."),
        ("Est-ce que je peux payer avec ma carte ?",
         "Si la ligne du bas n'est pas lisible. Mieux vaut demander avant de commander "
         "que de chercher un guichet après."),
    ], notes="Faire poser chaque question à voix haute, par un élève différent, avec "
             "« s'il vous plaît » à la fin.")

    d.piege("Additionner les prix du trio",
            "6,50 + 2,00 + 1,75",
            "le trio a son propre prix, plus bas",
            "Le trio n'est pas la somme des trois lignes : c'est justement pour ça "
            "qu'il existe. Son prix est écrit dans son propre bloc, à droite. Comparer "
            "les deux chiffres est la seule façon de savoir ce qui est avantageux.",
            notes="Faire faire la comparaison au tableau avec des montants inventés. "
                  "L'écart se voit en trois secondes.")

    d.billet(
        "Trouvez un menu et écrivez cinq informations.",
        exemples=[
            "Un plat, son prix, ce qui vient avec, un format, une ligne du bas.",
            "Une photo de menu sur un téléphone suffit.",
        ],
        notes="Devoir. C'est le premier travail de compréhension écrite autonome du "
              "module ; il sera repris au début de B3.")

    return d.save(dossier)
