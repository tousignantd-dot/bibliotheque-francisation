# -*- coding: utf-8 -*-
"""B1 · La personne-ressource, un mardi soir
Bloc B « Défi 1 » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`, vocabulaire de la section `t1`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-classe' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="La personne-ressource, un mardi soir",
        chapeau="Une personne invitée en classe ne parle pas comme un "
                "dialogue. Elle annonce un plan, elle le suit, elle le "
                "referme — et elle répond mal aux questions vagues.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 1. Si c'est possible, inviter une vraie "
                  "personne-ressource dans les semaines qui suivent : la séance "
                  "prend alors une valeur qu'aucun enregistrement ne donne.")

    d.objectifs([
        "suivre un exposé grâce au plan que la personne annonce ;",
        "nommer les mots du sujet de recherche de l'équipe de Neusa ;",
        "distinguer ce qui rafraîchit une rue de ce qui la réchauffe ;",
        "poser une question qui obtient une réponse utilisable.",
    ], notes="Le premier objectif est le savoir-faire du défi ; les deux suivants "
             "sont du contenu. Le quatrième est travaillé toute la séance et évalué "
             "au billet de sortie.")

    d.declencheur(
        'Observation', "Deux rues de la même ville, le même jour",
        image=IMG + 'rue-erables.jpg',
        pistes=[
            "Combien de degrés d'écart, à votre avis ?",
            "Qu'est-ce qui fait la différence : les arbres, l'asphalte, autre chose ?",
            "Laquelle des deux rues habitez-vous ?",
            "Est-ce qu'une rue plus fraîche est une rue plus agréable ?",
        ],
        notes="La photo est la rue plantée ; le stationnement d'asphalte a été vu en "
              "A3. Les mettre en regard mentalement. Ne pas donner le chiffre : il "
              "arrive dans le dialogue, et au conditionnel.")

    d.dialogue('Dialogue · 1 de 4', "Elle annonce où elle s'en va", [
        ("PERRINE", "Avant de commencer, je vous dis où je m'en vais : je vais parler d'abord de ce qu'est un îlot de chaleur.", True),
        ("PERRINE", "Ensuite de ce que fait un arbre exactement, et enfin de ce qui se passe chez vous, à Rivière-Noire.", True),
        ("NEUSA", "Merci d'être venue. Est-ce qu'on peut vous arrêter vraiment, ou c'est une formule ?", True),
        ("PERRINE", "Vraiment. Une question au bon moment vaut mieux qu'une main levée pendant vingt minutes.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire relever les trois parties annoncées et les écrire au tableau : "
             "elles serviront de cases de notes pour toute la séance.")

    d.dialogue('Dialogue · 2 de 4', "Ce qui est mesuré, ce qui est estimé", [
        ("MIGUEL", "Ça dépasse de combien ?", True),
        ("PERRINE", "Ce qui est mesuré et certain : l'asphalte noir en plein soleil monte bien plus haut qu'une pelouse à côté.", True),
        ("PERRINE", "Ce qui est estimé : chez vous, l'écart serait d'une dizaine de degrés. Je dis serait, parce que la mesure a été prise une seule journée.", True),
        ("NEUSA", "Vous avez dit serait au lieu de est. C'est volontaire ?", True),
    ], notes="Le point du défi, et il arrive tôt. Faire remarquer que c'est l'élève "
             "qui pose la question, pas l'enseignante : la classe peut faire pareil.")

    d.dialogue('Dialogue · 3 de 4', "Deux choses, et deux seulement", [
        ("PERRINE", "La première, tout le monde la connaît : l'arbre porte de l'ombre, donc le sol sous lui ne chauffe pas.", True),
        ("PERRINE", "La deuxième, on l'oublie toujours. L'arbre pompe de l'eau par ses racines et il la rejette par ses feuilles, sous forme de vapeur.", True),
        ("PERRINE", "Et rejeter de la vapeur, ça consomme de la chaleur. Autrement dit, il refroidit l'air autour de lui.", True),
        ("MIGUEL", "Donc un grand arbre vaut plus que dix petits ?", True),
    ], notes="Le contenu le plus dense du module. Le faire redire par un élève avec "
             "ses mots avant de continuer : c'est le mécanisme que l'exposé du bloc "
             "E devra expliquer à son tour.")

    d.dialogue('Dialogue · 4 de 4', "Le mot que Neusa trouve", [
        ("NEUSA", "Je vous arrête, parce que je veux être sûre de bien noter. Si je comprends bien, ce qui compte, ce n'est pas le nombre d'arbres.", True),
        ("NEUSA", "C'est la surface couverte par les cimes. C'est ça ?", True),
        ("PERRINE", "C'est exactement ça, et vous venez de nommer le mot que je gardais pour la fin. On l'appelle la canopée.", True),
        ("PERRINE", "Dernier point : le difficile, ce n'est pas de planter. C'est d'arroser pendant trois ans.", True),
    ], notes="Deux choses ici : la reformulation de Neusa, qui est le geste du bloc "
             "D avant l'heure, et la dernière réplique, qui donne à l'équipe son "
             "angle. Les deux méritent d'être nommées.")

    d.vocabulaire('Vocabulaire', "Les mots du dossier", [
        ("une personne-ressource", "Quelqu'un qui connaît bien un sujet et qu'on invite pour l'entendre et le questionner."),
        ("un îlot de chaleur", "Un secteur dont la surface devient beaucoup plus chaude que celle des secteurs voisins."),
        ("la canopée", "La couverture formée par la cime des arbres, vue d'en haut."),
        ("l'évapotranspiration", "L'eau qu'un arbre pompe par ses racines et rejette en vapeur par ses feuilles."),
        ("une estimation", "Un chiffre approché, calculé à partir de ce qu'on sait, mais qui n'a pas été mesuré."),
        ("un arbre de rue", "Un arbre planté dans le trottoir ou en bordure de la chaussée."),
    ], notes="« Évapotranspiration » fait peur à l'écrit et se dit très bien : le "
             "découper en deux, « évapo » et « transpiration », puis le recoller.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la rencontre.", [
        ("Perrine annonce son plan avant de commencer.", "vrai"),
        ("Un îlot de chaleur est une journée très chaude.", "faux - c'est un secteur"),
        ("L'écart de dix degrés est présenté comme certain.", "faux - au conditionnel"),
        ("Un arbre rafraîchit de deux façons.", "vrai - l'ombre et la vapeur"),
        ("Trois jeunes arbres valent un arbre mature.", "faux - pas pour rafraîchir"),
        ("Le plus difficile est d'arroser trois ans.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le troisième "
             "prépare la séance B3 : c'est une affaire de temps de verbe.")

    d.billet(
        "Écrivez la question que vous poseriez à Perrine si elle revenait.",
        exemples=[
            "Une seule question, écrite en entier.",
            "Une question à laquelle un chiffre peut répondre.",
        ],
        notes="Devoir concret. Trier les questions reçues en deux tas — celles qui "
              "appellent un chiffre et celles qui appellent « ça dépend » — et "
              "commencer B2 par là.")

    return d.save(dossier)
