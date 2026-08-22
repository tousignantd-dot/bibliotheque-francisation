# -*- coding: utf-8 -*-
"""B3 · « Le décor : l'imparfait »
Bloc B « Défi 1 · Ce qui est arrivé » · couleur ambre · 75 min.
Source : exercice `t1imp`, mini-leçon `t1imp`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Le décor : l'imparfait",
        chapeau="Il était quatre heures. Tout le monde dormait. Il ventait "
                "fort. L'immeuble avait quatre logements. Rien n'y commence "
                "ni n'y finit : c'est la toile de fond sur laquelle "
                "l'évènement va se planter.",
        duree='75 minutes')

    d.titre(notes="Ouvrir en lisant les quatre phrases du chapeau, puis en demandant "
                  "ce qui est arrivé dedans. La réponse est : rien. C'est exactement "
                  "ce qu'il faut comprendre — l'imparfait ne raconte pas, il "
                  "installe.")

    d.objectifs([
        "former l'imparfait à partir du radical du « nous » du présent ;",
        "reconnaître ce qui se met à l'imparfait dans un fait divers ;",
        "repérer les mots qui appellent l'imparfait ;",
        "construire une phrase à deux temps, décor et évènement.",
    ], notes="Le quatrième objectif est le plus important des quatre et le plus long "
             "à installer. Lui garder au moins vingt minutes en fin de séance.")

    d.regle("Une seule série de terminaisons, pour tous les verbes",
            "-ais · -ais · -ait · -ions · -iez · -aient. Sans exception, "
            "d'un bout à l'autre du français.",
            precision="On les colle au radical du « nous » du présent : nous "
                      "dorm-ons donne il dormait ; nous fais-ons donne il "
                      "faisait ; nous pren-ons donne elle prenait. Un seul "
                      "verbe sort du rang, et "
                      "c'est être : j'étais, tu étais, il était.",
            notes="Diapositive à photographier. Insister sur la bonne nouvelle : "
                  "l'imparfait est le temps le plus régulier du français, et les "
                  "élèves l'apprennent souvent plus vite que le présent.")

    d.tableau('Le décor', "Ce qu'on met à l'imparfait",
              ['Ce qu\'on dit', 'La phrase'],
              [["L'heure", "Il était quatre heures du matin."],
               ["Le temps qu'il faisait", "Il ventait fort. Il pleuvait depuis trois jours."],
               ["Ce que les gens faisaient", "Tout le monde dormait dans l'immeuble."],
               ["Ce qui existait déjà", "L'immeuble avait quatre logements."],
               ["Ce qui durait", "La rivière montait depuis trois jours."]],
              cle=1,
              notes="Faire cacher la colonne de droite et produire les phrases "
                    "oralement. Les cinq lignes couvrent tout ce qu'un fait divers "
                    "met à l'imparfait : il n'y a rien d'autre à mémoriser.")

    d.cartes("Les mots qui trahissent l'imparfait", "Quand vous les voyez, la situation dure", [
        ("pendant que",
         "Pendant que les pompiers travaillaient, la police fermait la rue."),
        ("depuis",
         "La rivière montait depuis trois jours."),
        ("quand",
         "Il dormait quand il a entendu l'alarme."),
        ("toujours, encore, chaque fois",
         "Les portes des cabanons n'étaient jamais barrées."),
    ], notes="La troisième carte est la charnière de la séance : « quand » introduit "
             "l'évènement, et c'est l'autre verbe de la phrase qui passe au passé "
             "composé. Y revenir à la diapositive suivante.")

    d.regle("La phrase à deux temps, à savoir par cœur",
            "Il dormait quand il a entendu l'alarme.",
            precision="L'imparfait pose la toile de fond, le passé composé y plante "
                      "l'évènement. L'eau montait déjà quand la Ville a distribué "
                      "les sacs de sable. Changez les deux de place et la phrase ne "
                      "veut plus rien dire.",
            notes="Faire répéter les deux phrases à voix haute cinq fois, en chœur. "
                  "Cette structure revient dans chaque fait divers du monde, et elle "
                  "s'installe par la bouche avant de s'installer par la règle.")

    d.pratique('Écriture', "Mettez le verbe à l'imparfait",
               "Le radical vient du « nous » du présent.", [
        ("Il ___ (être) quatre heures du matin.", "était"),
        ("Tout le monde ___ (dormir) dans l'immeuble.", "dormait"),
        ("La rivière ___ (monter) depuis trois jours.", "montait"),
        ("L'immeuble ___ (avoir) quatre logements.", "avait"),
        ("Les portes des cabanons ___ (ne pas être) barrées.", "n'étaient pas"),
        ("Pendant que les pompiers ___ (travailler), la police fermait la rue.", "travaillaient"),
    ], corrige=True,
       notes="Exercice t1imp de l'activité. Les deux dernières sont les plus "
             "instructives : la négation à l'imparfait, et la phrase en « pendant "
             "que » où les deux verbes restent à l'imparfait parce que les deux "
             "duraient.")

    d.piege("Mettre à l'imparfait ce qui s'est passé une fois",
            "Les pompiers arrivaient huit minutes après l'appel.",
            "Les pompiers sont arrivés huit minutes après l'appel.",
            "« Huit minutes après l'appel » désigne un moment précis : c'est un "
            "évènement, donc le passé composé. L'imparfait aurait voulu dire qu'ils "
            "arrivaient toujours en huit minutes, chaque fois.",
            notes="Faire entendre la différence en disant les deux phrases. La "
                  "deuxième lecture — « chaque fois » — fait rire, et c'est ce rire "
                  "qui installe la distinction.")

    d.piege("Chercher un radical d'imparfait dans l'infinitif",
            "faire, donc il fairait",
            "nous faisons, donc il faisait",
            "Le radical de l'imparfait ne vient jamais de l'infinitif : il vient "
            "toujours du « nous » du présent. Prenez le nous, enlevez -ons, ajoutez "
            "la terminaison. Trois gestes, et aucune exception sauf être.",
            notes="Faire faire l'opération à voix haute sur cinq verbes du module : "
                  "prendre, venir, faire, dire, pouvoir. C'est mécanique, et une fois "
                  "le geste automatisé, la faute disparaît.")

    d.billet(
        "Écrivez deux phrases de décor et une phrase à deux temps.",
        exemples=[
            "Le décor : l'heure, le temps qu'il faisait, ce que les gens faisaient.",
            "La phrase à deux temps : quelque chose durait quand un évènement est arrivé.",
        ],
        notes="Ramasser. Corriger surtout la troisième phrase : c'est celle qui sera "
              "évaluée en E1 et en E2, et celle que le corrigé automatique de "
              "l'activité regarde en premier.")

    return d.save(dossier)
