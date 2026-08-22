# -*- coding: utf-8 -*-
"""E1 · Je me lance : se renseigner à voix haute.
Bloc E « Je me lance » · teal · 75 min. Production orale.
Source du module : dialogue `appli`, exercice `aQui`, jeu de rôle « loisirs »
et production orale de « Je me lance ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Se renseigner à voix haute",
        chapeau="Marisol y retourne seule, pour une activité qu'elle n'a "
                "jamais essayée. Quatre questions, une récapitulation, et "
                "c'est fait. À votre tour : votre activité, votre quartier, "
                "votre voix.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Le jeu de rôle avec l'assistant se fait à "
                  "l'écran, en autonomie, avant l'enregistrement : c'est une répétition, "
                  "pas une évaluation. Le dire clairement en ouvrant.")

    d.objectifs([
        "me renseigner sur une activité, du bonjour au merci ;",
        "poser mes quatre questions, une à la fois ;",
        "faire répéter ce que je n'ai pas compris ;",
        "récapituler ce que j'ai retenu avant de partir.",
    ])

    d.dialogue('Dialogue · 1 de 2', "Toute seule au comptoir", [
        ("MARISOL", "Bonjour. Je voudrais des renseignements sur la danse en ligne.", True),
        ("ROXANE", "Bonjour ! C'est le jeudi soir, de sept heures à huit heures et demie.", True),
        ("MARISOL", "Le jeudi soir. Est-ce que ça commence cette semaine ?", True),
        ("ROXANE", "La session commence le 2 octobre. Dix semaines, jusqu'en décembre.", True),
        ("MARISOL", "Et le tarif ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Marisol pose ses questions dans l'ordre du module et répète chaque réponse. "
             "Compter à voix haute avec le groupe : une question, une réponse, une "
             "répétition. C'est le rythme à tenir dans l'enregistrement.")

    d.dialogue('Dialogue · 2 de 2', "Un essai gratuit", [
        ("ROXANE", "Soixante dollars pour les dix semaines, avec la preuve d'adresse.", True),
        ("MARISOL", "Est-ce qu'il faut apporter quelque chose ?", True),
        ("ROXANE", "Des souliers plats, pas de talons. Et de l'eau.", True),
        ("MARISOL", "Des souliers plats. Est-ce que je peux venir voir une fois avant de décider ?", True),
        ("ROXANE", "Bien sûr. Le premier jeudi est un essai gratuit.", True),
    ], notes="La question de l'essai gratuit est celle que personne n'ose poser, et elle "
             "existe presque partout. L'ajouter à la liste des sept sujets du jeu de "
             "rôle : « est-ce que je peux venir voir une fois ? »")

    d.pratique('Compréhension', "Qui parle ?",
               "Marisol, ou Roxane la préposée ?", [
        ("« Je voudrais des renseignements sur la danse en ligne. »", "Marisol"),
        ("« C'est le jeudi soir, de sept heures à huit heures et demie. »", "Roxane"),
        ("« Est-ce que ça commence cette semaine ? »", "Marisol"),
        ("« Soixante dollars pour les dix semaines. »", "Roxane"),
        ("« Est-ce que je peux venir voir une fois avant de décider ? »", "Marisol"),
        ("« Le premier jeudi est un essai gratuit. »", "Roxane"),
    ], corrige=True,
       notes="C'est l'exercice aQui du module. Faire remarquer que toutes les répliques "
             "de Marisol sont des questions, et toutes celles de Roxane des réponses : "
             "c'est la forme même de la situation.")

    d.tableau('Le plan', "La production orale, en trois temps",
              ["Temps", "Ce qu'on dit"],
              [["1. Saluer et dire ce qu'on cherche",
                "Bonjour. Je voudrais des renseignements sur…"],
               ["2. Poser les quatre questions",
                "C'est quand ? C'est combien ? C'est où ? Quoi apporter ?"],
               ["3. Récapituler et remercier",
                "Alors le mardi, à sept heures, trois dollars… Merci beaucoup !"]],
              cle=0,
              note="Environ 45 secondes. On peut recommencer autant de fois qu'on veut.",
              notes="Diapo à photographier — c'est la consigne de l'enregistrement. La "
                    "laisser à l'écran pendant que le groupe s'enregistre.")

    d.regle("Le jeu de rôle vient avant",
            "On répète avec l'assistant, puis on s'enregistre.",
            precision="À l'écran, l'assistant joue Roxane, la préposée. Elle ne donne "
                      "rien qu'on ne lui demande pas : c'est à vous d'aller chercher "
                      "chaque renseignement. Trois situations au choix — le badminton, "
                      "le ciné-club, la cuisine collective. On peut recommencer autant "
                      "de fois qu'on veut, et ça ne compte pas.",
            notes="Diapo à photographier. Insister sur « ça ne compte pas » : le jeu de "
                  "rôle est une répétition privée, et rien n'en est conservé. Seul "
                  "l'enregistrement envoyé arrive chez l'enseignante.")

    d.cartes("Deux phrases à garder sous la main", "Elles sauvent l'échange", [
        ("Vous pourriez répéter, s'il vous plaît ?",
         "Quand ça va trop vite. Elle ne dit pas « je ne comprends rien » : elle demande "
         "une deuxième écoute, ce que tout le monde accorde volontiers."),
        ("Alors, le mardi, à sept heures, trois dollars, des espadrilles.",
         "Avant de partir. Dix secondes, et l'erreur de soir est évitée. La personne "
         "confirme — « c'est exactement ça » — ou corrige."),
    ], cols=1,
       notes="Les faire dire à voix haute une dernière fois avant l'enregistrement. Ce "
             "sont les deux phrases que la rétroaction de l'assistant cherchera.")

    d.pratique('Pratique', "Deux par deux, avant de s'enregistrer",
               "Dos à dos. L'un se renseigne, l'autre répond. Puis on échange.", [
        ("Choisissez une activité", "la vôtre, pas celle du module"),
        ("Saluez et dites ce que vous cherchez", "« Je voudrais des renseignements sur… »"),
        ("Posez vos quatre questions", "une à la fois, en attendant la réponse"),
        ("Faites répéter au moins une fois", "« Vous pourriez répéter, s'il vous plaît ? »"),
        ("Récapitulez avant de partir", "les quatre renseignements, dans l'ordre"),
    ], notes="Circuler et noter les récapitulations réussies, pas les erreurs. Cinq "
             "minutes par personne suffisent : c'est court, et c'est voulu.")

    d.billet(
        "Enregistrez-vous, écoutez-vous, recommencez si vous voulez.",
        exemples=[
            "Environ 45 secondes, les trois temps du plan.",
            "Demandez la rétroaction avant d'envoyer à votre enseignant.",
        ],
        notes="L'enregistrement se fait dans le module, section « Je me lance ». La "
              "correction de l'assistant reste privée ; seul ce que l'élève choisit "
              "d'envoyer arrive dans le portail enseignant.")

    return d.save(dossier)
