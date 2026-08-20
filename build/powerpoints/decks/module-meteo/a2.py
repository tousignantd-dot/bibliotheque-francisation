# -*- coding: utf-8 -*-
"""A2 · Les consonnes qui tombent en fin de mot.
Bloc A · couleur indigo (graphie-phonie) · 60 min.
Source : exercice `prPhon` — le l, le r et le t finaux à l'oral.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
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
        "écrire correctement un mot qu'on entend sans sa consonne finale ;",
        "distinguer le son « é » du son « è » dans le vocabulaire du bulletin.",
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

    d.pratique('Pratique · 1 de 6', "Écrivez le mot entier",
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

    d.pratique('Pratique · 2 de 6', "La consonne tombe-t-elle ?",
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

    d.pratique('Pratique · 3 de 6', "Écoutez et écrivez la phrase",
               "Écrivez tous les mots en entier.", [
        ("« C'est pas possib' de monter aujourd'hui. »",
         "Ce n'est pas possible de monter aujourd'hui."),
        ("« On a quat' jours de retard. »", "On a quatre jours de retard."),
        ("« La memb' est glacée. »", "La membrane est glacée."),
        ("« C'est exac', il vente trop. »", "C'est exact, il vente trop."),
    ], corrige=True,
       notes="Faire remarquer la première phrase : « c'est pas » au lieu de « ce n'est "
             "pas ». Le « ne » tombe aussi à l'oral — c'est le module 1, séance C3.")

    d.pratique('Pratique · 4 de 6', "Lisez à voix haute, vite",
               "Le groupe dit si la consonne finale tombe ou non.", [
        ("Quatre couvreurs montent sur le toit.", "quat' couvreurs"),
        ("Quatre échelles sont appuyées au mur.", "quatr' échelles"),
        ("Ce n'est pas possible demain.", "possib' demain"),
        ("La membrane est glacée.", "membrane — la consonne reste"),
    ], corrige=True,
       notes="Faire lire debout et vite. Lentement, la consonne revient toujours : c'est "
             "la vitesse qui la fait tomber.")


    d.regle("L'autre difficulté du bulletin : é ou è",
            "L'accent change le son : « é » ferme la bouche, « è » l'ouvre.",
            precision="« Météo » et « mètres » se suivent dans le même bulletin. Le "
                      "premier a deux fois le son « é », le second le son « è ». "
                      "L'écart est petit à l'oreille et net à l'écrit.",
            notes="Enchaîner « météo, mètres, météo, mètres » lentement. La mâchoire "
                  "descend sur « è », elle reste haute sur « é ».")

    d.tableau('Analyse', "Les deux sons dans les mots de la météo",
              ['Le son', "Il s'écrit", 'Mots du module'],
              [["le son « é »", "é, et les finales -er, -ez, -ée", "météo, degrés, préparer, journée"],
               ["le son « è »", "è, ê, ai, ei, e suivi de deux consonnes", "mètres, neige, après, verglas"]],
              cle=0,
              note="Un verbe qui finit par -er se dit toujours avec le son « é » : "
                   "préparer, annuler, tomber. La règle n'a pas d'exception.",
              notes="La finale -er des verbes est le cas le plus rentable de la "
                    "séance : elle vaut pour des centaines de verbes.")

    d.piege('Le piège de « verglas »',
            "vé-glas, avec le son « é »",
            "ver-glas — le son « è », parce que le e est suivi de deux consonnes",
            "Sans accent écrit, on croit lire un « é ». Mais un e suivi de deux "
            "consonnes se dit « è » : verglas, personne, averse. C'est une règle qui "
            "se voit à l'œil, sans avoir à connaître le mot.",
            notes="Faire souligner les deux consonnes qui suivent le e dans verglas, "
                  "personne et averse. La règle devient visuelle.")

    d.pratique('Pratique · 5 de 6', 'Quel son entendez-vous ?',
               "Écoutez le mot, écrivez « é » ou « è ».", [
        ("météo", "le son « é »"),
        ("mètres", "le son « è »"),
        ("degrés", "le son « é »"),
        ("neige", "le son « è »"),
        ("préparer", "le son « é »"),
        ("verglas", "le son « è »"),
        ("journée", "le son « é »"),
        ("après", "le son « è »"),
    ], corrige=True, cols=2,
       notes="Les huit mots de l'exercice de sons du module en ligne, dans le même "
             "ordre. Ne pas montrer l'orthographe avant la correction : l'accent "
             "écrit donnerait la réponse.")

    d.pratique('Pratique · 6 de 6', 'Trois phrases de bulletin à lire à voix haute',
               "Chacun lit une phrase. Le groupe ne corrige que les é et les è.", [
        ("La météo annonce dix degrés sous zéro.", "é · é · é"),
        ("La neige tombe et la visibilité est de cent mètres.", "è · è"),
        ("Il faut préparer les crampons après le dîner.", "é · è"),
    ], corrige=True,
       notes="Faire lire lentement : à vitesse normale, la différence s'efface et "
             "l'exercice perd son intérêt.")

    d.billet(
        "Écrivez quatre mots dont la consonne finale tombe souvent à l'oral.",
        exemples=[
            "Écrivez la forme entière, puis la forme entendue à côté.",
            "Exemple : « quatre » — on entend « quat' ».",
        ],
        notes="Corriger la forme écrite avant tout. C'est elle qui compte dans un "
              "cahier ; la forme orale n'est là que pour l'oreille.")

    return d.save(dossier)
