# -*- coding: utf-8 -*-
"""A2 · Treize ou trente ?
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : mini-leçon `prSons`, exercice `prSons` (cartes à écouter).

Le seul point de phonétique du module, et il n'est pas décoratif : une date de
naissance, un numéro de local et un numéro de téléphone se jouent tous sur la
dernière syllabe d'un nombre.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Treize ou trente ?',
        chapeau="Deux nombres, une seule syllabe de différence — et une date "
                "de naissance qui change de vingt ans.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son. Écrire les nombres de 1 à 60 au "
                  "tableau avant l'arrivée du groupe et les laisser affichés toute la "
                  "séance.")

    d.objectifs([
        "entendre la fin d'un nombre ;",
        "distinguer 13 et 30, 14 et 40, 15 et 50 ;",
        "dire un nombre lentement ;",
        "faire répéter un chiffre qu'on n'a pas compris.",
    ])

    d.declencheur(
        'Écoute', "Ces deux nombres sont-ils pareils ?",
        pistes=[
            "treize · trente",
            "quatorze · quarante",
            "quinze · cinquante",
            "Lequel est le plus difficile pour vous ?",
        ],
        notes="Faire écouter chaque paire deux fois, sans rien écrire. Demander de lever "
              "une main pour le premier, deux pour le second.")

    d.tableau('Analyse · 1 de 2', "Les petits nombres finissent en « ze »",
              ['On entend', 'On écrit'],
              [["trei-ze", "13"],
               ["quator-ze", "14"],
               ["quin-ze", "15"],
               ["sei-ze", "16"]],
              cle=2,
              note="Le son « ze » vibre dans la gorge.",
              notes="Diapo à photographier. Marquer la coupure avec la main en la lisant : "
                    "le geste aide plus que l'explication.")

    d.tableau('Analyse · 2 de 2', "Les dizaines finissent en « te »",
              ['On entend', 'On écrit'],
              [["tren-te", "30"],
               ["quaran-te", "40"],
               ["cinquan-te", "50"],
               ["soixan-te", "60"]],
              cle=2,
              note="Le son « te » ne vibre pas : c'est un petit coup sec.",
              notes="Diapo à photographier. Faire poser la main sur la gorge et comparer "
                    "avec la diapositive précédente.")

    d.regle("Écoutez la fin, jamais le début",
            "Trei-ZE, tren-TE.",
            precision="Les petits nombres — 13, 14, 15, 16 — finissent tous par le son "
                      "<b>ze</b>, qui vibre. Les dizaines — 30, 40, 50, 60 — finissent "
                      "toutes par le son <b>te</b>, un petit coup sec. « Quat… » tout "
                      "seul ne dit rien : il faut attendre la fin du mot.",
            notes="Diapo à photographier. Faire poser la main sur la gorge : « ze » vibre, "
                  "« te » ne vibre pas. C'est vérifiable, donc mémorisable.")

    d.cartes("Les paires", "Quatre à connaître par cœur", [
        ("13 et 30",
         "Treize et trente. La plus fréquente, et celle qui fausse le plus de dates de "
         "naissance."),
        ("14 et 40",
         "Quatorze et quarante. Même début, fin différente."),
        ("15 et 50",
         "Quinze et cinquante. Plus facile : même le début change."),
        ("2 et 12",
         "Deux et douze. Une paire de plus, très fréquente au téléphone."),
    ], notes="Diapo à photographier. Dicter ensuite douze nombres pris dans ces paires, "
             "au hasard, et faire écrire les chiffres.")

    d.pratique('Compréhension', "Ze ou te ?",
               "Écoutez, puis dites si le nombre finit par « ze » ou par « te ».", [
        ("treize", "ze"),
        ("trente", "te"),
        ("quatorze", "ze"),
        ("quarante", "te"),
        ("quinze", "ze"),
        ("cinquante", "te"),
        ("seize", "ze"),
        ("soixante", "te"),
    ], corrige=True, cols=2,
       notes="Ce sont exactement les huit cartes à écouter de l'exercice `prSons`. Les "
             "faire d'abord ici, à l'oral, puis à l'ordinateur.")

    d.piege("Répondre sans vérifier",
            "Écrire 40 quand on entendait 14.",
            "Répéter le chiffre à voix haute avant de l'écrire.",
            "« Quatorze, un-quatre ? » — deux secondes, et plus d'erreur. Quand un chiffre "
            "compte (une date, un local, un numéro), on le fait toujours confirmer. Les "
            "gens d'ici le font aussi.",
            notes="Rassurer : faire répéter un chiffre n'est jamais impoli, c'est prudent.")

    d.pratique('Pratique · à deux', "Dictée de nombres",
               "L'un dit un nombre, l'autre l'écrit. Puis on échange.", [
        ("Série 1", "13 · 30 · 14 · 40"),
        ("Série 2", "15 · 50 · 16 · 60"),
        ("Série 3", "2 · 12 · 3 · 13"),
        ("Série 4", "votre âge, puis celui de votre voisin"),
    ], cols=1,
       notes="Vingt minutes. Circuler et écouter surtout la dernière syllabe de celui qui "
             "dicte : c'est souvent lui qui l'avale.")

    d.billet(
        "Écrivez trois nombres en chiffres, puis dites-les à voix haute.",
        exemples=[
            "Le numéro de votre appartement.",
            "Le jour de votre naissance.",
            "Le nombre de personnes chez vous.",
        ],
        notes="Ces trois nombres reviendront tous dans la fiche, aux séances B2 et C2.")

    return d.save(dossier)
