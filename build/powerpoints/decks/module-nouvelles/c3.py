# -*- coding: utf-8 -*-
"""C3 · L'accord du participe passé avec être.
Bloc C · couleur ambre (écriture) · 75 min.
Source : exercice `t2accord` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="L'accord avec être",
        chapeau="« La fillette est sortie. » « Les élèves sont arrivés. » Un e, un s — "
                "deux lettres qu'on n'entend pas et qui sautent aux yeux dans un texte "
                "écrit.",
        duree='75 minutes')

    d.titre(notes="Écrire « elle est sorti » et « elle est sortie » au tableau. Demander "
                  "laquelle est correcte. Beaucoup hésiteront, parce que les deux se "
                  "disent pareil.")

    d.objectifs([
        "accorder le participe passé avec le sujet quand l'auxiliaire est être ;",
        "reconnaître les verbes qui prennent être ;",
        "écrire les quatre formes : masculin, féminin, singulier, pluriel ;",
        "relire un texte en vérifiant ces accords.",
    ])

    d.regle('La règle',
            "Avec être, le participe passé s'accorde en genre et en nombre avec le sujet.",
            precision="Il est arrivé. Elle est arrivée. Ils sont arrivés. Elles sont "
                      "arrivées. Le participe se comporte comme un adjectif : il prend "
                      "les marques du sujet.",
            notes="Écrire les quatre formes au tableau, en carré. C'est la même logique "
                  "que l'accord de l'adjectif, vue au module 2.")

    d.tableau('Analyse', "Les quatre formes",
              ['Le sujet', 'La forme', 'La marque'],
              [["il", "il est arrivé", "rien"],
               ["elle", "elle est arrivée", "un e"],
               ["ils", "ils sont arrivés", "un s"],
               ["elles", "elles sont arrivées", "un e et un s"]],
              cle=2,
              note="Aucune des quatre ne s'entend. C'est un accord purement écrit.",
              notes="Faire lire les quatre à voix haute : elles sont identiques. C'est ce "
                    "qui rend l'erreur invisible à l'oral et très visible à l'écrit.")

    d.regle('Quels verbes prennent être',
            "Arriver, partir, sortir, venir, devenir, tomber, rester, monter, descendre, naître, mourir.",
            precision="Ce sont presque tous des verbes de mouvement ou de changement "
                      "d'état. Ils sont peu nombreux et ils reviennent constamment dans "
                      "les faits divers : à connaître par cœur.",
            notes="Écrire la liste au tableau et l'y laisser toute la séance. Ajouter les "
                  "verbes pronominaux, qui prennent tous être.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses à savoir en plus", [
        ("Avec avoir, aucun accord avec le sujet",
         "« Elle a organisé la collecte » — pas de e. L'accord ne se fait qu'avec "
         "l'auxiliaire être."),
        ("Un groupe collectif reste singulier",
         "« Toute la classe est partie » — un e, pas de s. « La classe » est un seul "
         "sujet, même s'il désigne plusieurs personnes."),
        ("« Vous » peut être singulier",
         "« Vous êtes venu » pour une personne, « vous êtes venus » pour plusieurs. "
         "C'est le sens qui décide, pas le mot."),
        ("Le passif emploie la même règle",
         "« La collecte a été organisée » — accord avec « la collecte ». C'est le même "
         "mécanisme qu'en B4."),
    ], notes="La quatrième carte relie les deux séances. Le faire remarquer : ce n'est "
             "pas une règle de plus, c'est la même.")

    d.pratique('Pratique · 1 de 4', "Accordez le participe",
               "Regardez le sujet : genre et nombre.", [
        ("Les élèves (arriver) ___ à l'école tôt ce matin-là.", "sont arrivés"),
        ("La fillette (sortir) ___ pour distribuer ses affiches.", "est sortie"),
        ("Le journaliste (arriver) ___ dix minutes plus tard.", "est arrivé"),
        ("Nous (monter) ___ sur la scène pour recevoir le prix.", "sommes montés"),
        ("Cette collecte (devenir) ___ une tradition dans l'école.", "est devenue"),
        ("Le chat (tomber) ___ dans la cour de la voisine.", "est tombé"),
    ], corrige=True,
       notes="Faire souligner le sujet avant d'accorder. C'est l'étape que les élèves "
             "sautent, et c'est celle qui fait tout le travail.")

    d.pratique('Pratique · 2 de 4', "Quatre plus difficiles",
               "Attention au genre et au nombre du sujet.", [
        ("Vous (venir) ___ voir les sculptures ?", "êtes venu ou êtes venus"),
        ("Toute la classe (partir) ___ tôt vendredi matin.", "est partie — un seul sujet"),
        ("L'équipe gagnante (revenir) ___ chercher son trophée.", "est revenue"),
        ("Les visiteurs (rester) ___ jusqu'au soir.", "sont restés"),
    ], corrige=True,
       notes="Les deux premiers items sont les pièges : « vous » ambigu, et « la classe » "
             "collective. Les corriger lentement.")

    d.piege("Le piège du groupe collectif",
            "Toute la classe sont parties tôt.",
            "Toute la classe est partie tôt.",
            "« La classe » désigne plusieurs personnes, mais c'est un seul mot, féminin "
            "singulier. Le verbe et le participe s'accordent avec le mot, pas avec le "
            "nombre de personnes. Même chose pour « l'équipe », « le groupe », « le "
            "jury ».",
            notes="Faire chercher trois autres noms collectifs. C'est une erreur logique "
                  "avant d'être grammaticale.")

    d.piege("Le piège de l'auxiliaire avoir",
            "Elle a arrivée en retard.",
            "Elle est arrivée en retard.",
            "« Arriver » prend toujours l'auxiliaire être, jamais avoir. L'erreur double "
            "ici : le mauvais auxiliaire, et un accord fait quand même. Vérifiez d'abord "
            "l'auxiliaire, puis l'accord.",
            notes="Lier au module 2, séance B2. Ceux qui l'ont fait retrouveront la liste "
                  "des verbes de mouvement.")

    d.pratique('Pratique · 3 de 4', "Avoir ou être ?",
               "Choisissez l'auxiliaire, puis accordez s'il y a lieu.", [
        ("Les élèves ___ décidé d'organiser une collecte.", "ont décidé — avoir"),
        ("Elle ___ arrivée en retard au concours.", "est arrivée — être"),
        ("Mes voisins ___ déménagé le mois dernier.", "ont déménagé — avoir"),
        ("Une journaliste ___ venue filmer l'événement.", "est venue — être"),
        ("La tempête ___ retardé le concours d'une heure.", "a retardé — avoir"),
        ("Les organisateurs ___ restés jusqu'à la fin.", "sont restés — être"),
    ], corrige=True,
       notes="Faire nommer l'auxiliaire à voix haute avant d'écrire. Le choix de "
             "l'auxiliaire décide de l'accord, jamais l'inverse.")

    d.pratique('Pratique · 4 de 4', "Relisez et corrigez",
               "Chaque phrase contient une erreur d'accord.", [
        ("La fillette est sorti chercher son chat.", "sortie — sujet féminin"),
        ("Les élèves sont arrivé tôt.", "arrivés — sujet pluriel"),
        ("Toute la classe sont parties.", "est partie — sujet singulier"),
        ("Elle a arrivée en retard.", "est arrivée — auxiliaire être"),
    ], corrige=True,
       notes="Exercice de relecture, la compétence qui sert vraiment. Faire chercher "
             "d'abord le sujet de chaque phrase.")

    d.billet(
        "Écrivez quatre phrases au passé composé avec l'auxiliaire être.",
        exemples=[
            "Une avec un sujet masculin, une féminin, une pluriel masculin, une pluriel "
            "féminin.",
            "Soulignez le sujet et la marque d'accord.",
        ],
        notes="Corriger les billets en dehors du cours. Cet accord demande une "
              "rétroaction individuelle et il revient dans tout le programme.")

    return d.save(dossier)
