# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : production orale et écrite du module, jeu de rôle `linge`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout ce qui a été appris se rassemble : nommer, dire sa "
                "taille, comparer deux prix. Un jeu de rôle, une production "
                "orale, une production écrite.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Prévoir des écouteurs : la production orale se "
                  "fait à l'ordinateur, chacun de son côté.")

    d.objectifs([
        "tenir une conversation complète dans un magasin de vêtements ;",
        "employer les trois défis dans une même production ;",
        "écrire une liste de linge d'hiver avec couleurs et tailles ;",
        "recevoir une correction et la relire.",
    ])

    d.cartes('Les trois défis, réunis', "Ce qui doit apparaître", [
        ("Défi 1 · demander",
         "Saluer, dire le vêtement avec sa couleur, donner sa taille, demander à essayer."),
        ("Défi 2 · comparer",
         "Demander le prix de deux articles, dire lequel est moins cher, montrer du doigt "
         "avec « celui-ci » et « celui-là »."),
        ("Défi 3 · conclure",
         "Comprendre le montant, faire répéter s'il le faut, garder la facture."),
    ], notes="Diapo à photographier. C'est la grille de la production orale.")

    d.regle("Le jeu de rôle",
            "Trois situations, deux rôles.",
            precision="Dans l'activité interactive : le <b>manteau d'hiver</b> (premier "
                      "hiver, taille inconnue), les <b>bottes en liquidation</b> (une "
                      "étiquette à deux prix), le <b>chandail en rabais</b> (une affiche "
                      "qui ne dit pas sur quoi). Vous choisissez d'être le <b>client</b> "
                      "ou la <b>conseillère</b> — faites les deux, ils n'emploient pas les "
                      "mêmes phrases.",
            notes="Six combinaisons en tout. Demander au moins deux tours, dont un dans "
                  "chaque rôle.")

    d.pratique('Production orale', "Ce qui est demandé",
               "Environ 45 secondes, à l'ordinateur.", [
        ("Ouvrir", "saluer et dire ce que vous cherchez, avec la couleur"),
        ("Préciser", "donner votre taille et demander à essayer"),
        ("Comparer", "demander deux prix et dire lequel est moins cher"),
        ("Choisir", "dire ce que vous prenez, et pourquoi"),
        ("Fermer", "remercier"),
    ], cols=1,
       notes="La correction par l'IA arrive tout de suite. Elle n'est pas conservée : "
             "l'élève la lit, la note, et recommence s'il le veut.")

    d.piege("Réciter au lieu de parler",
            "Apprendre le dialogue par cœur et le redire.",
            "Employer les structures avec ses propres mots.",
            "Un dialogue récité s'entend, et il ne prépare à rien : la vraie conseillère ne "
            "dira pas la réplique attendue. Les structures — « je cherche un… », « je "
            "porte du… », « celui-ci est moins cher que… » — se réemploient ; les phrases "
            "entières, non.",
            notes="Rassurer : hésiter, se reprendre et chercher un mot est normal et n'est "
                  "pas pénalisé.")

    d.pratique('Production écrite', "Ce qui est demandé",
               "Une liste de linge d'hiver, de 5 à 8 phrases.", [
        ("Le sujet", "ce dont vous avez besoin cet hiver, pour vous ou votre famille"),
        ("À employer", "cinq vêtements au moins, une couleur pour chacun"),
        ("À employer aussi", "une taille ou une pointure, et une comparaison de prix"),
        ("À vérifier", "la couleur après le vêtement, et son accord"),
    ], cols=1,
       notes="Les billets de B2 et C4 servent de matière première : les élèves ont déjà "
             "écrit une partie de ces phrases.")

    d.tableau('Analyse', "Ce qui est regardé",
              ['Le critère', 'Ce qui compte'],
              [["La tâche", "les trois moments sont là"],
               ["Le vocabulaire", "les mots du module sont employés"],
               ["La langue", "la couleur après le nom, l'accord, le « que »"],
               ["La clarté", "on comprend du premier coup"]],
              cle=3,
              note="La clarté passe avant la perfection : une phrase simple et juste vaut "
                   "mieux qu'une phrase compliquée et fausse.",
              notes="Diapo à photographier. Le dire avant que les élèves commencent.")

    d.cartes("Si vous bloquez", "Trois secours", [
        ("Les mini-leçons",
         "Sept panneaux « Ouvrir la mini-leçon » dans l'activité, avec l'audio. Ils restent "
         "ouverts pendant la production."),
        ("Les cartes mémoire",
         "Seize mots avec définition, exemple et image. Section « Je retiens des mots »."),
        ("Le bouton d'aide",
         "Il envoie un signal à l'enseignante avec le titre de l'exercice où vous êtes. "
         "Elle vient sans que vous ayez à lever la main."),
    ], notes="Montrer les trois à l'écran avant de lancer la production.")

    d.billet(
        "Notez ce que la correction vous a signalé.",
        exemples=[
            "Deux choses réussies, deux choses à travailler.",
            "Gardez la note : elle sert à la séance E2.",
        ],
        notes="La correction de l'IA n'est pas conservée par le système. Cette note est la "
              "seule trace qu'il en restera.")

    return d.save(dossier)
