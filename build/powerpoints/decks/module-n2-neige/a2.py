# -*- coding: utf-8 -*-
"""A2 · An ou on ?
Bloc A « Je découvre » · couleur indigo · 75 min. Séance de graphie-phonie.
Source : exercice `prSon` et sa mini-leçon « An et on : deux sons du nez ».

Le programme du niveau 2 demande le système vocalique et la graphie-phonie.
Deux sons nasaux décident de tout l'hiver : celui de « vent » et celui de
« bonjour ». Ils sont proches, et l'élève qui les confond dit « le vont » et
« ils sant ». La séance les sépare par la bouche avant de les séparer par
l'écriture.

Aucun alphabet phonétique sur les diapositives : le gabarit est en Verdana,
et le programme du niveau 2 n'en demande pas. Les sons se nomment par un mot
connu — « le son de vent », « le son de bonjour ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="An ou on ?",
        chapeau="Entendre et écrire les deux sons du nez : « vent » et « bonjour ».",
        duree='75 minutes')

    d.titre(notes="Deuxième séance. Commencer par dire quatre mots à voix haute — vent, "
                  "bonjour, temps, ils sont — et demander lesquels vont ensemble. "
                  "Personne ne se trompe complètement, et personne n'a tout bon.")

    d.objectifs([
        "entendre la différence entre « vent » et « bonjour » ;",
        "dire les deux sons avec la bonne bouche ;",
        "écrire an, am, en, em et on, om ;",
        "connaître la règle du m devant b et p.",
    ])

    d.regle("Deux sons passent par le nez.",
            "« Le vent » et « bonjour » ne se disent pas pareil.",
            precision="Pour le son de <b>vent</b>, la bouche s'ouvre grand. Pour le "
                      "son de <b>bonjour</b>, les lèvres font un rond. C'est la bouche "
                      "qui décide, pas l'oreille.",
            notes="Diapositive à photographier. Faire poser la main sous le menton : "
                  "pour « an », la mâchoire descend. C'est le repère le plus sûr.")

    d.tableau('Analyse · 1 de 2', "La famille du son de « vent »",
              ["On écrit", "Exemples"],
              [["an", "janvier · un an"],
               ["am", "une lampe · une chambre"],
               ["en", "le vent · l'argent"],
               ["em", "le temps · novembre · le printemps"]],
              cle=1,
              note="Un seul son, quatre façons de l'écrire.",
              notes="Diapositive à photographier. Faire lire la colonne de droite à voix "
                    "haute, en série, sans commenter. Le son s'installe par répétition.")

    d.tableau('Analyse · 2 de 2', "La famille du son de « bonjour »",
              ["On écrit", "Exemples"],
              [["on", "bonjour · long · ils sont"],
               ["om", "un nombre · tomber"],
               ["Les lèvres", "elles font un rond, comme pour siffler"],
               ["On ne dit pas", "« banjour » ni « ils sant »"]],
              cle=1,
              note="Deux façons de l'écrire seulement. C'est la famille la plus simple.",
              notes="Diapositive à photographier. Faire avancer les lèvres. Le son sort "
                    "plus petit et plus fermé que celui de « vent ».")

    d.regle("Devant b et p, on écrit m.",
            "novembre · décembre · le printemps · une chambre",
            precision="C'est la seule règle d'écriture de la séance, et elle explique "
                      "six mots de l'hiver d'un coup. Elle vaut pour les deux "
                      "familles : <b>nom</b>bre, <b>tom</b>ber.",
            notes="Diapositive à photographier. Faire chercher d'autres mots dans le "
                  "cahier : lampe, jambe, compter. La règle se vérifie à chaque fois.")

    d.pratique('Écoute', "An ou on ?",
               "Écoutez chaque mot. Levez une main pour « an », deux pour « on ».", [
        ("le vent", "an"),
        ("bonjour", "on"),
        ("le temps", "an"),
        ("ils sont", "on"),
        ("janvier", "an"),
        ("un manteau long", "on - c'est « long » qu'on écoute"),
        ("novembre", "an"),
        ("nous montons", "on"),
    ], corrige=True, cols=2,
       notes="Les mains levées disent tout de suite qui suit et qui devine. Reprendre "
             "seulement les mots où le groupe se sépare en deux.")

    d.pratique('Prononciation', "Trois pièges du son de « vent »",
               "Répétez après l'enseignant, puis entre vous.", [
        ("Ne pas dire « le vont »", "la bouche ne s'ouvre pas assez : ouvrez grand"),
        ("Ne pas prononcer le n de la fin", "la langue ne touche rien : « le van »"),
        ("Ne pas écrire « tenps »", "devant p, on écrit m : le temps"),
    ], cols=1,
       notes="Le deuxième piège est le plus fréquent chez les élèves hispanophones et "
             "arabophones. Faire tenir la langue en bas de la bouche pendant le mot.")

    d.pratique('Pratique · dictée courte', "Six mots à écrire",
               "L'enseignant dit le mot deux fois. Écrivez-le.", [
        ("janvier", "an"),
        ("novembre", "em, devant b"),
        ("bonjour", "on"),
        ("le temps", "em, devant p"),
        ("le printemps", "em, devant p"),
        ("ils sont", "on"),
    ], corrige=True, cols=2,
       notes="Corriger au tableau, un mot à la fois, en demandant à chaque fois "
             "pourquoi c'est m ou n. La règle se fixe en la disant, pas en l'écoutant.")

    d.billet(
        "Écrivez trois mots avec le son de « vent » et trois mots avec le son de « bonjour ».",
        exemples=[
            "le vent, janvier, novembre",
            "bonjour, ils sont, un nombre",
        ],
        notes="Devoir court. Accepter les mots trouvés ailleurs que dans le module : "
              "un élève qui rapporte « la chambre » a compris la règle.")

    return d.save(dossier)
