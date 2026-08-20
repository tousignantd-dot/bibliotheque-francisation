# -*- coding: utf-8 -*-
"""A1 · Excusez-moi, je cherche…
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`, mini-leçon `prLieu`.

Deuxième module court du projet. L'élève de niveau 2 tient une phrase à la
fois : les diapositives portent peu de mots, et chaque phrase projetée est
une phrase qu'il pourra dire lui-même en sortant.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-autobus/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Excusez-moi, je cherche…",
        chapeau="Aborder quelqu'un dans la rue et dire où on veut aller. "
                "Deux phrases suffisent pour ne plus jamais rester bloqué.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Commencer par une question au groupe, dans "
                  "la langue qu'on peut : « Vous êtes-vous déjà perdu ici ? » Presque "
                  "tout le monde lèvera la main. C'est le sujet du module.")

    d.objectifs([
        "aborder poliment une personne inconnue ;",
        "dire où on veut aller ;",
        "demander si c'est loin ;",
        "employer « à la », « au », « à l' ».",
    ])

    d.declencheur(
        'Observation', "Où sommes-nous, et que cherche-t-on ?",
        image=IMG + 'coin-rue.jpg',
        pistes=[
            "Que voit-on sur cette photo ?",
            "Comment s'appelle cet endroit, où deux rues se rencontrent ?",
            "Que fait-on quand on ne sait pas où aller ?",
            "À qui peut-on demander ?",
        ],
        notes="Laisser répondre dans la langue qu'on peut. Amener le mot « le coin » "
              "sans le forcer : il reviendra tout le module.")

    d.dialogue('Dialogue · 1 de 2', "Où est la bibliothèque ?", [
        ("HASSAN", "Excusez-moi, madame. Je cherche la bibliothèque.", True),
        ("MARIE-JOSÉE", "La bibliothèque ? Elle est sur la rue Bélanger.", True),
        ("HASSAN", "C'est loin d'ici ?", True),
        ("MARIE-JOSÉE", "Non, dix minutes à pied. Vous continuez tout droit.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Puis afficher et faire "
             "répéter réplique par réplique, en chœur. Insister sur « Excusez-moi » : "
             "c'est le mot qui ouvre la porte.")

    d.dialogue('Dialogue · 2 de 2', "Et après ?", [
        ("HASSAN", "Tout droit… et après ?", True),
        ("MARIE-JOSÉE", "Après le feu, vous tournez à droite. C'est au coin.", True),
        ("HASSAN", "Après le feu, à droite. Merci beaucoup.", True),
        ("MARIE-JOSÉE", "Bonne journée !", True),
    ], notes="Faire remarquer ce que Hassan fait à la dernière réplique : il redit ce "
             "qu'il a compris. C'est le cœur du module, et on y reviendra en B2.")

    d.tableau('Analyse', "Deux phrases pour aborder",
              ['Ce qu\'on dit', 'À quoi ça sert'],
              [["Excusez-moi, madame.", "on ouvre poliment"],
               ["Je cherche la bibliothèque.", "on dit où on va"],
               ["C'est loin d'ici ?", "on sait s'il faut marcher"]],
              cle=2,
              note="« Monsieur » ou « madame » après « excusez-moi » : c'est plus poli, "
                   "et c'est ce que tout le monde dit ici.",
              notes="Diapositive à photographier. Faire dire les trois phrases par chaque "
                    "élève, une fois, sans correction.")

    d.regle("Je vais à la, au, à l'",
            "Le même petit mot, trois formes.",
            precision="<b>à la</b> bibliothèque (féminin) · <b>au</b> parc (masculin) · "
                      "<b>à l'</b>école (voyelle). « À le » n'existe pas : les deux mots "
                      "se collent toujours et donnent <b>au</b>.",
            notes="Diapositive à photographier. Ne pas chercher à faire mémoriser le genre "
                  "de tous les noms : donner les cinq lieux du quartier que le groupe "
                  "fréquente vraiment, et s'en tenir là.")

    d.cartes("Les lieux du quartier", "Cinq lieux, cinq formes", [
        ("à la", "la bibliothèque, la pharmacie, la banque, la clinique"),
        ("au", "le parc, le marché, le CLSC, le dépanneur"),
        ("à l'", "l'école, l'hôpital, l'épicerie, l'arrêt"),
    ], cols=3, notes="Diapositive à photographier. Faire ajouter par le groupe deux lieux "
                     "du quartier réel, et les classer ensemble dans la bonne colonne.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Hassan cherche la bibliothèque.", "vrai"),
        ("La bibliothèque est sur la rue Bélanger.", "vrai"),
        ("C'est à une heure de marche.", "faux — dix minutes à pied"),
        ("Il faut tourner à gauche après le feu.", "faux — à droite"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement. Les faire d'abord à l'oral, en groupe, avant de "
             "les faire écrire.")

    d.pratique('Pratique · à deux', "Demandez votre chemin",
               "Deux par deux, trois fois avec trois personnes différentes.", [
        ("Étape 1", "Excusez-moi, madame. / Excusez-moi, monsieur."),
        ("Étape 2", "Je cherche… (un lieu du quartier)"),
        ("Étape 3", "C'est loin d'ici ?"),
        ("Étape 4", "Merci beaucoup."),
    ], cols=1,
       notes="Vingt minutes. Circuler, écouter, ne corriger que ce qui empêche de "
             "comprendre. Le genre des noms viendra plus tard.")

    d.billet(
        "Écrivez trois lieux de votre quartier, avec « je vais ».",
        exemples=[
            "Je vais à la pharmacie.",
            "Je vais au parc.",
            "Je vais à l'école.",
        ],
        notes="Devoir court. Demander d'écrire des lieux où ils vont vraiment : c'est ce "
              "qui fait retenir la forme.")

    return d.save(dossier)
