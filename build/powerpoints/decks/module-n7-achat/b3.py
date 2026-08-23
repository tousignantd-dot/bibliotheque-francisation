# -*- coding: utf-8 -*-
"""B3 · Systématiquement, par intermittence, seulement
Bloc B « Défi 1 · Le bruit qu'il faut décrire » · couleur ambre · grammaire ·
75 min.
Source : exercice `t1adv` et sa mini-leçon ; savoir « adverbes et GAdv » du
niveau 7 (deux points).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Systématiquement, par intermittence, seulement",
        chapeau="Entre « ça arrive souvent » et « ça arrive "
                "systématiquement », il n'y a qu'un mot — et toute la "
                "différence entre une impression et un fait vérifiable.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais rentable tout de suite : ces adverbes "
                  "servent au garage, au comptoir et dans la lettre. Le dire en "
                  "ouvrant, sinon le groupe croit qu'on change de sujet.")

    d.objectifs([
        "placer un adverbe de fréquence sur l'échelle du jamais au toujours ;",
        "employer « par intermittence » et savoir ce qu'il oblige à faire en plus ;",
        "restreindre avec « seulement » et avec « ne… que » ;",
        "placer l'adverbe au bon endroit avec un temps composé.",
    ], notes="Le troisième objectif porte le piège de la séance : « ne… que » n'est pas "
             "une négation. Le poser tôt et y revenir deux fois.")

    d.declencheur(
        'Observation', "« Souvent » et « systématiquement » : est-ce la même chose ?",
        pistes=[
            "Lequel des deux se vérifie ?",
            "Si vous dites « toujours », que fera le mécanicien ?",
            "Que veut dire « des fois » pour quelqu'un qui doit chercher ?",
            "Comment diriez-vous « trois matins sur cinq » sans chiffre ?",
        ],
        notes="La deuxième question a une réponse concrète : il fera un essai routier "
              "qui ne reproduira rien, et il facturera l'essai. « Toujours » est presque "
              "toujours faux.")

    d.tableau('Analyse', "L'échelle de la fréquence",
              ['Le mot', 'Ce qu\'il dit exactement'],
              [["jamais", "pas une fois, souvent dans une condition"],
               ["rarement", "moins d'une fois sur cinq"],
               ["souvent", "plus d'une fois sur deux, sans plus"],
               ["systématiquement", "chaque fois que la condition est réunie"],
               ["toujours", "sans aucune condition : rare pour une panne"]],
              cle=0,
              notes="Diapositive à photographier. Insister sur la différence entre les "
                    "deux dernières rangées : « systématiquement » nomme une condition, "
                    "« toujours » n'en nomme aucune.")

    d.regle("« Ne… que » restreint, il ne nie pas",
            "« Je n'ai fait que 900 kilomètres » affirme les 900 kilomètres, et souligne qu'ils sont peu.",
            precision="C'est exactement l'effet qu'on cherche dans une réclamation : "
                      "poser un chiffre et faire entendre qu'il est petit, sans "
                      "commentaire. Le test est simple : si l'on peut remplacer par "
                      "« seulement » sans changer le sens, c'est une restriction. Si "
                      "la phrase demande un « pas », c'est une négation.",
            notes="Diapositive à photographier. Faire l'essai à voix haute sur trois "
                  "phrases : le remplacement par « seulement » est infaillible et se "
                  "retient mieux qu'une règle.")

    d.cartes('Analyse', "Quatre outils, quatre emplois", [
        ("par intermittence", "apparaît et disparaît : il faut alors noter chaque fois, avec la date"),
        ("seulement, ne… que", "restreint, donc élimine tout le reste"),
        ("à peine", "tout juste perceptible : utile pour comparer deux moments"),
        ("nettement", "de façon marquée : utile pour dire que ça empire"),
    ], notes="La première carte demande un geste : trois lignes dans la boîte à gants, "
             "la date, l'heure, la température, ce qui se passait. C'est le seul cas où "
             "l'élève doit tenir un registre.")

    d.pratique('Grammaire', "Complétez avec le bon adverbe",
               "Un mot ou une locution par trou.", [
        ("Le cognement revient ___ le matin, quand l'auto a passé la nuit dehors.", "seulement (ou uniquement)"),
        ("Dans la montée, il se produit ___ : jamais une seule fois il n'a manqué.", "systématiquement"),
        ("Le soir, on l'entend ___ : il faut baisser la radio pour l'entendre.", "à peine"),
        ("Le témoin s'allume ___ : deux fois en avril, puis plus rien.", "par intermittence"),
        ("Depuis samedi, le jeu du levier est ___ plus grand qu'à la livraison.", "nettement (ou franchement)"),
        ("Elle ne roule ___ entre la maison et l'école.", "que"),
    ], corrige=True,
       notes="Huit items dans le module ; en projeter six. Le dernier est celui qui "
             "arrête tout le monde : faire relire la règle de « ne… que » avant de "
             "donner la réponse.")

    d.piege('Piège', "employer « toujours » pour insister",
            "le remplacer par la condition qui déclenche",
            "« Ça fait toujours ça » devient « ça le fait chaque fois que je pars à "
            "froid ». Même force, et la deuxième version se vérifie. C'est la seule "
            "correction de cette séance qui change quelque chose au comptoir d'un "
            "garage.",
            notes="Faire réécrire trois phrases du groupe sur ce modèle. Les élèves "
                  "voient alors que la précision n'affaiblit rien : elle rend crédible.")

    d.pratique('Grammaire', "Où se place l'adverbe ?",
               "Placez « souvent » au bon endroit, puis lisez la phrase à voix haute.", [
        ("Le bruit revient. (temps simple)", "Le bruit revient souvent."),
        ("Le bruit est revenu. (temps composé)", "Le bruit est souvent revenu."),
        ("Il est revenu. (avec « systématiquement »)", "Il est revenu systématiquement."),
        ("Elle a signalé le problème. (avec « déjà »)", "Elle a déjà signalé le problème."),
    ], corrige=True,
       notes="La règle en une phrase : entre l'auxiliaire et le participe, sauf les "
             "adverbes longs, qui passent après. Le troisième item montre l'exception, "
             "et le quatrième prépare B4.")

    d.billet(
        "Écris une phrase qui décrit un problème, avec un adverbe de fréquence précis.",
        exemples=[
            "Pas de « souvent » ni de « des fois ».",
            "Un chiffre ou « systématiquement ».",
        ],
        notes="Deux minutes. Faire lire trois billets à voix haute et demander au "
              "groupe si la fréquence se vérifie. C'est le seul critère.")

    return d.save(dossier)
