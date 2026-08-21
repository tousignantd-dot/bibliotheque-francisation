# -*- coding: utf-8 -*-
"""B1 · Lire le tableau avant de commander.
Bloc B « Défi 1 · Lire le menu » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-restaurant/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Lire le tableau avant de commander',
        chapeau="Le tableau du menu porte cinquante mots. Personne ne les lit "
                "tous — pas même les gens nés ici. On cherche un titre, on "
                "descend, on lit un prix.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 1. C'est la compétence que le programme met "
                  "au centre de cette situation au niveau 3 : lire un menu simple. Tout "
                  "le bloc B en découle.")

    d.objectifs([
        "comprendre une explication de menu entre deux camarades ;",
        "repérer les titres des blocs d'un tableau ;",
        "comprendre ce que « servi avec » veut dire ;",
        "savoir ce qu'un trio comprend.",
    ])

    d.declencheur(
        'Observation', "Par où commencer, sur un panneau comme celui-là ?",
        image=IMG + 'tableau-menu-haut.jpg',
        pistes=[
            "Combien de colonnes voyez-vous ?",
            "Où sont les prix, sur ce panneau ?",
            "Qu'est-ce qui est écrit le plus gros ?",
            "Combien de temps avez-vous pour le lire, dans une file ?",
        ],
        notes="La contrainte de temps est le vrai sujet : dans une file, on a vingt "
              "secondes. Le faire sentir en donnant justement vingt secondes au groupe "
              "avant de retirer l'image.")

    d.dialogue('Dialogue · 1 de 3', "Par où je commence ?", [
        ("YOLETTE", "Il y a beaucoup de choses écrites. Par où je commence ?", True),
        ("FATOU", "Par le titre des colonnes. « Sandwichs », « Soupes », « Breuvages », « Extras ».", True),
        ("YOLETTE", "Sandwich au poulet, sandwich aux œufs, sandwich au jambon.", True),
        ("FATOU", "« Au poulet », ça veut dire qu'il y a du poulet dedans. C'est ça qui change.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La deuxième réplique donne la stratégie de lecture de tout le bloc. "
             "L'écrire au tableau : le titre d'abord, le plat ensuite.")

    d.dialogue('Dialogue · 2 de 3', "Servi avec salade ou frites", [
        ("YOLETTE", "Et « servi avec salade ou frites » ?", True),
        ("FATOU", "C'est l'accompagnement. Il vient avec le sandwich, tu ne paies pas plus.", True),
        ("YOLETTE", "Alors le trio, c'est quoi ?", True),
        ("FATOU", "Le trio, c'est le sandwich, l'accompagnement et le breuvage ensemble. Un seul prix.", True),
    ], notes="Deux mots nouveaux dans quatre répliques : accompagnement et trio. Les "
             "faire redire par deux élèves différents, avec leurs définitions.")

    d.dialogue('Dialogue · 3 de 3', "La ligne du bas", [
        ("YOLETTE", "C'est moins cher que trois choses séparées ?", True),
        ("FATOU", "Oui, un peu. Regarde la colonne de droite et compare.", True),
        ("YOLETTE", "Et cette ligne en bas, avec le petit dessin de feuille ?", True),
        ("FATOU", "Ça veut dire sans viande. La soupe aux légumes est là.", True),
    ], notes="Les petits pictogrammes du bas d'un menu ne s'inventent pas : demander au "
             "groupe lesquels ils ont déjà vus, et ce qu'ils croient qu'ils veulent dire.")

    d.tableau('Analyse', "Les quatre blocs du tableau",
              ['Le titre', "Ce qu'on trouve dessous"],
              [["Sandwichs", "du pain avec du poulet, des œufs ou du jambon"],
               ["Soupes", "ce qui se mange chaud, dans un bol"],
               ["Breuvages", "le jus, le lait, le café, l'eau"],
               ["Trios", "trois choses ensemble, à un seul prix"]],
              cle=1,
              note="On lit le titre, puis on descend seulement dans le bloc utile.",
              notes="Diapo à photographier. Faire nommer un plat de chaque bloc par un "
                    "élève différent.")

    d.regle("Ce que « servi avec » veut dire",
            "« Sandwichs — servis avec salade ou frites »",
            precision="L'accompagnement est déjà dans le prix du sandwich : on "
                      "ne paie pas deux fois. La ligne est écrite une seule "
                      "fois, en petit, sous le titre du bloc, et elle vaut pour "
                      "tous les plats du bloc.",
            notes="Diapo à photographier. C'est l'information que les élèves manquent le "
                  "plus souvent, et elle coûte de l'argent quand elle est manquée.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("« Au poulet » dit ce qu'il y a dans le sandwich.", "vrai"),
        ("L'accompagnement coûte un prix en plus.", "faux — il est compris"),
        ("Le trio comprend le plat, l'accompagnement et le breuvage.", "vrai"),
        ("Le trio coûte plus cher que les trois choses séparées.", "faux — un peu moins"),
        ("Le petit dessin de feuille veut dire « sans viande ».", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Écrivez le nom des blocs d'un menu que vous connaissez.",
        exemples=[
            "Trois ou quatre titres suffisent.",
            "Et écrivez un plat sous chaque titre.",
        ],
        notes="Devoir court. Il prépare la séance B2, où l'on démonte le tableau ligne "
              "par ligne.")

    return d.save(dossier)
