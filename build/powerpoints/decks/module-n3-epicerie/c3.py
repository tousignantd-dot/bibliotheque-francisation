# -*- coding: utf-8 -*-
"""C3 · Lire la circulaire.
Bloc C « Défi 2 » · couleur ambre · 60 min.
Source : exercice `t2circulaire`. Séance qui s'appuie sur les circulaires
apportées par les élèves (billet de C1).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Lire la circulaire',
        chapeau="Six mentions à repérer, et le reste est du décor. Une fois "
                "qu'on sait où regarder, une circulaire se lit en deux "
                "minutes.",
        duree='60 minutes')

    d.titre(notes="Séance pratique : les élèves travaillent sur les circulaires qu'ils ont "
                  "apportées. En avoir quelques-unes de réserve.")

    d.objectifs([
        "repérer six mentions dans une circulaire ;",
        "calculer ce qu'un spécial fait économiser ;",
        "reconnaître un faux rabais ;",
        "préparer une liste à partir des spéciaux.",
    ])

    d.declencheur(
        'Observation', "Ouvrez votre circulaire. Que voyez-vous en premier ?",
        pistes=[
            "Un gros chiffre ?",
            "Une photo ?",
            "Où est le prix régulier ?",
            "Où est la date de fin ?",
        ],
        notes="Le gros chiffre attire l'œil ; le prix régulier et la date sont écrits "
              "petit. Ce n'est pas un hasard, et le dire.")

    d.tableau('Analyse', "Les six mentions",
              ['La mention', "Ce qu'elle dit"],
              [["Le gros prix", "le prix du spécial"],
               ["Prix régulier", "ce que ça coûte les autres semaines"],
               ["/ lb ou / kg", "le prix est au poids"],
               ["2 pour 5 $", "il faut en prendre deux"]],
              cle=1,
              note="Sans le prix régulier, on ne sait pas si le rabais est réel.",
              notes="Diapo à photographier. Deux autres mentions au tableau suivant.")

    d.tableau('Analyse', "Les six mentions (suite)",
              ['La mention', "Ce qu'elle dit"],
              [["Jusqu'au 27", "la date de fin"],
               ["Limite de 4", "au-delà, c'est le prix régulier"]],
              cle=0,
              note="La date est toujours écrite, toujours en petit, toujours en bas.",
              notes="Faire chercher ces deux mentions sur les circulaires apportées.")

    d.regle("Calculer l'économie réelle",
            "Prix régulier moins prix du spécial, fois la quantité.",
            precision="Le poulet passe de 4,79 $ à 3 $ la livre : l'économie est de "
                      "<b>1,79 $ la livre</b>. Pour trois livres, cela fait <b>5,37 $</b>. "
                      "C'est ce chiffre-là qui compte, pas la taille du rabais annoncé.",
            notes="Diapo à photographier. Faire le calcul au tableau avec un exemple tiré "
                  "d'une circulaire de la classe.")

    d.cartes("Trois faux rabais", "À reconnaître", [
        ("Le spécial sur un autre format",
         "Le rabais vaut pour le format de 500 ml ; celui de 1 litre est au prix régulier, "
         "juste à côté."),
        ("Le « 2 pour 5 $ » qui n'économise rien",
         "Si un seul article coûte 2,50 $, « 2 pour 5 $ » n'est pas un rabais du tout — "
         "c'est le prix normal, présenté autrement."),
        ("Le prix régulier gonflé",
         "Un « prix régulier » qu'on ne voit jamais le reste de l'année. Le seul contrôle "
         "est de connaître le prix habituel de ce qu'on achète."),
    ], notes="Ne pas transformer la séance en procès du commerce : donner les outils de "
             "lecture, c'est tout.")

    d.piege("Se déplacer pour un seul spécial",
            "Trois magasins pour économiser quatre dollars.",
            "Le temps et le transport comptent aussi.",
            "Deux dollars de billet d'autobus et quarante minutes de trajet effacent le "
            "rabais. Les spéciaux servent à ajuster une liste dans un magasin où l'on va "
            "déjà — pas à courir la ville.",
            notes="Conseil réaliste, surtout pour des élèves sans automobile.")

    d.pratique('Pratique · 1 de 2', "Que veut dire cette mention ?",
               "Répondez en une phrase.", [
        ("« 2 pour 5 $ »", "il faut en prendre deux ; un seul coûte plus cher"),
        ("« 3,99 $ / lb »", "le prix d'une livre — le total dépend du poids"),
        ("« Jusqu'au mercredi 27 »", "la date de fin du spécial"),
        ("« Limite de 4 par famille »", "au-delà de quatre, c'est le prix régulier"),
        ("« Prix régulier 6,49 $ »", "le prix des autres semaines"),
        ("« Quantités limitées »", "il peut ne plus y en avoir : venir tôt"),
    ], corrige=True,
       notes="Utiliser l'exercice 3 du module.")

    d.pratique('Pratique · 2 de 2', "Votre liste de la semaine",
               "À deux, avec vos circulaires.", [
        ("Étape 1", "trouver trois produits que vous achetez d'habitude"),
        ("Étape 2", "noter le prix régulier et le prix du spécial"),
        ("Étape 3", "calculer l'économie pour la quantité qu'il vous faut"),
        ("Étape 4", "dire à votre voisin lequel vaut la peine, et pourquoi"),
    ], cols=1,
       notes="Vingt-cinq minutes. C'est l'activité la plus utile du bloc C : elle produit "
             "une vraie liste, avec de vrais chiffres.")

    d.billet(
        "Écrivez ce que votre liste vous fera économiser cette semaine.",
        exemples=[
            "Trois produits, trois calculs.",
            "Le total : combien en tout ?",
        ],
        notes="Ramasser. Les totaux se comparent bien en début de séance suivante.")

    return d.save(dossier)
