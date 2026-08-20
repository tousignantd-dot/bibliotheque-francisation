# -*- coding: utf-8 -*-
"""D1 · Le dépliant de la ville.
Bloc D « Défi 3 · Le dépliant et l'inscription » · couleur acier · 75 min.
Source : mini-leçon `t3depliant`, dialogue `t3`, exercices `t3vf`, `t3depliant`
et `t3lire`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Le dépliant de la ville',
        chapeau="Une trentaine d'activités sur quatre pages, trois colonnes de "
                "chiffres et des petites étoiles. Un dépliant n'est pas fait "
                "pour être lu : il est fait pour qu'on y trouve quelque chose.",
        duree='75 minutes')

    d.titre(notes="Apporter de vrais dépliants municipaux, un par deux élèves si possible. "
                  "La séance ne vaut la peine que sur un document réel.")

    d.objectifs([
        "trouver une activité dans un dépliant en moins de deux minutes ;",
        "lire les trois chiffres dans le bon ordre ;",
        "chercher la légende avant de s'inquiéter d'un symbole ;",
        "savoir ce qu'un dépliant ne dit jamais.",
    ])

    d.dialogue('Dialogue · 1 de 2', "Par où commencer", [
        ("ROSA", "J'ai reçu le dépliant de la ville. Il y a une trentaine d'activités là-dedans.", False),
        ("DENIS", "Regarde d'abord la colonne de gauche : c'est le nom de l'activité et l'âge.", True),
        ("ROSA", "Et les chiffres à droite ?", False),
        ("DENIS", "Le premier, c'est le prix pour les résidents. Le deuxième, pour les autres. Le troisième, c'est le nombre de semaines.", True),
    ], consigne="Écoutez, puis repérez les deux conventions expliquées.",
       notes="Faire ouvrir un vrai dépliant en même temps. Les élèves vérifient que les "
             "trois chiffres y sont bien dans cet ordre — c'est presque toujours le cas.")

    d.dialogue('Dialogue · 2 de 2', "Les symboles", [
        ("ROSA", "Il y a des petites étoiles à côté de certaines activités.", False),
        ("DENIS", "Ça veut dire qu'il reste peu de places. En bas de la page, la légende l'explique.", True),
        ("ROSA", "La chorale du jeudi soir a une étoile. C'est celle qui m'intéresse le plus.", True),
        ("DENIS", "Alors inscris-toi cette semaine. Les places partent vite quand il y a une étoile.", True),
    ], notes="« C'est celle qui m'intéresse le plus » réunit le pronom démonstratif et le "
             "superlatif du bloc B. Le faire remarquer.")

    d.tableau('Analyse', "Les quatre conventions",
              ['Ce qu\'on voit', 'Ce que ça veut dire'],
              [["La colonne de gauche", "le nom et l'âge — c'est le tri"],
               ["Le premier chiffre", "le tarif résident"],
               ["Le deuxième chiffre", "le tarif non-résident"],
               ["Le troisième chiffre", "le nombre de semaines"]],
              cle=0,
              note="Toujours le même ordre, d'une ville à l'autre.",
              notes="Diapo centrale. Faire vérifier sur le dépliant réel : la constance "
                    "entre les villes surprend et rassure.")

    d.regle('Commencer par ce qui élimine',
            "L'âge, le jour, le tarif. Dans cet ordre.",
            precision="Lire quatre pages en entier prend vingt minutes. Trier d'abord par "
                      "âge, puis par jour disponible, puis par tarif, en prend deux — et "
                      "il ne reste souvent que trois ou quatre activités à comparer.",
            notes="Faire l'exercice en direct sur le dépliant réel, chronomètre en main. "
                  "L'effet est spectaculaire.")

    d.regle('La légende est en bas',
            "Un symbole ne veut rien dire tout seul.",
            precision="Étoile, astérisque, couleur : chacun renvoie à la légende, toujours "
                      "en bas de page, en petits caractères. C'est justement là que se "
                      "trouve l'information qui change une décision — comme « il reste peu "
                      "de places ».",
            notes="Faire chercher la légende sur le dépliant réel. Beaucoup d'élèves ne "
                  "l'avaient jamais remarquée.")

    d.piege("Croire le dépliant sur les places",
            "L'étoile dit qu'il reste des places, alors j'irai le mois prochain.",
            "L'étoile dit qu'il en restait peu à l'impression. Je téléphone.",
            "Un dépliant est imprimé des semaines avant la session. Il ne sait rien de ce "
            "qui reste aujourd'hui. Pour l'état réel des places, il n'y a qu'un moyen : "
            "téléphoner ou regarder en ligne.",
            notes="Savoir ce qu'un document ne dit pas est une compétence de lecture à part "
                  "entière. Le nommer comme telle.")

    d.pratique('Pratique · 1 de 2', "Où chercher ?",
               "Dites où se trouve la réponse dans le dépliant.", [
        ("« Mon garçon a-t-il le bon âge ? »", "la colonne de gauche"),
        ("« Combien je vais payer ? »", "le premier chiffre, si j'habite la ville"),
        ("« Combien de temps ça dure ? »", "le troisième chiffre"),
        ("« Que veut dire cette étoile ? »", "la légende, en bas de la page"),
        ("« Reste-t-il des places aujourd'hui ? »", "nulle part — il faut téléphoner"),
    ], corrige=True, cols=1,
       notes="Faire chercher pour de vrai dans le dépliant distribué, avant de corriger.")

    d.pratique('Pratique · 2 de 2', "Lisez la ligne",
               "Voici une ligne de dépliant. Que dit-elle ?", [
        ("Natation débutant · 8-10 ans · 85 · 110 · 12", "85 $ résident, 110 $ non-résident, 12 semaines"),
        ("Chorale adultes · 16 ans et + · 30 · 45 · 10 (étoile)", "30 $ résident, 10 semaines, peu de places"),
        ("Soccer · 10-12 ans · 120 · 160 · 16", "120 $ résident, 16 semaines"),
    ], corrige=True, cols=1,
       notes="Faire lire à voix haute chaque ligne, comme on lirait une phrase. Le tableau "
             "devient parlant.")

    d.billet(
        "Choisissez une activité dans un vrai dépliant et notez tout ce que la ligne vous apprend.",
        exemples=[
            "L'âge, les deux tarifs, la durée, les symboles.",
            "Notez aussi ce que la ligne ne vous dit pas.",
        ],
        notes="Devoir concret, à faire sur le dépliant distribué ou sur le site de la "
              "ville. Le plus utile du bloc D.")

    return d.save(dossier)
