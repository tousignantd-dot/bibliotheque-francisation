# -*- coding: utf-8 -*-
"""B4 · Le jour du camion.
Bloc B « Défi 1 · Le camion » · couleur ambre · 75 min.
Source : dialogue `t1b`, exercices `t1bvf` et `t1imper`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-emmenagement/images/')


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Le jour du camion",
        chapeau="Six heures de travail se dirigent en trois mots : "
                "« Montez-le », « Ne la posez pas là ».",
        duree='75 minutes')

    d.titre(notes="Séance la plus concrète du bloc B. Si le local le permet, faire "
                  "déplacer de vraies boîtes : les directives se comprennent en les "
                  "exécutant.")

    d.objectifs([
        "comprendre les directives données le jour d'un déménagement ;",
        "former l'impératif avec un pronom, à l'affirmative ;",
        "placer le pronom devant le verbe à la négative ;",
        "dire où va chaque chose sans hésiter.",
    ])

    d.declencheur(
        'Observation', "Le camion est devant la porte. Qui décide où vont les "
                       "boîtes ?",
        image=IMG + 'escalier-exterieur.jpg',
        pistes=[
            "Les déménageurs le savent-ils ?",
            "Qui connaît le logement ?",
            "Que se passe-t-il si personne ne dit rien ?",
            "Combien de mots faut-il pour le dire ?",
        ],
        notes="La réponse est toujours la même : c'est vous qui savez. Beaucoup d'élèves "
              "n'osent pas donner de directives à des travailleurs québécois. Nommer "
              "cette gêne : elle coûte une heure de camion.")

    d.dialogue('Dialogue · 1 de 2', "Par les meubles", [
        ("PATRICIA", "On commence par quoi ? Les meubles ou les boîtes ?", True),
        ("AMADOU", "Par les meubles, s'il vous plaît. Après, on remplira les trous "
                   "avec les boîtes.", True),
        ("PATRICIA", "D'accord. Le divan, on le monte tout de suite ?", True),
        ("AMADOU", "Montez-le, oui, mais faites attention au coin de l'escalier. "
                   "Il tourne serré.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="« Montez-le, oui, mais… » : la directive, puis la précaution. C'est le "
             "modèle à faire reproduire tout au long de la séance.")

    d.dialogue('Dialogue · 2 de 2', "Celle-là dans la cuisine", [
        ("AMADOU", "Dans la chambre du fond, celle qui donne sur la ruelle. Ne le "
                   "posez pas dans le salon, on ne pourra plus passer.", True),
        ("AMADOU", "Cette boîte-ci, avec le point rouge, c'est la vaisselle. Ne la "
                   "mettez pas en dessous des autres.", True),
        ("PATRICIA", "Les points rouges, on les garde sur le dessus. Vous avez bien "
                     "fait de les marquer.", True),
        ("AMADOU", "Celles-là aussi, dans la cuisine. Ce sont les casseroles et le "
                   "petit four.", True),
    ], notes="Les démonstratifs apparaissent ici pour la première fois : « cette boîte-ci », "
             "« celles-là ». Ils seront travaillés en C2. Les signaler sans les expliquer.")

    d.regle("À l'affirmative, le pronom passe derrière",
            "Montez-le. Démontez-la. Mettez-les dans la cuisine.",
            precision="Avec un trait d'union, toujours. Et « me » devient « moi » : "
                      "donnez-moi la clé, jamais « donnez-me ».",
            notes="Le trait d'union n'est pas décoratif : c'est lui qui montre que le "
                  "pronom appartient au verbe.")

    d.regle("À la négative, le pronom revient devant",
            "Ne la mettez pas dans le salon. Ne les montez pas tout de suite.",
            precision="Pas de trait d'union, et le pronom se glisse entre « ne » et le "
                      "verbe. Autrement dit : à l'affirmative il saute derrière, à la "
                      "négative il reprend sa place normale.",
            notes="Diapositive à photographier avec la précédente. C'est la règle qui se "
                  "trompe le plus, et les deux se retiennent ensemble ou pas du tout.")

    d.piege("Garder le pronom derrière à la négative",
            "Ne mettez-la pas dans le salon.",
            "Ne la mettez pas dans le salon.",
            "Le même verbe a deux formes selon qu'on dit oui ou non. C'est une des rares "
            "irrégularités vraiment gênantes du français, et elle s'entend tout de suite "
            "chez un déménageur.",
            notes="Faire alterner affirmative et négative sur le même verbe, dix fois de "
                  "suite : montez-le / ne le montez pas.")

    d.pratique('Transformation', "Donnez la directive",
               "L'enseignante lit la phrase ; le groupe la redit à l'impératif.", [
        ("Vous montez le divan.", "Montez-le."),
        ("Vous démontez la table.", "Démontez-la."),
        ("Vous mettez les boîtes dans la cuisine.", "Mettez-les dans la cuisine."),
        ("Vous ne posez pas le matelas dans le salon.", "Ne le posez pas dans le salon."),
        ("Vous me donnez la clé.", "Donnez-moi la clé."),
        ("Vous ne mettez pas la vaisselle en dessous.", "Ne la mettez pas en dessous."),
    ], corrige=True,
       notes="C'est le laboratoire de la mini-leçon t1imper. Comparer la première et la "
             "quatrième : même verbe, deux places pour le pronom.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("On commence par les boîtes, puis on monte les meubles.",
         "faux — par les meubles"),
        ("Le matelas va dans la chambre qui donne sur la ruelle.", "vrai"),
        ("Les boîtes marquées d'un point rouge contiennent la vaisselle.", "vrai"),
        ("On met les boîtes fragiles en dessous des autres.", "faux — sur le dessus"),
        ("La table passe entière dans la porte du deuxième.", "faux — il faut la démonter"),
        ("Amadou demande de laisser passer le voisin dans l'escalier.", "vrai"),
    ], corrige=True,
       notes="La dernière ligne prépare le défi 3 : c'est déjà du voisinage.")

    d.billet(
        "Écrivez cinq directives pour le jour de votre déménagement.",
        exemples=[
            "Trois à l'affirmative, deux à la négative.",
            "Chacune avec un pronom : « Montez-le », « Ne la posez pas là ».",
        ],
        notes="Ramasser les billets : ils montrent tout de suite qui a compris la double "
              "place du pronom.")

    return d.save(dossier)
