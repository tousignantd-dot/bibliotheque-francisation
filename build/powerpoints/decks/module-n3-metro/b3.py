# -*- coding: utf-8 -*-
"""B3 · Le titre qu'il me faut.
Bloc B « Défi 1 · Comprendre ce qu'on me répond » · couleur teal · 75 min.
Source : exercices `t1titres` et `t1duree`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre="Le titre qu'il me faut",
        chapeau="Six personnes, six situations, six titres différents. "
                "Il n'y a pas de bon titre en général : il y a le bon titre "
                "pour la façon dont on se déplace.",
        duree='75 minutes')

    d.titre(notes="Séance d'appariement et de justification orale. Reprendre les billets "
                  "de la séance B1 : chacun avait choisi un titre. Trois élèves "
                  "expliquent leur choix devant le groupe avant de commencer.")

    d.objectifs([
        "associer une façon de se déplacer au titre qui lui convient ;",
        "dire combien de temps chaque titre est bon ;",
        "justifier un choix de titre en une phrase ;",
        "comprendre ce qu'est un titre illimité.",
    ])

    d.tableau('Analyse', "Chaque titre et sa durée",
              ["Le titre", "Combien de temps"],
              [["Un titre mensuel", "tout le mois, jusqu'au dernier jour"],
               ["Un titre hebdomadaire", "du lundi au dimanche"],
               ["Un titre 24 h", "24 heures à partir de la validation"],
               ["Une Soirée illimitée", "de 18 h à 5 h le lendemain"]],
              cle=0,
              note="Les quatre sont illimités : autant de déplacements qu'on veut.",
              notes="Diapositive à photographier. « Illimité » est le mot à retenir : il "
                    "sépare les titres qui comptent des voyages de ceux qui comptent du "
                    "temps. Le faire redire par trois élèves.")

    d.tableau('Analyse', "Les titres qui comptent des voyages",
              ["Le titre", "Combien de temps"],
              [["Un passage", "un seul déplacement"],
               ["Dix passages", "dix déplacements, sans date limite"],
               ["Une correspondance", "120 minutes pour finir son trajet"]],
              cle=0,
              note="Ceux-là ne s'épuisent pas avec le temps, mais avec l'usage.",
              notes="Diapositive à photographier. La distinction « compter des voyages » "
                    "ou « compter du temps » est celle qui permet de choisir. Un dix "
                    "passages ne périme pas : c'est utile à savoir.")

    d.pratique('Association', "Quel titre pour quelle personne ?",
               "Dites quel titre convient le mieux, et pourquoi.", [
        ("Vous vous déplacez tous les jours, matin et soir, tout le mois.", "un titre mensuel"),
        ("Vous venez à Montréal une seule fois, pour un rendez-vous.", "un passage"),
        ("Votre sœur visite la ville du samedi au lundi.", "un Week-end illimité"),
        ("Vous travaillez cinq jours cette semaine, puis vous partez.", "un titre hebdomadaire"),
        ("Vous sortez seulement le soir, après six heures.", "une Soirée illimitée"),
        ("Vous vous déplacez cinq ou six fois par mois, sans jour fixe.", "un dix passages"),
    ], corrige=True,
       notes="C'est l'exercice 2 du défi 1. Exiger la justification, pas seulement la "
             "réponse : « un mensuel, parce qu'elle se déplace tous les jours ». C'est "
             "la phrase qui sera demandée à l'oral en E1.")

    d.regle("La question qui décide de tout",
            "« Est-ce que je paie des voyages, ou du temps ? »",
            precision="Un passage et un dix passages comptent des voyages : "
                      "chaque déplacement en enlève un. Un hebdo et un mensuel "
                      "comptent du temps : le nombre de déplacements n'a plus "
                      "d'importance. Dès qu'on se déplace tous les jours, payer "
                      "du temps coûte moins cher.",
            notes="Diapositive à photographier. C'est la découverte pratique de tout le "
                  "module, celle qui fait économiser de l'argent. La faire reformuler "
                  "par un élève dans ses propres mots.")

    d.pratique('Justification', "Dites pourquoi",
               "Complétez chaque phrase à voix haute.", [
        ("Je prends un mensuel parce que…", "je me déplace tous les jours"),
        ("Je prends un hebdo parce que…", "je travaille seulement cette semaine"),
        ("Je prends un passage parce que…", "je viens une seule fois"),
        ("Je prends un dix passages parce que…", "je sors quelques fois par mois"),
        ("Je ne prends pas de mensuel parce que…", "je me déplace rarement"),
    ], corrige=True,
       notes="Chacun répond pour lui-même, pas pour Rosario. Passer dans les rangées et "
             "corriger la prononciation des prix plutôt que la grammaire : c'est le "
             "moment de réinvestir la séance A4.")

    d.cartes("Deux titres qu'on oublie", "Ils existent, et personne ne les demande", [
        ("La Soirée illimitée",
         "Six dollars soixante-quinze, valide de dix-huit heures à cinq heures du "
         "matin. Autant de déplacements qu'on veut. Moins cher que deux passages "
         "dès qu'on sort le soir."),
        ("Le Week-end illimité",
         "Dix-sept dollars, du vendredi seize heures au lundi cinq heures. Trois "
         "jours complets. C'est le titre à conseiller à quelqu'un qui vient "
         "visiter la ville."),
    ], notes="Ces deux titres n'apparaissent pas dans les dialogues du bloc B : ils "
             "viennent du bloc D. Les poser ici parce qu'un élève qui les connaît "
             "économise sans effort.")

    d.billet(
        "Écrivez le titre que vous allez acheter le mois prochain, et pourquoi.",
        exemples=[
            "Je vais acheter ___ .",
            "Parce que je me déplace ___ .",
        ],
        notes="Devoir court. Certains découvriront qu'ils paient trop depuis des mois : "
              "accueillir cette découverte sans en faire un reproche à qui que ce soit.")

    return d.save(dossier)
