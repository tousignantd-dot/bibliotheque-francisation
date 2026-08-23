# -*- coding: utf-8 -*-
"""A3 · Dire la conséquence, pas l'émotion
Bloc A « Je découvre » · couleur ambre · grammaire et écriture · 75 min.
Source : exercice `prConseq` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre="Dire la conséquence, pas l'émotion",
        chapeau="« Ça me dérange » se discute et se perd. « Cela m'empêche de "
                "dormir plus de quatre heures depuis quinze jours » ne se "
                "discute pas.",
        duree='75 minutes')

    d.titre(notes="Séance de langue. C'est la plus utile du module et celle qui sert "
                  "hors du module : la même tournure vaut pour un employeur, une "
                  "clinique, un service public.")

    d.objectifs([
        "employer « cela m'empêche de » et « cela m'oblige à » ;",
        "remplacer un adjectif par un fait daté ;",
        "choisir entre en, pour, pendant et depuis ;",
        "écrire trois phrases de conséquence sur sa propre situation.",
    ], notes="Le deuxième objectif est le cœur : chaque adjectif se remplace par un "
             "chiffre ou une date, et la phrase devient impossible à contredire.")

    d.declencheur(
        'Observation', "« Je suis épuisée. » Qu'est-ce qu'on peut répondre à ça ?",
        pistes=[
            "Est-ce que quelqu'un peut vérifier cette phrase ?",
            "Et « je dors quatre heures par nuit depuis le 4 février » ?",
            "Laquelle des deux ferait bouger un propriétaire ?",
            "Pourquoi la première nous vient-elle d'abord ?",
        ],
        notes="Personne ne peut contredire une émotion, et c'est justement pour ça "
              "qu'elle ne sert à rien : elle n'oblige personne. Le laisser venir du "
              "groupe.")

    d.regle("Cela m'empêche de, cela m'oblige à",
            "On nomme ce qu'on ne peut plus faire, ou ce qu'on doit faire malgré soi.",
            precision="« Cela m'empêche de dormir plus de quatre heures. » « Cela "
                      "m'oblige à me lever à cinq heures trente. » Retenir le couple : "
                      "empêcher DE, obliger À. Les deux prépositions se mélangent tout "
                      "le temps, et l'erreur s'entend.",
            notes="Diapositive à photographier. Faire produire oralement une phrase de "
                  "chaque type par cinq élèves avant de passer à la suite.")

    d.tableau('Analyse', "Ce qui se discute, ce qui ne se discute pas",
              ['À éviter', 'À écrire plutôt'],
              [["Ça me dérange.", "Cela m'empêche de dormir plus de quatre heures."],
               ["Je suis épuisée.", "Je suis réveillée neuf matins sur quatorze."],
               ["C'est insupportable.", "Le bruit dure quarante minutes, dès 5 h 45."],
               ["Il n'a aucun respect.", "L'appareil n'a pas été déplacé au 12 mars."],
               ["Ça fait des mois.", "Je tiens un registre depuis le 4 février."]],
              cle=1,
              notes="Diapositive à photographier. Faire remarquer que la colonne de "
                    "droite est plus longue : c'est le prix, et il est faible.")

    d.cartes('Analyse', "Quatre prépositions de temps", [
        ("en + durée", "Le temps qu'il a fallu pour y arriver. « Je me rendormais en dix minutes. »"),
        ("pour + durée", "La durée prévue d'avance. « Il part pour la journée. »"),
        ("pendant + durée", "La durée complète de l'action. « Il court pendant quarante minutes. »"),
        ("depuis + date", "Le point de départ, et ça continue. « Je note depuis le 4 février. »"),
    ], notes="« Depuis » est le plus important des quatre dans ce module : c'est lui "
             "qui dit la répétition, et la répétition est ce qui fait passer un bruit "
             "du normal à l'anormal.")

    d.piege('Grammaire',
            "Cela m'empêche à dormir",
            "Cela m'empêche de dormir",
            "L'erreur est fréquente parce que les deux verbes se ressemblent par le "
            "sens : empêcher et obliger décrivent tous les deux une contrainte. Ils "
            "ne se ressemblent pas par la construction. Empêcher DE, obliger À — "
            "l'apprendre comme un couple, jamais séparément.",
            notes="Faire écrire les deux au tableau et les y laisser jusqu'à la fin "
                  "du module : ils reviennent dans les deux lettres du bloc D.")

    d.pratique('Pratique', "Complétez la conséquence",
               "Un mot par trou. Attention à la préposition.", [
        ("Le tapis démarre à 5 h 45. Cela m'___ de dormir plus de quatre heures.", "empêche"),
        ("Je suis réveillée avant l'aube. Cela m'___ à me lever à cinq heures trente.", "oblige"),
        ("La chambre est sous l'appareil. Cela m'___ d'utiliser ma propre chambre.", "empêche"),
        ("Avant février, je me rendormais ___ dix minutes.", "en"),
        ("Il court ___ quarante minutes, tous les matins de semaine.", "pendant"),
        ("Il part à l'atelier ___ la journée.", "pour"),
        ("Je note la date et l'heure ___ le 4 février.", "depuis"),
    ], corrige=True,
       notes="Faire relire les sept phrases à la suite après la correction : mises "
             "bout à bout, elles font le premier paragraphe de la lettre du bloc D.")

    d.billet(
        "Écris une conséquence vraie, chez toi, avec un chiffre dedans.",
        exemples=[
            "Commence par « Cela m'empêche de » ou « Cela m'oblige à ».",
            "Un chiffre ou une date, pas un adjectif.",
        ],
        notes="Deux minutes. Ramasser : ceux qui écrivent encore un adjectif auront "
              "besoin d'un rappel en D2, au moment de la lettre.")

    return d.save(dossier)
