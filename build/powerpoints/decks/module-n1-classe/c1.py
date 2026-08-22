# -*- coding: utf-8 -*-
"""C1 · À quelle heure ?
Bloc C « Défi 2 · L'heure et l'horaire » · couleur acier · 75 min.
Source du module : dialogue `t2`, exercices `t2vf` et `t2heure`, mini-leçon
`t2heure`.

Deuxième intention du programme : comprendre l'information sur le
fonctionnement de la classe. Elle commence par l'heure — celle du cours, celle
de la pause, celle de la fin.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n1-classe/images/')


def photo(nom):
    """Le chemin de l'image, ou rien si elle n'est pas encore produite."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='À quelle heure ?',
        chapeau="L'heure du cours, l'heure de la pause, l'heure de la fin. "
                "Trois heures à comprendre, et une horloge au mur.",
        duree='75 minutes')

    d.titre(notes="Commencer en montrant l'horloge de la salle et en demandant l'heure. "
                  "Ce que le groupe sait déjà se verra tout de suite, et c'est très "
                  "inégal.")

    d.objectifs([
        "dire une heure juste ;",
        "dire la demie et le quart ;",
        "employer midi ;",
        "comprendre « à quelle heure ? ».",
    ])

    d.declencheur(
        'Observation', "Quelle heure est-il ?",
        image=photo('horaire-mur.jpg'),
        pistes=[
            "Où est l'horloge dans notre salle ?",
            "À quelle heure commence notre cours ?",
            "À quelle heure est la pause ?",
            "À quelle heure finit le cours ?",
        ],
        notes="Répondre soi-même aux trois dernières, lentement, et les écrire au "
              "tableau : elles serviront toute la séance et tout le module.")

    d.dialogue('Dialogue', "Le cours finit à midi", [
        ("BOPHA", "Madame, le cours finit à quelle heure ?", True),
        ("MADAME CYR", "À midi. Le cours finit à midi.", True),
        ("BOPHA", "À midi. Et la pause ?", True),
        ("MADAME CYR", "La pause est à dix heures. Quinze minutes.", True),
        ("BOPHA", "Dix heures. D'accord.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Bopha répète l'heure entendue avant de continuer. C'est la bonne habitude "
             "du module : redire pour vérifier.")

    d.regle("Le nombre, puis le mot",
            "huit heures, dix heures, midi.",
            precision="Le nombre vient en premier. Pour l'heure d'un cours ou d'un "
                      "rendez-vous, on met <b>à</b> devant : « le cours commence "
                      "<b>à</b> huit heures et demie ».",
            notes="Diapositive à photographier. Le petit mot « à » manque très souvent : "
                  "le faire répéter dans la phrase entière, jamais seul.")

    d.tableau('Analyse', "Lire l'heure",
              ['On écrit', 'On dit'],
              [["8 h", "huit heures"],
               ["8 h 30", "huit heures et demie"],
               ["8 h 15", "huit heures et quart"],
               ["12 h", "midi"]],
              cle=2,
              note="À douze heures, on ne dit pas « douze heures » : on dit midi.",
              notes="Diapositive à photographier. Le « h » de l'horaire du centre se lit "
                    "« heures » : le montrer sur l'horaire affiché près de la porte.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le cours finit à midi.", "vrai"),
        ("La pause est à neuf heures.", "faux — à dix heures"),
        ("La pause dure quinze minutes.", "vrai"),
        ("Le cours commence à huit heures et demie.", "vrai"),
    ], corrige=True, cols=1,
       notes="Les quatre heures du dialogue sont celles de la vraie journée d'un groupe "
             "de francisation : les comparer avec celles du groupe.")

    d.piege("Dire « douze heures »",
            "Le cours finit à douze heures.",
            "Le cours finit à midi.",
            "« Douze heures » se comprend, mais personne ne le dit ici. Sur un horaire "
            "écrit, en revanche, « 12 h » est tout à fait normal.",
            notes="Distinguer l'écrit et l'oral : c'est la première fois du module qu'ils "
                  "ne disent pas la même chose.")

    d.pratique('Pratique', "Complétez",
               "Écrivez le mot qui manque.", [
        ("Il est huit ___ et demie.", "heures"),
        ("Le cours finit à ___ .", "midi"),
        ("La pause est ___ dix heures.", "à"),
        ("8 h 30, c'est huit heures ___ demie.", "et"),
    ], corrige=True, cols=1,
       notes="Quatre items suffisent. Corriger tous ensemble, à voix haute.")

    d.pratique('Pratique · à deux', "L'horloge de papier",
               "Deux par deux, avec une horloge dessinée sur une feuille.", [
        ("Étape 1", "A place les aiguilles et demande : « Quelle heure est-il ? »"),
        ("Étape 2", "B répond à voix haute."),
        ("Étape 3", "Cinq heures chacun, puis on change."),
        ("Étape 4", "Finir par les vraies heures du groupe : début, pause, fin."),
    ], cols=1,
       notes="Vingt minutes. Distribuer les horloges de papier au début du cours : les "
             "dessiner soi-même prend le temps de la séance.")

    d.billet(
        "Écrivez trois heures de votre journée.",
        exemples=[
            "Le cours commence à…",
            "La pause est à…",
            "Le cours finit à…",
        ],
        notes="Les trois phrases serviront de brouillon à l'horaire écrit de la séance "
              "E1. Le dire au groupe : rien n'est demandé pour rien.")

    return d.save(dossier)
