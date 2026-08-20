# -*- coding: utf-8 -*-
"""A2 · Treize ou trente ?
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : mini-leçon `prNombres`, exercice `prNombres` (cartes à écouter).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Treize ou trente ?',
        chapeau="Six paires de nombres se ressemblent, et ce sont celles "
                "qu'on entend le plus souvent : un numéro d'allée, un prix, "
                "une quantité. Toute la différence est à la fin du mot.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son. Commencer en disant « treize » puis "
                  "« trente » sans prévenir, et demander au groupe ce qui change.")

    d.objectifs([
        "entendre la différence entre 13 et 30, 14 et 40, 15 et 50 ;",
        "savoir que c'est la fin du mot qui décide ;",
        "faire répéter en donnant les deux possibilités ;",
        "employer ces nombres dans un prix et un numéro d'allée.",
    ])

    d.declencheur(
        'Écoute', "Ces deux mots sont-ils différents ?",
        pistes=[
            "« treize » et « trente »",
            "« quatorze » et « quarante »",
            "Qu'est-ce qui change ?",
            "Le début, ou la fin ?",
        ],
        notes="Faire écouter les paires avant toute explication. Le groupe entend qu'il y a "
              "une différence bien avant de pouvoir la nommer.")

    d.tableau('Analyse', "La fin du mot décide",
              ['On entend « ze »', 'On entend « te »'],
              [["treize · 13", "trente · 30"],
               ["quatorze · 14", "quarante · 40"],
               ["quinze · 15", "cinquante · 50"],
               ["seize · 16", "soixante · 60"]],
              cle=0,
              note="La colonne de gauche vibre, celle de droite claque.",
              notes="Diapo centrale, à photographier. Faire lire la colonne de gauche, puis "
                    "celle de droite, puis en alternance.")

    d.regle("Écouter la fin, pas le début",
            "« tr… » ne dit rien : les deux commencent pareil.",
            precision="Le son <b>ze</b> — celui du z de « zéro » — annonce un nombre entre "
                      "13 et 16. Le son <b>te</b> — celui du t de « table » — annonce une "
                      "dizaine : 30, 40, 50, 60. La fin est plus courte que le début, mais "
                      "c'est elle qui porte toute l'information.",
            notes="Diapo à photographier. Beaucoup d'élèves écoutent le début et devinent "
                  "le reste : c'est la cause de presque toutes les erreurs.")

    d.cartes("Là où ces nombres apparaissent", "Trois endroits", [
        ("Le numéro d'allée",
         "« Allée treize » ou « allée trente » ? Une épicerie n'a pas trente allées : le "
         "contexte aide, mais il ne suffit pas toujours."),
        ("Le prix",
         "« Treize dollars » ou « trente dollars » ? Ici, le contexte n'aide pas du tout — "
         "et l'erreur coûte dix-sept dollars."),
        ("La quantité et la date",
         "« Quinze pommes », « le spécial finit le quinze ». Même son, deux usages "
         "différents."),
    ], notes="Le deuxième cas est celui qu'il faut retenir : à la caisse, il n'y a aucun "
             "indice pour deviner.")

    d.regle("Faire répéter, la bonne façon",
            "« Pardon, treize ou trente ? »",
            precision="Donner les <b>deux</b> possibilités est la façon la plus rapide de "
                      "régler la question : la personne répond en un mot. Demander « vous "
                      "pouvez répéter ? » fait redire la même phrase à la même vitesse — et "
                      "on n'entend pas mieux la deuxième fois.",
            notes="Diapo à photographier. C'est la technique la plus utile de toute la "
                  "séance, et elle vaut bien au-delà des nombres.")

    d.piege("Deviner d'après le contexte",
            "Trente dollars pour du pain ? Ça doit être treize.",
            "Pardon, treize ou trente ?",
            "Le contexte trompe : les prix ont monté, et un panier d'épicerie ordinaire "
            "dépasse souvent ce qu'on imagine. Une question de deux secondes vaut mieux "
            "qu'une supposition.",
            notes="Ne pas dramatiser : deviner juste arrive souvent. C'est quand on devine "
                  "faux que ça coûte cher.")

    d.pratique('Pratique · 1 de 2', "Quel nombre entendez-vous ?",
               "Écoutez chaque mot.", [
        ("treize", "13 — la fin vibre"),
        ("trente", "30 — la fin claque"),
        ("quatorze", "14"),
        ("quarante", "40"),
        ("quinze", "15"),
        ("cinquante", "50"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module. Deux écoutes avant de corriger.")

    d.pratique('Pratique · 2 de 2', "Dans une phrase",
               "Écoutez et écrivez le nombre en chiffres.", [
        ("Allée treize, à côté des conserves.", "13"),
        ("Trente dollars pour la semaine.", "30"),
        ("Quarante-deux dollars et quinze cents.", "42,15 $"),
        ("Le spécial finit le quinze.", "15"),
        ("Soixante millilitres, c'est très peu.", "60"),
    ], corrige=True, cols=1,
       notes="Plus difficile : le nombre est noyé dans une phrase. Faire écouter deux fois.")

    d.billet(
        "Écrivez cinq prix que vous avez payés cette semaine.",
        exemples=[
            "En chiffres et en lettres : « 13,45 $ — treize dollars et quarante-cinq ».",
            "Lisez-les à voix haute avant de les écrire.",
        ],
        notes="Rendre à la séance suivante. Corriger surtout la lecture à voix haute.")

    return d.save(dossier)
