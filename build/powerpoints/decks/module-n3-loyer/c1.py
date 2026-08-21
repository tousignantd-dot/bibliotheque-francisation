# -*- coding: utf-8 -*-
"""C1 · Bonjour, je vous appelle pour l'annonce.
Bloc C « Défi 2 · Téléphoner pour visiter » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Bonjour, je vous appelle pour l'annonce",
        chapeau="Au téléphone, il n'y a ni gestes, ni visage, ni papier à "
                "montrer. Il reste la première phrase, et elle décide de tout "
                "l'appel.",
        duree='75 minutes')

    d.titre(notes="Première séance du bloc C, et celle que le groupe redoute le plus. Le "
                  "dire d'entrée : téléphoner dans une langue nouvelle est difficile "
                  "pour tout le monde, et c'est justement pour ça qu'on s'y prépare "
                  "pendant quatre séances.")

    d.objectifs([
        "dire pourquoi on appelle, dès la deuxième phrase ;",
        "répondre à la question « vous êtes combien de personnes ? » ;",
        "comprendre un loyer, une heure et une adresse dits au téléphone ;",
        "répéter le rendez-vous avant de raccrocher.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui est difficile au téléphone ?",
        pistes=[
            "Est-ce que vous téléphonez en français ? À qui ?",
            "Qu'est-ce qui est plus difficile qu'en personne ?",
            "Qu'est-ce que vous faites quand vous ne comprenez pas ?",
            "Est-ce que vous demandez de répéter, ou est-ce que vous dites oui ?",
        ],
        notes="Beaucoup avoueront dire oui sans avoir compris. Ne pas moraliser : "
              "montrer plutôt qu'une phrase de trois mois — « pouvez-vous répéter » — "
              "règle le problème, et c'est ce qu'on va apprendre.")

    d.dialogue('Dialogue · 1 de 3', "Vous êtes combien de personnes ?", [
        ("CLAUDINE", "Oui, allô ?", True),
        ("DILNOZA", "Bonjour, madame. Je vous appelle pour l'annonce du quatre et demie.", True),
        ("CLAUDINE", "Bonjour. Oui, il est encore libre. Vous êtes combien de personnes ?", True),
        ("DILNOZA", "Nous sommes trois : mon mari, mon garçon de six ans et moi.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire compter les phrases : Dilnoza dit pourquoi elle appelle en une seule "
             "phrase, la deuxième de l'appel. C'est la règle à retenir de toute la "
             "séance.")

    d.dialogue('Dialogue · 2 de 3', "J'aimerais poser trois questions", [
        ("DILNOZA", "J'aimerais poser trois questions, si vous avez une minute.", True),
        ("CLAUDINE", "Allez-y, je vous écoute.", True),
        ("DILNOZA", "Est-ce que le chauffage est vraiment compris dans le loyer ?", True),
        ("CLAUDINE", "Oui. Onze cent cinquante dollars, chauffage et électricité compris. Il n'y a rien à ajouter.", True),
    ], notes="« J'aimerais poser trois questions, si vous avez une minute » est la "
             "phrase la plus utile de la séance : elle annonce ce qui vient et elle "
             "laisse à l'autre la possibilité de dire non. Faire répéter en chœur.")

    d.dialogue('Dialogue · 3 de 3', "Sept mille quatre cent douze, rue Chabot", [
        ("DILNOZA", "Merci. Est-ce que je pourrais le visiter cette semaine ?", True),
        ("CLAUDINE", "Bien sûr. Samedi matin, dix heures, ça vous irait ?", True),
        ("DILNOZA", "Samedi, dix heures. Je vais venir avec mon mari. C'est quelle adresse ?", True),
        ("CLAUDINE", "Sept mille quatre cent douze, rue Chabot. Deuxième étage, la porte de droite.", True),
        ("DILNOZA", "Sept mille quatre cent douze, rue Chabot, samedi dix heures. Merci beaucoup, madame.", True),
    ], notes="La dernière réplique est le geste le plus important du bloc : elle répète "
             "l'adresse, le jour et l'heure. C'est le seul moment où une erreur peut "
             "encore se corriger. L'exiger de tout le monde.")

    d.tableau('Analyse', "Les quatre temps de l'appel",
              ["Le temps", "Ce qu'on dit"],
              [["1 · dire pourquoi on appelle", "Je vous appelle pour l'annonce."],
               ["2 · annoncer ses questions", "J'aimerais poser trois questions."],
               ["3 · demander la visite", "Est-ce que je pourrais le visiter ?"],
               ["4 · répéter le rendez-vous", "Samedi, dix heures, rue Chabot."]],
              cle=0,
              note="Trois minutes en tout, pas davantage.",
              notes="Diapositive à photographier. C'est le plan de la production orale "
                    "de la séance E1. Le faire recopier maintenant : il servira à chaque "
                    "séance du bloc.")

    d.regle("La phrase qui ouvre tous les appels",
            "« Bonjour. Je vous appelle pour l'annonce. »",
            precision="Elle dit tout de suite qui vous êtes et ce que vous "
                      "voulez. Sans elle, la personne ne sait pas à qui elle "
                      "parle et l'appel commence mal. Elle vient juste après "
                      "le bonjour, jamais plus tard.",
            notes="Diapositive à photographier. Faire répéter individuellement, en "
                  "regardant ailleurs pour imiter la situation du téléphone. C'est la "
                  "phrase du billet de sortie.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Dilnoza dit tout de suite pourquoi elle appelle.", "vrai"),
        ("Le logement est déjà loué.", "faux — il est encore libre"),
        ("Claudine demande combien de personnes vont habiter là.", "vrai"),
        ("La buanderie coûte deux dollars la brassée.", "vrai"),
        ("Le bail est de six mois.", "faux — douze mois"),
        ("Dilnoza répète l'adresse avant de raccrocher.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice 1 du Défi 2. Faire justifier chaque « faux » par la "
             "réplique exacte du dialogue.")

    d.billet(
        "Écrivez la première phrase que vous direz au téléphone.",
        exemples=[
            "Bonjour, ___ . Je vous appelle pour ___ .",
            "J'aimerais ___ .",
        ],
        notes="Devoir court. Faire écrire la phrase complète, avec le bonjour. Les "
              "billets se relisent à voix haute en début de séance C2.")

    return d.save(dossier)
