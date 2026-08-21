# -*- coding: utf-8 -*-
"""B3 · Un sandwich au poulet, une soupe aux légumes.
Bloc B « Défi 1 · Lire le menu » · couleur ambre · 75 min.
Source : exercice `t1au`, mini-leçon `t1au`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Au poulet, à la tomate, aux légumes',
        chapeau="Le nom du plat ne dit jamais ce qu'il y a dedans. C'est le "
                "petit mot d'après qui le dit — et il ne dépend que du mot "
                "qui le suit.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire et d'écriture. Le point de langue sert deux fois "
                  "dans le module : pour lire le menu, et pour commander sans se tromper "
                  "de plat.")

    d.objectifs([
        "comprendre ce que « au », « à la » et « aux » ajoutent au nom du plat ;",
        "choisir la forme juste selon le mot qui suit ;",
        "écrire une commande sans faute de déterminant ;",
        "employer « sans » pour retirer un ingrédient.",
    ])

    d.regle("Le petit mot regarde ce qui vient après lui",
            "un sandwich au poulet  ·  une soupe aux légumes",
            precision="Le nom du plat — sandwich, soupe, salade — n'a aucun "
                      "mot à dire. C'est le mot qui suit le petit mot qui "
                      "décide : masculin, féminin, voyelle ou pluriel.",
            notes="Diapo à photographier. C'est la règle entière de la séance. La faire "
                  "redire dans ses mots par deux élèves avant d'aller plus loin.")

    d.tableau('Analyse', "Quatre formes, quatre cas",
              ['Le mot qui suit est…', 'On écrit', 'Exemple'],
              [["masculin", "au", "un sandwich au poulet"],
               ["féminin", "à la", "une soupe à la tomate"],
               ["une voyelle", "à l'", "une salade à l'oignon"],
               ["au pluriel", "aux", "une soupe aux légumes"]],
              cle=1,
              note="« Au » est « à » et « le » collés ensemble : « à le » n'existe pas.",
              notes="Diapo à photographier. Faire recopier le tableau dans le cahier : "
                    "c'est la référence de tout le bloc B.")

    d.tableau('Analyse', "Le même contenu, trois plats",
              ['Le plat', 'Avec du poulet', 'Avec des légumes'],
              [["un sandwich", "au poulet", "aux légumes"],
               ["une soupe", "au poulet", "aux légumes"],
               ["une salade", "au poulet", "aux légumes"]],
              cle=0,
              note="Le plat change de genre, le petit mot ne change pas.",
              notes="Diapo à photographier. C'est la démonstration la plus efficace de "
                    "la règle : la colonne de gauche change, les deux autres non.")

    d.pratique('Écriture', "Au, à la, à l' ou aux ?",
               "Complétez la commande.", [
        ("Un sandwich ___ poulet, s'il vous plaît.", "au"),
        ("Une soupe ___ légumes, format moyen.", "aux"),
        ("Un sandwich ___ œufs et un jus de pomme.", "aux"),
        ("Une soupe ___ tomate, c'est la soupe du jour.", "à la"),
        ("Une salade ___ oignon, s'il vous plaît.", "à l'"),
        ("Un muffin ___ bleuets, pour emporter.", "aux"),
    ], corrige=True,
       notes="Faire écrire dans le cahier avant de corriger. Demander à chaque fois "
             "quel mot a décidé de la forme.")

    d.regle("Pour retirer quelque chose : sans",
            "« Un sandwich sans mayonnaise, s'il vous plaît. »",
            precision="Après « sans », le nom reste tout nu : ni du, ni de la, "
                      "ni des. C'est la phrase à connaître pour une allergie, "
                      "un goût ou une habitude alimentaire.",
            notes="Diapo à photographier. Faire dire la phrase avec trois ingrédients "
                  "différents. Beaucoup d'élèves ont une restriction alimentaire et "
                  "n'osent pas la dire : c'est le moment de leur donner la formule.")

    d.piege("Regarder le plat au lieu du contenu",
            "une soupe à la légumes",
            "une soupe aux légumes",
            "L'élève voit « soupe », qui est féminin, et écrit « à la ». Mais le petit "
            "mot ne regarde jamais en arrière : il regarde le mot qui vient juste "
            "après lui. Ici, « légumes » est au pluriel, donc « aux ».",
            notes="Faire souligner au crayon le mot qui suit, avant d'écrire. Deux "
                  "secondes de plus, et l'erreur disparaît.")

    d.pratique('Production orale', "Commandez et précisez",
               "Une phrase complète, avec le petit mot juste.", [
        ("un sandwich, du jambon", "Un sandwich au jambon, s'il vous plaît."),
        ("une soupe, des légumes", "Une soupe aux légumes, s'il vous plaît."),
        ("une salade, du poulet", "Une salade au poulet, s'il vous plaît."),
        ("un sandwich, pas de mayonnaise", "Un sandwich sans mayonnaise, s'il vous plaît."),
    ], corrige=True,
       notes="En paires, debout. Un élève donne les deux mots, l'autre fait la phrase. "
             "On change de rôle après deux items.")

    d.billet(
        "Écrivez quatre plats avec leur contenu.",
        exemples=[
            "Un de chaque forme : au, à la, à l', aux.",
            "Et un cinquième avec « sans ».",
        ],
        notes="Devoir court. Il prépare la séance B4, où l'on apprendra à montrer un "
              "plat du doigt quand on ne connaît pas encore son nom.")

    return d.save(dossier)
