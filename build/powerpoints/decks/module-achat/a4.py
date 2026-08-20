# -*- coding: utf-8 -*-
"""A4 · Dans le magasin.
Bloc A « Je découvre » · couleur teal · 50 min.
Source : exercice `prImg`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-achat/images/')


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre='Dans le magasin',
        chapeau="Huit choses qu'on rencontre en achetant un appareil, de "
                "l'étiquette d'énergie au camion de livraison. Les nommer, "
                "c'est savoir de quoi le vendeur parle.",
        duree='50 minutes')

    d.titre(notes="Séance visuelle et courte. Elle clôt le bloc A.")

    d.objectifs([
        "nommer huit éléments de l'achat d'un appareil ;",
        "lire une étiquette d'énergie ;",
        "distinguer la livraison de l'installation ;",
        "employer l'article juste : un électroménager, la capacité, le bon de livraison.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que cette étiquette vous apprend ?",
        image=IMG + 'etiquette-energie.jpg',
        pistes=[
            "Que représentent les barres colorées ?",
            "Où est-elle collée, sur un appareil neuf ?",
            "Pourquoi les magasins la laissent-ils en place ?",
            "Est-ce qu'un appareil économe coûte plus cher à l'achat ?",
        ],
        notes="La dernière piste ouvre le raisonnement du bloc B : plus cher à l'achat, "
              "moins cher à l'usage. Ne pas conclure ici.")

    d.cartes('Ce qui se lit', "Quatre choses écrites", [
        ("L'étiquette d'énergie",
         "Collée sur la porte. Elle donne la consommation annuelle et situe l'appareil par "
         "rapport aux autres de sa catégorie."),
        ("La fiche technique",
         "Sur la tablette ou en ligne. Dimensions, capacité, bruit, consommation — tout ce "
         "dont on a besoin pour décider."),
        ("Le bon de livraison",
         "Le papier qui dit quoi, quand, et ce qui est inclus. Tout ce qui n'y est pas "
         "écrit n'arrivera pas."),
        ("Le mode d'emploi",
         "Dans la boîte. On le travaillera au bloc D — c'est la partie la moins lue et une "
         "des plus utiles."),
    ], notes="La troisième carte reviendra en C4. Beaucoup de litiges viennent d'une "
             "promesse orale jamais écrite.")

    d.cartes('Ce qui se fait', "Quatre services distincts", [
        ("La livraison",
         "On apporte l'appareil chez vous et on le monte à l'endroit voulu. Souvent 50 à "
         "80 $, parfois gratuite au-dessus d'un montant."),
        ("L'installation",
         "On le branche et on le met en marche. C'est un service à part, qui se paie à "
         "part. La confusion la plus coûteuse du module."),
        ("La reprise",
         "Le magasin repart avec l'ancien appareil. Souvent gratuite, mais seulement si "
         "c'est noté sur le bon."),
        ("Le service après-vente",
         "Le technicien qui vient réparer. Son déplacement coûte environ 90 $, sauf si la "
         "garantie prolongée le couvre."),
    ], notes="Diapo à photographier. Ces quatre services sont quatre lignes distinctes sur "
             "la facture — et quatre sources de malentendu.")

    d.tableau('Analyse', "Livraison ou installation ?",
              ['Ce qui est fait', 'Quel service'],
              [["Descendre l'appareil du camion", "livraison"],
               ["Le monter jusqu'au sous-sol", "livraison"],
               ["Repartir avec l'emballage", "livraison"],
               ["Brancher l'eau et l'électricité", "installation"],
               ["Vérifier que l'appareil est de niveau", "installation"]],
              cle=3,
              note="Les livreurs montent. Ils ne branchent pas.",
              notes="Diapo à photographier. C'est la phrase du dialogue t2, et elle vaut "
                    "quarante dollars.")

    d.piege("Croire que tout est compris",
            "J'ai payé la livraison, donc ils vont l'installer.",
            "La livraison monte l'appareil. L'installation le branche. Deux services, deux prix.",
            "C'est la surprise la plus fréquente du jour de la livraison : l'appareil est "
            "dans la pièce, mais il ne fonctionne pas — et le technicien n'est pas prévu.",
            notes="Faire poser la question au moment de l'achat, pas après. C'est le "
                  "conseil pratique de la séance.")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec le mot du vocabulaire.", [
        ("Les ___ sont au fond du magasin.", "électroménagers"),
        ("La ___ de ce modèle est de cinq kilos.", "capacité"),
        ("Prenez les ___ de votre local.", "dimensions"),
        ("La ___ est d'un an, pièces et main-d'œuvre.", "garantie"),
        ("L'___ est un service à part.", "installation"),
        ("C'est écrit sur le ___ de livraison.", "bon"),
    ], corrige=True,
       notes="Ces six mots sont dans le banc de vocabulaire du module.")

    d.billet(
        "Choisissez un appareil que vous voudriez acheter et relevez sa fiche technique.",
        exemples=[
            "Dimensions, capacité, consommation, bruit, garantie.",
            "En ligne ou en magasin, comme vous préférez.",
        ],
        notes="Bilan du bloc A. Cette fiche servira de base au jeu de rôle de E1.")

    return d.save(dossier)
