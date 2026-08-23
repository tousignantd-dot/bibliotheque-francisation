# -*- coding: utf-8 -*-
"""A3 · Les mots du recrutement et les lieux du processus
Bloc A « Je découvre » · couleur framboise · 60 min.
Source : exercices `prVocab` et `prImg`, banc `FC_CARDS`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-recherche' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Seize mots, et onze qui ne s'illustrent pas",
        chapeau="Le vocabulaire d'un processus de sélection est abstrait : "
                "un échelon, une contrepartie, un motif. Il ne se retient pas "
                "en regardant une photo, il se retient en s'en servant.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire. Prévenir le groupe dès le début : cinq mots "
                  "seulement ont une image dans le module, et ce n'est pas un oubli. "
                  "Les onze autres ne se voient pas.")

    d.objectifs([
        "comprendre et employer les seize mots du module ;",
        "distinguer ce qui se photographie de ce qui ne se photographie pas ;",
        "associer les lieux du processus à ce qui s'y passe ;",
        "employer chaque mot dans une phrase tirée de sa propre expérience.",
    ], notes="Le deuxième objectif n'est pas décoratif : il prépare la lecture des "
             "documents du bloc C, qui sont abstraits d'un bout à l'autre.")

    d.declencheur(
        'Observation', "Ces cinq lieux, à quel moment du processus appartiennent-ils ?",
        image=IMG + 'salle-examen.jpg',
        pistes=[
            "Qu'est-ce que ces quatre personnes sont en train de faire ?",
            "Qu'est-ce qu'il n'y a pas sur la table ?",
            "Combien de temps dure une épreuve comme celle-là, à votre avis ?",
            "Est-ce qu'on cherche la bonne réponse, ou autre chose ?",
        ],
        notes="La question du « rien d'autre sur la table » est celle qui ouvre la "
              "discussion : ni téléphone, ni notes, ni ordinateur. C'est voulu.")

    d.vocabulaire('Vocabulaire 1 de 3', "Le processus", [
        ("un processus de sélection", "L'ensemble des étapes qu'un employeur fait franchir avant de choisir quelqu'un."),
        ("la présélection", "Le premier tri, souvent fait par téléphone, avant les vraies rencontres."),
        ("une mise en situation", "Un cas inventé qu'on donne à résoudre pour voir comment quelqu'un réfléchit."),
        ("une entrevue de groupe", "Une rencontre où plusieurs candidats sont reçus et observés en même temps."),
        ("un accusé de réception", "Le court message qui confirme qu'un envoi est bien arrivé, sans rien décider."),
        ("un motif de discrimination", "Une caractéristique personnelle qu'on n'a pas le droit d'invoquer contre quelqu'un."),
    ], notes="Le dernier sera repris en entier au bloc D. Ne pas l'expliquer "
             "longuement ici : le nommer suffit.")

    d.vocabulaire('Vocabulaire 2 de 3', "L'usine et le quart", [
        ("un contremaître", "La personne qui dirige une équipe directement sur le plancher d'une usine."),
        ("un quart de soir", "La période de travail qui commence en après-midi et se termine tard le soir."),
        ("une chaîne de production", "La suite de machines et de postes où un produit se fabrique du début à la fin."),
        ("un temps d'arrêt", "Le moment où une machine ne produit pas, prévu ou non."),
        ("un carnet de commandes", "L'ensemble des commandes déjà reçues et pas encore livrées."),
        ("le taux de roulement", "La proportion du personnel qui quitte une entreprise dans une année."),
    ], notes="Ce sont les six mots les plus concrets du module, et ce sont ceux qui "
             "servent à lire le profil d'entreprise du bloc C. Les faire employer "
             "dans une phrase chacun.")

    d.vocabulaire('Vocabulaire 3 de 3', "Les conditions", [
        ("une acquisition", "Le rachat d'une entreprise par une autre."),
        ("un échelon", "Un des degrés d'une échelle de salaires, à l'intérieur d'un même poste."),
        ("une contrepartie", "Ce qu'on offre en échange de ce qu'on demande."),
        ("le service continu", "Le temps travaillé sans interruption chez un même employeur."),
    ], notes="Quatre mots seulement, et ce sont les plus difficiles. « Contrepartie » "
             "est le mot pivot de tout le défi 3 : le poser soigneusement.")

    d.tableau('Analyse', "Pourquoi onze mots n'ont pas de photo",
              ['Se photographie', 'Ne se photographie pas'],
              [["un contremaître, un quart de soir",
                "une présélection, un échelon"],
               ["une chaîne, un temps d'arrêt",
                "une contrepartie, le service continu"],
               ["une entrevue de groupe",
                "un motif de discrimination, une acquisition"]],
              cle=0,
              notes="Diapositive à photographier. La leçon vaut au-delà du module : un "
                    "mot abstrait se retient par un exemple, jamais par une image, et "
                    "une image posée derrière lui montre le thème à sa place.")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec un mot du module.", [
        ("La ___ se fait par téléphone et dure une vingtaine de minutes.", "présélection"),
        ("L'échelle compte six ___, et on n'embauche pas toujours au premier.", "échelons"),
        ("Leur ___ a doublé en dix-huit mois : il a fallu ouvrir un troisième quart.", "carnet de commandes"),
        ("Un ___ de onze pour cent est bas pour ce secteur : les gens restent.", "taux de roulement"),
        ("Elle n'a pas demandé : elle a offert une ___ datée et mesurable.", "contrepartie"),
        ("Le ___ se compte chez un même employeur, sans interruption.", "service continu"),
    ], corrige=True,
       notes="Faire lire la phrase entière une fois le mot trouvé. Les six phrases sont "
             "réutilisables telles quelles dans une lettre.")

    d.pratique('Association', "Le lieu et le moment",
               "Reliez chaque lieu à ce qui s'y passe.", [
        ("Une longue table, quatre personnes, une feuille chacune", "l'examen écrit"),
        ("Deux chaises d'un côté, une seule de l'autre", "l'entrevue individuelle"),
        ("Une table ronde, quatre bloc-notes fermés", "l'entrevue de groupe"),
        ("Un stationnement sous la neige, vingt-trois heures trente", "la fin d'un quart de soir"),
        ("Deux tasses vides devant une vitrine", "se renseigner avant de postuler"),
    ], corrige=True,
       notes="Reprend l'exercice d'association du module. Le dernier n'est pas une "
             "étape du processus : c'est ce qu'on fait avant, et personne ne le fait.")

    d.billet(
        "Choisissez trois mots du module et écrivez une phrase avec chacun.",
        exemples=[
            "Une phrase qui parle de votre métier, pas de Boréalis.",
            "Au moins une des trois au conditionnel.",
        ],
        notes="Le conditionnel n'a pas encore été vu : c'est volontaire. Les phrases "
              "produites servent d'amorce à la séance B2.")

    return d.save(dossier)
