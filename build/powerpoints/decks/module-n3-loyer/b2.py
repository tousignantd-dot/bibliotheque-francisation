# -*- coding: utf-8 -*-
"""B2 · Une annonce écrite en abrégé.
Bloc B « Défi 1 · Lire la petite annonce » · couleur ambre · 75 min.
Source : exercice `t1abrev` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre='Une annonce écrite en abrégé',
        chapeau="Une annonce n'est pas une phrase : c'est une liste, sans "
                "verbe, où les mots longs sont coupés. Dix abréviations "
                "suffisent à les lire toutes.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture. Ouvrir en projetant une annonce complète sans rien "
                  "expliquer, et demander au groupe ce qu'il comprend. La liste des mots "
                  "incompris est le programme de la séance.")

    d.objectifs([
        "reconnaître les abréviations d'une petite annonce de logement ;",
        "lire une abréviation à voix haute, en phrase complète ;",
        "savoir que le point d'une abréviation ne finit pas une phrase ;",
        "trouver dans l'annonce les quatre renseignements qui comptent.",
    ])

    d.regle("Une annonce se paie à la ligne",
            "Alors elle coupe tout ce qu'elle peut couper",
            precision="Il n'y a ni verbe, ni phrase complète : seulement des "
                      "renseignements séparés par des virgules. Les mots longs "
                      "sont raccourcis et suivis d'un point. Ce point ne finit "
                      "pas une phrase : il dit que le mot est coupé.",
            notes="Diapositive à photographier. Cette explication rassure : les élèves "
                  "croient souvent que leur français est en cause, alors que c'est la "
                  "forme même de l'annonce qui empêche de lire.")

    d.tableau('Analyse', "Les abréviations du logement",
              ["Dans l'annonce", "On lit"],
              [["4 ½", "un quatre et demie"],
               ["2e ét.", "deuxième étage"],
               ["ch. et écl.", "chauffé et éclairé"],
               ["s.-sol", "sous-sol"]],
              cle=0,
              note="Le point dit que le mot est coupé, pas que la phrase finit.",
              notes="Diapositive à photographier. Premier des deux tableaux "
                    "d'abréviations. Faire lire chaque ligne à voix haute en phrase "
                    "complète : c'est ainsi qu'on les retient.")

    d.tableau('Analyse', "Les abréviations du logement — la suite",
              ["Dans l'annonce", "On lit"],
              [["stat.", "stationnement"],
               ["libre imm.", "libre immédiatement"],
               ["libre 1er juill.", "libre le premier juillet"],
               ["n/c", "non chauffé"]],
              cle=0,
              note="n/c ne veut pas dire « non compris » : c'est le chauffage.",
              notes="Diapositive à photographier. « n/c » est le piège classique. "
                    "Insister : c'est une abréviation qui change complètement le calcul "
                    "du prix.")

    d.tableau('Analyse', "L'annonce du quatre et demie, ligne par ligne",
              ["La ligne", "Ce qu'elle dit"],
              [["4 ½, rue Chabot, Villeray", "le logement et le quartier"],
               ["2e ét., 2 ch. fermées", "l'étage et les chambres"],
               ["ch. et écl., non meublé", "ce qui est compris"],
               ["libre 1er juill., 1 150 $", "la date et le prix"]],
              cle=0,
              note="Quatre lignes, quatre renseignements. Rien d'autre ne compte.",
              notes="Diapositive à photographier. C'est l'annonce que le module suit d'un "
                    "bout à l'autre : elle revient au jeu de rôle de la séance E1. La "
                    "faire recopier.")

    d.piege('Lecture',
            "lire « écl. » comme « ensoleillé »",
            "lire « écl. » comme « éclairé »",
            "« Éclairé » ne parle pas de la lumière du soleil : il dit que le "
            "compte d'électricité est compris dans le loyer. Pour la lumière "
            "naturelle, une annonce écrirait « ensoleillé ».",
            notes="C'est le contresens le plus fréquent, et il coûte de l'argent : un "
                  "élève qui croit avoir choisi un logement lumineux découvre en janvier "
                  "qu'il paie l'électricité.")

    d.piege('Lecture',
            "compter le demi comme une pièce de plus",
            "compter le demi comme la salle de bain",
            "Le chiffre compte toutes les pièces et le demi est toujours la "
            "salle de bain. Un quatre et demie a donc deux chambres, un salon "
            "et une cuisine.",
            notes="Rappel de la séance A1. Le refaire au tableau si le groupe hésite : "
                  "c'est l'erreur qui fait perdre le plus de temps dans une recherche.")

    d.pratique('Lecture', "Que veut dire cette abréviation ?",
               "Lisez chaque abréviation en phrase complète.", [
        ("4 ½", "un quatre et demie : deux chambres fermées"),
        ("2e ét.", "deuxième étage"),
        ("ch. et écl.", "chauffé et éclairé"),
        ("s.-sol", "sous-sol"),
        ("stat.", "stationnement"),
        ("libre 1er juill.", "libre le premier juillet"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 2 du Défi 1, où les six abréviations se glissent sur leur "
             "définition. Faire l'exercice à l'oral d'abord, puis ouvrir l'activité.")

    d.pratique('Lecture', "Trouvez le renseignement",
               "Dans l'annonce du quatre et demie.", [
        ("À quel étage ?", "au deuxième"),
        ("Combien de chambres fermées ?", "deux"),
        ("Qu'est-ce qui est compris ?", "le chauffage et l'électricité"),
        ("Est-ce qu'il y a des meubles ?", "non, le logement est non meublé"),
        ("À quelle date est-il libre ?", "le premier juillet"),
        ("Combien coûte-t-il ?", "1 150 $ par mois"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice 3 du Défi 1. Les six questions sont celles qu'on se pose "
             "vraiment devant une annonce : les faire recopier comme une grille de "
             "lecture réutilisable.")

    d.billet(
        "Écrivez une annonce en abrégé pour votre logement actuel.",
        exemples=[
            "___ ½, ___ ét., ___ .",
            "Libre le ___ . ___ $ par mois.",
        ],
        notes="Devoir court. Écrire une annonce oblige à comprendre les abréviations "
              "mieux que les lire. Les annonces produites servent d'exercice de lecture "
              "en début de séance B3.")

    return d.save(dossier)
