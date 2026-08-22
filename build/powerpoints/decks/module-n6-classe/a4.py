# -*- coding: utf-8 -*-
"""A4 · Les six moments du travail
Bloc A « Je découvre » · couleur framboise · 75 min. Méthode et vocabulaire.
Source du module : exercices `prEtapes` et `prImg`, et la mini-leçon `prEtapes`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='framboise',
        titre="Les six moments du travail",
        chapeau="Un travail de recherche ne se fait pas d'un bloc. La semaine "
                "qui ne produit aucune page est celle qui décide de la note.",
        duree='75 minutes')

    d.titre(notes="Séance de méthode. Ce n'est pas du français, et c'est "
                  "pourtant ce qui manque le plus : beaucoup d'adultes n'ont "
                  "jamais eu à organiser trois semaines de travail.")

    d.objectifs([
        "nommer les six moments d'un travail de recherche ;",
        "dire ce qui se décide dans chacun ;",
        "répartir trois semaines entre décider, écrire et corriger ;",
        "reconnaître un travail d'équipe d'un travail simplement partagé.",
    ], notes="Le quatrième point est celui qu'on entend le moins et qui se "
             "voit le plus à la correction.")

    d.declencheur(
        'Pour commencer', "Trois semaines : vous les partagez comment ?",
        pistes=[
            "Combien de jours pour chercher ?",
            "Combien pour écrire ?",
            "Et pour le reste — il y a un reste ?",
        ],
        notes="Presque personne ne prévoit de temps pour corriger et répéter. "
              "Noter les propositions au tableau et les comparer au tableau "
              "de la diapositive suivante.")

    d.tableau('Analyse', "Trois semaines, trois travaux différents",
              ['La semaine', 'Ce qui doit être fini'],
              [["Semaine 1 — décider", "le sujet approuvé et trois sources trouvées"],
               ["Semaine 2 — écrire", "le plan, puis un texte complet même imparfait"],
               ["Semaine 3 — finir", "la relecture à trois et l'exposé répété"]],
              cle=0,
              note="La première semaine ne produit aucune page. C'est elle qui décide de tout.",
              notes="Diapositive à photographier. Insister : un texte laid "
                    "mais complet se corrige, un texte troué se réécrit.")

    d.cartes('Analyse', "Les six moments, et ce qui s'y décide", [
        ("1 · L'équipe", "Qui fait quoi. Le dire à voix haute et l'écrire."),
        ("2 · Le sujet", "Une question précise, approuvée avant qu'on cherche."),
        ("3 · Les sources", "Trois genres différents, avec leur date."),
        ("4 · Le plan", "L'ordre des idées, une par paragraphe."),
        ("5 · Le texte", "Les phrases, la bibliographie, la relecture à voix haute."),
        ("6 · L'exposé", "Ce qu'on dira en cinq minutes, répété jusqu'à tenir."),
    ], cols=3,
       notes="C'est l'exercice `prEtapes` du module. Faire nommer, pour "
             "chaque moment, ce qui arrive si on le saute.")

    d.regle("Le plan vient avant le texte, toujours",
            "On ne déplace pas un paragraphe déjà écrit sans le réécrire au complet.",
            precision="Un plan se corrige en deux traits de crayon. C'est la "
                      "seule raison de l'écrire, et elle suffit.",
            notes="Diapositive à photographier. La consigne du module exige "
                  "d'ailleurs qu'on remette le plan avec le texte : ce n'est "
                  "pas un caprice, c'est ce qui rend la correction possible.")

    d.piege('Méthode',
            "se partager le travail en trois morceaux",
            "écrire chacun sa partie, puis relire à trois",
            "Trois textes collés bout à bout se reconnaissent à la première "
            "page : le ton change, les mots changent, et les mêmes choses "
            "sont dites deux fois. La relecture commune à voix haute prend "
            "une heure et fait disparaître les coutures.",
            notes="Proposer la relecture en classe, à la séance C5 ou E1, "
                  "pour les équipes qui n'auront pas trouvé le temps de se "
                  "voir en dehors.")

    d.tableau('Analyse', "Ce qu'on voit à chaque moment",
              ['Le moment', 'Ce qu\'on a devant soi'],
              [["l'annonce", "une classe, une enseignante, une pile de feuilles"],
               ["la consigne", "une feuille imprimée, quelques lignes soulignées"],
               ["la bibliothèque", "des étagères, une table ronde, une chaise tirée"],
               ["les sources", "trois documents étalés côte à côte"],
               ["le plan", "une feuille quadrillée, des ratures, des flèches"]],
              cle=0,
              note="Chaque moment a son décor, et le décor aide à se rappeler l'ordre.",
              notes="C'est l'exercice `prImg` du module, projeté sans les "
                    "photos : le module, lui, fait poser l'image sur la "
                    "phrase.")

    d.pratique('Pratique', "Chaque moment, ce qui s'y décide",
               "Reliez le moment à la décision qui s'y prend.", [
        ("la formation de l'équipe", "qui travaille avec qui, et qui se charge de quoi"),
        ("le choix du sujet", "la question précise à laquelle on répond"),
        ("la recherche des sources", "les trois documents et leurs dates"),
        ("l'écriture du plan", "l'ordre des idées, une par paragraphe"),
        ("la rédaction", "les phrases, la bibliographie, la relecture"),
        ("la préparation de l'exposé", "ce qu'on dira en cinq minutes"),
    ], corrige=True, cols=1,
       notes="Faire former les équipes juste après cet exercice : le groupe "
             "sait maintenant ce qu'il s'engage à faire.")

    d.billet(
        "Écris ce que ton équipe doit avoir fini vendredi prochain.",
        exemples=[
            "Une seule phrase, avec une date dedans.",
            "Exemple : « Vendredi 7, notre sujet est approuvé. »",
        ],
        notes="Trois minutes. Ramasser et garder : ces billets servent de "
              "point de départ à la rencontre d'équipe de la séance E1.")

    return d.save(dossier)
