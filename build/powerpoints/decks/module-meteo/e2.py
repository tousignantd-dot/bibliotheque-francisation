# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E · couleur framboise (vocabulaire et bilan) · 60 min.
Source : les cartes mémoire du module, révision des savoirs, autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
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

    d.vocabulaire('Vocabulaire · 1 de 3', "Les précipitations", [
        ("la poudrerie", "De la neige déjà tombée que le vent soulève."),
        ("la pluie verglaçante", "Une pluie qui gèle dès qu'elle touche une surface."),
        ("le grésil", "De petits grains de glace qui tombent du ciel."),
        ("le verglas", "La couche de glace qui reste sur les surfaces."),
        ("un redoux", "Un réchauffement court au milieu de l'hiver."),
        ("une éclaircie", "Un moment où les nuages s'ouvrent."),
    ], notes="Cacher la colonne de droite et faire donner les définitions. La distinction "
             "neige et poudrerie doit être acquise en sortant.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Le vent et la température", [
        ("une rafale", "Une hausse brusque du vent, qui dure quelques secondes."),
        ("le facteur éolien", "L'effet du vent, qui fait ressentir un froid plus intense."),
        ("le mercure", "Une autre façon de nommer la température."),
        ("le vent tombe", "Le vent diminue, il s'apaise."),
        ("le ciel se dégage", "Les nuages partent, le soleil revient."),
    ], notes="Les deux dernières sont des expressions de bulletin. Elles se retiennent "
             "en bloc, comme des mots.")

    d.vocabulaire('Vocabulaire · 3 de 3', "La route", [
        ("la chaussée", "La partie de la route où roulent les véhicules."),
        ("la visibilité", "La distance à laquelle on distingue ce qui nous entoure."),
        ("un avertissement", "Un message officiel qui signale un danger à venir."),
        ("praticable", "Où l'on peut rouler en sécurité."),
        ("un chasse-neige", "Un camion qui pousse la neige hors de la route."),
    ], notes="« Praticable » est le mot du défi 2. Faire refaire la distinction avec "
             "« ouverte » : c'est le savoir de sécurité du module.")

    d.tableau('Révision · 1 de 2', "Les savoirs du module",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["Les consonnes finales", "elles tombent à l'oral, jamais à l'écrit", "A2"],
               ["Décider selon la météo", "la condition, la règle, la solution", "A4"],
               ["Les chiffres", "toujours avec leur unité", "B2"],
               ["Pendant, en, il y a", "durée, réalisation, point dans le passé", "B3"],
               ["Le futur simple", "infinitif plus la terminaison, le r s'entend", "B4"]],
              cle=0,
              notes="Faire retrouver la règle avant d'afficher la colonne du milieu. Ce "
                    "qui ne revient pas est ce qu'il faut retravailler.")

    d.tableau('Révision · 2 de 2', "Les savoirs du module, suite",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["Lire un avertissement", "où, quoi, jusqu'à quand, quelle consigne", "C2"],
               ["Lui, leur, eux", "après « à », devant le verbe", "C3"],
               ["La condition", "jamais de futur après « si »", "C4"],
               ["Futur ou conditionnel", "le s dit la condition", "C5"]],
              cle=0, props=[0.3, 0.55, 0.15],
              note="Neuf savoirs pour un module. Chacun renvoie à une séance : c'est là "
                   "qu'il faut retourner.",
              notes="Insister sur la dernière colonne. Le module reste ouvert dans le "
                    "portail : chacun peut y revenir seul.")

    d.cartes('Les quatre gestes du module', "Ce qu'on sait faire maintenant", [
        ("Écouter un bulletin",
         "En cherchant les moments et les chiffres, pas en essayant de tout "
         "comprendre. Maintenant, avant-midi, après-midi, demain."),
        ("Lire un avertissement",
         "Où, quoi, jusqu'à quand, quelle consigne. Et surtout : quel tronçon de "
         "route."),
        ("Décider",
         "Une condition, une règle chiffrée, une solution de rechange. Ouverte ne veut "
         "pas dire praticable."),
        ("Expliquer sa décision",
         "Quatre phrases : la décision, la raison, la règle, ce qu'on fait à la place."),
    ], notes="Faire dire à chacun lequel des quatre lui paraît le plus solide, et lequel "
             "le moins. Personne ne doit répondre « tous ».")

    d.pratique('Bilan · 1 de 2', "Le vocabulaire, sans regarder",
               "Donnez le mot qui correspond à la définition.", [
        ("De la neige déjà tombée que le vent soulève.", "la poudrerie"),
        ("Une pluie qui gèle en touchant une surface.", "la pluie verglaçante"),
        ("L'effet du vent sur le froid ressenti.", "le facteur éolien"),
        ("Une autre façon de nommer la température.", "le mercure"),
        ("Où l'on peut rouler en sécurité.", "praticable"),
        ("Un réchauffement court au milieu de l'hiver.", "un redoux"),
    ], corrige=True,
       notes="Exercice individuel, cahier fermé, cinq minutes. Corriger ensemble sans "
             "compter les points.")

    d.pratique('Bilan · 2 de 2', "Autoévaluation",
               "Pour chaque énoncé : je sais faire, presque, ou pas encore.", [
        ("Je comprends un bulletin météo à la radio.", "séances B1, B2"),
        ("Je peux lire un avertissement routier.", "séance C2"),
        ("Je sais dire si une route est praticable.", "séances C1, C2"),
        ("Je peux écrire une prévision au futur simple.", "séance B4"),
        ("Je peux écrire une phrase avec une condition.", "séances C4, C5"),
        ("Je peux expliquer une décision à un collègue.", "séances B5, E1"),
    ], corrige=True,
       notes="La colonne de droite n'est pas une correction : c'est l'adresse où "
             "retourner. Le dire clairement au groupe.")

    d.billet(
        "Nommez une décision que vous avez prise cette semaine à cause de la météo.",
        exemples=[
            "Au travail, pour un déplacement, pour vos enfants.",
            "Une phrase pour la condition, une pour la décision.",
        ],
        notes="Fin du module. Ces billets disent ce qui est vraiment passé de la classe "
              "à la vie — c'est le seul bilan qui compte.")

    return d.save(dossier)
