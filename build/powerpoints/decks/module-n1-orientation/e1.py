# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : jeu de rôle `orientation`, production orale et écrite, exercices
`aQui` et `aPanneaux`, autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout le module tient dans une minute : je regarde un "
                "panneau, je dis le dessin, je lis le mot, je dis où je suis.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. Prévoir des écouteurs : la production orale se fait "
                  "à l'ordinateur, chacun de son côté. Rendre les billets corrigés "
                  "avant de commencer.")

    d.objectifs([
        "nommer cinq panneaux du centre à voix haute ;",
        "écrire la liste de ces panneaux ;",
        "réviser les mots du module ;",
        "évaluer ce que je suis maintenant capable de faire.",
    ])

    d.cartes('Les deux défis, réunis', "Ce qui doit apparaître", [
        ("Défi 1 · le mot sur la porte",
         "Le nom du lieu, avec son petit mot : les toilettes, la cafétéria, "
         "l'accueil, le service de garde."),
        ("Défi 2 · le panneau qui dit quoi faire",
         "Un ordre — poussez, tirez, entrez — et une interdiction : défense de "
         "fumer, ne pas entrer."),
    ], notes="Diapositive à photographier. C'est la grille de la production orale.")

    d.regle("Le jeu de rôle",
            "Trois situations, deux rôles.",
            precision="Dans l'activité : <b>devant deux portes</b> (vous cherchez les "
                      "toilettes), <b>le service de garde</b> (vous arrivez avec votre "
                      "enfant), <b>la porte qui ne s'ouvre pas</b>. Vous choisissez "
                      "d'être <b>l'élève</b> ou <b>la personne du centre</b>.",
            notes="L'assistant parle lentement, trois ou quatre mots à la fois, et "
                  "montre du doigt au lieu d'expliquer un chemin. Demander au moins "
                  "deux tours, dont un dans chaque rôle.")

    d.pratique('Production orale', "Ce qui est demandé",
               "Environ trente secondes, à l'ordinateur.", [
        ("Temps 1", "Dites ce que montre le dessin."),
        ("Temps 2", "Lisez le mot écrit à côté."),
        ("Temps 3", "Dites ce qu'on fait à cet endroit."),
        ("Temps 4", "Recommencez pour cinq panneaux."),
    ], cols=1,
       notes="Trente secondes suffisent au niveau 1. La correction par l'IA arrive tout "
             "de suite ; elle n'est pas conservée.")

    d.pratique('Production écrite', "Ce qui est demandé",
               "Votre liste, de 4 à 6 lignes.", [
        ("À écrire", "le mot du panneau, en MAJUSCULES"),
        ("À écrire", "le même mot en minuscules, avec le, la ou les"),
        ("À écrire", "ce qu'on fait à cet endroit"),
        ("À écrire", "au moins un panneau qui interdit quelque chose"),
    ], cols=1,
       notes="Les billets de A3, B1, B2 et C2 servent de brouillon : les quatre "
             "morceaux de la liste y sont déjà, corrigés.")

    d.tableau('Analyse', "Un modèle de ligne",
              ['Ce qu\'on écrit', 'Exemple'],
              [["le mot du panneau", "CAFÉTÉRIA"],
               ["le mot avec son article", "la cafétéria"],
               ["ce qu'on y fait", "on mange à midi"]],
              cle=1,
              note="CAFÉTÉRIA — la cafétéria — on mange à midi.",
              notes="Diapositive à photographier. Écrire la ligne complète au tableau "
                    "et l'y laisser pendant toute la production écrite.")

    d.piege("Recopier le dialogue par cœur",
            "Réciter les répliques de Rosa.",
            "Nommer les panneaux de son propre centre.",
            "Vous ne vous appelez pas Rosa et votre centre n'est pas le sien. Ce sont "
            "les <b>structures</b> qui se réemploient — « c'est la… », « c'est écrit… » "
            "— pas les phrases entières. Regardez vos vraies portes.",
            notes="Rassurer : hésiter, se reprendre, chercher un mot, c'est normal et "
                  "ce n'est pas pénalisé.")

    d.tableau('Analyse', "Ce qui est regardé",
              ['Le critère', 'Ce qui compte'],
              [["La tâche", "cinq panneaux, vraiment nommés"],
               ["Le petit mot", "le, la, les devant le nom"],
               ["La clarté", "on comprend du premier coup"]],
              cle=1,
              note="La clarté passe avant la perfection.",
              notes="Diapositive à photographier. Le dire avant que les élèves "
                    "commencent, pas après.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux dire ce que montre un dessin de panneau.",
            "Je peux lire TOILETTES, CAFÉTÉRIA, SORTIE, ENTRÉE.",
            "Je peux dire « c'est la cafétéria » avec le bon petit mot.",
            "Je peux dire si un panneau permet ou interdit quelque chose.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire "
              "remplir là : elle est conservée avec les traces de l'élève. C'est la "
              "fin du module.")

    return d.save(dossier)
