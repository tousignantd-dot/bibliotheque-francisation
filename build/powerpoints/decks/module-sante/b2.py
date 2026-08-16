# -*- coding: utf-8 -*-
"""B2 · L'heure du rendez-vous.
Bloc B « Défi 1 · À la pharmacie » · couleur teal (écoute et réponds) · 60 min.
Source du module : exercice `co2`, dialogue `prep` (« jeudi à onze heures »).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='teal',
        titre="L'heure du rendez-vous",
        chapeau="Une heure mal comprise, c'est un rendez-vous manqué — et souvent trois "
                "semaines d'attente pour le suivant.",
        duree='60 minutes')

    d.titre(notes="Séance courte et très concrète. Elle sert autant pour la santé que "
                  "pour le travail : c'est la même compétence.")

    d.objectifs([
        "comprendre une heure dite au téléphone ;",
        "passer de l'heure en lettres à l'heure en chiffres ;",
        "comprendre le système de 13 h à 23 h ;",
        "faire répéter une heure sans gêne.",
    ])

    d.tableau('Analyse', "Ce qu'on dit, ce qu'on écrit",
              ['On dit', 'On écrit'],
              [["onze heures", "11 h"],
               ["quatorze heures", "14 h"],
               ["neuf heures et demie", "9 h 30"],
               ["seize heures quinze", "16 h 15"],
               ["dix heures moins le quart", "9 h 45"]],
              cle=0,
              note="Au Québec, on écrit « h » avec une espace de chaque côté : 9 h 30.",
              notes="La dernière ligne est celle qui piège : « dix heures moins le "
                    "quart » s'écrit 9 h 45. On dit l'heure qui vient, on écrit celle "
                    "qui est passée.")

    d.regle('La règle des après-midi',
            "Après midi, on ajoute douze.",
            precision="Deux heures de l'après-midi, c'est quatorze heures. Quatre heures "
                      "et quart, c'est seize heures quinze. Les rendez-vous se donnent "
                      "presque toujours ainsi.",
            notes="Faire compter à voix haute de 13 à 20 heures, en groupe. Trente "
                  "secondes, et ça règle la moitié des erreurs.")

    d.pratique('Pratique · 1 de 4', "En lettres, en chiffres",
               "Associez.", [
        ("onze heures", "11 h"),
        ("quatorze heures", "14 h"),
        ("neuf heures et demie", "9 h 30"),
        ("seize heures quinze", "16 h 15"),
        ("dix heures moins le quart", "9 h 45"),
    ], corrige=True,
       notes="C'est l'exercice 2 du défi 1. Le faire à l'oral d'abord, en cachant la "
             "colonne de droite.")

    d.pratique('Pratique · 2 de 4', "Écoutez et notez",
               "L'enseignant dit l'heure, vous l'écrivez en chiffres.", [
        ("« Jeudi à onze heures. »", "jeudi 11 h"),
        ("« Mardi à quatorze heures trente. »", "mardi 14 h 30"),
        ("« Vendredi à huit heures et quart. »", "vendredi 8 h 15"),
        ("« Lundi à dix-sept heures. »", "lundi 17 h"),
        ("« Mercredi à midi moins le quart. »", "mercredi 11 h 45"),
    ], corrige=True,
       notes="Dire chaque heure une seule fois, au rythme normal du téléphone. Répéter "
             "seulement si un élève le DEMANDE — c'est l'exercice de B4 qui commence ici.")

    d.cartes('Analyse', "Faire répéter, poliment", [
        ("Demander de répéter",
         "« Pardon, pouvez-vous répéter, s'il vous plaît ? » La formule passe partout, "
         "au téléphone comme au comptoir."),
        ("Demander plus lentement",
         "« Est-ce que vous pouvez parler un peu plus lentement ? » On peut le demander "
         "sans s'excuser longuement."),
        ("Vérifier ce qu'on a compris",
         "« Donc c'est bien jeudi à onze heures ? » La meilleure des trois : elle "
         "confirme au lieu de redemander."),
        ("Épeler ou noter",
         "« Un instant, je note. » Personne ne raccroche parce que vous notez."),
    ], notes="La troisième est la plus efficace et la moins pratiquée. Insister : "
             "reformuler prouve qu'on a compris et corrige l'erreur du même coup.")

    d.pratique('Pratique · 3 de 4', "Confirmez le rendez-vous",
               "Reformulez pour vérifier.", [
        ("« Le docteur Tremblay est libre jeudi à onze heures. »",
         "Donc c'est bien jeudi 11 h avec le docteur Tremblay ?"),
        ("« On vous attend mardi à quatorze heures trente. »",
         "Donc mardi, deux heures et demie de l'après-midi ?"),
        ("« Venez vendredi à huit heures et quart. »",
         "Donc vendredi matin, 8 h 15 ?"),
    ], corrige=True,
       notes="Faire dire la reformulation avec l'intonation montante de la question. "
             "C'est ce qui la rend polie plutôt que sèche.")

    d.pratique('Pratique · 4 de 4', "Au téléphone, à deux",
               "Dos à dos, sans se voir — comme au téléphone.", [
        ("L'un propose", "trois heures possibles dans la semaine"),
        ("L'autre choisit", "et dit pourquoi les autres ne conviennent pas"),
        ("Puis il confirme", "« Donc c'est bien… »"),
        ("On échange", "et on recommence avec d'autres heures"),
    ], corrige=False,
       notes="Vingt minutes, dos à dos : sans les gestes et les lèvres, l'écoute "
             "travaille vraiment. C'est le meilleur moment de la séance.")

    d.billet(
        "Écrivez trois moments de la semaine où vous êtes libre pour un rendez-vous.",
        exemples=[
            "Le jour et l'heure, en chiffres : mardi 14 h 30.",
            "Vous en aurez besoin pour l'appel de E1.",
        ],
        notes="Ramasser. Ces disponibilités rendent l'appel enregistré de E1 réaliste : "
              "l'élève aura une vraie réponse à donner.")

    return d.save(dossier)
