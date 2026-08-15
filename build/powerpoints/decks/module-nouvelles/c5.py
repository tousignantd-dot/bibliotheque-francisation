# -*- coding: utf-8 -*-
"""C5 · Lire un fait divers seul.
Bloc C · couleur teal (lire et répondre) · 60 min.
Source : exercices `aFait2` et `aImg` — le documentaire sur le recyclage.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C5', section='teal',
        titre='Lire un fait divers seul',
        chapeau="Un texte qu'on n'a pas travaillé en classe, lu en autonomie. C'est la "
                "vraie situation : ni enseignant, ni corrigé, ni deuxième écoute.",
        duree='60 minutes')

    d.titre(notes="Ne rien expliquer avant l'exercice. Distribuer le texte, laisser dix "
                  "minutes de lecture silencieuse, puis passer aux questions.")

    d.objectifs([
        "lire un fait divers nouveau sans aide ;",
        "repérer une information qui n'est pas dite explicitement ;",
        "distinguer ce que le texte dit de ce qu'on suppose ;",
        "associer une nouvelle et une image.",
    ])

    d.cartes('Le texte', "Une classe filme un documentaire", [
        ("Le projet",
         "À Victoriaville, les élèves d'une classe de 4e secondaire ont réalisé un court "
         "documentaire sur le recyclage dans leur quartier."),
        ("Qui l'a proposé",
         "Leur enseignant de sciences, qui souhaitait rendre la matière plus concrète."),
        ("Comment ils ont travaillé",
         "Pendant trois semaines, ils ont interviewé des commerçants, des employés "
         "municipaux et des citoyens."),
        ("La suite",
         "Le documentaire, intitulé Ce qu'on jette, ce qu'on garde, a été présenté "
         "devant toute l'école. Il sera aussi diffusé au conseil municipal."),
    ], notes="Cette diapo sert de correction, pas de première lecture. Ne l'afficher "
             "qu'après l'exercice 1.")

    d.pratique('Pratique · 1 de 4', "Vrai ou faux",
               "D'après le texte que vous venez de lire.", [
        ("Le documentaire a été proposé par l'enseignant de sciences.", "VRAI"),
        ("Les élèves ont travaillé sur ce projet pendant un an.", "FAUX — trois semaines"),
        ("Le sujet du documentaire est le recyclage.", "VRAI"),
        ("Les élèves ont interviewé seulement des employés municipaux.",
         "FAUX — aussi des commerçants et des citoyens"),
        ("Le documentaire a été présenté à toute l'école.", "VRAI"),
        ("Le documentaire ne sera jamais présenté au conseil municipal.",
         "FAUX — il y sera diffusé"),
    ], corrige=True,
       notes="Les mots « seulement » et « jamais » rendent deux énoncés faux. C'est la "
             "stratégie vue au module 4 : les chercher en premier.")

    d.regle('Ce que le texte dit et ce qu'"'"'on suppose',
            "Une information vraie n'est pas toujours écrite dans le texte.",
            precision="« Victoriaville se trouve au Centre-du-Québec » est vrai, mais ce "
                      "n'est pas écrit. Dans un examen de compréhension, on répond "
                      "d'après le texte — et on distingue ce qu'on lit de ce qu'on sait "
                      "déjà.",
            notes="Distinction importante et rarement enseignée. La montrer avec deux ou "
                  "trois exemples du texte.")

    d.pratique('Pratique · 2 de 4', "Écrit ou supposé ?",
               "Est-ce que le texte le dit, ou est-ce qu'on le déduit ?", [
        ("Les élèves sont en 4e secondaire.", "écrit"),
        ("Le projet a duré trois semaines.", "écrit"),
        ("Les élèves ont appris beaucoup de choses.", "supposé — le texte ne le dit pas"),
        ("Victoriaville est au Centre-du-Québec.", "supposé — vrai, mais pas écrit"),
        ("Le documentaire dure moins d'une heure.", "supposé — « court » ne dit pas combien"),
    ], corrige=True,
       notes="Le dernier item est le plus fin : « court documentaire » est une catégorie, "
             "pas une durée. Le corriger en dernier.")

    d.piege("Le piège de ce qu'on sait déjà",
            "Je réponds avec ce que je sais, pas avec ce que le texte dit.",
            "Je cherche la phrase exacte avant de répondre.",
            "Une réponse vraie mais absente du texte est fausse dans un exercice de "
            "compréhension. Et dans la vraie vie, elle peut être fausse tout court : ce "
            "qu'on croit savoir n'est pas toujours à jour.",
            notes="Faire pointer la phrase exacte pour chaque réponse, systématiquement. "
                  "C'est une discipline de lecture.")

    d.pratique('Pratique · 3 de 4', "Associez la nouvelle et l'image",
               "Cinq nouvelles du module, cinq images.", [
        ("Des élèves ont amassé plus de deux cents paires de mitaines.",
         "la collecte de mitaines"),
        ("Une fillette a retrouvé son chat grâce à une affiche.", "le chat retrouvé"),
        ("L'équipe gagnante a façonné une sculpture de trois mètres.",
         "la sculpture sur neige"),
        ("Deux passants ont secouru un cycliste blessé à l'épaule.", "le cycliste secouru"),
        ("Des élèves ont interviewé des commerçants pour un documentaire.",
         "le documentaire de classe"),
    ], corrige=True,
       notes="Faire l'exercice dans le module interactif, sur les vraies images. Cette "
             "diapo sert de rappel et de correction.")

    d.pratique('Pratique · 4 de 4', "Les cinq questions du documentaire",
               "Appliquez la grille de A4.", [
        ("Qui ?", "des élèves de 4e secondaire et leur enseignant de sciences"),
        ("Quoi ?", "ils ont réalisé un court documentaire sur le recyclage"),
        ("Où ?", "à Victoriaville, dans leur quartier"),
        ("Quand ?", "pendant trois semaines ; présenté la semaine dernière"),
        ("Pourquoi ?", "pour rendre la matière plus concrète"),
    ], corrige=True,
       notes="La grille des cinq questions ferme le défi 2 comme elle a ouvert le "
             "module. Le faire remarquer.")

    d.billet(
        "Écrivez trois questions que vous poseriez à ces élèves.",
        exemples=[
            "Des questions dont la réponse n'est pas dans le texte.",
            "Exemple : « Combien de personnes avez-vous interviewées ? »",
        ],
        notes="Formuler une question dont la réponse manque est la preuve qu'on a "
              "vraiment lu. C'est un meilleur bilan qu'un vrai ou faux.")

    return d.save(dossier)
