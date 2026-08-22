# -*- coding: utf-8 -*-
"""A3 · Les seize mots du club
Bloc A « Je découvre » · couleur framboise · vocabulaire · 75 min.
Source : exercices `prVocab` et `prMot`, cartes `FC_CARDS`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='framboise',
        titre="Les seize mots du club",
        chapeau="Quatre familles : ce qu'on apporte, ce qui fait une "
                "histoire, les mots de la bande dessinée, et ceux de "
                "l'appréciation. Les seize se retrouvent dans les cartes "
                "mémoire du module et dans les trois exercices de « Je "
                "retiens des mots ».",
        duree='75 minutes')

    d.titre(notes="Séance de vocabulaire. Elle prépare tout le reste du module : les mots "
                  "de la troisième famille servent au défi 2, ceux de la quatrième au "
                  "défi 3. Ne pas tout donner d'un coup — les quatre familles se "
                  "présentent l'une après l'autre, avec un temps de pratique entre "
                  "chacune.")

    d.objectifs([
        "nommer une œuvre et son support avec le mot précis ;",
        "distinguer l'objet — le livre, l'album — de ce qu'il contient — l'histoire ;",
        "employer les mots de la bande dessinée : case, bulle, planche, onomatopée ;",
        "remplacer « c'est bon » par un adjectif qui dit quelque chose.",
    ], notes="Le deuxième objectif revient plusieurs fois dans le module : « le roman » "
             "désigne l'objet, « l'histoire » désigne ce qu'il y a dedans. La distinction "
             "sert à la reprise du défi 2 et elle règle plusieurs fautes d'un coup.")

    d.declencheur(
        'Mise en route', "Comment appelle-t-on la page complète d'une bande "
                         "dessinée ? Et le petit carré dedans ?",
        pistes=[
            "Quels mots employez-vous dans votre première langue ?",
            "Est-ce qu'un « album » veut dire la même chose en français ?",
            "Comment dit-on le bruit écrit en grosses lettres : BANG, TOC ?",
            "Et l'histoire elle-même, comment l'appelle-t-on ?",
        ],
        notes="Beaucoup d'élèves ont lu de la bande dessinée dans leur langue et n'ont "
              "jamais eu besoin de la nommer en français. Faire écrire les mots de la "
              "langue première au tableau à côté des mots français : la comparaison des "
              "onomatopées est toujours un bon moment.")

    d.vocabulaire('Famille 1 sur 4', "Ce qu'on apporte au club", [
        ("une œuvre", "Ce que quelqu'un a créé pour être lu, vu ou écouté."),
        ("un roman", "Un livre épais qui raconte une histoire inventée."),
        ("une série", "Une histoire coupée en épisodes qu'on suit l'un après l'autre."),
        ("un coup de cœur", "L'œuvre qu'on a envie de faire connaître tout de suite."),
        ("un extrait", "Un petit morceau : quelques pages, quelques minutes."),
    ], notes="« Un coup de cœur » est le mot de la bibliothèque : il est sur les cartons "
             "du comptoir, sur les tablettes, dans les infolettres. Le comprendre, c'est "
             "comprendre la moitié des affiches de l'entrée.")

    d.vocabulaire('Famille 2 sur 4', "Ce qui fait une histoire", [
        ("l'intrigue", "L'histoire elle-même : ce qui arrive aux personnages."),
        ("un personnage", "Une personne inventée à qui il arrive quelque chose."),
        ("le dénouement", "La toute fin, celle qui ne se raconte jamais."),
    ], notes="« Le dénouement » est le mot le plus important de la séance : c'est la "
             "limite du défi 1. Faire répéter la phrase du club : « on s'arrête avant le "
             "dénouement ».")

    d.vocabulaire('Famille 3 sur 4', "Les mots de la bande dessinée", [
        ("une case", "Le petit cadre, avec un dessin à l'intérieur."),
        ("une bulle", "La forme blanche qui contient les paroles d'un personnage."),
        ("une planche", "La page complète, avec toutes ses cases."),
        ("une onomatopée", "Un bruit écrit en grosses lettres, hors des bulles."),
        ("un album", "Le livre lui-même, souvent grand et cartonné."),
    ], notes="Donner l'ordre du plus petit au plus grand : bulle, case, planche, album. "
             "Une bulle tient dans une case, une case tient dans une planche, une planche "
             "tient dans un album. Retenu comme ça, personne ne se trompe plus.")

    d.vocabulaire('Famille 4 sur 4', "Dire ce qu'on en pense", [
        ("émouvant", "Se dit d'une œuvre qui serre le cœur."),
        ("prévisible", "Se dit d'une histoire dont on devine la suite d'avance."),
        ("recommander", "Conseiller une œuvre en disant pourquoi."),
    ], notes="Ces trois mots préparent le défi 3. Demander au groupe trois autres "
             "adjectifs pour parler d'une œuvre : lent, drôle, dur, surprenant, "
             "reposant. Les écrire au tableau et les garder affichés jusqu'à E1.")

    d.tableau('L\'objet et son contenu', "Deux mots pour la même chose, et ce n'est pas pareil",
              ['On parle de l\'objet', 'On parle de ce qu\'il contient'],
              [["le roman", "l'histoire"],
               ["l'album", "le récit"],
               ["le livre", "l'intrigue"],
               ["la série", "les épisodes"],
               ["On l'achète, on l'emprunte", "On la raconte, on l'aime"]],
              cle=1,
              notes="La dernière rangée donne le test : on achète un livre, on raconte une "
                    "histoire. « J'ai acheté une histoire » ne se dit pas. La distinction "
                    "servira à la reprise du défi 2, où il faut changer de mot à chaque "
                    "phrase sans changer de sujet.")

    d.pratique('Le mot juste', "Complétez avec le mot qui convient",
               "œuvre · roman · série · album · extrait · coup de cœur", [
        ("Chaque membre du club présente une ___ qu'il a aimée.", "œuvre"),
        ("J'ai fini mon ___ de quatre cents pages dans l'autobus.", "roman"),
        ("La ___ compte huit épisodes de quarante minutes chacun.", "série"),
        ("L'___ que vous tenez est le premier tome de la série.", "album"),
        ("Elle lit un ___ de deux pages pour donner le ton.", "extrait"),
        ("Le comptoir affiche les ___ du mois sur de petits cartons.", "coups de cœur"),
    ], corrige=True,
       notes="C'est l'exercice `prMot` du module interactif. Le faire à l'oral d'abord, "
             "puis le laisser refaire à l'écran. Sur la première ligne, accepter aussi "
             "« œuvre » au pluriel si l'élève l'explique.")

    d.piege("Confondre la série et l'album",
            "J'ai lu la série au complet. (…il n'a lu qu'un tome)",
            "J'ai lu le premier tome de la série.",
            "La série est l'ensemble ; l'album ou le tome est le livre qu'on a entre "
            "les mains. Au comptoir de la bibliothèque, la différence décide de ce "
            "qu'on vous donne.",
            notes="Faire la même distinction pour les séries télévisées : une saison, un "
                  "épisode, la série. Les élèves qui regardent des séries l'ont déjà, et "
                  "ils peuvent l'expliquer aux autres mieux que l'enseignante.")

    d.billet(
        "Écrivez cinq des seize mots, avec la définition dans vos propres mots.",
        exemples=[
            "Choisissez au moins un mot de la bande dessinée.",
            "Choisissez au moins un adjectif pour dire ce qu'on pense d'une œuvre.",
        ],
        notes="Le billet vérifie la séance et prépare les cartes mémoire du module : les "
              "définitions écrites par les élèves sont souvent meilleures que celles du "
              "banc, et elles se réemploient à la séance E2.")

    return d.save(dossier)
