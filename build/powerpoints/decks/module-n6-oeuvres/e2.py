# -*- coding: utf-8 -*-
"""E2 · Écris ton résumé pour L'Écho de la Magog
Bloc E « Je me lance » · couleur framboise · 75 min. Dernière séance.
Source : bloc « Je me lance » du module — production écrite et
autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écris ton résumé pour L'Écho de la Magog",
        chapeau="Deux paragraphes : le premier raconte le film et s'arrête "
                "avant le dénouement, le second dit ce que tu en penses. "
                "Mélanger les deux donne une humeur, pas un avis.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. L'hebdomadaire publie deux ou trois "
                  "réponses de lecteurs par semaine : le dire, et le dire "
                  "sérieusement. Un texte qui a un destinataire s'écrit autrement.")

    d.objectifs([
        "rédiger un texte d'un ou deux paragraphes pour raconter un film ;",
        "séparer nettement le récit de l'avis ;",
        "employer un plus-que-parfait, un « où » et une reprise sans répétition ;",
        "accorder un point au critique avant de le contredire.",
    ], notes="Le premier objectif est une attente de fin de cours du niveau 6, mot "
             "pour mot : « il rédige un texte d'un ou deux paragraphes pour raconter "
             "un film de façon sommaire ».")

    d.declencheur(
        'Observation', "Pourquoi séparer le récit de l'avis ?",
        pistes=[
            "Que se passe-t-il si on les mélange dans le même paragraphe ?",
            "Comment le lecteur sait-il ce qui est un fait et ce qui est un avis ?",
            "Quel paragraphe se lit en premier, et pourquoi ?",
            "Lequel des deux le journal coupera-t-il s'il manque de place ?",
        ],
        notes="La dernière piste est celle qui fait réfléchir : un journal coupe par "
              "la fin. Un texte dont l'essentiel est au début résiste mieux.")

    d.tableau('Analyse', "Deux paragraphes, deux métiers",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["premier", "le titre, où tu l'as vu, l'histoire dans l'ordre"],
               ["premier - fin", "il s'arrête avant le dénouement, toujours"],
               ["second", "un point accordé au critique, puis ton désaccord"],
               ["second - appui", "chaque jugement porte sur un moment précis du film"],
               ["ce qu'on ne fait pas", "mélanger les deux dans le même paragraphe"]],
              cle=0,
              note="Un texte qui sépare les deux se lit comme un avis ; un texte qui les mêle, comme une humeur.",
              notes="Diapositive à photographier. C'est le plan de la production. Le "
                    "laisser à l'écran pendant toute la rédaction.")

    d.regle("Découper en paragraphes",
            "Une idée principale par paragraphe, et un espace entre les deux.",
            precision="Le programme du niveau 6 le demande explicitement : découper "
                      "des idées principales en paragraphes, et les organiser "
                      "visuellement. Ce n'est pas de la décoration : c'est ce qui "
                      "permet au lecteur de savoir, avant de lire, combien d'idées "
                      "l'attendent.",
            notes="Diapositive à photographier. Montrer la différence à l'écran : le "
                  "même texte en un bloc, puis en deux paragraphes.")

    d.pratique('Production écrite', "Ce que ton texte doit contenir",
               "Cochez chaque élément avant d'envoyer.", [
        ("Deux paragraphes séparés : l'histoire, puis l'avis.", "obligatoire"),
        ("Le titre du film et l'endroit où tu l'as vu.", "obligatoire"),
        ("Aucun mot sur le dénouement.", "obligatoire"),
        ("Un plus-que-parfait qui recule d'un cran.", "vu en B3"),
        ("Un « où » qui rattache un lieu ou un moment.", "vu en C4"),
        ("Une reprise sans répétition : ce film, cette scène.", "vu en C4"),
    ], corrige=False,
       notes="Grille donnée d'avance, comme en E1. Les trois derniers items renvoient "
             "aux séances : un élève bloqué doit savoir où retourner chercher.")

    d.pratique('Production écrite', "Deux exigences de plus",
               "Elles portent sur le second paragraphe.", [
        ("Un point accordé au critique : c'est vrai que..., même si...", "vu en D2"),
        ("Un avis annoncé comme un avis : à mon avis, pour ma part...", "vu en D2"),
        ("Un jugement appuyé sur un moment précis du film.", "vu en D1"),
        ("Huit à douze phrases en tout.", "obligatoire"),
    ], corrige=False,
       notes="Compter les phrases est le contrôle le plus simple et le plus utile : "
             "un texte de cinq phrases n'a pas deux paragraphes, quoi qu'en dise sa "
             "mise en page.")

    d.piege("Écrire le résumé au passé simple",
            "Estelle revint au village et trouva une lettre.",
            "Estelle revient au village et trouve une lettre.",
            "Le passé simple se lit et ne s'écrit pas — c'était la règle de C3, et "
            "elle vaut ici. Un résumé de film s'écrit au présent, qui est le temps "
            "habituel du récit de film, ou au passé composé. Le passé simple dans un "
            "courriel de lecteur se remarque tout de suite, et pas en bien.",
            notes="Faute attendue et flatteuse : elle vient d'élèves qui ont bien "
                  "retenu C3. La corriger sans décourager.")

    d.cartes("Le bilan du module", "Ce que tu sais faire maintenant", [
        ("Repérer un déroulement",
         "même quand le film recule quatre fois, et sans perdre le fil."),
        ("Lire un texte suivi",
         "une biographie au passé simple, avec ses petits mots qui renvoient."),
        ("Lire une critique",
         "ce qu'elle dit vraiment, pas ce qu'on croit qu'elle dit."),
        ("Tenir un avis nuancé",
         "accorder un point, puis répondre, en s'appuyant sur un moment précis."),
    ], notes="Quatre acquis, un par bloc. Les lire à voix haute avant l'autoévaluation "
             "de l'activité : le groupe sous-estime toujours ce qu'il a appris.")

    d.billet(
        "Quel film aimerais-tu voir au ciné-club, et pourquoi ?",
        exemples=[
            "Deux phrases.",
            "Emploie un mot précis : un long métrage, un documentaire, une série.",
        ],
        notes="Trois minutes, pour finir. Ces billets font une liste de suggestions "
              "réelle, et ils montrent en une phrase si le vocabulaire précis de A3 "
              "est passé.")

    return d.save(dossier)
