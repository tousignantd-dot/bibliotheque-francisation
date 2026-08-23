# -*- coding: utf-8 -*-
"""B1 · Première écoute : de quoi ça parle ?
Bloc B « Défi 1 · Où travaille-t-on, là-bas ? » · couleur acier · 75 min.
Source : reportage `t1` (répliques 1 à 8), exercice `t1vf`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-recherche' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Première écoute : de quoi ça parle ?",
        chapeau="Une émission de vingt minutes sur l'économie d'une région "
                "ne se comprend pas d'un coup. On l'écoute trois fois, et la "
                "première fois on ne cherche ni les chiffres ni les dates.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 1. Annoncer la méthode avant de faire entendre "
                  "quoi que ce soit : trois écoutes, trois questions différentes. "
                  "Sans cette annonce, le groupe s'épuise dès la première.")

    d.objectifs([
        "écouter un long reportage sans chercher à tout comprendre ;",
        "repérer le sujet, le lieu et les personnes interrogées ;",
        "reconnaître qu'une émission annonce son plan et le résume ;",
        "accepter de perdre des phrases entières sans décrocher.",
    ], notes="Le quatrième objectif est le plus important, et il ne se note pas. "
             "Le dire clairement : perdre des phrases est normal, y compris pour "
             "un francophone distrait.")

    d.declencheur(
        'Observation', "Qu'est-ce qu'on fabrique dans ce genre d'endroit ?",
        image=IMG + 'usine-aluminium.jpg',
        pistes=[
            "Combien de personnes peuvent y travailler ?",
            "Quels métiers, en dehors de ceux qui sont sur la chaîne ?",
            "Qui vérifie que le produit est conforme ?",
            "Y a-t-il une usine comme celle-là près de chez vous ?",
        ],
        notes="Faire venir « laboratoire », « contrôle », « qualité » avant l'écoute. "
              "Une usine n'emploie pas que des opérateurs, et c'est précisément le "
              "point du reportage.")

    d.regle("Trois écoutes, trois questions",
            "Première écoute : de quoi ça parle. Deuxième : les chiffres. "
            "Troisième : ce que les chiffres veulent dire.",
            precision="On ne mélange pas les trois. Chercher un pourcentage pendant "
                      "qu'on cherche encore le sujet, c'est manquer les deux. Le début "
                      "et la fin d'une émission valent une écoute à eux seuls : "
                      "l'un annonce le plan, l'autre le résume.",
            notes="Diapositive à photographier. C'est la méthode du bloc entier et "
                  "elle resservira en C1, pour la lecture.")

    d.dialogue('Reportage · 1 de 3', "Les trois questions de l'émission", [
        ("ODILE", "Bienvenue à la troisième émission de notre série sur les économies régionales.", True),
        ("ODILE", "Aujourd'hui, le Saguenay–Lac-Saint-Jean. D'abord les chiffres, ensuite les gens qui embauchent.", True),
        ("ODILE", "Et pour finir la question qui revient toujours : est-ce qu'on peut y refaire sa vie professionnelle ?", True),
        ("ODILE", "Pour comprendre ce que ces chiffres veulent dire, j'ai demandé à Ghislain Néron, économiste régional.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Les trente premières secondes annoncent le plan en toutes lettres. "
             "Le faire remarquer : c'est vrai de presque toutes les émissions.")

    d.dialogue('Reportage · 2 de 3', "Le chiffre le plus révélateur", [
        ("GHISLAIN", "Le premier chiffre à retenir n'est pas le plus gros, c'est le plus révélateur.", True),
        ("GHISLAIN", "Le secteur primaire occupe quatre virgule deux pour cent de l'emploi régional. Ailleurs au Québec, deux pour cent.", True),
        ("GHISLAIN", "Autrement dit, la région tire deux fois plus de son sol et de sa forêt que la moyenne.", True),
        ("ODILE", "Et la fabrication ?", True),
    ], notes="Ne pas s'arrêter sur les chiffres aujourd'hui : ils sont l'objet de B2. "
             "Ce qui compte ici, c'est de repérer QUI parle et de quel métier il est.")

    d.dialogue('Reportage · 3 de 3', "Sur le terrain", [
        ("ODILE", "Frédérick Gauthier-Simard dirige le laboratoire de contrôle d'Alumico, à Jonquière.", True),
        ("ODILE", "Combien de personnes travaillent dans votre laboratoire ?", True),
        ("FRÉDÉRICK", "Sept. Nous devrions être neuf. J'ai deux postes affichés depuis février.", True),
        ("FRÉDÉRICK", "Et je n'ai reçu que onze candidatures. Onze, en six mois.", True),
    ], notes="Faire relever les trois voix du reportage : une journaliste, un "
             "économiste, un employeur. Chacune parle d'un endroit différent, et "
             "c'est ce qui rend l'émission crédible.")

    d.tableau('Analyse', "Qui parle, et à quel titre",
              ['La personne', 'Ce qu\'elle apporte'],
              [["Odile Pominville, journaliste", "le plan, les questions, le résumé"],
               ["Ghislain Néron, économiste", "les chiffres, et leur comparaison"],
               ["Frédérick Gauthier-Simard, employeur", "ce qu'il vit dans son laboratoire"]],
              cle=0,
              note="Trois sources, trois natures d'information. Aucune ne remplace les autres.",
              notes="Diapositive à photographier. Le tableau revient en B2, sous forme "
                    "d'exercice d'association.")

    d.pratique('Compréhension', "Première écoute : vrai ou faux ?",
               "Répondez sans chercher les chiffres.", [
        ("L'émission porte sur le Saguenay–Lac-Saint-Jean.", "vrai"),
        ("C'est la première émission de la série.", "faux - c'est la troisième"),
        ("Ghislain Néron est économiste régional.", "vrai"),
        ("Frédérick Gauthier-Simard est propriétaire d'une scierie.", "faux - chef de laboratoire"),
        ("Le laboratoire d'Alumico se trouve à Jonquière.", "vrai"),
        ("Selon l'économiste, la région est une région de bureaux.", "faux - une région d'usines"),
        ("L'employeur conseille de téléphoner avant d'envoyer son curriculum vitæ.", "vrai"),
        ("La prochaine émission portera sur la Gaspésie.", "faux - sur Chaudière-Appalaches"),
    ], corrige=True,
       notes="Exercice `t1vf` du module interactif. Faire justifier chaque « faux » "
             "par la réplique exacte, en réécoutant si nécessaire.")

    d.billet(
        "Après une seule écoute, qu'est-ce que vous avez retenu ?",
        exemples=[
            "Trois choses suffisent.",
            "Ne vous corrigez pas : écrivez ce que vous avez vraiment gardé.",
        ],
        notes="Ces billets servent d'avant-après : les ressortir à la fin de B2, une "
              "fois les trois écoutes faites. La progression est spectaculaire et "
              "elle rassure.")

    return d.save(dossier)
