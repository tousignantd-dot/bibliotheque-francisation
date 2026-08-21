# -*- coding: utf-8 -*-
"""A3 · Les mots du déménagement.
Bloc A « Je découvre » · couleur framboise · vocabulaire · 75 min.
Source : `FC_CARDS`, exercices `prVocab` et `prImg`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-emmenagement/images/')


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les mots du déménagement",
        chapeau="Seize mots pour six semaines : ceux des clés, ceux du camion, "
                "ceux de l'adresse et ceux de l'immeuble.",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Elle prépare tout le module : chacun de ces mots "
                  "revient dans un dialogue ou dans un exercice des blocs suivants.")

    d.objectifs([
        "nommer les objets du déménagement ;",
        "employer chaque mot avec son article ;",
        "associer un mot à sa définition et à une image ;",
        "commencer son propre banc de mots.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on voit sur cette photo, et à quoi ça sert ?",
        image=IMG + 'diable-charge.jpg',
        pistes=[
            "Comment ça s'appelle en français ?",
            "Pourquoi deux roues et pas quatre ?",
            "Qui le fournit : vous ou la compagnie ?",
            "Qu'est-ce qu'on met dessus en premier ?",
        ],
        notes="Le mot « diable » surprend toujours. Le donner après avoir laissé le groupe "
              "chercher : c'est un mot qu'on n'oublie plus une fois qu'on l'a entendu.")

    d.vocabulaire('Vocabulaire · 1 de 3', "Les clés et l'état des lieux", [
        ("emménager", "Entrer dans un logement neuf pour y vivre, avec ses affaires."),
        ("l'état des lieux", "La liste écrite de ce qui est déjà abîmé le jour de l'entrée."),
        ("un carton", "La grande boîte de papier épais qui sert à transporter."),
        ("un diable", "Le petit chariot à deux roues pour rouler une charge lourde."),
        ("une égratignure", "Une marque longue et mince laissée sur une surface dure."),
    ], notes="Opposer « déménager » (partir) et « emménager » (arriver). La paire est "
             "difficile et elle est au cœur du module.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Le camion et la compagnie", [
        ("un tarif horaire", "Le prix demandé pour chaque heure de travail."),
        ("le temps de déplacement", "Le temps du camion pour venir et retourner, qu'on paie aussi."),
        ("une couverture de déménagement", "La pièce de tissu épais qui protège un meuble."),
        ("un dépôt", "L'argent versé d'avance pour garder une date."),
    ], notes="Ces quatre mots sont ceux du bloc B. Les faire répéter avec leur article : "
             "« un dépôt de cent dollars », « le temps de déplacement ».")

    d.vocabulaire('Vocabulaire · 3 de 3', "L'adresse et l'immeuble", [
        ("un relevé de compteur", "Le nombre lu sur l'appareil qui mesure l'électricité."),
        ("brancher", "Faire arriver l'électricité, l'eau ou Internet jusque chez soi."),
        ("le réacheminement du courrier", "Le service qui fait suivre vos lettres."),
        ("le bac brun", "Le bac des restes de table et des pelures."),
        ("le déneigement", "Le travail qui consiste à enlever la neige des rues."),
        ("rendre service", "Faire quelque chose pour aider quelqu'un, sans être payé."),
    ], notes="« Rendre service » est le seul verbe de la liste, et c'est celui du défi 3. "
             "Le faire employer tout de suite dans une phrase.")

    d.pratique('Association', "Le mot et sa définition",
               "L'enseignante lit la définition ; le groupe donne le mot avec son "
               "article.", [
        ("La liste de ce qui est déjà abîmé le jour de l'entrée.", "l'état des lieux"),
        ("Le chariot à deux roues.", "un diable"),
        ("Le prix pour chaque heure de travail.", "un tarif horaire"),
        ("La pièce de tissu épais qui protège un meuble.", "une couverture de déménagement"),
        ("Le bac des restes de table.", "le bac brun"),
        ("L'argent versé d'avance pour garder une date.", "un dépôt"),
    ], corrige=True,
       notes="C'est l'exercice prVocab du module, fait à l'oral d'abord. Refuser les "
             "réponses sans article.")

    d.pratique('Images', "Quelle photo pour quelle phrase ?",
               "Chacun décrit une des huit photos de l'exercice prImg.", [
        ("Ce qu'on remplit pendant les deux semaines qui précèdent.", "la pile de cartons"),
        ("Le chariot à deux roues.", "le diable chargé"),
        ("Ce qu'on réserve six semaines d'avance.", "le camion de déménagement"),
        ("Ce qui tourne serré et ralentit les déménageurs.", "l'escalier extérieur"),
        ("L'appareil dont il faut relever le nombre.", "le compteur électrique"),
        ("Le local commun du sous-sol.", "la salle de lavage"),
    ], corrige=True,
       notes="Projeter les photos de l'activité interactive au fur et à mesure. Les élèves "
             "manipuleront les mêmes ensuite, à l'écran.")

    d.billet(
        "Écrivez cinq mots de la séance dans votre carnet, avec leur article.",
        exemples=[
            "Ajoutez pour chacun une phrase à vous, pas celle du cours.",
            "Un mot que vous n'avez jamais employé ne se retient pas.",
        ],
        notes="Le carnet de mots est celui de la section « Je retiens des mots » du "
              "module : c'est le même travail, sur papier puis à l'écran.")

    return d.save(dossier)
