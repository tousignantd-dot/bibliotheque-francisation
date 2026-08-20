# -*- coding: utf-8 -*-
"""C4 · Donner un coup de main.
Bloc C · couleur acier · 55 min.
Source : dialogue `t2b`, exercice `t2b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre='Donner un coup de main',
        chapeau="Cette fois, c'est Rosa qui reçoit les consignes — et qui va "
                "devoir en donner. Compter les enfants, garder les serviettes, "
                "envoyer à la douche. Trois consignes, et de vraies responsabilités.",
        duree='55 minutes')

    d.titre(notes="Séance courte. Elle clôt le bloc C en renversant la situation : de celui "
                  "qui écoute à celui qui parle.")

    d.objectifs([
        "comprendre trois consignes données rapidement, à l'oral ;",
        "les répéter dans mes mots pour vérifier ;",
        "reconnaître le tutoiement entre collègues ;",
        "savoir qu'accepter d'aider est une façon d'entrer dans un groupe.",
    ])

    d.declencheur(
        'Mise en situation', "On vous demande un coup de main. Que répondez-vous ?",
        pistes=[
            "Acceptez-vous tout de suite, ou demandez-vous d'abord ce qu'il faut faire ?",
            "Que faites-vous si vous n'avez pas compris la consigne ?",
            "Est-ce que le bénévolat existe dans votre pays ? Sous quelle forme ?",
            "Qu'est-ce que ça change, d'aider une fois ?",
        ],
        notes="Cinq minutes. La quatrième piste est celle qui compte : le bénévolat est "
              "une des voies d'entrée les plus rapides dans un réseau local. Le dire.")

    d.dialogue('Dialogue · 1 de 2', "Ce qu'il faut faire", [
        ("DENIS", "Rosa, tu peux m'aider deux minutes ? Il me manque quelqu'un pour les petits.", False),
        ("ROSA", "Oui, bien sûr. Qu'est-ce que je fais ?", True),
        ("DENIS", "Assieds-toi au bout, là. Compte-les quand ils entrent dans l'eau.", True),
        ("ROSA", "Je les compte, d'accord. Et s'il en manque un ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Qu'est-ce que je fais ? » est la bonne réponse : accepter, puis demander. "
             "La faire répéter par le groupe.")

    d.dialogue('Dialogue · 2 de 2', "Les consignes, et la récapitulation", [
        ("DENIS", "Tu me le dis tout de suite, tu ne le cherches pas toi-même.", True),
        ("DENIS", "Donne-les-leur à la sortie, pas avant. Sinon elles traînent par terre.", True),
        ("DENIS", "Si un enfant a froid, envoie-le à la douche chaude. N'attends pas qu'il pleure.", True),
        ("ROSA", "D'accord. Compter, garder les serviettes, envoyer à la douche.", True),
    ], notes="La dernière réplique est la récapitulation en trois mots. C'est ce que le "
             "module enseigne depuis A1, appliqué à des consignes de travail.")

    d.tableau('Analyse', "Trois consignes, trois pronoms",
              ['La consigne', 'Ce que le pronom remplace'],
              [["Compte-les quand ils entrent.", "les enfants"],
               ["Tu me le dis tout de suite.", "le fait qu'il en manque un"],
               ["Donne-les-leur à la sortie.", "les serviettes, aux enfants"],
               ["Envoie-le à la douche chaude.", "l'enfant qui a froid"]],
              cle=2,
              note="La troisième ligne enchaîne deux pronoms : c'est la forme vue en C2.",
              notes="Faire retrouver chaque mot remplacé avant d'afficher. Le contexte "
                    "suffit presque toujours.")

    d.regle("Répéter, encore",
            "« Compter, garder les serviettes, envoyer à la douche. »",
            precision="Trois mots, une phrase. C'est la même technique qu'au comptoir en "
                      "A1, et elle vaut encore plus ici : une consigne mal comprise dans "
                      "une piscine, ce n'est pas un déplacement perdu, c'est un risque.",
            notes="Diapo à photographier. Faire répéter par deux élèves.")

    d.cartes('Le tutoiement entre collègues', "Ce qui change", [
        ("Denis tutoie Rosa",
         "Ils travaillent ensemble, même bénévolement. Le tutoiement est normal entre "
         "collègues d'une même activité."),
        ("Louise vouvoie Rosa",
         "Au comptoir, c'est un service : on vouvoie. La même personne peut être tutoyée "
         "et vouvoyée dans le même édifice."),
        ("Ce qu'on fait dans le doute",
         "On vouvoie. La personne dira elle-même « tu peux me tutoyer » si elle le "
         "souhaite. Ce sujet sera repris en D2."),
    ], notes="Annoncer D2 : la variété de langue est un point du programme et une vraie "
             "difficulté pour les élèves.")

    d.piege('Accepter sans demander',
            "— Tu peux m'aider ? — Oui oui. [et ne rien faire de ce qui était attendu]",
            "— Oui, bien sûr. Qu'est-ce que je fais ?",
            "Accepter est bien ; accepter en sachant quoi faire est mieux. La question "
            "« qu'est-ce que je fais ? » prend deux secondes et évite un malentendu qui, "
            "au bord d'une piscine, peut être sérieux.",
            notes="Faire jouer les deux versions. La différence est immédiate.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Rosa doit compter les enfants quand ils entrent dans l'eau.", "vrai"),
        ("S'il manque un enfant, elle doit le chercher elle-même.", "faux — elle prévient Denis"),
        ("Les serviettes se donnent à la sortie, pas avant.", "vrai"),
        ("Si un enfant a froid, il faut attendre qu'il le dise.", "faux — on l'envoie à la douche"),
        ("Rosa répète les trois consignes à la fin.", "vrai"),
        ("Denis vouvoie Rosa.", "faux — il la tutoie"),
    ], corrige=True,
       notes="La dernière ligne prépare D2. Demander pourquoi il la tutoie : la réponse "
             "vient toute seule.")

    d.billet(
        "Racontez en quatre phrases une fois où vous avez aidé quelqu'un, ou refusé d'aider.",
        exemples=[
            "Qu'est-ce qu'on vous a demandé ? Qu'avez-vous répondu ?",
            "Employez au moins une consigne avec un pronom.",
        ],
        notes="Bilan du bloc C. Les billets alimentent la production orale de E1.")

    return d.save(dossier)
