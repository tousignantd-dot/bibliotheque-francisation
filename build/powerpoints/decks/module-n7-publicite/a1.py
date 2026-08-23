# -*- coding: utf-8 -*-
"""A1 · Cent quatre-vingt-neuf dollars pour neuf quatre-vingt-dix-neuf
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

import pathlib

# Chemin déduit du fichier, jamais écrit en dur : le dépôt est aussi construit
# depuis un worktree git, où un chemin absolu vers la copie principale
# pointerait sur des images qui n'y sont pas encore.
IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-publicite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Neuf quatre-vingt-dix-neuf, et la facture dit cent quatre-vingt-neuf",
        chapeau="Une annonce peut être exacte mot à mot et fausse dans son "
                "ensemble. C'est là-dessus que porte tout le module : sur ce "
                "que l'annonce vous laisse conclure sans jamais l'écrire.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "avez-vous déjà payé plus cher que le prix annoncé ? Les exemples "
                  "sortent vite — abonnements, forfaits de téléphone, meubles. "
                  "C'est la matière du module.")

    d.objectifs([
        "nommer les pièces d'une annonce : slogan, mention légale, astérisque ;",
        "distinguer ce qu'une annonce affirme de ce qu'elle laisse conclure ;",
        "savoir qu'au Québec une annonce se juge sur l'impression générale ;",
        "employer les premiers mots du dossier : un message implicite, un "
        "public cible, un annonceur.",
    ], notes="Le deuxième objectif est le cœur du module et il ne sera pas atteint "
             "aujourd'hui. Le poser quand même : les quinze séances y reviennent.")

    d.declencheur(
        'Observation', "Où la publicité vous a-t-elle rejoint cette semaine ?",
        image=IMG + 'abribus-soir.jpg',
        pistes=[
            "À la radio, dans l'autobus, dans votre boîte aux lettres ?",
            "Combien de fois avez-vous vu la même annonce ?",
            "Y en a-t-il une dont vous vous souvenez sans le vouloir ?",
            "Avez-vous déjà acheté quelque chose à cause d'une annonce ?",
        ],
        notes="Question sans mauvaise réponse. La troisième piste est la plus utile : "
              "se souvenir sans l'avoir voulu, c'est exactement ce que l'affichage "
              "achète. Ne pas conclure à leur place.")

    d.dialogue('Dialogue · 1 de 3', "Une facture qui ne concorde pas", [
        ("YAMILÉ", "J'ai pris un abonnement au centre de la rue Parent. L'annonce disait neuf quatre-vingt-dix-neuf par semaine.", True),
        ("YAMILÉ", "Le premier relevé dit cent quatre-vingt-neuf dollars. Trois semaines à dix dollars, ça fait trente, pas cent quatre-vingt-neuf.", True),
        ("RÉGINALD", "Non. Ça fait trente dollars, plus quelque chose que l'annonce ne vous a pas dit.", True),
        ("YAMILÉ", "Il y a une grosse ligne, une photo, et une étoile après le prix.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Laisser le groupe faire le calcul au tableau avant de continuer. "
             "L'écart de cent cinquante-neuf dollars est ce qui accroche la classe.")

    d.dialogue('Dialogue · 2 de 3', "Trente ans à écrire des annonces", [
        ("RÉGINALD", "Je vais vous dire une chose que j'ai passé trente ans à faire, et je ne suis pas très fier de toutes les années.", True),
        ("RÉGINALD", "J'ai écrit de la publicité. Des annonces de radio, surtout. Des centaines.", True),
        ("RÉGINALD", "Et je vais vous apprendre à les lire, parce que ça s'apprend.", True),
        ("RÉGINALD", "Ce n'est pas de l'intuition, c'est un métier avec des règles, et il y a des lois qui l'encadrent.", True),
    ], notes="Point de posture, à ne pas manquer : le module n'apprend pas à se "
             "méfier, il apprend un métier vu de l'intérieur. Réginald n'est ni un "
             "repenti ni un dénonciateur.")

    d.dialogue('Dialogue · 3 de 3', "L'impression générale", [
        ("YAMILÉ", "Mais si chaque mot est vrai, où est le problème ?", True),
        ("RÉGINALD", "Au Québec, on ne juge pas une annonce mot par mot. La loi regarde l'impression générale qu'elle donne.", True),
        ("RÉGINALD", "Si l'impression générale est fausse, l'annonce est trompeuse, même si chaque mot pris tout seul est exact.", True),
        ("RÉGINALD", "Et le commerçant n'a pas le droit d'omettre un fait important.", True),
    ], notes="Les deux règles de la séance, dites par un personnage. Les écrire au "
             "tableau et les y laisser jusqu'à E2. Aucun numéro d'article : ce n'est "
             "pas un cours de droit.")

    d.tableau('Analyse', "Quatre pièces, quatre travaux",
              ['La pièce', 'Ce qu\'elle fait'],
              [["Le slogan",
                "se faire retenir en trois ou quatre mots, toujours les mêmes"],
               ["La mention légale",
                "dire, parce que la loi l'oblige, ce que le reste a passé sous silence"],
               ["L'astérisque",
                "renvoyer d'une promesse à la condition écrite plus bas"],
               ["Le message implicite",
                "faire conclure quelque chose sans jamais l'affirmer"]],
              cle=0,
              note="Trois de ces quatre pièces sont visibles. La quatrième ne l'est pas.",
              notes="Diapositive à photographier. Insister sur la quatrième : elle "
                    "n'occupe aucune place sur la page, et c'est elle qui travaille.")

    d.regle("On juge l'effet, pas les mots",
            "Une annonce se juge sur l'impression générale qu'elle donne, "
            "et non sur chaque mot pris à part.",
            precision="Une annonce dont toutes les phrases sont exactes peut donc "
                      "être trompeuse, si l'ensemble fait croire autre chose. Et le "
                      "commerçant n'a pas le droit d'omettre un fait important : le "
                      "silence n'est pas une défense.",
            notes="Diapositive à photographier. Question fréquente : « alors on peut "
                  "se plaindre même s'ils n'ont pas menti ? » Oui, et c'est le point.")

    d.vocabulaire('Vocabulaire', "Six mots pour commencer", [
        ("un message implicite", "Ce qu'une annonce fait comprendre sans jamais l'écrire ni le dire."),
        ("un slogan", "La courte phrase qu'une entreprise répète partout pour qu'on la retienne."),
        ("un public cible", "Le groupe de personnes qu'une annonce cherche à atteindre."),
        ("un annonceur", "L'entreprise ou l'organisme qui paie pour faire passer un message."),
        ("un abribus", "Le petit abri vitré où l'on attend l'autobus, dont un côté sert de support à des annonces."),
        ("un panneau-réclame", "Le grand panneau installé au bord d'une route pour qu'on le voie en roulant."),
    ], notes="Faire répéter avec l'article. « Implicite » est le mot du module : le "
             "faire dire trois fois, il reviendra à chaque séance.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Yamilé a payé cent quatre-vingt-neuf dollars pour trois semaines.", "vrai"),
        ("Réginald a travaillé trente ans dans une agence de publicité.", "vrai"),
        ("Selon Réginald, l'annonce a écrit une chose fausse.", "faux - chaque mot est exact"),
        ("Au Québec, une annonce se juge mot par mot.", "faux - sur l'impression générale"),
        ("Omettre un fait important est permis si le reste est exact.", "faux - c'est interdit"),
        ("L'étoile après le prix renvoie à une condition écrite plus bas.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le troisième est "
             "le plus difficile : rien n'est faux, et pourtant l'annonce est en cause.")

    d.billet(
        "Nommez une annonce que vous avez vue cette semaine, et dites ce qu'elle promet.",
        exemples=[
            "Où l'avez-vous vue, et combien de fois ?",
            "Qu'est-ce qu'elle promet exactement, en une phrase ?",
        ],
        notes="Devoir concret. Les réponses servent de matière première tout le "
              "module : chaque élève arrive avec une annonce à démonter, et c'est "
              "celle qu'il présentera en E1.")

    return d.save(dossier)
