# -*- coding: utf-8 -*-
"""C2 · Il y a, contient, c'est, ce sont, rien de.
Bloc C « Défi 2 · Dire ce qu'il y a dedans, et payer » · couleur ambre · 75 min.
Source : mini-leçon `t2contenu`, exercice `t2contenu`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Il y a, contient, c'est, ce sont",
        chapeau="Cinq façons de nommer ce qu'il y a dans une boîte. La plus "
                "simple marche pour une chose comme pour dix, et c'est celle "
                "qu'on emploie neuf fois sur dix.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire et d'écriture. Elle donne les mots que la séance "
                  "C1 a fait entendre. Écrire les cinq tournures au tableau et les y "
                  "laisser toute la séance.")

    d.objectifs([
        "employer « il y a » pour nommer un contenu ;",
        "distinguer « c'est » et « ce sont » ;",
        "employer « rien de » pour rassurer ;",
        "écrire trois phrases qui décrivent un colis.",
    ])

    d.regle("La phrase qui marche toujours",
            "Il y a des vêtements et un livre.",
            precision="« Il y a » ne change jamais : ni au singulier, ni au "
                      "pluriel, ni au féminin. Une chose, dix choses, c'est la "
                      "même forme. C'est la tournure la plus sûre du français "
                      "pour dire ce qui se trouve quelque part.",
            notes="Diapo à photographier. Faire produire cinq phrases d'affilée avec "
                  "« il y a » et des objets de la classe : la forme ne bouge pas, et "
                  "c'est rassurant à ce stade.")

    d.tableau('Analyse', "Cinq façons de dire le contenu",
              ['La tournure', 'Quand', 'Exemple'],
              [["Il y a", "toujours, le plus simple", "Il y a des vêtements et un livre."],
               ["contient", "le mot de la préposée", "La boîte contient des vêtements."],
               ["C'est", "une seule chose derrière", "C'est un cadeau pour mon frère."],
               ["Ce sont", "plusieurs choses derrière", "Ce sont des vêtements d'hiver."],
               ["Rien de", "pour rassurer", "Rien de fragile, rien de liquide."]],
              cle=0,
              note="« Contenir » s'entend au comptoir, mais on n'a jamais besoin de le dire soi-même.",
              notes="Diapo à photographier. Insister sur la dernière colonne du haut : "
                    "les élèves doivent comprendre « contient », pas le produire.")

    d.regle("Le seul choix qui demande de réfléchir",
            "C'est un cadeau.  ·  Ce sont des vêtements.",
            precision="« C'est » devant une seule chose. « Ce sont » devant "
                      "plusieurs. On regarde ce qui vient APRÈS, pas ce qui vient "
                      "avant : la boîte reste une, mais son contenu peut être "
                      "pluriel.",
            notes="Diapo à photographier. C'est le point difficile de la séance. Faire "
                  "l'exercice au tableau avec dix exemples avant de passer à l'écrit.")

    d.cartes("Rien de : trois emplois", "La formule qui rassure", [
        ("Rien de fragile",
         "Aucun objet qui casse : pas de verre, pas d'assiette, pas de cadre. "
         "C'est la première des trois questions de sécurité."),
        ("Rien de liquide",
         "Pas de bouteille, pas de parfum, pas de crème. Les liquides voyagent mal "
         "et certains sont refusés dans l'avion."),
        ("Rien de dangereux",
         "Pas de produit qui brûle, pas d'aérosol, pas de pile toute seule. La "
         "question paraît étrange : elle est posée à tout le monde."),
        ("Attention au « de »",
         "On dit « rien DE fragile », jamais « rien fragile ». Le petit mot « de » "
         "est obligatoire, et il ne s'accorde pas."),
    ], notes="Faire répéter les trois formules à la suite, dans l'ordre : c'est ainsi "
             "qu'elles sortent au comptoir, comme une seule réponse.")

    d.pratique('Écriture', "Complétez la phrase",
               "Écrivez « il y a », « contient », « c'est », « ce sont » ou « rien ».", [
        ("___ des vêtements et un livre dans la boîte.", "Il y a"),
        ("La boîte ___ deux chandails et un cadre.", "contient"),
        ("___ un cadeau d'anniversaire pour mon frère.", "C'est"),
        ("___ des livres d'école, rien d'autre.", "Ce sont"),
        ("Il n'y a ___ de fragile là-dedans.", "rien"),
        ("Attention : ___ de la vaisselle, c'est fragile.", "c'est"),
    ], corrige=True,
       notes="C'est l'exercice `t2contenu` du module interactif. La dernière ligne est "
             "un piège volontaire : « de la vaisselle » est un singulier collectif, donc "
             "« c'est ». L'expliquer seulement si un élève le demande.")

    d.piege(
        "Le contenu",
        "Ce sont un cadeau.",
        "C'est un cadeau.",
        "Un seul objet derrière, donc « c'est ». L'erreur vient du fait que la boîte "
        "contient plusieurs choses d'habitude : on regarde le mot qui suit "
        "immédiatement, jamais la boîte elle-même.",
        notes="Faire chercher au groupe trois phrases avec « c'est » et trois avec "
              "« ce sont », à partir de leur propre billet de sortie de C1.")

    d.pratique('À l\'oral', "Répondez à la préposée",
               "Deux par deux : l'un pose les trois questions, l'autre répond.", [
        ("Qu'est-ce qu'il y a dans la boîte ?", "Il y a des vêtements et un livre."),
        ("Rien de fragile ?", "Non, rien de fragile."),
        ("Rien de liquide, rien de dangereux ?", "Non, rien."),
        ("C'est pour qui ?", "C'est un cadeau pour mon frère."),
    ], corrige=True,
       notes="Cinq minutes par rôle. C'est le passage obligé du jeu de rôle de la "
             "séance E1 : chaque élève doit l'avoir dit à voix haute au moins deux fois "
             "avant de sortir.")

    d.billet(
        "Décrivez le contenu d'une boîte en trois phrases.",
        exemples=[
            "Une phrase avec « il y a », une avec « c'est » ou « ce sont ».",
            "Une phrase avec « rien de ».",
        ],
        notes="Ramasser et corriger. C'est la trace écrite qui sert de brouillon à la "
              "production écrite de la séance E1.")

    return d.save(dossier)
