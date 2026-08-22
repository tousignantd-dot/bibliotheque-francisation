# -*- coding: utf-8 -*-
"""C3 · Avant ou après le nom, ce n'est pas la même chose
Bloc C « Défi 2 » · couleur ambre · lexique et grammaire · 75 min.
Source : exercice `t2place` et sa mini-leçon — le savoir « connaître le sens
de certains adjectifs selon leur place : grand, propre, drôle, ancien ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Avant ou après le nom, ce n'est pas la même chose",
        chapeau="Mon ancien manteau et un manteau ancien : le même mot, le "
                "même vêtement, et deux images très différentes de celui "
                "qui le porte.",
        duree='75 minutes')

    d.titre(notes="Séance courte à préparer, longue à discuter. Écrire au tableau les "
                  "deux expressions du chapeau et demander laquelle Ghislain préfère "
                  "qu'on emploie pour lui. La réponse est dans le dialogue du Défi 2.")

    d.objectifs([
        "distinguer un grand homme d'un homme grand ;",
        "employer ancien, propre, drôle, pauvre et seul aux deux places ;",
        "choisir la place qui dit ce qu'on veut dire ;",
        "reconnaître le sens juste dans un texte, sans hésiter.",
    ], notes="Le quatrième objectif est le seul évalué à la lecture : ces adjectifs "
             "se rencontrent bien plus souvent qu'ils ne s'emploient.")

    d.declencheur(
        'Observation', "Ton grand frère, est-ce qu'il est grand ?",
        pistes=[
            "Que veut dire grand frère, exactement ?",
            "Et une grande dame ? Un grand malade ?",
            "Est-ce que ta langue fait la même différence ?",
            "Comment dirais-tu qu'il mesure six pieds ?",
        ],
        notes="L'exemple du grand frère fait rire et règle la question en trente "
              "secondes. Il est aussi la source d'un malentendu très courant chez les "
              "élèves de niveau 5 et 6.")

    d.tableau('Analyse', "Le même mot, deux sens",
              ['L\'expression', 'Ce qu\'elle veut dire'],
              [["son ancien manteau", "celui qu'il portait autrefois"],
               ["un manteau ancien", "un manteau très vieux, presque une antiquité"],
               ["un grand homme", "un homme important, connu pour ce qu'il a fait"],
               ["un homme grand", "un homme de haute taille"],
               ["sa propre valise", "la valise qui lui appartient"],
               ["une valise propre", "une valise qui n'est pas sale"]],
              cle=0,
              notes="Diapositive à photographier. Six rangées, pas de note : c'est la "
                    "densité maximale. Faire lire chaque paire par deux élèves "
                    "différents.")

    d.regle("Avant le nom, l'adjectif juge ; après, il décrit",
            "C'est la place, et seulement la place, qui décide du sens.",
            precision="Rien ne s'entend, rien ne se voit dans le mot lui-même : le "
                      "français met le sens dans l'ordre des mots. Six adjectifs "
                      "fonctionnent ainsi, et ils sont tous très courants : ancien, "
                      "grand, propre, drôle, pauvre, seul.",
            notes="Diapositive à photographier. Insister : ce n'est pas une exception "
                  "bizarre, c'est un procédé régulier du français.")

    d.cartes('Trois autres', "Drôle, pauvre, seul", [
        ("une drôle de journée",
         "Bizarre, inhabituelle. Avant le nom, avec de : quelque chose ne tournait pas rond."),
        ("une journée drôle",
         "Amusante. Après le nom : on a ri."),
        ("une seule valise",
         "Une, et pas deux. Avant le nom, c'est le nombre."),
        ("une valise seule",
         "Abandonnée sur le quai, sans personne à côté. Après le nom, c'est l'état."),
    ], notes="La dernière carte est aussi une consigne de sécurité dans un terminus. "
             "L'occasion de faire remarquer qu'une valise seule s'annonce.")

    d.pratique('Sens', "Que veut dire cette expression ?",
               "Lisez l'expression, puis dites ce qu'elle veut dire.", [
        ("son ancien manteau", "celui qu'il portait autrefois"),
        ("un manteau ancien", "un manteau qui a beaucoup d'années"),
        ("un grand homme", "un homme important"),
        ("un homme grand", "un homme de haute taille"),
        ("sa propre valise", "la valise qui lui appartient"),
        ("une valise propre", "une valise qui n'est pas sale"),
    ], corrige=True, cols=2,
       notes="Puis inverser l'exercice : donner le sens, demander l'expression. C'est "
             "plus difficile, et c'est là que la règle s'installe.")

    d.piege('Sens', "J'ai apporté ma propre valise, elle sort du lavage",
            "J'ai apporté ma valise propre, elle sort du lavage",
            "Avant le nom, propre insiste sur l'appartenance : ma propre valise veut "
            "dire la mienne, et pas celle d'un autre. Pour dire qu'elle est nettoyée, "
            "il faut la placer après le nom.",
            notes="Faire construire deux phrases par le groupe, une pour chaque sens. "
                  "L'erreur ne se corrige que par l'usage.")

    d.billet(
        "Écris deux phrases avec le même adjectif, avant puis après le nom.",
        exemples=[
            "Choisis ancien, grand, propre, drôle, pauvre ou seul.",
            "Explique la différence en quelques mots.",
        ],
        notes="Deux minutes. Les meilleures paires se lisent au groupe en ouverture de "
              "C4.")

    return d.save(dossier)
