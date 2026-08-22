# -*- coding: utf-8 -*-
"""B1 · L'ordre d'une présentation qui se tient
Bloc B « Défi 1 · Ce que raconte l'histoire » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1a`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="L'ordre d'une présentation qui se tient",
        chapeau="Karim demande à Mai de raconter son roman. Elle le connaît "
                "par cœur et elle ne sait pas par où commencer — c'est le "
                "problème de tout le monde. Il y a un ordre, il tient en "
                "cinq temps, et il ne s'invente pas à chaque fois.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 1. Commencer en demandant à un élève de "
                  "raconter un film en une minute, sans préparation. Le groupe repère "
                  "tout de suite ce qui manque : on ne sait pas où ça se passe, on ne "
                  "sait pas qui est le personnage. Ne pas corriger — la séance le fera.")

    d.objectifs([
        "reconnaître les cinq temps d'une présentation d'œuvre ;",
        "commencer par ce qu'on raconte, jamais par un détail ;",
        "donner le lieu et l'époque en une seule phrase ;",
        "nommer le personnage principal et ce qu'il veut.",
    ], notes="Le deuxième objectif est celui qui demande le plus de reprises. La tentation "
             "est de commencer par « c'était vers la fin de l'hiver… » — un détail qui ne "
             "sert à rien tant qu'on ne sait pas de quoi on parle.")

    d.declencheur(
        'Mise en route', "Vous racontez un film à quelqu'un qui ne l'a pas vu. "
                         "Par quoi commencez-vous ?",
        pistes=[
            "Par le nom des personnages ? Par l'endroit ? Par la fin ?",
            "Qu'est-ce que la personne en face a besoin de savoir en premier ?",
            "Combien de personnages pouvez-vous nommer avant qu'on se perde ?",
            "Où vous arrêtez-vous ?",
        ],
        notes="Les réponses varient beaucoup, et c'est utile : le groupe découvre qu'il "
              "n'y a pas d'ordre naturel. La troisième piste a une réponse ferme — deux, "
              "trois au plus. Au-delà, personne ne suit.")

    d.dialogue('Dialogue · 1 de 3', "Par le commencement", [
        ("KARIM", "Vous avez fini votre roman ? Vous en parlez jeudi ?", True),
        ("MAI", "Je pense. Mais je ne sais pas comment le raconter.", True),
        ("KARIM", "Commencez par le commencement. Ça se passe où ?", True),
        ("MAI", "Dans un village au bord de la mer. Une femme y revient "
                "après vingt ans.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la réponse de Mai : deux informations en une phrase, le lieu "
             "et le personnage. C'est exactement la dose. Un troisième détail et la phrase "
             "devient trop longue à retenir.")

    d.dialogue('Dialogue · 2 de 3', "Ce que le personnage veut", [
        ("KARIM", "Bon. Et elle revient pour quoi ?", True),
        ("MAI", "Pour vendre la maison de sa mère. Elle veut repartir le jour même.", True),
        ("KARIM", "Attendez : vous racontez ça au présent ?", True),
        ("MAI", "Oui. C'est comme ça qu'on raconte une histoire, non ?", True),
    ], notes="La deuxième réplique donne le désir du personnage — « elle veut repartir le "
             "jour même ». C'est ce qui rend l'histoire intéressante avant même qu'il "
             "arrive quelque chose. Le faire remarquer : sans désir, pas d'histoire.")

    d.dialogue('Dialogue · 3 de 3', "Là où on s'arrête", [
        ("MAI", "Donc : elle arrive, elle ouvre la maison, et elle trouve une "
                "boîte de lettres.", True),
        ("KARIM", "Là, vous me tenez. Des lettres de qui ?", True),
        ("MAI", "Ça, je ne le dis pas. C'est ce qui fait tourner toute l'histoire.", True),
        ("KARIM", "Parfait. Vous ne dites jamais ce qui arrive à la fin.", False),
    ], notes="« Là, vous me tenez » est la phrase à relever : c'est l'obstacle qui donne "
             "envie, pas la solution. Et le refus de Mai — « ça, je ne le dis pas » — est "
             "le modèle de la séance B4.")

    d.regle("Cinq temps, toujours dans le même ordre",
            "De quoi je parle · où et quand · qui, et ce qu'il veut · ce qui "
            "complique tout · et je m'arrête.",
            precision="Chaque temps tient en une phrase. Cinq phrases font environ "
                      "quarante secondes : il vous en reste autant pour l'avis. Cet "
                      "ordre n'est pas une contrainte scolaire — c'est celui de tous "
                      "les résumés au dos des livres, et de toutes les bandes-annonces.",
            notes="Diapositive à photographier. Faire écrire les cinq temps sur une feuille "
                  "que l'élève gardera jusqu'à la séance E1. C'est le plan de sa "
                  "production orale.")

    d.tableau('Les cinq temps', "Ce que chacun contient, et ce qu'il ne contient pas",
              ['Le temps', 'Ce qu\'on y met'],
              [["1 · De quoi je parle", "Le support, le genre, une mesure. Une phrase."],
               ["2 · Où et quand", "Un lieu, une époque. Deux détails, pas trois."],
               ["3 · Qui, et ce qu'il veut", "Le personnage principal et son désir."],
               ["4 · Ce qui complique", "Un seul obstacle. Jamais trois."],
               ["5 · Je m'arrête", "Au moment du choix. « Je ne vous dis pas la fin. »"]],
              cle=1,
              notes="Insister sur la quatrième rangée : un seul obstacle. Raconter trois "
                    "complications, c'est raconter le livre. Faire écrire au groupe, pour "
                    "leur propre œuvre, la phrase du temps 4 — c'est la plus difficile.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("L'histoire se passe dans un village au bord de la mer.", "vrai"),
        ("La femme revient au village après cinq ans.", "faux — après vingt ans"),
        ("Elle revient pour vendre la maison de sa mère.", "vrai"),
        ("Elle a l'intention de rester tout l'été.", "faux — elle veut repartir le jour même"),
        ("Elle trouve une boîte de lettres dans la maison.", "vrai"),
        ("Mai raconte l'histoire au passé composé.", "faux — au présent"),
        ("Mai dit de qui viennent les lettres.", "faux — elle refuse"),
        ("Karim conseille de s'arrêter au moment du choix.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice `t1a` du module interactif. Faire justifier chaque « faux » "
             "par la réplique. La sixième prépare la séance B2, la septième la séance B4.")

    d.piege("Commencer par un détail",
            "C'était l'hiver, il y avait beaucoup de neige, et…",
            "C'est un roman. Une femme revient au village après vingt ans.",
            "Tant que la personne en face ne sait pas de quoi vous parlez, tous les "
            "détails tombent à côté : elle les entend sans pouvoir les ranger nulle "
            "part. Le décor vient au temps 2, jamais au temps 1.",
            notes="Faire l'exercice à l'envers : donner au groupe un détail seul — « il "
                  "pleuvait ce jour-là » — et demander ce qu'ils en font. Rien. Puis "
                  "donner la première phrase avant, et redonner le détail.")

    d.billet(
        "Écrivez les temps 1, 2 et 3 de votre présentation. Une phrase chacun.",
        exemples=[
            "Temps 2 : deux détails seulement — un lieu, une époque.",
            "Temps 3 : le personnage principal et ce qu'il veut, en une seule phrase.",
        ],
        notes="Ramasser les billets et les relire avant B2 : les temps 3 mal faits — "
              "« c'est l'histoire d'une famille » sans désir — donnent la matière de la "
              "reprise du début de séance suivante.")

    return d.save(dossier)
