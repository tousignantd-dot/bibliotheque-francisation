# -*- coding: utf-8 -*-
"""C1 · Mon premier hiver.
Bloc C « Défi 2 · Ce que j'ai vécu » · couleur acier · 60 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Mon premier hiver',
        chapeau="Il fera moins vingt demain. Mariama raconte son arrivée : "
                "l'aéroport en sandales, trois mois derrière une fenêtre, et "
                "une voisine qui a tout changé.",
        duree='60 minutes')

    d.titre(notes="Séance sensible : plusieurs élèves ont vécu une arrivée difficile. "
                  "Annoncer d'emblée que personne n'est obligé de raconter la sienne "
                  "aujourd'hui — la production personnelle vient en E1, et le sujet est "
                  "libre.")

    d.objectifs([
        "comprendre un récit de vie raconté à l'oral ;",
        "distinguer ce qui est le décor de ce qui est l'évènement ;",
        "repérer les mots qui situent dans le temps : le douze janvier, ce jour-là ;",
        "reconnaître qu'un récit avance par étapes, pas par explications.",
    ])

    d.declencheur(
        'Mise en situation', "De quoi vous souvenez-vous de vos premiers jours ici ?",
        pistes=[
            "Quel temps faisait-il ? Comment étiez-vous habillé ?",
            "Qui vous attendait ? Que vous a-t-on dit en premier ?",
            "Qu'est-ce qui vous a le plus surpris ?",
            "Qu'est-ce que vous ne saviez pas et que personne ne vous avait dit ?",
        ],
        notes="Cinq à dix minutes. Laisser parler ceux qui veulent, sans insister sur les "
              "autres. Ne rien corriger : c'est de l'écoute. Noter au tableau les mots de "
              "temps qui sortent — ils reviendront en C2.")

    d.dialogue('Dialogue · 1 de 3', "Des sandales, en janvier", [
        ("CHANTAL", "Il fait moins vingt demain. Tu vas encore me dire que tu aimes ça.", False),
        ("MARIAMA", "Maintenant, oui. Mon premier hiver, par exemple, ça a été autre chose.", True),
        ("MARIAMA", "Je suis arrivée le douze janvier. À l'aéroport, je portais une veste et des sandales.", True),
        ("CHANTAL", "Des sandales ! En janvier !", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Les deux répliques teintées contiennent le couple qui structure tout le bloc : "
             "« je suis arrivée » (l'évènement) et « je portais » (le décor). Ne pas encore "
             "nommer les temps — c'est la séance C2.")

    d.dialogue('Dialogue · 2 de 3', "Le froid, et le cousin", [
        ("MARIAMA", "Personne ne m'avait expliqué. Chez moi, il faisait trente degrés le matin même.", True),
        ("CHANTAL", "Et quand les portes se sont ouvertes ?", False),
        ("MARIAMA", "J'ai eu mal aux oreilles. Je pensais que j'étais malade.", True),
        ("MARIAMA", "Mon cousin m'attendait avec un manteau et des bottes dans un sac. Il avait tout prévu, sauf de me prévenir.", False),
    ], notes="La dernière réplique fait rire les groupes. La laisser vivre : l'humour "
             "détend un sujet qui peut être lourd.")

    d.dialogue('Dialogue · 3 de 3', "Ce qui a changé", [
        ("MARIAMA", "Les trois premiers mois, je ne sortais pas. Je regardais la neige par la fenêtre et je comptais les jours.", True),
        ("CHANTAL", "Qu'est-ce qui a changé ?", False),
        ("MARIAMA", "Une voisine m'a emmenée glisser avec ses enfants. J'ai compris ce jour-là qu'on pouvait aimer l'hiver.", True),
        ("MARIAMA", "Grâce à cette voisine, oui. Elle ne le sait même pas.", False),
    ], notes="« Grâce à » apparaît ici pour la première fois : le signaler, sans "
             "l'enseigner — c'est la séance D2. Demander seulement : est-ce une bonne ou "
             "une mauvaise chose ?")

    d.cartes('La structure du récit', "Quatre étapes, toujours les mêmes", [
        ("1 · Le décor",
         "Où, quand, comment c'était. « Je suis arrivée le douze janvier, je portais une "
         "veste et des sandales. »"),
        ("2 · Le problème",
         "Ce qui n'allait pas. « J'ai eu mal aux oreilles. Les trois premiers mois, je ne "
         "sortais pas. »"),
        ("3 · Le tournant",
         "Ce qui a changé, et grâce à qui. « Une voisine m'a emmenée glisser. »"),
        ("4 · Aujourd'hui",
         "Ce qu'on en garde. « Quatorze mois plus tard, je joue au volleyball par moins "
         "vingt. »"),
    ], notes="C'est le plan que les élèves suivront à la production orale de E1. Le faire "
             "recopier maintenant.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Elle savait qu'il ferait très froid à son arrivée.", "faux — personne ne lui avait expliqué"),
        ("Le matin de son départ, il faisait trente degrés chez elle.", "vrai"),
        ("Son cousin l'avait prévenue du froid avant son départ.", "faux — il avait tout prévu sauf ça"),
        ("Les trois premiers mois, elle sortait tous les jours.", "faux — elle ne sortait pas"),
        ("C'est une voisine qui l'a emmenée glisser.", "vrai"),
        ("Cette voisine sait qu'elle a changé la vie de Mariama.", "faux — elle ne le sait même pas"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. La dernière est la "
             "plus fine : elle demande d'avoir entendu la toute dernière phrase.")

    d.billet(
        "Notez trois mots ou expressions du récit qui situent dans le temps.",
        exemples=[
            "Exemple : « le douze janvier », « les trois premiers mois », « ce jour-là ».",
            "Pour chacun, dites s'il désigne un moment précis ou une durée.",
        ],
        notes="Ce billet prépare directement C2 : ces mots sont ceux qui décident du temps "
              "de verbe. Les recopier au tableau à la séance suivante.")

    return d.save(dossier)
