# -*- coding: utf-8 -*-
"""A1 · Bonjour, madame Roy.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.

Quatrième module court du projet. L'élève de niveau 2 tient une phrase à la
fois : les diapositives portent peu de mots, et chaque phrase projetée est
une phrase qu'il pourra dire lui-même en sortant.

Le niveau 1 apprend à dire son nom. Ici, on entre dans un échange — deux ou
trois répliques avec quelqu'un qu'on recroisera demain matin.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-bonjour/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Bonjour, madame Roy",
        chapeau="Deux phrases dans l'entrée de l'immeuble, et elles "
                "reviennent tous les matins.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Commencer debout : faire circuler le groupe "
                  "et demander à chacun de saluer trois personnes. On parle avant "
                  "d'expliquer.")

    d.objectifs([
        "dire bonjour à une personne qu'on croise ;",
        "répondre à « ça va ? » ;",
        "renvoyer la question avec « et vous ? » ;",
        "nommer les lieux et les gens de son immeuble.",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il ici ?",
        image=IMG + 'entree-immeuble.jpg',
        pistes=[
            "Où sont ces personnes ?",
            "Est-ce qu'elles se connaissent ?",
            "Que disent-elles, à votre avis ?",
            "Et vous, saluez-vous vos voisins ?",
        ],
        notes="La dernière question est la vraie : beaucoup d'élèves ne saluent personne "
              "dans leur immeuble parce qu'ils ne savent pas quoi dire. C'est de ça que "
              "le module s'occupe.")

    d.dialogue('Dialogue · 1 de 2', "Dans l'entrée, le matin", [
        ("NADIA", "Bonjour, madame Roy.", True),
        ("GILBERTE", "Bonjour, Nadia. Ça va ?", True),
        ("NADIA", "Ça va bien, merci. Et vous ?", True),
        ("GILBERTE", "Ça va. Tu vas au centre ce matin ?", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Puis afficher et faire "
             "répéter réplique par réplique, en chœur. Nadia est une élève comme eux ; "
             "madame Roy est sa voisine du deuxième.")

    d.dialogue('Dialogue · 2 de 2', "On se quitte", [
        ("NADIA", "Oui. Mon cours commence à huit heures et demie.", True),
        ("GILBERTE", "Bonne journée, alors.", True),
        ("NADIA", "Merci. Bonne journée, madame Roy.", True),
        ("GILBERTE", "À demain, Nadia.", True),
    ], notes="Faire remarquer que tout l'échange tient en huit répliques et dure trente "
             "secondes. Personne n'a besoin de plus.")

    d.tableau('Analyse', "Un échange en trois temps",
              ['Le moment', 'Ce qu\'on dit'],
              [["on arrive", "Bonjour."],
               ["on demande", "Ça va ?"],
               ["on répond, et on redemande", "Ça va bien, merci. Et vous ?"],
               ["on part", "Bonne journée ! À demain !"]],
              cle=2,
              note="Quatre lignes, et l'échange est complet. Le reste est du bonus.",
              notes="Diapositive à photographier. Faire jouer les quatre lignes deux par "
                    "deux, debout, avant de continuer.")

    d.vocabulaire('Vocabulaire', "Les mots de l'immeuble", [
        ("un voisin", "La personne qui habite tout près, dans le même immeuble."),
        ("un immeuble", "Une grande maison avec plusieurs logements."),
        ("une salutation", "Le petit mot qu'on dit en arrivant ou en partant."),
        ("le matin", "Le début de la journée, avant midi."),
    ], notes="Diapositive à photographier. Faire répéter chaque mot avec son article : "
             "l'article s'apprend avec le mot, jamais après.")

    d.regle("« Et vous ? »",
            "Trois mots qui gardent la conversation vivante.",
            precision="Sans eux, l'échange s'arrête après deux phrases. On répond d'abord "
                      "— « ça va bien, merci » — puis on renvoie la question : "
                      "« <b>et vous</b> ? » à une personne qu'on vouvoie, "
                      "« <b>et toi</b> ? » à un ami.",
            notes="Diapositive à photographier. C'est le geste le plus utile de toute la "
                  "séance : le faire répéter par chaque élève, un par un.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Nadia dit bonjour à madame Roy.", "vrai"),
        ("Nadia va travailler ce matin.", "faux — elle va au centre"),
        ("Le cours commence à huit heures et demie.", "vrai"),
        ("Les deux voisines se disent « à demain ».", "vrai"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement. Les faire d'abord à l'oral, en groupe, avant de "
             "les faire écrire.")

    d.pratique('Pratique · à deux', "Trente secondes dans l'entrée",
               "Deux par deux, debout, comme dans un vrai hall.", [
        ("Étape 1", "L'un arrive, l'autre descend l'escalier."),
        ("Étape 2", "Saluez, demandez « ça va ? »."),
        ("Étape 3", "Répondez et renvoyez la question."),
        ("Étape 4", "Quittez-vous : « bonne journée ! »."),
    ], cols=1,
       notes="Vingt minutes, et on change de partenaire trois fois. Debout : assis, ce "
             "n'est plus la même situation et les élèves le sentent.")

    d.billet(
        "Écrivez trois phrases que vous pouvez dire demain matin à un voisin.",
        exemples=[
            "Bonjour, madame.",
            "Ça va bien, merci. Et vous ?",
            "Bonne journée !",
        ],
        notes="Devoir court. Demander qu'ils les disent vraiment le lendemain, et qu'ils "
              "racontent au cours suivant ce qui s'est passé.")

    return d.save(dossier)
