# -*- coding: utf-8 -*-
"""C1 · Deux papiers sur la table
Bloc C « Défi 2 » · couleur acier · 75 min. Compréhension orale et écrite.
Source : dialogue `t2` et exercice `t2prog`, du type `texte`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Deux papiers sur la table",
        chapeau="La description du programme fait quatre pages ; l'avis en "
                "fait une. C'est la page qui fait peur — et c'est celle qui "
                "se lit le plus vite quand on sait où regarder.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc C. Le bloc entier porte sur l'écrit officiel : "
                  "annoncer que la voix humaine disparaît pendant deux séances et "
                  "que c'est le papier qui parle.")

    d.objectifs([
        "suivre une lecture à deux voix de deux documents officiels ;",
        "trouver dans une description de programme la durée, les voies et le stage ;",
        "repérer un passage précis d'un texte pour répondre à une question ;",
        "distinguer ce qui est décrit de ce qui est exigé.",
    ], notes="Le troisième objectif est nouveau au niveau 6 : l'élève ne résume plus, "
             "il localise. C'est l'exercice du type « texte » du module interactif.")

    d.declencheur(
        'Observation', "Quand vous recevez quatre pages, que lisez-vous ?",
        pistes=[
            "La première page en entier, ou vous cherchez tout de suite ?",
            "Qu'est-ce que vous cherchez en premier, en général ?",
            "Vous est-il arrivé de manquer quelque chose d'important ?",
        ],
        notes="Réponse honnête attendue : presque personne ne lit quatre pages. La "
              "séance ne demande pas de le faire, elle apprend à chercher.")

    d.dialogue('Dialogue · 1 de 3', "Conditionnelle, ça veut dire quoi ?", [
        ("ROSA", "Tu as reçu quoi, finalement ? Tu avais l'air blanche en sortant du comptoir.", True),
        ("BINTOU", "Deux papiers. La description du programme, quatre pages, et un avis officiel. Une page, celui-là. C'est la page qui me fait peur.", True),
        ("ROSA", "Montre. Ah, ça commence par « Avis d'admission conditionnelle ». Conditionnelle, ça veut dire quoi ?", True),
        ("BINTOU", "Que je suis acceptée, mais pas vraiment.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Arrêter sur la dernière réplique et demander au groupe si Bintou a "
             "raison. Elle a tort, et c'est une lecture inquiète très répandue : la "
             "place est bien à elle jusqu'à la date.")

    d.dialogue('Dialogue · 2 de 3', "La place est réservée jusqu'au six février", [
        ("ROSA", "Non, attends, ce n'est pas ce qui est écrit. Regarde la ligne encadrée : la place est réservée jusqu'au six février, et elle est libérée si la condition n'est pas remplie à cette date.", True),
        ("BINTOU", "Et la condition, c'est le test.", True),
        ("ROSA", "C'est le test. « La candidate fournira la preuve de réussite du test de développement général. » Fournira. Au futur.", True),
        ("BINTOU", "Pourquoi au futur ? Ce n'est pas une prédiction, c'est une obligation.", True),
    ], notes="Ne pas expliquer le futur aujourd'hui : c'est la séance C3. Se "
             "contenter de faire remarquer que Bintou a raison de s'en étonner.")

    d.dialogue('Dialogue · 3 de 3', "Toujours dans l'encadré", [
        ("BINTOU", "Regarde la description du programme, maintenant. La première page ne parle même pas du programme.", True),
        ("ROSA", "Elle raconte l'histoire du centre. « Le centre ouvrit ses portes en mille neuf cent soixante-huit. » Ouvrit.", True),
        ("BINTOU", "Et les préalables particuliers, ils sont où ?", True),
        ("ROSA", "Page trois, dans l'encadré gris, sous le titre en gras. C'est toujours dans l'encadré, ce qui compte. Le reste, c'est de la présentation.", True),
    ], notes="Deux annonces ici : le passé simple, travaillé en C4, et l'encadré, "
             "travaillé en C2. Les nommer sans les traiter.")

    d.tableau('Analyse', "Ce que la description du programme donne",
              ['On y cherche', 'On y trouve'],
              [["La durée", "onze mois à temps plein, de jour, du lundi au vendredi"],
               ["Les voies d'entrée", "trois, dans un paragraphe à part"],
               ["Le stage", "six semaines en milieu de travail, non rémunéré"],
               ["La date limite", "le 6 février, dernier jour où une place réservée demeure"]],
              cle=0,
              note="Quatre informations, quatre pages. Le reste est de la présentation, et se saute sans remords.",
              notes="Diapositive à photographier. Faire chercher les quatre "
                    "informations dans le texte de l'exercice, chronomètre en main : "
                    "trois minutes suffisent quand on sait quoi chercher.")

    d.regle("Un stage ne se remplace pas",
            "Six semaines en milieu de travail terminent la formation, et aucune expérience antérieure ne les remplace.",
            precision="C'est la réponse la plus dure du module pour un adulte qui a "
                      "déjà exercé le métier ailleurs. Elle est nette, elle est "
                      "écrite, et il vaut mieux la lire au centre que la découvrir en "
                      "novembre.",
            notes="Diapositive à photographier. Enchaîner tout de suite sur ce que "
                  "l'expérience apporte : la reconnaissance des acquis, le stage plus "
                  "facile, l'entrevue. Ne pas laisser le groupe sur le refus.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la description du programme.", [
        ("La formation dure onze mois à temps plein.", "vrai"),
        ("Elle se donne le soir, du lundi au jeudi.", "faux - de jour, du lundi au vendredi"),
        ("Trois voies mènent à l'admission.", "vrai"),
        ("Le stage dure six semaines et il est rémunéré.", "faux - il n'est pas rémunéré"),
        ("Une expérience de travail peut remplacer le stage.", "faux - aucune, quelle qu'elle soit"),
        ("Après le 6 février, la place est offerte à quelqu'un d'autre.", "vrai"),
    ], corrige=True,
       notes="Demander à chaque fois où la réponse se trouve, dans quel paragraphe. "
             "C'est ce repérage-là qu'on évalue, pas la mémoire.")

    d.billet(
        "Écris la question que tu poserais après avoir lu ces quatre pages.",
        exemples=[
            "Une seule question, la plus utile.",
            "Écris-la en question indirecte, comme en B4.",
        ],
        notes="Quatre minutes. Ces questions serviront en C2 : plusieurs auront leur "
              "réponse dans l'avis officiel, ce qui montre au groupe qu'un document "
              "répond souvent à ce qu'on allait demander au téléphone.")

    return d.save(dossier)
