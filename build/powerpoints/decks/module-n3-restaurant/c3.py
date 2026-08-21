# -*- coding: utf-8 -*-
"""C3 · Les cinq questions du préposé.
Bloc C « Défi 2 · Commander au comptoir » · couleur teal · 75 min.
Source : exercice `t2questions`, mini-leçon `t2questions`.

C'est la moitié « compréhension orale » de l'intention du programme :
« comprendre l'information donnée par le préposé ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre='Les cinq questions du préposé',
        chapeau="Commander, ce n'est pas surtout parler : c'est répondre. Le "
                "préposé pose toujours les mêmes cinq questions, à toute la "
                "file, dans le même ordre.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute. Prévoir les haut-parleurs : les cinq questions "
                  "doivent être entendues plusieurs fois, dites vite, comme au comptoir.")

    d.objectifs([
        "reconnaître les cinq questions à l'oreille ;",
        "répondre à chacune en deux mots ;",
        "distinguer une question à deux choix d'une question fermée ;",
        "demander de répéter sans gêne.",
    ])

    d.tableau('Analyse', "Trois questions, trois réponses",
              ['Le préposé demande', 'On répond'],
              [["Ce sera tout ?", "Oui, c'est tout, merci."],
               ["Avec salade ou avec frites ?", "Avec salade, s'il vous plaît."],
               ["Quel format ?", "Petit, s'il vous plaît."]],
              cle=1,
              note="Deux mots suffisent : le plat vient d'être nommé.",
              notes="Diapo à photographier. Faire répéter chaque paire question-réponse "
                    "par tout le groupe. Le tableau est coupé en deux : la suite est sur "
                    "la diapositive d'après.")

    d.tableau('Analyse', "Les deux dernières",
              ['Le préposé demande', 'On répond'],
              [["Pour ici ou pour emporter ?", "Pour ici."],
               ["Débit ou comptant ?", "Débit, s'il vous plaît."]],
              cle=1,
              note="Ce sont les deux qui surprennent le plus au début.",
              notes="Diapo à photographier. « Pour emporter » veut dire dans un sac ; "
                    "« comptant » veut dire en argent. Les deux méritent d'être "
                    "expliqués une fois, lentement.")

    d.regle("Une question à deux choix demande un des deux",
            "« Avec salade ou avec frites ? »",
            precision="Répondre « oui » ne dit rien : le préposé redemande, et "
                      "la file attend. Il faut nommer l'un des deux. C'est vrai "
                      "aussi pour « pour ici ou pour emporter ? » et pour "
                      "« débit ou comptant ? ».",
            notes="Diapo à photographier. C'est l'erreur la plus fréquente au comptoir, "
                  "et elle vient d'une bonne intention : dire oui pour être aimable.")

    d.pratique('Écoute', "Quelle réponse ?",
               "Écoutez la question, puis répondez en deux mots.", [
        ("Pour ici ou pour emporter ?  (vous mangez sur place)", "Pour ici."),
        ("Avec salade ou avec frites ?  (la salade)", "Avec salade, s'il vous plaît."),
        ("Quel format ?  (le plus petit)", "Petit, s'il vous plaît."),
        ("Ce sera tout ?  (vous avez fini)", "Oui, c'est tout, merci."),
        ("Débit ou comptant ?  (votre carte)", "Débit, s'il vous plaît."),
    ], corrige=True,
       notes="Dire les questions vite, comme au comptoir, sans les montrer. Les élèves "
             "répondent à voix haute, tous ensemble d'abord, puis un par un.")

    d.cartes("Ce que veulent dire les mots difficiles", "Quatre mots", [
        ("pour emporter",
         "Le repas part dans un sac, avec un couvercle sur ce qui est liquide. On dit "
         "aussi « pour apporter », mais « pour emporter » est le plus courant."),
        ("comptant",
         "En argent : billets et pièces. Beaucoup de casse-croûte prennent le comptant "
         "et le débit, mais pas la carte de crédit."),
        ("ce sera tout",
         "Le préposé demande si la commande est finie. On répond « oui, c'est tout » ou "
         "« non, j'aimerais aussi… »."),
        ("en sus",
         "Se dit d'un prix qui s'ajoute : « taxes en sus », « livraison en sus ». Le "
         "montant de la caisse sera plus haut que celui du tableau."),
    ], notes="Ces quatre mots ne se devinent pas. Les faire écrire dans le cahier avec "
             "leur définition, en français simple.")

    d.regle("Demander de répéter est normal",
            "« Pardon ? »  ·  « Pouvez-vous répéter, s'il vous plaît ? »",
            precision="Un casse-croûte est bruyant et les préposés parlent "
                      "vite, toute la journée, à des gens qui connaissent déjà "
                      "les questions. Demander de répéter n'est ni impoli ni "
                      "un aveu : c'est ce que tout le monde fait.",
            notes="Diapo à photographier. Faire dire les deux phrases à voix haute par "
                  "chaque élève. C'est la phrase de secours de tout le module.")

    d.pratique('Production orale', "Toute la commande, d'un bout à l'autre",
               "En paires : un préposé, un client. Cinq questions, cinq réponses.", [
        ("Le préposé", "pose les cinq questions dans l'ordre"),
        ("Le client", "salue, commande, répond en deux mots"),
        ("Le préposé", "donne un montant et un numéro"),
        ("Le client", "répète le numéro et remercie"),
    ], corrige=False,
       notes="Cinq minutes par paire, puis on change de rôle. Passer dans les rangées et "
             "noter les réponses en « oui » aux questions à deux choix.")

    d.billet(
        "Écrivez les cinq questions et vos cinq réponses.",
        exemples=[
            "Apprenez-les par cœur : c'est vingt secondes de travail.",
            "Ajoutez « Pardon ? » à la fin de la liste.",
        ],
        notes="Devoir court. Ces cinq paires sont ce qui reste du module dans un mois : "
              "insister sur la mémorisation.")

    return d.save(dossier)
