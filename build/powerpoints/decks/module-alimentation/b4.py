# -*- coding: utf-8 -*-
"""B4 · Garder, congeler, jeter.
Bloc B · couleur acier · 55 min.
Source : exercice `t1conserv`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-alimentation/images/')


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre='Garder, congeler, jeter',
        chapeau="Deux jours, trois jours, trois mois. Les durées de "
                "conservation ne s'inventent pas — et les connaître, c'est de "
                "l'argent qui reste dans le portefeuille.",
        duree='55 minutes')

    d.titre(notes="Séance de vocabulaire et de savoir pratique. Elle clôt le bloc B. "
                  "Question d'entrée : « combien jetez-vous, chaque semaine ? »")

    d.objectifs([
        "nommer les durées de conservation des aliments courants ;",
        "savoir comment emballer avant de congeler ;",
        "ranger le réfrigérateur : ce qui va en haut, ce qui va en bas ;",
        "distinguer un aliment abîmé d'un aliment simplement moins bon.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui va où, dans ce réfrigérateur ?",
        image=IMG + 'frigo-bas.jpg',
        pistes=[
            "Où mettez-vous la viande et le poisson ?",
            "Où mettez-vous les restes de la veille ?",
            "Quel est l'endroit le plus froid, selon vous ?",
            "Qu'est-ce qui ne va pas au réfrigérateur du tout ?",
        ],
        notes="La dernière piste amène les tomates, les pommes de terre, les oignons, le "
              "pain — plusieurs élèves les réfrigèrent par habitude.")

    d.tableau('Analyse', "Combien de temps au réfrigérateur",
              ['Aliment', 'Durée'],
              [["Poisson frais", "2 jours"],
               ["Bœuf haché", "2 jours"],
               ["Jambon tranché ouvert", "3 jours"],
               ["Viande en morceaux", "3 à 5 jours"],
               ["Restes cuisinés", "3 jours"]],
              cle=0,
              note="Les deux premiers sont les plus fragiles du comptoir.",
              notes="Diapo à photographier. Ces durées sont celles des autorités "
                    "sanitaires canadiennes : elles ne se discutent pas.")

    d.cartes('Bien congeler', "Quatre règles", [
        ("Congeler tout de suite",
         "Le jour de l'achat, pas le surlendemain. Congeler un aliment déjà vieux de deux "
         "jours ne le rajeunit pas."),
        ("Bien emballer",
         "Sac refermable ou contenant hermétique. Sinon, l'aliment sèche et prend le goût "
         "du congélateur."),
        ("Étiqueter la date",
         "Un ruban et un crayon suffisent. Sans date, on ne sait plus, et on finit par "
         "jeter."),
        ("Décongeler au réfrigérateur",
         "Jamais sur le comptoir. La veille, dans le bas du frigo : c'est plus long, mais "
         "c'est la seule façon sûre."),
    ], notes="La troisième carte est la plus utile et la plus simple à adopter. Beaucoup de "
             "gaspillage vient de sacs non datés.")

    d.regle('Le rangement du réfrigérateur',
            "Viande et poisson en bas. Toujours.",
            precision="Deux raisons : le bas est l'endroit le plus froid, et si l'emballage "
                      "fuit, le jus ne coule sur rien. Les restes cuisinés et les produits "
                      "laitiers vont plus haut ; les légumes, dans le tiroir.",
            notes="Diapo à photographier. C'est une règle d'hygiène de base, rarement "
                  "enseignée.")

    d.piege("Jeter après la date",
            "C'était « meilleur avant » hier, je jette.",
            "« Meilleur avant » est une date de qualité. Je regarde, je sens.",
            "Beaucoup d'aliments restent parfaitement bons plusieurs jours après cette "
            "date : yogourt, fromage, conserves, pâtes sèches. Ce qui décide, c'est "
            "l'aspect et l'odeur. Seule « date limite d'utilisation » est une date de "
            "sécurité.",
            notes="Point à traiter avec doigté : certains élèves ont une règle stricte pour "
                  "des raisons de santé. Nuancer sans imposer.")

    d.vocabulaire('Vocabulaire', "Garder les aliments", [
        ("emballer", "Envelopper pour protéger."),
        ("congeler", "Mettre au congélateur pour garder longtemps."),
        ("décongeler", "Ramener à température, de préférence au réfrigérateur."),
        ("un contenant hermétique", "Une boîte qui ferme complètement, sans laisser passer l'air."),
        ("se conserver", "Se garder. « Ça se conserve trois jours. »"),
    ], notes="« Hermétique » est un mot précis et utile ; il figure sur beaucoup "
             "d'emballages.")

    d.pratique('Pratique', "Combien de temps, et où ?",
               "Répondez pour chaque aliment.", [
        ("Du poisson frais acheté aujourd'hui", "2 jours, dans le bas du frigo"),
        ("Du bœuf haché", "2 jours au frigo, 3 mois congelé"),
        ("Du jambon tranché, ouvert hier", "3 jours, contenant fermé"),
        ("Une conserve non ouverte", "des mois, dans l'armoire"),
        ("Un reste de repas d'hier", "3 jours, contenant fermé"),
    ], corrige=True, cols=1,
       notes="Faire répondre à voix haute avant d'afficher. Ces durées se retiennent par "
             "répétition, pas par explication.")

    d.billet(
        "Faites le tour de votre réfrigérateur et notez trois choses à changer.",
        exemples=[
            "Ce qui est mal placé, ce qui n'est pas daté, ce qui devrait être congelé.",
            "Trois lignes suffisent.",
        ],
        notes="Bilan du bloc B. Devoir très concret : plusieurs élèves reviennent en "
              "disant qu'ils ont réorganisé tout le frigo.")

    return d.save(dossier)
