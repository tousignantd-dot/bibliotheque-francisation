# -*- coding: utf-8 -*-
"""D2 · L'adjectif s'accorde, et il se place.
Bloc D « Défi 3 · Il est comment ? » · couleur ambre (écriture) · 60 min.
Source : exercices `t3adj`, `t3int` et `t3aff`, mini-leçons `t3adj` et `t3int`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="L'adjectif s'accorde, et il se place",
        chapeau="Un chat roux, une tuque rousse. Un collier bleu, une porte "
                "bleue. L'adjectif suit le nom — en genre, en nombre, et le "
                "plus souvent en position.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Commencer par le jeu des billets de D1 : lire trois "
                  "descriptions à voix haute, faire retrouver l'objet dans la classe. "
                  "Celles qui échouent montrent d'elles-mêmes ce qui manque.")

    d.objectifs([
        "accorder l'adjectif avec le nom qu'il décrit ;",
        "placer l'adjectif après le nom, sauf les quelques-uns qui passent devant ;",
        "employer très, assez, un peu et trop ;",
        "écrire une affiche complète pour un objet ou un animal perdu.",
    ])

    d.regle("Il s'accorde avec le nom",
            "Un chat roux, une tuque rousse. Un collier bleu, une porte bleue.",
            precision="Au féminin, on ajoute souvent un « e » — et il "
                      "s'entend : rousse, bleue, blanche. Au pluriel, un "
                      "« s » — qui, lui, ne s'entend pas.",
            notes="Diapo à photographier. Le point important est celui de la précision : "
                  "le féminin change le son, le pluriel non. C'est ce qui explique que "
                  "l'erreur du pluriel survive longtemps à l'écrit.")

    d.tableau('Analyse', "Où se place l'adjectif",
              ["La place", "Les adjectifs concernés"],
              [["après le nom — la règle", "les couleurs, les formes, les matières"],
               ["", "un chat roux, un ourson usé"],
               ["avant le nom — l'exception", "les courts et les plus courants"],
               ["", "un petit ourson, une grande dame, un beau chat"]],
              cle=1,
              note="Les exceptions sont peu nombreuses : petit, grand, beau, "
                   "vieux, jeune, bon, gros. On les apprend comme une liste.",
              notes="Diapo à photographier. Ne pas chercher de règle derrière la liste — "
                    "il n'y en a pas d'utile à ce niveau. Sept mots à connaître, et tout "
                    "le reste passe derrière.")

    d.pratique('Écriture', "Écrivez l'adjectif à la bonne forme",
               "Attention au genre et au nombre du nom.", [
        ("Caramel est un chat ___ (roux).", "roux"),
        ("Il porte un collier ___ (bleu).", "bleu"),
        ("Il a une tache ___ (blanc) sous le menton.", "blanche"),
        ("La dame du premier a les cheveux ___ (court).", "courts"),
        ("Elle porte des lunettes ___ (rouge).", "rouges"),
        ("Sur les clés, il y a un ___ (petit) ourson en tissu.", "petit"),
    ], corrige=True,
       notes="C'est l'exercice `t3adj` du module interactif, mot pour mot. Faire chercher "
             "le nom avant d'écrire l'adjectif : c'est lui qui commande, et l'élève qui "
             "le nomme d'abord se trompe rarement.")

    d.regle("Quatre mots qui disent combien",
            "Très peureux. Assez gros. Un peu usé. Trop de place.",
            precision="Toujours devant l'adjectif, jamais derrière. Et "
                      "« trop » dit toujours qu'il y a un problème : un "
                      "chat n'est pas « trop gros » si personne ne s'en "
                      "plaint.",
            notes="Diapo à photographier. La nuance de « trop » est celle qui manque le "
                  "plus souvent : beaucoup d'élèves l'emploient comme un simple "
                  "« beaucoup », ce qui donne des compliments qui sonnent comme des "
                  "reproches.")

    d.pratique('Écriture', "Très, assez, un peu ou trop",
               "Choisissez le mot qui dit la bonne quantité.", [
        ("Caramel est ___ peureux : il se sauve tout le temps.", "très"),
        ("Il est ___ gros, mais ce n'est pas un gros chat.", "assez"),
        ("L'ourson des clés est ___ usé, il a servi longtemps.", "un peu"),
        ("Mon vélo prend ___ de place : je dois le déménager.", "trop"),
        ("Madame Lachapelle a été ___ gentille avec nous.", "très"),
        ("L'escalier est ___ étroit pour monter un divan.", "trop"),
    ], corrige=True,
       notes="C'est l'exercice `t3int` du module interactif. Les deux dernières lignes "
             "opposent « très » et « trop » sur la même construction : c'est là que la "
             "différence s'entend le mieux.")

    d.pratique('Compréhension', "L'affiche punaisée dans l'entrée",
               "« Mon chat est perdu. Il s'appelle Caramel. C'est un chat roux, assez "
               "gros, avec une tache blanche sous le menton. Il porte un collier bleu, "
               "sans médaille. Il est très peureux : n'essayez pas de le prendre, "
               "appelez-moi. Vu pour la dernière fois lundi soir, dans la ruelle. "
               "Manon Lachapelle, 2B. »", [
        ("L'affiche donne le nom de l'animal.", "vrai — Caramel"),
        ("Le chat est petit et noir.", "faux — roux et assez gros"),
        ("Le collier porte une médaille avec un numéro.", "faux — sans médaille"),
        ("L'affiche demande de ne pas essayer de prendre le chat.", "vrai"),
        ("On sait où le chat a été vu la dernière fois.", "vrai — dans la ruelle"),
        ("L'affiche dit à quelle porte frapper.", "vrai — au 2B"),
    ], corrige=True,
       notes="C'est l'exercice `t3aff` du module interactif. Projeter l'affiche et faire "
             "souligner les six renseignements : nom, couleur, taille, détail, caractère, "
             "lieu et porte. C'est le modèle de l'écrit demandé au billet.")

    d.billet(
        "Écrivez l'affiche d'un objet ou d'un animal perdu.",
        exemples=[
            "Le nom, la couleur, la taille, le détail.",
            "Où et quand vous l'avez vu la dernière fois, et votre numéro de porte.",
        ],
        notes="Devoir court, six lignes au plus. Ramasser : c'est le dernier écrit avant "
              "les productions de E1, et le seul où l'élève écrit pour des inconnus.")

    return d.save(dossier)
