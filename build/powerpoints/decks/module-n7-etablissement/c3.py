# -*- coding: utf-8 -*-
"""C3 · Mettre en avant ce qui compte
Bloc C « Défi 2 · L'entrevue de sélection » · couleur ambre · 75 min.
Source : exercice `t2emph` et sa mini-leçon (phrases emphatiques).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Mettre en avant ce qui compte',
        chapeau="À l'écrit on souligne ; à l'oral on encadre. Sans mise en "
                "relief, une réponse de vingt mots arrive plate, et c'est le "
                "dernier mot qui reste.",
        duree='75 minutes')

    d.titre(notes="Séance très orale. Chaque phrase se dit deux fois : une fois plate, "
                  "une fois encadrée. La différence s'entend, elle ne s'explique pas.")

    d.objectifs([
        "encadrer le sujet avec « c'est… qui » ;",
        "encadrer le reste avec « c'est… que » ;",
        "annoncer sa réponse avec « ce que… c'est » ;",
        "accorder le verbe après « qui » à la bonne personne.",
    ], notes="Le quatrième objectif est le seul point d'accord de la séance, et c'est "
             "la faute la plus audible : « c'est moi qui est ».")

    d.declencheur(
        'Écoute', "Laquelle des deux entend-on ?",
        pistes=[
            "« J'ai appris à observer en travaillant de nuit. »",
            "« C'est en travaillant de nuit que j'ai appris à observer. »",
            "Quel mot reste dans la tête, dans chaque cas ?",
            "Laquelle diriez-vous à un comité ?",
        ],
        notes="Faire dire les deux par le même élève, à la suite. Le groupe entend "
              "immédiatement laquelle porte, et personne n'a eu besoin de grammaire.")

    d.tableau('Analyse', "Trois façons de souligner à l'oral",
              ['La forme', 'Ce qu\'elle encadre'],
              [["c'est… qui", "le sujet : c'est mon horaire qui a décidé"],
               ["c'est… que", "le reste : c'est à l'unité prothétique que je travaille"],
               ["ce que… c'est", "la réponse : ce que je veux, c'est finir"],
               ["ce qui… c'est", "le sujet annoncé : ce qui me manque, c'est un préalable"]],
              cle=0,
              note="Deux emplois par entrevue portent ; dix deviennent un tic de "
                   "langage.",
              notes="Diapositive à photographier. La note compte autant que le "
                    "tableau : ces formes s'usent très vite.")

    d.regle("Après « qui », le verbe prend la personne encadrée",
            "C'est moi qui suis allée la voir. C'est vous qui avez mon dossier.",
            precision="« Qui » reprend ce qu'on encadre, et le verbe s'accorde avec "
                      "lui. « C'est moi qui est » est la faute la plus audible du "
                      "niveau, et la première personne est celle qu'on rate le plus.",
            notes="Diapositive à photographier. Faire conjuguer à voix haute : c'est "
                  "moi qui suis, c'est toi qui es, c'est nous qui sommes.")

    d.pratique('Grammaire', "Complétez la mise en relief",
               "Un seul mot ou groupe de mots par trou.", [
        ("Mon horaire a décidé de tout. On encadre : C'est mon horaire ___ a décidé de tout.", "qui"),
        ("C'est moi qui (être) ___ allée voir ma coordonnatrice la première.", "suis"),
        ("C'est en travaillant de nuit ___ j'ai appris à observer.", "que"),
        ("___ je veux, c'est être celle qu'on va chercher.", "Ce que"),
        ("___ me manque, c'est un préalable de mathématiques.", "Ce qui"),
        ("C'est vous ___ avez mon dossier devant vous, pas moi.", "qui"),
    ], corrige=True,
       notes="Faire lire chaque phrase corrigée à voix haute, avec l'insistance sur "
             "l'élément encadré. Sans l'intonation, l'exercice ne sert à rien.")

    d.cartes('Emploi', "Quatre phrases prêtes pour l'entrevue", [
        ("Dire ce qu'on veut",
         "Ce que je veux, c'est être celle qu'on va chercher plutôt que celle qui va "
         "chercher."),
        ("Dire ce qui manque",
         "Ce qui me manque, c'est un préalable de mathématiques, et je suis déjà "
         "inscrite."),
        ("Dire d'où vient une compétence",
         "C'est en travaillant de nuit que j'ai appris à observer."),
        ("Dire qui a fait le geste",
         "C'est moi qui suis allée voir ma coordonnatrice, avant de déposer."),
    ], notes="Faire adapter les quatre à leur propre parcours, à l'écrit, en dix "
             "minutes. C'est la préparation directe de la production orale du bloc E.")

    d.piege('Piège', "C'est moi qui est allée la voir.",
            "C'est moi qui suis allée la voir.",
            "Le pronom « qui » prend la personne de ce qu'il reprend. À la première "
            "personne, le verbe est « suis » — et l'erreur s'entend à trois mètres.",
            notes="Faute quasi universelle, y compris chez des locuteurs de longue "
                  "date. La reprendre sans dramatiser, mais la reprendre.")

    d.billet("Écris deux phrases sur toi, l'une avec « c'est… que », l'autre avec "
             "« ce que… c'est ».",
             exemples=["C'est en gardant mes trois enfants que j'ai appris à m'organiser.",
                       "Ce que je veux, c'est travailler dans mon domaine ici."],
             notes="Ramasser les billets et corriger uniquement l'accord et le choix "
                   "« ce que / ce qui ». Le contenu appartient à l'élève.")

    return d.save(dossier)
