# -*- coding: utf-8 -*-
"""B1 · Je vais être absente jeudi.
Bloc B « Défi 1 · Prévenir avant » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Je vais être absente jeudi',
        chapeau="Une démarche de deux minutes au comptoir : qui je suis, "
                "quel jour je serai absente, pourquoi — et s'il faut un "
                "papier.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Rappeler les quatre formules de A4 avant de "
                  "lancer le dialogue : elles y sont toutes, dans l'ordre.")

    d.objectifs([
        "comprendre un échange au comptoir du secrétariat ;",
        "donner son nom, son prénom et son groupe ;",
        "dire le jour et le moment d'une absence ;",
        "demander s'il faut apporter un papier.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que la secrétaire a besoin de savoir ?",
        pistes=[
            "Combien de renseignements, à votre avis ?",
            "Lequel vient en premier ?",
            "Est-ce qu'elle a besoin de savoir de quoi votre fille est malade ?",
            "Qu'est-ce qu'elle écrit, exactement ?",
        ],
        notes="Recueillir les réponses avant le dialogue. Le groupe en trouve "
              "généralement trois sur quatre : le nom, le jour, la raison. Le groupe "
              "est celui qu'on oublie, et c'est celui sans lequel elle ne peut rien "
              "inscrire.")

    d.dialogue('Dialogue · 1 de 3', "Je viens le dire avant", [
        ("NAWEL", "Bonjour, madame.", True),
        ("GINETTE", "Bonjour ! Qu'est-ce que je peux faire pour vous ?", True),
        ("NAWEL", "Je vais être absente jeudi. Je viens le dire avant.", True),
        ("GINETTE", "Merci de venir avant, c'est ce qu'il faut faire. Votre nom, s'il vous plaît ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Faire remarquer que Nawel dit son affaire en une seule phrase. C'est le "
             "modèle : une phrase, pas une histoire.")

    d.dialogue('Dialogue · 2 de 3', "Toute la journée ou l'avant-midi ?", [
        ("NAWEL", "Nawel Belkacem. B, E, L, K, A, C, E, M.", True),
        ("GINETTE", "Et votre groupe ?", True),
        ("NAWEL", "Groupe 12, l'avant-midi.", True),
        ("GINETTE", "Parfait. Jeudi… le 12 mars. Toute la journée ou l'avant-midi seulement ?", True),
    ], notes="Nawel épelle son nom sans qu'on le lui demande : c'est le réflexe à "
             "prendre. Faire épeler son nom de famille par chaque élève, à voix haute.")

    d.dialogue('Dialogue · 3 de 3', "Est-ce que je dois apporter un papier ?", [
        ("NAWEL", "L'avant-midi seulement. Le rendez-vous est à neuf heures.", True),
        ("GINETTE", "La raison, en une phrase ?", True),
        ("NAWEL", "Ma fille a un rendez-vous à la clinique et je dois y aller avec elle.", True),
        ("GINETTE", "D'accord. J'écris : absence prévenue, jeudi 12 mars, avant-midi.", True),
    ], notes="« La raison, en une phrase » : la secrétaire ne demande aucun détail "
             "médical et n'en demandera jamais. Le dire au groupe — plusieurs craignent "
             "d'avoir à tout expliquer.")

    d.tableau('Analyse', "Quatre renseignements, dans cet ordre",
              ["Ce qu'on donne", "Exemple"],
              [["1. Qui", "Nawel Belkacem, groupe 12"],
               ["2. Quoi", "je vais être absente"],
               ["3. Quand", "jeudi le 12 mars, l'avant-midi"],
               ["4. Pourquoi", "ma fille a un rendez-vous à la clinique"]],
              cle=1,
              note="Et une question pour finir : est-ce que je dois apporter "
                   "un papier ?",
              notes="Diapo à photographier. C'est la carte du défi 1 tout entier. La "
                    "faire recopier au carnet avant l'exercice suivant.")

    d.regle("La raison tient en une phrase",
            "« parce que ma fille a un rendez-vous »",
            precision="Personne ne demande de détail médical, ni au comptoir "
                      "ni sur un papier. Une phrase courte suffit, et elle "
                      "suffit vraiment : « je suis malade », « j'ai un "
                      "rendez-vous », « je déménage ».",
            notes="Diapo à photographier. Rassurer explicitement : c'est une inquiétude "
                  "très répandue et elle empêche des élèves de venir prévenir.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Nawel vient au comptoir avant son absence.", "vrai"),
        ("La secrétaire demande le nom et le groupe.", "vrai"),
        ("Nawel va manquer toute la journée de jeudi.", "faux — l'avant-midi seulement"),
        ("Le rendez-vous de sa fille est à neuf heures.", "vrai"),
        ("Pour une demi-journée, un papier est obligatoire.", "faux — il n'est pas obligatoire"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. Insister sur la "
             "dernière : le papier aide, il n'oblige pas.")

    d.billet(
        "Préparez votre démarche : quatre renseignements, une question.",
        exemples=[
            "Choisissez une vraie journée où vous ne pourriez pas venir.",
            "Écrivez les quatre lignes : qui, quoi, quand, pourquoi.",
        ],
        notes="Devoir de préparation. Il sert d'entrée à B2, où l'on met la deuxième "
              "ligne au futur proche.")

    return d.save(dossier)
