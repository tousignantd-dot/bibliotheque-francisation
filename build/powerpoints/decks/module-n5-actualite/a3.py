# -*- coding: utf-8 -*-
"""A3 · « Les seize mots du journal »
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : exercices `prVocab`, `prMot`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les seize mots du journal",
        chapeau="Le programme rattache à la lecture d'un fait divers deux "
                "champs de lexique : les actes criminels et les "
                "catastrophes naturelles. Les seize mots du module en "
                "sortent, plus les quatre qui décrivent le journal "
                "lui-même.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Elle vient en troisième position parce que les "
                  "mots ont d'abord été entendus dans le dialogue de A1 : on nomme ce "
                  "qu'on a déjà rencontré, jamais l'inverse.")

    d.objectifs([
        "nommer les parties d'un journal et ceux qui y parlent ;",
        "nommer un sinistre et ses conséquences pour les gens ;",
        "nommer ce qui suit un évènement : l'enquête, l'avertissement ;",
        "employer chaque mot avec son article.",
    ], notes="Le quatrième objectif est le moins spectaculaire et le plus rentable. "
             "L'article porte le genre, et le genre décide de tout ce qui suit.")

    d.vocabulaire('Vocabulaire · 1 de 4', "Le journal et ceux qui y parlent", [
        ("un fait divers", "Un court article qui raconte un évènement arrivé près de chez soi : un feu, un vol, une inondation."),
        ("un hebdomadaire", "Un journal qui paraît une seule fois par semaine, toujours le même jour."),
        ("le chapeau", "Les deux ou trois lignes en gras placées sous le titre, qui disent toute la nouvelle d'un coup."),
        ("un témoin", "La personne qui se trouvait sur place et qui a vu ce qui s'est passé."),
    ], notes="Ces quatre mots sont ceux de la séance A1. Les faire redire de mémoire "
             "avant d'afficher les définitions : la moitié du groupe les a déjà.")

    d.vocabulaire('Vocabulaire · 2 de 4', "Le sinistre et ceux qu'il touche", [
        ("un incendie", "Un feu qui échappe au contrôle et qui détruit un bâtiment ou une forêt."),
        ("évacuer", "Faire sortir tout le monde d'un endroit devenu dangereux, le plus vite possible."),
        ("un sinistré", "Une personne qui a perdu son logement ou ses biens dans un feu ou une inondation."),
        ("une inondation", "De l'eau qui monte et qui entre là où elle ne devrait pas : une rue, une cave, un champ."),
    ], notes="« Évacuer » est le seul verbe de la liste et il s'emploie des deux "
             "façons : on évacue un immeuble, et on évacue les gens. Donner les deux "
             "constructions tout de suite.")

    d.vocabulaire('Vocabulaire · 3 de 4', "Ce qui vient après", [
        ("une déclaration", "Ce que quelqu'un dit officiellement, et que le journal peut répéter mot pour mot."),
        ("une enquête", "Le travail qu'on fait après un évènement pour comprendre comment il est arrivé."),
        ("un enquêteur", "La personne chargée de chercher les causes et de poser les questions."),
        ("un avertissement", "L'annonce officielle qui prévient d'un danger qui s'en vient : pluie forte, verglas, chaleur."),
    ], notes="« Une enquête » et « un enquêteur » se tiennent par la main : les "
             "présenter ensemble, avec l'accent circonflexe au tableau. C'est celui "
             "qu'on oublie le plus souvent à l'écrit.")

    d.vocabulaire('Vocabulaire · 4 de 4', "Le délit et la prudence", [
        ("un vol", "Le fait de prendre une chose qui appartient à quelqu'un d'autre, sans permission."),
        ("un suspect", "La personne que la police croit responsable, tant que rien n'est prouvé."),
        ("un cabanon", "La petite bâtisse de la cour où on range les outils, les pelles et les vélos."),
        ("la prévention", "Tout ce qu'on fait d'avance pour empêcher qu'une chose fâcheuse arrive."),
    ], notes="« Un suspect » demande une précision culturelle : tant qu'un tribunal ne "
             "s'est pas prononcé, le journal écrit « présumé ». Ce n'est pas une "
             "politesse, c'est une obligation.")

    d.tableau('Deux familles', "Le sinistre, et le délit",
              ['La famille', 'Ce qui la caractérise'],
              [["Le sinistre", "Personne ne l'a voulu : un feu, une inondation, une tempête."],
               ["Ses victimes", "Ce sont les sinistrés. On les héberge, on les habille, on les reloge."],
               ["Le délit", "Quelqu'un l'a fait : un vol, une entrée par effraction, un méfait."],
               ["Sa suite", "La police cherche un suspect. Rien n'est prouvé avant le tribunal."],
               ["Dans les deux cas", "Une enquête commence, et le journal finit par « elle se poursuit »."]],
              cle=1,
              notes="Faire trier oralement une dizaine de mots au tableau avant "
                    "d'afficher : incendie, vol, verglas, effraction, glissement de "
                    "terrain, méfait. Le tri se fait tout seul une fois le principe "
                    "compris.")

    d.pratique('Écriture', "Le mot juste pour la nouvelle",
               "Complétez avec le mot qui convient.", [
        ("Un ___ a détruit les quatre logements de la rue Alexandre.", "incendie"),
        ("Après trois jours de pluie, l'___ a rempli une dizaine de sous-sols.", "inondation"),
        ("Un ___ raconte qu'il a vu trois vélos dans une remorque.", "témoin"),
        ("Les onze ___ ont été hébergés par la Croix-Rouge.", "sinistrés"),
        ("L'___ dira si le feu est parti de la cuisine.", "enquête"),
        ("Lis le ___ : tu sauras la nouvelle en deux lignes.", "chapeau"),
    ], corrige=True,
       notes="Exercice prMot de l'activité interactive. Le faire d'abord à l'oral, "
             "collectivement, puis laisser les élèves le refaire seuls sur les postes.")

    d.piege("Apprendre un mot sans son article",
            "incendie, enquête, cabanon",
            "un incendie, une enquête, un cabanon",
            "L'article porte le genre, et le genre décide de tout ce qui suit : « cet "
            "incendie », « cette enquête ». Un mot appris sans article est un mot à "
            "réapprendre.",
            notes="Les cartes mémoire du module donnent toujours l'article. Le montrer "
                  "à l'écran : c'est la raison pour laquelle elles sont faites ainsi.")

    d.piege("Employer « sinistré » pour un vol",
            "Les sinistrés du vol de vélos.",
            "Les victimes du vol de vélos.",
            "« Sinistré » ne s'emploie que pour un feu, une inondation, une tempête — "
            "quelque chose que personne n'a voulu. Pour un vol, on dit une victime, "
            "et le journal parle d'un délit.",
            notes="Erreur fréquente et facile à corriger : les deux familles du tableau "
                  "précédent servent exactement à ça. Y revenir en une phrase.")

    d.billet(
        "Choisissez trois mots de la séance et écrivez une phrase avec chacun.",
        exemples=[
            "Une phrase qui parle de votre quartier, pas de celui de Marisol.",
            "Vérifiez l'article avant de remettre votre billet.",
        ],
        notes="Ramasser. Les phrases des élèves sur leur propre quartier serviront "
              "d'exemples en A4 et au bloc B.")

    return d.save(dossier)
