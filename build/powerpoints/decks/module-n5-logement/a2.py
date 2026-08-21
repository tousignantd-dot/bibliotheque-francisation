# -*- coding: utf-8 -*-
"""A2 · Sur, dans ou à : ce qu'on entend vraiment.
Bloc A « Je découvre » · couleur indigo · 75 min.
Source : exercice `prPhon` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Sur, dans ou à : ce qu'on entend vraiment",
        chapeau="Vous connaissez « sur », « dans », « à ». Vous connaissez "
                "« le », « la », « les ». Et pourtant, au téléphone, la phrase "
                "passe sans que vous reconnaissiez rien.",
        duree='75 minutes')

    d.titre(notes="Séance de phonétique. Elle vient tôt dans le module parce que tout le "
                  "défi 1 se passe au téléphone : sans ces fusions, l'appel est "
                  "incompréhensible.")

    d.objectifs([
        "entendre que la préposition et le déterminant se collent à l'oral ;",
        "reconnaître sur le, sur la, dans la, dans les, à la dans une phrase ;",
        "distinguer « dans la » de « dans les » par la seule voyelle ;",
        "savoir que ce n'est pas du français mal parlé, mais la norme d'ici.",
    ])

    d.declencheur(
        'Écoute', "Combien de mots entendez-vous ?",
        pistes=[
            "« Les clés sont sur le comptoir. »",
            "Comptez les mots que vous entendez, pas ceux que vous devinez.",
            "Écrivez ce que vous avez entendu.",
            "Maintenant, regardez la phrase écrite.",
        ],
        notes="Lire la phrase deux fois, à vitesse normale, sans rien montrer. Presque "
              "personne n'entendra « sur le » en deux mots. C'est le but : faire vivre "
              "l'écart avant de l'expliquer.")

    d.regle("Deux mots écrits, une syllabe entendue",
            "À l'oral d'ici, la préposition et le déterminant se collent.",
            precision="Ce n'est pas de la mauvaise prononciation et ce n'est pas réservé "
                      "aux gens pressés. C'est le français parlé normal du Québec : une "
                      "avocate, une propriétaire et un professeur disent tous « dans boîte "
                      "aux lettres » quand ils parlent à vitesse normale.",
            notes="Diapositive à photographier. Rassurer : l'élève n'a pas mal appris, il "
                  "a appris la forme écrite, et personne ne lui a dit que l'oral diffère.")

    d.tableau('Les six fusions', "Ce qui est écrit, ce qui est entendu",
              ['On écrit', 'On entend'],
              [["sur le comptoir", "SUL comptoir — le « e » tombe"],
               ["sur la table", "SA table — le « r » tombe"],
               ["dans la boîte", "DAN boîte — voyelle allongée"],
               ["dans les chambres", "DIN chambres — la voyelle dit le pluriel"],
               ["dans un immeuble", "DUN immeuble"],
               ["à la propriétaire", "A propriétaire — une seule voyelle"]],
              cle=0,
              note="Le singulier et le pluriel ne se distinguent que par la voyelle.",
              notes="Diapositive à photographier. Faire répéter chaque ligne en chœur, "
                    "colonne de droite seulement, avant de montrer la gauche.")

    d.cartes("Ce qui disparaît", "Trois sons qui s'effacent", [
        ("Le « e » de « le »",
         "sur le → SUL. Le nom qui suit se colle : il n'y a plus de pause."),
        ("Le « r » de « sur »",
         "sur la → SA. C'est la fusion qui trompe le plus : « sur la table » "
         "ressemble à « sa table »."),
        ("Le « s » de « dans les »",
         "Il ne se prononce jamais. Seule la voyelle porte le pluriel : dan / din."),
        ("Le « l » de « à la »",
         "à la → A. Rien ne reste. Seule la longueur de la voyelle dit qu'il y "
         "avait deux mots."),
    ], notes="Insister sur la deuxième carte : c'est la seule qui crée une vraie ambiguïté "
             "de sens, et c'est le contexte qui tranche.")

    d.pratique('Discrimination', "Sur, dans ou à ?",
               "Écoutez et dites quelle préposition vous avez entendue.", [
        ("Les clés sont sur le comptoir.", "sur"),
        ("La lettre était dans la boîte aux lettres.", "dans"),
        ("Elle s'adresse à la propriétaire.", "à"),
        ("L'avis était sur la table de cuisine.", "sur"),
        ("Il y a du bois franc dans les chambres.", "dans"),
        ("Ils habitent dans un immeuble de six logements.", "dans"),
        ("Pas de barbecue sur un balcon.", "sur"),
        ("Le linge se lave dans une buanderie commune.", "dans"),
    ], corrige=True,
       notes="Lire chaque phrase à vitesse normale, sans détacher. Répéter à la demande, "
             "mais jamais en séparant les mots : ce serait supprimer la difficulté.")

    d.piege("Chercher deux mots au lieu d'une syllabe",
            "J'attends d'entendre « sur » puis « la ».",
            "J'écoute une seule petite syllabe au début du groupe.",
            "Si vous attendez deux mots, vous cherchez pendant que la phrase continue, et "
            "vous perdez la suite. Écoutez la syllabe, puis le nom qui suit : c'est le nom "
            "qui vous dira de quoi on parle.",
            notes="C'est la stratégie d'écoute la plus utile de la séance. La faire "
                  "pratiquer : le nom d'abord, la préposition ensuite.")

    d.pratique('Production', "À votre tour",
               "Lisez ces phrases à vitesse normale, en collant les mots.", [
        ("Les clés sont sur le comptoir.", "SUL comptoir"),
        ("L'avis était sur la table.", "SA table"),
        ("La lettre était dans la boîte aux lettres.", "DAN boîte"),
        ("Il y a du bois franc dans les chambres.", "DIN chambres"),
        ("Elle s'adresse à la propriétaire.", "A propriétaire"),
        ("Ils habitent dans un immeuble.", "DUN immeuble"),
    ], corrige=True,
       notes="Ne pas exiger la fusion en production : l'objectif du niveau 5 est de la "
             "COMPRENDRE. Ceux qui y arrivent en parlant y gagnent, mais ce n'est pas "
             "évalué ici.")

    d.billet(
        "Écoutez la radio ou la télévision cinq minutes cette semaine.",
        exemples=[
            "Notez une phrase où vous avez entendu « dans la » ou « sur le » collés.",
            "Écrivez-la comme vous l'avez entendue, puis comme elle s'écrit.",
        ],
        notes="Devoir d'écoute. Il montre que la fusion est partout, y compris chez les "
              "journalistes, ce qui règle la question du « français mal parlé ».")

    return d.save(dossier)
