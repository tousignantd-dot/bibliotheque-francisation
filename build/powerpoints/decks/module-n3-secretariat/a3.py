# -*- coding: utf-8 -*-
"""A3 · Une journée au centre.
Bloc A « Je découvre » · couleur teal (écoute et réponds) · 75 min.
Source : exercices `prVocab` et `prImg`, banc `FC_CARDS` (section prep).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Une journée au centre',
        chapeau="Seize mots pour tout le module, et huit images pour les "
                "poser : le comptoir, la chaise vide, le calendrier, le petit "
                "papier de la clinique.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Prévoir l'exercice 3 du module interactif à "
                  "l'écran : les huit photos se glissent sur leur phrase, et c'est ce "
                  "geste-là qui fixe les mots.")

    d.objectifs([
        "associer un mot du centre à sa définition ;",
        "reconnaître les objets d'une démarche au secrétariat ;",
        "employer chaque mot dans une phrase ;",
        "noter les mots nouveaux avec leur article.",
    ])

    d.vocabulaire('Vocabulaire', "Les mots du lieu et des gens", [
        ("le secrétariat", "le bureau où on donne et où on demande les papiers"),
        ("le comptoir", "le meuble haut derrière lequel on est reçu"),
        ("la secrétaire", "la personne qui reçoit et qui écrit dans les dossiers"),
        ("le groupe", "le numéro de votre classe, avec votre enseignante"),
        ("le dossier", "vos papiers au centre : absences, résultats"),
    ], notes="Faire dire chaque mot avec son article. « Le secrétariat » est long à "
             "prononcer : le découper en quatre morceaux au tableau.")

    d.vocabulaire('Vocabulaire', "Les mots de l'absence", [
        ("une absence", "le fait de ne pas être au cours un jour de cours"),
        ("prévenir", "dire à l'avance ce qui va arriver"),
        ("l'avant-midi", "la partie de la journée entre le matin et midi"),
        ("un rendez-vous", "une heure fixée d'avance pour rencontrer quelqu'un"),
        ("un billet d'absence", "le papier qui explique pourquoi on n'était pas là"),
    ], notes="« L'avant-midi » est un mot d'ici : ailleurs on dit « la matinée ». Le "
             "signaler, parce que l'horaire du centre l'emploie partout.")

    d.tableau('Analyse', "Les mots du papier",
              ["Le mot", "Ce que c'est"],
              [["justifier", "donner la raison pour que l'absence soit acceptée"],
               ["une photocopie", "la copie faite par la machine du bureau"],
               ["l'original", "le premier papier, celui qui a été signé"],
               ["une attestation de fréquentation", "le papier qui prouve qu'on a suivi le cours"],
               ["signer", "écrire son nom à la main au bas d'un papier"]],
              cle=1,
              note="Ces cinq mots reviennent aux défis 2 et 3 : ce sont les mots "
                   "des papiers.",
              notes="Diapo à photographier. Distinguer tout de suite l'original de la "
                    "photocopie : c'est le point du défi 2 que les élèves oublient.")

    d.pratique('Vocabulaire', "Le mot et sa définition",
               "Associez chaque mot à ce qu'il veut dire.", [
        ("Le bureau où on annonce une absence", "le secrétariat"),
        ("Le numéro de votre classe", "le groupe"),
        ("Dire à l'avance qu'on sera absent", "prévenir"),
        ("Le papier de la clinique", "un billet d'absence"),
        ("La copie faite par la machine", "une photocopie"),
        ("Écrire son nom au bas d'un papier", "signer"),
    ], corrige=True,
       notes="Reprend l'exercice de vocabulaire du module interactif. Faire à l'oral "
             "d'abord, à l'écran ensuite.")

    d.cartes("Huit images, huit phrases", "L'exercice 3 du module", [
        ("Les lieux",
         "le comptoir de l'accueil, la salle d'attente de la clinique, l'horloge du "
         "corridor un peu avant huit heures."),
        ("Les papiers",
         "le petit feuillet plié de la clinique, le calendrier du mur, la feuille qui "
         "sort du photocopieur."),
        ("Les gestes",
         "une main qui signe au bas d'une feuille, une chaise vide devant un pupitre."),
    ], cols=3,
       notes="Faire décrire chaque image avant de la glisser : c'est la description qui "
             "travaille, pas le déplacement. Un élève décrit, un autre choisit.")

    d.regle("Un mot nouveau s'écrit avec son article",
            "une absence  ·  un billet  ·  le dossier",
            precision="Rien dans l'objet ne dit le genre. Écrire « absence » "
                      "tout seul dans son carnet, c'est se préparer une "
                      "hésitation pour des années. Deux lettres de plus, et la "
                      "question est réglée.",
            notes="Diapo à photographier. Vérifier les carnets à la fin de la séance : "
                  "c'est le moment de prendre l'habitude, pas dans trois mois.")

    d.billet(
        "Écrivez six mots du module avec leur article, et une phrase avec deux d'entre eux.",
        exemples=[
            "un dossier, une absence, le comptoir…",
            "« Je vais au secrétariat pour mon billet d'absence. »",
        ],
        notes="Devoir d'écriture. Ramasser : c'est la première trace écrite du module et "
              "elle sert de référence tout le long.")

    return d.save(dossier)
