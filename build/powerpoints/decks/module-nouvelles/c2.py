# -*- coding: utf-8 -*-
"""C2 · L'imparfait du verbe être.
Bloc C · couleur ambre (écriture) · 60 min.
Source : exercice `t2etre` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="L'imparfait du verbe être",
        chapeau="« Il était 8 h quand les pompiers sont arrivés. » Deux temps du passé "
                "dans une phrase : l'un plante le décor, l'autre raconte l'événement.",
        duree='60 minutes')

    d.titre(notes="Écrire la phrase du chapeau au tableau et demander lequel des deux "
                  "verbes dit ce qui est arrivé. Le groupe trouvera « sont arrivés ».")

    d.objectifs([
        "conjuguer le verbe être à l'imparfait, aux six personnes ;",
        "employer l'imparfait pour décrire une situation passée ;",
        "distinguer l'imparfait du passé composé ;",
        "écrire le décor d'un fait divers.",
    ])

    d.regle('La formation',
            "Le radical ét- et les terminaisons de l'imparfait.",
            precision="J'étais, tu étais, il était, nous étions, vous étiez, ils "
                      "étaient. Le radical ne change jamais ; seules les terminaisons "
                      "bougent, et ce sont celles de tous les verbes à l'imparfait.",
            notes="Écrire les six formes au tableau, en colonne. Faire remarquer que "
                  "trois d'entre elles se prononcent pareil : étais, était, étaient.")

    d.tableau('Analyse', "Être à l'imparfait",
              ['La personne', 'La forme', 'Un exemple'],
              [["je", "j'étais", "J'étais curieux de voir la sculpture."],
               ["tu", "tu étais", "Tu étais au concours samedi ?"],
               ["il, elle, on", "il était", "Il était 8 h quand ils sont arrivés."],
               ["nous", "nous étions", "Nous étions au chalet ce jour-là."],
               ["vous", "vous étiez", "Vous étiez nombreux à la remise des prix."],
               ["ils, elles", "ils étaient", "Les organisateurs étaient débordés."]],
              cle=1, props=[0.2, 0.22, 0.58],
              notes="Six formes, six exemples tirés du module. Faire lire à voix haute : "
                    "étais, était et étaient se disent de la même façon.")

    d.regle("À quoi sert l'imparfait",
            "Il décrit une situation, un décor, un état — pas un événement.",
            precision="« Il était 8 h » : le décor. « Les pompiers sont arrivés » : "
                      "l'événement. Dans un fait divers, l'imparfait plante la scène et "
                      "le passé composé raconte ce qui s'est passé.",
            notes="Diapo centrale de la séance. Faire chercher les deux temps dans le "
                  "texte du concours, en C1.")

    d.cartes('En apprendre plus', "Quatre emplois de l'imparfait", [
        ("L'heure et la date",
         "« Il était 8 h. » « C'était un samedi. » Toujours à l'imparfait, jamais au "
         "passé composé."),
        ("Le temps qu'il faisait",
         "« Il faisait froid. » « La neige était collante. » Le décor météo d'un fait "
         "divers est toujours à l'imparfait."),
        ("L'état des personnes",
         "« Le jury était impressionné. » « Les organisateurs étaient débordés. » Un "
         "état dure ; il n'est pas un événement."),
        ("Ce qui se passait déjà",
         "« Deux passants qui marchaient à proximité… » L'action était en cours quand "
         "l'événement est arrivé."),
    ], notes="La quatrième carte relie l'imparfait à « pendant que ». Le signaler à ceux "
             "qui ont fait le module 4.")

    d.pratique('Pratique · 1 de 4', "Conjuguez être à l'imparfait",
               "Regardez le sujet.", [
        ("Le jury ___ impressionné par les détails de la sculpture.", "était"),
        ("L'incendie s'est déclaré quand nous ___ au chalet.", "étions"),
        ("Il ___ 8 h quand les pompiers sont arrivés.", "était"),
        ("J'___ curieux de voir la sculpture gagnante.", "étais"),
        ("La semaine dernière, les organisateurs ___ débordés de travail.", "étaient"),
        ("Vous ___ au concours samedi ?", "étiez"),
    ], corrige=True,
       notes="Faire souligner le sujet avant d'écrire. Trois des six formes se "
             "prononcent pareil : c'est l'écrit qui les distingue.")

    d.pratique('Pratique · 2 de 4', "Décor ou événement ?",
               "L'imparfait décrit, le passé composé raconte.", [
        ("Il était 8 h du matin.", "décor — imparfait"),
        ("Les pompiers sont arrivés.", "événement — passé composé"),
        ("Il faisait très froid ce jour-là.", "décor — imparfait"),
        ("Le jury a remis le premier prix.", "événement — passé composé"),
        ("Les organisateurs étaient débordés.", "décor — imparfait"),
    ], corrige=True,
       notes="Exercice de classement. Faire remarquer que le décor est toujours à "
             "l'imparfait, sans exception, dans un fait divers.")

    d.piege("Le piège de l'heure",
            "Il a été 8 h quand les pompiers sont arrivés.",
            "Il était 8 h quand les pompiers sont arrivés.",
            "L'heure, la date et le temps qu'il faisait sont toujours à l'imparfait : ce "
            "ne sont pas des événements, ce sont des états. « Il a été 8 h » voudrait "
            "dire que 8 h est arrivé puis reparti.",
            notes="Erreur fréquente. La corriger en demandant : est-ce que 8 h est "
                  "arrivé, ou est-ce qu'il était déjà là ?")

    d.piege("Le piège des trois formes semblables",
            "Les organisateurs était débordés.",
            "Les organisateurs étaient débordés.",
            "« Étais », « était » et « étaient » se prononcent exactement pareil. À "
            "l'oral, personne ne peut vous corriger ; à l'écrit, l'erreur est très "
            "visible. Regardez le sujet, n'écoutez pas le verbe.",
            notes="Même logique qu'au module 1, séance C2, pour les verbes en -er. Le "
                  "rappeler.")

    d.pratique('Pratique · 3 de 4', "Complétez le fait divers",
               "Imparfait pour le décor, passé composé pour l'événement.", [
        ("Il ___ (être) 22 h et il ___ (faire) très froid.", "était · faisait"),
        ("Un feu ___ (se déclarer) dans un garage.", "s'est déclaré"),
        ("Le propriétaire ___ (dormir) à l'étage.", "dormait"),
        ("Les pompiers ___ (arriver) dix minutes plus tard.", "sont arrivés"),
        ("Personne ___ (ne être) blessé.", "n'a été"),
    ], corrige=True,
       notes="Le dernier item est au passé composé malgré le verbe être : c'est un "
             "événement, pas un état. Le corriger en dernier.")

    d.pratique('Pratique · 4 de 4', "Écrivez le décor",
               "Trois phrases à l'imparfait avant l'événement.", [
        ("L'heure et le jour", "Il était sept heures du matin, un samedi."),
        ("Le temps qu'il faisait", "Il faisait moins vingt et la neige était collante."),
        ("Les gens présents", "Les équipes étaient déjà sur la place du village."),
    ], corrige=True,
       notes="Faire ajouter ensuite une phrase au passé composé : l'événement. Le "
             "contraste entre les quatre phrases est parlant.")

    d.billet(
        "Écrivez le début d'un fait divers : trois phrases de décor, une d'événement.",
        exemples=[
            "Les trois premières à l'imparfait, la dernière au passé composé.",
            "L'heure, le temps qu'il faisait, les gens présents, puis ce qui est arrivé.",
        ],
        notes="Corriger le temps de chaque verbe. Rendre avant C3, où l'accord du "
              "participe passé reviendra.")

    return d.save(dossier)
