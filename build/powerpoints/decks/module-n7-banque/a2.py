# -*- coding: utf-8 -*-
"""A2 · Un taux, un montant, une durée
Bloc A « Je découvre » · couleur indigo · 60 min. Écoute des nombres.
Source : exercice `prChiffres` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Un taux, un montant, une durée',
        chapeau="Presque toutes les phrases d'un rendez-vous à la caisse "
                "contiennent un nombre. Ce qui décide de la compréhension, "
                "c'est le mot qui vient après.",
        duree='60 minutes')

    d.titre(notes="Séance courte et très orale. Le groupe écoute plus qu'il ne parle "
                  "pendant la première demi-heure, puis c'est l'inverse.")

    d.objectifs([
        "reconnaître à l'oreille un taux, un montant et une durée ;",
        "noter un grand nombre par tranches, à mesure ;",
        "dire un pourcentage à la québécoise : dix-neuf et quatre-vingt-dix ;",
        "demander le point de départ d'une durée.",
    ], notes="Le quatrième objectif est un réflexe de langue autant qu'un réflexe "
             "pratique : « trente jours » sans date de départ ne veut rien dire.")

    d.declencheur(
        'Écoute', "Trois phrases, trois nombres. Lequel est un prix ?",
        pistes=[
            "« cinq pour cent du solde »",
            "« cinq dollars de frais »",
            "« cinq jours ouvrables »",
            "Qu'est-ce qui change, dans les trois ?",
        ],
        notes="Dire les trois phrases à voix haute, sans les écrire. Le groupe trouve "
              "toujours, et il trouve pour la bonne raison : le mot qui suit.")

    d.regle("Le mot qui suit le nombre vous renseigne",
            "Le taux finit par « pour cent », le montant par « dollars », la durée par "
            "une unité de temps.",
            precision="Le nombre lui-même ne dit rien. C'est ce qui vient après qui "
                      "décide, et c'est aussi la partie de la phrase que l'on entend le "
                      "moins bien, parce qu'elle est dite vite et qu'elle porte "
                      "l'accent de fin de groupe.",
            notes="Diapositive à photographier. Faire écouter la fin des phrases plutôt "
                  "que leur début : c'est l'inverse du réflexe de tout le monde.")

    d.tableau('Analyse', "Ce qu'on entend, ce qu'on note",
              ["Ce qu'on entend", "Ce qu'on note"],
              [["dix-neuf et quatre-vingt-dix", "19,90 % par année"],
               ["neuf mille quatre cent douze", "9 412 $"],
               ["quatre-vingts mensualités", "80 mois"],
               ["cinq pour cent du solde", "le minimum légal"],
               ["trente jours de la réception", "une durée, avec son départ"]],
              cle=0,
              notes="Diapositive à photographier. Dicter la colonne de gauche et faire "
                    "écrire la colonne de droite : c'est l'exercice, pas le corrigé.")

    d.regle("Un grand nombre se note par tranches",
            "Le français dit « neuf mille, quatre cent, douze » : écrivez à mesure, "
            "n'attendez pas la fin.",
            precision="Attendre la fin du nombre pour l'écrire est ce qui fait perdre "
                      "les grands montants. Le découpage en tranches n'est pas un "
                      "hasard de la langue : il existe justement pour qu'on puisse "
                      "suivre à l'écrit.",
            notes="Exercice de dictée immédiate : cinq montants, dits une seule fois, "
                  "notés à mesure. Corriger au tableau.")

    d.pratique('Discrimination', "Taux, montant ou durée ?",
               "Écoutez chaque phrase et dites ce que le chiffre annonce.", [
        ("dix-neuf et quatre-vingt-dix pour cent", "un taux"),
        ("neuf mille quatre cent douze dollars", "un montant"),
        ("quatre-vingts mensualités", "une durée"),
        ("cent mille dollars par catégorie de dépôts", "un montant"),
        ("trente jours à compter de la réception", "une durée"),
        ("cinq pour cent du solde", "un taux"),
        ("sept cent quatre-vingts dollars", "un montant"),
        ("deux ans avant le cégep", "une durée"),
    ], corrige=True,
       notes="Lire les phrases à voix haute, une seule fois chacune. Ne pas montrer la "
             "diapositive pendant l'écoute : la révéler après pour la correction.")

    d.piege('Le piège', "dix-neuf dollars par mois",
            "dix-neuf et quatre-vingt-dix pour cent par année",
            "C'est l'erreur la plus coûteuse du module entier. Dix-neuf dollars par "
            "mois, ce serait 228 $ par année ; dix-neuf et quatre-vingt-dix pour cent "
            "sur 9 000 $, c'est environ 1 800 $. Le mot « pour cent » fait toute la "
            "différence, et il est dit à la fin.",
            notes="Refaire le calcul au tableau devant le groupe. C'est le moment de la "
                  "séance où quelqu'un dit toujours : « je pensais que c'était par "
                  "mois ». Le laisser dire.")

    d.pratique('Production', "Dites-le à voix haute",
               "À deux : l'un lit le chiffre écrit, l'autre dit ce que c'est.", [
        ("3,10 %", "trois et dix pour cent, un taux"),
        ("152 $", "cent cinquante-deux dollars, un montant"),
        ("80 versements", "quatre-vingts versements, une durée"),
        ("7 000 $", "sept mille dollars, un montant"),
        ("5 %", "cinq pour cent, un taux"),
        ("21 jours", "vingt et un jours, une durée"),
    ], corrige=True,
       notes="Circuler et écouter la virgule : « trois et dix » plutôt que « trois "
             "virgule dix » est la forme d'ici, et les deux se comprennent.")

    d.billet("Écris trois phrases : une avec un taux, une avec un montant, une avec "
             "une durée. Prends les chiffres de ta vraie vie ou invente-les.",
             exemples=["Mon taux est de quatorze pour cent par année.",
                       "Je paie deux cents dollars par mois.",
                       "Il me reste dix-huit mois de paiements."],
             notes="Deux minutes. Les billets montrent tout de suite qui confond encore "
                   "le taux et le montant.")

    return d.save(dossier)
