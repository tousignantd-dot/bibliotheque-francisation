# -*- coding: utf-8 -*-
"""C4 · Lire l'horaire, écrire la fiche
Bloc C « Défi 2 » · couleur acier · 75 min. Lecture, puis production écrite.
Source : exercices `t2hor` et `t2fiche`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-quebec/vocab/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre="Lire l'horaire, écrire la fiche",
        chapeau="Un horaire interurbain n'est pas un horaire d'autobus de "
                "ville : il donne des heures de départ et d'arrivée pour "
                "chaque arrêt, sur plusieurs jours, et tous les départs ne "
                "font pas les mêmes arrêts. On y lit une ligne, pas une "
                "colonne.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 2. Elle ferme le bloc par une production "
                  "écrite : la fiche de voyage en six lignes. Prévoir la seconde moitié "
                  "de la séance pour l'écriture, en silence, avec l'horaire projeté.")

    d.objectifs([
        "lire une ligne d'horaire interurbain d'un bout à l'autre ;",
        "calculer une durée de trajet à partir de deux heures ;",
        "repérer une correspondance et son temps d'attente ;",
        "écrire une fiche de voyage complète en six lignes.",
    ], notes="Le deuxième objectif demande un calcul sur des heures — de 7 h à 15 h 10 — "
             "et beaucoup d'élèves n'osent pas le faire à voix haute. Le faire "
             "collectivement au tableau une première fois.")

    d.declencheur(
        'Observation', "Trois départs le lundi. Lequel prenez-vous, et "
                       "pourquoi ?",
        image=img('horaire.jpg'),
        pistes=[
            "Sept heures, midi trente, dix-huit heures quinze : que change l'heure ?",
            "À quelle heure arriverez-vous, dans chaque cas ?",
            "Lequel est direct, lequel a une correspondance ?",
            "Est-ce qu'on veut arriver dans une ville inconnue à minuit ?",
        ],
        notes="La dernière piste est le vrai critère et il n'est pas dans l'horaire : "
              "arriver de jour dans un endroit qu'on ne connaît pas. C'est un rappel du "
              "principe de C1 — l'écrit ne dit pas tout.")

    d.tableau('Une ligne d\'horaire', "Le départ de sept heures, lundi",
              ["L'arrêt", "L'heure"],
              [["Montréal", "7 h 00"],
               ["Trois-Rivières", "8 h 35"],
               ["Québec", "10 h 20"],
               ["Rivière-du-Loup", "13 h 25"],
               ["Rimouski", "15 h 10"]],
              cle=1,
              notes="Faire calculer la durée totale — huit heures dix — puis la durée "
                    "entre deux arrêts. Les arrêts sont ceux du dialogue de B1 et ils "
                    "sont réels ; les heures sont vraisemblables et inventées, comme "
                    "tout ce qui change trop vite pour être écrit dans un module.")

    d.cartes("Trois mots de l'horaire", "Ils décident du trajet", [
        ("Direct",
         "Un seul autocar du départ à l'arrivée."),
        ("Une correspondance",
         "On change d'autocar en chemin, et on attend."),
        ("Le temps d'attente",
         "Quarante minutes à Québec, dans le dialogue."),
        ("Le quai",
         "Le numéro d'où part l'autocar. Il change chaque jour."),
    ], notes="« Correspondance » est le mot le plus utile des quatre et il vaut pour le "
             "train, l'avion et le métro. Faire remarquer qu'une correspondance ratée "
             "fait perdre bien plus que quarante minutes sur une ligne interurbaine.")

    d.pratique('Lecture', "Répondez d'après l'horaire",
               "À l'oral, en montrant la ligne au tableau.", [
        ("À quelle heure part l'autocar de Montréal ?", "7 h 00"),
        ("À quelle heure arrive-t-il à Québec ?", "10 h 20"),
        ("Combien de temps dure le trajet complet ?", "huit heures dix"),
        ("Combien de temps entre Québec et Rivière-du-Loup ?", "trois heures cinq"),
        ("Le départ de midi trente est-il direct ?", "non — correspondance à Québec"),
        ("Combien de temps dure l'attente à Québec ?", "quarante minutes"),
    ], corrige=True,
       notes="Faire venir les élèves montrer la ligne au tableau plutôt que répondre "
             "de leur place. Suivre la ligne du doigt est exactement le geste qui "
             "manque à ceux qui se perdent dans un horaire.")

    d.piege("Lire l'horaire en colonne au lieu de le lire en ligne",
            "Je regarde la colonne « Rimouski » et je prends la première heure.",
            "Je suis la ligne de mon départ, d'un arrêt à l'autre, jusqu'au bout.",
            "Une colonne mélange des départs différents. En la lisant de haut en "
            "bas, on associe l'heure de départ d'un autocar à l'heure d'arrivée "
            "d'un autre — et on se présente au mauvais moment.",
            notes="C'est l'erreur qui fait manquer des autocars. La faire commettre "
                  "exprès au tableau, puis corriger : elle ne se comprend qu'en la "
                  "voyant.")

    d.regle("La fiche de voyage, en six lignes",
            "Où · quand · comment · combien de temps · où dormir · ce qu'on "
            "veut voir.",
            precision="Six lignes suffisent à tout dire, et elles se relisent en "
                      "dix secondes au comptoir ou au téléphone.",
            notes="Diapositive à photographier et à laisser projetée pendant "
                  "l'écriture. Rendre ici les billets de C3 : la comparaison et le "
                  "choix deviennent les lignes trois et cinq.")

    d.pratique('Autoévaluation', "Relisez votre fiche avant de la remettre",
               "Répondez honnêtement.", [
        ("Peut-on savoir où vous allez en lisant la première ligne ?", "sinon, recommencez par là"),
        ("Les dates sont-elles en chiffres ?", "« bientôt » ne se réserve pas"),
        ("Avez-vous dit combien de nuits ?", "l'hébergement se compte en nuits"),
        ("Avez-vous justifié un de vos choix ?", "une seule raison suffit"),
        ("Les prépositions de lieu sont-elles justes ?", "à, en, au, dans les"),
    ], corrige=True,
       notes="Faire faire l'autoévaluation avant la remise, jamais après. La dernière "
             "ligne renvoie à A4 : c'est le point qui se corrige le plus vite quand on "
             "pense à le regarder.")

    d.billet(
        "En une ligne : quelle information vous a manqué pour finir votre fiche ?",
        exemples=[
            "Une information précise, et où vous iriez la chercher.",
            "Si rien ne vous a manqué, notez ce qui a été le plus long à trouver.",
        ],
        notes="Ramasser les billets : ils ouvrent le défi 3, où l'on va justement "
              "chercher auprès des gens ce qui n'est écrit nulle part.")

    return d.save(dossier)
