# -*- coding: utf-8 -*-
"""C4 · Ce qui est servi avec.
Bloc C · couleur acier · 50 min.
Source : exercice `t2accomp`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-restaurant/images/')


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre='Ce qui est servi avec',
        chapeau="Le plat arrive rarement seul. Riz, légumes, frites, salade, "
                "pain, café : savoir ce qui vient avec évite de commander deux "
                "fois la même chose.",
        duree='50 minutes')

    d.titre(notes="Séance courte, de vocabulaire. Elle clôt le bloc C et prépare le calcul "
                  "du bloc D.")

    d.objectifs([
        "nommer les accompagnements courants ;",
        "demander ce qui est servi avec un plat ;",
        "choisir un accompagnement quand on vous le propose ;",
        "savoir ce qui est gratuit et ce qui ne l'est pas.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui est dans cette assiette ?",
        image=IMG + 'assiette-plat.jpg',
        pistes=[
            "Quel est le plat principal ? Quels sont les accompagnements ?",
            "Aurait-on pu les choisir ?",
            "Que demanderiez-vous avant de commander ce plat ?",
            "Qu'est-ce qui arrive à part, sur la table ?",
        ],
        notes="La quatrième piste amène le pain et l'eau, apportés sans qu'on les demande "
              "et gratuits. Beaucoup d'élèves ne le savent pas.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Les accompagnements", [
        ("un accompagnement", "Ce qui est servi à côté du plat."),
        ("du riz", "Accompagnement fréquent avec le poisson et la volaille."),
        ("des légumes", "Souvent de saison, parfois « au choix »."),
        ("des frites", "Accompagnement courant, souvent au choix avec la salade."),
        ("une salade", "En accompagnement, ou en entrée selon la taille."),
    ], notes="« Au choix » revient souvent : cela veut dire que le serveur vous demandera "
             "lequel vous voulez.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Ce qui arrive à part", [
        ("le pain", "Apporté sans qu'on le demande, gratuit, souvent renouvelé."),
        ("une carafe d'eau", "Gratuite. Il suffit de la demander."),
        ("le beurre", "Servi avec le pain, sans supplément."),
        ("un café", "Payant, sauf s'il est inclus dans une formule."),
        ("une boisson gazeuse", "Toujours payante, prix sur la carte."),
    ], notes="La distinction gratuit / payant est très concrète et rarement expliquée. Elle "
             "évite des surprises sur l'addition.")

    d.tableau('Analyse', "Le plat et son accompagnement",
              ['Le plat', 'Servi avec'],
              [["La truite du jour", "des légumes et du riz"],
               ["Le poulet", "une sauce, des pommes de terre"],
               ["La soupe-repas", "du pain"],
               ["Le sandwich", "une salade ou des frites, au choix"]],
              cle=3,
              note="« Au choix » veut dire qu'on vous demandera lequel.",
              notes="Faire chercher les accompagnements dans les menus distribués. Ils sont "
                    "presque toujours écrits.")

    d.regle("Demander ce qui vient avec",
            "« C'est servi avec quoi ? »",
            precision="Quatre mots, et vous savez si vous devez commander autre chose. "
                      "Cette question évite de se retrouver avec deux salades, ou avec un "
                      "plat seul quand on avait faim.",
            notes="Diapo à photographier. Faire répéter la question par le groupe.")

    d.piege("Commander deux fois la même chose",
            "Je prends le sandwich, et une salade en accompagnement. — Il est déjà servi avec une salade.",
            "C'est servi avec quoi, le sandwich ?",
            "Sans la question, on commande — et on paie — un accompagnement déjà compris. "
            "L'erreur est fréquente et se voit seulement quand l'assiette arrive.",
            notes="Faire raconter au groupe : plusieurs auront vécu la situation.")

    d.pratique('Pratique', "Gratuit ou payant ?",
               "Dans un restaurant d'ici.", [
        ("L'eau du robinet, en carafe", "gratuit"),
        ("Le pain sur la table", "gratuit"),
        ("Une bouteille d'eau", "payant"),
        ("Le café, hors formule", "payant"),
        ("Le café inclus dans le menu du midi", "gratuit — c'est compris"),
        ("Une deuxième corbeille de pain", "gratuit, en général"),
    ], corrige=True,
       notes="La distinction eau du robinet / eau en bouteille surprend souvent. « De "
             "l'eau, s'il vous plaît » suffit pour obtenir la gratuite.")

    d.billet(
        "Choisissez trois plats d'un menu réel et notez ce qui est servi avec.",
        exemples=[
            "Recopiez la ligne du menu.",
            "Notez ce que vous auriez à commander en plus, s'il y a lieu.",
        ],
        notes="Bilan du bloc C. Le travail se fait sur les menus rapportés en A3.")

    return d.save(dossier)
