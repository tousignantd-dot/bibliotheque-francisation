# -*- coding: utf-8 -*-
"""A1 · À la table d'inscription.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `pr1` et `prImg`.

Deuxième module du niveau 1 : le stade reste celui du grand débutant. Les
diapositives portent peu de mots, et chaque phrase projetée est une phrase que
l'élève pourra dire lui-même. La différence avec le module précédent tient en
un mot : ici, on écrit.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="À la table d'inscription",
        chapeau="Une feuille, huit cases, et quelqu'un qui pose une question "
                "à la fois. C'est ainsi que commence toute inscription.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Apporter de vraies fiches vierges — une par "
                  "élève — et les distribuer tout de suite : elles serviront de fil "
                  "conducteur pendant les huit séances.")

    d.objectifs([
        "reconnaître une fiche d'inscription ;",
        "nommer une case ;",
        "comprendre la question « vous venez pour l'inscription ? » ;",
        "écrire son nom en lettres majuscules.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on vous demande ?",
        pistes=[
            "Où êtes-vous assis ?",
            "Qu'est-ce qu'il y a sur la table ?",
            "Qui pose les questions ?",
            "Combien de cases faut-il remplir ?",
        ],
        notes="Faire circuler la fiche vierge pendant la discussion. Laisser répondre dans "
              "la langue qu'on peut : à ce stade, comprendre la situation compte plus que "
              "la dire en français.")

    d.dialogue('Dialogue · 1 de 2', "On vous donne la fiche", [
        ("MADAME CÔTÉ", "Bonjour ! Vous venez pour l'inscription ?", True),
        ("YUSUF", "Oui. Bonjour, madame.", True),
        ("MADAME CÔTÉ", "Voici votre fiche. Il y a huit cases.", True),
        ("YUSUF", "Huit cases ? C'est beaucoup.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapo masquée. Puis afficher et faire répéter "
             "réplique par réplique, en chœur.")

    d.dialogue('Dialogue · 2 de 2', "Une case à la fois", [
        ("MADAME CÔTÉ", "Non, non. Je vous aide. Une case à la fois.", True),
        ("YUSUF", "D'accord. Merci.", True),
        ("MADAME CÔTÉ", "On commence par le nom. Écrivez en lettres majuscules.", True),
    ], notes="Insister sur « une case à la fois » : c'est la phrase qui désamorce la peur "
             "du formulaire, et c'est aussi la méthode de tout le module.")

    d.tableau('Analyse', "Trois mots à retenir",
              ['Le mot', 'Ce que c\'est'],
              [["une inscription", "le moment où on donne son nom pour entrer dans un cours"],
               ["une fiche", "la feuille de papier avec les cases"],
               ["une case", "le petit rectangle où on écrit une seule chose"]],
              cle=2,
              note="Une case, un renseignement. Jamais deux choses dans la même case.",
              notes="Diapo à photographier. Montrer les trois sur la fiche distribuée en "
                    "début de séance.")

    d.regle("Écrire en lettres majuscules",
            "DAOUD, YUSUF.",
            precision="On vous le demandera presque partout. Les lettres détachées se "
                      "lisent sans erreur, même quand le nom ne vient pas d'ici. Écrivez "
                      "lentement, une lettre à la fois, sans les coller.",
            notes="Diapo à photographier. Faire écrire son nom de famille en majuscules "
                  "sur la fiche vierge, tout de suite.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Yusuf vient pour l'inscription.", "vrai"),
        ("La fiche a huit cases.", "vrai"),
        ("Madame Côté ne l'aide pas.", "faux — elle l'aide"),
        ("On commence par le nom.", "vrai"),
        ("On écrit en lettres majuscules.", "vrai"),
    ], corrige=True, cols=1,
       notes="Cinq énoncés seulement : à ce stade, huit seraient trop.")

    d.pratique('Pratique · à deux', "Ce qu'on voit ce jour-là",
               "Nommez ce que vous voyez, puis dites à quoi ça sert.", [
        ("La table", "C'est ici qu'on s'inscrit."),
        ("La fiche", "On écrit dedans."),
        ("Le stylo", "On écrit avec."),
        ("La boîte aux lettres", "On y reçoit son courrier."),
    ], cols=1,
       notes="Vingt minutes. Circuler, écouter, ne corriger que ce qui empêche de "
             "comprendre. Les six photos de l'exercice `prImg` sont dans l'activité "
             "interactive : y renvoyer les élèves rapides.")

    d.billet(
        "Écrivez votre nom de famille et votre prénom, en lettres majuscules.",
        exemples=[
            "Une lettre à la fois, bien détachées.",
            "Puis dites-les à voix haute, chez vous, trois fois.",
        ],
        notes="Devoir minuscule et essentiel. Plusieurs écriront leur nom en majuscules "
              "pour la première fois.")

    return d.save(dossier)
