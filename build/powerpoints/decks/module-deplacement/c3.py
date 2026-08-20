# -*- coding: utf-8 -*-
"""C3 · Celui, celle, ceux.
Bloc C · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t2demo`, exercice `t2demo`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Celui, celle, ceux',
        chapeau="Douze autobus au terminus, et vous voulez en désigner un seul "
                "sans répéter le mot « autobus » à chaque phrase. C'est le "
                "travail des pronoms démonstratifs.",
        duree='75 minutes')

    d.titre(notes="Écrire au tableau : « Prenez l'autobus. L'autobus va vers Saint-Hubert. » "
                  "Demander ce qui cloche. La répétition saute aux yeux.")

    d.objectifs([
        "remplacer un nom par celui, celle, ceux ou celles ;",
        "accorder le pronom avec le nom remplacé, pas avec moi ;",
        "faire suivre le pronom de -là, qui, que ou de ;",
        "ne pas confondre celui et ce.",
    ])

    d.tableau('Analyse', "Quatre formes, selon le nom remplacé",
              ['Le nom remplacé', 'Le pronom', 'Exemple'],
              [["un autobus", "celui", "celui qui va vers le sud"],
               ["une colonne", "celle", "celle de gauche"],
               ["des cercles", "ceux", "ceux des correspondances"],
               ["des lignes", "celles", "celles qui vont vers la Rive-Sud"]],
              cle=0,
              note="C'est le nom remplacé qui décide de la forme — jamais la personne qui parle.",
              notes="Diapo centrale. Faire recopier. Insister sur la note : une femme qui "
                    "parle d'un autobus dit « celui ».")

    d.regle('Jamais tout seul',
            "Un pronom démonstratif est toujours suivi de quelque chose.",
            precision="Quatre suites possibles : <b>-là</b> (celui-là), <b>qui</b> (celui "
                      "qui va vers…), <b>que</b> (celui que je prends), <b>de</b> (celui de "
                      "7 h 51). « Celui » tout seul n'existe pas. Dans le doute, employez "
                      "<b>-là</b>.",
            notes="Le dire simplement : si vous ne savez pas quoi mettre après, mettez -là. "
                  "C'est toujours correct.")

    d.regle('Le lien avec qui et que',
            "Après le pronom, qui et que fonctionnent exactement comme ailleurs.",
            precision="« Celui <b>qui</b> va vers Gaétan-Boucher » : après qui, un verbe. "
                      "« Celui <b>que</b> je prends » : après que, un sujet. Rien de "
                      "nouveau à apprendre — c'est la même règle, appliquée après un autre "
                      "mot.",
            notes="Si le groupe a fait le module 11, faire le rappel explicite. Sinon, "
                  "donner la règle : verbe après › qui ; sujet après › que.")

    d.piege('Confondre celui et ce',
            "Celui autobus va vers Saint-Hubert.",
            "Cet autobus va vers Saint-Hubert. / Celui-là va vers Saint-Hubert.",
            "<b>ce</b>, <b>cet</b> et <b>cette</b> accompagnent un nom ; <b>celui</b> et "
            "<b>celle</b> le remplacent. On ne peut pas avoir les deux : soit le nom, soit "
            "le pronom, jamais les deux ensemble.",
            notes="Écrire les deux colonnes au tableau — les déterminants d'un côté, les "
                  "pronoms de l'autre — et les y laisser.")

    d.pratique('Pratique · 1 de 2', "Quelle forme ?",
               "Complétez avec celui, celle, ceux ou celles.", [
        ("Prenez ___ qui va vers Gaétan-Boucher. [un autobus]", "celui"),
        ("L'édifice est le troisième, ___ qui a une porte vitrée.", "celui"),
        ("— Le parc avec les jeux ? — ___, oui.", "Celui-là"),
        ("Cet horaire a deux colonnes : ___ de gauche est celle de la semaine.", "celle"),
        ("Les cercles noirs ? Ce sont ___ des correspondances.", "ceux"),
        ("Parmi toutes les lignes, ___ qui vont vers la Rive-Sud sont les plus rapides.", "celles"),
    ], corrige=True,
       notes="Faire nommer à voix haute le nom remplacé avant chaque réponse. C'est lui qui "
             "décide.")

    d.pratique('Pratique · 2 de 2', "Supprimez la répétition",
               "Récrivez la deuxième phrase avec un pronom démonstratif.", [
        ("Prenez l'autobus. L'autobus va vers Saint-Hubert.", "Prenez celui qui va vers Saint-Hubert."),
        ("Il y a deux sorties. La sortie de droite donne sur Victoria.", "Celle de droite donne sur Victoria."),
        ("Ne prends pas le départ de 7 h 42. Prends le départ de 7 h 51.", "Prends celui de 7 h 51."),
        ("Regarde les cercles. Les cercles noirs sont les correspondances.", "Ceux qui sont noirs sont les correspondances."),
    ], corrige=True, cols=1,
       notes="Plusieurs récritures sont acceptables. Ce qui compte est que la répétition "
             "disparaisse et que la forme s'accorde.")

    d.cartes('Où ça sert vraiment', "Trois situations du module", [
        ("Choisir un véhicule",
         "« Prenez celui qui va vers Gaétan-Boucher. » Douze autobus, un seul désigné, sans "
         "répéter le mot."),
        ("Choisir un bâtiment",
         "« C'est celui qui a une grande porte vitrée. » Le repère visuel remplace le "
         "numéro civique."),
        ("Choisir une heure",
         "« Prends celui de 7 h 51. » Deux départs, une seule bonne réponse."),
    ], notes="Faire produire une phrase de chaque type par le groupe, avec un exemple de "
             "leur propre trajet.")

    d.billet(
        "Écrivez quatre phrases avec celui, celle, ceux et celles.",
        exemples=[
            "Chacune doit désigner une chose parmi plusieurs.",
            "Soulignez, dans chaque phrase, le nom que le pronom remplace.",
        ],
        notes="Corriger surtout l'accord avec le nom remplacé, et la présence d'une suite "
              "après le pronom.")

    return d.save(dossier)
