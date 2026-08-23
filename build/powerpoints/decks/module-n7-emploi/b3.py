# -*- coding: utf-8 -*-
"""B3 · Les panneaux de la route
Bloc B « Défi 1 · La réunion de production » · couleur ambre · 75 min.
Source du module : exercice `t1connect`, mini-leçon `t1connect`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Les panneaux de la route",
        chapeau="Un connecteur n'ajoute aucune information : il dit où l'on "
                "est rendu. C'est exactement le rôle d'un panneau routier, qui "
                "ne construit pas la route mais sans lequel personne ne sait "
                "s'il faut tourner.",
        duree='75 minutes')

    d.titre(notes="Premier point de grammaire du texte du module. Insister sur la "
                  "différence avec la grammaire de la phrase : ici, rien ne s'accorde "
                  "et rien ne se conjugue. Ce qui se travaille, c'est ce qui relie deux "
                  "phrases.")

    d.objectifs([
        "reconnaître les quatre familles de connecteurs : énumération, "
        "conséquence, opposition, clôture ;",
        "choisir le connecteur qui dit la relation qu'on veut dire ;",
        "distinguer le registre écrit du registre oral ;",
        "doser : un connecteur toutes les deux ou trois phrases.",
    ], notes="Le quatrième objectif est celui qu'on oublie d'enseigner, et c'est celui "
             "qui distingue un texte agréable d'un texte fatigant.")

    d.declencheur(
        'Observation', "Enlevez les connecteurs, et écoutez ce qui reste",
        pistes=[
            "« On mesure. On trace. On essaie. On installe. »",
            "« D'abord on mesure, ensuite on trace, puis on essaie, enfin on installe. »",
            "Laquelle des deux se retient ?",
            "Qu'est-ce que les quatre petits mots ont ajouté comme information ?",
        ],
        notes="Réponse attendue à la dernière question : aucune. Ils n'ajoutent rien "
              "au contenu, et pourtant la seconde version se retient. C'est tout le "
              "sujet de la séance.")

    d.tableau('Analyse', "Les quatre familles",
              ['La relation', 'Les mots'],
              [["Énumérer", "d'abord, ensuite, puis, enfin"],
               ["Dire la conséquence", "par conséquent, c'est pourquoi, ainsi, donc"],
               ["Dire l'opposition", "en revanche, cependant, toutefois, par contre"],
               ["Donner un exemple", "par exemple, notamment, ainsi, prenons"],
               ["Fermer", "en somme, pour résumer, en définitive"]],
              cle=0,
              note="« Enfin » annonce la dernière : jamais au milieu. « Notamment » annonce un exemple parmi d'autres, jamais une liste complète.",
              notes="Diapositive à photographier. Les deux pièges de la note sont ceux "
                    "qu'on entend le plus souvent, y compris chez des francophones.")

    d.tableau('Analyse', "Écrit ou oral : le même sens, pas le même mot",
              ['À l\'écrit', 'À l\'oral'],
              [["par conséquent", "donc, résultat"],
               ["en revanche, cependant", "par contre, mais"],
               ["toutefois, néanmoins", "quand même, pareil"],
               ["en somme, en définitive", "pour résumer, bref"]],
              cle=0,
              note="« Par contre » est parfaitement correct en français du Québec. C'est une question de registre, pas de correction.",
              notes="Diapositive à photographier. La note désamorce une croyance très "
                    "répandue selon laquelle « par contre » serait fautif. Il ne l'est "
                    "pas ; il est simplement d'un autre registre.")

    d.regle("On ne mélange pas les deux registres",
            "Dans une lettre, tout est formel. En réunion, tout peut être courant.",
            precision="« En revanche » suivi de « par contre » deux phrases plus loin "
                      "s'entend comme une hésitation : le lecteur se demande à quel "
                      "niveau vous parlez. Choisissez selon le document, et tenez-vous-y "
                      "du début à la fin.",
            notes="Diapositive à photographier. C'est la règle que la note de service "
                  "et la lettre d'affaires du bloc D vont mettre à l'épreuve.")

    d.pratique('Pratique', "Le connecteur qui convient",
               "Complétez. Chacun ne sert qu'une fois.", [
        ("..., on mesure : deux semaines de relevés.", "D'abord"),
        ("..., on trace un plan à l'échelle.", "Ensuite"),
        ("..., on installe pour de bon.", "Enfin"),
        ("Le quai n'a pas changé ; ..., les camions attendent.", "par conséquent"),
        ("L'essai coûte quatre cents dollars. ..., l'installation en coûterait douze mille.", "En revanche"),
        ("Certains risques sont faciles à prévoir, ... la circulation modifiée.", "notamment"),
    ], corrige=True,
       notes="C'est l'exercice `t1connect` du module, qui en compte huit. Il est en "
             "`cols:1` dans le module parce que ses items font deux phrases : le "
             "signaler, c'est une contrainte de lisibilité qui vaut aussi au tableau.")

    d.piege('Écriture',
            "un connecteur à chaque phrase",
            "un connecteur toutes les deux ou trois phrases",
            "Au-delà, l'exposé sonne comme une liste d'épicerie : on n'entend plus que "
            "les panneaux et plus du tout la route. Le bon minimum, dans un exposé de "
            "dix minutes, est de quatre : un pour ouvrir, un pour enchaîner, un pour "
            "opposer, un pour fermer. Quatre charnières, pas quarante.",
            notes="Faire compter les connecteurs dans la présentation de monsieur "
                  "Cormier : il y en a une dizaine pour douze minutes. C'est la bonne "
                  "mesure, et elle se vérifie.")

    d.pratique('Pratique', "Réécrivez sans changer le sens",
               "Passez du registre oral au registre écrit.", [
        ("« Donc les camions attendent. »", "Par conséquent, les camions attendent."),
        ("« Par contre, ça coûte cher. »", "En revanche, cela coûte cher."),
        ("« Bref, on fait un essai. »", "En somme, nous procéderons à un essai."),
        ("« Mais on n'achète rien tout de suite. »", "Toutefois, aucun achat n'est prévu dans l'immédiat."),
        ("« Pareil, il faut le noter. »", "Néanmoins, il convient de le noter."),
    ], corrige=True,
       notes="Exercice de passage de registre, qui prépare le bloc D. Faire remarquer "
             "que le verbe change souvent en même temps que le connecteur : c'est tout "
             "le registre qui monte, pas seulement un mot.")

    d.billet(
        "Reprenez votre objectif et ajoutez-lui deux phrases reliées par un connecteur.",
        exemples=[
            "Une phrase de contexte, puis « par conséquent », puis l'objectif.",
            "Relisez à voix haute : est-ce que le connecteur dit la bonne relation ?",
        ],
        notes="Ramasser. Corriger le choix du connecteur, pas le reste : c'est un "
              "devoir de grammaire du texte.")

    return d.save(dossier)
