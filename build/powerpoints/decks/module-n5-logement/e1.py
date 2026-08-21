# -*- coding: utf-8 -*-
"""E1 · Je me lance — la visite, des deux côtés.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle `louer` et production orale du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="La visite, des deux côtés",
        chapeau="Au niveau 5, il ne suffit plus de comprendre ce qu'on vous "
                "dit d'un logement : il faut savoir le dire à votre tour.",
        duree='75 minutes')

    d.titre(notes="Première séance de production. Prévoir les appareils : le jeu de rôle "
                  "et l'enregistrement se font dans le module interactif. Vérifier les "
                  "micros avant que le groupe arrive.")

    d.objectifs([
        "mener une visite en posant les questions utiles ;",
        "faire visiter en donnant les renseignements sans qu'on les redemande ;",
        "réemployer les relatifs, le gérondif et le futur ;",
        "s'enregistrer, s'écouter, se corriger.",
    ])

    d.declencheur(
        'Mise en route', "Qu'est-ce qui est le plus difficile : visiter ou faire visiter ?",
        pistes=[
            "Quand vous visitez, que devez-vous faire ?",
            "Quand vous faites visiter, que devez-vous faire ?",
            "Lequel des deux demande le plus de vocabulaire ?",
            "Lequel avez-vous déjà fait dans votre vie ?",
        ],
        notes="Faire visiter demande plus : il faut décrire, chiffrer et anticiper les "
              "questions. C'est pour cela que le programme du niveau 5 le demande, et que "
              "la production orale porte là-dessus.")

    d.tableau('Le jeu de rôle', "Trois logements, deux rôles",
              ['Le logement', 'Ce que dit l\'annonce'],
              [["Le 2 ½ du centre-ville", "meublé, 3e étage, 690 $, libre le 1er octobre"],
               ["Le 5 ½ de Fleurimont", "3 chambres, sous-sol fini, 2 stationnements, 1 390 $"],
               ["Le 4 ½ du Vieux-Nord", "maison centenaire, bois, balcon, non-fumeur, 1 050 $"]],
              cle=0,
              note="L'annonce est tout ce que les deux personnes ont sous les yeux. Le reste se demande.",
              notes="Chaque élève fait les deux rôles, sur deux logements différents. "
                    "L'assistant ne donne jamais un renseignement avant qu'on le lui "
                    "demande : c'est ce qui rend l'exercice utile.")

    d.cartes("Les sept sujets à couvrir", "La grille du jeu de rôle", [
        ("Ce qui est inclus dans le loyer", "La première question, toujours."),
        ("Le chauffage et l'électricité", "Un chiffre, pas une impression."),
        ("Les électroménagers et la buanderie", "Ce qui est fourni, ce qui ne l'est pas."),
        ("Le stationnement", "Combien de cases, et incluses ou non."),
        ("Les animaux", "Se demande tôt : c'est éliminatoire ou non."),
        ("Le bruit et le voisinage", "Ce qu'aucune annonce n'écrit."),
        ("La date et la durée du bail", "Et le loyer de l'ancien locataire."),
    ], cols=2,
       notes="Projeter la grille pendant tout le jeu de rôle. Les élèves cochent au fur et "
             "à mesure — c'est ce qui les empêche d'oublier trois sujets sur sept.")

    d.regle("Répondez, puis précisez",
            "« Non, le chauffage n'est pas inclus » — puis : « comptez environ cent "
            "dollars par mois l'hiver ».",
            precision="Un simple « non » oblige le visiteur à poser trois questions de "
                      "plus. Donner le chiffre tout de suite, c'est ce qui distingue "
                      "quelqu'un qui répond de quelqu'un qui renseigne.",
            notes="Diapositive à photographier. C'est le premier critère de correction de "
                  "la production orale.")

    d.tableau('La production orale', "Quatre temps, une minute",
              ['Le temps', 'Ce qu\'on dit'],
              [["Accueillir et situer", "« C'est un quatre et demie au deuxième étage. »"],
               ["Décrire les pièces", "« Le salon est ensoleillé, c'est la pièce qui donne sur la cour. »"],
               ["Dire ce qui est inclus", "« Le chauffage n'est pas inclus : environ cent dollars par mois. »"],
               ["Annoncer le bail", "« Le bail se terminera le 30 juin et se renouvellera. »"]],
              cle=0,
              note="Un relatif, un gérondif, un futur : les trois points du module doivent s'entendre.",
              notes="Diapositive à photographier. C'est le plan de la production, et la "
                    "grille de correction. Le projeter pendant les enregistrements.")

    d.piege("Dire seulement ce qui est beau",
            "C'est un beau logement, vous allez voir, il est très bien.",
            "Honnêtement, on entend marcher au-dessus. Les voisins sont tranquilles.",
            "Un défaut annoncé d'avance devient une information et inspire confiance ; "
            "découvert après la signature, il devient un conflit. Hélène le fait dans le "
            "dialogue, et Nadège la remercie.",
            notes="Faire réécouter la réplique d'Hélène au défi 2. C'est le modèle.")

    d.pratique('Production orale', "Enregistrez-vous",
               "Une minute. Vous faites visiter le logement de votre choix.", [
        ("Temps 1", "Accueillir et dire de quel logement il s'agit"),
        ("Temps 2", "Décrire deux pièces, avec un relatif"),
        ("Temps 3", "Dire ce qui est inclus, avec un chiffre"),
        ("Temps 4", "Annoncer les conditions du bail, au futur"),
    ], corrige=False,
       notes="Trois écoutes minimum : l'élève s'enregistre, s'écoute, recommence. La "
             "rétroaction de l'assistant vient ensuite, et le dépôt à l'enseignante en "
             "dernier. Les corrections de l'assistant ne sont jamais conservées.")

    d.billet(
        "Réécoutez votre enregistrement une fois de plus, ce soir.",
        exemples=[
            "Avez-vous donné au moins un chiffre ?",
            "Avez-vous employé un « qui », un « en -ant » et un futur ?",
        ],
        notes="Devoir d'autoécoute. C'est souvent la deuxième écoute, à froid, qui fait "
              "entendre les répétitions et les blancs.")

    return d.save(dossier)
