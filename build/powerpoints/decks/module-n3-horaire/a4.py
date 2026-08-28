# -*- coding: utf-8 -*-
"""A4 · Les moments de la journée.
Bloc A « Je découvre » · couleur ambre (écriture) · 60 min.
Source : exercice `prMoments`, mini-leçon `prMoments`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Les moments de la journée",
        chapeau="Le matin, le midi, l'après-midi, le soir. Quatre mots, et "
                "une petite lettre qui change tout : « je travaille le "
                "lundi » n'est pas « je travaille lundi ».",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture, dernière du bloc A. Elle prépare directement le "
                  "défi 1 : on ne peut pas lire un horaire sans savoir dire à quel "
                  "moment de la journée on travaille.")

    d.objectifs([
        "nommer les quatre moments d'une journée de travail ;",
        "distinguer « le matin » et « ce matin » ;",
        "distinguer « lundi » et « le lundi » ;",
        "dire ce qu'une case vide veut dire sur un horaire.",
    ])

    d.tableau('Analyse', "Quatre moments, et rien de plus",
              ["Le moment", "À peu près quand"],
              [["le matin", "de six heures à onze heures"],
               ["le midi", "autour de midi"],
               ["l'après-midi", "de treize heures à dix-sept heures"],
               ["le soir", "après dix-huit heures"]],
              cle=1,
              note="Un quart de travail se dit presque toujours avec l'un "
                   "de ces quatre mots, avant même de donner les heures.",
              notes="Diapo à photographier. Faire dire à chacun son propre moment : "
                    "« je travaille le soir », « j'étudie l'après-midi ». La phrase "
                    "complète, pas le mot seul.")

    d.regle("« Le » veut dire : chaque fois",
            "Je travaille le matin. — Je travaille ce matin.",
            precision="La première phrase parle d'une habitude : tous les "
                      "matins. La seconde parle d'aujourd'hui seulement. Un "
                      "seul petit mot les sépare, et un chef d'équipe "
                      "n'entendra pas la même chose.",
            notes="Diapo à photographier. Faire produire les deux versions pour chaque "
                  "élève, à partir de son vrai horaire. C'est là que la différence "
                  "s'installe, pas dans l'explication.")

    d.regle("Lundi, ou le lundi",
            "Je travaille lundi. — Je travaille le lundi.",
            precision="Sans « le » : ce lundi-ci, celui qui vient. Avec "
                      "« le » : tous les lundis, c'est mon horaire "
                      "habituel. La même règle que pour le matin.",
            notes="Diapo à photographier. Le piège se joue à l'oral aussi : « le lundi » "
                  "et « lundi » se distinguent mal quand on parle vite. Faire répéter "
                  "lentement.")

    d.pratique('Écriture', "Le matin, le midi, l'après-midi ou le soir ?",
               "Complétez d'après l'horaire de Fabiola et de Miguel.", [
        ("Le quart de Fabiola commence à six heures : elle travaille ___ .", "le matin"),
        ("Miguel entre à quatorze heures : il travaille ___ .", "l'après-midi"),
        ("Miguel finit à vingt-deux heures : il travaille aussi ___ .", "le soir"),
        ("La pause de onze heures et demie, c'est presque ___ .", "le midi"),
        ("Samedi, rien n'est écrit sur sa ligne : Fabiola est en ___ .", "congé"),
    ], corrige=True,
       notes="C'est l'exercice `prMoments` du module interactif, mot pour mot. La "
             "dernière ligne est la plus importante du module : une case vide veut dire "
             "congé, et ça ne s'écrit jamais.")

    d.regle("Ce qui n'est pas écrit",
            "Une case vide sur l'horaire veut dire congé.",
            precision="Personne n'écrit le mot « congé » sur un tableau de "
                      "personnel : on le lit dans le vide. C'est la seule "
                      "information d'un horaire qui se comprend par "
                      "l'absence.",
            notes="Diapo à photographier. Beaucoup d'élèves cherchent une confirmation "
                  "écrite et n'osent pas demander. Leur dire qu'ils peuvent demander — "
                  "« samedi, je suis en congé, c'est bien ça ? » — vaut la séance "
                  "entière.")

    d.pratique('Écriture', "Habitude, ou aujourd'hui ?",
               "Écrivez « le » quand il s'agit d'une habitude.", [
        ("Je travaille ___ matin, de six heures à quatorze heures. (toutes les semaines)", "le matin"),
        ("___ matin, je commence plus tôt : à cinq heures. (aujourd'hui)", "Ce matin"),
        ("Je prends ma pause ___ midi. (chaque jour)", "le midi"),
        ("___ après-midi, je finis à quatorze heures. (aujourd'hui)", "Cet après-midi"),
        ("Miguel travaille ___ soir. (son quart habituel)", "le soir"),
        ("Je ne travaille pas ___ mercredi. (tous les mercredis)", "le mercredi"),
    ], corrige=True,
       notes="Faire lire la parenthèse avant d'écrire : c'est elle qui donne la réponse, "
             "et c'est le raisonnement qu'il faut installer, pas la forme.")

    d.billet(
        "Écrivez votre semaine, en cinq lignes.",
        exemples=[
            "Un jour par ligne, avec le moment de la journée.",
            "« Lundi : je travaille le matin, de 7 h à 15 h. »",
        ],
        notes="Devoir court. Ramasser : cette semaine écrite servira de matière au "
              "défi 1, où chacun lira son propre horaire au lieu de celui de Fabiola.")

    return d.save(dossier)
