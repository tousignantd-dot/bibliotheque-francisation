# -*- coding: utf-8 -*-
"""B4 · Ce qui est établi, ce qui est approché
Bloc B « Défi 1 » · couleur acier · 75 min.
Source : exercices `t1fait` et `t1img`, mini-leçon `t1fait`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-classe' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre="Ce qui est établi, ce qui est approché",
        chapeau="Pendant une rencontre, tout arrive au même rythme et sur le "
                "même ton. Trois heures plus tard, devant ses notes, on ne "
                "sait plus lequel de ces chiffres était mesuré.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 1. Elle réunit ce que les trois "
                  "précédentes ont posé : écouter un plan, entendre un "
                  "conditionnel, prendre des notes utilisables.")

    d.objectifs([
        "distinguer un fait établi d'un chiffre approché ;",
        "reconnaître les marqueurs qui signalent une estimation ;",
        "noter un chiffre avec sa source et son statut ;",
        "décrire ce qu'on a observé dans son quartier.",
    ], notes="Le troisième objectif est le seul qui se vérifie sur une feuille : "
             "ramasser les notes en fin de séance et regarder si les chiffres y "
             "portent leur année.")

    d.declencheur(
        'Observation', "Ce que l'équipe est allée voir",
        image=IMG + 'trottoir-racine.jpg',
        pistes=[
            "Qu'est-ce qui a soulevé le trottoir ?",
            "Est-ce une raison de ne pas planter d'arbres en ville ?",
            "Qui paie la réparation, à votre avis ?",
            "Avez-vous vu la même chose près de chez vous ?",
        ],
        notes="La deuxième piste divise la classe, et c'est utile : elle prépare le "
              "désaccord du bloc D, où deux coéquipiers ne s'entendent pas non plus. "
              "Ne pas trancher.")

    d.tableau('Analyse', "Trois statuts, trois signes",
              ['Le statut', 'Ce qui le signale'],
              [["Un fait",
                "le présent, aucune prudence, et ça se vérifie ailleurs"],
               ["Une estimation",
                "environ, une dizaine, on estime que, ou le conditionnel"],
               ["Une opinion",
                "je pense que, à mon avis, ou un mot qui évalue"]],
              cle=0,
              note="Les trois se notent — jamais de la même façon.",
              notes="Diapositive à photographier. L'opinion d'une personne du métier "
                    "vaut beaucoup : elle se garde, avec le nom devant.")

    d.pratique('Compréhension', "Un fait, ou une estimation ?",
               "Classez chaque phrase entendue chez Perrine.", [
        ("« L'asphalte monte plus haut qu'une pelouse. »", "un fait"),
        ("« L'écart serait d'une dizaine de degrés. »", "une estimation"),
        ("« Un arbre rejette de l'eau par ses feuilles. »", "un fait"),
        ("« Ce serait sous les dix pour cent. »", "une estimation"),
        ("« La canopée se mesure en pourcentage. »", "un fait"),
        ("« On estime la perte à un sur cinq. »", "une estimation"),
    ], corrige=True,
       notes="Aller vite. Puis demander le signe à chaque fois : c'est le signe "
             "qu'on apprend, pas la réponse.")

    d.regle("Un chiffre se note avec deux choses",
            "D'où il vient, et s'il est mesuré ou approché. Sans ces deux "
            "choses, un chiffre est inutilisable trois jours plus tard.",
            precision="Dans la marge, un signe suffit : un tiret pour le fait, un "
                      "point d'interrogation pour l'estimation, des guillemets pour "
                      "l'opinion de quelqu'un.",
            notes="Diapositive à photographier. Faire reprendre les notes de B1 avec "
                  "ces trois signes : dix minutes, et elles deviennent utilisables.")

    d.pratique('Observation', "Décrire ce qu'on voit",
               "Une phrase complète par photo, à l'écrit puis à voix haute.", [
        ("Le stationnement", "un grand stationnement d'asphalte noir, sans un seul arbre"),
        ("La rue plantée", "des érables matures dont les branches se rejoignent au-dessus de la chaussée"),
        ("Le jeune arbre", "tenu droit par deux tuteurs, un sac d'arrosage à sa base"),
        ("La cour d'école", "entièrement asphaltée, une mince bande de gazon jauni le long de la clôture"),
        ("Le trottoir", "soulevé et fendu par la racine de l'arbre planté à côté"),
        ("La ruelle", "en gravier, entièrement à l'ombre entre deux rangées de hangars"),
    ], corrige=True,
       notes="Les six photos sont dans le module. En classe, les projeter une à une "
             "et faire produire la phrase avant de montrer la réponse : c'est de la "
             "production orale déguisée, et elle prépare l'exposé.")

    d.piege('Notes',
            "« 17 % »",
            "« 17 % — canopée, ville, relevé de l'an dernier »",
            "Le premier ne veut plus rien dire dans trois jours, et il ne "
            "peut pas être cité dans un travail. Le second se cite tel quel. "
            "La différence a coûté quatre secondes d'écriture.",
            notes="Point de méthode. Beaucoup d'élèves notent des chiffres nus depuis "
                  "des années : montrer une feuille de notes réelle, la leur, et "
                  "leur faire compter les chiffres sans source.")

    d.billet(
        "Notez un chiffre de votre sujet, avec sa source, son année et son statut.",
        exemples=[
            "Une seule ligne.",
            "Mesuré ou approché ? Dites lequel.",
        ],
        notes="Billet de sortie du Défi 1. Les lignes reçues montrent tout de suite "
              "qui a compris : celles où le statut manque appellent une reprise en "
              "C1, avant que le résumé commence.")

    return d.save(dossier)
