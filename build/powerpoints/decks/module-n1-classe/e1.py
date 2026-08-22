# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source du module : jeu de rôle `classe1`, production orale, production écrite,
autoévaluation.

Ce que le niveau 1 demande tient en peu de choses : nommer, montrer,
comprendre une heure. La séance ne demande donc jamais d'expliquer quoi que ce
soit — c'est ce qui la sépare de la même séance au niveau 2.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout le module tient en trente secondes de parole : cinq "
                "objets, où en est un, et l'heure du cours.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. Prévoir des écouteurs : la production orale se fait "
                  "à l'ordinateur, chacun de son côté. Rendre les billets corrigés avant "
                  "de commencer.")

    d.objectifs([
        "nommer cinq objets à voix haute ;",
        "dire où est un objet ;",
        "dire l'heure du cours ;",
        "écrire son horaire de la semaine.",
    ])

    d.cartes('Les deux défis, réunis', "Ce qui doit apparaître", [
        ("Défi 1 · la consigne",
         "Comprendre écoutez, regardez, ouvrez, fermez — et dire où est la chose : sur, "
         "dans, sous."),
        ("Défi 2 · l'heure et l'horaire",
         "L'heure du début, l'heure de la pause, l'heure de la fin, et les jours de "
         "cours."),
    ], notes="Diapositive à photographier. C'est la grille de la production orale.")

    d.regle("Le jeu de rôle",
            "Trois situations, deux rôles.",
            precision="Dans l'activité : <b>la consigne</b> (l'enseignante dit deux mots, "
                      "vous faites), <b>l'objet</b> (on vous montre une chose, vous la "
                      "nommez), <b>l'heure</b> (vous demandez à quelle heure). Vous "
                      "choisissez d'être l'<b>élève</b> ou l'<b>enseignante</b>.",
            notes="L'assistant dit une seule chose à la fois, en trois ou quatre mots. "
                  "Demander au moins deux tours, dont un dans chaque rôle.")

    d.pratique('Production orale', "Ce qui est demandé",
               "Environ trente secondes, à l'ordinateur.", [
        ("Temps 1", "Nommez cinq objets : un livre, un stylo…"),
        ("Temps 2", "Dites où est un objet : mon sac est sous ma chaise."),
        ("Temps 3", "Dites l'heure : le cours commence à huit heures et demie."),
        ("Temps 4", "Dites l'heure de la fin : il finit à midi."),
    ], cols=1,
       notes="Trente secondes suffisent au niveau 1. La correction par l'IA arrive tout "
             "de suite ; elle n'est pas conservée.")

    d.pratique('Production écrite', "Ce qui est demandé",
               "Votre horaire, de 3 à 5 phrases.", [
        ("À écrire", "les jours de cours, en minuscules"),
        ("À écrire", "l'heure du début, avec « à »"),
        ("À écrire", "l'heure de la fin"),
        ("À écrire", "l'heure de la pause"),
    ], cols=1,
       notes="Les billets de C1 et de C2 servent de brouillon : les phrases sont déjà "
             "écrites et corrigées.")

    d.piege("Apprendre le dialogue par cœur",
            "Réciter les répliques de Bopha.",
            "Dire ses propres phrases.",
            "Vous ne vous appelez pas Bopha et votre horaire n'est pas le sien. Ce sont "
            "les <b>phrases utiles</b> qui se réemploient — « c'est un… », « il est "
            "sous… », « à huit heures » — pas le dialogue entier.",
            notes="Rassurer : hésiter, chercher un mot, se reprendre, c'est normal et ce "
                  "n'est pas pénalisé.")

    d.tableau('Analyse', "Ce qui est regardé",
              ['Le critère', 'Ce qui compte'],
              [["La tâche", "les cinq objets sont nommés"],
               ["L'heure", "on comprend quelle heure c'est"],
               ["La clarté", "on comprend du premier coup"]],
              cle=2,
              note="La clarté passe avant la perfection. L'article n'est pas compté.",
              notes="Diapositive à photographier. Le dire avant que les élèves "
                    "commencent : au niveau 1, on n'enlève rien pour un « un » à la "
                    "place d'une « une ».")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux nommer six objets de ma classe.",
            "Je peux comprendre une consigne courte et faire le geste.",
            "Je peux dire où est un objet.",
            "Je peux comprendre l'heure de mon cours et lire mon horaire.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire "
              "remplir là : elle est conservée avec les traces de l'élève. C'est la fin "
              "du module.")

    return d.save(dossier)
