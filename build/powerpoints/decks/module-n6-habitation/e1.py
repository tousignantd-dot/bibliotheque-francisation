# -*- coding: utf-8 -*-
"""E1 · Redis le diagnostic, puis pose tes questions
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : bloc « Je me lance » de custom.js — jeu de rôle et production orale.
La tâche vient de l'intention de la situation elle-même : comprendre de
l'information et poser des questions reliées à des travaux de réparation ou de
rénovation, portée en compréhension comme en production.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Redis le diagnostic, puis pose tes questions",
        chapeau="Quelqu'un n'était pas là quand l'entrepreneur est passé. "
                "Quatre-vingt-dix secondes pour lui dire ce qui a été trouvé, "
                "ce qu'on fait faire, et ce qui reste à demander.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Prévoir la moitié du temps pour le jeu de "
                  "rôle avec l'assistant et l'autre moitié pour l'enregistrement. "
                  "Les élèves qui n'ont pas fini enregistrent à la maison.")

    d.objectifs([
        "redire un diagnostic entendu, dans l'ordre et avec ses chiffres ;",
        "distinguer la cause du résultat à voix haute ;",
        "poser deux questions précises ;",
        "se réécouter et se corriger avant d'envoyer.",
    ], notes="Le quatrième objectif est celui qu'on saute toujours. Insister : "
             "personne n'envoie un premier enregistrement.")

    d.declencheur(
        'Observation', "Vous racontez un diagnostic à quelqu'un. Par où commencez-vous ?",
        pistes=[
            "Par ce qu'on voit, ou par ce qui l'a causé ?",
            "Combien de chiffres faut-il donner ?",
            "À quel moment posez-vous vos questions ?",
        ],
        notes="Il n'y a pas de mauvais ordre, mais celui du module — le résultat, puis "
              "la cause, puis les travaux — est le plus facile à suivre pour "
              "quelqu'un qui n'était pas là.")

    d.tableau('Analyse', "Le plan en trois temps",
              ['Le temps', 'Ce qu\'on y dit'],
              [["TEMPS 1", "ce qui a été trouvé, et ce qui l'a causé"],
               ["TEMPS 2", "ce qu'on fait faire, dans l'ordre, avec un chiffre"],
               ["TEMPS 3", "les deux questions qu'on posera avant de signer"]],
              cle=0,
              note="Quatre-vingt-dix secondes : environ trente par temps.",
              notes="Diapositive à photographier. Le même plan est affiché dans le "
                    "module, sous la production orale. Le faire recopier au verso de "
                    "la fiche.")

    d.regle("Un chiffre par minute",
            "Une explication sans chiffre ne se distingue pas d'une impression.",
            precision="Un mètre de fissure. Quarante centimètres entre la gouttière et "
                      "le mur. Dix-neuf pour cent d'humidité. Quatre semaines de "
                      "séchage. Ce sont ces chiffres-là qui font qu'on vous croit, "
                      "et ce sont eux que votre interlocuteur retiendra.",
            notes="Diapositive à photographier. C'est le critère de correction le plus "
                  "visible : compter les chiffres donnés.")

    d.pratique('Modèle', "Trois débuts possibles",
               "Lisez-les à voix haute, puis choisissez celui qui vous ressemble.", [
        ("Le mur de fondation est fendu, mais ce n'est pas ça, le problème.", "on annonce tout de suite"),
        ("Il y a une fissure d'un mètre. La cause, c'est la gouttière.", "on donne le chiffre d'abord"),
        ("L'entrepreneur a passé une heure en bas. Voici ce qu'il a trouvé.", "on situe la scène"),
        ("Ce qu'on voit, c'est une fissure. Ce qui la produit est dehors.", "on oppose les deux"),
    ], corrige=True,
       notes="Faire lire les quatre à voix haute par quatre élèves différents. Les "
             "quatre fonctionnent : le but est que chacun s'en approprie un.")

    d.tableau('Analyse', "Ce qu'on réutilise du module",
              ['Le point', 'Un exemple'],
              [["la cause", "le mur fend parce que le sol pousse"],
               ["le faire causatif", "je fais injecter la fissure par un spécialiste"],
               ["la reprise", "la fissure ? je ne veux pas qu'on la répare avant"],
               ["l'hypothèse", "si le permis sort dans dix jours, ce sera prêt"],
               ["la question", "quel délai entre l'injection et le gypse ?"]],
              cle=0,
              note="Cinq points, cinq séances. Aucun n'est nouveau.",
              notes="Diapositive à photographier. C'est la synthèse du module, et elle "
                    "arrive au moment où elle sert.")

    d.piege('Piège', "enchaîner un fait et une opinion",
            "annoncer l'opinion",
            "« La peinture n'est pas comprise, ça vaut la peine de la faire "
            "nous-mêmes. » Celui qui écoute prend la seconde phrase pour un fait. "
            "Ajoutez trois mots : « d'après la soumission… ; à mon avis… ». Rien "
            "n'a changé sauf le statut de chaque phrase, et c'est tout ce qui "
            "compte.",
            notes="Reprise de D2. Le rappeler ici parce que c'est le point le plus "
                  "souvent perdu à l'oral, où l'on va vite.")

    d.pratique('Préparation', "Trois minutes pour préparer",
               "Notez au crayon, en mots-clés, pas en phrases.", [
        ("le résultat", "une fissure d'un mètre, mur nord"),
        ("la cause", "gouttière à 40 cm, pente du terrain"),
        ("l'ordre", "gouttières, pente, injection, séchage"),
        ("un chiffre", "dix-neuf pour cent, quatre semaines"),
        ("deux questions", "quel délai ? qu'arrive-t-il si un imprévu ?"),
    ], corrige=True,
       notes="Trois minutes, montre en main. En mots-clés : un texte rédigé se lit, et "
             "un texte lu s'entend tout de suite. C'est la seule consigne "
             "importante de la préparation.")

    d.billet(
        "Après t'être réécouté : qu'est-ce que tu changerais ?",
        exemples=[
            "Une chose seulement.",
            "Puis refais-le, et envoie la deuxième version.",
        ],
        notes="Cinq minutes. Ramasser les billets et les rendre avec la rétroaction : "
              "ce que l'élève a repéré lui-même vaut plus que ce qu'on lui signale.")

    return d.save(dossier)
