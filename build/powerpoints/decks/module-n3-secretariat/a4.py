# -*- coding: utf-8 -*-
"""A4 · Bonjour madame.
Bloc A « Je découvre » · couleur ambre (écriture) · 60 min.
Source : exercice `prSalut`, mini-leçon `prSalut`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre='Bonjour madame',
        chapeau="Trois secondes avant de parler de son affaire : saluer, "
                "nommer la personne, vouvoyer. Ce n'est pas de la décoration, "
                "c'est ce que le programme appelle les formules d'appel.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Elle prépare directement le défi 1 : sans ces "
                  "formules, l'échange du comptoir commence mal et l'élève le sent.")

    d.objectifs([
        "saluer et s'adresser au personnel du centre ;",
        "employer le vous de politesse ;",
        "accorder votre et vos ;",
        "écrire les quatre formules qui ouvrent et ferment une démarche.",
    ])

    d.regle("On salue avant de demander",
            "« Bonjour, madame. »",
            precision="Le mot madame ou monsieur vient après bonjour, séparé "
                      "par une petite pause : deux mots, pas un seul. Une "
                      "demande qui commence par « je veux » se fait servir "
                      "quand même, mais moins bien et plus lentement.",
            notes="Diapo à photographier. Faire l'expérience : deux élèves jouent la même "
                  "demande, l'une sans salutation, l'autre avec. Demander au groupe ce "
                  "qui change — ils le voient tout de suite.")

    d.tableau('Analyse', "Au centre, on vouvoie",
              ["À qui", "On dit"],
              [["la secrétaire", "vous"],
               ["l'enseignante", "vous"],
               ["la direction", "vous"],
               ["les camarades de classe", "tu"]],
              cle=1,
              note="Le vous de politesse se conjugue comme le vous de plusieurs "
                   "personnes : une seule forme à apprendre.",
              notes="Diapo à photographier. Le tutoiement est très courant au Québec "
                    "entre collègues, mais pas d'un élève au personnel d'un "
                    "établissement. C'est une distinction utile bien au-delà du centre.")

    d.tableau('Analyse', "Votre, vos, mon, mes : un miroir",
              ["Elle demande", "Vous répondez"],
              [["Votre nom ?", "Mon nom, c'est…"],
               ["Votre groupe ?", "Mon groupe, c'est le 12."],
               ["Vos journées d'absence ?", "Mes journées : lundi et mardi."],
               ["Votre billet ?", "Voici mon billet."]],
              cle=1,
              note="Le mot qu'elle emploie annonce le vôtre. Il n'y a rien à "
                   "décider : c'est un miroir.",
              notes="Diapo à photographier. Faire jouer les quatre échanges en paires, "
                    "debout, une minute. Le geste du miroir se retient par le corps.")

    d.pratique('Écriture', "Madame, monsieur, vous ou votre ?",
               "Complétez chaque phrase.", [
        ("Bonjour, ___ . Je viens pour une absence.", "madame / monsieur"),
        ("— ___ nom, s'il vous plaît ? — Nawel Belkacem.", "Votre"),
        ("Est-ce que ___ pouvez répéter, s'il vous plaît ?", "vous"),
        ("Merci beaucoup, ___ Ferland. Bonne journée.", "monsieur"),
        ("Quel est ___ groupe, madame Belkacem ?", "votre"),
        ("Est-ce que ___ avez un papier de la clinique ?", "vous"),
    ], corrige=True,
       notes="Faire écrire d'abord, corriger ensuite au tableau. Demander chaque fois "
             "qui parle : la secrétaire ou l'élève.")

    d.cartes("Les quatre formules d'une démarche", "À apprendre par cœur", [
        ("Ouvrir",
         "« Bonjour, madame. » Rien d'autre avant : c'est la première phrase, toujours."),
        ("Se nommer",
         "« Mon nom, c'est Nawel Belkacem, groupe 12. » Nom, prénom, groupe : les trois, "
         "chaque fois."),
        ("Demander",
         "« Est-ce que je peux… ? » · « Pourriez-vous… ? » Deux questions qui ouvrent "
         "toutes les portes du comptoir."),
        ("Fermer",
         "« Merci beaucoup. Bonne journée. » La personne au comptoir le redit : c'est la "
         "fin normale d'une démarche."),
    ], notes="Faire écrire les quatre formules au carnet, dans cet ordre. Le défi 1 "
             "consiste à mettre quelque chose entre la deuxième et la quatrième.")

    d.piege("Appeler quelqu'un par « madame » tout seul",
            "« Madame ! J'ai besoin d'un papier. »",
            "« Bonjour, madame. J'aimerais un papier, s'il vous plaît. »",
            "« Madame » toute seule sonne comme un ordre, ou comme un appel dans la rue. "
            "Le mot va après « bonjour », jamais en tête de phrase.",
            notes="Erreur fréquente et jamais signalée à l'élève, parce qu'on le sert "
                  "quand même. C'est justement pour ça qu'il faut l'enseigner.")

    d.billet(
        "Écrivez les quatre phrases de votre démarche, dans l'ordre.",
        exemples=[
            "Bonjour, madame. / Mon nom, c'est… / Est-ce que je peux… ? / Merci. Bonne journée.",
            "Apprenez-les par cœur : le défi 1 les réutilise telles quelles.",
        ],
        notes="Fin du bloc A. Vérifier à l'entrée de B1 que chacun sait dire ses quatre "
              "phrases sans papier.")

    return d.save(dossier)
