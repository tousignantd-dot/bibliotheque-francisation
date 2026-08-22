# -*- coding: utf-8 -*-
"""A4 · Mardi, ou le mardi ?
Bloc A « Je découvre » · couleur ambre · 75 min. Écriture.
Source du module : exercice `prSemaine`, mini-leçon `prSemaine`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Mardi, ou le mardi ?",
        chapeau="Un mot de deux lettres sépare « mardi prochain » de « tous "
                "les mardis ». C'est le mot que porte tout horaire de loisirs, "
                "du début à la fin, et c'est celui qu'on oublie.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. C'est le premier vrai point de langue du "
                  "module, et il est court : garder du temps pour l'écriture à la fin.")

    d.objectifs([
        "comprendre ce que change le petit mot « le » devant un jour ;",
        "dire un rendez-vous unique et une habitude hebdomadaire ;",
        "écrire les sept jours de la semaine correctement ;",
        "ajouter le moment de la journée : le samedi matin, le jeudi soir.",
    ])

    d.regle("La règle en une phrase",
            "« Mardi » = une fois. « Le mardi » = toutes les semaines.",
            precision="« Mardi, je vais au badminton » parle de mardi prochain, une "
                      "seule fois. « Le mardi, je vais au badminton » parle de tous les "
                      "mardis de la session. Le feuillet du centre est écrit "
                      "entièrement avec la deuxième forme : il décrit des habitudes, "
                      "pas des dates.",
            notes="Diapo à photographier. La faire recopier telle quelle dans le cahier : "
                  "c'est la phrase qu'on relira au moment d'écrire le message du bloc E.")

    d.tableau('Analyse', "Les deux formes, côte à côte",
              ["Sans « le » — une fois", "Avec « le » — toutes les semaines"],
              [["Mardi, j'essaie le badminton.", "Le mardi, il y a du badminton."],
               ["Samedi, on va voir un film.", "Le samedi, le centre ouvre à neuf heures."],
               ["Jeudi, j'y vais pour la première fois.", "Le jeudi, il y a de la danse en ligne."],
               ["Mercredi prochain, je commence.", "Le mercredi, la cuisine se réunit."]],
              props=[0.5, 0.5],
              note="À gauche, une date. À droite, un horaire.",
              notes="Diapo à photographier. Faire lire une colonne par la moitié de la "
                    "classe et l'autre par la seconde moitié, en alternance : la "
                    "différence de sens s'entend mieux qu'elle ne s'explique.")

    d.vocabulaire('Vocabulaire', "Les sept jours et les trois moments", [
        ("lundi · mardi · mercredi",
         "Toujours en petites lettres, sauf au début d'une phrase. Jamais de majuscule "
         "au milieu d'un texte, contrairement à l'anglais."),
        ("jeudi · vendredi",
         "Les deux soirs les plus occupés du centre : la danse en ligne et le ciné-club."),
        ("samedi · dimanche",
         "La fin de semaine. Le samedi matin est l'heure des familles ; le dimanche, le "
         "centre est fermé."),
        ("le matin · l'après-midi · le soir",
         "Le moment se colle juste après le jour : le samedi matin, le jeudi soir. "
         "Rien entre les deux."),
    ], notes="Le mot « fin de semaine » est celui du Québec ; « week-end » se comprend "
             "mais ne s'écrit pas dans un texte scolaire. Le signaler en passant.")

    d.piege('Le piège', "au jeudi soir", "le jeudi soir",
            "On ne met rien devant : ni « au », ni « du », ni « dans le ». Le jour et le "
            "moment de la journée se collent l'un à l'autre, et le petit mot « le » "
            "suffit à dire que c'est toutes les semaines.",
            notes="C'est la faute la plus fréquente de la séance, et elle vient souvent "
                  "d'une langue où la préposition est obligatoire. Le dire ainsi : en "
                  "français, ici, il n'y en a pas.")

    d.pratique('Écriture · 1 de 2', "Mardi, ou le mardi ?",
               "Complétez avec « mardi », « le mardi », « jeudi », « le jeudi », "
               "« samedi » ou « le samedi ».", [
        ("___ , il y a du badminton toutes les semaines.", "Le mardi"),
        ("___ prochain, j'essaie le badminton pour la première fois.", "Mardi"),
        ("La danse en ligne, c'est ___ , de sept heures à huit heures et demie.", "le jeudi"),
        ("___ , l'heure des familles va de dix heures à onze heures.", "Le samedi"),
        ("Camila et moi, on y va ___ , parce que c'est mon congé cette semaine-là.", "samedi"),
        ("Le centre est fermé ___ , toute l'année.", "le dimanche"),
    ], corrige=True,
       notes="C'est l'exercice prSemaine du module. Faire justifier chaque réponse par "
             "« une fois » ou « toutes les semaines » avant de valider.")

    d.pratique('Écriture · 2 de 2', "Écrivez la ligne du feuillet",
               "Pour chaque activité, écrivez une ligne comme celles du feuillet.", [
        ("badminton libre, mardi, 19 h à 21 h",
         "Le mardi soir, de dix-neuf heures à vingt et une heures."),
        ("danse en ligne, jeudi, 19 h à 20 h 30",
         "Le jeudi soir, de dix-neuf heures à vingt heures trente."),
        ("ciné-club, vendredi, 19 h",
         "Le vendredi soir, à dix-neuf heures."),
        ("heure des familles, samedi, 10 h à 11 h",
         "Le samedi matin, de dix heures à onze heures."),
        ("cuisine collective, mercredi, 13 h à 16 h",
         "Le mercredi après-midi, de treize heures à seize heures."),
    ], corrige=True,
       notes="Les heures ne sont pas encore travaillées — elles le seront en C2. Ici, "
             "n'exiger que le « le » et le moment de la journée ; accepter l'heure "
             "recopiée telle quelle.")

    d.billet(
        "Écrivez trois lignes d'horaire pour votre propre semaine.",
        exemples=[
            "Une chose que vous faites toutes les semaines : « Le lundi, je… »",
            "Une chose que vous faites une seule fois : « Vendredi, je… »",
        ],
        notes="Devoir court, et premier écrit personnel du module. Ramasser : les "
              "erreurs relevées ici se corrigent seules au bloc E, quand le message "
              "d'invitation demande exactement la même forme.")

    return d.save(dossier)
