# -*- coding: utf-8 -*-
"""A2 · « Un » et « pain ».
Bloc A « Je découvre » · couleur teal · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='teal',
        titre='« Un » et « pain »',
        chapeau="Deux voyelles nasales que beaucoup de francophones ont "
                "fondues en une seule — mais qui restent bien distinctes ici. "
                "Et « un » revient dans presque chaque phrase.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute. Prévoir le son. Commencer en disant « un » puis "
                  "« pain » lentement, en montrant les lèvres : la différence se voit "
                  "avant de s'entendre.")

    d.objectifs([
        "distinguer à l'oreille le son de « un » et celui de « pain » ;",
        "savoir que la graphie décide : un, um d'un côté ; in, ain, ein, im de l'autre ;",
        "produire le son de « un » avec les lèvres arrondies ;",
        "reconnaître ces sons dans les mots du magasin.",
    ])

    d.tableau('Analyse', "Deux sons, deux positions de lèvres",
              ['Le son', 'Les lèvres', 'Comme dans'],
              [["celui de « un »", "arrondies, avancées", "un, brun, lundi"],
               ["celui de « pain »", "étirées, en sourire", "pain, brin, magasin"]],
              cle=0,
              note="La différence se voit sur le visage de celui qui parle.",
              notes="Diapo centrale. Faire produire les deux par tout le groupe, en se "
                    "regardant. L'effet de miroir aide beaucoup.")

    d.regle("La graphie décide",
            "un et um d'un côté ; in, ain, ein, im, aim de l'autre.",
            precision="Le son de « un » ne s'écrit que <b>un</b> ou <b>um</b> : un, brun, "
                      "lundi, chacun, aucun, parfum. Tout le reste se dit comme « pain ». "
                      "C'est une des rares règles d'orthographe française sans exception "
                      "utile.",
            notes="Diapo à photographier. Elle dispense de deviner à l'oreille : la façon "
                  "d'écrire donne la réponse.")

    d.cartes('La courte liste', "Les mots du son « un »", [
        ("un, aucun, chacun",
         "Les trois plus fréquents. « Un » à lui seul revient dans presque chaque phrase."),
        ("brun, lundi",
         "Deux mots du quotidien. « Lundi » est le seul jour de la semaine dans cette "
         "famille."),
        ("parfum, humble",
         "Plus rares, mais ils s'écrivent avec <b>um</b> — d'où le son."),
        ("Tout le reste",
         "magasin, linge, certain, plein, important, simple, matin : tous du côté de "
         "« pain »."),
    ], notes="La quatrième carte rassure : la famille de « un » est très petite. Il suffit "
             "de la connaître.")

    d.piege("Deviner à l'oreille",
            "Je n'entends pas la différence, je ne sais pas lequel dire.",
            "Je regarde comment le mot s'écrit : un/um, ou in/ain/ein/im.",
            "Vous n'avez pas à deviner. L'orthographe donne la réponse à tous les coups, et "
            "vous connaissez déjà l'orthographe des mots que vous employez. Entendre la "
            "différence viendra avec le temps.",
            notes="Le dire clairement : beaucoup d'élèves se découragent sur les voyelles "
                  "nasales. La règle graphique leur donne prise tout de suite.")

    d.pratique('Pratique · 1 de 2', "Quel son ?",
               "Écoutez chaque mot.", [
        ("un", "comme « un » — lèvres arrondies"),
        ("pain", "comme « pain » — lèvres étirées"),
        ("brun", "comme « un »"),
        ("brin", "comme « pain »"),
        ("lundi", "comme « un »"),
        ("magasin", "comme « pain »"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module. Deux écoutes avant de corriger.")

    d.pratique('Pratique · 2 de 2', "D'après la graphie",
               "Sans écouter : lequel des deux sons, d'après l'orthographe ?", [
        ("chacun", "un › son de « un »"),
        ("certain", "ain › son de « pain »"),
        ("aucun", "un › son de « un »"),
        ("important", "im › son de « pain »"),
        ("parfum", "um › son de « un »"),
        ("plein", "ein › son de « pain »"),
    ], corrige=True,
       notes="Cet exercice est le plus utile : il montre que la règle graphique suffit, "
             "sans écoute.")

    d.cartes('Pourquoi ça compte ici', "Une particularité du Québec", [
        ("La distinction se maintient",
         "Beaucoup de francophones d'Europe prononcent « un » comme « in ». Ici, les deux "
         "sons restent distincts, et cela s'entend."),
        ("On vous comprendra quand même",
         "Prononcer « un » comme « in » ne gêne pas la compréhension. Ce n'est pas une "
         "faute à corriger d'urgence."),
        ("Mais l'entendre aide à comprendre",
         "Reconnaître les deux sons, c'est mieux distinguer « un » de « hein », « brun » "
         "de « brin » — et suivre plus facilement ce qu'on vous dit."),
    ], notes="Cadrer l'objectif : la compréhension d'abord, la production ensuite. C'est "
             "aussi ce que demande le programme.")

    d.billet(
        "Relevez cinq mots contenant un de ces deux sons, entendus cette semaine.",
        exemples=[
            "Écrivez-les, puis classez-les d'après leur orthographe.",
            "Un mot de la famille de « un » vaut deux mots de l'autre famille.",
        ],
        notes="La dernière consigne est ludique et juste : les mots du son « un » sont "
              "rares et méritent d'être repérés.")

    return d.save(dossier)
