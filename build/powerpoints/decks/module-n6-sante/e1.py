# -*- coding: utf-8 -*-
"""E1 · La consultation, pour vrai
Bloc E « Je me lance » · couleur teal · 75 min. Jeu de rôle et production orale.
Source : `ROLE_CAS` de custom.js et la production orale du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="La consultation, pour vrai",
        chapeau="Vingt minutes, et c'est vous qui parlez. L'assistant répond "
                "à tout ce que vous demandez, mais il ne devine rien : si "
                "vous ne racontez pas, il n'a rien à chercher.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Prévoir trente minutes de jeu de rôle à "
                  "l'écran et vingt minutes d'enregistrement. Le reste est de la "
                  "préparation et de l'écoute mutuelle.")

    d.objectifs([
        "s'informer auprès d'une spécialiste en posant ses propres questions ;",
        "raconter dans l'ordre, avec des repères de temps ;",
        "demander qu'on répète ou qu'on explique un mot ;",
        "raconter ensuite le rendez-vous à un proche, en trois temps.",
    ], notes="Le troisième objectif est celui qu'on oublie de pratiquer et qui sauve "
             "le plus de rendez-vous. Le faire répéter avant le jeu de rôle.")

    d.declencheur(
        'Observation', "Ressortez votre billet de la séance C2",
        pistes=[
            "C'est la phrase que vous diriez en entrant dans le bureau.",
            "Est-ce qu'elle contient une date ou un changement ?",
            "Est-ce que vous la diriez encore aujourd'hui, ou l'amélioreriez-vous ?",
        ],
        notes="Cinq minutes. Rendre les billets de C2. Chacun entrera dans le jeu de "
              "rôle avec sa propre première phrase, écrite trois semaines plus tôt : "
              "c'est le moment le plus satisfaisant du module.")

    d.tableau('Analyse', "Trois situations au choix",
              ['La situation', 'Ce que vous devez obtenir'],
              [["Huit mois de fatigue", "faire comprendre ce qui a changé, et depuis quand"],
               ["Un mot sur une feuille", "savoir ce qu'un résultat dit, et ce qu'il ne dit pas"],
               ["Et après ?", "repartir en sachant qui fait quoi, et avec quel papier"]],
              cle=0,
              note="Choisissez celle qui ressemble le plus à ce que vous vivez : le jeu de rôle sert mieux quand il n'est pas imaginaire.",
              notes="Diapositive à photographier. Laisser choisir librement. Ceux qui "
                    "prennent la troisième situation ont souvent un rendez-vous "
                    "réel qui approche.")

    d.tableau('Analyse', "Les sept sujets à couvrir",
              ['Le sujet', 'Un exemple de phrase'],
              [["Raconter dans l'ordre", "ça a commencé en février, quand mon fils est parti"],
               ["Un changement", "avant je montais en parlant, maintenant j'arrête"],
               ["Un exemple précis", "chez ma cliente, il y a douze marches"],
               ["Demander à répéter", "je ne connais pas ce mot, pouvez-vous l'expliquer ?"],
               ["Redire la suite", "donc je repasse au laboratoire, puis vous m'appelez"]],
              cle=0,
              note="Et deux de plus : répondre sans minimiser, et poser au moins deux questions à vous.",
              notes="Diapositive à photographier. La note du bas porte les deux "
                    "derniers sujets : le tableau refuserait sept rangées, et ces "
                    "deux-là méritent d'être répétés à voix haute avant de commencer.")

    d.regle("L'assistant ne donnera aucun diagnostic",
            "Il explique une démarche, il demande des examens, et il dit ce qu'il ne sait pas.",
            precision="C'est voulu, et c'est réaliste : une première consultation se "
                      "termine presque toujours par un plan et non par une réponse. "
                      "Ce qui s'exerce ici est la langue d'une consultation, pas la "
                      "médecine — aucun conseil de santé n'y est donné.",
            notes="Diapositive à photographier. Le dire avant de commencer évite deux "
                  "malentendus : celui de l'élève qui attend une réponse, et celui "
                  "qui croirait recevoir un avis médical.")

    d.cartes('Rappel', "Cinq structures à réutiliser", [
        ("Reculer d'un cran", "Mon médecin avait envoyé la demande en avril."),
        ("Accrocher un moment", "C'est le mois où mon fils a déménagé."),
        ("Annoncer un exemple", "Je monte moins bien, par exemple les douze marches."),
        ("Reprendre sans répéter", "Une fatigue est arrivée. Cette fatigue n'est pas repartie."),
        ("Vérifier une consigne", "Il faut que je note mes journées, c'est bien ça ?"),
    ], notes="Une carte à la fois, lue à voix haute par le groupe. Ce sont les cinq "
             "points de langue du module, réunis en cinq phrases utilisables telles "
             "quelles.")

    d.pratique('Préparation', "Vos deux questions, écrites",
               "Cinq minutes, en silence, avant d'ouvrir l'écran.", [
        ("Question 1 : celle qui passe avant les autres.", ""),
        ("Question 2 : celle que vous oublieriez.", ""),
    ],
       notes="Cinq minutes. Sans ces deux lignes, le jeu de rôle devient un "
             "interrogatoire où l'élève ne fait que répondre — exactement ce que le "
             "module cherche à défaire.")

    d.tableau('Production orale', "Raconter le rendez-vous, en trois temps",
              ['Le temps', 'Ce qu\'on y met'],
              [["Temps 1", "pourquoi j'y allais, et depuis quand j'attendais"],
               ["Temps 2", "ce qu'elle a demandé et ce qu'elle a expliqué"],
               ["Temps 3", "ce qui arrive ensuite, avec les dates"]],
              cle=0,
              note="Quatre-vingt-dix secondes environ. On peut recommencer autant de fois qu'on veut.",
              notes="Diapositive à photographier. Le troisième temps est celui qu'on "
                    "escamote : rappeler qu'une nouvelle sans date laisse "
                    "l'interlocuteur aussi inquiet qu'avant.")

    d.billet(
        "Qu'est-ce qui a été le plus difficile dans le jeu de rôle ?",
        exemples=[
            "Trouver les mots ? Poser une question ? Ne pas dire « ça va » ?",
            "Une phrase suffit.",
        ],
        notes="Deux minutes, à la toute fin. Lire les billets avant E2 : ils disent "
              "quoi reprendre en cinq minutes au début de la dernière séance.")

    return d.save(dossier)
