# -*- coding: utf-8 -*-
"""A4 · Une laveuse, un réfrigérateur, des micro-ondes.
Bloc A « Je découvre » · couleur ambre (écriture) · 60 min.
Source : exercice `prComposes`, mini-leçon `prComposes`, banc `FC_CARDS`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre='Une laveuse, un réfrigérateur',
        chapeau="Le genre d'un appareil ne se devine pas. Il s'apprend avec "
                "le mot, dès la première fois, et il s'écrit dans le carnet "
                "avec son article.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Prévoir que chaque élève ait son carnet de "
                  "vocabulaire ouvert : la séance se termine par une liste écrite.")

    d.objectifs([
        "employer un, une ou des devant un nom d'appareil ;",
        "reconnaître la famille des noms en -teur ;",
        "écrire les noms à trait d'union et leur pluriel ;",
        "noter un mot nouveau avec son article.",
    ])

    d.regle("Un mot d'appareil s'apprend avec son article",
            "une laveuse  ·  un réfrigérateur",
            precision="Rien dans l'objet ne dit le genre : une laveuse et un "
                      "réfrigérateur sont deux grosses boîtes blanches. Il n'y a "
                      "rien à comprendre, il y a quelque chose à ranger.",
            notes="Diapo à photographier. Insister : écrire « laveuse » tout seul dans "
                  "son carnet, c'est se préparer une hésitation pour des années.")

    d.tableau('Analyse', "Les appareils, par genre",
              ['Féminin', 'Masculin'],
              [["une laveuse", "un réfrigérateur"],
               ["une sécheuse", "un aspirateur"],
               ["une cuisinière", "un ordinateur"],
               ["une affichette", "un micro-ondes"]],
              cle=0,
              note="Les trois mots en -teur sont tous masculins : c'est la seule "
                   "vraie famille du tableau.",
              notes="Faire lire la colonne de gauche, puis celle de droite, à voix haute. "
                    "Le e final des féminins ne s'entend presque pas : c'est justement "
                    "pour ça qu'il faut l'écrire.")

    d.cartes("Les mots à trait d'union", "Trois choses à savoir", [
        ("Deux mots collés",
         "un micro-ondes, un lave-vaisselle, un grille-pain. Le premier morceau dit ce "
         "que l'appareil fait, le second sur quoi il le fait."),
        ("Le trait d'union n'est pas décoratif",
         "Sans lui, ce sont deux mots séparés et le sens se perd. « Lave vaisselle » "
         "n'est pas un appareil, c'est un ordre."),
        ("Le pluriel ne change rien",
         "un micro-ondes donne des micro-ondes ; un lave-vaisselle donne des "
         "lave-vaisselle. Seul le déterminant change."),
    ], cols=3,
       notes="Écrire les trois mots au tableau et faire venir un élève poser les traits "
             "d'union à la craie. Le geste se retient mieux que la règle.")

    d.pratique('Écriture', "Un, une ou des ?",
               "Complétez chaque phrase.", [
        ("Je cherche ___ laveuse pas trop chère.", "une"),
        ("Il y a ___ réfrigérateur en spécial.", "un"),
        ("Le magasin vend ___ micro-ondes de toutes les grandeurs.", "des"),
        ("Mon fils a besoin d'___ ordinateur portable.", "un"),
        ("Nous avons acheté ___ cuisinière blanche.", "une"),
        ("Au deuxième rayon, il y a ___ aspirateurs.", "des"),
    ], corrige=True,
       notes="Faire écrire d'abord, corriger ensuite au tableau. Demander à chaque fois "
             "pourquoi : le genre du mot, jamais celui de l'objet.")

    d.piege("Mettre un s à micro-ondes",
            "des micro-ondeses",
            "des micro-ondes",
            "Le s est déjà dans le mot au singulier — c'est le pluriel de « onde ». Au "
            "pluriel, rien ne bouge : seul « un » devient « des ». Même chose pour « des "
            "lave-vaisselle ».",
            notes="Erreur logique, donc fréquente chez les bons élèves. La signaler "
                  "avant qu'elle ne se produise.")

    d.tableau('Analyse', "Deux mots, un seul appareil",
              ['Au singulier', 'Au pluriel'],
              [["un ordinateur portable", "des ordinateurs portables"],
               ["une laveuse blanche", "des laveuses blanches"],
               ["un micro-ondes noir", "des micro-ondes noirs"]],
              cle=1,
              note="Quand l'appareil a un adjectif, les deux prennent la marque du "
                   "pluriel — sauf le mot à trait d'union, qui ne bouge jamais.",
              notes="Diapo à photographier. Faire remarquer que l'adjectif se met après "
                    "le nom, comme pour les vêtements du module précédent.")

    d.billet(
        "Écrivez six appareils avec leur article, puis mettez-les au pluriel.",
        exemples=[
            "une laveuse, des laveuses",
            "un micro-ondes, des micro-ondes",
        ],
        notes="Devoir d'écriture. Ramasser et corriger : c'est la seule trace écrite du "
              "bloc A, et elle sert de référence pour tout le module.")

    return d.save(dossier)
