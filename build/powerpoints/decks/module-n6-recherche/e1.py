# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : les trois productions du module, jeu de rôle `entrevue`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout ce qui a été appris se rassemble : lire l'offre, "
                "décrire ses tâches, développer une réponse. Une entrevue "
                "avec l'assistant, une production orale, une production écrite.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Prévoir des écouteurs : l'entrevue et la "
                  "production orale se font à l'ordinateur, chacun de son côté.")

    d.objectifs([
        "tenir une courte entrevue du début à la fin ;",
        "offrir ses services en quatre-vingt-dix secondes ;",
        "décrire par écrit ses fonctions et son expérience ;",
        "recevoir une correction et la relire.",
    ])

    d.cartes('Les trois défis, réunis', "Ce qui doit apparaître", [
        ("Défi 1 · l'offre",
         "Montrer qu'on a lu l'offre : reprendre le titre exact du poste et une "
         "expression de la liste des tâches."),
        ("Défi 2 · la demande",
         "Décrire ses fonctions avec des verbes d'action, un chiffre, et une phrase "
         "en « après avoir »."),
        ("Défi 3 · l'entrevue",
         "Développer avec un connecteur d'exemple, placer une information avec "
         "« j'aimerais que vous sachiez », poser une question."),
    ], notes="Diapositive à photographier. C'est la grille des deux productions.")

    d.regle("Le jeu de rôle",
            "Trois postes, deux rôles.",
            precision="Dans l'activité interactive : <b>commis à l'inventaire</b> chez "
                      "Boisverte, <b>aide-cuisinier</b> dans un restaurant de quartier, "
                      "<b>préposé à l'entretien</b> dans un immeuble de bureaux. Vous "
                      "choisissez d'être le <b>candidat</b> ou l'<b>employeur</b> — "
                      "faites les deux : on comprend mieux les questions quand on a eu "
                      "à les poser.",
            notes="Six combinaisons. Demander au moins deux tours, dont un dans chaque "
                  "rôle. L'assistant relance quand la réponse tient en une phrase : c'est "
                  "voulu.")

    d.pratique('Production orale', "Offrez vos services",
               "Quatre-vingt-dix secondes, à l'ordinateur.", [
        ("Temps 1", "qui vous êtes et ce que vous avez fait, avec une durée"),
        ("Temps 2", "un exemple précis, avec un chiffre"),
        ("Temps 3", "ce que vous cherchez et quand vous êtes disponible"),
    ], cols=1,
       notes="La correction par l'IA arrive tout de suite. Elle n'est pas conservée : "
             "l'élève la lit, la note, et recommence s'il le veut.")

    d.pratique('Production écrite', "Remplissez la page trois",
               "De six à dix phrases, en deux courts paragraphes.", [
        ("Le titre exact", "de votre dernier poste"),
        ("Quatre verbes d'action", "à l'imparfait : je recevais, je vérifiais, je préparais…"),
        ("Un chiffre", "durée, quantité, ou nombre de personnes"),
        ("Une phrase en « après avoir »", "ou « après être », avec l'accord"),
        ("Un connecteur d'exemple", "par exemple, notamment, entre autres"),
        ("Une phrase avec « où »", "l'entreprise où…, l'année où…"),
    ], cols=2,
       notes="Six exigences, c'est beaucoup. Les projeter pendant l'écriture et laisser "
             "la diapositive affichée : la liste est une aide, pas un examen.")

    d.piege("Réciter au lieu de parler",
            "Un texte appris par cœur, débité sans pause.",
            "Un plan en trois temps, et des phrases dites.",
            "Une réponse récitée s'entend, et elle s'effondre à la première question "
            "imprévue. Le plan en trois temps tient debout même quand la question change, "
            "parce qu'il porte sur ce qu'on a vraiment fait.",
            notes="Rappeler la séance D2 : la situation, ce qu'on faisait, le résultat. "
                  "Trois repères, pas un texte.")

    d.billet(
        "Envoyez vos deux productions à votre enseignante.",
        exemples=[
            "L'enregistrement oral et la description écrite.",
            "Notez la question de l'assistant qui vous a le plus surpris.",
        ],
        notes="Les productions déposées sont conservées ; les corrections de l'IA ne le "
              "sont pas. Le dire au groupe : ce qu'ils envoient est ce qui sera lu.")

    return d.save(dossier)
