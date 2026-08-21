# -*- coding: utf-8 -*-
"""A3 · Les seize mots du transport collectif.
Bloc A « Je découvre » · couleur framboise · 75 min. Vocabulaire.
Source : exercices `prVocab` et `prImg`, banc FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre='Les seize mots du transport collectif',
        chapeau="Quatre familles de mots : la station, les titres, l'achat, "
                "la grille. Seize mots qui reviennent dans les seize séances.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Elle vient après la phonétique pour que les "
                  "mots nouveaux soient dits correctement dès la première fois. Ouvrir "
                  "en demandant quels mots du transport chacun connaît déjà, et les "
                  "écrire au tableau sans corriger.")

    d.objectifs([
        "nommer ce qu'on trouve dans une station : le point de service, la borne, le tourniquet ;",
        "nommer les titres : le passage, l'hebdomadaire, le mensuel ;",
        "nommer les gestes de l'achat : recharger, valider, payer comptant ;",
        "nommer ce que dit la grille : la zone, la catégorie d'âge, la place réservée.",
    ])

    d.vocabulaire('Vocabulaire · 1 de 4', "Dans la station", [
        ("une carte OPUS", "la carte de plastique bleue et blanche, gardée des années"),
        ("le point de service", "le comptoir de la station, avec une personne derrière"),
        ("le tourniquet", "la barrière qui s'ouvre quand le titre est bon"),
        ("un passage", "un seul voyage, d'un point à un autre"),
    ], notes="Faire dire chaque mot avec son article. « Le tourniquet » est celui que "
             "personne ne connaît et que tout le monde utilise deux fois par jour.")

    d.vocabulaire('Vocabulaire · 2 de 4', "Les titres et les tarifs", [
        ("un titre de transport", "ce qu'on achète et qu'on met sur la carte"),
        ("un titre mensuel", "bon pour tout un mois, autant de fois qu'on veut"),
        ("un titre hebdomadaire", "bon pour une semaine, du lundi au dimanche"),
        ("le tarif réduit", "le prix plus bas pour les jeunes, les étudiants et les aînés"),
    ], notes="« Hebdomadaire » est un mot long : le faire répéter en quatre morceaux. "
             "Au comptoir, on dit presque toujours « l'hebdo », et il faut le savoir.")

    d.vocabulaire('Vocabulaire · 3 de 4', "Acheter et se déplacer", [
        ("recharger sa carte", "mettre un nouveau titre sur une carte qu'on a déjà"),
        ("valider son titre", "passer sa carte sur l'appareil pour que le voyage compte"),
        ("payer comptant", "payer avec de l'argent en papier et en pièces"),
        ("une correspondance", "le droit de changer de véhicule sans payer une deuxième fois"),
    ], notes="« Valider » est le mot dont l'oubli coûte une amende : insister. La "
             "correspondance surprend toujours — beaucoup d'élèves paient deux fois "
             "sans le savoir.")

    d.vocabulaire('Vocabulaire · 4 de 4', "Ce que dit la grille", [
        ("une zone tarifaire", "une partie du territoire qui a ses propres prix"),
        ("une catégorie d'âge", "un groupe de personnes qui paient le même prix"),
        ("une place réservée", "un siège gardé pour les personnes qui en ont le plus besoin"),
        ("le transport adapté", "le service pour les personnes qui ne peuvent pas prendre l'autobus ordinaire"),
    ], notes="Ces quatre mots sont ceux du bloc D. Les poser ici sans les développer : "
             "ils seront repris devant la grille elle-même.")

    d.tableau('Analyse', "Trois verbes du programme",
              ["Le verbe", "Ce qu'il veut dire"],
              [["se déplacer", "aller d'un endroit à un autre"],
               ["se repérer", "savoir où on est"],
               ["se renseigner", "aller chercher l'information, demander"],
               ["se perdre", "ne plus savoir où on est — ce qu'on veut éviter"]],
              cle=0,
              note="Les quatre se disent avec « se » : je me déplace, je me repère.",
              notes="Diapositive à photographier. Ce sont les verbes que le programme "
                    "rattache à cette situation. Faire conjuguer « je me déplace, tu te "
                    "déplaces » à l'oral, rapidement, sans tableau de conjugaison.")

    d.pratique('Vocabulaire', "Le mot et sa définition",
               "Dites de quel mot il s'agit.", [
        ("La carte de plastique bleue et blanche.", "une carte OPUS"),
        ("La barrière de la station qui s'ouvre.", "le tourniquet"),
        ("Le comptoir où on vend les titres.", "le point de service"),
        ("Mettre un nouveau titre sur sa carte.", "recharger sa carte"),
        ("Passer sa carte sur l'appareil en montant.", "valider son titre"),
        ("Le prix plus bas pour les aînés.", "le tarif réduit"),
    ], corrige=True,
       notes="C'est l'exercice de vocabulaire du module, sous forme orale. Enchaîner "
             "avec l'activité interactive, où les seize mots se travaillent six à la "
             "fois par glisser-déposer.")

    d.pratique('Observation', "Ce qu'on voit dans la station",
               "Décrivez chaque endroit en une phrase.", [
        ("Le comptoir du point de service.", "un guichet vitré, avec une ouverture en bas"),
        ("La rangée de tourniquets.", "avant les escaliers, un lecteur sur chacun"),
        ("La grille des tarifs.", "un grand panneau affiché au mur"),
        ("La borne de vente.", "une machine où on achète tout seul"),
        ("Les places réservées.", "les premiers sièges, en avant de l'autobus"),
    ], corrige=True,
       notes="Prépare l'exercice 3 de l'activité, qui fait glisser des photos sur ces "
             "mêmes phrases. Si le groupe a une station à proximité, la visiter : "
             "quinze minutes sur place valent une heure de diapositives.")

    d.billet(
        "Écrivez les quatre mots du transport qui vous manquaient avant aujourd'hui.",
        exemples=[
            "Je ne connaissais pas le mot ___ .",
            "Maintenant je sais que ___ veut dire ___ .",
        ],
        notes="Devoir court. Les mots qui reviennent le plus souvent dans les billets "
              "sont à reprendre en début de séance A4.")

    return d.save(dossier)
