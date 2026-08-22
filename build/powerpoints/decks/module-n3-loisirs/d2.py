# -*- coding: utf-8 -*-
"""D2 · Pelez, coupez, ajoutez : les consignes et les quantités.
Bloc D « Défi 3 · La cuisine collective » · ambre · 75 min.
Source du module : exercices `t3imper`, `t3quant` et `t3abrev`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Pelez, coupez, ajoutez",
        chapeau="Une recette ne raconte rien : elle demande de faire. D'où "
                "des verbes sans sujet devant, des quantités qu'on ne compte "
                "pas, et des mots écrits en abrégé. Trois points de langue, "
                "et la feuille se lit d'un trait.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 3, et la plus dense du module. Trois points "
                  "de langue : ne pas tout expliquer, faire faire. La recette du "
                  "dialogue de D1 sert de support du début à la fin.")

    d.objectifs([
        "employer la forme en -ez des consignes de recette ;",
        "choisir entre du, de la, de l' et des ;",
        "employer « de » après une quantité et après une négation ;",
        "lire les abréviations d'une recette : ml, c. à soupe, c. à thé.",
    ])

    d.regle("Les consignes d'une recette",
            "« Pelez six pommes de terre. » — aucun sujet devant le verbe.",
            precision="On prend le verbe avec « vous » et on enlève le mot « vous ». "
                      "Pelez, coupez, égouttez, écrasez, ajoutez, mélangez. Trois "
                      "verbes irréguliers reviennent tout le temps : faites, mettez, "
                      "soyez.",
            notes="Diapo à photographier. « Faites », pas « faisez » : c'est le seul "
                  "vraiment traître, et il est dans la recette du dialogue.")

    d.tableau('Analyse · 1 de 2', "Les six verbes de la recette",
              ["Le verbe", "Avec vous — la recette écrite", "Avec tu — entre amis"],
              [["peler", "Pelez les pommes de terre.", "Pèle les pommes de terre."],
               ["couper", "Coupez-les en morceaux.", "Coupe-les en morceaux."],
               ["ajouter", "Ajoutez 60 ml de lait.", "Ajoute 60 ml de lait."],
               ["mélanger", "Mélangez jusqu'au bout.", "Mélange jusqu'au bout."],
               ["faire", "Faites bouillir vingt minutes.", "Fais bouillir vingt minutes."]],
              cle=1,
              note="À l'écrit, toujours la colonne du milieu. Et avec « tu », pas de s aux verbes en -er.",
              notes="Diapo à photographier. Le « pèle » avec accent grave surprend : le "
                    "signaler sans en faire une règle, c'est du vocabulaire à ce stade.")

    d.pratique('Écriture · 1 de 3', "Écrivez la consigne",
               "Complétez avec le verbe entre parenthèses, à la forme de la recette.", [
        ("___ six pommes de terre. (peler)", "Pelez"),
        ("___ -les en gros morceaux. (couper)", "Coupez"),
        ("___ bouillir vingt minutes. (faire)", "Faites"),
        ("___ 60 ml de lait et une cuillère à soupe de beurre. (ajouter)", "Ajoutez"),
        ("___ jusqu'à ce que ce soit lisse. (mélanger)", "Mélangez"),
        ("___ le chaudron sur le rond arrière. (mettre)", "Mettez"),
    ], corrige=True,
       notes="C'est l'exercice t3imper du module. Faire lire les six consignes à la "
             "suite, à voix haute : la voix descend à la fin de chacune, ce n'est pas "
             "une question.")

    d.regle("Ce qui se compte, ce qui ne se compte pas",
            "du lait · de la crème · de l'eau · des pommes de terre",
            precision="On ne compte pas le lait : on en prend une partie, d'où « du ». "
                      "On compterait les pommes de terre une par une, d'où « des ». "
                      "Mais après une quantité — 60 ml, un peu, beaucoup — il ne reste "
                      "que « de » : un peu DE sel, jamais « un peu du sel ».",
            notes="Diapo à photographier. La dernière phrase est la faute la plus "
                  "fréquente du niveau, et la plus facile à corriger : après une "
                  "quantité, « de », point.")

    d.tableau('Analyse · 2 de 2', "Le petit mot devant l'aliment",
              ["Le cas", "Ce qu'on met", "Exemple"],
              [["masculin, une partie", "du", "du lait, du sel"],
               ["féminin, une partie", "de la", "de la crème"],
               ["devant une voyelle", "de l'", "de l'eau, de l'huile"],
               ["ça se compte", "des", "des oignons"],
               ["après une quantité", "de", "un peu de sel"],
               ["à la forme négative", "pas de", "pas de maïs"]],
              cle=1,
              notes="Diapo à photographier. Les deux dernières lignes valent pour tous "
                    "les genres : du, de la et des y deviennent tous « de ». Faire "
                    "couvrir la colonne du milieu et faire retrouver le petit mot à "
                    "partir de l'exemple.")

    d.pratique('Écriture · 2 de 3', "Du, de la, des, ou de ?",
               "Complétez avec « du », « de la », « de l' », « des », « de » ou « d' ».", [
        ("Ajoutez ___ lait et une cuillère à soupe de beurre.", "du"),
        ("La recette demande ___ crème, mais on peut la remplacer.", "de la"),
        ("Pelez ___ pommes de terre et deux oignons.", "des"),
        ("Mettez un peu ___ sel, pas plus.", "de"),
        ("Camila ne veut ___ maïs dans sa portion.", "pas de"),
        ("Faites bouillir beaucoup ___ eau dans le gros chaudron.", "d'"),
    ], corrige=True,
       notes="C'est l'exercice t3quant du module. Faire justifier chaque réponse par la "
             "ligne du tableau : c'est le raisonnement qui compte.")

    d.piege('Le piège', "un peu du sel, six des pommes de terre",
            "un peu de sel, six pommes de terre",
            "Deux fautes qui viennent du même réflexe : garder le petit mot alors qu'une "
            "quantité l'a déjà remplacé. Après « un peu », « beaucoup », « 60 ml » ou "
            "une tasse, il ne reste que « de ». Et devant un nombre, il ne reste rien "
            "du tout.",
            notes="Demander qui a déjà écrit l'un ou l'autre. C'est une faute d'excès de "
                  "zèle, pas d'ignorance : le dire, ça change la façon dont l'élève la "
                  "reçoit.")

    d.pratique('Écriture · 3 de 3', "Les abréviations de la recette",
               "Que veut dire chaque abréviation ?", [
        ("ml", "millilitre — une mesure de liquide"),
        ("c. à soupe", "cuillère à soupe — la grande, 15 ml"),
        ("c. à thé", "cuillère à thé — la petite, 5 ml"),
        ("g", "gramme — une mesure de poids"),
        ("min", "minute — le temps de cuisson"),
        ("1 t.", "une tasse — 250 ml"),
        ("4 pers.", "pour quatre personnes"),
    ], corrige=True,
       notes="C'est l'exercice t3abrev du module. Insister sur les deux cuillères : une "
             "c. à soupe vaut trois c. à thé, et confondre les deux triple la quantité. "
             "C'est l'erreur la plus coûteuse d'une recette.")

    d.billet(
        "Écrivez trois lignes d'une recette que vous connaissez.",
        exemples=[
            "Employez la forme en -ez : pelez, coupez, ajoutez, mélangez.",
            "Mettez au moins une quantité : un peu de…, 60 ml de…, une tasse de…",
        ],
        notes="Devoir court, et dernier écrit avant le bloc E. Ramasser : les deux "
              "points de langue de la séance s'y voient tout de suite.")

    return d.save(dossier)
