# -*- coding: utf-8 -*-
"""A2 · « La voix qui monte, la voix qui descend »
Bloc A « Je découvre » · couleur indigo · 75 min. Phonétique.
Source : exercice `prPhon`, mini-leçon `prPhon`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="La voix qui monte, la voix qui descend",
        chapeau="« Vous venez samedi. » et « Vous venez samedi ? » ont les "
                "mêmes mots, dans le même ordre. Seule la voix les sépare. "
                "C'est la façon la plus courante de poser une question en "
                "français parlé du Québec.",
        duree='75 minutes')

    d.titre(notes="Séance de phonétique, mais elle n'est pas décorative : sans elle, "
                  "l'élève n'entend pas qu'on lui pose une question, et son silence passe "
                  "pour de l'impolitesse. Commencer en disant deux fois la même phrase, "
                  "une fois montante, une fois descendante, sans rien expliquer. "
                  "Demander ce qui a changé.")

    d.objectifs([
        "entendre si une phrase monte ou descend à la fin ;",
        "poser une question sans « est-ce que », par la seule intonation ;",
        "reconnaître qu'une question en « quand » ou « qui » descend ;",
        "dire une exclamation sans qu'elle ressemble à un doute.",
    ], notes="Le quatrième objectif servira au défi 3 : une félicitation dite avec une "
             "voix montante a l'air d'une mise en doute. Le dire dès maintenant.")

    d.regle("La voix monte : on demande",
            "À la fin d'une question sans mot interrogatif, la voix monte "
            "comme une marche qu'on gravit.",
            precision="Vous venez samedi ? · Il faut apporter quelque chose ? · "
                      "C'est dans la ruelle ? Plus la montée est nette, plus la "
                      "question s'entend. Au téléphone, il faut monter davantage : "
                      "la ligne mange les nuances.",
            notes="Faire dire les trois phrases par toute la classe en même temps, la "
                  "main levée qui monte avec la voix. Le geste aide plus que "
                  "l'explication, et il reste.")

    d.regle("La voix descend : on affirme, ou on demande autrement",
            "La voix descend à la fin d'une affirmation, et aussi à la fin "
            "d'une question qui commence par un mot interrogatif.",
            precision="La fête est le 7 juin. · Quand est-ce que ça commence ? · "
                      "Qui organise la fête ? Le mot « quand », « qui » ou « où » a "
                      "déjà posé la question : la voix n'a plus besoin de monter.",
            notes="C'est la découverte qui surprend le plus : une question peut finir en "
                  "descendant. Ce n'est pas le point d'interrogation qui fait monter la "
                  "voix, c'est l'absence de mot interrogatif.")

    d.cartes("Trois autres mouvements", "Ce que la voix fait encore", [
        ("Au milieu d'une phrase longue",
         "La voix monte un peu à chaque virgule : ce n'est pas fini."),
        ("Dans une énumération",
         "Un plat, une chaise, et votre bonne humeur : montée, montée, descente."),
        ("Dans une exclamation",
         "La voix part haut et redescend, avec force sur la première syllabe."),
        ("Dans un ordre",
         "Répondez-moi avant jeudi. La voix descend, fermement."),
    ], notes="La deuxième carte sert le plus au défi 2 : c'est ce qui rend une invitation "
             "facile à noter au téléphone. Chaque montée dit à celui qui écrit qu'il "
             "reste une information après.")

    d.tableau("À l'oreille", "La même phrase, deux intentions",
              ['On entend', 'Ce que ça veut dire'],
              [["Vous venez samedi. (descend)", "On vous informe : c'est prévu"],
               ["Vous venez samedi ? (monte)", "On vous demande : répondez"],
               ["Quelle bonne nouvelle. (descend)", "On constate, sans chaleur"],
               ["Quelle bonne nouvelle ! (haut puis bas)", "On se réjouit avec vous"],
               ["Quelle bonne nouvelle ? (monte)", "On doute, et ça blesse"]],
              cle=1,
              notes="Dire les cinq versions à voix haute, dans le désordre, et faire "
                    "deviner. Les trois dernières préparent le défi 3 : la troisième et "
                    "la cinquième sont deux façons de rater une félicitation.")

    d.pratique('Écoute', "La voix monte, ou elle descend ?",
               "Écoutez chaque phrase et choisissez.", [
        ("Vous venez samedi ?", "monte — question sans mot interrogatif"),
        ("La fête est le 7 juin.", "descend — affirmation"),
        ("Il faut apporter quelque chose ?", "monte"),
        ("Quand est-ce que ça commence ?", "descend — « quand » a posé la question"),
        ("C'est dans la ruelle ?", "monte"),
        ("Qui organise la fête ?", "descend"),
        ("Vous avez changé d'horaire ?", "monte"),
        ("Quelle bonne nouvelle !", "descend — exclamation : haut, puis bas"),
    ], corrige=True,
       notes="Reprendre ensuite dans l'activité interactive, exercice prPhon : les dix "
             "cartes sont écoutables une à une, ce qui permet de réécouter autant de fois "
             "qu'il le faut. C'est un exercice qui se refait en autonomie.")

    d.piege("Croire qu'il faut « est-ce que » pour poser une question",
            "Est-ce que vous venez samedi ? (à chaque fois)",
            "Vous venez samedi ?",
            "« Est-ce que » est correct, mais lourd à l'oral. Entre voisins, on laisse "
            "la voix faire le travail. Gardez « est-ce que » pour l'écrit et pour les "
            "situations officielles.",
            notes="Beaucoup d'élèves ont appris « est-ce que » comme la seule forme "
                  "correcte. Les rassurer : elle l'est. Mais l'intonation seule est ce "
                  "qu'ils entendront quatre fois sur cinq dans la rue.")

    d.piege("Dire une exclamation comme une question",
            "Quelle bonne nouvelle ? (la voix monte)",
            "Quelle bonne nouvelle ! (haut, puis descente)",
            "Avec la voix qui monte, vous avez l'air de mettre la nouvelle en doute. "
            "L'exclamation part haut sur « quelle » et redescend jusqu'au point.",
            notes="Faire pratiquer en binôme : l'un annonce une bonne nouvelle inventée, "
                  "l'autre réagit. Ne corriger que la mélodie, jamais les mots.")

    d.billet(
        "Écrivez deux phrases identiques : une affirmation et une question.",
        exemples=[
            "Par exemple : Vous travaillez samedi. / Vous travaillez samedi ?",
            "Dites-les à voix haute à votre voisin de table avant de sortir.",
        ],
        notes="Le billet oblige à produire la paire, pas seulement à la reconnaître. "
              "Écouter deux ou trois paires à voix haute avant la sortie.")

    return d.save(dossier)
