# -*- coding: utf-8 -*-
"""B2 · Faire des comparaisons.
Bloc B · couleur ambre (écriture) · 75 min.
Source : exercice `t1compare` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Faire des comparaisons',
        chapeau="« Plus courte que », « moins cher que », « plus vite que ». Trois mots "
                "et deux éléments comparés : c'est la construction dont Solange et Omar "
                "se servent d'un bout à l'autre du dialogue.",
        duree='75 minutes')

    d.titre(notes="Relire le dialogue de B1 et faire souligner toutes les comparaisons. "
                  "Il y en a quatre : c'est le point de départ.")

    d.objectifs([
        "construire une comparaison avec plus… que et moins… que ;",
        "comparer avec un adjectif et avec un adverbe ;",
        "repérer les deux éléments comparés ;",
        "employer « celui de » et « celle de » pour éviter une répétition.",
    ])

    d.regle('La règle',
            "Plus ou moins + le mot + que + le deuxième élément.",
            precision="« La capsule de la friperie est plus courte que celle de la "
                      "cuisine collective. » Le mot au milieu peut être un adjectif "
                      "(courte) ou un adverbe (vite). La construction ne change pas.",
            notes="Écrire la formule au tableau : PLUS/MOINS + mot + QUE + élément. Elle "
                  "vaut pour tous les exercices.")

    d.tableau('Analyse', "Avec un adjectif ou un adverbe",
              ['Le type', 'Un exemple'],
              [["adjectif", "La capsule est plus courte que l'affiche."],
               ["adjectif", "L'annonce est moins chère que la publicité du journal."],
               ["adverbe", "À la friperie, on parle plus vite que sur l'autre capsule."],
               ["adverbe", "Les bénévoles arrivent plus tôt que ceux du dimanche."]],
              cle=0, props=[0.2, 0.8],
              note="L'adjectif décrit une chose ; l'adverbe décrit une action. La "
                   "construction reste la même.",
              notes="Ne pas insister sur la distinction adjectif et adverbe : elle "
                    "n'change rien à la construction. La mentionner et passer.")

    d.tableau('Analyse', "Les deux éléments comparés",
              ['La phrase', 'Élément 1', 'Élément 2'],
              [["La radio du quartier rejoint moins d'auditeurs que la radio de la ville.",
                "la radio du quartier", "la radio de la ville"],
               ["L'affiche coûte moins cher que l'annonce dans le journal.",
                "l'affiche", "l'annonce dans le journal"],
               ["Le grille-pain de Solange est plus vieux que celui d'Omar.",
                "le grille-pain de Solange", "celui d'Omar"]],
              cle=0, props=[0.48, 0.26, 0.26],
              notes="Le premier élément est avant le verbe, le second après « que ». "
                    "C'est mécanique.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("« Celui de », « celle de »",
         "« Le grille-pain de Solange est plus vieux que celui d'Omar. » On évite de "
         "répéter « le grille-pain » : « celui » le remplace."),
        ("« Ceux de », « celles de »",
         "Au pluriel : « les bénévoles du samedi arrivent plus tôt que ceux du "
         "dimanche »."),
        ("Bon devient meilleur",
         "On ne dit pas « plus bon » : on dit « meilleur ». « Cette capsule est "
         "meilleure que l'autre. »"),
        ("Bien devient mieux",
         "On ne dit pas « plus bien » : on dit « mieux ». « On comprend mieux la "
         "deuxième capsule. »"),
    ], notes="Les deux dernières cartes sont les seules exceptions du système. Les "
             "signaler clairement : tout le reste suit la règle.")

    d.pratique('Pratique · 1 de 4', "Trouvez les deux éléments comparés",
               "Le premier avant le verbe, le second après « que ».", [
        ("La radio du quartier rejoint moins d'auditeurs que la radio de la ville.",
         "la radio du quartier et la radio de la ville"),
        ("L'affiche du babillard coûte moins cher que l'annonce dans le journal.",
         "l'affiche du babillard et l'annonce dans le journal"),
        ("Le grille-pain de Solange est plus vieux que celui d'Omar.",
         "le grille-pain de Solange et celui d'Omar"),
        ("Les bénévoles du samedi arrivent plus tôt que ceux du dimanche.",
         "les bénévoles du samedi et ceux du dimanche"),
        ("Une lampe réparée dure plus longtemps qu'une lampe achetée à rabais.",
         "une lampe réparée et une lampe achetée à rabais"),
    ], corrige=True,
       notes="Faire souligner les deux éléments dans chaque phrase. Le motif est toujours "
             "le même.")

    d.pratique('Pratique · 2 de 4', "Écrivez la comparaison",
               "Plus ou moins, selon le sens.", [
        ("la capsule à la radio — l'affiche du babillard",
         "La capsule à la radio est plus courte que l'affiche du babillard."),
        ("réparer un appareil — acheter un appareil neuf",
         "Réparer un appareil coûte moins cher qu'acheter un appareil neuf."),
        ("la capsule de la friperie — celle de la cuisine collective",
         "La capsule de la friperie est moins claire que celle de la cuisine collective."),
        ("les bénévoles du samedi — ceux du dimanche",
         "Les bénévoles du samedi arrivent plus tôt que ceux du dimanche."),
    ], corrige=True,
       notes="Accepter toute comparaison correcte. Vérifier une seule chose : la "
             "construction, et la présence de « que ».")

    d.piege("Le piège du « que » oublié",
            "La capsule est plus courte l'affiche.",
            "La capsule est plus courte que l'affiche.",
            "Le mot « que » relie les deux éléments comparés. Sans lui, la phrase reste "
            "en suspens : on ne sait pas par rapport à quoi. C'est l'oubli le plus "
            "fréquent, et il vient de langues où ce mot n'existe pas.",
            notes="Faire relire les quatre phrases de l'exercice précédent en vérifiant "
                  "uniquement la présence de « que ».")

    d.piege("Le piège de « plus bon »",
            "Cette capsule est plus bonne que l'autre.",
            "Cette capsule est meilleure que l'autre.",
            "« Bon » et « bien » ont des formes de comparaison à part : meilleur et "
            "mieux. Ce sont les deux seules exceptions du système, et elles sont très "
            "fréquentes — il faut donc les apprendre par cœur.",
            notes="Faire produire deux phrases avec « meilleur » et deux avec « mieux ». "
                  "La distinction entre les deux vaut la peine d'être travaillée.")

    d.pratique('Pratique · 3 de 4', "Meilleur ou mieux ?",
               "Meilleur décrit une chose, mieux décrit une action.", [
        ("Cette capsule est ___ que l'autre.", "meilleure"),
        ("On comprend ___ la deuxième capsule.", "mieux"),
        ("La musique est ___ réglée sur celle de la cuisine collective.", "mieux"),
        ("C'est le ___ slogan des trois.", "meilleur"),
    ], corrige=True,
       notes="Le critère : y a-t-il un nom après ? Alors « meilleur ». Y a-t-il un "
             "verbe ? Alors « mieux ».")

    d.pratique('Pratique · 4 de 4', "Comparez deux publicités",
               "Trois comparaisons, sur trois critères différents.", [
        ("La durée", "La capsule radio est plus courte que l'affiche."),
        ("Le coût", "L'affiche coûte moins cher que l'annonce dans le journal."),
        ("La portée", "La radio rejoint plus de gens que le babillard."),
        ("La clarté", "L'affiche est plus claire que la capsule, parce qu'on peut la relire."),
    ], corrige=True,
       notes="Ces quatre comparaisons sont celles qu'on emploie pour choisir un canal. "
             "Elles serviront en E1.")

    d.billet(
        "Écrivez trois comparaisons sur deux publicités que vous connaissez.",
        exemples=[
            "Une avec un adjectif, une avec un adverbe, une avec « meilleur » ou "
            "« mieux ».",
            "Soulignez les deux éléments comparés dans chacune.",
        ],
        notes="Corriger la construction et la présence de « que ». Rendre avant B3, où "
              "l'on comparera des slogans.")

    return d.save(dossier)
