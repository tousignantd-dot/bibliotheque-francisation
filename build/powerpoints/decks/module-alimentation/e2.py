# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur framboise · 60 min.
Source : cartes mémoire, banc de vocabulaire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Quinze mots, sept points de langue, quatre questions de "
                "comptoir. Dernière séance : on rassemble, on révise, et "
                "chacun fait le point.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer.")

    d.objectifs([
        "rassembler le vocabulaire du module en quatre familles ;",
        "réviser avec les cartes mémoire, seul ou à deux ;",
        "reformuler les points de langue en une phrase chacun ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire.",
    ])

    d.vocabulaire('Famille · 1 de 4', "Dans le magasin", [
        ("une allée", "Le corridor entre deux rangées d'étagères."),
        ("une conserve", "Un aliment vendu dans une boîte de métal."),
        ("un comptoir", "L'endroit où un employé sert les clients."),
        ("une étiquette", "Le papier collé sur un produit."),
        ("la provenance", "Le pays ou la région d'où vient un produit."),
    ], notes="Faire redire l'article avec chaque mot. Dernière occasion de le corriger.")

    d.vocabulaire('Famille · 2 de 4', "Commander et mesurer", [
        ("une livre", "Environ 454 grammes — encore très employée ici."),
        ("le bœuf haché", "De la viande de bœuf passée au hachoir."),
        ("une poitrine", "Un morceau de poulet, vendu à l'unité ou au poids."),
        ("tranché mince", "Coupé en tranches fines, à la charcuterie."),
        ("la balance", "L'appareil qui donne le poids et le prix."),
    ], notes="Ces cinq mots suffisent pour commander à n'importe quel comptoir.")

    d.vocabulaire('Famille · 3 de 4', "Garder les aliments", [
        ("emballer", "Envelopper pour protéger."),
        ("congeler", "Mettre au congélateur pour garder longtemps."),
        ("se conserver", "Se garder. « Ça se conserve trois jours. »"),
        ("un contenant hermétique", "Une boîte qui ferme complètement."),
        ("la date de péremption", "La date après laquelle on ne consomme plus."),
    ], notes="« Se conserver » réunit le vocabulaire et le point de langue de B3.")

    d.vocabulaire('Famille · 4 de 4', "Lire une étiquette", [
        ("la valeur nutritive", "Le tableau des calories, du sodium et des sucres."),
        ("la portion", "La quantité à laquelle tous les chiffres du tableau se rapportent."),
        ("un mode d'emploi", "Le texte qui explique comment utiliser un produit."),
        ("diluer", "Mélanger avec de l'eau pour rendre moins fort."),
        ("un avertissement", "Un texte qui prévient d'un danger."),
    ], notes="« La portion » est le mot le plus important du bloc D. Dernier rappel.")

    d.tableau('Les points de langue', "Une phrase chacun",
              ['Le point', 'En une phrase'],
              [["la liaison des quantités", "c'est le mot suivant qui décide"],
               ["du, de la, des", "le nom décide, pas la quantité"],
               ["pas de, une livre de", "négation ou quantité : toujours « de »"]],
              cle=1,
              note="Quatre autres au tableau suivant.",
              notes="Faire reformuler chaque ligne par un élève différent avant d'afficher "
                    "la colonne de droite.")

    d.tableau('Les points de langue', "Une phrase chacun (suite)",
              ['Le point', 'En une phrase'],
              [["ça se garde", "la chose est le sujet, personne n'est nommé"],
               ["le pronom en", "devant le verbe, la quantité reste"],
               ["livres et grammes", "les deux sont compris partout"],
               ["l'étiquette", "portion, sodium, sucres — trois lignes"]],
              cle=1,
              notes="La dernière ligne est celle que les élèves rapportent le plus souvent "
                    "comme utile. La faire répéter.")

    d.regle("Ce qu'il faut retenir du module",
            "Demandez, et vérifiez avant de partir.",
            precision="Farida n'a pas appris le français en douze semaines. Elle a appris à "
                      "demander où est un produit, combien de temps il se garde, et combien "
                      "ça coûte en tout. Trois questions qui lui font gagner du temps et de "
                      "l'argent chaque semaine.",
            notes="Diapo à photographier. C'est la phrase de clôture du module.")

    d.cartes('Réviser seul', "Trois façons de le faire", [
        ("Les cartes mémoire",
         "Dans l'activité interactive, section « Je retiens des mots ». La traduction est "
         "masquée par défaut."),
        ("Les trois exercices de vocabulaire",
         "Le mot et sa définition, le mot et l'image, le mot à écrire. Les mêmes quinze "
         "mots."),
        ("Les sept mini-leçons",
         "Sept panneaux « En apprendre plus », avec de l'audio. Ils restent accessibles "
         "après la fin du module."),
    ], notes="Montrer les trois à l'écran, une minute chacun.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux commander à un comptoir en donnant une quantité avec la bonne unité.",
            "Je peux demander comment un aliment se garde et se prépare.",
            "Je peux lire les trois lignes qui comptent sur une étiquette.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive. La faire remplir "
              "là : elle est conservée avec les traces de l'élève.")

    return d.save(dossier)
