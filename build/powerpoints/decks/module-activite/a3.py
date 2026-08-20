# -*- coding: utf-8 -*-
"""A3 · Les six questions.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercices `prQuest` et `prTarif`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Les six questions',
        chapeau="Savoir quoi demander vaut mieux que tout comprendre. Six "
                "questions font le tour de n'importe quelle inscription — et "
                "elles sont toujours les mêmes.",
        duree='60 minutes')

    d.titre(notes="Reprendre les billets de A1 : les questions notées par le groupe. Les "
                  "écrire au tableau et les comparer aux six de la séance.")

    d.objectifs([
        "poser les six questions d'une inscription ;",
        "reconnaître ce que chaque question cherche vraiment ;",
        "demander une précision quand la réponse est vague ;",
        "récapituler avant de partir.",
    ])

    d.tableau('Analyse · 1 de 2', "Les six questions",
              ['La question', 'Ce que je veux savoir'],
              [["C'est quand, exactement ?", "le jour, l'heure, la durée"],
               ["Ça coûte combien ?", "le tarif, et s'il change selon où j'habite"],
               ["Qu'est-ce qu'il faut apporter ?", "le matériel obligatoire"]],
              cle=1,
              note="Trois autres au tableau suivant.",
              notes="Faire recopier. Ces six questions sont la liste de vérification du "
                    "module.")

    d.tableau('Analyse · 2 de 2', "Les six questions (suite)",
              ['La question', 'Ce que je veux savoir'],
              [["Qu'est-ce que je dois fournir ?", "les documents demandés"],
               ["Il reste des places ?", "si je peux encore m'inscrire"],
               ["Je peux m'inscrire en ligne ?", "la façon de s'inscrire et de payer"]],
              cle=1,
              notes="La cinquième question est celle qu'on oublie le plus. Elle décide "
                    "pourtant s'il faut se dépêcher.")

    d.regle('Le mot qui obtient une réponse précise',
            "Ajoutez « exactement » à votre question.",
            precision="« C'est quand ? » obtient « le samedi matin ». « À quelle heure "
                      "exactement ? » obtient « de neuf heures à dix heures ». Un seul mot "
                      "change la précision de la réponse.",
            notes="C'est ce que fait Rosa dans le dialogue de A1. Le faire remarquer et "
                  "faire pratiquer sur trois questions.")

    d.cartes('Quand la réponse est vague', "Trois façons de préciser", [
        ("Demander un chiffre",
         "« C'est vers quelle heure ? » — « De neuf à dix heures. » Un chiffre ne se "
         "discute pas."),
        ("Demander un exemple",
         "« Qu'est-ce qui compte comme preuve, par exemple ? » — « Une facture "
         "d'électricité. » L'exemple vaut mieux que la catégorie."),
        ("Répéter en affirmant",
         "« Donc le bonnet est obligatoire ? » La personne confirme ou corrige. C'est la "
         "façon la plus rapide de vérifier."),
    ], notes="La troisième carte est la plus efficace et la moins employée. Faire "
             "pratiquer : un élève donne une réponse vague, l'autre reformule en affirmant.")

    d.piege('La question trop large',
            "Comment ça marche ?",
            "C'est quel jour, et à quelle heure exactement ?",
            "« Comment ça marche ? » oblige la personne à choisir par où commencer — et "
            "elle commence rarement par ce qui vous intéresse. Une question précise obtient "
            "une réponse précise, en deux fois moins de temps.",
            notes="Ne pas présenter la gauche comme une faute : c'est une question polie, "
                  "mais peu efficace.")

    d.pratique('Pratique · 1 de 2', "Quelle question poser ?",
               "Vous voulez savoir ceci. Que demandez-vous ?", [
        ("Vous voulez savoir si vous payez 85 $ ou 110 $.", "Est-ce qu'il y a un tarif pour les résidents ?"),
        ("Vous voulez savoir ce que votre enfant doit apporter.", "Qu'est-ce qu'il faut apporter pour le cours ?"),
        ("Vous voulez savoir s'il faut vous dépêcher.", "Est-ce qu'il reste des places ?"),
        ("Vous voulez savoir quel papier fournir.", "Qu'est-ce que je dois fournir comme preuve ?"),
        ("Vous voulez savoir combien de temps ça dure.", "La session dure combien de semaines ?"),
    ], corrige=True, cols=1,
       notes="Accepter toutes les formulations qui obtiennent l'information. Ce n'est pas "
             "un exercice de grammaire.")

    d.pratique('Pratique · 2 de 2', "Précisez la réponse vague",
               "La personne répond vaguement. Que dites-vous ?", [
        ("— C'est le samedi matin.", "À quelle heure exactement ?"),
        ("— Il faut une preuve d'adresse.", "Qu'est-ce qui compte, par exemple ?"),
        ("— Il faut le matériel habituel.", "Qu'est-ce qui est obligatoire, exactement ?"),
        ("— Il en reste quelques-unes.", "Donc je devrais m'inscrire cette semaine ?"),
    ], corrige=True, cols=1,
       notes="Faire jouer les paires à deux. C'est l'exercice le plus utile de la séance.")

    d.billet(
        "Écrivez les six questions, dans l'ordre où vous les poseriez.",
        exemples=[
            "Ajoutez « exactement » à au moins deux d'entre elles.",
            "Terminez par la phrase de récapitulation.",
        ],
        notes="Corriger et rendre : cette page devient la fiche que l'élève emportera au "
              "comptoir. Plusieurs la garderont dans leur portefeuille.")

    return d.save(dossier)
