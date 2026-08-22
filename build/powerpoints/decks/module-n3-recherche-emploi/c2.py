# -*- coding: utf-8 -*-
"""C2 · Chaque ligne répond à une question.
Bloc C « Défi 2 » · couleur ambre · 75 min. Lecture et écriture.
Source du module : exercices `t2lignes` et `t2offre`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Chaque ligne répond à une question',
        chapeau="Une offre d'emploi tient en huit lignes, et chaque ligne "
                "répond à une question précise. Les lire dans l'ordre, c'est "
                "savoir en trente secondes si l'on se déplace.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture. Prévoir des surligneurs : le geste de marquer "
                  "chaque ligne d'une couleur est ce qui fixe la méthode.")

    d.objectifs([
        "repérer les six renseignements d'une offre d'emploi ;",
        "trouver rapidement l'horaire et le salaire ;",
        "repérer à qui s'adresser et comment ;",
        "décider si l'offre convient.",
    ])

    d.tableau('Analyse', "Six lignes, six questions",
              ['La ligne de l\'annonce', 'La question à laquelle elle répond'],
              [["Aide à la cuisine", "Quel poste ? Le nom du travail."],
               ["20 heures par semaine", "Combien d'heures ? Plein ou partiel ?"],
               ["Du mardi au samedi, de 9 h à 13 h", "Quels jours et quelles heures ?"],
               ["16,50 $ de l'heure", "Combien pour chaque heure travaillée ?"],
               ["Aucune expérience exigée", "Faut-il avoir déjà fait ce travail ?"],
               ["Demander Hugo Pelletier, 514 555-0148", "À qui s'adresser, et comment ?"]],
              cle=0,
              note="Aucune de ces six lignes n'est facultative : une seule suffit à écarter l'offre.",
              notes="Diapo à photographier, la plus utile du défi 2. Faire recopier "
                    "la colonne de droite : ce sont les six questions à se poser.")

    d.regle("La dernière ligne dit comment s'y prendre",
            "Se présenter en personne, entre 9 h et 11 h. Demander Hugo Pelletier.",
            precision="C'est la ligne qu'on lit le moins et celle qui décide de tout : "
                      "elle donne l'heure, l'adresse et le nom de la personne. Arriver "
                      "à un autre moment, c'est arriver pour rien.",
            notes="Diapo à photographier. Faire relire la dernière ligne des annonces "
                  "réelles apportées par le groupe, s'il y en a.")

    d.cartes("L'offre du centre Léo-Bourdon", "Lire les huit lignes", [
        ("Le haut",
         "CENTRE COMMUNAUTAIRE LÉO-BOURDON. Recherche : AIDE À LA CUISINE. Le nom du "
         "lieu, puis le poste, en gros."),
        ("Le milieu",
         "20 heures par semaine, du mardi au samedi, de 9 h à 13 h. Salaire : 16,50 $ "
         "de l'heure, payé aux deux semaines."),
        ("Les tâches",
         "Laver les légumes, servir les repas, faire la vaisselle. Trois verbes : c'est "
         "ce qu'on fera vraiment de ses journées."),
        ("Le bas",
         "Aucune expérience exigée. Formation donnée sur place. Il faut parler "
         "français. Se présenter au 2140, rue Bélanger, et demander Hugo Pelletier."),
    ], notes="Lire l'annonce entière à voix haute une fois, puis la faire relire par "
             "quatre élèves, une carte chacun.")

    d.piege("Ne lire que le salaire",
            "16,50 $ de l'heure, ça me va. J'y vais.",
            "Je lis les six lignes, puis je décide.",
            "Le salaire ne dit ni quand on travaille, ni ce qu'on fait, ni s'il faut de "
            "l'expérience, ni à qui se présenter. Une offre bien payée dont l'horaire "
            "est impossible ne vaut rien, et la visite est perdue.",
            notes="Rappeler l'exemple de Fanta en C1 : la meilleure offre pour elle "
                  "n'était pas la première qu'elle a lue.")

    d.pratique('Lecture', "Vrai ou faux ?",
               "Lisez l'offre du centre Léo-Bourdon, puis répondez.", [
        ("Le travail est de vingt heures par semaine.", "vrai"),
        ("On travaille le dimanche et le lundi.", "faux — du mardi au samedi"),
        ("Le salaire est payé chaque semaine.", "faux — aux deux semaines"),
        ("Faire la vaisselle fait partie des tâches.", "vrai"),
        ("Il faut avoir déjà travaillé en cuisine.", "faux — aucune expérience exigée"),
        ("L'annonce donne une adresse et un numéro.", "vrai"),
    ], corrige=True,
       notes="Mêmes énoncés que l'exercice t2offre du module. Faire pointer la ligne "
             "exacte de l'annonce pour chaque réponse.")

    d.pratique('Appariement', "Quelle question pose chaque ligne ?",
               "Reliez la ligne de l'annonce à la question qu'elle règle.", [
        ("Aide à la cuisine", "Quel poste ?"),
        ("20 heures par semaine", "Combien d'heures ?"),
        ("Du mardi au samedi, de 9 h à 13 h", "Quel horaire ?"),
        ("16,50 $ de l'heure", "Combien d'argent ?"),
        ("Aucune expérience exigée", "Faut-il de l'expérience ?"),
        ("Demander Hugo Pelletier", "À qui parler ?"),
    ], corrige=True,
       notes="Même appariement que t2lignes dans le module. Le refaire ensuite sur une "
             "annonce apportée par un élève.")

    d.pratique('Écriture', "Écrivez une offre en six lignes",
               "Inventez un poste de votre quartier et écrivez son offre.", [
        ("Ligne 1", "Le nom du commerce et le poste."),
        ("Ligne 2", "Le nombre d'heures par semaine."),
        ("Ligne 3", "Les jours et les heures."),
        ("Ligne 4", "Le salaire de l'heure."),
        ("Ligne 5", "Ce qu'il faut, ou « aucune expérience exigée »."),
        ("Ligne 6", "À qui s'adresser, et comment."),
    ], notes="Vingt minutes. Faire échanger les feuilles ensuite : chacun lit l'offre "
             "du voisin et dit en une phrase si elle lui conviendrait.")

    d.billet(
        "Quelle ligne d'une offre regardez-vous en premier, et pourquoi ?",
        exemples=[
            "Une phrase, avec « parce que ».",
            "Il n'y a pas de mauvaise réponse : la vôtre dépend de votre vie.",
        ],
        notes="Deux minutes. Les réponses sont utiles à relire en C4, quand il sera "
              "question de ce qui est exigé.")

    return d.save(dossier)
