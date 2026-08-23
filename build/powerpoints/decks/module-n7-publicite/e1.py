# -*- coding: utf-8 -*-
"""E1 · L'appel, et l'exposé
Bloc E « Je me lance » · couleur teal · production orale · 75 min.
Source : section `appli` du module — jeu de rôle `publicite`, production orale.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="L'appel, et l'exposé",
        chapeau="Un appel qui reproche n'obtient rien. Un appel qui nomme "
                "précisément ce qui n'était pas dit obtient une réponse. "
                "Ensuite, deux minutes debout pour démonter une annonce.",
        duree='75 minutes')

    d.titre(notes="Première séance de production. Les élèves arrivent avec leur "
                  "annonce, notée dès A1 et travaillée à chaque billet de sortie. "
                  "Vérifier que chacun l'a avant de commencer.")

    d.objectifs([
        "exposer au téléphone ce qu'une annonce laissait croire ;",
        "poser une question précise sur ce qu'elle ne disait pas ;",
        "reformuler la réponse reçue pour la faire confirmer ;",
        "démonter une annonce en trois temps devant la classe.",
    ], notes="Le deuxième objectif est celui qui décide de tout. « Ce n'est pas "
             "correct » n'obtient rien ; « pourriez-vous me confirmer le total de la "
             "première année » obtient un chiffre.")

    d.declencheur(
        'Préparation', "Que demandez-vous, exactement ?",
        pistes=[
            "Vous appelez pour vous plaindre, ou pour obtenir quelque chose ?",
            "Qu'est-ce que vous voulez qu'on vous dise ?",
            "Quel chiffre vous manque-t-il encore ?",
            "Que ferez-vous de la réponse ?",
        ],
        notes="La deuxième question est la plus utile. Un appel sans demande précise "
              "se termine par « tout était dans les conditions », et l'élève "
              "raccroche sans rien.")

    d.tableau('Analyse', "Les sept sujets de l'appel",
              ['Le moment', 'Ce qu\'on dit'],
              [["Se présenter", "qui vous êtes, et pourquoi vous appelez"],
               ["Rappeler l'annonce", "ce qu'elle laissait croire, sans accuser"],
               ["Poser la question", "une question précise, sur un chiffre"],
               ["Faire préciser", "un montant, une durée, une date"],
               ["Reformuler", "autrement dit… si je comprends bien…"],
               ["Demander l'écrit", "une confirmation avant de raccrocher"]],
              cle=0,
              notes="Diapositive à photographier, et à garder ouverte pendant l'appel. "
                    "Le jeu de rôle du module suit exactement cette liste.")

    d.cartes('Analyse', "Les tournures à réutiliser", [
        ("Demander poliment", "Pourriez-vous me confirmer le montant total de la première année ?"),
        ("Reformuler", "Autrement dit, je m'engage pour douze mois. C'est bien ça ?"),
        ("Accorder, puis maintenir", "Bien que le tarif soit exact, l'annonce ne mentionnait pas les frais."),
        ("Limiter", "L'annonce ne donnait que le prix par semaine."),
        ("Dire le degré", "La condition était écrite trop petit pour que je la voie."),
        ("Conclure", "En somme, à qui dois-je m'adresser pour la suite ?"),
    ], cols=1,
       notes="Les six tournures viennent des six séances de grammaire du module. "
             "Chacune a été travaillée : le rappeler, ça donne confiance.")

    d.piege('Oral',
            "« Votre annonce est mensongère. »",
            "« L'annonce ne mentionnait pas les frais d'adhésion. »",
            "La première est une accusation, et elle se répond en une ligne : "
            "« tout était dans les conditions ». La seconde est un fait "
            "vérifiable, et elle oblige l'interlocuteur à répondre sur le "
            "fond. Nommer précisément ce qui manquait est la seule chose qui "
            "fasse avancer un appel.",
            notes="À dire avant de lancer le jeu de rôle. La différence entre les deux "
                  "phrases est ce que le module entier a servi à construire.")

    d.pratique('Jeu de rôle', "Trois situations au choix",
               "Choisissez-en une, et menez l'appel jusqu'au bout.", [
        ("L'abonnement à 9,99 $", "faire préciser le total, la durée, les frais"),
        ("La trottinette « offerte »", "demander s'il y a eu contrepartie"),
        ("L'affiche du commerce neuf", "expliquer la règle sans accuser"),
        ("Dans les trois cas", "demander une confirmation écrite avant de raccrocher"),
    ], corrige=False,
       notes="Le module offre les trois situations avec l'assistant. En classe, faire "
             "travailler en paires, l'un tenant la liste des sept sujets et cochant "
             "au fur et à mesure.")

    d.tableau('Production orale', "L'exposé, en trois temps",
              ['Le temps', 'Ce qu\'on dit'],
              [["Ce que l'annonce montre", "où, quand, combien de fois vue"],
               ["Ce qu'elle promet sans le dire", "la phrase exacte, entre guillemets"],
               ["Le procédé, nommé", "et ce que vous en concluez"]],
              cle=0,
              note="Deux minutes, debout, sans lire ses notes mot à mot.",
              notes="Diapositive à photographier. Le deuxième temps est celui qu'on "
                    "escamote : exiger la citation exacte, préparée depuis B4.")

    d.billet(
        "Écrivez les trois phrases de votre exposé, une par temps.",
        exemples=[
            "Une seule phrase par temps, pas un paragraphe.",
            "La deuxième doit contenir une citation entre guillemets.",
        ],
        notes="Devoir de préparation. Trois phrases suffisent : un exposé de deux "
             "minutes qui tient sur trois phrases est meilleur qu'un texte lu.")

    return d.save(dossier)
