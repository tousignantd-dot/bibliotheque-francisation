# -*- coding: utf-8 -*-
"""C4 · Lire l'affichette, entendre la mesure.
Bloc C « Défi 2 · Trouver le rayon et demander » · couleur teal · 60 min.
Source : exercices `t2affichette` et `t2mesures`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-electro/images/')


def build(dossier):
    d = Deck(
        code='C4', section='teal',
        titre="Lire l'affichette",
        chapeau="Le petit carton devant l'appareil répète la circulaire et "
                "ajoute une chose qu'elle ne dit pas toujours : le format, en "
                "pouces. C'est lui qui décide si l'appareil entre chez vous.",
        duree='60 minutes')

    d.titre(notes="Séance de lecture et d'écoute. Prévoir un ruban à mesurer : les "
                  "pouces se comprennent en les montrant, pas en les expliquant.")

    d.objectifs([
        "lire les cinq lignes d'une affichette de rayon ;",
        "comprendre une mesure en pouces et en pieds cubes ;",
        "distinguer à l'oreille un prix d'une mesure ;",
        "vérifier qu'un appareil entre chez soi.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui est écrit sur le petit carton ?",
        image=IMG + 'affichette-appareil.jpg',
        pistes=[
            "Combien de lignes voyez-vous ?",
            "Laquelle est le prix ?",
            "Qu'est-ce que veut dire « 27 po » ?",
            "Qu'est-ce qui n'est pas écrit dessus ?",
        ],
        notes="Faire deviner avant d'expliquer. Le mot « po » pour pouce est une "
              "abréviation que personne ne devine seul : la donner après.")

    d.tableau('Analyse', "Les cinq lignes d'une affichette",
              ['La ligne', 'Ce qu\'elle donne'],
              [["Norlac", "la marque"],
               ["LT 4200", "le modèle exact"],
               ["27 po de large", "la place que l'appareil prend"],
               ["849 $", "le prix de cette semaine"],
               ["Rég. 1 049 $", "le prix des autres semaines"]],
              cle=1,
              note="« Livraison en sus » est écrit plus bas, en plus petit.",
              notes="Diapo à photographier. Faire remarquer que l'affichette répète la "
                    "circulaire : c'est voulu, et ça permet de vérifier sur place.")

    d.cartes("Les mesures d'ici", "Trois unités à reconnaître", [
        ("le pouce",
         "La largeur et la hauteur d'un appareil : 27 pouces de large, 66 pouces de "
         "haut. On écrit « po ». Un pouce fait un peu plus de deux centimètres et demi."),
        ("le pied cube",
         "Le volume d'un réfrigérateur ou d'une laveuse : 18 pieds cubes. On écrit "
         "« pi³ ». Plus le chiffre est gros, plus l'appareil contient."),
        ("le watt",
         "La puissance d'un micro-ondes : 1 000 watts. Plus il y a de watts, plus ça "
         "chauffe vite."),
    ], cols=3,
       notes="Montrer un pouce sur le ruban à mesurer, puis 27 pouces contre le mur de "
             "la classe. La mesure devient concrète en dix secondes.")

    d.pratique('Écoute', "Un prix ou une mesure ?",
               "Écoutez et dites ce que vous entendez.", [
        ("huit cent quarante-neuf dollars", "un prix"),
        ("vingt-sept pouces de large", "une mesure"),
        ("cent vingt-neuf dollars", "un prix"),
        ("soixante-six pouces de haut", "une mesure"),
        ("mille quarante-neuf dollars", "un prix"),
        ("dix-huit pieds cubes", "une mesure"),
    ], corrige=True,
       notes="Dire chaque énoncé deux fois, sans le montrer. C'est le mot de la fin — "
             "dollars, pouces, pieds cubes — qui donne la réponse : le faire remarquer "
             "après le premier tour.")

    d.regle("Mesurer avant de partir",
            "« J'ai vingt-huit pouces entre le mur et la porte. »",
            precision="Un appareil trop large revient au magasin, et le "
                      "transport se paie deux fois. Le chiffre se prend chez "
                      "soi, il s'écrit sur un papier, et il se garde dans la "
                      "poche.",
            notes="Diapo à photographier. Faire ressortir le chiffre relevé au devoir de "
                  "A3 : chacun devrait l'avoir dans son cahier.")

    d.piege("Se fier à l'apparence",
            "« Elle a l'air de la même grandeur. »",
            "Elle fait combien de large ?",
            "Deux laveuses côte à côte peuvent avoir trois pouces de différence, et "
            "trois pouces suffisent à empêcher la porte de fermer. La question coûte "
            "cinq secondes ; l'erreur coûte une livraison.",
            notes="Raconter, si le groupe est réceptif, un cas réel : la plupart des "
                  "classes en ont un.")

    d.pratique('Lecture', "Répondez d'après l'affichette",
               "Marque Norlac, modèle LT 4200, 27 po de large, 849 $, rég. 1 049 $.", [
        ("Quelle est la marque ?", "Norlac"),
        ("Quel est le modèle ?", "LT 4200"),
        ("Combien de large ?", "27 pouces"),
        ("Combien ça coûte cette semaine ?", "849 $"),
    ], corrige=True,
       notes="Poser les questions à l'oral, sans projeter l'affichette. Les élèves "
             "répondent de mémoire : c'est la situation réelle du magasin.")

    d.billet(
        "Écrivez les cinq lignes de l'affichette de l'appareil que vous voulez.",
        exemples=[
            "La marque, le modèle, le format, les deux prix.",
            "Ajoutez la mesure que vous avez prise chez vous.",
        ],
        notes="Devoir de préparation. Cette fiche sert de point de départ à la "
              "production écrite de E1.")

    return d.save(dossier)
