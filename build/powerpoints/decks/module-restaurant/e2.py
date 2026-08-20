# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur foret · 60 min.
Source : cartes mémoire, banc de vocabulaire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='foret',
        titre='Je retiens des mots',
        chapeau="Quinze mots, six points de langue, six questions. Dernière "
                "séance : on rassemble, on révise, et chacun fait le point.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer.")

    d.objectifs([
        "rassembler le vocabulaire du module en quatre familles ;",
        "réviser avec les cartes mémoire, seul ou à deux ;",
        "reformuler les points de langue en une phrase chacun ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire.",
    ])

    d.vocabulaire('Famille · 1 de 4', "Le menu", [
        ("la carte", "La liste de tout ce que le restaurant sert."),
        ("le menu du jour", "Un choix limité qui change chaque jour."),
        ("la table d'hôte", "Un prix fixe pour trois services."),
        ("à la carte", "Un plat seul, sans formule."),
        ("le plat du jour", "Le plat préparé seulement aujourd'hui."),
    ], notes="Ces cinq mots sont la compétence la plus rentable du module. Dernier rappel.")

    d.vocabulaire('Famille · 2 de 4', "Le repas", [
        ("une entrée", "Le premier service : soupe, salade."),
        ("le plat principal", "Le plat le plus important du repas."),
        ("un accompagnement", "Ce qui est servi à côté : riz, légumes, frites."),
        ("une carafe", "Le pichet d'eau qu'on met sur la table."),
        ("l'eau du robinet", "L'eau ordinaire, servie gratuitement ici."),
    ], notes="L'eau du robinet gratuite surprend encore, à la fin du module. La redire.")

    d.vocabulaire('Famille · 3 de 4', "Demander poliment", [
        ("je voudrais", "Pour dire ce qu'on veut."),
        ("je prendrais", "Pour commander un plat."),
        ("pourriez-vous", "Pour demander une action."),
        ("est-ce que je pourrais avoir", "Pour une petite chose."),
        ("excusez-moi", "Pour attirer l'attention."),
    ], notes="Ces cinq formes couvrent toutes les demandes du module — et beaucoup au-delà.")

    d.vocabulaire('Famille · 4 de 4', "L'addition", [
        ("l'addition", "Le papier qui donne le total à payer."),
        ("taxes comprises", "Le montant inclut déjà les taxes."),
        ("le pourboire", "Environ 15 %, ajouté par le client."),
        ("payer séparément", "Chacun paie sa part."),
        ("la facture", "Le reçu détaillé, utile si c'est pour le travail."),
    ], notes="« Taxes comprises » et « le pourboire s'ajoute » : la distinction à retenir "
             "de tout le bloc D.")

    d.tableau('Les points de langue', "Une phrase chacun",
              ['Le point', 'En une phrase'],
              [["le e qui tombe", "réinsère-le et la phrase réapparaît"],
               ["l'accueil", "on attend qu'on nous place"],
               ["les formules du menu", "quatre mots, quatre prix"]],
              cle=1,
              note="Trois autres au tableau suivant.",
              notes="Faire reformuler chaque ligne par un élève différent avant d'afficher "
                    "la colonne de droite.")

    d.tableau('Les points de langue', "Une phrase chacun (suite)",
              ['Le point', 'En une phrase'],
              [["je voudrais, pourriez-vous", "une question, pas un ordre"],
               ["demander et signaler", "signaler n'est pas se plaindre"],
               ["taxes et pourboire", "les taxes sont dedans, le pourboire s'ajoute"]],
              cle=2,
              notes="La dernière ligne est celle que les élèves rapportent le plus souvent "
                    "comme utile.")

    d.regle("Ce qu'il faut retenir du module",
            "Connaître l'ordre du repas vaut mieux que tout comprendre.",
            precision="Andrés n'a pas appris tout le vocabulaire de la cuisine. Il a appris "
                      "ce qui va arriver, dans quel ordre, et quelle question poser à "
                      "chaque moment. C'est ce qui lui permet d'inviter quelqu'un sans "
                      "appréhension.",
            notes="Diapo à photographier. C'est la phrase de clôture du module.")

    d.cartes('Réviser seul', "Trois façons de le faire", [
        ("Les cartes mémoire",
         "Dans l'activité interactive, section « Je retiens des mots ». La traduction est "
         "masquée par défaut."),
        ("Les trois exercices de vocabulaire",
         "Le mot et sa définition, le mot et l'image, le mot à écrire. Les mêmes quinze "
         "mots."),
        ("Les six mini-leçons",
         "Six panneaux « En apprendre plus », avec de l'audio. Ils restent accessibles "
         "après la fin du module."),
    ], notes="Montrer les trois à l'écran, une minute chacun.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je comprends la différence entre la carte, le menu du jour et la table d'hôte.",
            "Je peux signaler poliment un plat froid ou une erreur de commande.",
            "Je sais calculer le pourboire et je comprends l'addition.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire remplir "
              "là : elle est conservée avec les traces de l'élève.")

    return d.save(dossier)
