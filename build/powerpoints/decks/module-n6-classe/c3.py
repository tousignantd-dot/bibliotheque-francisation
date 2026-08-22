# -*- coding: utf-8 -*-
"""C3 · Le, en, y : ce que remplacent les petits mots
Bloc C « Défi 2 » · couleur ambre · 75 min. Grammaire du texte.
Source du module : exercice `t2repr` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Le, en, y : ce que remplacent les petits mots",
        chapeau="Deux lettres qui ne se prononcent presque pas, et qui "
                "décident du sens de la phrase suivante. C'est le savoir le "
                "plus caractéristique du niveau 6.",
        duree='75 minutes')

    d.titre(notes="Ce n'est pas un détail de grammaire : c'est un accident de "
                  "lecture. Un élève qui perd un renvoi écrit tranquillement "
                  "le contraire de sa source, et il ne s'en aperçoit jamais "
                  "seul.")

    d.objectifs([
        "retrouver ce que « le » ramasse dans la phrase d'avant ;",
        "reconnaître le « en » des groupes en « de » et des quantités ;",
        "reconnaître le « y » des groupes en « à » et des lieux ;",
        "prendre le réflexe de reculer d'une phrase.",
    ], notes="L'objectif visé est un réflexe de lecture, pas une "
             "connaissance. Il s'installe en une semaine si on le fait à "
             "voix haute les premières fois.")

    d.declencheur(
        'Observation', "« La ville affirme que le plastique est refusé. Youssef ne le croit pas. » Il ne croit pas quoi ?",
        pistes=[
            "La ville en général ?",
            "Cette phrase-là seulement ?",
            "Comment le savoir ?",
        ],
        notes="Le groupe se partage, et c'est tout l'intérêt : la même "
              "phrase donne deux lectures très différentes selon ce qu'on "
              "croit que « le » remplace.")

    d.tableau('Analyse', "Trois mots, trois travaux",
              ['Le mot', 'Ce qu\'il remplace'],
              [["le, l'", "une phrase entière, souvent après « que »"],
               ["en", "ce qui suivait « de », et les quantités"],
               ["y", "ce qui suivait « à », et les lieux"]],
              cle=0,
              note="Ni « en » ni « y » ne s'emploient pour une personne : on dit « je pense à elle ».",
              notes="Diapositive à photographier. La note du bas règle une "
                    "faute très répandue et qu'on n'entend presque jamais "
                    "corriger.")

    d.regle("Le « le » d'une phrase reprise ne s'accorde jamais",
            "Elle pense que la collecte fonctionne. Elle le pense. — Jamais « elle la pense ».",
            precision="Il ne désigne ni un homme, ni une femme, ni un "
                      "pluriel : une phrase n'a pas de genre. Devant une "
                      "voyelle, il devient « l' ».",
            notes="Diapositive à photographier. C'est la seule règle "
                  "d'accord de la séance, et elle consiste à ne rien "
                  "accorder.")

    d.tableau('Analyse', "Sept renvois du dossier",
              ['La phrase', 'Ce que le mot remplace'],
              [["Nous n'en avons gardé qu'un.", "des trois chiffres du bulletin"],
               ["Youssef ne le croit pas.", "que la collecte ne sert à rien"],
               ["Elle y passe ses jeudis.", "à la bibliothèque du centre"],
               ["L'équipe y met ses sources.", "dans la bibliographie"],
               ["Youssef l'a oublié là.", "le plan"]],
              cle=0,
              note="Chaque fois : reculez d'une phrase, et demandez-vous ce que ça remplace.",
              notes="Diapositive à photographier. Faire lire chaque phrase "
                    "avec celle qui la précède : sans le contexte, aucune "
                    "n'a de sens, et c'est précisément le point.")

    d.piege('Lecture',
            "passer par-dessus sans s'arrêter",
            "reculer d'une phrase, chaque fois",
            "Ces mots font deux lettres et ne portent presque aucun son. "
            "C'est pour ça qu'on les saute — et qu'on perd le fil d'un "
            "paragraphe sans rien sentir. Faites-le à voix haute les "
            "premières fois : au bout d'une semaine, ça devient "
            "automatique.",
            notes="Faire l'exercice à voix haute sur un paragraphe de la "
                  "page de la ville, en s'arrêtant à chaque pronom. Long la "
                  "première fois, rapide dès la troisième.")

    d.pratique('Pratique', "De quoi parle ce petit mot ?",
               "Dites ce que remplace le mot en gras dans la deuxième phrase.", [
        ("Le bulletin donne trois chiffres. Nous n'en avons gardé qu'un.", "des trois chiffres"),
        ("La lectrice croit que la collecte ne sert à rien. Youssef ne le croit pas.", "que la collecte ne sert à rien"),
        ("Milagros travaille à la bibliothèque. Elle y passe ses jeudis.", "à la bibliothèque"),
        ("Le texte finit par une bibliographie. L'équipe y met ses sources.", "dans la bibliographie"),
        ("Il leur manque une source. Ils en cherchent une depuis lundi.", "une source"),
        ("Le plan est resté sur la table. Youssef l'a oublié là.", "le plan"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2repr` du module. En cols:1 comme lui : "
             "chaque item fait deux phrases et deux colonnes les rendraient "
             "illisibles.")

    d.billet(
        "Écris deux phrases : la seconde reprend quelque chose de la première.",
        exemples=[
            "Emploie « le », « en » ou « y » dans la seconde.",
            "Souligne, dans la première, ce que le petit mot remplace.",
        ],
        notes="Trois minutes. Le soulignement compte autant que la phrase : "
              "c'est lui qui montre si le renvoi est compris.")

    return d.save(dossier)
