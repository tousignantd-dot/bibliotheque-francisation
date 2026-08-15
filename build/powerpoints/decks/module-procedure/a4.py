# -*- coding: utf-8 -*-
"""A4 · Expliquer une procédure à un collègue.
Bloc A · couleur acier (compréhension et reformulation) · 60 min.
Source : exercice `aEtapes` — les quatre étapes d'une demande de remboursement.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='acier',
        titre='Expliquer une procédure',
        chapeau="Comprendre une procédure ne suffit pas : il faut pouvoir l'expliquer à "
                "quelqu'un d'autre. C'est le test le plus honnête de ce qu'on a "
                "vraiment compris.",
        duree='60 minutes')

    d.titre(notes="Séance de reformulation. Rendre les billets de A1 au début : ils "
                  "contiennent déjà les étapes, écrites par les élèves eux-mêmes.")

    d.objectifs([
        "expliquer une procédure en quatre étapes, dans l'ordre ;",
        "employer les mots qui marquent l'ordre : d'abord, ensuite, puis, enfin ;",
        "répondre aux questions d'un collègue qui ne connaît pas la procédure ;",
        "dire ce qui est obligatoire et ce qui ne l'est pas.",
    ])

    d.tableau('Analyse', "Les mots qui marquent l'ordre",
              ['Le mot', 'Où il se place'],
              [["d'abord", "la première étape"],
               ["ensuite, puis", "les étapes du milieu"],
               ["après ça", "les étapes du milieu, à l'oral"],
               ["enfin, finalement", "la dernière étape"]],
              cle=0,
              note="Sans ces mots, une explication devient une liste et l'auditeur perd "
                   "l'ordre. Avec eux, il peut suivre sans noter.",
              notes="Écrire les quatre au tableau. Ils serviront à toutes les productions "
                    "orales du module.")

    d.regle('La règle de la séance',
            "Une étape par phrase, et un mot d'ordre au début de chaque phrase.",
            precision="« D'abord, tu ouvres l'application. Ensuite, tu prends une photo "
                      "du reçu. Puis tu inscris le montant. Enfin, tu appuies sur "
                      "Envoyer. » Quatre phrases courtes valent mieux qu'une longue.",
            notes="Faire dire les quatre phrases par un élève, puis la même chose en une "
                  "seule phrase. Le groupe entendra la différence.")

    d.cartes('Analyse', "Quatre questions qu'un collègue va poser", [
        ("« C'est quoi, cette application ? »",
         "Répondez d'abord à quoi elle sert, puis comment elle s'appelle : « C'est "
         "l'application où on fait les demandes de remboursement. Elle s'appelle "
         "Ressources+. »"),
        ("« Par où je commence ? »",
         "Une seule étape à la fois : « D'abord, tu ouvres l'application et tu appuies "
         "sur Nouvelle demande. »"),
        ("« Est-ce que c'est obligatoire ? »",
         "Répondez clairement, oui ou non, puis la conséquence : « Oui, la photo du "
         "reçu est obligatoire, sinon la demande est refusée. »"),
        ("« Ça prend combien de temps ? »",
         "Donnez le délai et la condition : « Environ dix jours ouvrables, une fois que "
         "ton superviseur a approuvé. »"),
    ], notes="Faire remarquer que chaque bonne réponse contient deux parties : la réponse "
             "et sa conséquence ou sa condition.")

    d.pratique('Pratique · 1 de 4', "Répondez à votre collègue",
               "Deux parties par réponse : l'information, puis la condition.", [
        ("C'est quoi, l'application Ressources+ ?",
         "C'est l'application où on fait les demandes de remboursement."),
        ("Quelle est la première étape ?",
         "D'abord, tu ouvres l'application et tu appuies sur Nouvelle demande."),
        ("Est-ce que je peux envoyer ma demande sans photo du reçu ?",
         "Non, la photo est obligatoire, sinon la demande est refusée."),
        ("Combien de temps avant d'être remboursé ?",
         "Environ dix jours ouvrables, une fois la demande approuvée."),
    ], corrige=True,
       notes="La troisième réponse est la plus importante : elle dit non ET pourquoi. "
             "Un simple « non » laisse le collègue sans solution.")

    d.pratique('Pratique · 2 de 4', "Remettez les étapes dans l'ordre",
               "Numérotez de 1 à 5.", [
        ("Prendre une photo claire du reçu.", "3"),
        ("Ouvrir l'application Ressources+.", "1"),
        ("Choisir la catégorie et appuyer sur Envoyer.", "5"),
        ("Appuyer sur Nouvelle demande.", "2"),
        ("Inscrire le montant exact.", "4"),
    ], corrige=True,
       notes="Laisser chercher seul trois minutes. La difficulté est entre les étapes 1 "
             "et 2, qu'on a tendance à fusionner.")

    d.pratique('Pratique · 3 de 4', "Ajoutez les mots d'ordre",
               "D'abord, ensuite, puis, enfin.", [
        ("___, tu ouvres l'application Ressources+.", "D'abord"),
        ("___, tu appuies sur Nouvelle demande.", "Ensuite"),
        ("___ tu prends une photo claire du reçu.", "Puis"),
        ("___, tu inscris le montant et tu appuies sur Envoyer.", "Enfin"),
    ], corrige=True,
       notes="Faire lire les quatre phrases d'un seul trait après correction. C'est le "
             "modèle de l'exercice oral qui suit.")

    d.piege("Le piège de l'explication en une phrase",
            "Tu ouvres l'application et tu appuies sur nouvelle demande et tu prends une photo et tu inscris le montant et tu envoies.",
            "D'abord, tu ouvres l'application. Ensuite, tu prends une photo du reçu…",
            "Une explication liée par des « et » ne se retient pas : l'auditeur perd le "
            "compte des étapes dès la troisième. Une phrase par étape, avec un mot "
            "d'ordre, et il peut suivre sans écrire.",
            notes="Faire l'expérience : dire la version longue, puis demander au groupe "
                  "de répéter les étapes. Presque personne n'y arrive.")

    d.pratique('Pratique · 4 de 4', "Jeu de rôle · expliquer à un collègue",
               "À deux. L'un explique, l'autre pose des questions. Puis on échange.", [
        ("Le collègue demande", "Comment je fais pour me faire rembourser ?"),
        ("Vous expliquez", "quatre étapes, un mot d'ordre par étape"),
        ("Le collègue demande", "Est-ce que c'est obligatoire, la photo ?"),
        ("Le collègue demande", "Ça prend combien de temps ?"),
        ("Vous concluez", "et tu gardes ton reçu original jusqu'au versement"),
    ], corrige=False,
       notes="Quinze minutes. Circuler et vérifier une seule chose : est-ce que les mots "
             "d'ordre sont là ? C'est le critère de la séance.")

    d.billet(
        "Expliquez une procédure que vous connaissez, en quatre phrases.",
        exemples=[
            "N'importe quelle procédure : au travail, à l'école, à la banque.",
            "Un mot d'ordre au début de chaque phrase : d'abord, ensuite, puis, enfin.",
        ],
        notes="Ramasser. Les procédures apportées par les élèves sont souvent meilleures "
              "que les exemples du cours : en garder quelques-unes pour E1.")

    return d.save(dossier)
