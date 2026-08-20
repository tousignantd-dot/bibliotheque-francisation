# -*- coding: utf-8 -*-
"""C1 · Les consignes du moniteur.
Bloc C « Défi 2 · Comprendre et donner des consignes » · couleur acier · 60 min.
Source : dialogue `t2`, exercices `t2vf` et `t2suivi`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-activite/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Les consignes du moniteur',
        chapeau="Au bord de la piscine, Kevin parle vite et court. "
                "« Prenez-la. » « Ne la lâchez pas. » « Mets-toi là. » Huit "
                "consignes en deux minutes, et il faut suivre.",
        duree='60 minutes')

    d.titre(notes="Ouverture du bloc C. Prévenir le groupe : ce dialogue est volontairement "
                  "rapide. On va l'écouter trois fois, et c'est normal de ne pas tout "
                  "saisir la première.")

    d.objectifs([
        "comprendre une consigne dite vite, dans le bruit ;",
        "distinguer une consigne affirmative d'une consigne négative ;",
        "reconnaître ce que le petit mot remplace : la planche, les enfants ;",
        "vérifier si une consigne a été suivie ou non.",
    ])

    d.declencheur(
        'Observation', "Que vont faire ces enfants dans les prochaines minutes ?",
        image=IMG + 'planches.jpg',
        pistes=[
            "À quoi sert cet objet ?",
            "Comment doit-on le tenir, selon vous ?",
            "Quelles consignes de sécurité imaginez-vous au bord d'une piscine ?",
            "Qu'est-ce qui est interdit, presque toujours ?",
        ],
        notes="Les élèves connaissent presque tous les règles de base — ne pas courir, ne "
              "pas sauter, ne pas pousser. Faire sortir le vocabulaire avant l'écoute.")

    d.dialogue('Dialogue · 1 de 2', "Se placer", [
        ("KEVIN", "Tout le monde s'assoit au bord ! Les pieds dans l'eau, on ne saute pas.", True),
        ("KEVIN", "Mateo, mets-toi à côté de Sofia. Non, ne te lève pas, reste assis.", True),
        ("KEVIN", "Prenez la planche à deux mains. Tenez-la bien devant vous, ne la lâchez pas.", True),
    ], consigne="Écoutez trois fois, diapo masquée. La première fois, ne notez rien.",
       notes="Trois écoutes : la première pour l'ensemble, la deuxième pour repérer les "
             "verbes, la troisième pour les détails. Annoncer le plan avant de commencer.")

    d.dialogue('Dialogue · 2 de 2', "Faire, et refaire", [
        ("KEVIN", "Mateo, regarde-moi. Souffle dans l'eau, comme ça. Ne ferme pas les yeux.", True),
        ("KEVIN", "Très bien ! Recommence, mais plus lentement cette fois.", False),
        ("KEVIN", "On se replace en ligne. Laissez la planche au bord, ne la jetez pas dans l'eau.", True),
        ("KEVIN", "Dernier tour, et après on sort. Sortez par l'échelle, pas par le bord.", True),
    ], notes="« Regarde-moi » et « ne ferme pas les yeux » se suivent : une consigne "
             "affirmative, une négative. C'est exactement le contraste de la séance C2.")

    d.tableau('Analyse', "Ce que le petit mot remplace",
              ['La consigne', 'Le mot remplacé'],
              [["Tenez-la bien devant vous.", "la planche"],
               ["Ne la lâchez pas.", "la planche"],
               ["Regarde-moi.", "le moniteur"],
               ["Ne les jetez pas dans l'eau.", "les planches"]],
              cle=0,
              note="Le petit mot change de place selon que la consigne est affirmative ou négative.",
              notes="Ne pas expliquer la règle ici : la faire seulement remarquer. C2 s'en "
                    "charge. Faire trouver le mot remplacé par le groupe.")

    d.cartes('Les consignes de sécurité', "Quatre interdits universels", [
        ("Ne pas courir",
         "Au bord d'une piscine, le plancher est toujours mouillé. C'est la consigne la "
         "plus répétée de tous les centres sportifs."),
        ("Ne pas sauter",
         "Sauf aux endroits prévus. « On ne saute pas » se dit à l'indicatif, mais c'est "
         "un ordre."),
        ("Ne pas pousser",
         "Dans l'eau comme sur le bord. Souvent dit sous la forme « on ne pousse pas »."),
        ("Sortir par l'échelle",
         "Pas en se hissant sur le bord : c'est là que se produisent les blessures aux "
         "côtes et aux poignets."),
    ], notes="Ces quatre consignes valent dans toutes les piscines publiques du Québec. "
             "Elles sont affichées, mais rarement lues.")

    d.regle("Une consigne dite vite reste une consigne",
            "Si vous n'avez pas compris, demandez : « Pardon ? »",
            precision="Un moniteur répète volontiers, et souvent plus lentement. Ce qui "
                      "est dangereux, c'est de faire semblant d'avoir compris — au bord "
                      "d'une piscine, une consigne manquée est une question de sécurité, "
                      "pas de politesse.",
            notes="Faire répéter la phrase par le groupe. Elle reviendra en D2 avec le "
                  "registre.")

    d.pratique('Pratique', "La consigne est-elle suivie ?",
               "Le moniteur a dit ceci. L'enfant fait cela. Est-ce correct ?", [
        ("« Ne saute pas. » — Il s'assoit au bord.", "oui"),
        ("« Tenez-la bien devant vous. » — Il la tient d'une main.", "non"),
        ("« Ne te lève pas. » — Il se lève pour mieux voir.", "non"),
        ("« Souffle dans l'eau. » — Il souffle, les yeux ouverts.", "oui"),
        ("« Laissez la planche au bord. » — Il la dépose sur le rebord.", "oui"),
        ("« Sortez par l'échelle. » — Il se hisse par le bord.", "non"),
    ], corrige=True, cols=1,
       notes="Faire justifier chaque « non » en citant la consigne. C'est de la "
             "compréhension fine, pas de la mémoire.")

    d.billet(
        "Notez quatre consignes que vous entendez souvent dans une activité.",
        exemples=[
            "Au travail, à l'école de vos enfants, dans un cours.",
            "Deux affirmatives, deux négatives.",
        ],
        notes="Les relevés servent d'entrée en matière à C2, où la place du pronom sera "
              "expliquée.")

    return d.save(dossier)
