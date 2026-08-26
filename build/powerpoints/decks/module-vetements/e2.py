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
        chapeau="Quinze mots, six points de langue, six questions. Dernière "
                "séance : on rassemble, on révise, et chacun fait le point.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer.")

    d.objectifs([
        "rassembler le vocabulaire du module en trois familles ;",
        "réviser avec les cartes mémoire, seul ou à deux ;",
        "reformuler les points de langue en une phrase chacun ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire.",
    ])

    d.vocabulaire('Famille · 1 de 3', "Le vêtement et la taille", [
        ("un manteau", "Le vêtement d'extérieur long et chaud de l'hiver."),
        ("une cabine d'essayage", "Le petit espace fermé où on essaie."),
        ("la taille", "La grandeur d'un vêtement : petit, moyen, grand."),
        ("la pointure", "La grandeur d'une chaussure — jamais « taille »."),
        ("serré", "Trop petit, qui empêche de bouger."),
        ("une manche", "La partie qui couvre le bras."),
    ], notes="La distinction taille / pointure est celle qui revient le plus souvent. "
             "Dernier rappel.")

    d.vocabulaire('Famille · 2 de 3', "Le manteau et son entretien", [
        ("le duvet", "Les plumes légères qui remplissent un manteau chaud."),
        ("un capuchon", "La partie qui couvre la tête."),
        ("le mode d'entretien", "L'étiquette qui dit comment laver et sécher."),
        ("la sécheuse", "L'appareil qui sèche le linge."),
        ("imperméable", "Qui ne laisse pas passer l'eau."),
    ], notes="« La sécheuse » : le mot d'ici. En France, on dit « sèche-linge ». Le "
             "signaler sans en faire une leçon.")

    d.vocabulaire('Famille · 3 de 3', "Après l'achat", [
        ("un échange", "Rapporter un article et en prendre un autre."),
        ("un remboursement", "Rapporter un article et récupérer son argent."),
        ("la mise de côté", "Le magasin garde l'article, contre un dépôt."),
        ("un dépôt", "Une partie du prix payée d'avance."),
    ], notes="Ces quatre mots sont ceux que les élèves n'ont jamais entendus. Les faire "
             "répéter.")

    d.tableau('Les points de langue', "Une phrase chacun",
              ['Le point', 'En une phrase'],
              [["le féminin qu'on entend", "le -e réveille la consonne finale"],
               ["dire ce qui ne va pas", "degré + adjectif + endroit"],
               ["décrire un vêtement", "l'adjectif suit le nom, la couleur s'accorde"]],
              cle=1,
              note="Trois autres au tableau suivant.",
              notes="Faire reformuler chaque ligne par un élève différent avant d'afficher "
                    "la colonne de droite.")

    d.tableau('Les points de langue', "Une phrase chacun (suite)",
              ['Le point', 'En une phrase'],
              [["demander et donner un avis", "je trouve que, il me semble, à mon avis"],
               ["cinq dessins dans le col", "bac, triangle, carré, fer, cercle"],
               ["échanger", "facture, étiquettes, état, délai"]],
              cle=2,
              notes="La dernière ligne est celle que les élèves rapportent le plus souvent "
                    "comme utile.")

    d.regle("Ce qu'il faut retenir du module",
            "Un vêtement se choisit avec deux étiquettes, pas une.",
            precision="Celle du prix dit combien il coûte aujourd'hui. Celle du col dit "
                      "combien il coûtera, comment il se lave, et combien de temps il "
                      "durera. Kofi a acheté un manteau qu'il portera cinq hivers parce "
                      "qu'il a lu la deuxième.",
            notes="Diapo à photographier. C'est la phrase de clôture du module.")

    d.cartes('Réviser seul', "Trois façons de le faire", [
        ("Les cartes mémoire",
         "Dans l'activité interactive, section « Je retiens des mots ». La traduction est "
         "masquée par défaut."),
        ("Les trois exercices de vocabulaire",
         "Le mot et sa définition, le mot et l'image, le mot à écrire. Les mêmes quinze "
         "mots."),
        ("Les six mini-leçons",
         "Six panneaux « Ouvrir la mini-leçon », avec de l'audio. Ils restent accessibles "
         "après la fin du module."),
    ], notes="Montrer les trois à l'écran, une minute chacun.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux dire ce qui ne va pas avec un vêtement, et où.",
            "Je peux demander un avis et en donner un sans blesser.",
            "Je peux lire les cinq symboles de l'étiquette d'entretien.",
            "Je peux demander un échange, un remboursement ou une mise de côté.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire remplir "
              "là : elle est conservée avec les traces de l'élève.")

    return d.save(dossier)
