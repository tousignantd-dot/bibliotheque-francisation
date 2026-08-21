# -*- coding: utf-8 -*-
"""A2 · Le son IN et le son AN.
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prPhon` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Le son IN et le son AN',
        chapeau="Au guichet, presque tout ce qu'on entend est un nombre. "
                "Deux sons du nez s'y ressemblent, et les confondre fait "
                "payer le mauvais prix.",
        duree='75 minutes')

    d.titre(notes="Séance de phonétique, placée tôt parce que tout le reste du module "
                  "repose sur des chiffres entendus. Commencer en disant « vingt » et "
                  "« vent » l'un après l'autre, sans rien expliquer, et demander au "
                  "groupe si c'est le même mot.")

    d.objectifs([
        "entendre la différence entre le son IN et le son AN ;",
        "reconnaître les deux sons dans les nombres et les jours ;",
        "savoir que EN se prononce comme AN ;",
        "dire correctement les nombres du guichet : vingt-cinq, soixante-quinze, cent vingt.",
    ])

    d.regle("Deux mots repères, et rien d'autre",
            "LUNDI pour le son IN · TRENTE pour le son AN",
            precision="Devant un nombre nouveau, dites-le à côté de l'un des "
                      "deux et laissez l'air passer par le nez. La bouche est "
                      "étirée sur les côtés pour IN, bien ouverte pour AN. "
                      "Mettez la main devant la bouche : pour AN, l'air sort "
                      "plus large.",
            notes="Diapositive à photographier. Faire répéter les deux mots repères en "
                  "chœur, puis un par un. Ne jamais écrire de symboles phonétiques : le "
                  "groupe travaille avec des mots, pas avec un alphabet.")

    d.tableau('Analyse', "Le son IN — la bouche étirée",
              ["On écrit", "Exemples"],
              [["un", "un, lundi, brun"],
               ["in", "matin, quinze, vingt"],
               ["ain / ein", "main, plein"],
               ["ien", "combien, bien, rien"],
               ["oin", "moins, loin"]],
              cle=0,
              note="Cinq écritures différentes, un seul son.",
              notes="Diapositive à photographier. Faire lire une écriture à la fois. "
                    "Insister sur « combien » et « moins », les deux mots du guichet.")

    d.tableau('Analyse', "Le son AN — la bouche ouverte",
              ["On écrit", "Exemples"],
              [["an", "dimanche, quarante, an"],
               ["en", "trente, cent, argent"],
               ["am / em", "comptant, ensemble"]],
              cle=0,
              note="EN et AN donnent exactement le même son.",
              notes="Diapositive à photographier. C'est la découverte qui surprend le "
                    "plus : « trente » et « dimanche » riment. Le faire entendre plutôt "
                    "que l'affirmer.")

    d.piege('Prononciation',
            "« vent-cinq dollars »",
            "« vingt-cinq dollars »",
            "C'est le piège le plus coûteux du module : au guichet, un nombre mal "
            "dit fait payer le mauvais prix ou fait acheter le mauvais titre. "
            "Étirez bien la bouche pour « vingt », comme pour sourire.",
            notes="Demander qui a déjà eu ce problème. Dédramatiser : c'est une "
                  "difficulté d'oreille, pas d'intelligence, et elle se corrige par la "
                  "répétition.")

    d.tableau('Analyse', "Les nombres où les deux sons se suivent",
              ["Le nombre", "Ce qu'on entend"],
              [["vingt-cinq", "IN, puis IN"],
               ["soixante-quinze", "AN, puis IN"],
               ["cent vingt", "AN, puis IN"],
               ["trente-cinq", "AN, puis IN"]],
              cle=1,
              note="Dites-les lentement, en deux morceaux.",
              notes="Ce sont les quatre nombres les plus fréquents du module : "
                    "« trois dollars soixante-quinze », « trente-cinq dollars », "
                    "« cent vingt minutes ». Les faire répéter jusqu'à ce qu'ils "
                    "sortent d'un seul souffle.")

    d.pratique('Écoute', "IN comme LUNDI, ou AN comme TRENTE ?",
               "Écoutez chaque mot et dites quel son vous entendez.", [
        ("lundi", "IN"),
        ("trente", "AN"),
        ("un passage", "IN"),
        ("comptant", "AN"),
        ("combien", "IN"),
        ("dimanche", "AN"),
        ("moins cher", "IN"),
        ("cent dix dollars", "AN"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 2 du module, mot pour mot. Le faire d'abord à l'oral, "
             "livre fermé, puis ouvrir l'activité interactive : les élèves y "
             "réentendront chaque mot autant de fois qu'ils veulent.")

    d.pratique('Répétition', "Six phrases du comptoir",
               "Écoutez, puis répétez en marquant les deux sons.", [
        ("Un passage, s'il vous plaît.", "IN deux fois"),
        ("Trente-cinq dollars.", "AN une fois"),
        ("C'est combien ?", "IN une fois"),
        ("Du lundi au dimanche.", "IN puis AN"),
        ("Cent dix dollars pour le mois.", "AN deux fois"),
        ("Trois dollars soixante-quinze.", "AN puis IN"),
    ], corrige=True,
       notes="Répétition en chœur, puis en rangées, puis individuellement. Corriger la "
             "bouche plutôt que le son : « ouvre davantage », « étire les lèvres ».")

    d.billet(
        "Écrivez trois nombres avec le son IN et trois nombres avec le son AN.",
        exemples=[
            "Son IN : vingt, quinze, ___",
            "Son AN : trente, cent, ___",
        ],
        notes="Devoir court. Vérifier au ramassage que personne n'a mis « trente » dans "
              "la colonne IN : c'est l'erreur qui reste après la séance.")

    return d.save(dossier)
