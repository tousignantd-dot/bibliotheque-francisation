# -*- coding: utf-8 -*-
"""B4 · Trouver sans chercher.
Bloc B « Défi 1 » · couleur acier · 50 min. Bilan du défi 1.
Source : exercice `t1nombre`, banc de vocabulaire.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre='Trouver sans chercher',
        chapeau="Lire l'affichette, demander, vérifier le chiffre, regarder "
                "en bas. Quatre réflexes qui transforment une heure "
                "d'épicerie en vingt minutes.",
        duree='50 minutes')

    d.titre(notes="Bilan du défi 1. La moitié de la séance est de la pratique orale à deux.")

    d.objectifs([
        "enchaîner les quatre réflexes ;",
        "comprendre un nombre dans une phrase ;",
        "réviser le vocabulaire du défi 1 ;",
        "préparer le jeu de rôle de la section « Je me lance ».",
    ])

    d.declencheur(
        'Rappel', "Sans vos notes : que faites-vous en arrivant à l'épicerie ?",
        pistes=[
            "Avez-vous une liste ?",
            "Regardez-vous les affichettes ?",
            "Demandez-vous, ou cherchez-vous ?",
            "Combien de temps y passez-vous ?",
        ],
        notes="Laisser parler trois ou quatre élèves. Les habitudes du groupe sont le vrai "
              "point de départ de cette séance.")

    d.tableau('Analyse', "Les quatre réflexes",
              ['Le réflexe', "Ce qu'il évite"],
              [["Lire l'affichette du bout de l'allée", "parcourir la rangée pour rien"],
               ["Demander au lieu de chercher", "vingt minutes dans quinze allées"],
               ["Vérifier le chiffre entendu", "aller dans la mauvaise allée"],
               ["Regarder aussi en bas", "croire qu'il n'y en a plus"]],
              cle=1,
              note="Trente secondes de questions valent vingt minutes de recherche.",
              notes="Diapo à photographier. C'est le résumé du défi 1.")

    d.cartes("Les mots du défi 1", "À revoir", [
        ("Les lieux",
         "une allée, une affichette, une tablette, un rayon, le fond, l'entrée, la caisse."),
        ("Les positions",
         "dans, au fond, au bout, à côté de, en face de, près de, en haut, au milieu, en bas."),
        ("Les demandes",
         "Excusez-moi. Je cherche… Où est… ? Pourriez-vous m'indiquer… ?"),
        ("Les vérifications",
         "Pardon ? Vous pouvez répéter ? Plus lentement. Cinq ou quinze ?"),
    ], notes="Diapo à photographier. C'est la liste de révision du défi 1.")

    d.regle("Le nombre dans la phrase",
            "Il arrive vite, et il ne se répète pas.",
            precision="« C'est allée cinq, au milieu, à côté du vinaigre. » Le nombre passe "
                      "en une demi-seconde, au milieu d'une phrase. C'est pour cela qu'on "
                      "le <b>répète à voix haute</b> tout de suite : « allée cinq », avant "
                      "même de remercier.",
            notes="Diapo à photographier. Répéter le chiffre à voix haute aide aussi à le "
                  "retenir jusqu'à l'allée.")

    d.piege("Retenir trois choses à la fois",
            "Allée cinq, au milieu, à côté du vinaigre, et le grand format en bas…",
            "Une chose à la fois, et on demande le reste sur place.",
            "La mémoire de travail ne tient pas quatre informations dans une langue qu'on "
            "apprend. Retenez le numéro d'allée — le reste se retrouve une fois sur place, "
            "et on peut toujours redemander.",
            notes="Conseil réaliste, qui soulage. Beaucoup d'élèves croient devoir tout "
                  "mémoriser.")

    d.pratique('Pratique · 1 de 2', "Qu'est-ce que ça veut dire ?",
               "Associez chaque expression à son sens.", [
        ("« Allée douze »", "le numéro d'une rangée"),
        ("« Trois dollars la livre »", "un prix au poids"),
        ("« Deux pour cinq dollars »", "un spécial : il faut en prendre deux"),
        ("« Quarante-deux quinze »", "un montant : 42 $ et 15 ¢"),
        ("« Format de 750 millilitres »", "la grosseur du contenant"),
    ], corrige=True, cols=1,
       notes="Utiliser l'exercice 4 du module. Il prépare le défi 2.")

    d.pratique('Pratique · 2 de 2', "À deux · la course complète",
               "Un client cherche trois produits ; le commis répond.", [
        ("Le client", "les quatre étapes, pour chaque produit"),
        ("Le commis", "répond vite, comme dans la vraie vie"),
        ("Une contrainte", "le commis dit un nombre difficile : 13, 15, 40, 50"),
        ("On change de rôle", "après trois produits"),
    ], cols=1,
       notes="Vingt minutes. La contrainte sur les nombres fait travailler A2 et B1 "
             "ensemble.")

    d.billet(
        "Écrivez votre liste d'épicerie de la semaine.",
        exemples=[
            "Six produits au moins.",
            "À côté de chacun : dans quelle allée il se trouve, si vous le savez.",
        ],
        notes="Fin du bloc B. Cette liste servira de matière première à la production "
              "écrite de la section « Je me lance ».")

    return d.save(dossier)
