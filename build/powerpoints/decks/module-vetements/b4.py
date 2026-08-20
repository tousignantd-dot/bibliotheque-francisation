# -*- coding: utf-8 -*-
"""B4 · Ce qu'il faut vérifier.
Bloc B « Défi 1 » · couleur acier · 50 min. Séance de bilan du défi 1.
Source : exercice `t1verifier`, banc de vocabulaire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre="Ce qu'il faut vérifier",
        chapeau="Quatre gestes en cabine, trente secondes en tout. C'est ce "
                "qui sépare un manteau qu'on portera cinq ans d'un manteau "
                "qu'on regrettera en novembre.",
        duree='50 minutes')

    d.titre(notes="Bilan du défi 1. Séance courte : la moitié du temps est de la pratique "
                  "orale à deux.")

    d.objectifs([
        "faire les quatre vérifications de la cabine ;",
        "dire ce qui ne va pas en une phrase complète ;",
        "demander une autre taille ou une autre coupe ;",
        "réviser le vocabulaire du défi 1.",
    ])

    d.declencheur(
        'Rappel', "Sans regarder vos notes : que vérifie-t-on en cabine ?",
        pistes=[
            "Combien de choses ?",
            "Dans quel ordre ?",
            "Quel geste fait-on avec les bras ?",
            "Qu'est-ce qui doit rester possible sous le manteau ?",
        ],
        notes="Laisser chercher deux minutes. Le groupe retrouve en général trois des "
              "quatre points.")

    d.tableau('Analyse', "Les quatre vérifications",
              ['Le geste', "Ce qu'on cherche"],
              [["Lever les bras", "les épaules ne serrent pas"],
               ["Regarder le poignet, bras levé", "la manche le couvre encore"],
               ["Se regarder de loin", "la longueur descend aux genoux"],
               ["Glisser la main sous le manteau", "il reste la place d'un chandail"]],
              cle=0,
              note="Trente secondes. Chaque geste répond à une question précise.",
              notes="Diapo à photographier. Faire faire les quatre gestes debout, tous "
                    "ensemble, avec ce qu'ils portent.")

    d.regle("Une phrase, trois morceaux",
            "degré + adjectif + endroit",
            precision="« Il est un peu serré aux épaules. » C'est la phrase du défi 1. "
                      "Elle sert en magasin, mais aussi au téléphone, ou pour expliquer un "
                      "échange. Elle vaut d'être sue par cœur.",
            notes="Rappel de B2. Faire répéter la structure, pas la phrase exacte.")

    d.cartes("Les mots du défi 1", "À revoir", [
        ("Les mesures",
         "la taille, la pointure, petit, moyen, grand, la coupe, ajusté, ample."),
        ("Les problèmes",
         "serré, large, court, long, étroit, il flotte, il me serre, il ne ferme pas."),
        ("Les endroits",
         "aux épaules, aux bras, à la taille, à la poitrine, aux hanches, au cou."),
        ("Les demandes",
         "Auriez-vous la taille au-dessus ? Vous l'avez en plus petit ? Est-ce que je peux "
         "l'essayer ?"),
    ], notes="Diapo à photographier. C'est la liste de révision du défi 1.")

    d.piege("Essayer par-dessus un gros chandail",
            "J'ai essayé avec mon manteau de laine dessous.",
            "Essayer avec ce qu'on portera vraiment.",
            "Un manteau essayé par-dessus trop de couches semblera toujours petit ; essayé "
            "en t-shirt, il semblera parfait et sera trop juste en janvier. Essayez avec un "
            "chandail ordinaire — c'est ce que vous porterez la plupart du temps.",
            notes="Nuance utile : ni trop, ni rien.")

    d.pratique('Pratique · 1 de 2', "Que dire ?",
               "Une phrase complète pour chaque situation.", [
        ("Vous ne pouvez pas lever les bras.", "Il est trop serré aux épaules."),
        ("La fermeture ne monte pas.", "Il ne ferme pas à la poitrine."),
        ("Le manteau descend aux chevilles.", "Il est trop long pour moi."),
        ("Vous flottez dedans.", "Il est trop grand ; auriez-vous la taille en dessous ?"),
        ("Les manches couvrent vos mains.", "Les manches sont trop longues."),
    ], corrige=True, cols=1,
       notes="Chaque réponse doit contenir un degré, un adjectif et un endroit.")

    d.pratique('Pratique · 2 de 2', "À deux · en cabine",
               "Un client, une conseillère. Trois vêtements, trois problèmes.", [
        ("Le client", "essaie, fait les quatre vérifications, dit ce qui ne va pas"),
        ("La conseillère", "demande où ça serre, propose une taille ou une coupe"),
        ("On change de rôle", "après trois vêtements"),
    ], cols=1,
       notes="Vingt minutes. Circuler et noter deux formulations réussies à lire au groupe "
             "à la fin.")

    d.billet(
        "Notez la taille et la pointure que vous faites, en français.",
        exemples=[
            "« Je fais un moyen. » « Je fais du 9. »",
            "Ajoutez une phrase sur ce qui ne vous va jamais.",
        ],
        notes="Fin du bloc B. La dernière consigne fait produire la structure du défi 1 "
              "sans le dire.")

    return d.save(dossier)
