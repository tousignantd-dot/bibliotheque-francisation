# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur framboise · 60 min.
Source : cartes mémoire, banc de vocabulaire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Quinze mots, six points de langue, un récit. Dernière séance : "
                "on rassemble, on révise, et chacun fait le point sur ce qu'il "
                "sait maintenant faire.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer : chacun doit avoir ses propres traces sous les yeux.")

    d.objectifs([
        "rassembler le vocabulaire du module en quatre familles ;",
        "réviser avec les cartes mémoire, seul ou à deux ;",
        "reformuler les six points de langue en une phrase chacun ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire.",
    ])

    d.vocabulaire('Famille · 1 de 4', "Ma journée et ma semaine", [
        ("une brassée", "Une quantité de linge qu'on lave en une fois."),
        ("la balayeuse", "L'appareil qui aspire la poussière."),
        ("le bac de recyclage", "Le bac du papier, du carton et du plastique."),
        ("un quart de travail", "Les heures qu'on travaille dans une journée."),
        ("un congé", "Une journée où on ne travaille pas."),
    ], notes="Faire redire l'article avec chaque mot. C'est la dernière occasion de le "
             "corriger.")

    d.vocabulaire('Famille · 2 de 4', "Mes loisirs", [
        ("le covoiturage", "Voyager à plusieurs dans la même voiture."),
        ("un centre communautaire", "Un lieu de quartier pour le sport et les activités."),
        ("une coéquipière", "Une personne de la même équipe que soi."),
        ("s'entraîner", "Pratiquer souvent pour devenir meilleur."),
        ("un tournoi", "Une compétition sur une ou deux journées."),
    ], notes="Demander à chacun de nommer une activité de son quartier. Si personne n'en "
             "connaît, c'est le moment de donner l'adresse du centre local.")

    d.vocabulaire('Famille · 3 de 4', "Les évènements de la vie", [
        ("un déménagement", "Le changement de logement."),
        ("une naissance", "L'arrivée d'un bébé."),
        ("un mariage", "L'union de deux personnes."),
        ("un voyage", "Un déplacement de plusieurs jours."),
        ("une arrivée", "Le moment où l'on arrive dans un pays."),
    ], notes="Ces cinq mots sont ceux du récit oral de E1. Les faire employer dans une "
             "phrase au passé composé.")

    d.vocabulaire('Famille · 4 de 4', "Donner des nouvelles", [
        ("des nouvelles", "Ce qu'on raconte de sa vie à quelqu'un de loin."),
        ("une carte postale", "Une carte envoyée pendant un voyage."),
        ("une carte de vœux", "Une carte pour féliciter ou souhaiter."),
        ("féliciter", "Dire à quelqu'un qu'on est content pour lui."),
        ("souhaiter", "Exprimer ce qu'on désire de bon pour quelqu'un."),
    ], notes="« Des nouvelles » est toujours au pluriel dans ce sens. Dernier rappel.")

    d.tableau('Les six points de langue', "Une phrase chacun",
              ['Le point', 'En une phrase'],
              [["qui, que, où", "ce qui suit le trou décide"],
               ["imparfait / passé composé", "le décor dure, l'évènement arrive"],
               ["y et là", "on ne répète jamais le lieu"]],
              cle=1,
              note="Trois autres au tableau suivant.",
              notes="Faire reformuler chaque ligne par un élève différent, dans ses mots, "
                    "avant d'afficher la colonne de droite.")

    d.tableau('Les six points de langue', "Une phrase chacun (suite)",
              ['Le point', 'En une phrase'],
              [["grâce à / à cause de", "heureux ou ennuyeux, ce n'est pas neutre"],
               ["l'accent d'insistance", "la voix monte sur le mot qui compte"],
               ["le [t] de « je suis-t-arrivée »", "on l'entend, on ne l'écrit pas"]],
              cle=1,
              notes="Ces trois-là sont les plus vite oubliés. Y consacrer un peu plus de "
                    "temps qu'aux trois premiers.")

    d.cartes('Réviser seul', "Trois façons de le faire", [
        ("Les cartes mémoire",
         "Dans l'activité interactive, section « Je retiens des mots ». La traduction est "
         "masquée par défaut : essayez d'abord, révélez ensuite."),
        ("Les trois exercices de vocabulaire",
         "Le mot et sa définition, le mot et l'image, le mot à écrire. Les trois portent "
         "sur les mêmes quinze mots."),
        ("Les mini-leçons",
         "Sept panneaux « Ouvrir la mini-leçon », avec de l'audio. Ils restent accessibles "
         "après la fin du module."),
    ], notes="Montrer les trois à l'écran, une minute chacun. Beaucoup d'élèves ignorent "
             "que le module reste ouvert après la dernière séance.")

    d.regle("Ce qu'il faut retenir du module",
            "Parler de sa semaine et raconter son histoire, c'est ce qui fait entrer "
            "quelqu'un dans un groupe.",
            precision="Mariama n'a pas appris le volleyball cette année : elle savait déjà "
                      "jouer. Ce qu'elle a appris, c'est à répondre quand on lui demande "
                      "depuis quand elle joue. C'est ça, une relation sociale.",
            notes="Diapo à photographier. C'est la phrase de clôture du module.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux parler de mes journées et de mon horaire.",
            "Je peux raconter une expérience du passé : le décor et les évènements.",
            "Je peux écrire une carte postale et une carte de vœux.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive, section « Je "
              "retiens des mots ». La faire remplir là : elle est conservée avec les "
              "traces de l'élève.")

    return d.save(dossier)
