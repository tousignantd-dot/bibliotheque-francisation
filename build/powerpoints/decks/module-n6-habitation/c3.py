# -*- coding: utf-8 -*-
"""C3 · La soumission, et ce qu'elle exclut
Bloc C « Défi 2 · Les papiers du chantier » · couleur ambre · 75 min.
Source : exercice `t2soum` (type texte) et la mini-leçon `t2mise`. Savoir du
programme : tenir compte de la présentation matérielle et de la mise en page ;
comprendre des textes informatifs et injonctifs.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="La soumission, et ce qu'elle exclut",
        chapeau="Cinq postes, un total, un échéancier — et cinq lignes en "
                "bas de page qui décident de la facture finale.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture, deuxième document. Commencer par faire relire à "
                  "voix haute la phrase du bloc : le rapport décrit ce qui est, la "
                  "soumission décrit ce qui sera fait.")

    d.objectifs([
        "lire une soumission par postes plutôt que ligne à ligne ;",
        "trouver le total, l'acompte et la durée de validité ;",
        "lire les exclusions avant de regarder le total ;",
        "reconnaître la clause de la condition non visible.",
    ], notes="Le troisième objectif inverse l'habitude de tout le monde. Le dire "
             "franchement : on regarde le total en premier, et c'est justement ce "
             "qu'il ne faut pas faire.")

    d.declencheur(
        'Observation', "34 500 $. Est-ce cher ?",
        pistes=[
            "Que faut-il savoir avant de pouvoir répondre ?",
            "Le prix comprend-il les taxes ?",
            "Que se passe-t-il si on trouve autre chose en ouvrant ?",
        ],
        notes="La question n'a pas de réponse, et c'est le but. Un montant seul ne "
              "veut rien dire : il faut savoir ce qu'il couvre, ce qu'il exclut et "
              "combien de temps il tient.")

    d.tableau('Analyse', "Les cinq postes de la soumission 2024-411",
              ['Le poste', 'Le prix'],
              [["gouttières et terrain", "4 200 $"],
               ["injection de la fissure", "2 600 $"],
               ["séchage assisté", "1 150 $"],
               ["isolation et gypse", "14 800 $"],
               ["plomberie et électricité", "11 750 $"]],
              cle=0,
              note="Total avant taxes : 34 500 $. Tous les montants du module sont inventés.",
              notes="Diapositive à photographier. Le troisième poste est celui qui "
                    "étonne : on paie l'attente. Le faire remarquer, c'est ce qui "
                    "rend un échéancier lisible.")

    d.tableau('Analyse', "Ce qui n'est pas dans le prix",
              ['L\'exclusion', 'Ce que ça veut dire'],
              [["le permis municipal", "vous le demandez et vous le payez"],
               ["la peinture", "à faire vous-même, ou à part"],
               ["les luminaires", "l'électricien pose ce que vous achetez"],
               ["la condition non visible", "ce qu'on découvrira en ouvrant"]],
              cle=0,
              note="La dernière est la seule dont on ne peut pas prévoir le montant.",
              notes="Diapositive à photographier. C'est le cœur de la séance et la "
                    "porte du bloc D. Prendre le temps sur la quatrième rangée.")

    d.regle("Lire les exclusions avant le total",
            "Le montant ne veut rien dire tant qu'on ne sait pas ce qu'il ne couvre pas.",
            precision="Deux soumissions de 30 000 $ et de 34 500 $ ne se comparent "
                      "pas tant qu'on n'a pas lu les deux listes d'exclusions. La "
                      "moins chère est souvent celle qui exclut le plus — et la "
                      "différence se paie plus tard, en pleine saison, quand on n'a "
                      "plus le choix de l'entrepreneur.",
            notes="Diapositive à photographier. C'est la règle de la séance, et c'est "
                  "celle qui sert le plus dans la vraie vie des élèves.")

    d.pratique('Lecture', "Où est la réponse ?",
               "Dites à quel endroit de la soumission chaque réponse se trouve.", [
        ("Combien de temps le prix reste-t-il valide ?", "première ligne, avec le numéro"),
        ("Quel est le montant total avant taxes ?", "après les cinq postes"),
        ("Que faut-il verser à la signature ?", "juste sous le total"),
        ("Combien de temps les travaux vont-ils durer ?", "ligne de l'échéancier"),
        ("Quel poste paie l'attente du séchage ?", "poste 3 des postes inclus"),
        ("Quelle phrase couvre ce qu'on découvrira ?", "dernière ligne des exclusions"),
    ], corrige=True,
       notes="Le même exercice existe dans le module, en type « texte » : neuf "
             "passages, neuf questions. Ici, faire encercler au crayon.")

    d.piege('Piège', "accepter un prix donné de vive voix",
            "demander une soumission écrite et détaillée",
            "Un chiffre lancé sur le pas de la porte n'engage personne, et il est "
            "toujours plus bas que la facture. Ce n'est pas de la malhonnêteté : on "
            "ne peut pas chiffrer ce qu'on n'a pas détaillé. Une soumission écrite "
            "n'est pas une marque de méfiance, c'est un outil de travail pour les "
            "deux parties.",
            notes="Le moment de la séance à ne pas presser. Plusieurs élèves ont vécu "
                  "l'inverse et s'en sont bien tirés : ne pas nier leur expérience, "
                  "mais nommer le risque.")

    d.pratique('Écriture', "Demander une précision par écrit",
               "Écrivez la phrase que vous ajouteriez à la soumission.", [
        ("un imprévu doit être annoncé avant d'être fait",
         "Toute condition imprévue fera l'objet d'un avis écrit avant exécution."),
        ("les taxes doivent apparaître", "Le montant total, taxes comprises, sera indiqué."),
        ("le séchage compte dans le délai", "L'échéancier de six semaines comprend la période de séchage."),
        ("la garantie doit être écrite", "La garantie sur l'injection sera précisée par écrit."),
    ], corrige=True,
       notes="Exercice d'écriture, premier du bloc. Accepter toute formulation claire. "
             "Le point à souligner : une phrase courte et précise s'ajoute sans "
             "discussion ; une phrase longue se négocie.")

    d.billet(
        "Quelle exclusion t'inquiéterait le plus, et pourquoi ?",
        exemples=[
            "Une phrase.",
            "Dis ce que tu ferais pour t'en protéger.",
        ],
        notes="Trois minutes. La plupart choisiront la condition non visible : c'est "
              "la bonne réponse, et c'est exactement ce qui arrive au bloc D.")

    return d.save(dossier)
