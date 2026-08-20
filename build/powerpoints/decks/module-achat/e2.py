# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur framboise · 60 min.
Source : cartes mémoire, banc de vocabulaire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Quinze mots, sept points de langue, six questions de rayon. "
                "Dernière séance : on rassemble, on révise, et chacun fait le "
                "point.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer.")

    d.objectifs([
        "rassembler le vocabulaire du module en quatre familles ;",
        "réviser avec les cartes mémoire, seul ou à deux ;",
        "reformuler les points de langue en une phrase chacun ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire.",
    ])

    d.vocabulaire('Famille · 1 de 4', "L'appareil", [
        ("un électroménager", "Un gros appareil de la maison."),
        ("une laveuse", "L'appareil qui lave le linge."),
        ("la capacité", "Ce qui entre dedans."),
        ("les dimensions", "Hauteur, largeur, profondeur."),
        ("économe", "Qui consomme peu d'eau ou d'électricité."),
    ], notes="Faire redire l'article avec chaque mot. Dernière occasion de le corriger.")

    d.vocabulaire('Famille · 2 de 4', "La garantie", [
        ("la garantie", "La promesse de réparer sans frais."),
        ("pièces et main-d'œuvre", "Ni la pièce ni le travail ne sont facturés."),
        ("un défaut de fabrication", "Un problème venu de l'usine."),
        ("la garantie prolongée", "Des années de plus, en option."),
        ("le déplacement", "La venue du technicien — souvent facturée à part."),
    ], notes="« Pièces et main-d'œuvre » est la formule à reconnaître : elle figure sur "
             "tous les contrats.")

    d.vocabulaire('Famille · 3 de 4', "Payer et se faire livrer", [
        ("un versement", "Une partie du prix, payée à une date donnée."),
        ("la livraison", "Le transport jusque chez soi."),
        ("l'installation", "Le branchement et la mise en marche."),
        ("la reprise", "Le magasin repart avec l'ancien appareil."),
        ("un bon de livraison", "Le papier qui dit quoi, quand, et ce qui est inclus."),
    ], notes="Livraison et installation : la distinction la plus rentable du module. "
             "Dernier rappel.")

    d.vocabulaire('Famille · 4 de 4', "Le mode d'emploi", [
        ("un boulon de transport", "La pièce qui bloque le tambour pendant le transport."),
        ("être de niveau", "Être bien droit sur le plancher."),
        ("un cycle", "Un programme complet, du début à la fin."),
        ("l'essorage", "La partie du cycle où le tambour tourne vite."),
        ("le tableau des problèmes", "La page qui dit quoi vérifier quand ça ne marche pas."),
    ], notes="Ces cinq mots valent quatre-vingt-dix dollars par appel de service évité. Le "
             "redire une dernière fois.")

    d.tableau('Les points de langue', "Une phrase chacun",
              ['Le point', 'En une phrase'],
              [["« un » et « pain »", "la graphie décide : un/um, ou in/ain/ein/im"],
               ["l'adjectif", "après le nom, sauf une petite liste"],
               ["ce et celui", "l'un accompagne, l'autre remplace"]],
              cle=1,
              note="Quatre autres au tableau suivant.",
              notes="Faire reformuler chaque ligne par un élève différent avant d'afficher "
                    "la colonne de droite.")

    d.tableau('Les points de langue', "Une phrase chacun (suite)",
              ['Le point', 'En une phrase'],
              [["la garantie", "les défauts d'usine, pas les accidents"],
               ["les deux futurs", "l'un pour la conversation, l'autre pour l'engagement"],
               ["le prix affiché", "ce n'est jamais le total"],
               ["le mode d'emploi", "quatre pages sur quarante"]],
              cle=2,
              notes="La troisième ligne est celle que les élèves rapportent le plus souvent "
                    "comme utile.")

    d.regle("Ce qu'il faut retenir du module",
            "Mesurez avant, demandez ce qui n'est pas dit, faites écrire ce qui est promis.",
            precision="Yin n'a pas appris à réparer une laveuse. Elle a appris à mesurer "
                      "son local, à demander ce que veut dire un chiffre, et à faire noter "
                      "sur le bon ce qu'on lui avait promis. Trois réflexes qui valent pour "
                      "tous les achats importants.",
            notes="Diapo à photographier. C'est la phrase de clôture du module.")

    d.cartes('Réviser seul', "Trois façons de le faire", [
        ("Les cartes mémoire",
         "Dans l'activité interactive, section « Je retiens des mots ». La traduction est "
         "masquée par défaut."),
        ("Les trois exercices de vocabulaire",
         "Le mot et sa définition, le mot et l'image, le mot à écrire. Les mêmes quinze "
         "mots."),
        ("Les sept mini-leçons",
         "Sept panneaux « En apprendre plus », avec de l'audio. Ils restent accessibles "
         "après la fin du module."),
    ], notes="Montrer les trois à l'écran, une minute chacun.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux dire l'espace dont je dispose et demander si l'appareil y entre.",
            "Je peux demander ce que couvre la garantie, et ce qu'elle ne couvre pas.",
            "Je comprends ce qui s'ajoute au prix affiché.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire remplir "
              "là : elle est conservée avec les traces de l'élève.")

    return d.save(dossier)
