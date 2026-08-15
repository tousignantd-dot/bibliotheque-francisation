# -*- coding: utf-8 -*-
"""C1 · Un concours haut en couleur.
Bloc C · couleur acier (compréhension écrite) · 75 min.
Source : exercice `t2lecture` — le concours de sculptures sur neige.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Un concours haut en couleur',
        chapeau="Un fait divers écrit, plus long que ceux de la radio. Neuf questions, "
                "et la moitié porte sur des mots qu'on doit deviner par le contexte.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Prévenir : ici, on lit. On peut relire, revenir "
                  "en arrière, souligner. Ce sont des avantages qu'on n'a pas à l'oral.")

    d.objectifs([
        "lire un fait divers de dix lignes et en tirer l'essentiel ;",
        "deviner le sens d'un mot par le contexte ;",
        "trouver un synonyme dans le texte ;",
        "comprendre une expression figée.",
    ])

    d.cartes('Le texte', "Le concours de Rivière-Claire", [
        ("Ce qui s'est passé",
         "Le concours de sculptures sur neige de Rivière-Claire connaît un franc succès "
         "depuis cinq ans. La fin de semaine dernière, une trentaine d'équipes ont "
         "participé, sur la place du village."),
        ("Les œuvres",
         "Les visiteurs ont pu admirer des œuvres impressionnantes, façonnées à la "
         "tronçonneuse et à la pelle."),
        ("Les gagnants",
         "L'équipe Les Frimousses givrées a remporté le premier prix avec Le Renard "
         "argenté, une sculpture de près de trois mètres de haut. Le jury a apprécié la "
         "précision des détails du pelage."),
        ("Autour du concours",
         "Des artisans locaux ont vendu leurs créations aux festivaliers venus nombreux "
         "malgré le froid. Les organisateurs prévoient une édition plus grande l'an "
         "prochain."),
    ], notes="Faire lire le texte en silence cinq minutes avant d'afficher cette diapo. "
             "Elle sert de support à la correction, pas de première lecture.")

    d.regle('La règle de lecture',
            "Un mot inconnu se devine par ce qui l'entoure.",
            precision="« Façonnées à la tronçonneuse et à la pelle » : même sans "
                      "connaître « façonner », les outils disent qu'il s'agit de "
                      "fabriquer. Lisez la phrase entière avant de chercher le mot dans "
                      "un dictionnaire.",
            notes="Diapo centrale de la séance. Faire l'expérience sur trois mots du "
                  "texte avant de passer aux exercices.")

    d.tableau('Analyse', "Quatre mots à deviner par le contexte",
              ['Le mot', "L'indice dans le texte", 'Le sens'],
              [["façonnées", "à la tronçonneuse et à la pelle", "fabriquées"],
               ["festivaliers", "venus nombreux au concours", "ceux qui vont au festival"],
               ["locaux", "des artisans qui vendent sur place", "de la région"],
               ["pelage", "les détails, sur un renard", "les poils de l'animal"]],
              cle=0, props=[0.22, 0.5, 0.28],
              notes="Faire chercher l'indice avant de donner le sens. C'est l'indice qui "
                    "s'apprend, pas le mot.")

    d.pratique('Pratique · 1 de 4', "Les faits du texte",
               "Répondez d'après le fait divers.", [
        ("Où se déroule le concours ?", "à Rivière-Claire, sur la place du village"),
        ("Depuis combien d'années a-t-il lieu ?", "depuis cinq ans"),
        ("Avec quels outils les sculptures sont-elles façonnées ?",
         "à la tronçonneuse et à la pelle"),
        ("Quelle équipe a remporté le premier prix ?", "Les Frimousses givrées"),
        ("Comment s'appelle la sculpture gagnante ?", "Le Renard argenté"),
        ("Quelle est sa hauteur ?", "près de trois mètres"),
    ], corrige=True,
       notes="Faire pointer la phrase exacte pour chaque réponse. C'est la méthode de "
             "lecture qu'on installe.")

    d.pratique('Pratique · 2 de 4', "Devinez le sens",
               "Servez-vous du contexte, pas du dictionnaire.", [
        ("Trouvez un synonyme de « fabriquées » dans le texte.", "façonnées"),
        ("Que veut dire « un franc succès » ?", "une vraie réussite, un grand succès"),
        ("Comment appelle-t-on les personnes qui participent à un festival ?",
         "des festivaliers"),
        ("Dans « artisans locaux », que veut dire « locaux » ?", "de la région, du coin"),
        ("Que veut dire « le pelage » d'un renard ?", "ses poils"),
    ], corrige=True,
       notes="Faire nommer l'indice pour chacun. Un élève qui trouve le sens sans "
             "pouvoir dire pourquoi n'a pas encore la méthode.")

    d.piege("Le piège du dictionnaire ouvert trop tôt",
            "Je cherche chaque mot inconnu avant de finir la phrase.",
            "Je finis la phrase, puis je décide si le mot est nécessaire.",
            "La plupart des mots inconnus d'un fait divers ne sont pas nécessaires à la "
            "compréhension. Chercher chacun d'eux coupe la lecture et fait perdre le "
            "fil. Finissez la phrase, puis le paragraphe, et voyez ce qui manque "
            "vraiment.",
            notes="Faire compter les mots inconnus du texte, puis ceux qui empêchent "
                  "vraiment de répondre aux questions. L'écart est frappant.")

    d.piege("Le piège de l'expression figée",
            "« Un franc succès » veut dire un succès honnête.",
            "« Franc » veut dire ici complet, entier.",
            "Dans une expression figée, les mots ne gardent pas leur sens habituel. "
            "« Franc succès », « haut en couleur », « venus nombreux » : ce sont des "
            "blocs qu'on apprend entiers. Les décomposer mène à un contresens.",
            notes="Faire relever trois expressions figées du texte. Les faire noter comme "
                  "des blocs, pas comme des mots séparés.")

    d.pratique('Pratique · 3 de 4', "Les cinq questions",
               "Appliquez la grille de A4 au fait divers.", [
        ("Qui ?", "une trentaine d'équipes, les Frimousses givrées, le jury, des artisans"),
        ("Quoi ?", "un concours de sculptures sur neige, remporté par une équipe"),
        ("Où ?", "à Rivière-Claire, sur la place du village"),
        ("Quand ?", "la fin de semaine dernière"),
        ("Pourquoi ?", "un concours annuel, qui existe depuis cinq ans"),
    ], corrige=True,
       notes="Faire remarquer que la réponse à « qui » est longue : un fait divers écrit "
             "nomme plus de personnes qu'un reportage radio.")

    d.pratique('Pratique · 4 de 4', "Résumez en trois phrases",
               "L'essentiel, le gagnant, la suite.", [
        ("L'essentiel",
         "Le concours de sculptures sur neige de Rivière-Claire a eu lieu la fin de "
         "semaine dernière."),
        ("Le gagnant",
         "L'équipe Les Frimousses givrées a remporté le premier prix avec Le Renard "
         "argenté."),
        ("La suite",
         "Les organisateurs prévoient une édition plus grande l'an prochain."),
    ], corrige=True,
       notes="Trois phrases pour dix lignes : c'est le rapport habituel d'un bon résumé. "
             "Le dire au groupe.")

    d.billet(
        "Relevez trois mots que vous avez devinés par le contexte.",
        exemples=[
            "Le mot, puis l'indice qui vous a aidé.",
            "Exemple : « façonnées » — les outils nommés juste après.",
        ],
        notes="Ce billet évalue la méthode, pas le vocabulaire. Un élève qui nomme "
              "l'indice a compris, même s'il s'est trompé de sens.")

    return d.save(dossier)
