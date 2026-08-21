# -*- coding: utf-8 -*-
"""A3 · Bonjour, bonsoir, bonne journée.
Bloc A « Je découvre » · couleur teal · 75 min.
Source : exercices `prMoment` et `prImg`, mini-leçon `prMoment`.

La séance des formules. Le programme du niveau 2 demande des « énoncés à
mémoriser » — salutations, politesse, souhaits — et c'est exactement ce
qu'on fait ici : deux familles de mots, ceux de l'arrivée et ceux du départ,
et le moment de la journée qui décide.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-bonjour/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre="Bonjour, bonsoir, bonne journée",
        chapeau="Les mots de l'arrivée et les mots du départ. On ne les "
                "échange pas.",
        duree='75 minutes')

    d.titre(notes="Séance de mémorisation. Ces formules ne s'analysent pas, elles "
                  "s'apprennent par cœur et se disent vite. Viser la vitesse, pas "
                  "l'explication.")

    d.objectifs([
        "choisir entre bonjour et bonsoir ;",
        "dire la bonne formule en partant ;",
        "nommer les moments de la journée ;",
        "saluer une personne connue et une personne inconnue.",
    ])

    d.declencheur(
        'Observation', "Quelle heure est-il, à votre avis ?",
        image=IMG + 'soir-fenetre.jpg',
        pistes=[
            "Fait-il jour ou nuit dehors ?",
            "Que dit-on quand on arrive à cette heure-là ?",
            "Et quand on part ?",
            "Dites-vous quelque chose à vos voisins le soir ?",
        ],
        notes="Projeter aussi l'image du matin (matin-dejeuner) et faire comparer. Les "
              "deux photos suffisent à poser la journée entière.")

    d.tableau('Analyse', "Deux familles de mots",
              ['En arrivant', 'En partant'],
              [["Bonjour", "Bonne journée"],
               ["Bonsoir", "Bonne soirée"],
               ["Salut (à un ami)", "Salut · À demain"],
               ["—", "Au revoir"]],
              cle=2,
              note="En arrivant, on salue. En partant, on souhaite quelque chose.",
              notes="Diapositive à photographier. Faire dire à voix haute chaque colonne "
                    "de haut en bas, puis mélanger.")

    d.vocabulaire('Vocabulaire', "Les moments de la journée", [
        ("le matin", "Le début de la journée, avant midi."),
        ("l'après-midi", "Après le dîner, avant le soir."),
        ("le soir", "La fin de la journée, quand il fait noir."),
        ("la nuit", "Quand tout le monde dort."),
    ], notes="Diapositive à photographier. Faire dire à chacun ce qu'il fait à chacun de "
             "ces moments : une phrase, pas plus. C'est déjà le défi 1 qui commence.")

    d.regle("Bonne nuit",
            "Se dit seulement à une personne qui va se coucher.",
            precision="Ce n'est pas un « au revoir ». À un commis, à huit heures du soir, "
                      "on dit « <b>bonne soirée</b> ». « Bonne nuit » se garde pour la "
                      "famille, sur le pas de la chambre.",
            notes="Diapositive à photographier. C'est l'erreur la plus fréquente et la "
                  "plus visible : elle vaut trois minutes d'insistance.")

    d.cartes("Quatre situations", "Que dit-on ?", [
        ("Vous entrez au dépanneur à 20 h", "Bonsoir !"),
        ("Vous sortez du dépanneur", "Merci, bonne soirée !"),
        ("Vous croisez un voisin le matin", "Bonjour !"),
        ("Vous quittez le cours, à demain", "Bonne journée ! À demain !"),
    ], cols=2, notes="Diapositive à photographier. Faire jouer les quatre situations "
                     "debout, en dix minutes, avant l'exercice écrit.")

    d.pratique('Compréhension', "Quel mot, à quel moment ?",
               "Écrivez ce qu'on dit dans chaque situation.", [
        ("Vous arrivez au centre à huit heures.", "Bonjour !"),
        ("Vous arrivez chez une voisine à sept heures du soir.", "Bonsoir !"),
        ("Vous partez le matin, la personne reste.", "Bonne journée !"),
        ("Vous partez après le souper.", "Bonne soirée !"),
        ("Vous revoyez la personne demain.", "À demain !"),
        ("Vous parlez à un ami dans la rue.", "Salut !"),
    ], corrige=True, cols=2,
       notes="Faire d'abord à l'oral, en groupe, puis à l'écrit. Six situations, pas "
             "davantage.")

    d.pratique('Pratique · en groupe', "Le tour de l'immeuble",
               "En groupe, debout, chacun joue un moment de la journée.", [
        ("Étape 1", "Chaque élève reçoit une heure : 7 h, 13 h, 19 h, 22 h."),
        ("Étape 2", "Circulez et saluez trois personnes."),
        ("Étape 3", "Chaque personne répond selon son heure à elle."),
        ("Étape 4", "Quittez-vous avec la bonne formule."),
    ], cols=1,
       notes="Vingt minutes, et c'est bruyant : c'est voulu. Circuler et corriger d'un "
             "mot, sans arrêter le groupe.")

    d.billet(
        "Notez ce que vous direz demain, à trois moments de la journée.",
        exemples=[
            "Le matin, au voisin : Bonjour !",
            "L'après-midi, en partant du centre : Bonne journée !",
            "Le soir, au dépanneur : Bonsoir !",
        ],
        notes="Devoir court, et vérifiable : demander au cours suivant qui l'a vraiment "
              "dit.")

    return d.save(dossier)
