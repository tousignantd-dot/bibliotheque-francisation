# -*- coding: utf-8 -*-
"""D1 · Lire la grille sans se perdre.
Bloc D « Défi 3 · Lire la grille des tarifs » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf`, `t3grille` et `t3cat`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Lire la grille sans se perdre',
        chapeau="Un tableau se lit en croix : une ligne pour le titre, une "
                "colonne pour la personne, et le prix à l'intersection. "
                "C'est tout.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3, qui est la compétence de compréhension écrite du "
                  "programme. Projeter d'abord une vraie grille tarifaire et laisser le "
                  "groupe la regarder trente secondes en silence. Presque tout le monde "
                  "la trouvera illisible : c'est le point de départ.")

    d.objectifs([
        "trouver une ligne et une colonne dans un tableau ;",
        "reconnaître les quatre zones tarifaires ;",
        "reconnaître les quatre catégories de personnes ;",
        "savoir qu'un tarif réduit exige une carte avec photo.",
    ])

    d.dialogue('Dialogue · 1 de 2', "Montrez-moi la ligne", [
        ("ROSARIO", "Monsieur, la grille est affichée au mur, mais je ne comprends pas tout.", True),
        ("NORMAND", "Montrez-moi la ligne qui vous embête.", True),
        ("ROSARIO", "Ici : « Soirée illimitée, six dollars soixante-quinze, valide de 18 h à 5 h ».", True),
        ("NORMAND", "Ça veut dire à partir de six heures du soir, jusqu'à cinq heures le lendemain matin.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Rosario emploie « ce titre-là » et montre du doigt : c'est exactement ce "
             "que la séance B2 a préparé. Le faire remarquer au groupe.")

    d.dialogue('Dialogue · 2 de 2', "Et cette colonne-là ?", [
        ("ROSARIO", "Et cette colonne-là ? « Réduit 6-17 ans ».", True),
        ("NORMAND", "C'est le prix pour les jeunes de six à dix-sept ans. Avec une carte avec photo.", True),
        ("ROSARIO", "Mon garçon a neuf ans. Est-ce que je paie pour lui ?", True),
        ("NORMAND", "Onze ans et moins, c'est gratuit, s'il est avec vous.", True),
        ("ROSARIO", "Gratuit ? Je ne savais pas ça.", True),
    ], notes="La gratuité des onze ans et moins est le renseignement que presque "
             "personne ne connaît, et il vaut plusieurs centaines de dollars par an "
             "pour une famille. Le vérifier avec le groupe : qui le savait ?")

    d.tableau('Analyse', "Les quatre zones tarifaires",
              ["La zone", "Ce qu'elle couvre"],
              [["A", "l'agglomération de Montréal"],
               ["B", "Laval et l'agglomération de Longueuil"],
               ["C", "les couronnes nord et sud"],
               ["D", "hors du territoire"]],
              cle=0,
              note="Un titre « Tous modes A » sert seulement dans Montréal.",
              notes="Diapositive à photographier. Demander qui habite ou travaille hors "
                    "de l'île : ceux-là doivent lire un autre bloc de la grille, et "
                    "c'est le piège le plus coûteux du défi 3.")

    d.tableau('Analyse', "Les quatre colonnes de la grille",
              ["La colonne", "Pour qui"],
              [["Ordinaire", "le prix plein, la plupart des adultes"],
               ["Réduit 6-17 ans", "les enfants et les adolescents"],
               ["Réduit étudiant", "18 ans et plus, aux études à temps plein"],
               ["Réduit 65 ans et plus", "les personnes aînées"]],
              cle=0,
              note="Les trois colonnes « Réduit » exigent une carte avec photo.",
              notes="Diapositive à photographier. Faire placer chaque élève dans sa "
                    "colonne, et les membres de sa famille. Plusieurs découvriront "
                    "qu'ils paient le plein prix sans raison.")

    d.regle("Ce qu'il faut pour un tarif réduit",
            "Le bon âge ET une carte OPUS avec photo",
            precision="Les deux, toujours. Avec le bon âge mais sans la photo, "
                      "on paie le tarif ordinaire. La photo se fait au point de "
                      "service : il faut venir avec la personne concernée et une "
                      "preuve de son âge.",
            notes="Diapositive à photographier. C'est le renseignement pratique le plus "
                  "rentable du module. Encourager le groupe à faire faire les cartes de "
                  "leurs enfants et de leurs parents.")

    d.tableau('Analyse', "La grille de la zone A",
              ["Le titre", "Ordinaire · Réduit"],
              [["1 passage", "3,75 $ · 2,75 $"],
               ["10 passages", "35,00 $ · 23,50 $"],
               ["Hebdo, du lundi au dimanche", "33,25 $ · 20,00 $"],
               ["Mensuel", "110,00 $ · 66,00 $"]],
              cle=1,
              note="Le titre 24 h coûte 11,25 $ et n'a pas de tarif réduit.",
              notes="Diapositive à photographier. Ce sont les vrais prix. Faire "
                    "calculer à voix haute l'économie d'une famille de quatre personnes "
                    "dont deux ont droit au tarif réduit.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue et la grille.", [
        ("La Soirée illimitée est valide de dix-huit heures à cinq heures.", "vrai"),
        ("La colonne « Réduit 6-17 ans » s'adresse aux adultes.", "faux — aux jeunes"),
        ("Un enfant de neuf ans accompagné voyage gratuitement.", "vrai — 11 ans et moins"),
        ("Une personne peut accompagner dix enfants.", "faux — cinq au maximum"),
        ("Le bon âge suffit pour avoir le tarif réduit.", "faux — il faut aussi la carte avec photo"),
    ], corrige=True,
       notes="Faire justifier chaque réponse en montrant la ligne ou la colonne de la "
             "grille projetée. C'est la compétence même du défi 3 : trouver, pas "
             "deviner.")

    d.billet(
        "Écrivez dans quelle colonne de la grille vous vous trouvez, et pourquoi.",
        exemples=[
            "Je suis dans la colonne ___ parce que j'ai ___ ans.",
            "Dans ma famille, ___ a droit au tarif réduit.",
        ],
        notes="Devoir court. Ramasser et vérifier : ceux qui se placent dans la mauvaise "
              "colonne perdent de l'argent tous les mois, et le billet permet de les "
              "reprendre individuellement.")

    return d.save(dossier)
