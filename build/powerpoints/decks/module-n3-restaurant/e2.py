# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur framboise · 60 min.
Source : banc `FC_CARDS`, cartes mémoire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Seize mots, quatre familles, et une question : qu'est-ce que "
                "je suis maintenant capable de faire au comptoir d'un "
                "casse-croûte ?",
        duree='60 minutes')

    d.titre(notes="Dernière séance du module. Prévoir les cartes mémoire du module "
                  "interactif : la révision se fait à l'écran, en paires.")

    d.objectifs([
        "revoir les seize mots du module, par familles ;",
        "employer chaque mot dans une phrase ;",
        "évaluer ce qu'on est capable de faire ;",
        "nommer ce qui reste à travailler.",
    ])

    d.cartes("L'endroit et le menu", "Neuf mots", [
        ("un casse-croûte, le comptoir",
         "Le petit restaurant rapide, et le long meuble où on commande. Ce sont les "
         "deux mots qui nomment la situation entière."),
        ("le tableau du menu, un plateau",
         "Le panneau qu'on lit de loin, et le carré de plastique qu'on porte. L'un "
         "avant la file, l'autre pendant."),
        ("un format, une portion",
         "La grandeur qu'on choisit, et la quantité qu'on reçoit. Trois formats : "
         "petit, moyen, grand."),
        ("un breuvage, un accompagnement, un trio",
         "Ce qu'on boit, ce qui vient avec le plat, et les trois réunis à un seul prix."),
    ], notes="Faire dire chaque mot avec son article, puis dans une phrase complète.")

    d.cartes("Commander et le plateau", "Sept mots", [
        ("la caisse, le numéro de commande",
         "L'endroit où on paie, et le chiffre qu'on appelle quand le repas est prêt. On "
         "le répète toujours à voix haute."),
        ("pour emporter",
         "Le repas part dans un sac, avec un couvercle sur ce qui est liquide. La "
         "réponse à la question la plus déroutante du comptoir."),
        ("un ustensile, une serviette de table",
         "La fourchette et la cuillère, et le petit papier carré. Les deux sont presque "
         "toujours en libre-service."),
        ("un condiment, un couvercle",
         "Le sel, le poivre, le ketchup, la moutarde ; et le rond de plastique qui "
         "ferme un bol ou un verre."),
    ], notes="Faire retrouver chaque mot dans un vrai casse-croûte, en devoir. Ce qui ne "
             "se retrouve pas se réexplique.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez avec un mot du module.", [
        ("Le grand panneau au-dessus de la caisse est le ___ du menu.", "tableau"),
        ("Petit, moyen et grand sont trois ___ .", "formats"),
        ("La salade qui vient avec le sandwich est un ___ .", "accompagnement"),
        ("Le plat, l'accompagnement et le breuvage font un ___ .", "trio"),
        ("La fourchette et la cuillère sont des ___ .", "ustensiles"),
        ("Le sel et le ketchup sont des ___ .", "condiments"),
    ], corrige=True,
       notes="Exercice d'entrée. Il reprend exactement l'exercice 2 de « Je me lance » "
             "du module interactif.")

    d.tableau('Analyse', "Ce que le module a appris à faire",
              ['Compétence', "Ce qu'on sait faire"],
              [["Lire", "trouver un plat, un format et un prix sur un tableau de menu"],
               ["Écouter", "comprendre les cinq questions du préposé"],
               ["Parler", "commander poliment et demander ce qui manque"],
               ["Écrire", "une courte commande pour plusieurs personnes"]],
              cle=1,
              note="Commander au comptoir et lire un menu simple : les deux "
                   "intentions que le programme donne à cette situation.",
              notes="Diapo à photographier. C'est la carte du module entier, et le "
                    "point de départ de l'autoévaluation.")

    d.pratique('Autoévaluation', "Qu'est-ce que je suis capable de faire ?",
               "Pour chaque énoncé : pas encore, un peu, ou oui.", [
        ("Je trouve un plat, son prix et son format sur le tableau du menu.", ""),
        ("Je comprends « servi avec » et ce qu'un trio comprend.", ""),
        ("Je peux commander avec « je voudrais » et « s'il vous plaît ».", ""),
        ("Je peux choisir un format : petit, moyen ou grand.", ""),
        ("Je comprends les questions du préposé et je réponds.", ""),
        ("Je peux demander un ustensile, une serviette ou un condiment.", ""),
    ], corrige=False,
       notes="Les mêmes énoncés que dans le module interactif. Les élèves répondent à "
             "l'écran ; la diapositive sert à la mise en commun.")

    d.regle("Ce qui reste à faire, chacun le nomme",
            "« La prochaine fois, je vais demander… »",
            precision="Une seule chose, écrite en une phrase. C'est ce qui "
                      "reste du module dans un mois — davantage que les seize "
                      "mots.",
            notes="Faire dire la phrase à voix haute par chaque élève, en tour de table. "
                  "Cinq minutes, et le module se ferme sur du concret.")

    d.billet(
        "Écrivez la phrase de votre prochaine fois.",
        exemples=[
            "« La prochaine fois, je vais demander une cuillère tout de suite. »",
            "Gardez-la dans votre cahier.",
        ],
        notes="Fin du module. Rappeler que les cartes mémoire restent accessibles et "
              "que le jeu de rôle peut se refaire autant de fois qu'on veut.")

    return d.save(dossier)
