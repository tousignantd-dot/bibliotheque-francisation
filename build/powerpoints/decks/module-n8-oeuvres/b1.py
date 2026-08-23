# -*- coding: utf-8 -*-
"""B1 · La finale des « Eaux basses »
Bloc B « Défi 1 · La dernière scène » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t11`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-oeuvres' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="La finale des « Eaux basses »",
        chapeau="Deux personnes ont vu exactement la même scène. Elles "
                "s'entendent sur tout ce qui s'y passe, et elles n'en tirent "
                "pas la même histoire.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 1. Le module bascule ici : jusqu'à présent on "
                  "apprenait à séparer trois opérations, maintenant on s'en sert "
                  "devant une œuvre entière.")

    d.objectifs([
        "suivre une conversation de vingt-huit répliques sur une seule scène ;",
        "décrire une scène sans l'interpréter — plus difficile qu'il n'y paraît ;",
        "distinguer une fin ouverte d'une fin à laquelle il manquerait quelque chose ;",
        "relever les indices d'une scène et dire à quelle lecture ils servent.",
    ], notes="Le deuxième objectif est celui qu'on rate. Demandez à quelqu'un de "
             "raconter la scène : il dira « elle renonce » avant d'avoir dit « elle "
             "s'assoit ».")

    d.declencheur(
        'Observation', "Décrivez cette photo sans rien deviner",
        image=IMG + 'taquet-corde.jpg',
        pistes=[
            "Que voit-on, exactement ? Nommez trois choses.",
            "Combien de tours la corde fait-elle ?",
            "Est-ce qu'on peut dire d'ici si quelqu'un va partir ?",
            "Qu'est-ce qui vous ferait le dire ?",
        ],
        notes="Exercice de description pure, deux minutes. La troisième piste est le "
              "point : rien dans l'image ne dit ce qui va se passer, et pourtant "
              "chacun a déjà une idée.")

    d.dialogue('Dialogue · 1 de 3', "Racontez-moi la scène", [
        ("LÉANDRE", "Six épisodes pour arriver à ça. Ils ont manqué de temps, c'est tout.", True),
        ("FATOUMATA", "Racontez-moi la dernière scène. Juste ce qui s'y passe, sans dire ce que vous en pensez.", True),
        ("LÉANDRE", "Estelle sort du chalet. Elle descend au quai, elle retourne la chaloupe, elle la remet à l'eau. Elle s'assoit dedans.", True),
        ("FATOUMATA", "Vous avez oublié deux choses.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="La consigne de Fatoumata est celle de la séance. La répéter au groupe "
             "avant la deuxième écoute : ce qui s'y passe, sans ce qu'on en pense.")

    d.dialogue('Dialogue · 2 de 3', "Les deux choses oubliées", [
        ("FATOUMATA", "Avant de descendre, elle met les bottes de caoutchouc de sa mère.", True),
        ("FATOUMATA", "Et la corde de la chaloupe reste attachée au taquet du quai.", True),
        ("LÉANDRE", "La corde... c'est vrai. Elle ne la détache pas.", True),
        ("FATOUMATA", "Elle est assise dans une chaloupe qui ne peut pas partir.", True),
    ], notes="Les deux indices oubliés sont ceux qui portent les deux lectures. "
             "Coïncidence ? Non : on oublie ce qui ne sert pas la lecture qu'on a "
             "déjà. Le dire au groupe, mais seulement en B2.")

    d.dialogue('Dialogue · 3 de 3', "Fin ouverte ou fin manquante", [
        ("LÉANDRE", "Et vous appelez ça une fin ? Moi j'appelle ça un épisode qu'on n'a pas fini de tourner.", True),
        ("FATOUMATA", "C'est une fin ouverte. Ce n'est pas la même chose qu'une fin manquante.", True),
        ("FATOUMATA", "Une fin manquante, c'est quand il manque un renseignement et que personne ne peut le deviner.", True),
        ("FATOUMATA", "Une fin ouverte, c'est quand on a tout ce qu'il faut, et que ce qu'on en fait dépend de nous.", True),
    ], notes="Distinction centrale du défi, et elle vaut hors du cours : beaucoup de "
             "gens quittent une série en disant « ils n'ont pas fini ». Écrire les "
             "deux définitions au tableau.")

    d.tableau('Analyse', "Ce que la scène montre, en six lignes",
              ['Le geste', 'Ce qu\'on vérifie'],
              [["Les bottes", "celles de ville enlevées"],
               ["La chaloupe", "retournée, remise à l'eau"],
               ["La corde", "restée attachée au taquet"],
               ["Le téléphone", "il sonne ; elle ne répond pas"],
               ["La lampe", "elle s'allume seule"],
               ["Le plan", "quatorze secondes"]],
              cle=0,
              notes="Diapositive à photographier, et à garder affichée pendant tout le "
                    "bloc B : six faits, aucune interprétation. C'est le terrain "
                    "commun, et la liste sur laquelle B2, B3 et B4 travaillent.")

    d.regle("Une fin ouverte n'est pas une fin manquante",
            "Une fin manquante retient un renseignement. Une fin ouverte vous "
            "donne tout et vous laisse conclure.",
            precision="La différence est vérifiable : dans une fin manquante, personne "
                      "ne peut deviner, faute d'information. Dans une fin ouverte, "
                      "deux personnes peuvent défendre deux conclusions — parce que "
                      "les deux ont tout ce qu'il faut.",
            notes="Diapositive à photographier. Confondre les deux fait passer un "
                  "choix d'auteur pour une paresse, et c'est exactement ce que fait "
                  "Léandre au début.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Fatoumata a regardé la finale deux fois.", "vrai"),
        ("Estelle détache la corde avant de s'asseoir.", "faux - elle la laisse"),
        ("C'est Estelle qui allume la lumière du quai.", "faux - elle s'allume seule"),
        ("Le plan des bottes dure quatorze secondes.", "vrai"),
        ("Fatoumata reconnaît qu'un de ses arguments est mauvais.", "vrai"),
        ("Léandre accepte que sa remarque soit une lecture.", "faux - il s'en défend"),
    ], corrige=True,
       notes="Exercice `t11` du module. Faire justifier chaque « faux » par la "
             "réplique exacte : c'est l'entraînement au retour au texte, qui servira "
             "en C2 et en D2.")

    d.billet(
        "Revoyez en pensée la fin d'une œuvre que vous connaissez et écrivez "
        "quatre faits, sans aucune interprétation.",
        exemples=[
            "Un geste, un objet, un mot dit, un son.",
            "Interdiction d'employer « il veut », « elle pense », « ils décident ».",
        ],
        notes="L'interdiction du deuxième exemple est le vrai exercice. Les copies "
              "qui la respectent sont rares à la première tentative.")

    return d.save(dossier)
