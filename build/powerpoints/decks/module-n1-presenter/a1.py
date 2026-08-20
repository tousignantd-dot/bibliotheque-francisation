# -*- coding: utf-8 -*-
"""A1 · Bonjour, je m'appelle…
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.

Premier module du niveau 1 : le stade est celui du grand débutant. Les
diapositives portent moins de mots que celles du niveau 4, et chaque phrase
projetée est une phrase que l'élève pourra dire lui-même.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n1-presenter/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Bonjour, je m'appelle…",
        chapeau="La première phrase qu'on dit dans une langue nouvelle. Elle "
                "sert le premier jour, et elle servira toute la vie.",
        duree='75 minutes')

    d.titre(notes="Première séance du module et, pour plusieurs, première séance de "
                  "français. Commencer debout : chacun dit son prénom à voix haute, en "
                  "cercle. Rien d'autre.")

    d.objectifs([
        "dire bonjour ;",
        "dire son nom ;",
        "comprendre la question « comment vous appelez-vous ? » ;",
        "épeler son nom de famille.",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il ici ?",
        image=IMG + 'accueil-centre.jpg',
        pistes=[
            "Où sommes-nous ?",
            "Qui arrive ?",
            "Que dit-on en arrivant ?",
            "Qu'est-ce qu'on demande ?",
        ],
        notes="Laisser répondre dans la langue qu'on peut. À ce stade, comprendre la "
              "situation compte plus que la dire en français.")

    d.dialogue('Dialogue · 1 de 2', "Le nom", [
        ("MADAME ROY", "Bonjour ! Comment vous appelez-vous ?", True),
        ("AMINA", "Bonjour. Je m'appelle Amina.", True),
        ("MADAME ROY", "Amina. Vous pouvez épeler, s'il vous plaît ?", True),
        ("AMINA", "A - M - I - N - A.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapo masquée. Puis afficher, faire répéter "
             "réplique par réplique, en chœur.")

    d.dialogue('Dialogue · 2 de 2', "Le nom de famille", [
        ("MADAME ROY", "Merci. Et votre nom de famille ?", True),
        ("AMINA", "Benali. B - E - N - A - L - I.", True),
        ("MADAME ROY", "Parfait. Bienvenue, madame Benali.", True),
    ], notes="« Bienvenue » ici est un vrai accueil. Plus loin dans le module, on verra "
             "qu'il veut aussi dire « de rien ».")

    d.tableau('Analyse', "Deux mots, deux choses",
              ['Le mot', 'Un exemple'],
              [["le prénom", "Amina"],
               ["le nom de famille", "Benali"],
               ["ici, on dit d'abord", "le prénom : Amina Benali"]],
              cle=2,
              note="Sur un formulaire, les deux cases sont séparées et nommées.",
              notes="Diapo à photographier. L'ordre prénom-nom n'est pas le même partout "
                    "dans le monde : le dire simplement, sans le commenter.")

    d.regle("Je m'appelle…",
            "La phrase la plus utile de toutes.",
            precision="On l'emploie partout : au centre, chez le médecin, au travail, "
                      "avec un voisin. On peut aussi dire, entre amis : « <b>Moi, "
                      "c'est</b> Amina. »",
            notes="Diapo à photographier. Faire répéter la phrase par chaque élève, une "
                  "fois, sans correction.")

    d.cartes("Épeler", "Trois choses à savoir", [
        ("On vous le demandera souvent",
         "Un nom qui ne vient pas d'ici ne s'écrit pas comme il se prononce. On demande "
         "aussi aux gens nés ici d'épeler leur nom."),
        ("Une lettre à la fois",
         "« A — M — I — N — A. » Avec une petite pause entre les lettres. Vite, les "
         "lettres se collent."),
        ("Le truc qui marche",
         "« B comme bonjour. » Tout le monde le fait. Choisissez d'avance un mot pour "
         "les lettres difficiles de votre nom."),
    ], notes="Diapo à photographier. Faire épeler son prénom par chaque élève, lentement.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La femme s'appelle Amina.", "vrai"),
        ("Son nom de famille est Benali.", "vrai"),
        ("On lui demande d'épeler son nom.", "vrai"),
        ("Amina ne dit pas bonjour.", "faux — elle dit bonjour"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement : à ce stade, six seraient trop.")

    d.pratique('Pratique · à deux', "Présentez-vous",
               "Deux par deux, trois fois avec trois personnes différentes.", [
        ("Étape 1", "Bonjour."),
        ("Étape 2", "Je m'appelle… (votre prénom)"),
        ("Étape 3", "Épelez votre nom de famille, lentement."),
        ("Étape 4", "Merci."),
    ], cols=1,
       notes="Vingt minutes. Circuler, écouter, ne corriger que ce qui empêche de "
             "comprendre. Le reste viendra.")

    d.billet(
        "Écrivez votre prénom et votre nom de famille.",
        exemples=[
            "En lettres détachées, bien lisibles.",
            "Puis épelez-les à voix haute, chez vous, trois fois.",
        ],
        notes="Devoir minuscule et essentiel. Plusieurs écriront leur nom en français pour "
              "la première fois.")

    return d.save(dossier)
