# -*- coding: utf-8 -*-
"""B1 · Première écoute : de quoi ça parle ?
Bloc B « Défi 1 · Le reportage » · couleur acier · 75 min.
Source : extrait `t1` (le reportage), exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n7-actualite/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Première écoute : de quoi ça parle ?",
        chapeau="Un reportage dure trois minutes et personne ne le répète. "
                "On ne le comprend pas d'un coup : on l'écoute trois fois, et "
                "chaque écoute a sa question.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 1. Prévenir le groupe : l'extrait d'aujourd'hui "
                  "est long, beaucoup plus long que ceux des modules précédents. C'est "
                  "voulu, et personne n'est censé tout comprendre à la première écoute.")

    d.objectifs([
        "suivre un reportage long sans décrocher ;",
        "repérer, à la première écoute, le sujet, le lieu et les personnes ;",
        "accepter de perdre des phrases sans arrêter d'écouter ;",
        "connaître la méthode des trois écoutes et savoir pourquoi elle marche.",
    ], notes="Le troisième objectif est un objectif de comportement, pas de langue. "
             "C'est pourtant celui qui débloque le plus d'élèves.")

    d.declencheur(
        'Écoute', "Écoutez sans rien noter. Que retenez-vous ?",
        image=IMG + 'local-vide.jpg',
        pistes=[
            "De quoi parle-t-on ?",
            "Où cela se passe-t-il ?",
            "Combien de personnes différentes avez-vous entendues ?",
            "Y a-t-il un chiffre que vous avez retenu malgré vous ?",
        ],
        notes="Consigne stricte : crayons posés. La première écoute se fait sans écrire. "
              "Les élèves qui notent perdent le fil et confirment leur impression "
              "d'échec.")

    d.regle("Les trois écoutes",
            "Une écoute, une question. Jamais les trois en même temps.",
            precision="Première écoute : de quoi ça parle, où, et qui parle. Deuxième "
                      "écoute : les chiffres, les dates, les noms, avec le droit "
                      "d'arrêter et de revenir en arrière. Troisième écoute : le détail, "
                      "et surtout ce qui est confirmé par rapport à ce qui ne l'est pas.",
            notes="Diapositive à photographier. C'est la méthode du bloc entier : B1 "
                  "fait la première écoute, B2 la deuxième, B3 la troisième.")

    d.dialogue('Reportage · 1 de 3', "L'ouverture pose le sujet", [
        ("LUDOVIC", "Radio du Ruisseau, il est six heures dix. Un point de dépôt pour les contenants consignés pourrait ouvrir cet automne dans le quartier du Ruisseau.", True),
        ("LUDOVIC", "D'abord, les faits. L'ancien local de la caisse populaire, au coin de Boisjoli et de la 4e Avenue, est vide depuis deux ans.", True),
        ("LUDOVIC", "La Ville confirme qu'elle étudie ce local pour y installer un point de dépôt, c'est-à-dire un endroit où les citoyens rapportent leurs contenants vides et récupèrent leur consigne.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Un reportage annonce son plan dans les vingt premières secondes. Faire "
             "remarquer « D'abord, les faits » : le journaliste dit ce qu'il va faire "
             "avant de le faire.")

    d.dialogue('Reportage · 2 de 3', "Les gens concernés prennent la parole", [
        ("HÉLÈNE", "Je comprends que les gens veuillent une date. Mais je ne vais pas en donner une aujourd'hui pour la reprendre dans trois mois. Le dossier est à l'étude.", True),
        ("BENOÎT", "Moi, ça fait onze ans que je reprends les canettes à mon comptoir. Onze ans. Ce qui m'inquiète, c'est le stationnement.", True),
        ("MARJOLAINE", "Franchement, huit places de stationnement contre un service pour trois mille personnes ? Moi, je n'ai pas d'auto. Je marche.", True),
    ], notes="Trois voix, trois positions. Faire nommer chacune : l'élue prudente, le "
             "commerçant inquiet, la résidente sans auto. Aucune n'a tort, et c'est ce "
             "qui rend le dossier intéressant.")

    d.dialogue('Reportage · 3 de 3', "La fin résume tout", [
        ("LUDOVIC", "En ce qui concerne les heures d'ouverture, aucune information ne circule pour l'instant.", True),
        ("LUDOVIC", "En somme : un local vide, deux emplacements possibles, une décision attendue avant la fin de l'année, et un stationnement qui inquiète les commerçants.", True),
        ("LUDOVIC", "Le dossier sera présenté à la séance du conseil du 14 octobre. Ludovic Chagnon, Radio du Ruisseau.", True),
    ], notes="La phrase qui commence par « En somme » est le résumé du journaliste. Si "
             "un élève n'a retenu qu'une phrase du reportage, c'est celle-là qu'il faut "
             "qu'il ait. Le dire : la fin d'un reportage vaut une écoute à elle seule.")

    d.pratique('Compréhension', "Première écoute : vrai ou faux ?",
               "Répondez sans réécouter.", [
        ("Le reportage porte sur un point de dépôt de contenants consignés.", "vrai"),
        ("Le local est celui d'une ancienne caisse populaire.", "vrai"),
        ("Une seule personne est interrogée dans le reportage.", "faux - quatre voix en tout"),
        ("Hélène Ferron est conseillère du district du Ruisseau.", "vrai"),
        ("Benoît Sarrazin est le propriétaire du local visé.", "faux - il tient le dépanneur d'en face"),
        ("Marjolaine Cusson se déplace en automobile.", "faux - elle marche"),
        ("Le reportage se termine en annonçant une séance du conseil.", "vrai"),
    ], corrige=True,
       notes="Aucune de ces questions ne porte sur un chiffre : c'est délibéré. Les "
             "chiffres sont l'affaire de B2. Rassurer ceux qui ne les ont pas retenus.")

    d.billet(
        "En une phrase : de quoi parlait ce reportage ?",
        exemples=[
            "Une phrase, pas trois. Comme si vous le racontiez à quelqu'un dans l'escalier.",
            "Sans chiffre, sans date.",
        ],
        notes="Deux minutes. Comparer quelques billets à voix haute : la variété des "
              "formulations montre qu'on peut résumer juste de plusieurs façons.")

    return d.save(dossier)
