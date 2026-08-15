# -*- coding: utf-8 -*-
"""C2 · Le, la, les : général ou précis ?
Bloc C · couleur ambre (écriture) · 60 min.
Source : exercice `t2determinant` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Général ou précis ?',
        chapeau="« J'aime les vieux objets » et « j'aime les vieux objets que tu "
                "répares ». Le même déterminant, et deux sens très différents : tous, "
                "ou ceux-là seulement.",
        duree='60 minutes')

    d.titre(notes="Écrire les deux phrases du chapeau au tableau et demander la "
                  "différence. Le groupe la sentira sans pouvoir la nommer : c'est la "
                  "séance.")

    d.objectifs([
        "distinguer un emploi général d'un emploi précis ;",
        "reconnaître ce qui rend un groupe du nom précis ;",
        "comprendre pourquoi une publicité emploie souvent le général ;",
        "choisir le bon sens à la lecture.",
    ])

    d.regle('La règle',
            "Le, la, les peuvent désigner tout un ensemble, ou des choses précises.",
            precision="« J'aime les objets bien faits » : tous les objets bien faits, en "
                      "général. « J'aime les objets que ton grand-père a fabriqués » : "
                      "ceux-là précisément. C'est ce qui suit qui décide.",
            notes="Écrire la règle au tableau. Le critère est simple : y a-t-il une "
                  "précision après le nom ?")

    d.tableau('Analyse', "Ce qui rend un groupe précis",
              ['La précision', 'Un exemple'],
              [["une phrase avec « que »", "les objets que tu répares"],
               ["une phrase avec « qui »", "les bénévoles qui arrivent tôt"],
               ["un complément avec « de »", "la capsule de Solange"],
               ["un moment ou un lieu", "le cours du vendredi soir"]],
              cle=0, props=[0.35, 0.65],
              note="Sans aucune de ces quatre précisions, le groupe reste général.",
              notes="Relier à « qui » et « que », vus aux modules 3 et 4. C'est le même "
                    "mécanisme, employé ici pour préciser.")

    d.cartes('Analyse', "Pourquoi la publicité emploie le général", [
        ("Pour parler à plus de gens",
         "« On répare les petits appareils » vise tout le monde. « On répare les petits "
         "appareils de la marque X » réduit le public."),
        ("Pour poser une valeur",
         "« Je déteste le gaspillage » nomme une idée générale. C'est ainsi qu'on porte "
         "une valeur, vue en A4."),
        ("Pour créer une habitude",
         "« On écoute la radio le matin » décrit une routine, pas un moment précis. "
         "C'est très employé en publicité."),
        ("Le précis vient ensuite",
         "L'affiche commence par le général — « tout se répare » — et donne ensuite le "
         "précis : la date, l'adresse, l'heure."),
    ], notes="La quatrième carte explique la structure d'une affiche : du général au "
             "précis. Le faire vérifier sur les deux affiches de C1.")

    d.pratique('Pratique · 1 de 4', "Général ou précis ?",
               "Y a-t-il une précision après le nom ?", [
        ("J'aime les objets bien faits.", "général — tous"),
        ("J'aime les objets que ton grand-père a fabriqués.", "précis — ceux-là"),
        ("On écoute la radio le matin.", "général — une habitude"),
        ("On écoute la capsule que Solange a enregistrée.", "précis"),
        ("Je déteste le gaspillage.", "général"),
        ("Je prends le cours de couture du vendredi soir.", "précis"),
    ], corrige=True,
       notes="Faire souligner la précision quand il y en a une. Là où rien n'est "
             "souligné, c'est général.")

    d.piege("Le piège du déterminant seul",
            "« Les » veut toujours dire tous.",
            "C'est ce qui suit le nom qui décide.",
            "Le déterminant est le même dans les deux cas : c'est la suite de la phrase "
            "qui dit s'il s'agit de tous ou de quelques-uns. Regardez toujours après le "
            "nom avant de conclure.",
            notes="Faire relire les six phrases de l'exercice en cachant tout ce qui "
                  "suit le nom. Elles deviennent toutes générales.")

    d.piege("Le piège de la publicité trompeuse",
            "« Les meilleurs prix de la ville » — tous les prix sont les meilleurs.",
            "Cherchez la précision cachée en petits caractères.",
            "Une publicité emploie le général pour paraître large, puis ajoute une "
            "précision en petits caractères : « sur les articles sélectionnés », « pour "
            "les nouveaux clients ». Le général attire, le précis limite.",
            notes="Point d'analyse critique. Apporter une vraie publicité commerciale : "
                  "la précision est presque toujours là, en bas.")

    d.pratique('Pratique · 2 de 4', "Trouvez la précision",
               "Qu'est-ce qui limite le groupe du nom ?", [
        ("les objets que tu répares", "la phrase avec « que »"),
        ("la capsule de Solange", "le complément avec « de »"),
        ("le cours du vendredi soir", "le moment"),
        ("les bénévoles qui arrivent tôt", "la phrase avec « qui »"),
        ("les ateliers de la bibliothèque Saint-Charles", "le complément avec « de »"),
    ], corrige=True,
       notes="Cinq façons de préciser. Faire remarquer qu'elles se combinent souvent dans "
             "une vraie affiche.")

    d.pratique('Pratique · 3 de 4', "Rendez la phrase précise",
               "Ajoutez une précision après le nom.", [
        ("J'aime les vieux objets.", "J'aime les vieux objets que mon père a gardés."),
        ("On répare les appareils.", "On répare les appareils qu'on nous apporte."),
        ("Je prends le cours.", "Je prends le cours du vendredi soir."),
        ("Écoutez la capsule.", "Écoutez la capsule de Radio Limoilou."),
    ], corrige=True,
       notes="Accepter toute précision correcte. Vérifier une seule chose : est-ce "
             "qu'elle limite vraiment le groupe ?")

    d.pratique('Pratique · 4 de 4', "Dans les affiches du module",
               "Général ou précis ?", [
        ("« Rien ne se jette, tout se répare. »", "général — une valeur"),
        ("« Apportez votre grille-pain, votre lampe ou votre chaise bancale. »",
         "précis — ces objets-là"),
        ("« La bibliothèque Saint-Charles ouvre ses ateliers. »", "précis — cette bibliothèque"),
        ("« Nos mécaniciens bénévoles vous montreront à régler vos freins. »",
         "précis — vos freins à vous"),
    ], corrige=True,
       notes="Faire remarquer que le slogan est le seul général. C'est ce qui lui permet "
             "de parler à tout le monde.")

    d.billet(
        "Écrivez quatre phrases : deux générales, deux précises.",
        exemples=[
            "Sur le même sujet, pour que la différence se voie.",
            "Soulignez la précision dans les deux dernières.",
        ],
        notes="Corriger la présence et la nature de la précision. C'est le savoir de la "
              "séance.")

    return d.save(dossier)
