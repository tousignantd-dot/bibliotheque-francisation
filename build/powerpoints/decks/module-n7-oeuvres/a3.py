# -*- coding: utf-8 -*-
"""A3 · Le vocabulaire d'une soirée de spectacle
Bloc A « Je découvre » · couleur framboise · vocabulaire · 75 min.
Source : exercices `prVocab`, `prMots` et `prImg`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-oeuvres' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Le vocabulaire d'une soirée de spectacle",
        chapeau="Une première partie, un rappel, une chute, un refrain : les "
                "mots du métier sont peu nombreux et ils reviennent tous "
                "les jours dans une conversation ordinaire.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Le lexique de cette situation est presque "
                  "entièrement abstrait : peu d'images, beaucoup de définitions. "
                  "Prévoir plus d'oral et moins de tableau.")

    d.objectifs([
        "nommer les lieux où l'on rencontre une œuvre ;",
        "employer les mots d'une soirée de spectacle ;",
        "distinguer une critique d'un compte rendu ;",
        "définir un mot abstrait sans le répéter dans sa définition.",
    ], notes="Le quatrième objectif est un savoir-faire, pas une liste : il servira "
             "en E2, quand il faudra écrire un compte rendu clair pour des gens qui "
             "n'étaient pas là.")

    d.declencheur(
        'Observation', "Combien de ces lieux connaissez-vous ?",
        image=IMG + 'sous-sol-deglise.jpg',
        pistes=[
            "Une salle de spectacle, un cinéma de quartier, une bibliothèque ?",
            "Un sous-sol d'église transformé en salle, un bar avec une scène ?",
            "Y êtes-vous déjà entré, ici, depuis votre arrivée ?",
            "Qu'est-ce qui vous en a empêché, s'il y a lieu ?",
        ],
        notes="La quatrième piste amène le prix, la langue, l'horaire, la garde des "
              "enfants. Ce sont de vraies réponses et elles méritent deux minutes : "
              "le module suppose qu'on peut sortir, et ce n'est pas donné à tous.")

    d.cartes('Vocabulaire', "Six lieux, six mots", [
        ("une salle de spectacle", "des fauteuils, une scène, un balcon"),
        ("un cinéma de quartier", "un hall, un comptoir, un écran"),
        ("un sous-sol d'église", "des chaises pliantes, une scène sur des palettes"),
        ("une scène de bar", "un tabouret, un micro sur pied, un rideau noir"),
        ("une bibliothèque", "un rayon de romans, un fauteuil, une lampe"),
        ("un studio", "une guitare, un casque, une vitre au fond"),
    ], cols=2,
       notes="Exercice `prImg` du module. En classe, faire décrire chaque lieu à voix "
             "haute avant de montrer la photo : l'élève cherche ses mots, et c'est là "
             "que le vocabulaire se fixe.")

    d.vocabulaire('Vocabulaire', "Six mots de la soirée", [
        ("la première partie", "Le court spectacle présenté avant le spectacle principal, par quelqu'un d'autre."),
        ("un rappel", "Une ou deux chansons de plus, jouées quand le public applaudit après la fin."),
        ("un sketch", "Une courte scène jouée ou racontée pour faire rire."),
        ("une chute", "La dernière phrase d'une histoire drôle, celle qui déclenche le rire."),
        ("un refrain", "Les quelques vers d'une chanson qui reviennent après chaque partie."),
        ("un couplet", "La partie d'une chanson qui change chaque fois et qui fait avancer l'histoire."),
    ], notes="Faire répéter avec l'article. « Une chute » et « un rappel » sont les "
             "deux mots que personne ne devine : ils n'ont rien à voir avec leur sens "
             "courant.")

    d.tableau('Analyse', "Deux mots qu'on confond",
              ['Le mot', 'Ce qu\'il est exactement'],
              [["Une critique",
                "un texte publié, signé, qui présente une œuvre et la juge"],
               ["Un compte rendu",
                "un écrit qui rapporte ce qui s'est dit et décidé dans une rencontre"]],
              cle=0,
              note="Une critique juge une œuvre. Un compte rendu rapporte une discussion.",
              notes="Diapositive à photographier. Les deux se ressemblent et l'élève "
                    "écrira les deux : la critique se lit en D2, le compte rendu "
                    "s'écrit en E2.")

    d.regle("Une définition ne contient jamais le mot",
            "Définir « une appréciation » par « le fait d'apprécier » n'apprend "
            "rien à personne.",
            precision="La règle vaut pour la classe et pour la vie : quand un mot "
                      "vous manque, définissez-le sans lui. « La chose qu'on pense "
                      "d'un film après l'avoir vu » se comprend tout de suite, et "
                      "c'est ainsi qu'on se fait comprendre sans le mot exact.",
            notes="Diapositive à photographier. C'est une stratégie de communication "
                  "autant qu'un exercice : elle sert chaque fois qu'un mot manque.")

    d.pratique('Vocabulaire', "Le mot et sa définition",
               "Associez chaque mot à ce qu'il désigne exactement.", [
        ("la première partie", "le court spectacle avant celui qu'on est venu voir"),
        ("un rappel", "les chansons jouées en plus, après la fin annoncée"),
        ("un tour de chant", "un spectacle où une personne chante ses chansons"),
        ("une chute", "la dernière phrase d'une histoire drôle"),
        ("un long métrage", "un film de cinéma de plus d'une heure"),
        ("une critique", "un texte publié qui présente une œuvre et la juge"),
    ], corrige=True,
       notes="Exercice `prMots` du module. Faire faire à l'oral en équipes de deux "
             "avant l'écran : celui qui explique retient mieux que celui qui associe.")

    d.billet(
        "Choisissez un mot abstrait de la liste et définissez-le sans l'employer.",
        exemples=[
            "Une appréciation, une concession, un argument, une image.",
            "Deux lignes, et vérifiez que le mot n'y est pas.",
        ],
        notes="Ramasser les billets : ils montrent tout de suite qui définit par "
              "l'exemple, qui définit par la famille du mot, et qui tourne en rond.")

    return d.save(dossier)
