# -*- coding: utf-8 -*-
"""D1 · Le formulaire d'Hugo.
Bloc D « Défi 3 · Mon nom sur le papier » · couleur acier · 75 min.
Source du module : dialogue `t3`, exercices `t3vf` et `t3cases`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Le formulaire d'Hugo",
        chapeau="Il reste toujours un papier à remplir, et il se remplit "
                "d'une seule façon : en lettres moulées, case par case, sans "
                "en sauter une.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Apporter un vrai formulaire vierge si "
                  "possible — de clinique, de bibliothèque, peu importe : la forme "
                  "est la même partout et le tenir en main change tout.")

    d.objectifs([
        "comprendre les consignes d'un formulaire ;",
        "savoir ce qu'on écrit dans chaque case ;",
        "écrire en lettres moulées ;",
        "ne laisser aucune case vide.",
    ])

    d.declencheur(
        'Observation', "Quels formulaires avez-vous déjà remplis ici ?",
        pistes=[
            "À la clinique ? À l'école ? À la banque ?",
            "Qu'est-ce qui était difficile ?",
            "Est-ce qu'on vous a demandé d'écrire en lettres moulées ?",
            "Avez-vous déjà laissé une case vide ?",
        ],
        notes="Presque tout le monde en a rempli, et presque tout le monde a bloqué au "
              "même endroit : le vocabulaire des consignes. C'est ce que la séance règle.")

    d.dialogue('Dialogue · 1 de 3', "En lettres moulées", [
        ("HUGO", "Bonjour. Vous venez pour le poste à la cuisine ?", True),
        ("FANTA", "Oui, monsieur. J'ai vu l'annonce au babillard de l'épicerie.", True),
        ("HUGO", "Parfait. Remplissez ce formulaire, et je le regarde tout de suite.", True),
        ("HUGO", "Ce n'est pas long. Écrivez en lettres moulées, s'il vous plaît.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Fanta est arrivée par l'annonce lue en C1. Le faire remarquer : les trois "
             "défis racontent la même semaine.")

    d.dialogue('Dialogue · 2 de 3', "Suivez les cases", [
        ("FANTA", "En lettres moulées ? C'est-à-dire ?", True),
        ("HUGO", "En majuscules, bien détachées. Comme sur une carte d'assurance maladie.", True),
        ("FANTA", "Ah, d'accord. Et ici, « prénom » d'abord ou « nom » d'abord ?", True),
        ("HUGO", "Suivez les cases. Nom de famille dans la première, prénom dans la deuxième.", True),
    ], notes="Fanta demande deux fois ce qu'elle ne comprend pas. C'est la même phrase "
             "qu'en A1 : « Qu'est-ce que ça veut dire ? » Elle traverse le module.")

    d.dialogue('Dialogue · 3 de 3', "Ne laissez jamais une case vide", [
        ("FANTA", "Et « disponibilités » ? J'écris les jours ?", True),
        ("HUGO", "Les jours et les heures. Soyez précise : « du mardi au samedi, de 9 h à 13 h ».", True),
        ("FANTA", "Ici, il y a une case à cocher : « Avez-vous un permis de conduire ? »", True),
        ("HUGO", "Cochez « non » si vous n'en avez pas. Ne laissez jamais une case vide.", True),
    ], notes="La phrase des disponibilités est exactement celle apprise en B4 : la "
             "même formulation sert à l'oral et à l'écrit.")

    d.tableau('Analyse', "Chaque case, et ce qu'on y écrit",
              ['La case', "Ce qu'on y met"],
              [["Nom de famille", "TRAORÉ, en lettres moulées, sans le prénom"],
               ["Prénom", "FANTA"],
               ["Adresse", "le numéro, la rue, l'appartement, le code postal"],
               ["Poste demandé", "aide à la cuisine, le poste exact de l'annonce"]],
              cle=0,
              note="Le poste demandé se recopie de l'annonce, mot pour mot.",
              notes="Diapo à photographier. La dernière ligne évite un flou fréquent : "
                    "« n'importe quoi » n'est pas un poste demandé.")

    d.tableau('Analyse · suite', "Le bas du formulaire",
              ['La case', "Ce qu'on y met"],
              [["Disponibilités", "du mardi au samedi, de 9 h à 13 h"],
               ["Permis de conduire", "une case cochée : oui ou non"],
               ["Signature", "son nom écrit à la main, toujours pareil"],
               ["Date", "le jour, le mois et l'année"]],
              cle=0,
              note="Une case vide n'est pas un « non » : c'est une réponse manquante.",
              notes="Diapo à photographier. Faire signer et dater une feuille blanche "
                    "à chacun : beaucoup n'ont jamais fixé leur signature.")

    d.regle("Les lettres moulées",
            "Des majuscules bien détachées, une par case.",
            precision="C'est demandé partout : sur un formulaire d'emploi, à la "
                      "clinique, à l'école. La raison est simple — personne ne doit se "
                      "tromper en lisant votre nom, et une machine doit pouvoir le lire "
                      "aussi.",
            notes="Diapo à photographier. Faire écrire son nom en lettres moulées sur "
                  "une grille dessinée au tableau, deux ou trois volontaires.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Hugo demande à Fanta de remplir un formulaire.", "vrai"),
        ("Il faut écrire en lettres attachées.", "faux — en lettres moulées"),
        ("Le nom de famille va dans la première case.", "vrai"),
        ("Pour « poste demandé », elle écrit « aide à la cuisine ».", "vrai"),
        ("On peut laisser une case vide si la réponse est non.", "faux — on coche non"),
        ("Fanta signe et met la date.", "vrai"),
    ], corrige=True,
       notes="Mêmes énoncés que l'exercice t3vf du module. Faire justifier chaque "
             "« faux » par la réplique exacte.")

    d.billet(
        "Écrivez votre nom de famille et votre prénom en lettres moulées.",
        exemples=[
            "Une lettre par case, bien détachées.",
            "Puis signez en dessous, à la main.",
        ],
        notes="Deux minutes. Ramasser : c'est le seul moment du module où l'on voit "
              "l'écriture de chacun, et où l'on peut corriger sans humilier.")

    return d.save(dossier)
