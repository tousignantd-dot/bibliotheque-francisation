# -*- coding: utf-8 -*-
"""C2 · Lundi, mardi, mercredi.
Bloc C « Défi 2 · L'heure et l'horaire » · couleur ambre · 60 min.
Source du module : dialogue `appli`, exercices `t2jours` et `t2lire`,
mini-leçon `t2jours`.

Ferme le défi 2 : les jours de la semaine, puis l'horaire du groupe lu comme
un tout — quels jours, de quelle heure à quelle heure, et quel jour il n'y a
pas de cours.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Lundi, mardi, mercredi',
        chapeau="Sept jours dans la semaine, quatre jours de cours. Tout est "
                "écrit sur la feuille affichée près de la porte.",
        duree='60 minutes')

    d.titre(notes="Apporter en classe l'horaire réel du groupe, affiché près de la "
                  "porte. Toute la séance se fait avec lui sous les yeux.")

    d.objectifs([
        "dire les sept jours dans l'ordre ;",
        "dire quels jours il y a cours ;",
        "lire l'horaire du groupe ;",
        "comprendre « il n'y a pas de cours ».",
    ])

    d.dialogue('Dialogue', "Tu viens vendredi ?", [
        ("IVAN", "Bopha, tu viens vendredi ?", True),
        ("BOPHA", "Vendredi ? Non. Il n'y a pas de cours.", True),
        ("IVAN", "Ah bon ?", True),
        ("BOPHA", "Regarde l'horaire. Lundi, mardi, mercredi, jeudi.", True),
        ("IVAN", "Quatre jours. Et vendredi, non.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="C'est Bopha, l'élève arrivée la dernière, qui renseigne Ivan. Le faire "
             "remarquer : savoir lire son horaire rend service aux autres.")

    d.tableau('Analyse', "La semaine",
              ['Le jour', 'Y a-t-il cours ?'],
              [["lundi, mardi", "oui, de 8 h 30 à midi"],
               ["mercredi, jeudi", "oui, de 8 h 30 à midi"],
               ["vendredi", "non, pas de cours"],
               ["samedi, dimanche", "non, le centre est fermé"]],
              cle=2,
              note="Vendredi, le centre est ouvert : c'est le groupe qui n'a pas cours.",
              notes="Diapositive à photographier. Remplacer les heures par celles du "
                    "groupe si elles diffèrent — l'horaire projeté doit être le vrai.")

    d.regle("Il n'y a pas de cours",
            "La phrase qui dit qu'on ne vient pas.",
            precision="Elle ne veut pas dire que le centre est fermé. Le secrétariat "
                      "répond, on peut venir chercher un papier. C'est le <b>groupe</b> "
                      "qui ne se réunit pas.",
            notes="Diapositive à photographier. La distinction est pratique, pas "
                  "grammaticale : un élève s'est déjà présenté un vendredi.")

    d.cartes('Écoute', "Deux jours qui se ressemblent", [
        ("mardi",
         "Deux parties : mar-di. Le mot est court."),
        ("mercredi",
         "Trois parties : mer-cre-di. Le mot est long."),
        ("Le truc",
         "Comptez les parties du mot dans votre tête. Le plus long est le mercredi."),
    ], notes="Diapositive à photographier. Faire dire les deux mots en frappant dans les "
             "mains à chaque partie.")

    d.pratique('Pratique', "Cours ou pas de cours ?",
               "Répondez pour chaque jour.", [
        ("lundi", "cours"),
        ("mercredi", "cours"),
        ("vendredi", "pas de cours"),
        ("samedi", "pas de cours"),
    ], corrige=True, cols=2,
       notes="Puis refaire l'exercice avec les vrais jours du groupe, sans la "
             "diapositive.")

    d.pratique('Lecture', "Lire l'horaire",
               "Répondez avec l'horaire affiché.", [
        ("Le cours commence à ___ heures et demie.", "huit"),
        ("Le cours finit à ___ .", "midi"),
        ("La pause est à ___ heures.", "dix"),
        ("Le jour sans cours, c'est ___ .", "vendredi"),
        ("Je viens ___ jours par semaine.", "quatre"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice du module, repris tel quel. Les élèves qui l'ont déjà "
             "fait à l'ordinateur peuvent aider leur voisin.")

    d.billet(
        "Écrivez les jours où vous venez au centre.",
        exemples=[
            "En minuscules : lundi, mardi…",
            "Puis ajoutez : « Le cours commence à… Il finit à… »",
        ],
        notes="Les jours en minuscules : c'est la seule règle d'orthographe de la séance, "
              "et elle surprend ceux qui écrivent l'anglais.")

    return d.save(dossier)
