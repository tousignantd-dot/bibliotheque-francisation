# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E · couleur foret (vocabulaire et bilan) · 60 min.
Source : les cartes mémoire du module, révision des savoirs, autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='foret',
        titre='Je retiens des mots',
        chapeau="Dernière séance du module. On rassemble le vocabulaire, on revoit les "
                "savoirs, et chacun fait le point sur ce qu'il est maintenant capable "
                "de faire.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Ton différent des autres : on ne présente rien de "
                  "nouveau. Laisser beaucoup de place aux questions restées en suspens.")

    d.objectifs([
        "revoir les mots essentiels du module ;",
        "retrouver les savoirs travaillés et savoir où chacun sert ;",
        "évaluer honnêtement ce que je suis capable de faire ;",
        "savoir où retourner chercher ce qui n'est pas encore acquis.",
    ])

    d.vocabulaire('Vocabulaire · 1 de 3', "Les sortes de nouvelles", [
        ("un fait divers", "Une nouvelle sur des faits quotidiens qui attire la curiosité."),
        ("une nouvelle régionale", "Une nouvelle qui touche une région de la province."),
        ("une nouvelle nationale", "Une nouvelle qui touche la province ou le pays."),
        ("une nouvelle internationale", "Une nouvelle qui provient de l'extérieur du pays."),
        ("un reportage", "Un texte ou une émission qui présente une nouvelle en détail."),
    ], notes="Cacher la colonne de droite et faire donner les définitions. Puis "
             "l'inverse.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Les gens et les groupes", [
        ("un témoin", "Une personne qui a vu un événement."),
        ("un organisme", "Un groupe organisé qui offre un service ou mène une cause."),
        ("un festivalier", "Une personne qui participe à un festival."),
        ("un artisan local", "Une personne de la région qui fabrique des objets à la main."),
        ("le jury", "Le groupe qui juge et décide du gagnant."),
    ], notes="Faire produire une phrase avec chaque mot, sur une nouvelle du module.")

    d.vocabulaire('Vocabulaire · 3 de 3', "Les mots du récit", [
        ("amasser", "Réunir, accumuler peu à peu."),
        ("avertir", "Informer quelqu'un d'un danger ou d'une nouvelle importante."),
        ("façonner", "Fabriquer, donner une forme à quelque chose."),
        ("un franc succès", "Une vraie réussite, un grand succès."),
        ("à ce jour", "Jusqu'à maintenant, jusqu'à aujourd'hui."),
        ("un concours", "Une compétition organisée pour désigner un gagnant."),
    ], notes="Les deux expressions figées — « un franc succès », « à ce jour » — se "
             "retiennent en bloc. Les faire employer telles quelles.")

    d.tableau('Révision · 1 de 2', "Les savoirs du module",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["Les catégories", "la portée, pas l'importance", "A2"],
               ["Les marqueurs de temps", "au début, avec une virgule", "A3"],
               ["Les cinq questions", "tout est dans les deux premières phrases", "A4"],
               ["C'est… qui, c'est… que", "qui si l'élément fait l'action", "B3"],
               ["La phrase passive", "être + participe, le sujet subit", "B4"]],
              cle=0,
              notes="Faire retrouver la règle avant d'afficher la colonne du milieu. Ce "
                    "qui ne revient pas est ce qu'il faut retravailler.")

    d.tableau('Révision · 2 de 2', "Les savoirs du module, suite",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["L'imparfait", "il décrit le décor, pas l'événement", "C2"],
               ["L'accord avec être", "avec le sujet, en genre et en nombre", "C3"],
               ["Avoir ou être", "avoir par défaut, être par exception", "C4"],
               ["Lire seul", "ce que le texte dit, pas ce que je sais", "C5"]],
              cle=0, props=[0.28, 0.57, 0.15],
              note="Neuf savoirs pour un module. Chacun renvoie à une séance : c'est là "
                   "qu'il faut retourner.",
              notes="Insister sur la dernière colonne. Le module reste ouvert dans le "
                    "portail : chacun peut y revenir seul.")

    d.cartes('Les quatre gestes du module', "Ce qu'on sait faire maintenant", [
        ("Écouter une nouvelle",
         "En cherchant cinq réponses : qui, quoi, où, quand, pourquoi. Pas en essayant "
         "de tout comprendre."),
        ("Lire un fait divers",
         "En devinant les mots par le contexte, et en distinguant ce que le texte dit "
         "de ce qu'on suppose."),
        ("Raconter une nouvelle",
         "Le résultat d'abord, puis les étapes dans l'ordre du temps, avec un marqueur "
         "chacune."),
        ("Écrire un fait divers",
         "Un titre avec un verbe, le décor à l'imparfait, les événements au passé "
         "composé."),
    ], notes="Faire dire à chacun lequel des quatre lui paraît le plus solide, et lequel "
             "le moins. Personne ne doit répondre « tous ».")

    d.pratique('Bilan · 1 de 2', "Le vocabulaire, sans regarder",
               "Donnez le mot qui correspond à la définition.", [
        ("Une personne qui a vu un événement.", "un témoin"),
        ("Réunir, accumuler peu à peu.", "amasser"),
        ("Une nouvelle qui provient de l'extérieur du pays.", "une nouvelle internationale"),
        ("Fabriquer, donner une forme à quelque chose.", "façonner"),
        ("Une vraie réussite.", "un franc succès"),
        ("Une compétition pour désigner un gagnant.", "un concours"),
    ], corrige=True,
       notes="Exercice individuel, cahier fermé, cinq minutes. Corriger ensemble sans "
             "compter les points.")

    d.pratique('Bilan · 2 de 2', "Autoévaluation",
               "Pour chaque énoncé : je sais faire, presque, ou pas encore.", [
        ("Je peux dire de quelle catégorie est une nouvelle.", "séance A2"),
        ("Je peux repérer les cinq informations essentielles.", "séances A4, B1"),
        ("Je peux deviner un mot par le contexte.", "séances B2, C1"),
        ("Je peux raconter une nouvelle en trente secondes.", "séance B5"),
        ("Je choisis l'auxiliaire et j'accorde le participe.", "séances C3, C4"),
        ("Je peux écrire un fait divers de dix lignes.", "séance E1"),
    ], corrige=True,
       notes="La colonne de droite n'est pas une correction : c'est l'adresse où "
             "retourner. Le dire clairement au groupe.")

    d.billet(
        "Nommez une nouvelle en français que vous avez comprise cette semaine.",
        exemples=[
            "À la radio, à la télévision, dans un journal, sur un site.",
            "Écrivez-la en une phrase : qui, quoi, où, quand.",
        ],
        notes="Fin du module. Ces billets disent ce qui est vraiment passé de la classe "
              "à la vie — c'est le seul bilan qui compte.")

    return d.save(dossier)
