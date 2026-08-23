# -*- coding: utf-8 -*-
"""C2 · « La chaise du fond » — six pages, quatre gestes
Bloc C « Défi 2 · Ce qui n'est pas écrit » · couleur acier · 75 min.
Source : exercice `t2nouv` (type `texte`) et sa mini-leçon.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-oeuvres' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C2', section='acier',
        titre="« La chaise du fond » : six pages, quatre gestes",
        chapeau="La nouvelle ne dit jamais ce que Gisèle éprouve. Elle montre "
                "quatre gestes et vous laisse faire l'addition. Ce n'est pas "
                "un manque de clarté : c'est de la place laissée.",
        duree='75 minutes')

    d.titre(notes="Séance de compréhension écrite. Faire distribuer l'extrait imprimé "
                  "avant d'ouvrir l'écran : on lit sur papier, on répond à l'écran.")

    d.objectifs([
        "lire un récit littéraire au passé simple sans buter dessus ;",
        "repérer au plus-que-parfait ce qui s'était décidé avant la scène ;",
        "trouver l'endroit unique où le narrateur sort de la scène ;",
        "comparer deux lectures en comptant ce que chacune explique.",
    ], notes="Le troisième objectif est une méthode de lecture générale : dans un "
             "texte court, cherchez la seule fois où la voix qui raconte se permet "
             "quelque chose.")

    d.declencheur(
        'Observation', "Où s'assoit-on quand on arrive à sa propre fête ?",
        image=IMG + 'table-du-fond.jpg',
        pistes=[
            "Deux places restent libres : une au centre, une au fond.",
            "Laquelle prendriez-vous ? Pourquoi ?",
            "À quoi sert cette table-là, le reste de l'année ?",
            "Que comprend la salle si vous prenez le fond ?",
        ],
        notes="Question à faire circuler dans le groupe : les réponses sont très "
              "différentes selon les cultures d'origine, et c'est exactement le sujet "
              "du texte. Ne trancher pas.")

    d.tableau('Analyse', "Quatre gestes, et rien d'autre",
              ['Le geste', 'Ce que le texte dit'],
              [["La chaise", "elle prend celle du fond, la table des stagiaires"],
               ["Le silence", "personne ne dit rien, personne ne corrige"],
               ["La lecture", "elle demande à sa voisine de lire à sa place"],
               ["La nappe", "elle la plie et la met dans son sac"]],
              cle=0,
              note="Aucun de ces gestes n'est expliqué. La nouvelle s'arrête après le quatrième.",
              notes="Diapositive à photographier. Faire remarquer que le texte ne "
                    "contient aucun adjectif de sentiment : ni triste, ni fâchée, ni "
                    "déçue. C'est un choix, pas une pauvreté.")

    d.regle("Le passé simple se reconnaît, il ne se parle pas",
            "Verbes en -er : elle poussa, ils poussèrent. La plupart des "
            "autres : elle prit, il fit, elle dit, elle vint.",
            precision="Vous ne l'emploierez jamais dans une conversation, et personne "
                      "ne vous le demandera. Vous le lirez dans chaque roman, chaque "
                      "nouvelle et chaque conte que vous ouvrirez ici. Six irréguliers "
                      "suffisent : fut, eut, fit, dit, vit, vint.",
            notes="Diapositive à photographier. Le dire clairement : cette liste-là est "
                  "à reconnaître, pas à produire. Cela soulage la moitié du groupe.")

    d.tableau('Analyse', "Trois temps, trois plans du récit",
              ['Le temps', 'Ce qu\'il porte'],
              [["Imparfait", "le décor : la salle était pleine"],
               ["Passé simple", "l'action : elle traversa la salle"],
               ["Plus-que-parfait", "l'avant : on avait commencé sans elle"]],
              cle=0,
              note="Rangez chaque phrase dans une colonne, et le texte s'organise seul.",
              notes="Diapositive à photographier. Dans cette nouvelle, tout ce qui "
                    "s'est décidé sans Gisèle est au plus-que-parfait : la grammaire "
                    "dit la même chose que l'histoire.")

    d.piege('Piège', "confondre le narrateur et l'auteure",
            "les tenir séparés",
            "Celui qui raconte est une voix construite : il peut se taire, se "
            "tromper, ou juger. Odile Brassard-Vézina n'est pas plus « la voix » "
            "de cette nouvelle que Gisèle n'est elle-même. La confusion est "
            "banale et elle coûte cher : elle transforme une lecture de texte "
            "en procès d'intention contre une personne.",
            notes="Dans cette nouvelle, le narrateur ne juge jamais Gisèle. Il note ce "
                  "qu'elle fait — et une seule fois ce qu'elle cache.")

    d.cartes('Analyse', "La parenthèse, et ce qu'elle change", [
        ("Ce qu'elle dit", "qu'elle avait oublié ses lunettes"),
        ("Ce que le narrateur ajoute", "qu'elle ne les avait pas oubliées"),
        ("Combien de fois", "une seule, en six pages"),
        ("Ce que ça prouve", "rien : cela oriente, et cela suffit"),
        ("Lecture tendre", "une femme effacée : explique deux gestes"),
        ("Lecture de la colère", "un geste public : explique les quatre"),
    ], notes="Les deux dernières cases sont le décompte de B2 appliqué à un texte. "
             "Quatre contre deux : la lecture de la colère n'est pas plus vraie, elle "
             "couvre plus de texte.")

    d.pratique('Compréhension', "Où est-ce écrit ?",
               "Retrouvez le passage qui répond.", [
        ("Montre que la fête avait commencé avant elle.", "on avait commencé sans elle"),
        ("Indique qu'on lui avait gardé la place d'honneur.", "une chaise restait libre"),
        ("Dit comment la salle réagit à son choix.", "personne ne dit rien"),
        ("Nomme l'erreur du contremaître.", "il l'appela deux fois Ginette"),
        ("Dit que sa raison de ne pas lire est fausse.", "la parenthèse"),
        ("Ferme la nouvelle.", "elle plia la nappe et la mit dans son sac"),
    ], corrige=True,
       notes="Exercice `t2nouv` du module, en version papier. À l'écran, l'élève clique "
             "le passage dans le texte : le faire ensuite, la manipulation vaut la "
             "reprise.")

    d.pratique('Pratique', "Passé simple ou plus-que-parfait ?",
               "Complétez.", [
        ("Gisèle ___ (pousser) la porte à midi cinq.", "poussa"),
        ("Elle ___ (prendre) la chaise du fond.", "prit"),
        ("Le contremaître ___ (faire) un discours.", "fit"),
        ("Quand elle arriva, on ___ (commencer) sans elle.", "avait commencé"),
        ("Personne ne ___ (s'asseoir) sur la chaise du centre.", "s'était assis"),
        ("Elle prétendit qu'elle ___ (oublier) ses lunettes.", "avait oublié"),
    ], corrige=True,
       notes="Exercice `t2temps` du module, moitié avant. L'autre moitié est en C4 : "
             "ici on l'installe sur le texte qu'on vient de lire, ce qui aide.")

    d.billet(
        "En deux phrases : quelle lecture de « La chaise du fond » "
        "défendez-vous, et sur quel geste précis ?",
        exemples=[
            "Une phrase pour la lecture, une pour le geste.",
            "Le geste doit être un de ceux du tableau : on doit pouvoir le montrer.",
        ],
        notes="Ramasser. Les copies qui donnent un sentiment au lieu d'un geste "
              "(« parce qu'elle est triste ») disent que le partage fait / "
              "interprétation n'est pas encore acquis : y revenir en C3.")

    return d.save(dossier)
