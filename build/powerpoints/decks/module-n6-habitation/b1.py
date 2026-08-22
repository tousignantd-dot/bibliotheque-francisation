# -*- coding: utf-8 -*-
"""B1 · Une heure au sous-sol
Bloc B « Défi 1 · Le diagnostic » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`, cartes de FC_CARDS de la section t1.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Une heure au sous-sol",
        chapeau="L'entrepreneur a fait le tour. Il explique ce qu'il a "
                "trouvé, ce qui l'a causé, et dans quel ordre on va "
                "travailler. Vingt minutes sans reprendre son souffle.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Prévenir le groupe : on écoute d'abord sans "
                  "rien noter, puis on réécoute en notant. Une explication technique "
                  "ne se comprend pas à la première écoute, et il faut le dire pour "
                  "que personne ne se croie en retard.")

    d.objectifs([
        "suivre une explication technique du début à la fin ;",
        "nommer les quatre mots de la fondation et du drainage ;",
        "repérer les chiffres donnés au passage ;",
        "arrêter quelqu'un poliment pour lui faire répéter.",
    ], notes="Le quatrième objectif s'exerce pour vrai : faire pratiquer « attendez, "
             "je n'ai pas suivi » et « pouvez-vous reprendre la dernière partie ? ».")

    d.declencheur(
        'Observation', "Quelqu'un vous explique un problème technique. Que faites-vous quand vous perdez le fil ?",
        pistes=[
            "L'arrêtes-tu, ou attends-tu la fin ?",
            "Que dis-tu exactement pour l'arrêter ?",
            "As-tu déjà fait semblant de comprendre ? Qu'est-ce qui est arrivé ?",
        ],
        notes="La dernière question fait toujours rire, et elle donne le ton du bloc. "
              "Recueillir deux ou trois formules d'interruption polies et les écrire "
              "au tableau.")

    d.dialogue('Dialogue · 1 de 3', "Ce qu'il a trouvé", [
        ("FERNAND", "Je viens de passer une heure en bas et j'ai fait le tour du terrain. Je vais vous expliquer, et après vous poserez vos questions.", True),
        ("DOÏNA", "Allez-y. Je vous préviens, je vais vous arrêter souvent.", True),
        ("FERNAND", "Arrêtez-moi tant que vous voulez. Premièrement, la fissure. Elle est dans le mur de fondation, du côté nord, et elle monte en biais sur à peu près un mètre.", True),
        ("DOÏNA", "Elle est apparue quand ? On a acheté la maison il y a deux ans.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="La deuxième réplique de Doïna est le modèle à installer : elle annonce "
             "qu'elle va interrompre, et l'entrepreneur accepte. Faire remarquer que "
             "ça se dit, et que ça change tout le reste de la conversation.")

    d.dialogue('Dialogue · 2 de 3', "La cause est dehors", [
        ("FERNAND", "Elle s'était ouverte bien avant que vous achetiez. Votre inspectrice l'avait notée dans son rapport, d'ailleurs.", True),
        ("FERNAND", "La cause est dehors. Vous voyez la descente de gouttière, au coin ? Elle se vide à trente centimètres du mur.", True),
        ("DOÏNA", "Et c'est un problème ?", True),
        ("FERNAND", "Chaque grosse pluie, vous envoyez des centaines de litres d'eau contre votre fondation. Le sol se gorge, il pousse sur le mur, et le mur finit par fendre.", True),
    ], notes="Les deux répliques au plus-que-parfait sont celles de B4. Les signaler "
             "sans les expliquer : on y revient dans deux séances.")

    d.dialogue('Dialogue · 3 de 3', "L'ordre des travaux", [
        ("DOÏNA", "Alors ce n'est pas la fissure, le vrai problème.", True),
        ("FERNAND", "Vous venez de dire la chose la plus importante de la matinée. La fissure, c'est le résultat. Si je la répare sans toucher au reste, elle revient dans trois ans.", True),
        ("FERNAND", "Dans l'ordre : on rallonge les descentes de gouttière, on refait la pente du terrain, et seulement après, on fait injecter la fissure.", True),
        ("DOÏNA", "Vous dites « on fait injecter ». Ce n'est pas vous qui le faites ?", True),
    ], notes="La deuxième réplique porte tout le défi. L'écrire au tableau et l'y "
             "laisser : « la fissure, c'est le résultat ». La quatrième annonce B4 et "
             "le faire causatif.")

    d.tableau('Analyse', "Ce qui tient la maison debout",
              ['Le mot', 'Ce que c\'est'],
              [["la fondation", "le mur de béton enfoui, sur lequel tout repose"],
               ["une fissure", "une fente qui traverse le mur et qui bouge"],
               ["la descente", "le tuyau qui amène l'eau du toit jusqu'au sol"],
               ["la pente", "l'inclinaison du sol autour de la maison"]],
              cle=0,
              note="Trois des quatre sont dehors. C'est là que se règlent les problèmes du sous-sol.",
              notes="Diapositive à photographier. La colonne de gauche est volontairement "
                    "courte : « la descente » et « la pente » suffisent, les mots "
                    "complets sont dans le module.")

    d.regle("Le visible arrive toujours en second",
            "Une fissure, une tache, un plancher qui gondole : ce sont des résultats.",
            precision="La cause est ailleurs, presque toujours dehors, et presque "
                      "toujours une histoire d'eau. Le test tient en une phrase : "
                      "« si je répare seulement ça et que rien d'autre ne change, "
                      "est-ce que ça revient ? » Si la réponse est oui, vous "
                      "regardez un résultat.",
            notes="Diapositive à photographier. C'est la règle du bloc B, et elle "
                  "s'exerce en entier à la prochaine séance.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'explication de Fernand Trudelle.", [
        ("La fissure se trouve dans le mur de fondation, du côté nord.", "vrai"),
        ("Elle est apparue après l'achat de la maison.", "faux - bien avant"),
        ("La descente de gouttière se vide à trois mètres du mur.", "faux - à trente centimètres"),
        ("Fernand veut injecter la fissure avant de toucher au terrain.", "faux - après"),
        ("L'injection sera faite par un spécialiste.", "vrai"),
        ("Il faut laisser sécher trois ou quatre semaines.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le quatrième est "
             "celui qui compte : c'est l'ordre des travaux, et il se travaille en B2.")

    d.billet(
        "Redis en deux phrases ce que Fernand a trouvé et pourquoi.",
        exemples=[
            "Une phrase pour le résultat, une pour la cause.",
            "Emploie « parce que » ou « à cause de ».",
        ],
        notes="Trois minutes. C'est la première répétition de la production orale de "
              "E1. Ramasser les billets et en lire deux ou trois à voix haute sans "
              "nommer les auteurs.")

    return d.save(dossier)
