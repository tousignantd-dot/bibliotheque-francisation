# -*- coding: utf-8 -*-
"""D2 · Jusqu'à quand, et moins cher que quoi.
Bloc D « Défi 3 · Lire la grille des tarifs » · couleur ambre · 75 min.
Source : exercices `t3temps`, `t3compar` et `t3places`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Jusqu'à quand, et moins cher que quoi",
        chapeau="Chaque ligne de la grille dit un prix et une durée. Se "
                "tromper sur cinq petits mots, c'est acheter le mauvais titre.",
        duree='75 minutes')

    d.titre(notes="Deuxième et dernière séance du défi 3. Elle porte sur les mots "
                  "grammaticaux qui font la grille : les prépositions de temps et la "
                  "comparaison. Ouvrir en projetant la ligne « du vendredi 16 h au "
                  "lundi 5 h » et en demandant si le titre marche le samedi.")

    d.objectifs([
        "lire une durée : de… à…, du… au…, jusqu'à, à partir de, pendant ;",
        "comparer deux prix avec « plus cher que » et « moins cher que » ;",
        "lire une borne d'âge : 11 ans et moins, 65 ans et plus ;",
        "savoir qui a droit aux places réservées.",
    ])

    d.tableau('Analyse', "Les cinq mots qui disent une durée",
              ["Le mot", "Ce qu'il dit"],
              [["de… à…", "un début et une fin, avec des heures"],
               ["du… au…", "un début et une fin, avec des jours"],
               ["jusqu'à", "seulement la fin"],
               ["à partir de", "seulement le début"],
               ["pendant", "une longueur de temps qui se compte"]],
              cle=0,
              note="Devant un jour, « de » devient « du » et « à » devient « au ».",
              notes="Diapositive à photographier. Faire retrouver chacun des cinq dans "
                    "la grille projetée : ils y sont tous, et souvent dans la même "
                    "ligne.")

    d.tableau('Analyse', "Les cinq titres et leur durée",
              ["Le titre", "Comment c'est écrit"],
              [["Soirée illimitée", "valide de 18 h à 5 h"],
               ["Hebdo", "du lundi au dimanche"],
               ["Week-end illimité", "du vendredi 16 h au lundi 5 h"],
               ["Mensuel", "bon jusqu'à la fin du mois"],
               ["Correspondance", "pendant 120 minutes"]],
              cle=1,
              note="Le titre 24 h commence à partir de la validation, pas de l'achat.",
              notes="Diapositive à photographier. Insister sur la note : un titre 24 h "
                    "acheté le matin peut être commencé le soir. Beaucoup d'élèves "
                    "l'ignorent et le gaspillent.")

    d.piege('Lecture',
            "acheter un mensuel le 28 du mois",
            "acheter un mensuel en début de mois",
            "Un mensuel finit le dernier jour du mois, pas trente jours après "
            "l'achat. Acheté le 28, il ne sert que trois ou quatre jours pour "
            "cent dix dollars. C'est le piège de lecture le plus coûteux de la "
            "grille.",
            notes="Le faire calculer au tableau. Poser la question inverse : quel titre "
                  "prendre si on arrive au Québec le 25 du mois ? Réponse : un hebdo, "
                  "puis un mensuel le premier.")

    d.pratique('Lecture', "Le petit mot qui manque",
               "Complétez chaque ligne de la grille.", [
        ("Soirée illimitée : valide ___ 18 h à 5 h.", "de"),
        ("Hebdo : valide du lundi ___ dimanche.", "au"),
        ("Week-end illimité : ___ vendredi 16 h au lundi 5 h.", "du"),
        ("Le mensuel est bon ___ la fin du mois.", "jusqu'à"),
        ("La correspondance dure ___ cent vingt minutes.", "pendant"),
        ("Le titre 24 h est bon ___ partir de la validation.", "à"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 2 du défi 3. Faire relire chaque ligne complétée en "
             "montrant la case correspondante sur la grille projetée.")

    d.tableau('Analyse', "Comparer deux prix",
              ["La forme", "Exemple"],
              [["moins cher que", "l'hebdo est moins cher que le dix passages"],
               ["plus cher que", "le mensuel est plus cher que l'hebdo"],
               ["aussi cher que", "le dix passages est presque aussi cher que l'hebdo"],
               ["plus de / moins de", "moins de douze ans · plus de cinq enfants"]],
              cle=0,
              note="On compare avec « que ». Devant un nombre, c'est « de ».",
              notes="Diapositive à photographier. L'oubli du « que » est la faute la "
                    "plus fréquente à ce niveau et elle s'entend tout de suite. La "
                    "corriger une fois clairement.")

    d.pratique('Comparaison', "Plus cher, moins cher, plus de, moins de",
               "Complétez chaque phrase.", [
        ("L'hebdo à 33,25 $ est ___ le dix passages à 35 $.", "moins cher que"),
        ("Le mensuel à 110 $ est ___ l'hebdo à 33,25 $.", "plus cher que"),
        ("Les enfants de ___ douze ans voyagent gratuitement.", "moins de"),
        ("Une personne ne peut pas accompagner ___ cinq enfants.", "plus de"),
        ("Le tarif réduit à 66 $ est ___ le tarif ordinaire à 110 $.", "moins cher que"),
        ("Aller à Laval coûte ___ rester à Montréal.", "plus cher que"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 4 du défi 3. Rappeler que la borne d'un âge est toujours "
             "incluse : « 65 ans et plus » comprend une personne de soixante-cinq ans "
             "exactement.")

    d.cartes("Deux choses différentes, souvent confondues", "Les places et le service", [
        ("Les places réservées",
         "Les premières rangées de l'autobus ordinaire, juste après le chauffeur, "
         "signalées par un petit dessin. Pour les personnes à mobilité réduite, les "
         "femmes enceintes et les personnes âgées. On peut s'y asseoir, mais on se "
         "lève dès qu'une de ces personnes monte, sans attendre qu'elle demande."),
        ("Le transport adapté",
         "Un service à part, avec ses propres véhicules, pour les personnes qui ne "
         "peuvent pas prendre l'autobus ordinaire. Il faut s'inscrire une fois, avec "
         "un document médical, puis réserver chaque déplacement d'avance."),
    ], notes="Le programme nomme les deux dans la même ligne de son lexique, ce qui "
             "entretient la confusion. Les séparer clairement. Faire dire la phrase "
             "« Prenez ma place, madame » par tout le groupe : deux mots suffisent, et "
             "on ne discute pas.")

    d.billet(
        "Écrivez jusqu'à quand votre titre est bon, avec le bon petit mot.",
        exemples=[
            "Mon titre est bon ___ la fin du mois.",
            "L'hebdo va ___ lundi ___ dimanche.",
        ],
        notes="Devoir court. Dernier billet avant le bloc E : vérifier que les cinq "
              "petits mots sont acquis, ce sont eux qu'on retrouvera dans la production "
              "écrite de la séance E2.")

    return d.save(dossier)
