# -*- coding: utf-8 -*-
"""A2 · Les consonnes qui tombent en fin de mot.
Bloc A · couleur violet (graphie-phonie) · 60 min.
Source : exercice `prPhon` — le l, le r et le t finaux à l'oral.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='violet',
        titre='Les consonnes qui tombent',
        chapeau="« Possible », « quatre », « exact ». À l'écrit, la consonne finale est "
                "là. À l'oral, au Québec, elle disparaît souvent — et c'est pour ça "
                "qu'on ne reconnaît pas le mot.",
        duree='60 minutes')

    d.titre(notes="Dire « c'est pas possib' » et « c'est pas possible » à voix haute. "
                  "Demander au groupe s'il entend la même chose. La leçon commence là.")

    d.objectifs([
        "reconnaître un mot dont la consonne finale n'est pas prononcée ;",
        "savoir quelles consonnes tombent le plus souvent ;",
        "comprendre un débit rapide sur un chantier ;",
        "écrire correctement un mot qu'on entend sans sa consonne finale.",
    ])

    d.regle('La règle',
            "En parlant vite, la consonne finale après une autre consonne tombe souvent.",
            precision="Possible se dit « possib' ». Quatre se dit « quat' ». Autre se "
                      "dit « aut' ». Ce n'est pas une faute : c'est le français parlé "
                      "ordinaire, au Québec comme en France.",
            notes="Le dire clairement : ce n'est pas du mauvais français. Beaucoup "
                  "d'élèves croient qu'on leur parle mal, alors qu'on leur parle "
                  "normalement.")

    d.tableau('Analyse', "À l'écrit et à l'oral",
              ["À l'écrit", "À l'oral, souvent"],
              [["possible", "possib'"],
               ["autre", "aut'"],
               ["quatre", "quat'"],
               ["membrane", "membrane — la consonne reste"],
               ["exact", "exac'"]],
              cle=0,
              note="La quatrième ligne montre la limite : quand la consonne est suivie "
                   "d'une voyelle, elle reste.",
              notes="Faire lire les deux colonnes. La différence s'entend surtout dans "
                    "les mots de deux syllabes ou plus.")

    d.cartes('Analyse', "Quand la consonne tombe, et quand elle reste", [
        ("Elle tombe · devant une consonne",
         "« Quatre couvreurs » se dit « quat' couvreurs ». La consonne finale tombe "
         "parce que le mot suivant commence par une consonne."),
        ("Elle reste · devant une voyelle",
         "« Quatre échelles » se dit « quatr' échelles ». Le r se rattache à la voyelle "
         "qui suit."),
        ("Elle tombe · à la fin d'une phrase",
         "« C'est pas possible. » se dit souvent « c'est pas possib' ». Il n'y a rien "
         "après pour retenir la consonne."),
        ("Le t final",
         "« Exact », « strict », « correct » perdent souvent leur t. « Exactement », "
         "lui, garde tout : la suite du mot le retient."),
    ], notes="La deuxième carte est la clé : c'est ce qui suit qui décide. Le faire "
             "vérifier sur quatre exemples au tableau.")

    d.pratique('Pratique · 1 de 4', "Écrivez le mot entier",
               "Vous entendez la forme courte. Comment l'écrit-on ?", [
        ("« acceptab' »", "acceptable"),
        ("« chapit' »", "chapitre"),
        ("« exac' »", "exact"),
        ("« tab' »", "table"),
        ("« théât' »", "théâtre"),
        ("« memb' »", "membre"),
    ], corrige=True,
       notes="C'est l'exercice le plus utile du module pour la compréhension orale : "
             "reconstruire le mot écrit à partir de ce qu'on entend.")

    d.pratique('Pratique · 2 de 4', "La consonne tombe-t-elle ?",
               "Regardez ce qui suit le mot.", [
        ("quatre couvreurs", "elle tombe — consonne après"),
        ("quatre échelles", "elle reste — voyelle après"),
        ("possible aujourd'hui", "elle reste — voyelle après"),
        ("possible demain", "elle tombe — consonne après"),
        ("un autre toit", "elle tombe — consonne après"),
    ], corrige=True,
       notes="Faire dire chaque groupe à voix haute, vite. Le groupe entendra lui-même "
             "la différence.")

    d.piege("Le piège du mot non reconnu",
            "Vous entendez « quat' » et vous cherchez un mot nouveau.",
            "C'est « quatre », prononcé vite.",
            "La plupart des mots qu'on ne reconnaît pas à l'oral ne sont pas des mots "
            "inconnus : ce sont des mots connus, prononcés autrement. Avant de chercher "
            "un mot nouveau, essayez d'ajouter la consonne finale.",
            notes="Conseil de méthode qui débloque beaucoup d'élèves. Le donner "
                  "explicitement comme une stratégie d'écoute.")

    d.piege("Le piège de l'écriture",
            "Vous écrivez « quat » parce que vous l'entendez ainsi.",
            "À l'écrit, la consonne finale est toujours là.",
            "Ce qui tombe à l'oral ne tombe jamais à l'écrit. « Possible », « quatre », "
            "« autre » s'écrivent toujours en entier. C'est une des différences les plus "
            "marquées entre le français parlé et le français écrit.",
            notes="Faire écrire les six mots de l'exercice 1 dans le cahier, en entier. "
                  "C'est la forme écrite qu'on retient.")

    d.pratique('Pratique · 3 de 4', "Écoutez et écrivez la phrase",
               "Écrivez tous les mots en entier.", [
        ("« C'est pas possib' de monter aujourd'hui. »",
         "Ce n'est pas possible de monter aujourd'hui."),
        ("« On a quat' jours de retard. »", "On a quatre jours de retard."),
        ("« La memb' est glacée. »", "La membrane est glacée."),
        ("« C'est exac', il vente trop. »", "C'est exact, il vente trop."),
    ], corrige=True,
       notes="Faire remarquer la première phrase : « c'est pas » au lieu de « ce n'est "
             "pas ». Le « ne » tombe aussi à l'oral — c'est le module 1, séance C3.")

    d.pratique('Pratique · 4 de 4', "Lisez à voix haute, vite",
               "Le groupe dit si la consonne finale tombe ou non.", [
        ("Quatre couvreurs montent sur le toit.", "quat' couvreurs"),
        ("Quatre échelles sont appuyées au mur.", "quatr' échelles"),
        ("Ce n'est pas possible demain.", "possib' demain"),
        ("La membrane est glacée.", "membrane — la consonne reste"),
    ], corrige=True,
       notes="Faire lire debout et vite. Lentement, la consonne revient toujours : c'est "
             "la vitesse qui la fait tomber.")

    d.billet(
        "Écrivez quatre mots dont la consonne finale tombe souvent à l'oral.",
        exemples=[
            "Écrivez la forme entière, puis la forme entendue à côté.",
            "Exemple : « quatre » — on entend « quat' ».",
        ],
        notes="Corriger la forme écrite avant tout. C'est elle qui compte dans un "
              "cahier ; la forme orale n'est là que pour l'oreille.")

    return d.save(dossier)
