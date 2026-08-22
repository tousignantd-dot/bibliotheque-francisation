# -*- coding: utf-8 -*-
"""E1 · S'informer pour choisir
Bloc E « Je me lance » · couleur teal · 75 min. Jeu de rôle et production orale.
Source : bloc « Je me lance » de custom.js, scénario `orientationscolaire`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="S'informer pour choisir",
        chapeau="Le conseiller répond à tout, mais il ne devine rien. Si "
                "vous ne dites pas votre situation, il ne peut rien "
                "calculer — et l'heure passe.",
        duree='75 minutes')

    d.titre(notes="Première séance de production. Tout ce qui précède y sert : les "
                  "questions indirectes de B4, la reprise de B3, la démarche en six "
                  "étapes de B2. Le dire au groupe avant de commencer.")

    d.objectifs([
        "exposer sa situation en phrases suivies, pas en mots isolés ;",
        "poser au moins deux questions indirectes ;",
        "reformuler la démarche à la fin pour vérifier ;",
        "expliquer ensuite cette démarche à voix haute, en quatre-vingt-dix secondes.",
    ], notes="Le troisième objectif est celui qu'on oublie et qui sauve tout : "
             "reformuler avant de partir. Une minute, et le rendez-vous devient "
             "utilisable.")

    d.declencheur(
        'Observation', "Qu'est-ce qui rate, dans un rendez-vous ?",
        pistes=[
            "Vous ne dites pas assez de choses, ou l'autre en dit trop ?",
            "Sortez-vous en général avec des dates, ou avec une impression ?",
            "Osez-vous demander de répéter ?",
        ],
        notes="Rappeler la comparaison de B2 : sortir avec « c'était intéressant » ou "
              "sortir avec quatre dates. Personne ne veut du premier.")

    d.cartes('Préparation', "Trois situations au choix", [
        ("Quel programme ?", "Vous terminez en février. Vous avez travaillé six ans dans un métier avant d'arriver ici et vous voudriez y revenir. Vous ne savez pas quel programme y mène."),
        ("Ce qui me manque", "Vous savez quel programme vous visez. Vous ne savez pas quels préalables il vous manque, ni comment on les obtient : un cours, un test, un papier ?"),
        ("Mes papiers de là-bas", "Vous avez un diplôme, un relevé de notes et une évaluation comparative. On vous a dit que c'était une équivalence. Vous voulez savoir ce que ça vaut ici."),
    ], cols=3,
       notes="Laisser choisir. La troisième situation est la plus proche du vécu de "
             "beaucoup d'élèves ; ne pas l'imposer pour autant.")

    d.tableau('Analyse', "Les sept choses à couvrir",
              ['Le moment', 'Ce qu\'il faut dire'],
              [["Au début", "votre situation, en phrases suivies, avec une date"],
               ["Tout de suite après", "ce que vous cherchez, précisément"],
               ["Pendant", "au moins deux questions indirectes"],
               ["Quand un mot échappe", "demandez de répéter ou de préciser"],
               ["Aux chiffres", "notez, puis redites la date à voix haute"],
               ["À la fin", "reformulez la démarche dans l'ordre"]],
              cle=0,
              notes="Diapositive à photographier. Elle sert de grille d'observation à "
                    "l'élève qui regarde pendant que deux autres jouent.")

    d.regle("Reformuler n'est pas répéter",
            "« Si je comprends bien, je m'inscris au test, je dépose la preuve, et on se revoit en janvier. » — une phrase, et le rendez-vous devient utilisable.",
            precision="Cette phrase-là fait deux choses à la fois : elle vérifie que "
                      "vous avez bien entendu, et elle oblige l'autre à confirmer ou "
                      "à corriger. Elle prend dix secondes et elle vaut la moitié de "
                      "l'entretien.",
            notes="Diapositive à photographier. Faire dire la phrase par tout le "
                  "groupe, à voix haute, avant de commencer le jeu de rôle.")

    d.pratique('Préparation', "Vos questions, en question indirecte",
               "Écrivez-les avant de commencer. Vous les aurez sous les yeux.", [
        ("Je me demande si ...", ""),
        ("Je voudrais savoir ...", ""),
        ("Je ne sais pas ce que ...", ""),
        ("Pouvez-vous me dire quand ...", ""),
        ("J'aimerais savoir ce qui ...", ""),
    ],
       notes="Cinq minutes, en silence. Les élèves reprennent les questions écrites "
             "au billet de B4. Circuler et corriger les « est-ce que » qui auraient "
             "survécu.")

    d.tableau('Analyse', "La production orale, en trois temps",
              ['Le temps', 'Ce qu\'on y met'],
              [["1", "de quoi il s'agit et auprès de qui vous vous êtes informé"],
               ["2", "les étapes dans l'ordre, avec les dates et les lieux"],
               ["3", "ce que vous en pensez, annoncé comme un avis"]],
              cle=0,
              note="Quatre-vingt-dix secondes. Le troisième temps est le plus court et c'est celui qu'on oublie.",
              notes="Diapositive à photographier. C'est la consigne exacte de la "
                    "production orale du module interactif ; les élèves la "
                    "retrouveront à l'écran.")

    d.piege('Production',
            "je veux de l'information sur les cours",
            "je veux savoir quels préalables il me manque",
            "Une demande vague reçoit une réponse vague, et l'heure passe en "
            "généralités. Une demande précise permet à la personne d'en face "
            "d'ouvrir votre dossier et de calculer. C'est la même politesse, "
            "et ce n'est pas le même rendez-vous.",
            notes="Faire comparer les deux à voix haute. Puis demander à chaque élève "
                  "de dire la sienne, en une phrase, avant de commencer.")

    d.billet(
        "Enregistre ta production orale, écoute-toi, recommence une fois.",
        exemples=[
            "Quatre-vingt-dix secondes, trois temps.",
            "La deuxième prise est toujours meilleure : ne t'arrête pas à la première.",
        ],
        notes="Vingt minutes. L'assistant du module donne une rétroaction avant "
              "l'envoi. Insister sur la deuxième prise : c'est là que le module "
              "produit son effet.")

    return d.save(dossier)
