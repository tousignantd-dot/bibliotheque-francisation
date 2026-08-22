# -*- coding: utf-8 -*-
"""B2 · Les étages et l'horaire.
Bloc B « Défi 1 » · couleur ambre · 75 min. Séance d'écriture et de lecture.
Source : dialogue `t1b`, exercices `t1etage`, `t1horaire` et `t1notes`,
mini-leçon « Les étages et les numéros de local ».

C'est la première des deux séances de **lecture** du module, et le programme
la demande explicitement : « comprendre de l'information sur le
fonctionnement de l'établissement de formation ». L'information, ici, c'est
un horaire d'ouverture — cinq lignes, deux nombres par ligne, et une notion
qui n'est écrite nulle part : le bureau ferme le midi.

La séance finit par une fiche de notes. Un jour et une heure entendus au
comptoir s'oublient avant l'escalier ; on les écrit tout de suite.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Les étages et l'horaire",
        chapeau="Lire un horaire d'ouverture et noter ce qu'on a entendu.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance du Défi 1. Commencer par projeter l'horaire réel du "
                  "secrétariat du centre, s'il en existe un affiché. Le vrai document "
                  "vaut mieux que celui de la diapositive.")

    d.objectifs([
        "dire premier, deuxième, troisième étage ;",
        "trouver l'étage d'un local à partir de son numéro ;",
        "lire un horaire d'ouverture et y trouver une heure ;",
        "écrire un jour et une heure dans son carnet.",
    ])

    d.dialogue('Dialogue', "À quelle heure ouvre le secrétariat ?", [
        ("AMEL", "Madame, une question. Le secrétariat ouvre à quelle heure ?", True),
        ("LINE", "À huit heures, du lundi au vendredi.", True),
        ("AMEL", "Et il ferme quand ?", True),
        ("LINE", "À seize heures. Mais le midi, c'est fermé.", True),
        ("AMEL", "Le midi… De midi à treize heures ?", True),
        ("LINE", "C'est ça. Une heure.", True),
    ], consigne="Écoutez, puis dites les trois heures que vous avez entendues.",
       notes="Faire écouter deux fois. Demander les trois nombres : huit, seize, midi. "
             "Les écrire au tableau, puis effacer et redemander.")

    d.tableau('Analyse · 1 de 2', "SECRÉTARIAT — heures d'ouverture",
              ["Quand", "Ouvert ou fermé"],
              [["Lundi au jeudi", "8 h à 12 h · 13 h à 16 h"],
               ["Vendredi", "8 h à 12 h"],
               ["Le midi", "fermé, de 12 h à 13 h"],
               ["Samedi et dimanche", "fermé"],
               ["Le soir", "fermé après 16 h"]],
              cle=1,
              note="Le vendredi après-midi est fermé aussi : la ligne ne le dit pas, il faut le lire.",
              notes="Diapositive à photographier. Poser trois questions dessus avant de "
                    "passer à la suite : « Mardi à quinze heures ? », « Vendredi à "
                    "quatorze heures ? », « Samedi ? »")

    d.tableau('Analyse · 2 de 2', "Le numéro dit l'étage",
              ["Le local", "L'étage"],
              [["005", "le rez-de-chaussée"],
               ["108", "le premier étage"],
               ["214", "le deuxième étage"],
               ["302", "le troisième étage"],
               ["401", "le quatrième étage"]],
              cle=1,
              note="On dit le nombre entier : « le local deux cent quatorze ».",
              notes="Diapositive à photographier. Faire dire les cinq numéros à voix "
                    "haute, en nombre entier. La lecture chiffre par chiffre ne sert "
                    "que quand on n'a pas été compris.")

    d.regle("Écrivez tout de suite.",
            "Un jour entendu s'oublie avant l'escalier.",
            precision="Trois choses à noter, et rien d'autre : le <b>papier</b> "
                      "demandé, le <b>jour</b>, l'<b>heure</b>. Trois mots dans un "
                      "carnet valent mieux qu'une bonne mémoire, et personne au "
                      "comptoir ne trouve ça impoli.",
            notes="Diapositive à photographier. Distribuer un vrai carton de la taille "
                  "d'une carte : ceux qui en ont un s'en servent, ceux qui n'en ont pas "
                  "oublient.")

    d.pratique('Pratique · 1 de 3', "À quel étage ?",
               "Écrivez l'étage en toutes lettres.", [
        ("Le local 214 est au ___ étage.", "deuxième"),
        ("Le local 108 est au ___ étage.", "premier"),
        ("Le local 302 est au ___ étage.", "troisième"),
        ("Le secrétariat est au ___.", "rez-de-chaussée"),
        ("Le local 401 est au ___ étage.", "quatrième"),
    ], corrige=True, cols=2,
       notes="Faire à l'oral d'abord. L'écriture de « deuxième » et « troisième » est "
             "le vrai travail : les faire écrire deux fois chacun.")

    d.pratique('Pratique · 2 de 3', "Lire l'horaire",
               "Vrai ou faux, d'après le tableau de l'horaire.", [
        ("Le secrétariat ouvre à huit heures.", "vrai"),
        ("Le midi, on peut aller au comptoir.", "faux - c'est fermé de 12 h à 13 h"),
        ("Le vendredi après-midi, c'est fermé.", "vrai"),
        ("Le samedi, le secrétariat est ouvert.", "faux - fermé la fin de semaine"),
        ("À dix-sept heures, on peut demander un papier.", "faux - fermé après 16 h"),
    ], corrige=True, cols=1,
       notes="Les deux dernières demandent de convertir : dix-sept heures, c'est cinq "
             "heures du soir. Le faire au tableau si le groupe hésite.")

    d.pratique('Pratique · 3 de 3', "Ma fiche de notes",
               "Réécoutez le dialogue du comptoir, puis remplissez.", [
        ("Le papier demandé", "une attestation"),
        ("Le nom donné", "Amel Tazi"),
        ("Le groupe", "madame Dufresne"),
        ("Le jour", "jeudi"),
        ("L'heure", "après neuf heures"),
    ], corrige=True, cols=2,
       notes="Vingt minutes. Refaire ensuite avec un vrai renseignement : l'heure "
             "d'ouverture du secrétariat du centre, que chacun va vérifier.")

    d.billet(
        "Écrivez l'horaire du secrétariat de votre centre.",
        exemples=[
            "Le secrétariat ouvre à…",
            "Il ferme à…",
            "Le midi, c'est…",
        ],
        notes="Devoir court, mais il oblige à sortir : l'horaire est affiché sur la "
              "porte, et personne ne l'a jamais lu.")

    return d.save(dossier)
