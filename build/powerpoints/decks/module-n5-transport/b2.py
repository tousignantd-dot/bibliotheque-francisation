# -*- coding: utf-8 -*-
"""B2 · Où, exactement
Bloc B « Défi 1 · Ce qui bloque la route » · couleur acier · 75 min.
Source : exercice `t1ou` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="Où, exactement",
        chapeau="« Il y a un accident sur la 40 » ne dit presque rien : "
                "l'autoroute traverse toute l'île. Le bulletin donne toujours "
                "deux repères, jamais un seul — et c'est le deuxième que tout "
                "le monde manque.",
        duree='75 minutes')

    d.titre(notes="Séance de prépositions, mais pas une séance de grammaire abstraite : "
                  "chaque préposition sert à situer une entrave. Ouvrir en disant « il y "
                  "a un accident sur la 40 » et en demandant au groupe si cela suffit "
                  "pour décider. Non — et c'est parti.")

    d.objectifs([
        "employer « sur » pour une route, un pont, un boulevard ;",
        "situer un point précis avec « à la hauteur de » ;",
        "situer une portion de route avec « entre… et… » ;",
        "dire le sens avec « en direction de » et « dans les deux sens ».",
    ], notes="Le quatrième objectif est celui qui a le plus de conséquences pratiques : "
             "une entrave dans l'autre sens ne concerne pas l'élève. Beaucoup de détours "
             "inutiles viennent de cet oubli.")

    d.regle("Deux repères, toujours",
            "La route d'abord, puis la précision : sur la 40, à la hauteur de "
            "la sortie Côte-de-Liesse.",
            precision="Un seul repère ne fait décider personne. C'est vrai du "
                      "bulletin, et c'est vrai de vous quand vous l'expliquez.",
            notes="Diapositive à photographier. La reprendre en E1 : c'est le premier "
                  "critère du jeu de rôle, et le collègue redemande tant qu'il n'a pas "
                  "les deux repères.")

    d.tableau('Les prépositions', "Chacune dit autre chose",
              ['On dit', 'Cela situe'],
              [["sur la 40", "la route"],
               ["à la hauteur de la sortie", "un point précis"],
               ["entre la 15 et Marcel-Laurin", "une portion"],
               ["en direction ouest", "le sens"],
               ["dans les deux sens", "les deux à la fois"]],
              cle=1,
              notes="Faire trouver la colonne de droite par le groupe. Insister sur la "
                    "différence entre un point et une portion : ce n'est pas la même "
                    "décision.")

    d.cartes("Une exception, et une contraction", "Deux détails qui trompent", [
        ("Sur le pont, dans le tunnel",
         "Un tunnel est fermé de tous les côtés : « dans »."),
        ("À la hauteur de la sortie",
         "Devant un nom féminin : « de la »."),
        ("À la hauteur du pont",
         "Devant un nom masculin : « du »."),
        ("En direction de Montréal",
         "Devant une ville : « de », sans article."),
    ], notes="La contraction « de la » / « du » est la seule difficulté grammaticale de "
             "la séance. La traiter vite : c'est la règle ordinaire, elle n'a rien de "
             "propre à la route.")

    d.piege("Dire « dans l'autoroute »",
            "Il y a un accident dans la 40.",
            "Il y a un accident sur la 40.",
            "On roule sur une autoroute, un boulevard, un pont, une rue. « Dans » "
            "est réservé au tunnel, et à rien d'autre dans ce vocabulaire.",
            notes="Une des rares règles du module qui n'a aucune exception. La faire "
                  "répéter avec cinq noms de routes réelles du quartier.")

    d.piege("Oublier de dire le sens",
            "Il y a un carambolage sur la 40.",
            "Il y a un carambolage sur la 40, en direction ouest.",
            "Sans le sens, l'autre personne va peut-être changer de chemin pour "
            "une entrave qui ne la touche pas. Le sens fait la moitié de "
            "l'information.",
            notes="C'est l'oubli le plus fréquent dans les productions du module. Le "
                  "signaler ici évite de le corriger dix fois en E1.")

    d.pratique('Prépositions', "Complétez l'annonce",
               "Choisissez la préposition qui convient.", [
        ("Un accident ___ l'autoroute 40 bloque deux voies.", "sur"),
        ("L'entrave se trouve ___ la sortie Côte-de-Liesse.", "à la hauteur de"),
        ("Vingt minutes de plus ___ la 15 ___ Marcel-Laurin.", "entre … et"),
        ("La circulation est dense ___ Montréal.", "en direction de"),
        ("Le pont est fermé ___ jusqu'à neuf heures.", "dans les deux sens"),
        ("Tout est ouvert ___ le pont-tunnel.", "dans"),
    ], corrige=True,
       notes="Les six mêmes phrases sont dans l'exercice `t1ou` de l'activité "
             "interactive. Faire justifier la dernière : c'est l'exception du tunnel.")

    d.billet(
        "Situez une entrave sur votre propre trajet, avec deux repères et le sens.",
        exemples=[
            "Sur le boulevard X, à la hauteur de la rue Y, en direction du nord.",
            "Si vous prenez l'autobus, dites la ligne et l'arrêt.",
        ],
        notes="Ramasser les billets. Ceux à qui il manque un repère ou le sens sont "
              "exactement ceux qu'il faudra suivre en E1.")

    return d.save(dossier)
