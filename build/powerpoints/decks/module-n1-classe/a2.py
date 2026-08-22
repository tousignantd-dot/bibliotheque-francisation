# -*- coding: utf-8 -*-
"""A2 · Deux ou douze ?
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source du module : exercice `prNombres` et sa mini-leçon.

Les nombres sont la première chose qu'un débutant doit entendre juste : la
page, l'heure, le local, le nombre de feuilles. Quatre paires font presque
toutes les erreurs, et elles ne diffèrent que par la fin du mot.

Aucun symbole hors Verdana dans cette séance : les sons se nomment par leurs
lettres et par un mot repère, jamais par l'alphabet phonétique.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Deux ou douze ?',
        chapeau="Quatre paires de nombres qui se ressemblent beaucoup. Le "
                "début est presque pareil : c'est la fin qui change.",
        duree='75 minutes')

    d.titre(notes="Séance d'écoute. Prévoir des écouteurs si la salle en a : l'exercice "
                  "du module se fait carte par carte, chacun à son rythme.")

    d.objectifs([
        "compter de un à seize ;",
        "entendre la différence entre deux et douze ;",
        "écrire le nombre entendu ;",
        "dire « Pardon ? » quand on n'est pas sûr.",
    ])

    d.regle("La fin du mot",
            "Le petit nombre est court. Le grand continue.",
            precision="<b>deux</b> et <b>douze</b>, <b>trois</b> et <b>treize</b>, "
                      "<b>six</b> et <b>seize</b> : le grand nombre finit par le son "
                      "« ze ». Le petit s'arrête avant.",
            notes="Diapositive à photographier. Dire les paires lentement, puis "
                  "normalement. Faire lever la main gauche pour le petit, la droite pour "
                  "le grand.")

    d.tableau('Analyse', "Les quatre paires",
              ['Avant dix', 'Après dix'],
              [["deux", "douze"],
               ["trois", "treize"],
               ["quatre", "quatorze"],
               ["six", "seize"]],
              cle=2,
              note="Quatorze est plus long à dire que quatre. Le plus long est le plus "
                   "grand.",
              notes="Diapositive à photographier. Faire répéter chaque paire trois fois, "
                    "en chœur puis un par un.")

    d.pratique('Écoute', "Petit ou grand ?",
               "L'enseignante dit un nombre. Écrivez P ou G.", [
        ("1.", "douze — G"),
        ("2.", "trois — P"),
        ("3.", "quatorze — G"),
        ("4.", "six — P"),
        ("5.", "treize — G"),
        ("6.", "quatre — P"),
    ], corrige=True, cols=2,
       notes="Dire les six nombres une fois, à vitesse normale. Puis reprendre le "
             "corrigé en les redisant lentement.")

    d.cartes('Compter', "De un à seize", [
        ("De un à six",
         "un, deux, trois, quatre, cinq, six. Ce sont les nombres courts."),
        ("De sept à onze",
         "sept, huit, neuf, dix, onze. Onze est le premier des grands, et il ne "
         "ressemble à rien."),
        ("De douze à seize",
         "douze, treize, quatorze, quinze, seize. Tous finissent par le même son."),
    ], notes="Diapositive à photographier. Compter ensemble à voix haute, deux fois, en "
             "montrant les doigts.")

    d.pratique('Écriture', "Le nombre entendu",
               "Écrivez le chiffre, pas le mot.", [
        ("Ouvrez à la page deux.", "2"),
        ("Ouvrez à la page douze.", "12"),
        ("Il y a treize personnes.", "13"),
        ("Le local quatorze.", "14"),
        ("Prenez seize feuilles.", "16"),
        ("La pause dure quinze minutes.", "15"),
    ], corrige=True, cols=1,
       notes="Le nombre est dans une phrase, pas seul : c'est ainsi qu'on l'entend en "
             "classe. Lire chaque phrase deux fois.")

    d.piege("Écrire avant la fin du mot",
            "On entend « deu… » et on écrit 2.",
            "Attendre la fin du mot.",
            "Le début de « deux » et de « douze » se ressemble beaucoup. Une seconde "
            "d'attente suffit : c'est la <b>fin</b> qui porte la différence.",
            notes="Insister : ce n'est pas un problème d'oreille. Ces mots se ressemblent "
                  "vraiment, et tout le monde fait répéter au téléphone.")

    d.regle("Pardon ?",
            "Un seul mot pour faire répéter.",
            precision="Quand vous n'êtes pas sûr du nombre, dites « <b>Pardon ?</b> » "
                      "L'enseignante répétera plus lentement. Ce n'est pas une faute : "
                      "c'est une phrase de la langue.",
            notes="Diapositive à photographier. Faire dire « Pardon ? » par tout le "
                  "groupe, une fois, à voix haute. Enlever la gêne tout de suite.")

    d.pratique('Pratique · à deux', "Dis un nombre",
               "Deux par deux, avec un papier et un crayon.", [
        ("Étape 1", "A dit un nombre entre 1 et 16."),
        ("Étape 2", "B écrit le chiffre."),
        ("Étape 3", "A montre son papier : est-ce le bon ?"),
        ("Étape 4", "Dix nombres, puis on change de rôle."),
    ], cols=1,
       notes="Vingt minutes. Encourager l'emploi de « Pardon ? » : compter combien de "
             "fois il sert dans le groupe et le dire à la fin.")

    d.billet(
        "Écrivez en lettres : 2, 12, 4, 14, 6, 16.",
        exemples=[
            "Un nombre par ligne.",
            "Puis dites-les à voix haute, dans l'ordre, trois fois.",
        ],
        notes="Écrire le mot en entier oblige à entendre la fin. C'est là tout l'intérêt "
              "du devoir.")

    return d.save(dossier)
