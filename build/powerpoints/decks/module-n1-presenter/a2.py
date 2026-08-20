# -*- coding: utf-8 -*-
"""A2 · Épeler son nom.
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : mini-leçon `prAlpha`, exercice `prAlpha` (cartes à écouter).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Épeler son nom',
        chapeau="Vingt-six lettres, et six qui se ressemblent. Ce sont "
                "toujours les mêmes qu'on doit répéter.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son. Écrire l'alphabet au tableau avant "
                  "l'arrivée du groupe et le laisser affiché toute la séance.")

    d.objectifs([
        "dire les lettres de l'alphabet ;",
        "entendre la différence entre E et I, G et J, M et N ;",
        "épeler son nom lentement ;",
        "demander de répéter une lettre.",
    ])

    d.declencheur(
        'Écoute', "Ces deux lettres sont-elles pareilles ?",
        pistes=[
            "E et I",
            "G et J",
            "M et N",
            "Laquelle est la plus difficile pour vous ?",
        ],
        notes="Faire écouter chaque paire deux fois. Demander de lever la main quand on "
              "entend la première, puis la seconde.")

    d.tableau('Analyse', "Les trois paires difficiles",
              ['On entend', 'On écrit'],
              [["« eu »", "E"],
               ["« i »", "I"],
               ["« jé »", "G"],
               ["« ji »", "J"]],
              cle=0,
              note="Deux autres au tableau suivant.",
              notes="Diapo à photographier. Faire répéter chaque paire en alternance : "
                    "E-I, E-I, puis G-J, G-J.")

    d.tableau('Analyse', "Les trois paires difficiles (suite)",
              ['On entend', 'On écrit'],
              [["« èm »", "M"],
               ["« èn »", "N"]],
              cle=0,
              note="Ces six lettres font presque toutes les erreurs d'épellation.",
              notes="Si un élève a l'une d'elles dans son nom, il devra la répéter souvent. "
                    "Le dire d'avance évite qu'il le prenne mal.")

    d.regle("Une lettre à la fois",
            "Avec une petite pause entre chaque.",
            precision="« A — M — I — N — A. » Puis on redit le mot en entier : "
                      "« Amina. » Cela permet à la personne de vérifier ce qu'elle a "
                      "écrit.",
            notes="Diapo à photographier. Faire la démonstration deux fois : une fois "
                  "trop vite, une fois bien. La différence s'entend tout de suite.")

    d.regle("Le truc qui marche",
            "« B comme bonjour. »",
            precision="On donne un mot qui commence par la lettre. Tout le monde le fait, "
                      "même les gens nés ici. Choisissez d'avance un mot pour chaque "
                      "lettre difficile de votre nom : vous n'aurez plus à chercher.",
            notes="Diapo à photographier. Faire choisir à chaque élève un mot pour la "
                  "lettre la plus difficile de son nom, et l'écrire au billet.")

    d.cartes("Pour faire répéter", "Trois phrases", [
        ("Pardon ?",
         "La plus courte. Elle suffit presque toujours."),
        ("Plus lentement, s'il vous plaît.",
         "La plus utile : ce n'est pas le volume qui manque, c'est la vitesse."),
        ("E ou I ?",
         "Donner les deux possibilités : la personne répond en un mot."),
    ], notes="Diapo à photographier. Ces trois phrases reviendront au défi 2.")

    d.piege("Épeler trop vite",
            "« amina » d'un seul souffle",
            "A — M — I — N — A.",
            "Vite, les lettres se collent et personne ne les distingue. Une petite pause "
            "entre chaque lettre suffit — et il vaut mieux être lent que de recommencer "
            "trois fois.",
            notes="Ne pas dramatiser : c'est le réflexe de tout le monde quand on est gêné.")

    d.pratique('Pratique · 1 de 2', "Quelle lettre entendez-vous ?",
               "Écoutez bien la fin du son.", [
        ("E", "la première"),
        ("I", "la deuxième"),
        ("G", "la première"),
        ("J", "la deuxième"),
        ("M", "la première"),
        ("N", "la deuxième"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module. Deux écoutes avant de corriger.")

    d.pratique('Pratique · 2 de 2', "À deux · épelez",
               "L'un épelle, l'autre écrit. Puis on vérifie.", [
        ("Étape 1", "épelez votre prénom, lentement"),
        ("Étape 2", "votre voisin l'écrit"),
        ("Étape 3", "vous vérifiez ensemble"),
        ("Étape 4", "on change de rôle, avec le nom de famille"),
    ], cols=1,
       notes="Vingt-cinq minutes. C'est l'activité la plus utile du bloc A : elle produit "
             "une vraie erreur, tout de suite corrigée.")

    d.billet(
        "Écrivez votre nom, et un mot pour chaque lettre difficile.",
        exemples=[
            "« B comme bonjour, E comme enfant. »",
            "Apprenez-les par cœur.",
        ],
        notes="Rendre à la séance suivante. Ces mots serviront tout le module.")

    return d.save(dossier)
