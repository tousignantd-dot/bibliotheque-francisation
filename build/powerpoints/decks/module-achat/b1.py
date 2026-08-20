# -*- coding: utf-8 -*-
"""B1 · Ce modèle-ci ou celui-là ?
Bloc B « Défi 1 · S'informer sur l'appareil » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1compare`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Ce modèle-ci ou celui-là ?',
        chapeau="Deux laveuses presque identiques, cent dollars d'écart. Ce "
                "qui les sépare tient en deux chiffres — encore faut-il savoir "
                "quoi demander.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Écrire au tableau : « qu'est-ce qui justifie cent "
                  "dollars ? ». C'est la question de toute la séance.")

    d.objectifs([
        "demander ce qui distingue deux modèles ;",
        "comprendre ce que veut dire « capacité » ;",
        "calculer si un appareil plus cher revient moins cher à l'usage ;",
        "savoir jusqu'à quand un rabais est valable.",
    ])

    d.declencheur(
        'Mise en situation', "Deux appareils se ressemblent, mais l'un coûte cent dollars de plus. Que demandez-vous ?",
        pistes=[
            "Quelle est votre première question ?",
            "Comment savoir si l'écart vaut la peine ?",
            "Sur combien d'années faut-il calculer ?",
            "Le moins cher est-il toujours le meilleur choix ?",
        ],
        notes="Cinq minutes. La troisième piste est celle qu'on n'a pas le réflexe de "
              "poser : un appareil se garde dix ans.")

    d.dialogue('Dialogue · 1 de 3', "Ce qui les distingue", [
        ("YIN", "Quelle est la différence entre ce modèle-ci et celui-là ? Ils se ressemblent beaucoup.", True),
        ("MARTIN", "Presque tout est pareil. Deux choses changent : la capacité et la consommation d'eau.", True),
        ("YIN", "La capacité, ça veut dire quoi exactement ?", True),
        ("MARTIN", "Combien de linge entre dedans. Celui-ci prend quatre kilos et demi, celui-là cinq kilos et demi.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Quatre répliques teintées : la question de comparaison, la réponse, la "
             "demande de définition, la définition. C'est le modèle exact de l'échange.")

    d.dialogue('Dialogue · 2 de 3', "Ce que ça change vraiment", [
        ("YIN", "Un kilo de plus, ça change quoi pour nous ?", True),
        ("MARTIN", "Environ une brassée de moins par semaine, pour une famille de quatre.", False),
        ("YIN", "Et l'eau ?", False),
        ("MARTIN", "Le modèle plus cher consomme trente litres de moins par brassée. Sur cinq ans, ça compense la différence de prix.", True),
    ], notes="« Ça change quoi pour nous ? » est la meilleure question du dialogue : elle "
             "ramène le chiffre à la vie réelle. La faire répéter.")

    d.dialogue('Dialogue · 3 de 3', "La garantie et le rabais", [
        ("YIN", "Ils sont garantis pareil ?", False),
        ("MARTIN", "Un an tous les deux, pièces et main-d'œuvre. La garantie prolongée est offerte sur les deux.", False),
        ("YIN", "Celui-ci est en spécial jusqu'à quand ?", True),
        ("MARTIN", "Jusqu'à dimanche. Après, il remonte de cent dollars.", True),
    ], notes="La dernière question décide s'il faut acheter aujourd'hui. Peu de gens la "
             "posent, et elle change souvent le calcul.")

    d.tableau('Analyse', "Les six questions du rayon",
              ['La question', 'Ce qu\'elle apprend'],
              [["Il fait quelles dimensions ?", "s'il entre, porte ouverte comprise"],
               ["Quelle est la capacité ?", "ce qui entre dedans"],
               ["Il est bruyant ?", "si je l'entendrai de l'étage"],
               ["Il consomme combien ?", "ce qu'il coûtera chaque mois"]],
              cle=0,
              note="Deux autres : « quelle est la différence ? » et « le spécial finit quand ? »",
              notes="Diapo centrale. Faire recopier : c'est la liste de vérification du "
                    "bloc B.")

    d.regle("Calculer sur la durée de vie",
            "Un appareil se garde dix ans. Cent dollars d'écart, c'est dix dollars par an.",
            precision="Trente litres d'eau de moins par brassée, trois brassées par "
                      "semaine, sur cinq ans : l'économie dépasse l'écart de prix. Le "
                      "modèle plus cher revient moins cher. Ce raisonnement vaut pour tous "
                      "les gros appareils.",
            notes="Faire le calcul au tableau avec le groupe. C'est de l'arithmétique "
                  "simple, et elle change les décisions.")

    d.piege("Comparer seulement les prix affichés",
            "Celui-là coûte cent dollars de moins, je le prends.",
            "Il consomme trente litres de plus par brassée. Sur cinq ans, il coûte davantage.",
            "Le prix d'achat n'est qu'une partie du coût. L'eau, l'électricité et les "
            "réparations s'ajoutent année après année. Pour un appareil qu'on garde dix "
            "ans, c'est le coût d'usage qui décide.",
            notes="Ne pas transformer cela en règle absolue : sur un budget serré, le prix "
                  "d'achat peut primer, et c'est légitime. Le dire.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Trois choses différencient les deux modèles.", "faux — deux"),
        ("La capacité, c'est la quantité de linge qui entre.", "vrai"),
        ("Le premier prend cinq kilos et demi.", "faux — quatre et demi"),
        ("Le modèle plus cher consomme plus d'eau.", "faux — trente litres de moins"),
        ("Les deux ont la même garantie.", "vrai"),
        ("Le spécial se termine dimanche.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Comparez deux appareils du même type et écrivez quatre phrases.",
        exemples=[
            "Ce qui les distingue, et ce que ça change pour vous.",
            "Terminez par votre choix, avec sa raison.",
        ],
        notes="Ramasser. Ces comparaisons servent au jeu de rôle de E1.")

    return d.save(dossier)
