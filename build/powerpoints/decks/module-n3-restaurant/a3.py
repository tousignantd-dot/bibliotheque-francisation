# -*- coding: utf-8 -*-
"""A3 · Dans le casse-croûte.
Bloc A « Je découvre » · couleur teal · 75 min.
Source : exercice `prImg`, banc `FC_CARDS` (sections prep et t3).
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-restaurant/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Dans le casse-croûte',
        chapeau="Le comptoir, le plateau, les bacs d'ustensiles, les sachets "
                "de condiments : huit objets qu'on voit tous les midis et "
                "qu'on ne sait pas encore nommer.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire par l'image. Prévoir le module interactif à "
                  "l'écran : l'exercice 3 de « Je découvre » fait glisser les mêmes huit "
                  "photos sur les mêmes huit phrases.")

    d.objectifs([
        "nommer les huit objets d'un comptoir de casse-croûte ;",
        "décrire chaque objet en une phrase ;",
        "distinguer ce qu'on prend soi-même de ce qu'on demande ;",
        "employer chaque mot avec son article.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on prend soi-même, ici ?",
        image=IMG + 'bac-ustensiles.jpg',
        pistes=[
            "Qu'est-ce qu'il y a dans ces bacs ?",
            "Est-ce qu'il faut les demander au préposé ?",
            "Où sont les serviettes, d'habitude ?",
            "Et le sel, le poivre, le ketchup : ils sont où ?",
        ],
        notes="Beaucoup d'élèves n'osent pas se servir eux-mêmes et repartent sans "
              "ustensile. C'est le vrai enjeu de la séance, davantage que le vocabulaire.")

    d.tableau('Analyse', "Ce qu'on prend, et où",
              ["L'objet", "Où il se prend"],
              [["le plateau", "empilé au début du comptoir"],
               ["les ustensiles", "dans les bacs, près du ramassage"],
               ["les serviettes de table", "dans la boîte de métal, sur le comptoir"],
               ["les condiments", "en sachets, au bout du comptoir"]],
              cle=1,
              note="Ces quatre-là sont en libre-service : on ne les demande pas.",
              notes="Diapo à photographier. Insister : « Servez-vous » veut dire "
                    "« prends-en toi-même ». Ce n'est ni un reproche ni un refus.")

    d.cartes("Les objets du comptoir", "Quatre mots", [
        ("un plateau",
         "Le carré de plastique qui porte le repas. Il se prend au début du comptoir, "
         "avant même de commander, et se rapporte au bac à vaisselle en partant."),
        ("un ustensile",
         "La fourchette, le couteau ou la cuillère. Au singulier, le mot est rare ; on "
         "dit presque toujours « les ustensiles », au pluriel."),
        ("une serviette de table",
         "Le petit papier carré. Le mot complet est important : « une serviette » toute "
         "seule peut aussi vouloir dire celle de la salle de bain."),
        ("un condiment",
         "Le sel, le poivre, le ketchup, la moutarde. Ce qu'on ajoute pour le goût, et "
         "qui vient en petits sachets."),
    ], notes="Faire dire chaque mot avec son article, puis dans une phrase complète. Ces "
             "quatre mots sont ceux que le programme nomme pour cette situation.")

    d.tableau('Analyse', "Les objets qu'on reçoit",
              ["L'objet", "Ce qu'il sert à faire"],
              [["le tableau du menu", "lire ce qu'il y a, avant d'arriver au comptoir"],
               ["le reçu", "porter le numéro de la commande"],
               ["le sac de papier", "emporter le repas ailleurs"],
               ["le couvercle", "fermer un bol ou un verre pour le transport"]],
              cle=1,
              note="Ces quatre-là viennent du préposé : on ne les prend pas soi-même.",
              notes="Diapo à photographier. La séparation entre « je me sers » et « on me "
                    "donne » est la clé pratique de tout le bloc.")

    d.regle("Le mot complet, toujours",
            "« une serviette de table »",
            precision="Trois mots, jamais deux. Une serviette de bain, une "
                      "serviette de plage et une serviette de table sont trois "
                      "objets très différents. Au comptoir, le mot complet évite "
                      "un malentendu qui fait sourire.",
            notes="Diapo à photographier. Faire répéter à voix haute, deux fois, en "
                  "insistant sur les trois mots liés.")

    d.pratique('Vocabulaire', "Quel objet ?",
               "Nommez l'objet décrit.", [
        ("Le carré de plastique qui porte le repas.", "un plateau"),
        ("Le grand panneau au-dessus de la caisse.", "le tableau du menu"),
        ("Ce qu'on prend dans les bacs pour manger.", "des ustensiles"),
        ("Le petit papier pour s'essuyer les mains.", "une serviette de table"),
        ("Le sel, le poivre, le ketchup.", "des condiments"),
        ("Le rond de plastique qui ferme un bol.", "un couvercle"),
    ], corrige=True,
       notes="Exercice de reprise. Il reprend exactement les définitions du banc de "
             "vocabulaire du module interactif.")

    d.pratique('Production orale', "Décrivez la photo",
               "Une phrase par photo, avec l'article juste.", [
        ("La file devant le comptoir.", "Des personnes attendent devant le comptoir."),
        ("Le panneau au-dessus de la caisse.", "C'est le tableau du menu."),
        ("Trois verres côte à côte.", "Ce sont les trois formats."),
        ("Un sac de papier brun.", "C'est un sac, pour emporter."),
    ], corrige=True,
       notes="Faire passer quatre élèves différents. Corriger l'article, rien d'autre : "
             "le genre des noms est l'objet de la séance A4.")

    d.billet(
        "Écrivez six objets qu'il y a dans l'endroit où vous dînez.",
        exemples=[
            "Avec leur article : un plateau, une serviette de table…",
            "Et dites lesquels on prend soi-même.",
        ],
        notes="Devoir court. Il prépare la séance A4 sur les formats et le genre des "
              "noms du comptoir.")

    return d.save(dossier)
