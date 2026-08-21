# -*- coding: utf-8 -*-
"""A2 · La fin des mots : le son « é ».
Bloc A « Je découvre » · couleur indigo · 75 min.
Source : exercice `prSons`, mini-leçon `prSons`.

La séance de graphie-phonie du module. Le programme du niveau 2 demande de
relier une graphie à son son ; la salle de classe l'offre tout fait, parce
que toutes ses consignes finissent par la même chose : ouvr-ez, ferm-ez,
écout-ez.

Le gabarit de diapositives est en Verdana : ni alphabet phonétique, ni
flèches. Le son se dit donc en toutes lettres — « é », entre guillemets — et
les symboles restent dans le module interactif.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-classe/images/')


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="La fin des mots : le son « é »",
        chapeau="Quand un mot de la classe finit par « é », c'est presque "
                "toujours une consigne, et elle est pour vous.",
        duree='75 minutes')

    d.titre(notes="Séance d'oreille avant tout. Parler peu, faire écouter beaucoup. "
                  "Certains élèves n'entendront pas la différence au premier cours : "
                  "elle vient avec la répétition, pas avec l'explication.")

    d.objectifs([
        "entendre le son « é » à la fin d'un mot ;",
        "reconnaître une consigne à sa terminaison ;",
        "distinguer « ouvrez » et « j'ouvre » ;",
        "écrire correctement la terminaison -ez.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui change entre ces deux phrases ?",
        image=IMG + 'tableau-classe.jpg',
        pistes=[
            "Écoutez : « Ouvrez votre cahier. »",
            "Écoutez : « J'ouvre mon cahier. »",
            "Est-ce que c'est la même personne qui parle ?",
            "Qu'est-ce qui vous l'a dit ?",
        ],
        notes="Dire les deux phrases plusieurs fois, lentement, sans expliquer. Laisser "
              "le groupe chercher. La règle vient après l'oreille, jamais avant.")

    d.tableau('Analyse', "Trois façons d'écrire, un seul son",
              ["Ce qui est écrit", "Ce qu'on entend"],
              [["ouvrez, fermez, écoutez", "« ouvré », « fermé », « écouté »"],
               ["effacer, répéter", "« effacé », « répété »"],
               ["un cahier, la clé", "« cahié », « clé »"],
               ["j'ouvre, une gomme", "rien à la fin"]],
              cle=2,
              note="Le z et le r de la fin ne s'entendent jamais dans ces mots.",
              notes="Diapositive à photographier. Faire lire la colonne de gauche et dire "
                    "la colonne de droite : c'est l'exercice, en une page.")

    d.regle("La terminaison -ez se dit « é »",
            "Le z se voit, il ne s'entend pas.",
            precision="Toutes les consignes de la classe finissent ainsi : "
                      "ouvr<b>ez</b>, ferm<b>ez</b>, écout<b>ez</b>, pren<b>ez</b>, "
                      "écriv<b>ez</b>. Les lettres <b>-er</b> et <b>-é</b> font le même "
                      "son : effac<b>er</b>, la cl<b>é</b>.",
            notes="Diapositive à photographier. Faire dire les cinq consignes deux fois "
                  "chacune, en chœur puis un par un.")

    d.piege('Le piège du jour',
            "« ouvrez-ze »",
            "« ouvré »",
            "Le z de la fin est muet. Beaucoup d'élèves le prononcent parce qu'ils "
            "le voient — et le mot devient impossible à reconnaître pour un locuteur "
            "du Québec. Le même piège vaut pour le r de « effacer ».",
            notes="Faire entendre les deux versions, la fausse d'abord, la juste ensuite. "
                  "Le groupe rit, et il retient.")

    d.pratique('Écoute', "« é » ou pas « é » ?",
               "Écoutez chaque mot et dites si la fin sonne « é ».", [
        ("ouvrez", "oui — « ouvré »"),
        ("j'ouvre", "non — rien à la fin"),
        ("écoutez", "oui — « écouté »"),
        ("j'écoute", "non — rien à la fin"),
        ("un cahier", "oui — « cahié »"),
        ("une gomme", "non — rien à la fin"),
        ("répéter", "oui — « répété »"),
        ("une feuille", "non — rien à la fin"),
    ], corrige=True, cols=2,
       notes="Huit mots, dits lentement, deux fois chacun. Les élèves lèvent la main "
             "quand ils entendent « é » : on voit tout de suite qui suit.")

    d.pratique('Pratique · à deux', "Le jeu des deux phrases",
               "Deux par deux. L'un dit, l'autre devine.", [
        ("Étape 1", "L'un choisit : « Ouvrez le cahier » ou « J'ouvre le cahier »."),
        ("Étape 2", "Il le dit à voix haute, une seule fois."),
        ("Étape 3", "L'autre dit qui parle : l'enseignante, ou l'élève ?"),
        ("Étape 4", "On change de rôle, avec fermer, écouter, effacer."),
    ], cols=1,
       notes="Vingt minutes. Le jeu marche parce que les deux phrases ne diffèrent que "
             "par la dernière syllabe : il n'y a rien d'autre à écouter.")

    d.billet(
        "Écrivez trois consignes que votre enseignante dit souvent.",
        exemples=[
            "Ouvrez votre cahier.",
            "Écoutez bien.",
            "Fermez votre cahier.",
        ],
        notes="Devoir court. Vérifier la terminaison -ez à l'écrit : c'est là que le "
              "piège se retourne, puisque le son ne l'indique pas.")

    return d.save(dossier)
