# -*- coding: utf-8 -*-
"""D2 · Du sel, des serviettes — et il n'en reste plus.
Bloc D « Défi 3 · Comprendre le préposé » · couleur ambre · 75 min.
Source : exercices `t3partitif` et `t3plus`, mini-leçons du même nom.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-restaurant/images/')


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Du sel, des serviettes — et il n'en reste plus",
        chapeau="Deux points de langue pour le même moment : demander un peu "
                "de quelque chose, et comprendre la réponse quand le "
                "casse-croûte n'en a plus.",
        duree='75 minutes')

    d.titre(notes="Dernière séance de contenu du module. Elle réunit les deux points de "
                  "langue du défi 3 : le déterminant partitif et la négation « ne… plus ».")

    d.objectifs([
        "demander un condiment avec du, de la, de l' ou des ;",
        "employer « de » seul après une quantité ;",
        "comprendre « il n'y a plus de » et « il n'en reste plus » ;",
        "répondre quand ce qu'on voulait n'est plus disponible.",
    ])

    d.declencheur(
        'Observation', "Comment on demande ça ?",
        image=IMG + 'sachets-condiments.jpg',
        pistes=[
            "Comment s'appellent ces petits sachets ?",
            "Est-ce qu'on dit « un sel » ou « du sel » ?",
            "Et pour la moutarde, on dit quoi ?",
            "Et s'il en faut deux, on dit comment ?",
        ],
        notes="Laisser le groupe hésiter entre « un sel » et « du sel ». L'hésitation "
              "est exactement le point de langue de la séance.")

    d.regle("Le sel ne se compte pas",
            "« Est-ce que je peux avoir du sel ? »",
            precision="On ne dit pas combien parce qu'on ne le sait pas : un "
                      "peu, ce qu'il faut. Le français a un petit mot exprès "
                      "pour ça, et il change selon le nom qui suit — comme au "
                      "bloc B.",
            notes="Diapo à photographier. Faire le lien explicite avec « au, à la, aux » "
                  "de la séance B3 : c'est la même mécanique, avec un autre petit mot.")

    d.tableau('Analyse', "Quatre formes, quatre cas",
              ['Le mot qui suit est…', 'On dit', 'Exemple'],
              [["masculin", "du", "du sel, du ketchup"],
               ["féminin", "de la", "de la moutarde"],
               ["une voyelle", "de l'", "de l'eau"],
               ["au pluriel", "des", "des serviettes, des ustensiles"]],
              cle=1,
              note="C'est la même règle qu'au bloc B : on regarde le mot qui suit.",
              notes="Diapo à photographier. Faire recopier le tableau sous celui de la "
                    "séance B3 : les deux se lisent ensemble.")

    d.regle("Dès qu'on dit la quantité, il ne reste que « de »",
            "un peu de sel  ·  deux serviettes  ·  un sachet de ketchup",
            precision="« Un peu du sel » ne se dit pas. Après un nombre, après "
                      "« un peu », après « un sachet », on garde seulement "
                      "« de » — ou rien du tout quand le nombre suffit.",
            notes="Diapo à photographier. Faire produire trois exemples au tableau par "
                  "trois élèves différents.")

    d.pratique('Écriture', "Du, de la, de l' ou des ?",
               "Complétez la demande.", [
        ("Est-ce que je peux avoir ___ sel ?", "du"),
        ("Je voudrais ___ moutarde sur mon sandwich.", "de la"),
        ("Il me faut ___ serviettes de table.", "des"),
        ("Est-ce qu'il y a ___ eau quelque part ?", "de l'"),
        ("Le café est amer : je vais mettre ___ sucre.", "du"),
    ], corrige=True,
       notes="Faire écrire dans le cahier avant de corriger. Demander à chaque fois quel "
             "mot a décidé de la forme.")

    d.regle("Quand le casse-croûte n'en a plus",
            "« Il n'y a plus de soupe. »  ·  « Il n'en reste plus. »",
            precision="« Ne… plus » veut dire qu'il y en avait et qu'il n'y en "
                      "a maintenant plus — pas qu'on n'en fait jamais. Après "
                      "« plus », toujours « de » : plus de frites, plus d'eau. "
                      "Jamais « plus des frites ».",
            notes="Diapo à photographier. Ça arrive tous les jours après une heure et "
                  "demie : la phrase doit se reconnaître à l'oreille du premier coup.")

    d.tableau('Analyse', "Ce qu'on répond",
              ['On entend', 'On répond'],
              [["Il n'y a plus de soupe.", "Ce n'est pas grave."],
               ["Il n'en reste plus.", "Qu'est-ce que vous avez d'autre ?"],
               ["Plus de frites après trois heures.", "Alors je vais prendre autre chose."]],
              cle=1,
              note="La deuxième réponse est la plus utile : elle relance le préposé.",
              notes="Diapo à photographier. C'est lui qui connaît la cuisine : lui poser "
                    "la question fait gagner du temps à tout le monde.")

    d.piege("Comprendre le contraire",
            "« y'en a plus » entendu comme « il y en a beaucoup »",
            "il n'y en a plus du tout",
            "À l'oral, le « ne » tombe presque toujours : on entend « y'en a plus ». "
            "Le mot « plus » veut alors dire zéro, pas beaucoup. C'est le ton et la "
            "situation qui le disent — et si on hésite, on demande.",
            notes="Faire écouter les deux phrases : « il y en a plus » (beaucoup, le s "
                  "se prononce) et « il n'y en a plus » (zéro). La différence est fine ; "
                  "le contexte du comptoir tranche presque toujours.")

    d.billet(
        "Écrivez quatre demandes de condiments et deux réponses du préposé.",
        exemples=[
            "Une avec du, une avec de la, une avec de l', une avec des.",
            "Et deux phrases avec « il n'y a plus de ».",
        ],
        notes="Fin du bloc D. Ces phrases seront réemployées telles quelles dans le jeu "
              "de rôle du bloc E.")

    return d.save(dossier)
