# -*- coding: utf-8 -*-
"""C3 · Quatre questions au vendeur.
Bloc C « Défi 2 · Trouver le rayon et demander » · couleur teal · 60 min.
Source : exercice `t2questions`, mini-leçon `t2questions`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre='Quatre questions au vendeur',
        chapeau="Où, combien, est-ce que vous avez, combien de large. Avec "
                "quatre débuts de phrase et un nom d'appareil, on obtient "
                "tout ce dont on a besoin.",
        duree='60 minutes')

    d.titre(notes="Séance d'oral. Prévoir beaucoup de travail en paires : la séance ne "
                  "vaut que si chaque élève dit ses quatre questions au moins trois fois.")

    d.objectifs([
        "poser une question avec où, combien et est-ce que ;",
        "faire monter la voix à la fin d'une question ;",
        "demander de répéter quand on n'a pas compris ;",
        "conclure un achat en une phrase.",
    ])

    d.tableau('Analyse', "Les quatre questions du magasin",
              ['Ce qu\'on veut savoir', 'Ce qu\'on dit'],
              [["où c'est", "Où est le rayon des laveuses ?"],
               ["le prix", "C'est combien, celui-là ?"],
               ["si le magasin l'a", "Est-ce que vous avez ce modèle en gris ?"],
               ["le format", "Elle fait combien de large ?"]],
              cle=1,
              note="Une question à la fois : on attend la réponse avant de "
                   "poser la suivante.",
              notes="Diapo à photographier. Faire lire les quatre questions par le "
                    "groupe entier, puis par des élèves seuls.")

    d.regle("Est-ce que transforme n'importe quelle phrase en question",
            "Vous avez ce modèle.  ·  Est-ce que vous avez ce modèle ?",
            precision="On pose « est-ce que » devant la phrase, et rien "
                      "d'autre ne change. C'est l'outil le plus rentable du "
                      "niveau : il sert dans toutes les situations.",
            notes="Diapo à photographier. Donner trois phrases affirmatives et faire "
                  "produire les questions à voix haute, à la chaîne.")

    d.cartes("Trois façons de demander le prix", "Toutes les trois correctes", [
        ("C'est combien ?",
         "La plus courte et la plus entendue. On l'accompagne du doigt."),
        ("Elle coûte combien ?",
         "Un peu plus complète. Le verbe change selon l'appareil : elle coûte, il coûte."),
        ("Quel est le prix de ce modèle ?",
         "Plus soutenue. Correcte, mais on l'entend surtout au téléphone."),
    ], cols=3,
       notes="Faire choisir à chaque élève celle qu'il retiendra. Une seule suffit : "
             "mieux vaut une phrase qui sort toute seule que trois qui hésitent.")

    d.pratique('Production', "Que dites-vous ?",
               "Une phrase courte et polie pour chaque situation.", [
        ("Vous entrez et vous cherchez les laveuses.",
         "Bonjour, où est le rayon des laveuses ?"),
        ("Vous voulez le prix de la machine blanche.",
         "Elle coûte combien ?"),
        ("Vous voulez savoir si le magasin l'a en gris.",
         "Est-ce que vous l'avez en gris ?"),
        ("Vous voulez la largeur de l'appareil.",
         "Elle fait combien de large ?"),
        ("Le vendeur a parlé trop vite.",
         "Pardon, pouvez-vous répéter, s'il vous plaît ?"),
        ("Vous avez choisi : vous la voulez.",
         "Je la prends."),
    ], corrige=True,
       notes="En paires : l'un lit la situation, l'autre répond sans regarder. Inverser "
             "à mi-chemin, puis faire jouer deux paires devant le groupe.")

    d.piege("Rester bloqué quand on n'a pas compris",
            "faire oui de la tête sans avoir compris",
            "Pardon, pouvez-vous répéter, s'il vous plaît ?",
            "C'est la phrase la plus utile du module, et tout le monde la dit, y compris "
            "les gens d'ici entre eux. Un vendeur qui répète plus lentement, c'est "
            "normal ; un client qui repart avec le mauvais appareil, c'est une journée "
            "perdue.",
            notes="Faire répéter la phrase par tout le groupe, deux fois. Elle doit "
                  "sortir sans hésitation.")

    d.regle("La voix monte à la fin de la question",
            "Vous l'avez en gris ?",
            precision="Sans « est-ce que », c'est l'intonation seule qui fait "
                      "la question. Si la voix descend, le vendeur entend une "
                      "affirmation et ne répond pas.",
            notes="Diapo à photographier. Faire dire la même phrase deux fois, voix qui "
                  "monte puis voix qui descend. La différence s'entend tout de suite.")

    d.billet(
        "Préparez votre achat : écrivez vos quatre questions.",
        exemples=[
            "Choisissez un appareil dont vous avez besoin.",
            "Écrivez les quatre questions dans l'ordre où vous les poserez.",
        ],
        notes="Devoir de préparation. Ces quatre questions serviront telles quelles dans "
              "le jeu de rôle et la production orale de E1.")

    return d.save(dossier)
