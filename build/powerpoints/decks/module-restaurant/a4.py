# -*- coding: utf-8 -*-
"""A4 · Au restaurant, en images.
Bloc A « Je découvre » · couleur teal · 50 min.
Source : exercice `prImg`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-restaurant/images/')


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre='Au restaurant, en images',
        chapeau="Huit moments d'un repas, de l'entrée au terminal de "
                "paiement. Les nommer, c'est savoir ce qui va arriver — et "
                "dans quel ordre.",
        duree='50 minutes')

    d.titre(notes="Séance visuelle et courte. Elle clôt le bloc A : à la fin, chacun doit "
                  "pouvoir raconter le déroulement d'un repas.")

    d.objectifs([
        "nommer huit éléments d'un repas au restaurant ;",
        "connaître l'ordre : accueil, commande, repas, addition ;",
        "employer l'article juste : la carte, une carafe, l'addition ;",
        "savoir ce qui est gratuit et ce qui ne l'est pas.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui est sur cette table, et à quel moment du repas ?",
        image=IMG + 'table-deux.jpg',
        pistes=[
            "Que voyez-vous sur la table avant l'arrivée des plats ?",
            "Qu'est-ce qu'on apporte en premier ?",
            "Qu'est-ce qui est gratuit, à votre avis ?",
            "Y a-t-il quelque chose que vous ne reconnaissez pas ?",
        ],
        notes="La troisième piste amène l'eau du robinet et le pain. Les deux sont gratuits "
              "au Québec, ce qui n'est pas le cas partout.")

    d.cartes('Le déroulement', "Quatre moments, toujours les mêmes", [
        ("1 · L'accueil",
         "On attend qu'on vous place. Trois questions : combien, réservation, préférence."),
        ("2 · La commande",
         "On vous donne la carte. Vous pouvez prendre deux minutes. Le serveur revient."),
        ("3 · Le repas",
         "Le serveur passe demander si tout va bien. C'est le moment de demander ou de "
         "signaler."),
        ("4 · L'addition",
         "Vous la demandez — elle n'arrive pas toute seule. Puis le pourboire, puis le "
         "paiement."),
    ], notes="Diapo à photographier. Connaître l'ordre vaut mieux que tout comprendre : on "
             "sait ce qui s'en vient.")

    d.cartes("Ce qui est gratuit ici", "Quatre choses", [
        ("L'eau du robinet",
         "Servie en carafe, gratuite, et il suffit de la demander. Beaucoup de gens ne "
         "savent pas qu'on peut."),
        ("Le pain",
         "Souvent apporté sans qu'on le demande, et souvent renouvelé si on le finit."),
        ("Le café du menu du midi",
         "Fréquemment inclus dans la formule. C'est écrit sous le prix."),
        ("Ce qui n'est pas gratuit",
         "L'eau en bouteille, les boissons gazeuses, le deuxième café hors formule. Le "
         "prix est sur la carte."),
    ], notes="La première carte fait souvent une petite révélation. « De l'eau, s'il vous "
             "plaît » suffit — inutile de préciser « du robinet ».")

    d.tableau('Analyse', "Le mot et le moment",
              ['Le mot', 'Quand'],
              [["la carte", "à l'accueil, avant de commander"],
               ["une entrée", "le premier service"],
               ["le plat principal", "après l'entrée"],
               ["une carafe", "pendant tout le repas"],
               ["l'addition", "à la fin, quand on la demande"]],
              cle=4,
              note="L'addition n'arrive jamais toute seule : il faut la demander.",
              notes="La note est importante. Dans plusieurs pays, l'addition arrive d'elle-"
                    "même ; ici, l'apporter sans qu'on la demande serait presque impoli.")

    d.regle("L'addition se demande",
            "« L'addition, s'il vous plaît. »",
            precision="Le serveur ne l'apporte pas de lui-même : cela reviendrait à vous "
                      "presser de partir. Vous pouvez rester à table après le repas sans "
                      "que personne ne vous dérange — et c'est vous qui décidez du moment.",
            notes="Diapo à photographier. Beaucoup d'élèves attendent longtemps sans savoir "
                  "qu'il faut demander.")

    d.piege("Attendre l'addition",
            "On attend depuis vingt minutes, personne ne vient.",
            "L'addition, s'il vous plaît.",
            "Le serveur attend votre signal. Tant que vous ne demandez pas, il considère "
            "que vous prenez votre temps — et c'est une politesse de sa part.",
            notes="Faire répéter la phrase par le groupe. Trois mots qui évitent vingt "
                  "minutes d'attente.")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec le mot du vocabulaire.", [
        ("Voici la ___ , je vous laisse choisir.", "carte"),
        ("Le menu du jour est sur l'___ .", "ardoise"),
        ("Soupe ou salade en ___ .", "entrée"),
        ("Une ___ d'eau pour deux, s'il vous plaît.", "carafe"),
        ("L'eau du ___ est gratuite.", "robinet"),
        ("L'___ , s'il vous plaît.", "addition"),
    ], corrige=True,
       notes="Ces six mots sont dans le banc de vocabulaire du module.")

    d.billet(
        "Racontez le déroulement d'un repas au restaurant, en quatre phrases.",
        exemples=[
            "Une phrase par moment : accueil, commande, repas, addition.",
            "Employez au moins quatre mots du vocabulaire.",
        ],
        notes="Bilan du bloc A. Ces récits sont le brouillon de la production orale de E1.")

    return d.save(dossier)
