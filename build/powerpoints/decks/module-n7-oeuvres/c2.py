# -*- coding: utf-8 -*-
"""C2 · Les paroles du « Troisième étage »
Bloc C « Défi 2 » · couleur acier · compréhension écrite · 75 min.
Source : exercices `t2paroles` (type texte) et `t2img`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-oeuvres' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C2', section='acier',
        titre="Les paroles du « Troisième étage »",
        chapeau="Une chanson se lit comme un texte : d'abord sa structure, "
                "puis ce qui s'y filme, puis ce qui s'y répète.",
        duree='75 minutes')

    d.titre(notes="Distribuer les paroles sur papier. Les élèves doivent pouvoir "
                  "souligner le refrain et entourer les répétitions : c'est un "
                  "travail de crayon avant d'être un travail d'écran.")

    d.objectifs([
        "repérer la structure d'une chanson : couplet, refrain, fin ;",
        "séparer ce qui se filme de ce qui ne se filme pas ;",
        "relever les mots qui reviennent et se demander pourquoi ;",
        "retrouver dans le texte le passage qui répond à une question.",
    ], notes="Le quatrième objectif est la compétence de lecture du niveau : trouver "
             "l'endroit exact, et non résumer l'impression générale.")

    d.declencheur(
        'Observation', "Que voit-on dans cette chanson ?",
        image=IMG + 'sacs-sur-la-marche.jpg',
        pistes=[
            "Faites la liste des choses qu'on pourrait filmer.",
            "Combien y en a-t-il en tout ?",
            "Est-ce beaucoup, pour une chanson de vingt lignes ?",
            "Qu'est-ce qui n'est pas filmable, dans le refrain ?",
        ],
        notes="La classe trouve six ou sept objets. C'est peu, et c'est le point : "
              "une chanson dit beaucoup avec très peu de choses.")

    d.tableau('Analyse', "La structure, en cinq morceaux",
              ['Le morceau', 'Ce qu\'il fait'],
              [["Premier couplet", "l'heure, la glace, les sacs, la rampe neuve"],
               ["Refrain", "l'escalier a des idées, et elle n'arrive jamais"],
               ["Deuxième couplet", "la fenêtre, la boîte, les neuf promesses"],
               ["Refrain", "le même, mot pour mot"],
               ["Un seul vers de fin", "ce soir le sac est moins lourd"]],
              cle=0,
              notes="Diapositive à photographier. Faire remarquer que le refrain ne "
                    "change pas d'un mot : c'est la définition d'un refrain, et c'est "
                    "ce qui le rend repérable en dix secondes.")

    d.cartes('Analyse', "Six choses que la chanson nomme", [
        ("l'escalier en colimaçon", "couvert de glace, monté depuis le trottoir"),
        ("deux sacs d'épicerie", "sur une marche de béton enneigée"),
        ("la rampe neuve", "boulonnée sur un escalier vieux et rouillé"),
        ("la fenêtre allumée", "au troisième, vue d'en bas, un soir d'hiver"),
        ("la boîte de carton", "fermée, seule dans le corridor, depuis neuf ans"),
        ("la ruelle", "étroite, la neige qui tourne dans le vent"),
    ], cols=2,
       notes="Exercice `t2img` du module. Les six objets sont concrets, et pourtant "
             "trois d'entre eux portent autre chose. Demander lesquels.")

    d.regle("Une répétition n'est jamais un hasard",
            "Dans une chanson de vingt lignes, un mot répété trois fois est le "
            "sujet réel.",
            precision="Ici, le verbe « monter » revient trois fois dans le refrain "
                      "seul, et le nombre « neuf » revient deux fois : neuf ans, neuf "
                      "fois. Un mouvement qui recommence, une promesse qui se répète. "
                      "Le titre lui-même est un étage.",
            notes="Diapositive à photographier. Faire compter les répétitions avant "
                  "de chercher le sens : la méthode y mène toute seule.")

    d.tableau('Analyse', "Trois passages, trois lectures",
              ['Le passage', 'Ce qu\'il apporte'],
              [["Ils ont refait la rampe",
                "un pronom sans référent : ceux qui décident"],
               ["Tellement froid que j'oublie",
                "un degré et sa conséquence, travaillés en C4"],
               ["Le sac est moins lourd",
                "quelque chose a changé, et ce n'est pas le sac"]],
              cle=0,
              note="Le dernier vers ne s'explique pas. Il déplace, et il s'arrête là.",
              notes="Diapositive à photographier. Les deux premiers passages "
                    "annoncent C3 et C4 ; le troisième reste ouvert et doit le rester.")

    d.pratique('Lecture', "Retrouvez le passage",
               "Quel passage du texte répond à la question ?", [
        ("Quel passage donne l'heure et l'état de la rue ?", "il est six heures moins dix, la rue est en glace"),
        ("Quelle est la seule chose qui a été réparée ?", "la rampe est neuve, refaite en septembre"),
        ("Où un pronom désigne-t-il des gens jamais nommés ?", "ils ont refait la rampe"),
        ("Quel vers donne une pensée à l'escalier ?", "le troisième étage a des idées sur moi"),
        ("Quel objet n'a pas bougé depuis neuf ans ?", "la boîte de carton dans le corridor"),
        ("Quel vers final change quelque chose sans dire quoi ?", "ce soir le sac est moins lourd"),
    ], corrige=True,
       notes="Exercice `t2paroles` du module, qui compte onze questions. Six ici ; "
             "les cinq autres à l'écran. Exiger le passage exact, pas un résumé.")

    d.pratique('Production écrite', "Une image de votre langue",
               "Écrivez une image de votre langue première et expliquez-la.", [
        ("La phrase", "dans votre langue, puis traduite mot à mot"),
        ("Ce qu'elle montre", "la chose concrète qu'elle nomme"),
        ("Ce qu'elle veut dire", "en français, en une phrase"),
        ("Est-ce qu'elle marche en français ?", "oui, non, et pourquoi"),
    ], corrige=False,
       notes="Quinze minutes. C'est le meilleur exercice du bloc : chaque élève est "
             "expert de sa langue, et la classe découvre que l'image existe partout, "
             "avec des objets différents.")

    d.billet(
        "Quel objet de la chanson porte le plus de choses, selon vous ?",
        exemples=[
            "L'escalier, la rampe neuve, la boîte de carton, la fenêtre ?",
            "Une phrase pour dire pourquoi.",
        ],
        notes="Aucune bonne réponse. Lire trois billets à voix haute au début de C3 : "
              "trois lectures différentes du même objet, et personne n'a tort.")

    return d.save(dossier)
