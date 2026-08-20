# -*- coding: utf-8 -*-
"""A2 · Toujours, souvent, jamais.
Bloc A « Je découvre » · couleur teal · 75 min.
Source : exercice `prFreq` et son encadré de savoir.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='teal',
        titre='Toujours, souvent, jamais',
        chapeau="Combien de fois ? En français, on répond souvent sans chiffre. "
                "Cinq petits mots suffisent — mais ils ne se placent pas "
                "n'importe où dans la phrase.",
        duree='75 minutes')

    d.titre(notes="Reprendre les billets de sortie de A1. Lire deux ou trois phrases à voix "
                  "haute, sans nommer leur auteur, et demander : combien de fois par semaine ?")

    d.objectifs([
        "employer toujours, souvent, parfois, rarement et jamais à bon escient ;",
        "placer l'adverbe après le verbe simple, et entre l'auxiliaire et le participe ;",
        "savoir que jamais réclame un ne devant le verbe ;",
        "répondre à la question « combien de fois ? » sans donner de chiffre.",
    ])

    d.tableau('Analyse · 1 de 2', "Du plus souvent au moins souvent",
              ['Adverbe', 'Ce que ça veut dire'],
              [["toujours", "chaque fois, sans exception"],
               ["souvent", "la plupart du temps"],
               ["parfois", "de temps en temps"],
               ["rarement", "presque pas"],
               ["jamais", "aucune fois"]],
              cle=4,
              notes="Faire lire la colonne de droite par le groupe, puis la cacher et "
                    "redemander le sens de chaque adverbe.")

    d.tableau('Analyse · 2 de 2', "Les mêmes, dans une phrase",
              ['Adverbe', 'Exemple'],
              [["toujours", "Julie est toujours la première arrivée."],
               ["souvent", "Je cuisine souvent le dimanche."],
               ["rarement", "Ils vont rarement au tournoi."],
               ["jamais", "Elle ne sort jamais le soir."]],
              cle=3,
              note="La dernière ligne est la seule qui change la phrase : jamais réclame un ne.",
              notes="Demander un exemple personnel pour chaque adverbe avant d'afficher "
                    "la colonne de droite.")

    d.regle('La place dans la phrase',
            "Avec un verbe simple, l'adverbe se met juste après le verbe.",
            precision="« Je cuisine souvent le dimanche » et non « Je souvent cuisine ». "
                      "C'est l'inverse de plusieurs langues, où l'adverbe précède le verbe. "
                      "L'erreur s'entend immédiatement à l'oral.",
            notes="Écrire les deux phrases au tableau et barrer la mauvaise devant le groupe.")

    d.regle('Au passé composé',
            "L'adverbe se glisse entre l'auxiliaire et le participe passé.",
            precision="« Je n'ai jamais joué au hockey. » · « Elle a souvent travaillé le "
                      "soir. » L'adverbe ne va ni avant l'auxiliaire, ni après le participe.",
            notes="Cette règle sera réutilisée telle quelle au bloc C, quand tout le récit "
                  "passera au passé composé. Le dire aux élèves : ça se paie deux fois.")

    d.piege('Le cas de jamais',
            "Elle sort jamais le soir.",
            "Elle ne sort jamais le soir.",
            "À l'oral, au Québec comme ailleurs, le « ne » tombe très souvent : on entend "
            "« a sort jamais le soir ». Ce n'est pas une faute d'écoute. Mais à l'écrit, le "
            "« ne » est obligatoire — et son absence est une des fautes les plus visibles.",
            notes="Insister : ce qu'on entend et ce qu'on écrit ne sont pas la même chose "
                  "ici. Les élèves qui apprennent surtout à l'oreille écrivent la forme "
                  "entendue.")

    d.pratique('Pratique · 1 de 2', "Quel adverbe ?",
               "Complétez chaque phrase avec l'adverbe qui convient au sens.", [
        ("Le jeudi, Mariama finit à quatre heures : elle arrive ___ à l'heure.", "toujours / souvent"),
        ("Les autres soirs, elle sort à six heures : elle n'arrive ___ à temps.", "jamais"),
        ("Chantal fait son ménage le dimanche. Elle le fait ___ le samedi.", "rarement / parfois"),
        ("Chantal décide à cinq heures et demie : c'est ___ la panique.", "toujours / souvent"),
        ("Le tournoi a lieu une fois par année : les joueuses y vont ___.", "rarement"),
        ("Julie déteste attendre : elle est ___ la première arrivée.", "toujours"),
    ], corrige=True,
       notes="Plusieurs réponses sont acceptables aux lignes 1, 3 et 4. Accepter et faire "
             "justifier : c'est le sens qui tranche, pas une clé unique.")

    d.pratique('Pratique · 2 de 2', "Remettre l'adverbe à sa place",
               "Réécrivez chaque phrase en plaçant correctement l'adverbe entre parenthèses.", [
        ("Je fais le lavage le soir. (souvent)", "Je fais souvent le lavage le soir."),
        ("Elle a travaillé de nuit. (jamais)", "Elle n'a jamais travaillé de nuit."),
        ("Nous sortons les ordures le mardi. (toujours)", "Nous sortons toujours les ordures le mardi."),
        ("Il a passé la balayeuse. (rarement)", "Il a rarement passé la balayeuse."),
        ("Ils vont au centre communautaire. (parfois)", "Ils vont parfois au centre communautaire."),
    ], corrige=True, cols=1,
       notes="Les lignes 2 et 4 sont au passé composé : c'est là que la place se joue. "
             "Faire venir deux élèves au tableau pour ces deux-là.")

    d.cartes('Pour aller plus loin', "Trois façons de dire combien de fois", [
        ("Avec un adverbe",
         "« Je cuisine souvent le dimanche. » Court, naturel, sans chiffre. C'est ce qu'on "
         "emploie le plus dans une conversation."),
        ("Avec une fréquence chiffrée",
         "« Trois fois par semaine », « une fois par mois », « deux soirs sur trois ». "
         "Plus précis, utile quand la précision compte."),
        ("Avec un jour",
         "« Le jeudi » — avec l'article — veut dire tous les jeudis. Sans article, "
         "« jeudi » désigne un seul jeudi, celui qui vient."),
    ], notes="La troisième carte est une vraie difficulté : « je joue le jeudi » (chaque "
             "semaine) contre « je joue jeudi » (cette semaine). Faire produire les deux "
             "phrases par le groupe.")

    d.billet(
        "Écrivez quatre phrases sur vous, une par adverbe : toujours, souvent, rarement, jamais.",
        exemples=[
            "Une des quatre doit être au passé composé.",
            "Exemple : « Je n'ai jamais travaillé de nuit. »",
        ],
        notes="Corriger surtout la place de l'adverbe et le « ne » de jamais. Rendre à la "
              "séance suivante.")

    return d.save(dossier)
