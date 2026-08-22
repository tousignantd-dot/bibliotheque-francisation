# -*- coding: utf-8 -*-
"""B4 · Amorcer, et reprendre sans répéter
Bloc B « Défi 1 » · couleur framboise · 75 min. Conventions et grammaire du texte.
Source : exercices `t1amorce` et `t1repr`, leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='framboise',
        titre="Amorcer, et reprendre sans répéter",
        chapeau="Deux gestes qui n'ont l'air de rien : entrer dans une "
                "conversation, et redire la même chose sans employer le même "
                "mot. Ce sont eux qui tiennent un échange debout.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1. Elle réunit une compétence de "
                  "conversation et un savoir de grammaire du texte : les deux "
                  "servent la même chose, faire tenir un échange ensemble.")

    d.objectifs([
        "amorcer une conversation avec un inconnu, sans rien demander de privé ;",
        "reprendre un mot de l'autre pour montrer qu'on écoutait ;",
        "reprendre un référent en changeant seulement le déterminant ;",
        "reprendre un référent en changeant de mot.",
    ], notes="Les deux premiers objectifs se pratiquent debout, en circulant. Les "
             "deux derniers s'écrivent. Prévoir la bascule au milieu de la séance.")

    d.declencheur(
        'Observation', "Relisez vos phrases d'ouverture de mardi",
        pistes=[
            "Est-ce qu'elle demande quelque chose de privé ?",
            "Est-ce qu'on peut y répondre en un seul mot ?",
            "Est-ce qu'elle laisse à l'autre le choix de continuer ?",
        ],
        notes="Projeter trois ou quatre billets de B1, sans nommer les auteurs, et "
              "les faire évaluer par les trois questions. C'est la meilleure entrée "
              "en matière possible : les exemples viennent du groupe.")

    d.tableau('Analyse', "Sept phrases, sept travaux",
              ['La phrase', 'Ce qu\'elle fait'],
              [["Vous attendez ?", "ouvrir sur ce qui est commun aux deux"],
               ["Ah, tout ce temps-là ?", "reprendre un mot pour montrer qu'on écoutait"],
               ["Chez nous, c'était pareil.", "donner un peu de soi"],
               ["Fatiguée comment ?", "demander une précision, une fois l'autre lancé"],
               ["Ça, c'est une bonne nouvelle.", "réagir avant d'enchaîner sur soi"]],
              cle=0,
              note="Et pour finir : « Bon, ils vous appellent. Bonne chance. » On termine sans se justifier.",
              notes="Diapositive à photographier. La note du bas porte la septième "
                    "phrase : le tableau refuserait six rangées avec une note aussi "
                    "longue, et la fin de conversation mérite d'être isolée.")

    d.regle("On donne un peu avant de demander",
            "Questionner sans rien dire de soi donne l'impression d'un interrogatoire.",
            precision="« Chez nous, c'était pareil avec mon père » libère l'autre : "
                      "il peut raconter à son tour, ou non. C'est ce qui distingue "
                      "une conversation d'une enquête, et ça s'apprend en une phrase.",
            notes="Diapositive à photographier. Plusieurs élèves posent beaucoup de "
                  "questions par politesse, sans rien dire d'eux, et s'étonnent que "
                  "l'échange retombe.")

    d.pratique('Conversation', "Debout, deux minutes chacun",
               "Amorcez, reprenez un mot, donnez un peu de vous, terminez.", [
        ("Vous attendez à l'urgence, un samedi soir.", ""),
        ("Vous attendez à la pharmacie, avant la fermeture.", ""),
        ("Vous attendez l'autobus, en février.", ""),
        ("Vous attendez au comptoir d'un centre de services.", ""),
    ],
       notes="Vingt minutes. Faire circuler : chacun rencontre trois personnes "
             "différentes. Passer sans corriger la langue ; noter seulement qui "
             "n'arrive pas à terminer, c'est ce qui manque le plus souvent.")

    d.tableau('Analyse', "Reprendre en changeant le déterminant",
              ['Première phrase', 'La reprise'],
              [["Une fatigue est apparue.", "Cette fatigue n'est jamais repartie."],
               ["Elle a attendu sept mois.", "Ce délai lui a paru interminable."],
               ["Gilles accompagne sa femme.", "Sa patience étonne tout le monde."],
               ["Ils se parlent le dimanche.", "Leurs appels durent une heure."]],
              cle=0,
              note="Passer de « une » à « cette » ou à « la » dit que la chose a déjà été présentée.",
              notes="Diapositive à photographier. Faire remarquer que le nom, lui, ne "
                    "change pas : seul le petit mot devant bouge. C'est la reprise la "
                    "plus simple et la plus fréquente.")

    d.tableau('Analyse', "Reprendre en changeant de mot",
              ['Le moyen', 'Un exemple'],
              [["Un synonyme", "un rendez-vous devient une rencontre"],
               ["Un mot plus général", "une échographie devient cet examen"],
               ["Le nom tiré du verbe", "il a fallu attendre devient cette attente"]],
              cle=0,
              note="Quand aucun synonyme ne vient, montez d'un cran : cet examen, cette démarche, ce papier.",
              notes="Diapositive à photographier. Le mot plus général est la "
                    "technique qui sauve, et c'est celle que les élèves oublient le "
                    "plus vite.")

    d.piege('Écriture',
            "la docteure a expliqué, la docteure a demandé, la docteure a dit",
            "elle a expliqué, puis elle a demandé des examens",
            "Le texte n'est pas faux : il est illisible. Reprendre autrement "
            "n'est pas une élégance de style, c'est ce qui permet au lecteur de "
            "savoir qu'on parle encore de la même chose sans le lui répéter à "
            "chaque phrase.",
            notes="Projeter le mauvais exemple en entier avant de le corriger : "
                  "l'effet de lourdeur se sent immédiatement et personne n'a besoin "
                  "d'explication.")

    d.pratique('Grammaire', "Reprenez sans répéter",
               "Complétez la deuxième phrase.", [
        ("Une fatigue est apparue en février. ___ fatigue n'est jamais repartie.", "Cette"),
        ("Elle a attendu sept mois. ___ délai lui a paru interminable.", "Ce"),
        ("On a demandé deux examens. ___ examens se font en bas.", "Ces"),
        ("Il a fallu attendre la matinée. Cette ___ est la partie la plus dure.", "attente"),
        ("Elle est arrivée en retard. Ce ___ n'a rien changé.", "retard"),
    ], corrige=True,
       notes="Les deux derniers sont des noms tirés d'un verbe : c'est l'entrée du "
             "Défi 3, où toute la question sera de passer de la parole à l'écrit. "
             "L'annoncer en corrigeant.")

    d.billet(
        "Écrivez deux phrases sur le rendez-vous de Leyla, sans répéter de mot.",
        exemples=[
            "Première phrase : ce qui est arrivé.",
            "Deuxième phrase : reprenez-le autrement.",
        ],
        notes="Cinq minutes. Ramasser et relire trois billets à la séance suivante : "
              "la reprise se corrige mieux sur des phrases d'élèves que sur des "
              "phrases de manuel.")

    return d.save(dossier)
