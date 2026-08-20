# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : production orale et écrite, jeu de rôle `presenter`, autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout le module tient dans une minute de parole : bonjour, "
                "mon nom, je l'épelle, d'où je viens, ce que je parle, merci.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. Prévoir des écouteurs : la production orale se fait à "
                  "l'ordinateur, chacun de son côté. Rendre les billets corrigés avant de "
                  "commencer.")

    d.objectifs([
        "se présenter à voix haute, seul ;",
        "écrire sa fiche ;",
        "réviser les mots du module ;",
        "évaluer ce que je suis maintenant capable de faire.",
    ])

    d.cartes('Les deux défis, réunis', "Ce qui doit apparaître", [
        ("Défi 1 · se présenter",
         "Le nom, l'épellation, le pays, la ville, les langues, la famille."),
        ("Défi 2 · saluer et remercier",
         "Bonjour au début, merci à la fin — et « plus lentement » si vous ne comprenez "
         "pas la question."),
    ], notes="Diapo à photographier. C'est la grille de la production orale.")

    d.regle("Le jeu de rôle",
            "Trois situations, deux rôles.",
            precision="Dans l'activité : <b>à l'accueil</b> (on vous demande votre nom), "
                      "<b>dans la classe</b> (une nouvelle personne s'assoit à côté de "
                      "vous), <b>au secrétariat</b> (on remplit votre fiche). Vous "
                      "choisissez d'être <b>l'élève</b> ou <b>la personne qui "
                      "accueille</b>.",
            notes="L'assistant parle lentement et pose une question à la fois. Demander au "
                  "moins deux tours, dont un dans chaque rôle.")

    d.pratique('Production orale', "Ce qui est demandé",
               "Environ trente secondes, à l'ordinateur.", [
        ("Temps 1", "Bonjour. Je m'appelle…"),
        ("Temps 2", "Épelez votre nom de famille."),
        ("Temps 3", "Je viens de… J'habite à… Je parle…"),
        ("Temps 4", "Merci."),
    ], cols=1,
       notes="Trente secondes suffisent au niveau 1. La correction par l'IA arrive tout de "
             "suite ; elle n'est pas conservée.")

    d.pratique('Production écrite', "Ce qui est demandé",
               "Votre fiche, de 4 à 6 phrases.", [
        ("À écrire", "prénom et nom de famille"),
        ("À écrire", "le pays d'où vous venez"),
        ("À écrire", "la ville où vous habitez"),
        ("À écrire", "les langues que vous parlez"),
    ], cols=1,
       notes="Le billet de B1 sert de brouillon : les cinq phrases sont déjà écrites et "
             "corrigées.")

    d.piege("Apprendre le dialogue par cœur",
            "Réciter les répliques d'Amina.",
            "Dire ses propres phrases.",
            "Vous ne vous appelez pas Amina et vous ne venez pas d'Algérie. Ce sont les "
            "<b>structures</b> qui se réemploient — « je m'appelle… », « je viens de… » — "
            "pas les phrases entières.",
            notes="Rassurer : hésiter, se reprendre, chercher un mot, c'est normal et ce "
                  "n'est pas pénalisé.")

    d.tableau('Analyse', "Ce qui est regardé",
              ['Le critère', 'Ce qui compte'],
              [["La tâche", "les cinq phrases sont là"],
               ["La politesse", "bonjour au début, merci à la fin"],
               ["La clarté", "on comprend du premier coup"]],
              cle=2,
              note="La clarté passe avant la perfection.",
              notes="Diapo à photographier. Le dire avant que les élèves commencent.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux dire mon nom et l'épeler.",
            "Je peux dire d'où je viens et où j'habite.",
            "Je peux saluer et remercier.",
            "Je peux dire que je ne comprends pas.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire remplir "
              "là : elle est conservée avec les traces de l'élève. C'est la fin du module.")

    return d.save(dossier)
