# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur foret · 60 min.
Source : cartes mémoire, banc de vocabulaire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='foret',
        titre='Je retiens des mots',
        chapeau="Quinze mots, six points de langue, une règle d'or. Dernière "
                "séance : on rassemble, on révise, et chacun fait le point sur "
                "ce qu'il sait maintenant faire.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Rendre tous les billets corrigés du module avant de "
                  "commencer.")

    d.objectifs([
        "rassembler le vocabulaire du module en quatre familles ;",
        "réviser avec les cartes mémoire, seul ou à deux ;",
        "reformuler les six points de langue en une phrase chacun ;",
        "évaluer honnêtement ce que je suis maintenant capable de faire.",
    ])

    d.vocabulaire('Famille · 1 de 4', "Dans la rue", [
        ("un coin de rue", "L'endroit où deux rues se croisent."),
        ("un feu de circulation", "Le signal lumineux rouge, jaune et vert."),
        ("un trottoir", "La partie réservée aux piétons."),
        ("traverser", "Passer d'un côté à l'autre."),
        ("un sentier", "Un petit chemin de terre, dans un parc."),
    ], notes="Faire redire l'article avec chaque mot. Dernière occasion de le corriger.")

    d.vocabulaire('Famille · 2 de 4', "Dans le transport", [
        ("un terminus", "Le dernier arrêt d'une ligne — il donne la direction."),
        ("un quai", "L'endroit où on attend avant de monter."),
        ("une correspondance", "Le changement d'une ligne à une autre."),
        ("la direction", "Le sens dans lequel va un véhicule."),
        ("un titre de transport", "La carte ou le billet qui donne le droit de monter."),
    ], notes="Ces cinq mots sont ceux dont un élève a besoin dès sa première semaine ici.")

    d.vocabulaire('Famille · 3 de 4', "Ce qu'on cherche des yeux", [
        ("une enseigne", "Le panneau qui porte le nom d'un commerce."),
        ("un édifice", "Un bâtiment, souvent grand, avec des bureaux ou des logements."),
        ("un panneau", "L'affiche qui indique la direction."),
        ("un escalier", "Souvent le point de décision dans un itinéraire intérieur."),
        ("en face de", "De l'autre côté, vis-à-vis."),
    ], notes="Faire employer chacun dans une phrase d'itinéraire réelle, tirée du quartier "
             "de l'école.")

    d.vocabulaire('Famille · 4 de 4', "Sur un horaire ou un plan", [
        ("un horaire", "Le tableau des heures de passage."),
        ("un plan de réseau", "La carte de toutes les lignes, une couleur par ligne."),
        ("la fréquence", "Le temps entre deux passages."),
        ("desservir un arrêt", "S'y arrêter."),
        ("une interruption de service", "L'arrêt temporaire d'une ligne."),
    ], notes="« Desservir » et « interruption de service » sont les deux mots des annonces. "
             "Dernier rappel.")

    d.tableau('Les six points de langue', "Une phrase chacun",
              ['Le point', 'En une phrase'],
              [["les consonnes qui tombent", "rends au mot sa dernière consonne"],
               ["l'impératif", "pas de sujet, et pas de -s en -er"],
               ["jusqu'à, vers, par", "où j'arrête, de quel côté, par où"]],
              cle=1,
              note="Trois autres au tableau suivant.",
              notes="Faire reformuler chaque ligne par un élève différent avant d'afficher "
                    "la colonne de droite.")

    d.tableau('Les six points de langue', "Une phrase chacun (suite)",
              ['Le point', 'En une phrase'],
              [["les repères de lieu", "un repère fixe ne se trompe jamais de côté"],
               ["celui, celle, ceux", "jamais tout seul"],
               ["l'horaire et le plan", "le terminus donne la direction"]],
              cle=1,
              notes="La dernière ligne est la règle d'or du module. La faire répéter par "
                    "tout le groupe.")

    d.regle("Ce qu'il faut retenir du module",
            "Le nom du terminus donne la direction. Et on répète toujours l'itinéraire "
            "avant de partir.",
            precision="Ces deux réflexes valent plus que tout le vocabulaire de la semaine. "
                      "Le premier empêche de partir dans le mauvais sens ; le second, "
                      "d'oublier la moitié du chemin.",
            notes="Diapo à photographier. C'est la phrase de clôture du module.")

    d.cartes('Réviser seul', "Trois façons de le faire", [
        ("Les cartes mémoire",
         "Dans l'activité interactive, section « Je retiens des mots ». La traduction est "
         "masquée par défaut : essayez d'abord."),
        ("Les trois exercices de vocabulaire",
         "Le mot et sa définition, le mot et l'image, le mot à écrire. Les trois portent "
         "sur les mêmes quinze mots."),
        ("Les six mini-leçons",
         "Six panneaux « En apprendre plus », avec de l'audio. Ils restent accessibles "
         "après la fin du module."),
    ], notes="Montrer les trois à l'écran, une minute chacun. Beaucoup ignorent que le "
             "module reste ouvert après la dernière séance.")

    d.billet(
        "Autoévaluation : pour chaque énoncé, pas encore, un peu, ou oui.",
        exemples=[
            "Je peux demander mon chemin et comprendre la réponse du premier coup.",
            "Je peux expliquer un trajet à l'impératif, étape par étape.",
            "Je peux lire un horaire et un plan sans me tromper de direction.",
        ],
        notes="L'autoévaluation complète est dans l'activité interactive, section « Je "
              "retiens des mots ». La faire remplir là : elle est conservée avec les traces "
              "de l'élève.")

    return d.save(dossier)
