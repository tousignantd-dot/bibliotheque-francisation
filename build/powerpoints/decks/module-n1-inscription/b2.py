# -*- coding: utf-8 -*-
"""B2 · Quel, quelle, et la date de naissance.
Bloc B « Défi 1 » · couleur ambre · 60 min.
Source : mini-leçons `t1quel` et `t1date`, dialogue `t1b`, exercices du même nom.

Deuxième et dernière séance du défi 1. Deux points de langue, et le second est
celui qui coûte le plus cher quand il est raté : l'ordre de la date.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Quel, quelle, et la date de naissance',
        chapeau="Le jour avant le mois. Ce n'est pas l'ordre de tout le "
                "monde, et une date lue à l'envers vous change d'âge.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Prévoir un calendrier au mur, ou l'écrire au "
                  "tableau : les douze mois avec leur numéro, visibles toute la séance.")

    d.objectifs([
        "écrire quel devant un mot masculin, quelle devant un mot féminin ;",
        "dire sa date de naissance ;",
        "l'écrire dans l'ordre jour / mois / année ;",
        "écrire l'année en quatre chiffres.",
    ])

    d.dialogue('Dialogue', "Quelle est votre date de naissance ?", [
        ("MADAME CÔTÉ", "Quelle est votre date de naissance ?", True),
        ("YUSUF", "Le douze mars.", True),
        ("MADAME CÔTÉ", "Quelle année ?", True),
        ("YUSUF", "Mille neuf cent quatre-vingt-douze.", True),
        ("MADAME CÔTÉ", "Douze, zéro trois, quatre-vingt-douze.", True),
        ("YUSUF", "Zéro trois ? Pourquoi ?", True),
        ("MADAME CÔTÉ", "Mars, c'est le mois numéro trois.", True),
        ("YUSUF", "Ah ! Le jour avant le mois.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="La question de Yusuf — « zéro trois ? pourquoi ? » — est celle que les élèves "
             "n'osent pas poser. La faire répéter telle quelle.")

    d.tableau('Analyse · 1 de 2', "Quel ou quelle ?",
              ['Devant un mot masculin', 'Devant un mot féminin'],
              [["quel est votre nom ?", "quelle est votre adresse ?"],
               ["quel est votre prénom ?", "quelle est votre date ?"],
               ["quel est votre numéro ?", "quelle est votre année ?"]],
              note="C'est le mot qui suit qui décide, jamais la personne qui parle.",
              notes="Diapo à photographier. Un homme dit bien « quelle est mon adresse ? » : "
                    "le dire explicitement, l'erreur est très fréquente.")

    d.regle("Quel et quelle se disent pareil",
            "On entend « kel » dans les deux cas.",
            precision="La différence ne se voit qu'à l'écrit, et elle vient du mot d'après : "
                      "<b>le</b> nom, <b>le</b> prénom, <b>le</b> numéro sont masculins ; "
                      "<b>l'</b>adresse, <b>la</b> date, <b>l'</b>année sont féminines. À "
                      "l'oral, vous ne pouvez pas vous tromper.",
            notes="Diapo à photographier. C'est une bonne nouvelle : la dire comme telle.")

    d.tableau('Analyse · 2 de 2', "Les douze mois en chiffres",
              ['Le mois', 'Le numéro'],
              [["janvier · février · mars", "01 · 02 · 03"],
               ["avril · mai · juin", "04 · 05 · 06"],
               ["juillet · août · septembre", "07 · 08 · 09"],
               ["octobre · novembre · décembre", "10 · 11 · 12"]],
              cle=2,
              note="Comptez sur vos doigts : c'est le seul moyen, et il marche.",
              notes="Diapo à photographier. Faire trouver à chacun le numéro de son mois de "
                    "naissance, à voix haute, en tour de table.")

    d.regle("Le jour, le mois, puis l'année",
            "Le 12 mars 1992 s'écrit 12 / 03 / 1992.",
            precision="Deux chiffres pour le jour — le 5 janvier s'écrit <b>05</b> / 01 — "
                      "deux pour le mois, et <b>quatre</b> pour l'année : 1992, jamais 92. "
                      "Dans plusieurs pays le mois passe devant : la même date y devient "
                      "03 / 12 / 1992, c'est-à-dire le 3 décembre.",
            notes="Diapo à photographier. Quand on doute, on écrit le mois en lettres : "
                  "12 mars 1992. Personne ne peut alors se tromper.")

    d.pratique('Pratique', "Complétez",
               "Yusuf est né le 12 mars 1992.", [
        ("Le jour : ___", "12"),
        ("Le mois de mars s'écrit ___", "03"),
        ("L'année : ___", "1992"),
        ("Le 5 janvier s'écrit ___ / 01", "05"),
        ("Le jour, le ___ , l'année.", "mois"),
        ("Le mois de septembre s'écrit ___", "09"),
    ], corrige=True, cols=2,
       notes="Ce sont les six énoncés de l'exercice `t1date`. Au tableau d'abord, à "
             "l'ordinateur ensuite.")

    d.piege("Écrire l'année à deux chiffres",
            "Naissance : 12 / 03 / 92.",
            "Naissance : 12 / 03 / 1992.",
            "Quatre chiffres, toujours. Une fiche refuse souvent les deux chiffres, et "
            "« 26 » peut vouloir dire 1926 comme 2026. Le premier jour du mois, lui, "
            "s'écrit <b>1er</b> : le 1er novembre, jamais « un novembre ».",
            notes="Deux erreurs dans le même piège, parce qu'elles arrivent ensemble sur la "
                  "même ligne de la fiche.")

    d.pratique('Pratique · à deux', "Votre date, la sienne",
               "Demandez, écoutez, écrivez — puis faites vérifier.", [
        ("Étape 1", "Quelle est votre date de naissance ?"),
        ("Étape 2", "Écrivez-la en chiffres : __ / __ / ____"),
        ("Étape 3", "Relisez à voix haute : « douze, zéro trois, mille neuf cent… »"),
        ("Étape 4", "Montrez ce que vous avez écrit. C'est bien ça ?"),
    ], cols=1,
       notes="Quinze minutes. L'étape 4 est la plus importante : c'est elle qui attrape le "
             "13 écrit à la place du 30, entendu à la séance A2.")

    d.billet(
        "Écrivez votre date de naissance de deux façons.",
        exemples=[
            "En chiffres : __ / __ / ____",
            "En lettres : le … (mois) …",
            "Puis dites-la à voix haute, lentement.",
        ],
        notes="Deux minutes. C'est le brouillon de la fiche écrite de la séance E1.")

    return d.save(dossier)
