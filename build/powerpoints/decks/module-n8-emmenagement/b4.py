# -*- coding: utf-8 -*-
"""B4 · Le pronom relatif après une préposition
Bloc B « Défi 1 · Ce qui est couvert » · couleur ambre · 75 min. Écriture.
Source du module : l'exercice `t1rel` et la mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Le pronom relatif après une préposition",
        chapeau="« La clause sur laquelle vous vous appuyez. » Sans ce "
                "pronom-là, il faut deux phrases, et un contrat en contient "
                "trois par paragraphe.",
        duree='75 minutes')

    d.titre(notes="Le programme du niveau 8 demande que l'adulte « emploie "
                  "différents pronoms relatifs ». C'est aussi ce qui rend un "
                  "contrat illisible quand on ne les maîtrise pas : la séance "
                  "sert donc à lire autant qu'à écrire.")

    d.objectifs([
        "former préposition + lequel, accordé au nom repris ;",
        "souder correctement avec « à » et avec « de » ;",
        "employer « dont » et connaître sa limite ;",
        "retrouver la préposition en refaisant la phrase simple.",
    ], notes="Le quatrième objectif est le seul repère fiable. Y revenir à "
             "chaque item de la pratique.")

    d.declencheur(
        'Pour commencer', "« La clause. Vous vous appuyez sur cette clause. » "
                          "Faites-en une seule phrase.",
        pistes=[
            "Quel petit mot faut-il garder de la deuxième phrase ?",
            "Et si c'était « je me fie à cette évaluation » ?",
            "Et « je vous parle de ce meuble » ?",
        ],
        notes="Les trois pistes donnent les trois cas de la séance : sur "
              "laquelle, à laquelle, dont. Laisser chercher : la difficulté "
              "n'est jamais le pronom, c'est de retrouver la préposition.")

    d.regle("Préposition + lequel, accordé au nom repris",
            "lequel · laquelle · lesquels · lesquelles — soudé avec à : auquel, à laquelle, auxquels — soudé avec de : duquel, de laquelle, desquels",
            precision="Avec toutes les autres — sur, dans, par, pour, avec, "
                      "sans, chez — il reste séparé : sur lequel, dans "
                      "laquelle, par lesquels.",
            notes="Diapositive à photographier. Signaler la bizarrerie "
                  "d'orthographe : « auquel » se soude, « à laquelle » non. "
                  "C'est de l'orthographe, pas de la grammaire.")

    d.tableau('Analyse', "La phrase simple, puis la relative",
              ['Les deux phrases séparées', 'La relative'],
              [["Vous vous appuyez sur cette clause.", "la clause sur laquelle vous vous appuyez"],
               ["Je me fie à cette évaluation.", "l'évaluation à laquelle je me fie"],
               ["Je ne renonce pas à ce point.", "le point auquel je ne renonce pas"],
               ["Je vous parle de ce meuble.", "le meuble dont je vous parle"],
               ["Je négocie avec cette personne.", "la personne avec qui je négocie"]],
              cle=0,
              note="La préposition ne change jamais : elle appartient au verbe.",
              notes="Diapositive à photographier. Faire dire la phrase simple "
                    "à voix haute avant chaque transformation : c'est la "
                    "méthode, et elle doit devenir un réflexe.")

    d.cartes('Attention', "Deux raccourcis, et la limite de « dont »", [
        ("Pour une personne", "après une préposition, on préfère « qui » : la personne à qui j'ai parlé."),
        ("Pour un lieu ou un moment", "« où » remplace tout : le jour où le camion est reparti."),
        ("« dont » remplace « de + quelque chose »", "une clause dont le sens est équivoque."),
        ("Sa limite", "jamais après une autre préposition : au bas duquel, jamais « au bas dont »."),
    ], cols=2,
       notes="La limite de « dont » est la seule chose vraiment difficile de "
             "la séance. La règle pratique : si le groupe qui précède "
             "contient déjà une préposition, c'est duquel.")

    d.piege('Attention',
            "« la clause dont je m'appuie »",
            "« la clause sur laquelle je m'appuie »",
            "S'appuyer se construit avec « sur », pas avec « de ». L'erreur "
            "vient de l'habitude de « dont », qui semble aller partout. Le "
            "seul remède est de refaire la phrase simple dans sa tête et "
            "d'écouter quelle préposition le verbe réclame.",
            notes="Faire chercher trois autres verbes qui piègent de la même "
                  "façon : penser à, se fier à, compter sur, tenir à.")

    d.pratique('Pratique', "Complétez avec le pronom relatif qui convient",
               "dont · auquel · à laquelle · sur laquelle · à qui · où", [
        ("C'est la clause ___ l'assureur s'appuie pour refuser.", "sur laquelle"),
        ("Le vaisselier ___ je vous parle appartenait à ma mère.", "dont"),
        ("Voici l'évaluation ___ je me fie.", "à laquelle"),
        ("L'ébéniste ___ j'ai montré la fente exerce rue Bonaventure.", "à qui"),
        ("C'est le seul point ___ je ne renonce pas.", "auquel"),
        ("Le jour ___ le camion est reparti, il pleuvait.", "où"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t1rel` du module, dans sa version projetée. "
             "Faire dire la phrase simple avant chaque réponse — sinon on "
             "devine, et deviner ne s'exporte pas.")

    d.billet(
        "Écris une phrase avec « sur laquelle » et une avec « dont », sur ton contrat.",
        exemples=[
            "Deux phrases séparées.",
            "Vérifie : peux-tu refaire la phrase simple derrière chacune ?",
        ],
        notes="Cinq minutes. Ramasser : l'erreur la plus fréquente sera "
              "« dont » là où il faut « sur laquelle ». C'est celle du piège.")

    return d.save(dossier)
