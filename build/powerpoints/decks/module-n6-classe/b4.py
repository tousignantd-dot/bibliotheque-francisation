# -*- coding: utf-8 -*-
"""B4 · L'ordre des étapes quand rien ne dit « d'abord »
Bloc B « Défi 1 » · couleur ambre · 75 min. Grammaire du texte.
Source du module : exercice `t1ordre` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="L'ordre des étapes quand rien ne dit « d'abord »",
        chapeau="Dans un mode d'emploi, tout est numéroté. Dans une consigne "
                "de travail, presque rien ne l'est : l'ordre se cache dans "
                "des mots de deux syllabes.",
        duree='75 minutes')

    d.titre(notes="Le programme du niveau 6 nomme ce savoir précisément : "
                  "comprendre l'ordre des étapes d'une consigne à partir "
                  "d'indices linguistiques autres que les connecteurs de "
                  "temps. Aucun autre niveau ne le demande.")

    d.objectifs([
        "reconnaître quatre indices qui rangent sans dire « d'abord » ;",
        "récrire une phrase à l'endroit quand elle inverse l'ordre ;",
        "entendre la condition cachée dans « dès que » ;",
        "traduire une interdiction déguisée en ordre positif.",
    ], notes="« D'abord », « ensuite », « enfin » ont été appris au niveau 3. "
             "Ce sont précisément ceux qui manquent ici.")

    d.declencheur(
        'Observation', "« Avant de choisir, lisez la liste au complet. » Que fait-on en premier ?",
        pistes=[
            "Le premier verbe de la phrase, c'est « choisir ».",
            "Est-ce que c'est la première action ?",
            "Comment le vérifier ?",
        ],
        notes="Une bonne moitié du groupe répond « choisir ». Laisser "
              "l'erreur s'installer avant de la défaire : c'est le meilleur "
              "moment d'apprentissage de la séance.")

    d.tableau('Analyse', "Quatre indices qui rangent",
              ['L\'indice', 'Ce qu\'il dit'],
              [["une fois", "ce qui suit est fini avant que le reste commence"],
               ["avant de", "le verbe écrit en premier vient en second"],
               ["dès que", "ensuite, mais aussi : pas avant"],
               ["sans avoir", "une interdiction déguisée en conseil"]],
              cle=0,
              note="Ces quatre-là couvrent presque toutes les consignes, à l'école comme au travail.",
              notes="Diapositive à photographier. Faire chercher les quatre "
                    "dans la feuille de consigne du module : il y en a trois "
                    "sur quatre.")

    d.regle("« Avant de » inverse l'ordre de lecture",
            "« Avant de choisir, lisez la liste au complet » : on lit d'abord, on choisit ensuite.",
            precision="C'est le seul des quatre indices qui met l'action "
                      "seconde en premier dans la phrase. Récrivez ces "
                      "phrases à l'endroit sur votre feuille de plan.",
            notes="Diapositive à photographier. Une seule inversion, dans une "
                  "consigne, décale tout le reste — et coûte ici une semaine "
                  "de recherche sur un sujet qui sera refusé.")

    d.tableau('Analyse', "Six phrases, six ordres",
              ['La phrase de la consigne', 'Ce qu\'on fait en premier'],
              [["Une fois le sujet approuvé…", "faire approuver le sujet"],
               ["Avant de choisir, lisez…", "lire la liste"],
               ["Dès que vous avez trois sources…", "trouver la troisième"],
               ["Ne commencez pas sans avoir lu…", "lire la grille"],
               ["Le texte se terminera par…", "rien encore : c'est la fin"]],
              cle=1,
              note="La cinquième ne contient aucun indice : c'est la place dans la page qui parle.",
              notes="Diapositive à photographier. La cinquième ligne "
                    "introduit la dernière idée de la séance : ce qui est "
                    "écrit en dernier se fait presque toujours en dernier.")

    d.piege('Grammaire',
            "lire « dès que » comme un simple « ensuite »",
            "entendre aussi le « pas avant »",
            "« Dès que vous avez trois sources, écrivez le plan » ne dit pas "
            "seulement dans quel ordre : il dit que deux sources ne "
            "suffisent pas. C'est une condition, pas un moment — et une "
            "équipe qui l'a lu comme un moment écrit son plan trop tôt.",
            notes="Faire reformuler par le groupe : « avec deux sources, on "
                  "n'écrit pas encore le plan ». La reformulation vaut mieux "
                  "que l'explication.")

    d.pratique('Pratique', "Qu'est-ce qui vient avant quoi ?",
               "Pour chaque phrase, dites ce que la consigne vous apprend sur l'ordre.", [
        ("Une fois le sujet approuvé, cherchez trois sources.", "l'approbation d'abord ; la recherche pas avant"),
        ("Avant de choisir, lisez la liste au complet.", "la lecture d'abord, le choix ensuite"),
        ("Dès que vous avez trois sources, écrivez le plan.", "le plan attend les trois sources"),
        ("Ne commencez pas à écrire sans avoir lu la grille.", "la grille avant la première phrase"),
        ("Le texte se terminera par une bibliographie.", "c'est la dernière partie du document"),
        ("L'équipe présentera ensuite son compte rendu.", "l'oral après la remise du texte"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t1ordre` du module. Faire récrire les deux "
             "premières phrases à l'endroit, par écrit : c'est le geste qu'on "
             "veut installer.")

    d.billet(
        "Récris à l'endroit une phrase de la consigne qui inverse l'ordre.",
        exemples=[
            "Commence par ce qui se fait en premier.",
            "Exemple : « Avant de choisir, lisez la liste » devient « Lisez la liste, puis choisissez ».",
        ],
        notes="Trois minutes. Le geste est simple et il se garde : les élèves "
              "le refont d'eux-mêmes sur les consignes des autres cours, "
              "d'après ce qu'ils rapportent.")

    return d.save(dossier)
