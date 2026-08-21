# -*- coding: utf-8 -*-
"""A4 · Décrire un dégât avec précision.
Bloc A « Je découvre » · couleur ambre · 75 min. Écriture.
Source : exercice `prDegat`, mini-leçon `prDegat`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-degat/images/')


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Décrire un dégât avec précision",
        chapeau="« C'est brisé » ne donne rien à personne. Une description "
                "utile tient en trois éléments, et elle n'est pas plus longue.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle rassemble le vocabulaire de A3 et "
                  "prépare l'appel du défi 1. Prévoir du temps d'écriture individuelle : "
                  "c'est là que la séance se joue.")

    d.objectifs([
        "décrire un dommage en disant quoi, où et de quelle taille ;",
        "employer le verbe qui va avec chaque surface ;",
        "dire ce que le dégât empêche de faire ;",
        "séparer ce qui appartient au bâtiment et ce qui vous appartient.",
    ])

    d.regle("Quoi, où exactement, de quelle taille",
            "Une description utile répond à trois questions, pas une de moins.",
            precision="« Il y a de l'eau » ne permet ni de chiffrer, ni de dater, ni de "
                      "décider de l'urgence. « Un cerne brun d'environ un mètre au "
                      "plafond de la chambre, dans le coin nord » permet les trois. "
                      "Remarquez que la seconde phrase n'est pas plus longue : elle est "
                      "mieux choisie.",
            notes="Écrire les deux phrases au tableau, l'une sous l'autre, et compter les "
                  "mots à voix haute. L'effet est immédiat.")

    d.tableau('Du flou au précis', "Quatre phrases refaites",
              ['Ce qu\'on dit souvent', 'Ce qu\'il faut dire'],
              [["Il y a de l'eau.",
                "Un cerne brun d'environ un mètre au plafond de la chambre."],
               ["Le mur est abîmé.",
                "La peinture cloque sur trente centimètres, à mi-hauteur."],
               ["Le plancher est bizarre.",
                "Le plancher gondole sur trois lattes, le long du mur."],
               ["J'ai perdu des affaires.",
                "Un matelas humide et une boîte de documents trempée."]],
              cle=1,
              note="Une mesure comptable — trois lattes, trente centimètres — vaut mieux "
                   "que n'importe quel adjectif.",
              notes="Faire lire la colonne de gauche par un élève, celle de droite par un "
                    "autre. Le contraste s'entend mieux qu'il ne se voit.")

    d.cartes("Ce qu'une description doit contenir", "Quatre éléments", [
        ("Le quoi",
         "La marque, avec le verbe du métier : cerne, cloque, gondole, moisit."),
        ("Le où",
         "La pièce, le mur ou le coin, la hauteur. Trois repères suffisent."),
        ("La taille",
         "Une mesure annoncée : « environ un mètre », « trois lattes »."),
        ("Ce que ça empêche",
         "« Je ne peux plus coucher dans ma chambre. » C'est ce qui fonde une demande."),
    ], notes="La quatrième carte est celle qu'on oublie, et c'est la seule qui transforme "
             "un dommage en préjudice. Y revenir au défi 3.")

    d.declencheur(
        'Observation', "Décrivez ce mur en une phrase, avec le verbe juste et une mesure.",
        image=IMG + 'peinture-cloque.jpg',
        pistes=[
            "Quel verbe : elle cloque, elle se décolle, elle gonfle ?",
            "Sur quelle longueur ?",
            "À quelle hauteur du mur ?",
            "Dans quelle pièce ?",
        ],
        notes="Faire écrire la phrase avant de la faire dire : à l'oral, le groupe "
              "s'entraîne à approuver la première réponse entendue.")

    d.regle("Le bâtiment n'est pas à vous",
            "Deux listes, dès la première description.",
            precision="Le plafond, le plancher, les murs et la plomberie appartiennent à "
                      "l'immeuble : c'est le propriétaire qui les fait réparer. Le "
                      "matelas, les meubles, les vêtements et les papiers sont à vous : "
                      "c'est votre assurance. Faire cette séparation dès le premier appel "
                      "évite d'être renvoyé d'une porte à l'autre pendant deux semaines.",
            notes="Reprise au défi 3, avec l'assureur. L'installer ici, sans détailler "
                  "les assurances.")

    d.pratique('Pratique · exercice prDegat', "Le mot juste",
               "Complétez chaque phrase. Un mot par trou.",
               [("Au plafond, l'eau a laissé un ___ brun d'environ un mètre.", "cerne"),
                ("Les lattes du plancher se soulèvent : le plancher ___ .", "gondole"),
                ("La peinture se décolle en petites bulles : elle ___ .", "cloque"),
                ("Pour recueillir l'eau, elle a placé une ___ sous la fuite.",
                 "chaudière"),
                ("Le gros réservoir qui a lâché, c'est le ___ .", "chauffe-eau"),
                ("L'eau qui traverse lentement un plancher, c'est une ___ .",
                 "infiltration")],
               corrige=True, cols=1,
               notes="Faire répondre à l'oral avant d'ouvrir le module. La correction "
                     "écrite vient ensuite.")

    d.piege("Décrire ses émotions au lieu des faits",
            "C'est un cauchemar, je n'en peux plus.",
            "Trois nuits sans chambre, un matelas humide, un plafond taché.",
            "L'émotion est légitime, et elle a sa place — une phrase. Mais elle ne se "
            "traite pas : personne ne peut chiffrer un cauchemar. Gardez une phrase pour "
            "dire que c'est difficile, et donnez le reste en faits mesurés. Vous serez "
            "mieux entendu, pas moins.",
            notes="Point délicat à amener sans condescendance : beaucoup d'élèves vivent "
                  "réellement ces situations. Dire que c'est une question d'efficacité, "
                  "pas de retenue.")

    d.billet(
        "Décrivez un dommage de votre logement, ou un imaginé, en une phrase.",
        exemples=[
            "Quoi + où exactement + de quelle taille.",
            "« Une tache brune de vingt centimètres au plafond de la salle de bain. »",
        ],
        notes="Trois minutes. Ces phrases sont le point de départ de la production orale "
              "de la séance E1 : les garder.")

    return d.save(dossier)
