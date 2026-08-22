# -*- coding: utf-8 -*-
"""E2 · L'introduction en trois paragraphes, et le bilan
Bloc E « Je me lance » · couleur framboise · 75 min. Production écrite et bilan.
Source du module : le bloc « Production écrite » et la liste d'autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="L'introduction en trois paragraphes, et le bilan",
        chapeau="Le début du texte que l'équipe remettra. Trois paragraphes, "
                "un blanc entre chacun, une idée par paragraphe — et les "
                "quatre points d'organisation sont gagnés.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. La production écrite vient des "
                  "attentes de fin de cours : « l'adulte rédige un court "
                  "texte en organisant ses idées à l'aide de paragraphes ».")

    d.objectifs([
        "écrire une introduction en trois paragraphes ;",
        "poser le sujet comme une question, dès la première phrase ;",
        "nommer ses trois sources avec leur genre ;",
        "faire le bilan de ce qu'on est maintenant capable de faire.",
    ], notes="Prévoir quarante minutes d'écriture réelle. Le reste de la "
             "séance sert au modèle et au bilan.")

    d.declencheur(
        'Pour commencer', "Une introduction annonce-t-elle ce qu'on va chercher, ou ce qu'on a trouvé ?",
        pistes=[
            "Quand l'écrit-on, alors ?",
            "Avant le reste du texte, ou après ?",
            "Pourquoi ?",
        ],
        notes="C'est le seul paragraphe d'un travail qu'il vaut mieux "
              "rédiger en dernier. Presque personne ne le sait, et ça change "
              "la qualité des introductions du tout au tout.")

    d.tableau('Analyse', "Trois paragraphes, trois travaux",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["le premier", "le sujet, posé comme une question précise"],
               ["le deuxième", "les trois sources, nommées, et ce que chacune apporte"],
               ["le troisième", "ce que le texte va montrer, et dans quel ordre"]],
              cle=0,
              note="Un blanc entre chacun. C'est le blanc, autant que le texte, qui se voit à la correction.",
              notes="Diapositive à photographier. Montrer une introduction "
                    "sans blancs à côté d'une introduction aérée : la "
                    "différence se voit à trois mètres.")

    d.regle("Une idée principale par paragraphe",
            "Deux idées dans un même paragraphe, c'est un paragraphe de trop peu.",
            precision="Le test : essayez de résumer votre paragraphe en une "
                      "phrase. Si vous avez besoin de deux phrases, coupez-le "
                      "en deux.",
            notes="Diapositive à photographier. Ce test est aussi ce qui "
                  "permet de vérifier son propre texte sans personne pour "
                  "le relire.")

    d.tableau('Analyse', "Ce que l'introduction doit contenir",
              ['L\'élément', 'Où le mettre'],
              [["la question de recherche", "première phrase du premier paragraphe"],
               ["les trois sources", "deuxième paragraphe, avec leur genre"],
               ["un connecteur d'exemple", "n'importe où : par exemple, notamment"],
               ["une reprise par un nom", "deuxième ou troisième paragraphe"],
               ["un « où » de temps ou de lieu", "n'importe où, une fois suffit"]],
              cle=0,
              note="Cinq éléments, et la ligne « organisation » de la grille est couverte.",
              notes="Diapositive à photographier. C'est la liste "
                    "d'exigences du bloc écrit du module, dans le même "
                    "ordre.")

    d.pratique('Pratique', "Les phrases qui ouvrent",
               "Dites à quel paragraphe chaque phrase appartient.", [
        ("Qu'est-ce qui a le droit d'aller dans le bac brun, et pourquoi ?", "premier : la question"),
        ("Notre équipe a consulté trois documents.", "deuxième : les sources"),
        ("La page de la ville explique la règle ; le bulletin raconte les débuts.", "deuxième : ce que chacune apporte"),
        ("Une lectrice, elle, affirme le contraire.", "deuxième : la troisième source"),
        ("Nous montrerons d'abord la règle, puis ce qui s'est passé.", "troisième : l'ordre du texte"),
        ("Cette distribution avait eu lieu deux mois plus tôt.", "troisième : ce qu'on va montrer"),
    ], corrige=True, cols=1,
       notes="Faire écrire l'introduction juste après cet exercice, en "
             "équipe, sur papier. Quarante minutes, avec la grille de la "
             "séance B3 sur la table.")

    d.piege('Écriture',
            "remettre sans avoir relu la consigne une dernière fois",
            "ressortir la feuille, la liste à la main",
            "Une consigne se lit trois fois : au début, avant d'écrire, et "
            "une dernière fois juste avant de remettre. Cette troisième "
            "lecture prend quatre minutes et rattrape chaque session ce qui "
            "aurait coûté des points — un document oublié, une date, une "
            "bibliographie sans date.",
            notes="Faire faire la troisième lecture en classe, ici, avant que "
                  "le module se termine. C'est le geste que le module veut "
                  "installer, et il ne s'installe qu'en le faisant.")

    d.tableau('Bilan', "Ce que je suis maintenant capable de faire",
              ['Le savoir-faire', 'Où je l\'ai travaillé'],
              [["lire une consigne entière", "défi 1, B1 et B2"],
               ["lire une grille d'avance", "défi 1, B3"],
               ["suivre un texte suivi", "défi 2, C2 et C3"],
               ["distinguer fait et avis", "défi 2, C1 et C2"],
               ["rendre compte", "je me lance, E1 et E2"]],
              cle=0,
              notes="Diapositive à photographier. Terminer par l'écran "
                    "d'autoévaluation du module, en classe : dix minutes, et "
                    "chacun voit ce qu'il a gagné en trois semaines.")

    d.billet(
        "Écris une chose que tu sais faire aujourd'hui et que tu ne savais pas faire il y a trois semaines.",
        exemples=[
            "Une phrase, à la première personne.",
            "Ce n'est pas une note : c'est ce que tu emportes.",
        ],
        notes="Cinq minutes, et lire quelques réponses à voix haute si le "
              "groupe le veut bien. C'est la dernière minute du module et "
              "elle mérite d'être tenue.")

    return d.save(dossier)
