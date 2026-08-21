# -*- coding: utf-8 -*-
"""A4 · Un salon, une cuisine.
Bloc A « Je découvre » · couleur ambre · 75 min. Grammaire.
Source : exercice `prGenre` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre='Un salon, une cuisine',
        chapeau="Le genre ne se devine pas et ne se traduit pas : il "
                "s'apprend avec le mot. Quatre séances plus loin, c'est lui "
                "qui décidera de l'accord des adjectifs d'une annonce.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Ouvrir en reprenant les mots relevés dans "
                  "les billets de la séance A3, et en demandant chaque fois « un ou "
                  "une ? ». Le groupe hésitera : c'est le sujet de la séance.")

    d.objectifs([
        "choisir entre un et une devant le nom d'une pièce ;",
        "savoir que le genre ne se traduit pas d'une langue à l'autre ;",
        "apprendre chaque mot nouveau avec son article ;",
        "comprendre pourquoi le genre reviendra dans l'accord des adjectifs.",
    ])

    d.regle("La règle est qu'il n'y a pas de règle",
            "L'article fait partie du mot",
            precision="Rien dans un salon ne le rend masculin, rien dans une "
                      "cuisine ne la rend féminine. On ne peut pas le deviner, "
                      "et on ne peut pas le traduire : le même objet change de "
                      "genre d'une langue à l'autre. On l'apprend en même temps "
                      "que le mot, jamais après.",
            notes="Diapositive à photographier. Le dire franchement plutôt que de "
                  "laisser espérer une règle : les élèves qui cherchent une logique "
                  "perdent des mois. Ce qui marche, c'est de noter l'article.")

    d.tableau('Analyse', "Les pièces masculines",
              ["On dit", "La fin du mot"],
              [["un salon", "en -on"],
               ["un balcon", "en -on"],
               ["un couloir", "en -oir"],
               ["un sous-sol", "en -ol"]],
              cle=0,
              note="Beaucoup de mots en -on et en -oir sont masculins. Ça aide, ça ne décide pas.",
              notes="Diapositive à photographier. Présenter la terminaison comme une "
                    "aide à la mémoire, pas comme une règle : « une maison » finit "
                    "aussi en -on et elle est féminine.")

    d.tableau('Analyse', "Les pièces féminines",
              ["On dit", "La fin du mot"],
              [["une cuisine", "en -ine"],
               ["une chambre", "en -ambre"],
               ["une salle de bain", "en -alle"],
               ["une fenêtre", "en -être"]],
              cle=0,
              note="Beaucoup de mots en -ine et en -elle sont féminins.",
              notes="Diapositive à photographier. Faire chercher au groupe d'autres mots "
                    "du logement en -ine : la cuisine, la piscine, la vitrine. Tous "
                    "féminins.")

    d.tableau('Analyse', "Au pluriel, un seul mot pour les deux",
              ["Singulier", "Pluriel"],
              [["un salon", "des salons"],
               ["une chambre", "des chambres"],
               ["une chambre fermée", "des chambres fermées"],
               ["un balcon fermé", "des balcons fermés"]],
              cle=1,
              note="Le genre ne s'entend plus, mais il s'écrit encore dans l'adjectif.",
              notes="Diapositive à photographier. C'est le pont vers la séance B4 : "
                    "l'accord de l'adjectif. Ne pas le développer ici, seulement le "
                    "montrer.")

    d.piege('Grammaire',
            "« un cuisine, parce que c'est masculin dans ma langue »",
            "« une cuisine »",
            "Le genre change d'une langue à l'autre : le même objet est "
            "masculin ici et féminin ailleurs. Il n'y a rien à traduire — il "
            "faut réapprendre le mot avec son article français.",
            notes="Demander au groupe le genre de « cuisine » et de « salon » dans leurs "
                  "langues. Les réponses seront contradictoires, et c'est exactement la "
                  "démonstration qu'il faut faire.")

    d.piege('Méthode',
            "noter « chambre » dans son carnet",
            "noter « une chambre »",
            "Trois secondes de gagnées, et un doute pour des années. Un mot "
            "noté sans son article devra être réappris avec.",
            notes="Faire ouvrir les carnets et corriger sur-le-champ les mots déjà notés "
                  "sans article. C'est le geste le plus utile de la séance.")

    d.pratique('Grammaire', "Un ou une ?",
               "Complétez chaque phrase.", [
        ("Le logement a ___ salon et deux chambres.", "un"),
        ("Il y a ___ cuisine avec un balcon arrière.", "une"),
        ("Mon garçon veut ___ chambre à lui.", "une"),
        ("Il y a ___ salle de bain au fond du couloir.", "une"),
        ("La buanderie est dans ___ sous-sol propre.", "un"),
        ("L'immeuble a ___ escalier extérieur.", "un"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 4 de « Je découvre ». Faire justifier chaque réponse par "
             "le mot lui-même, jamais par l'habitude : « on dit une cuisine ».")

    d.pratique('Répétition', "Six pièces avec leur article",
               "Écoutez, puis répétez le mot entier.", [
        ("un salon", "masculin"),
        ("une cuisine", "féminin"),
        ("une chambre", "féminin"),
        ("une salle de bain", "féminin"),
        ("un balcon", "masculin"),
        ("un sous-sol", "masculin"),
    ], corrige=True, cols=2,
       notes="Répétition en chœur. Ne jamais faire répéter le mot seul, sans article : "
             "c'est ce qui installe le doute.")

    d.billet(
        "Écrivez quatre mots du logement avec leur article, sans regarder vos notes.",
        exemples=[
            "___ salon, ___ cuisine.",
            "___ chambre, ___ balcon.",
        ],
        notes="Devoir court. Dernier billet du bloc A. Corriger sans commenter : le but "
              "est de savoir qui aura besoin d'un rappel au moment de l'accord des "
              "adjectifs, en B4.")

    return d.save(dossier)
