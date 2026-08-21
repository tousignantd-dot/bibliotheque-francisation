# -*- coding: utf-8 -*-
"""A1 · Je voudrais m'inscrire.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `prVocab` et `pr1`.

Septième module court du projet. L'élève de niveau 2 tient une phrase à la
fois : les diapositives portent peu de mots, et chaque phrase projetée est
une phrase qu'il dira vraiment au comptoir du secrétariat.

La situation du programme est « Inscription ». Elle est la première démarche
que fait un adulte immigrant au Québec, souvent avant même de savoir dire
bonjour — et elle se joue devant un papier couvert de mots qu'il ne lit pas
encore. Le module commence donc par nommer le papier, pas par le remplir.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-inscription/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Je voudrais m'inscrire",
        chapeau="Nommer ce qu'il y a sur un comptoir de secrétariat et dire "
                "pourquoi on vient.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Commencer sans diapositive : demander à "
                  "chacun s'il se souvient du jour de sa propre inscription, et qui "
                  "l'accompagnait. Presque personne n'y est allé seul.")

    d.objectifs([
        "nommer cinq choses du secrétariat ;",
        "dire pourquoi on vient, en une phrase ;",
        "comprendre le mot « case » et le mot « formulaire » ;",
        "demander de répéter quand ça va trop vite.",
    ])

    d.declencheur(
        'Observation', "Où est-ce que cette photo a été prise ?",
        image=IMG + 'comptoir-secretariat.jpg',
        pistes=[
            "Qu'est-ce qu'il y a sur le comptoir ?",
            "Qu'est-ce qu'on vient faire ici ?",
            "Qu'est-ce qu'il faut apporter ?",
            "Vous, qu'est-ce que vous avez apporté le premier jour ?",
        ],
        notes="Laisser chercher le mot « secrétariat » avant de le donner. La quatrième "
              "piste ouvre toujours le groupe : chacun raconte le papier qui lui a "
              "manqué.")

    d.dialogue('Dialogue · 1 de 2', "Yara pousse la porte du secrétariat", [
        ("YARA", "Bonjour. Je voudrais m'inscrire au cours de français.", True),
        ("MME BOURGEOIS", "Bonjour ! Vous êtes au bon endroit. C'est ici, le secrétariat.", True),
        ("YARA", "C'est possible aujourd'hui ?", True),
        ("MME BOURGEOIS", "Oui. Voici le formulaire d'inscription.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. La première réplique est la "
             "phrase la plus utile du module : la faire répéter par chacun, debout, "
             "avant de continuer.")

    d.dialogue('Dialogue · 2 de 2', "Il y a beaucoup de cases", [
        ("YARA", "Il y a beaucoup de cases…", True),
        ("MME BOURGEOIS", "On les remplit ensemble. Une case à la fois.", True),
        ("YARA", "D'accord. Merci beaucoup, madame.", True),
        ("MME BOURGEOIS", "Asseyez-vous. On commence par votre nom.", True),
    ], notes="Quatre répliques, et une démarche qui devient possible. Faire remarquer "
             "que Yara dit qu'elle ne comprend pas — elle ne fait pas semblant.")

    d.tableau('Analyse', "Ce que dit Yara, ce que répond la secrétaire",
              ["Yara dit", "Madame Bourgeois répond"],
              [["Je voudrais m'inscrire.", "Vous êtes au bon endroit."],
               ["C'est possible aujourd'hui ?", "Oui. Voici le formulaire."],
               ["Il y a beaucoup de cases…", "Une case à la fois."],
               ["Merci beaucoup, madame.", "On commence par votre nom."]],
              cle=1,
              note="Yara dit une chose à la fois. La secrétaire répond une chose à la fois.",
              notes="Diapositive à photographier. Faire jouer les quatre lignes à deux, "
                    "debout, avant de passer au vocabulaire.")

    d.vocabulaire('Vocabulaire', "Les mots du secrétariat", [
        ("une inscription", "Ce qu'on fait pour entrer dans un cours."),
        ("un formulaire", "La feuille avec des cases vides à remplir."),
        ("une case", "Le petit espace vide où on écrit une seule réponse."),
        ("le secrétariat", "Le bureau du centre où on donne ses papiers."),
    ], notes="Diapositive à photographier. Faire répéter chaque mot avec son article : "
             "l'article s'apprend avec le mot, jamais après.")

    d.regle("« Je voudrais m'inscrire au cours de français. »",
            "Une seule phrase, et la porte s'ouvre.",
            precision="On dit d'abord <b>bonjour</b>, puis ce qu'on veut, puis on "
                      "attend. Personne n'a besoin de plus. « Je voudrais » est plus "
                      "poli que « je veux », et c'est la forme qu'on entend partout "
                      "au comptoir.",
            notes="Diapositive à photographier. Faire dire la phrase par chaque élève, "
                  "un par un, à voix haute. C'est la phrase la plus utile du module.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Yara veut s'inscrire au cours de français.", "vrai"),
        ("Madame Bourgeois dit que c'est le mauvais endroit.", "faux - elle est au bon endroit"),
        ("Le formulaire a beaucoup de cases.", "vrai"),
        ("Yara remplit le formulaire toute seule.", "faux - elles le remplissent ensemble"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement. Les faire d'abord à l'oral, en groupe, avant de "
             "les faire écrire.")

    d.pratique('Pratique · au comptoir', "Deux par deux, debout",
               "Vingt minutes. Un élève au comptoir, l'autre derrière.", [
        ("Étape 1", "A dit bonjour et dit pourquoi il vient."),
        ("Étape 2", "B répond « vous êtes au bon endroit » et tend une feuille."),
        ("Étape 3", "A dit qu'il ne comprend pas une case."),
        ("Étape 4", "B répond « une case à la fois », et on échange les rôles."),
    ], cols=1,
       notes="Prévoir de vraies feuilles : un formulaire vierge du centre, ou une "
             "photocopie. Le papier dans la main change complètement l'exercice.")

    d.billet(
        "Écrivez la phrase que vous direz au comptoir, et le nom de trois choses du secrétariat.",
        exemples=[
            "Je voudrais m'inscrire au cours de français.",
            "un formulaire",
            "une case",
            "le secrétariat",
        ],
        notes="Devoir court. Demander l'article avec le mot : c'est là qu'il s'apprend, "
              "et le corriger plus tard coûte trois fois plus cher.")

    return d.save(dossier)
