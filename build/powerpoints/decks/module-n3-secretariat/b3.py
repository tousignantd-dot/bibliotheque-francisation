# -*- coding: utf-8 -*-
"""B3 · Jeudi ou le jeudi ?
Bloc B « Défi 1 · Prévenir avant » · couleur ambre (écriture) · 60 min.
Source : exercice `t1jours`, mini-leçon `t1jours`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre='Jeudi ou le jeudi ?',
        chapeau="Deux lettres décident seules du sens de la phrase : une "
                "journée manquée, ou toutes les semaines de la session.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Le point vient directement des savoirs du "
                  "niveau 3 : la présence ou l'absence du déterminant devant un jour de "
                  "la semaine. C'est court à expliquer et long à installer.")

    d.objectifs([
        "distinguer jeudi et le jeudi ;",
        "nommer les sept jours et les écrire sans majuscule ;",
        "écrire une date à la française ;",
        "ajouter prochain ou passé pour lever tout doute.",
    ])

    d.tableau('Analyse', "Un seul petit mot de différence",
              ["On dit", "Ça veut dire"],
              [["Jeudi, je vais être absente.", "jeudi qui vient, une seule journée"],
               ["Le jeudi, je travaille.", "tous les jeudis, toutes les semaines"],
               ["Lundi, j'ai un rendez-vous.", "lundi prochain"],
               ["Le lundi, mon fils va à la piscine.", "chaque semaine"]],
              cle=1,
              note="Au comptoir, c'est presque toujours la forme sans « le » : "
                   "une absence, c'est une journée.",
              notes="Diapo à photographier. Lire les quatre phrases à voix haute : la "
                    "différence s'entend à peine, et pourtant elle décide de tout.")

    d.regle("Avec « le », c'est chaque semaine",
            "jeudi = une fois  ·  le jeudi = toutes les semaines",
            precision="« Le jeudi, je vais être absente » annonce qu'on "
                      "manquera tous les jeudis de la session. La secrétaire "
                      "va le faire répéter — et elle a raison.",
            notes="Diapo à photographier. Raconter le cas : un élève qui dit « le jeudi » "
                  "en pensant à une seule journée, et le dossier qui note une absence "
                  "récurrente. Ça arrive vraiment.")

    d.tableau('Analyse', "Les sept jours et la date",
              ["Ce qu'on écrit", "Comment"],
              [["les sept jours", "lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche"],
               ["la majuscule", "aucune, sauf en début de phrase"],
               ["la date", "le 12 mars — le chiffre d'abord, le mois ensuite"],
               ["jamais", "mars 12, qui vient de l'anglais"]],
              cle=1,
              note="Dans un courriel au secrétariat, « le 12 mars » est la seule "
                   "forme acceptée.",
              notes="Diapo à photographier. La forme anglaise est très ancrée chez les "
                    "élèves qui passent par l'anglais : la signaler explicitement plutôt "
                    "que de la corriger vingt fois.")

    d.pratique('Écriture', "Jeudi ou le jeudi ?",
               "Complétez chaque phrase.", [
        ("___ , je vais être absente. Une seule journée.", "Jeudi"),
        ("___ , je travaille : je ne suis jamais au cours ce jour-là.", "Le jeudi"),
        ("Je serai absente ___ prochain, le 12 mars.", "jeudi"),
        ("___ , mon fils va à la piscine : c'est toutes les semaines.", "Le lundi"),
        ("J'ai manqué le cours ___ passé, à cause de la grippe.", "lundi"),
        ("On écrit la date « le 12 ___ », jamais « mars 12 ».", "mars"),
    ], corrige=True,
       notes="Faire écrire, puis faire justifier oralement : une fois ou toutes les "
             "semaines ? C'est la question à se poser, et elle suffit.")

    d.cartes("Trois façons de ne plus être ambigu", "Au comptoir", [
        ("Ajoutez prochain ou passé",
         "« jeudi prochain » est celui qui vient ; « jeudi passé » est celui qui est "
         "fini. Deux mots, et le doute disparaît."),
        ("Ajoutez la date",
         "« jeudi prochain, le 12 mars ». C'est ce que la secrétaire écrit : donnez-le "
         "vous-même, elle n'aura pas à le demander."),
        ("Répétez avant de partir",
         "Redites la date à voix haute. Elle la redira aussi : c'est exprès, et ce n'est "
         "jamais de la méfiance."),
    ], cols=3,
       notes="Faire pratiquer la troisième en paires : l'un donne une date, l'autre la "
             "répète. Dix secondes, et une journée manquée pour rien en moins.")

    d.piege("Écrire la date à l'anglaise",
            "mars 12",
            "le 12 mars",
            "En français, le chiffre vient d'abord et le mois ensuite. Les jours et les "
            "mois s'écrivent en minuscules. Les deux erreurs vont souvent ensemble et "
            "se corrigent d'un coup.",
            notes="Montrer les deux formes côte à côte au tableau. Faire écrire cinq "
                  "dates réelles : anniversaires, rendez-vous, fin de session.")

    d.billet(
        "Écrivez trois dates de votre session, à la française.",
        exemples=[
            "« le 12 mars », « le 28 mars », « le 3 avril »",
            "Puis une phrase : « Jeudi prochain, le ___ , je vais être absent. »",
        ],
        notes="Devoir d'écriture. Il prépare directement le courriel de « Je me lance », "
              "où les dates sont ce qui se corrige le plus souvent.")

    return d.save(dossier)
