# -*- coding: utf-8 -*-
"""A4 · Depuis quand ça dure.
Bloc A « Je découvre » · couleur ambre · 75 min. Écriture.
Source : exercice `prDuree` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Depuis quand ça dure",
        chapeau="C'est la question qu'on vous posera dans les trente "
                "premières secondes, à chaque fois, par tout le monde. Une "
                "seule réponse à préparer : un chiffre et une unité.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Relire deux ou trois phrases du billet de "
                  "sortie de A3, puis annoncer que la séance porte sur la seule question "
                  "qui revient à tous les appels.")

    d.objectifs([
        "employer « depuis » avec une date et avec une durée ;",
        "employer « ça fait… que » à l'oral ;",
        "distinguer « depuis » de « il y a » et choisir le temps du verbe ;",
        "écrire trois phrases qui situent un problème dans la durée.",
    ])

    d.declencheur(
        'Observation', "« Ça fait longtemps, docteure. » Est-ce que ça renseigne "
                       "quelqu'un ?",
        image=IMG + 'calendrier-rendezvous.jpg',
        pistes=[
            "Longtemps, c'est combien ?",
            "Deux semaines ou deux ans ?",
            "Qu'est-ce que le médecin peut faire avec cette réponse ?",
            "Comment répondre autrement, en trois mots ?",
        ],
        notes="C'est la réponse spontanée de presque tous les élèves. Ne pas la corriger "
              "sèchement : montrer simplement qu'elle ne permet aucune décision.")

    d.regle("Avec « depuis », le verbe reste au présent",
            "« J'ai mal depuis trois mois » — et non « j'ai eu mal ».",
            precision="Ce présent est ce qui dit au médecin que le problème est encore là "
                      "aujourd'hui. Le passé composé, lui, ferait croire que c'est fini "
                      "et qu'on vient raconter une vieille histoire.",
            notes="Diapositive à photographier. C'est la seule règle de grammaire de la "
                  "séance, et elle rend la moitié du travail.")

    d.cartes("Trois façons de dire depuis quand", "Et ce qui les sépare", [
        ("depuis + un moment ou une durée",
         "Ça a commencé et ça continue. « J'ai des étourdissements depuis le mois de mars. »"),
        ("ça fait… que",
         "La même idée, à l'oral, avec la durée en tête. « Ça fait trois mois que ça dure. »"),
        ("il y a",
         "Un moment terminé, dans le passé, avec un passé composé. « Ça a commencé il y a trois mois. »"),
        ("depuis que + une phrase",
         "Quand le départ n'est pas une date mais un évènement. « Depuis que j'ai changé d'horaire… »"),
    ], notes="Les quatre disent presque la même chose. Conseiller aux élèves d'en choisir "
             "deux et de les rendre automatiques, plutôt que d'en savoir quatre à moitié.")

    d.tableau('Le test en une ligne', "Depuis, ou il y a ?",
              ['On peut ajouter…', 'Alors on emploie'],
              [["« et c'est encore le cas »", "depuis"],
               ["« et c'est fini »", "il y a"],
               ["j'ai mal ___ trois mois", "depuis (ça continue)"],
               ["ça a commencé ___ trois mois", "il y a (c'est daté)"]],
              cle=0,
              notes="Faire appliquer le test à voix haute sur les deux dernières lignes "
                    "avant de donner la réponse.")

    d.piege("Répondre « longtemps » à la question de la durée",
            "« Ça fait longtemps que j'ai ça. »",
            "« Ça fait environ trois mois. »",
            "« Longtemps » ne permet aucune décision : ni la durée du rendez-vous, ni "
            "l'ordre des examens. Un chiffre approximatif vaut infiniment mieux qu'un "
            "mot vague — « environ trois mois », « depuis le printemps ».",
            notes="Insister : personne n'exige une date exacte. C'est l'ordre de grandeur "
                  "qui compte, et il est toujours connu.")

    d.pratique('Écriture', "Complétez la phrase",
               "Avec depuis, ça fait… que, ou il y a.", [
        ("J'ai des étourdissements ___ le mois de mars.", "depuis"),
        ("___ trois mois que ça dure.", "Ça fait"),
        ("Ça a commencé ___ trois mois, un lundi matin.", "il y a"),
        ("___ que j'ai changé d'horaire, je dors moins.", "Depuis"),
        ("Je suis fatigué ___ des semaines.", "depuis"),
        ("J'ai arrêté le soccer ___ deux mois.", "il y a — c'est fini"),
    ], corrige=True,
       notes="Faire justifier la dernière : « j'ai arrêté » est un fait terminé, donc "
             "« il y a ». C'est le cas qui trompe le plus.")

    d.pratique('Production', "Deux phrases sur trois mois",
               "Écrivez, puis lisez à voix haute.", [
        ("Une phrase avec « depuis » et une date.", "J'ai mal au dos depuis le mois d'avril."),
        ("Une phrase avec « ça fait… que ».", "Ça fait six semaines que je dors mal."),
        ("Une phrase avec « il y a » et un passé composé.", "J'ai arrêté de courir il y a un mois."),
        ("Une phrase avec « depuis que ».", "Depuis que je travaille de nuit, je suis fatigué."),
    ], corrige=True,
       notes="Circuler pendant l'écriture et corriger le temps du verbe à voix basse, "
             "individuellement. C'est là que la règle entre vraiment.")

    d.billet(
        "Préparez la première phrase de votre appel : le problème, et depuis quand.",
        exemples=[
            "Une seule phrase, écrite en toutes lettres, prête à être lue au téléphone.",
            "Vous l'utiliserez telle quelle dans le défi 1.",
        ],
        notes="Ce billet est le matériau de B1 : le ramasser et le rendre au début de la "
              "séance suivante, corrigé.")

    return d.save(dossier)
