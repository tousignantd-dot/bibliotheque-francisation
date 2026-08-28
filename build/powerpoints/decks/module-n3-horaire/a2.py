# -*- coding: utf-8 -*-
"""A2 · Le son « ou » et le son « u ».
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : exercice `prPhon`, mini-leçon `prPhon`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le son « ou » et le son « u »",
        chapeau="Douze et du. Jour et jure. Four et fut. Deux sons que "
                "beaucoup de langues n'opposent pas — et qui séparent, ici, "
                "des mots qu'on emploie toute la journée.",
        duree='60 minutes')

    d.titre(notes="Séance de prononciation. Elle vient tôt exprès : les deux sons sont "
                  "dans « douze », « une minute », « le four », « la cuisine » — c'est-à-"
                  "dire dans le vocabulaire de tout le module.")

    d.objectifs([
        "entendre la différence entre « ou » et « u » ;",
        "placer la langue et les lèvres pour chacun ;",
        "prononcer les mots du travail qui les contiennent ;",
        "ne plus confondre douze et du, jour et jure.",
    ])

    d.regle("Deux sons, un seul geste qui change",
            "OU : la langue en arrière. U : la langue en avant.",
            precision="Les lèvres sont arrondies dans les deux cas — c'est "
                      "ce qui trompe. Ce n'est pas la bouche qu'il faut "
                      "regarder, c'est la langue, qui avance pour « u » et "
                      "recule pour « ou ».",
            notes="Diapo à photographier. Faire dire « ou-u-ou-u » lentement, main devant "
                  "la bouche : les lèvres ne bougent presque pas. C'est la démonstration "
                  "la plus convaincante de la séance.")

    d.tableau('Analyse', "Les paires du lieu de travail",
              ["Le son OU", "Le son U"],
              [["un jour", "elle jure"],
               ["douze", "du café"],
               ["tout de suite", "tu commences"],
               ["le four", "il fut chaud"]],
              cle=1,
              note="La deuxième ligne est celle du casier : « le douze », "
                   "pas « le duze ».",
              notes="Diapo à photographier. Faire lire les colonnes verticalement, puis "
                    "horizontalement. C'est en passant d'un mot à l'autre que l'oreille "
                    "se forme, pas en répétant le même.")

    d.pratique('Écoute', "OU comme JOUR, ou U comme MINUTE ?",
               "Écoutez chaque mot et classez-le.", [
        ("un jour", "OU"),
        ("une minute", "U"),
        ("douze", "OU"),
        ("une heure", "U"),
        ("le four", "OU"),
        ("un uniforme", "U"),
        ("tout de suite", "OU"),
        ("la cuisine", "U"),
    ], corrige=True,
       notes="C'est l'exercice `prPhon` du module interactif, mot pour mot. Le faire "
             "livre fermé, à l'oreille seulement. « Une heure » surprend souvent : le "
             "« eu » n'est ni l'un ni l'autre, mais il est du côté de « u ».")

    d.piege("Dire « le casier duze »",
            "Mon casier, c'est le duze.",
            "Mon casier, c'est le douze.",
            "Un numéro mal prononcé envoie quelqu'un au mauvais casier, au "
            "mauvais étage, à la mauvaise porte. C'est le genre d'erreur "
            "qu'on ne corrige jamais parce que personne n'ose la relever.",
            notes="Faire dire à chacun un numéro à voix haute — casier, appartement, "
                  "autobus. Corriger doucement, une seule fois par personne.")

    d.pratique('Prononciation', "Deux par deux : lisez et faites deviner",
               "L'un lit un mot de la paire, l'autre dit lequel il a entendu.", [
        ("jour / jure", "le son OU est en arrière"),
        ("douze / du", "le numéro du casier"),
        ("tout / tu", "les deux dans la même phrase"),
        ("four / fut", "le mot du défi 3"),
        ("pour / pur", "on emploie surtout le premier"),
        ("sous / su", "attention : les deux existent au travail"),
    ], corrige=False, cols=1,
       notes="Dix minutes, puis on inverse. Celui qui écoute a le rôle le plus utile : "
             "c'est lui qui travaille l'oreille. Le dire, sinon les élèves croient que "
             "seul celui qui parle apprend.")

    d.regle("La phrase qui contient les deux",
            "Une minute, je poinçonne.",
            precision="« Une » et « minute » portent le son U ; "
                      "« poinçonne » n'en a aucun des deux, mais la phrase "
                      "entière est celle qu'on dit dix fois par semaine au "
                      "travail. La prononcer juste, c'est déjà beaucoup.",
            notes="Diapo à photographier. Faire répéter la phrase entière plutôt que les "
                  "sons isolés : c'est en contexte que la prononciation tient.")

    d.billet(
        "Écrivez six mots de votre travail, trois avec OU, trois avec U.",
        exemples=[
            "Des mots que vous dites vraiment, pas des mots de dictionnaire.",
            "Vous les lirez à voix haute en A3.",
        ],
        notes="Devoir court. Les mots rapportés sont souvent hors du module — outil, "
              "chariot, uniforme, ustensile — et c'est tant mieux : ils ancrent le son "
              "dans le métier de chacun.")

    return d.save(dossier)
