# -*- coding: utf-8 -*-
"""A1 · Ouvrez votre cahier.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.

Cinquième module court du projet. L'élève de niveau 2 tient une phrase à la
fois : les diapositives portent peu de mots, et chaque phrase projetée est
une phrase qu'il entendra vraiment le lendemain matin.

La situation du programme est « Salle de classe ». C'est la plus immédiate
de toutes : l'élève est déjà dedans. On commence donc par nommer ce qu'il a
sous les yeux avant de toucher à la moindre règle.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-classe/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Ouvrez votre cahier",
        chapeau="Nommer ce qu'on a sur son pupitre, et comprendre la première "
                "consigne du matin.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Commencer sans diapositive : dire « ouvrez "
                  "votre cahier » et regarder qui ouvre. Ceux qui n'ouvrent pas sont "
                  "exactement ceux pour qui le module est fait.")

    d.objectifs([
        "nommer six objets de la classe ;",
        "comprendre une première consigne ;",
        "dire qu'on n'a pas compris ;",
        "demander un objet qu'on n'a pas.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'il y a sur cette table ?",
        image=IMG + 'cahier-ouvert.jpg',
        pistes=[
            "Comment s'appelle cet objet ?",
            "Et celui-là, à côté ?",
            "Qu'est-ce que vous avez, vous, sur votre pupitre ?",
            "Qu'est-ce qui vous manque aujourd'hui ?",
        ],
        notes="Faire sortir les objets sur les pupitres pendant qu'on parle. Les élèves "
              "nomment en montrant : c'est le seul moment du module où le mot et l'objet "
              "sont ensemble sous les yeux.")

    d.dialogue('Dialogue · 1 de 2', "La première consigne du matin", [
        ("MADAME LEDUC", "Bonjour, tout le monde. Ouvrez votre cahier.", True),
        ("TARIQ", "Excusez-moi, madame. Je n'ai pas compris.", True),
        ("MADAME LEDUC", "Ouvrez votre cahier. Page douze.", True),
        ("TARIQ", "Page douze. Merci.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Insister sur la deuxième "
             "réplique : Tariq ne se cache pas, il le dit. C'est le comportement que le "
             "module veut installer, plus encore que le vocabulaire.")

    d.dialogue('Dialogue · 2 de 2', "Un crayon qui manque", [
        ("MYRIAM", "Madame, je n'ai pas de crayon.", True),
        ("MADAME LEDUC", "Myriam, prends un crayon dans la boîte.", True),
        ("MYRIAM", "Le crayon rouge ?", True),
        ("MADAME LEDUC", "Oui, le rouge. Maintenant, écoutez bien.", True),
    ], notes="Quatre répliques, et un problème réglé. Faire remarquer que Myriam ne "
             "s'excuse pas : elle dit ce qui manque, et c'est assez.")

    d.tableau('Analyse', "Ce que dit l'enseignante, ce que fait l'élève",
              ["L'enseignante dit", "L'élève fait"],
              [["Ouvrez votre cahier.", "il ouvre son cahier"],
               ["Page douze.", "il cherche le numéro 12"],
               ["Prends un crayon dans la boîte.", "il se lève et va en avant"],
               ["Écoutez bien.", "il arrête d'écrire et il regarde"]],
              cle=2,
              note="Une consigne n'attend pas de réponse : elle attend un geste.",
              notes="Diapositive à photographier. Faire jouer les quatre lignes pour "
                    "vrai : dire la consigne, et regarder la classe la faire.")

    d.vocabulaire('Vocabulaire', "Les objets de la classe", [
        ("un cahier", "Des feuilles attachées ensemble, où on écrit en classe."),
        ("un crayon", "Ce qu'on tient dans la main pour écrire."),
        ("une feuille", "Un papier blanc, seul, qui n'est pas dans un cahier."),
        ("un pupitre", "La petite table où l'élève s'assoit pour travailler."),
    ], notes="Diapositive à photographier. Faire répéter chaque mot avec son article : "
             "l'article s'apprend avec le mot, jamais après.")

    d.regle("« Je n'ai pas compris. »",
            "Quatre mots qui débloquent toute la matinée.",
            precision="On le dit <b>tout de suite</b>, pas à la fin du cours. On commence "
                      "par « <b>excusez-moi</b> », puis on dit la phrase. L'enseignante "
                      "répète : c'est son travail, et personne ne se fâche.",
            notes="Diapositive à photographier. Faire dire la phrase par chaque élève, un "
                  "par un, à voix haute. C'est la phrase la plus utile du module entier.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Madame Leduc demande d'ouvrir le cahier.", "vrai"),
        ("Tariq comprend la consigne tout de suite.", "faux — il demande de répéter"),
        ("Le travail est à la page douze.", "vrai"),
        ("Myriam prend un crayon bleu.", "faux — un crayon rouge"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés seulement. Les faire d'abord à l'oral, en groupe, avant de "
             "les faire écrire.")

    d.pratique('Pratique · en groupe', "Montrez et nommez",
               "Debout, avec les objets sur les pupitres.", [
        ("Étape 1", "L'enseignante montre un objet ; le groupe le nomme."),
        ("Étape 2", "Un élève montre ; les autres nomment."),
        ("Étape 3", "L'enseignante nomme ; chacun montre l'objet sur son pupitre."),
        ("Étape 4", "Un élève demande ce qui lui manque : « Je n'ai pas de… »"),
    ], cols=1,
       notes="Vingt minutes, et personne ne reste assis. L'étape 4 est la plus utile : "
             "elle transforme un mot de vocabulaire en demande réelle.")

    d.billet(
        "Écrivez le nom de quatre objets que vous avez dans votre sac.",
        exemples=[
            "un cahier",
            "un crayon",
            "une gomme à effacer",
            "une feuille",
        ],
        notes="Devoir court. Demander l'article avec le mot : c'est là qu'il s'apprend, "
              "et le corriger plus tard coûte trois fois plus cher.")

    return d.save(dossier)
