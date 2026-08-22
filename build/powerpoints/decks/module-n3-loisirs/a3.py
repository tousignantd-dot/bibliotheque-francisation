# -*- coding: utf-8 -*-
"""A3 · Dans le centre communautaire.
Bloc A « Je découvre » · couleur teal · 60 min. Écoute et vocabulaire.
Source du module : exercices `prVocab` et `prImg`, cartes FC_CARDS.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-loisirs/images/')


def img(nom):
    """Le chemin de la photo, ou None tant qu'elle n'existe pas.

    Voir la note de a1.py : les images sont produites par gen_images.py, et
    `theme.image()` ouvrirait un fichier absent. La séance se construit sans
    photo et la reprend dès qu'elle est là.
    """
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Dans le centre communautaire",
        chapeau="Un gymnase, une cuisine, une salle de projection, un "
                "comptoir d'accueil. Quatre pièces, quatre activités "
                "possibles. Savoir les nommer, c'est déjà savoir demander où "
                "l'on va.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire. Si le centre communautaire du quartier est "
                  "proche, une visite de vingt minutes vaut mieux que toutes les photos "
                  "— la séance se fait alors sur place, feuillet en main.")

    d.objectifs([
        "nommer les pièces d'un centre communautaire ;",
        "associer une pièce à l'activité qui s'y déroule ;",
        "reconnaître les objets qu'on apporte à une activité ;",
        "employer les mots du module avec leur article.",
    ])

    d.declencheur(
        'Observation', "Quelle activité peut se faire dans cette pièce ?",
        image=img('gymnase-badminton.jpg'),
        pistes=[
            "Qu'est-ce qui est peint sur le plancher, et pourquoi ?",
            "Pourquoi le plancher est-il en bois, et pas en ciment ?",
            "Qu'est-ce qu'on doit avoir aux pieds pour entrer ici ?",
            "Combien de personnes peuvent jouer en même temps ?",
        ],
        notes="La question des espadrilles arrive presque toujours d'elle-même. Si "
              "personne ne la pose, la poser : elle prépare le défi 1, où c'est la "
              "quatrième question à poser au téléphone.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Les pièces du centre", [
        ("un gymnase",
         "La grande salle au plancher de bois où l'on joue et où l'on bouge."),
        ("une cuisine collective",
         "La grande cuisine où un groupe prépare des repas ensemble et les partage."),
        ("une salle de projection",
         "La salle où l'on présente les films, avec des chaises en rangées."),
        ("le comptoir d'accueil",
         "L'endroit où l'on se renseigne, en entrant. C'est là qu'on pose ses questions."),
        ("un babillard",
         "Le panneau de liège de l'entrée, couvert de feuilles et de punaises."),
    ], notes="Faire répéter chaque mot avec son article. « Un gymnase » et « une "
             "cuisine » : le genre ne s'entend pas dans le mot, seulement dans l'article.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Ce qu'on apporte, ce qu'on paie", [
        ("des espadrilles",
         "Les souliers souples de sport, à semelle de caoutchouc. Propres, obligatoirement."),
        ("une bouteille d'eau",
         "Ce qu'on apporte à toutes les activités où l'on bouge, sans qu'on le demande."),
        ("une preuve d'adresse",
         "Un papier qui montre où l'on habite : un compte d'électricité, un bail."),
        ("le tarif du quartier",
         "Le prix plus bas offert aux gens qui habitent le quartier, sur preuve d'adresse."),
        ("une séance",
         "Une fois où l'activité a lieu : un soir, une heure précise."),
    ], notes="« Preuve d'adresse » est le mot le plus utile de la liste, et le moins "
             "deviné : beaucoup d'élèves ne savent pas qu'un compte d'électricité en "
             "tient lieu. Le dire explicitement.")

    d.tableau('Analyse', "Chaque pièce, son activité",
              ["La pièce", "Ce qui s'y passe"],
              [["le gymnase", "le badminton du mardi, la danse en ligne du jeudi"],
               ["la salle de projection", "le ciné-club du vendredi"],
               ["la cuisine", "la cuisine collective du mercredi après-midi"],
               ["le comptoir d'accueil", "on s'y renseigne et on y paie son entrée"],
               ["le babillard de l'entrée", "on y lit ce que le centre annonce"]],
              cle=0,
              note="Un même bâtiment, quatre pièces, quatre activités différentes.",
              notes="Diapo à photographier. Faire couvrir la colonne de droite et faire "
                    "redire l'activité de chaque pièce.")

    d.pratique('Association', "Quelle photo, quelle phrase ?",
               "Lisez la phrase, puis dites de quelle pièce ou de quel objet il s'agit.", [
        ("Le panneau de liège de l'entrée, couvert de feuilles retenues par des punaises.",
         "le babillard"),
        ("La grande salle au plancher de bois, avec un filet tendu au milieu.",
         "le gymnase"),
        ("Le comptoir avec un ordinateur et un présentoir à dépliants.",
         "l'accueil"),
        ("La salle avec des chaises placées en rangées devant un écran.",
         "la salle de projection"),
        ("Une paire de souliers de sport propres, à côté d'une bouteille d'eau.",
         "des espadrilles"),
        ("Deux longues tables de travail et des chaudrons dans les armoires.",
         "la cuisine collective"),
    ], corrige=True,
       notes="C'est l'exercice prImg du module, où les mêmes phrases se glissent sur des "
             "photos. Le faire ici à l'oral prépare le glisser-déposer à l'écran.")

    d.piege('Le piège', "un gymnasium, une gymnase", "un gymnase",
            "Le mot est masculin — un gymnase — et il n'a pas de forme en -ium en "
            "français, contrairement à l'anglais. Même chose pour « auditorium », qu'on "
            "dit ici « une salle » tout simplement.",
            notes="Beaucoup d'élèves passent par l'anglais pour ces mots-là. Le dire sans "
                  "en faire un reproche : c'est un raccourci normal, pas une faute de "
                  "paresse.")

    d.billet(
        "Écrivez le nom de trois pièces d'un centre communautaire, avec leur article.",
        exemples=[
            "Ajoutez, pour chacune, une activité qui peut s'y faire.",
            "Exemple : le gymnase — le badminton du mardi soir.",
        ],
        notes="Devoir court. Relever les articles à la correction : c'est le seul endroit "
              "du module où le genre des mots se travaille explicitement.")

    return d.save(dossier)
