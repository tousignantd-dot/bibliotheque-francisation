# -*- coding: utf-8 -*-
"""B2 · Un crayon rouge, une feuille blanche.
Bloc B « Défi 1 · La consigne de l'enseignante » · couleur ambre · 75 min.
Source : exercice `t1couleur`, mini-leçon `t1couleur`.

La séance d'écriture du Défi 1. A3 a nommé les six couleurs ; ici on les
place et on les accorde — le premier accord du niveau 2, et celui qui revient
ensuite partout, à l'épicerie comme au magasin.

Une seule règle, tenue jusqu'au bout : c'est le mot de l'objet qui décide,
jamais la couleur.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-classe/images/')


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Un crayon rouge, une feuille blanche",
        chapeau="La couleur se dit après l'objet — et elle change de forme "
                "quand l'objet est féminin.",
        duree='75 minutes')

    d.titre(notes="Séance d'écriture. Prévoir des crayons de couleur et des feuilles : "
                  "les élèves écrivent les groupes de mots à côté de l'objet réel, ce "
                  "qui rend l'accord visible.")

    d.objectifs([
        "placer la couleur après l'objet ;",
        "accorder la couleur au féminin ;",
        "ajouter le -s du pluriel ;",
        "écrire six groupes de mots sans faute.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui change entre ces deux mots ?",
        image=IMG + 'boite-crayons.jpg',
        pistes=[
            "un cahier vert — une gomme verte",
            "Est-ce que ça s'écrit pareil ?",
            "Est-ce que ça se dit pareil ?",
            "Qu'est-ce qui a changé avant la couleur ?",
        ],
        notes="La quatrième piste est la bonne : ce qui a changé, c'est « un » devenu "
              "« une ». Laisser le groupe le trouver ; c'est toute la règle.")

    d.tableau('Analyse', "C'est l'objet qui décide",
              ["Masculin", "Féminin"],
              [["un cahier vert", "une gomme verte"],
               ["le tableau noir", "la chaise noire"],
               ["un mur blanc", "une feuille blanche"],
               ["un crayon rouge", "une gomme rouge"]],
              cle=2,
              note="Rouge et jaune ne changent jamais : ils finissent déjà par un e.",
              notes="Diapositive à photographier. Faire lire les deux colonnes à voix "
                    "haute : le t de « verte » s'entend, celui de « vert » non.")

    d.regle("L'objet d'abord, la couleur ensuite",
            "L'ordre ne change jamais en français.",
            precision="On dit « un crayon <b>rouge</b> », jamais « un rouge crayon ». "
                      "Beaucoup de langues font l'inverse : c'est l'erreur la plus "
                      "fréquente du niveau, et elle disparaît vite quand on la nomme.",
            notes="Diapositive à photographier. Demander au groupe comment ça se dit dans "
                  "leur langue : la comparaison ancre la règle mieux qu'une répétition.")

    d.regle("Le -e du féminin",
            "Trois couleurs changent, deux ne changent pas.",
            precision="Elles changent : vert / <b>verte</b>, noir / <b>noire</b>, "
                      "blanc / <b>blanche</b>. Elles ne changent pas : <b>rouge</b>, "
                      "<b>jaune</b>. Au pluriel, tout prend un -s : deux crayons "
                      "<b>bleus</b>, trois feuilles <b>blanches</b>.",
            notes="Diapositive à photographier. Le -s ne s'entend pas : le dire, sinon "
                  "les élèves croient l'avoir mal entendu et cherchent une différence "
                  "qui n'existe qu'à l'écrit.")

    d.piege('Le piège du jour',
            "une feuille blanc",
            "une feuille blanche",
            "L'élève regarde la couleur pour décider. Il faut regarder « une » : "
            "c'est le petit mot devant l'objet qui commande tout le reste de la "
            "phrase, y compris la couleur.",
            notes="Faire le geste : couvrir la couleur avec la main, lire « une "
                  "feuille », puis découvrir. Le réflexe s'installe en une séance.")

    d.pratique('Écriture', "Complétez avec la bonne forme",
               "Écrivez la couleur entre parenthèses à la bonne forme.", [
        ("Myriam prend un crayon ___ . (rouge)", "rouge"),
        ("Prenez une feuille ___ . (blanc)", "blanche"),
        ("Les cinq mots du tableau sont ___ . (bleu)", "bleus"),
        ("Le sac de Tariq est ___ . (vert)", "vert"),
        ("J'ai deux gommes ___ . (jaune)", "jaunes"),
        ("La chaise du fond est ___ . (noir)", "noire"),
    ], corrige=True, cols=1,
       notes="Ce sont les six énoncés de l'exercice 3 du module en ligne. Les faire "
             "écrire au tableau par six élèves différents, et corriger en groupe.")

    d.pratique('Pratique · à deux', "Décrivez votre pupitre",
               "Deux par deux, en écrivant.", [
        ("Étape 1", "Chacun écrit six groupes : objet + couleur."),
        ("Étape 2", "On échange les feuilles et on vérifie les accords."),
        ("Étape 3", "On lit à voix haute : le t de « verte » doit s'entendre."),
        ("Étape 4", "On recommence au pluriel : deux crayons, trois feuilles."),
    ], cols=1,
       notes="Vingt minutes. L'étape 2 vaut mieux qu'une correction de l'enseignante : "
             "chercher la faute d'un autre apprend plus que se faire corriger.")

    d.billet(
        "Décrivez trois objets de votre sac, avec leur couleur.",
        exemples=[
            "un cahier bleu",
            "une gomme blanche",
            "deux crayons noirs",
        ],
        notes="Devoir court. Corriger l'accord cette fois : c'est la matière de la "
              "séance, et le module y revient en E1 dans la production écrite.")

    return d.save(dossier)
