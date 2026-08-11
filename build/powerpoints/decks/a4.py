# -*- coding: utf-8 -*-
"""A4 · Nommer et classer un problème.
Bloc A · couleur teal · 50 min.
Source : exercices `prImg` (photos de problèmes) et `prType` (types de problème).
"""
from theme import Deck

IMG = '/Users/danieltousignant/Claude/bibliotheque-francisation/assets/interactive/module-probleme/images/'


def build(dossier):
    d = Deck(
        code='A4', section='teal',
        titre='Nommer et classer un problème',
        chapeau="Une fuite, un bris, une infiltration, de l'insalubrité, un trouble de "
                "voisinage : chaque type de problème a son mot, et ce mot dit à lui seul "
                "à qui s'adresser et à quelle vitesse.",
        duree='50 minutes')

    d.titre(notes="Dernière séance du bloc A. Reprendre les billets de sortie de la séance A1 : "
                  "on va classer les problèmes que le groupe a lui-même décrits.")

    d.objectifs([
        "reconnaître un problème sur une photo et le décrire en une phrase ;",
        "nommer le type de problème avec le mot juste ;",
        "distinguer ce qui est urgent de ce qui peut attendre ;",
        "distinguer ce qui relève de mon logement de ce qui relève de l'immeuble.",
    ])

    d.declencheur('Observation', "Décrivez ce que vous voyez en une seule phrase.",
                  image=IMG + 'moisissure.jpg',
                  pistes=[
                      "Quelle est la couleur ? Où est-ce, exactement ?",
                      "Est-ce que c'est de la saleté ou autre chose ?",
                      "Le mot juste : de la moisissure.",
                      "D'où vient la moisissure ? De l'humidité, pas du manque de ménage.",
                  ],
                  notes="Point important à dire clairement : la moisissure n'est pas une "
                        "question de propreté. Beaucoup d'élèves ont honte de la signaler, "
                        "croyant qu'on va les accuser de mal entretenir leur logement.")

    d.pratique('Pratique', 'Décrire ce qu\'on voit',
               "Chaque phrase décrit une des photos du module. Laquelle ?", [
        ("De la moisissure noire s'est formée dans le coin du mur.", "photo du mur de la salle de bain"),
        ("Le robinet de la cuisine coule goutte à goutte.", "photo du robinet"),
        ("La serrure de la porte d'entrée a été forcée.", "photo de la serrure"),
        ("Les lattes du plancher de bois ont gondolé.", "photo du plancher"),
        ("La prise de courant est noircie autour des trous.", "photo de la prise"),
        ("Une tache brune s'agrandit au plafond de la chambre.", "photo du plafond"),
    ], corrige=True,
       notes="Projeter les photos du module en parallèle, dans l'activité interactive. "
             "Faire remarquer la structure commune : quoi · où · depuis quand ou comment.")

    d.regle('Le mot du type',
            "Chaque type de problème a son mot — et ce mot dit déjà l'urgence.",
            precision="Une fuite, un bris, une infiltration, une défectuosité, un excès "
                      "d'humidité, une invasion d'insectes, de l'insalubrité, un trouble "
                      "de voisinage. Dire « il y a une infiltration » ne décrit pas seulement "
                      "de l'eau : ça annonce un dégât qui va empirer, donc une intervention "
                      "rapide.",
            notes="Écrire les huit mots au tableau. Ils servent de banque pour l'exercice "
                  "qui suit.")

    d.pratique('Pratique', 'Nommer le type de problème',
               "Associez chaque situation au mot qui la nomme.", [
        ("Le robinet goutte jour et nuit.", "une fuite"),
        ("Des fourmis sortent de la plinthe de la cuisine.", "une invasion d'insectes"),
        ("La vitre de la fenêtre est cassée.", "un bris"),
        ("Le miroir de la salle de bain reste embué une heure.", "un excès d'humidité"),
    ], corrige=True)

    d.pratique('Pratique', 'Suite',
               "Même consigne. Les quatre derniers.", [
        ("Des déchets s'accumulent devant le local à ordures.", "de l'insalubrité"),
        ("Le calorifère ne chauffe plus même à vingt-deux degrés.", "une défectuosité"),
        ("L'eau de pluie entre par le toit.", "une infiltration"),
        ("La musique du voisin s'entend jusqu'à deux heures du matin.", "un trouble de voisinage"),
    ], corrige=True,
       notes="« Insalubrité » est un mot fort, qui a un sens légal. Le distinguer de "
             "« malpropreté » : l'insalubrité est dangereuse pour la santé.")

    d.cartes('Classer', "Deux questions à se poser", [
        ("Est-ce urgent ?",
         "Urgent : ce qui met en danger, ce qui abîme vite, ce qui rend le logement "
         "invivable. Un dégât d'eau, une panne de chauffage en hiver, une serrure forcée. "
         "On appelle le jour même."),
        ("Ou est-ce que ça peut attendre ?",
         "Un robinet qui goutte, une vitre fêlée, une porte qui coince. On signale par "
         "écrit et on laisse un délai raisonnable — mais on signale quand même."),
        ("Est-ce chez moi ?",
         "Ce qui est à l'intérieur de mon logement : appareils, murs, plafonds, plomberie. "
         "Je m'adresse à la personne propriétaire."),
        ("Ou est-ce dans l'immeuble ?",
         "Corridors, escaliers, local à ordures, stationnement, entrée. Ce sont les parties "
         "communes : le concierge est le premier contact, et le problème touche tout le monde."),
    ], notes="Ces deux questions structurent tout le reste du module : le bloc B traite du "
             "logement, le bloc C des parties communes.")

    d.tableau('Classement · 1 de 2', "Ce qui n'attend pas",
              ['Situation', 'Type', 'Urgence'],
              [["L'eau de pluie entre par le toit", "une infiltration", "urgent"],
               ["Le calorifère ne chauffe plus", "une défectuosité", "urgent en hiver"],
               ["Des fourmis sortent de la plinthe", "une invasion d'insectes", "rapide"],
               ["Déchets devant le local à ordures", "de l'insalubrité", "rapide"]],
              cle=1,
              note="Urgent veut dire : on téléphone le jour même, et on confirme par écrit "
                   "après l'appel.",
              notes="Demander au groupe s'il est d'accord avec la colonne urgence. Les "
                    "désaccords sont utiles : tout dépend de la saison et de qui habite le "
                    "logement — un bébé change tout.")

    d.tableau('Classement · 2 de 2', "Ce qui peut attendre — mais se signale quand même",
              ['Situation', 'Type', 'Urgence'],
              [["La vitre de la fenêtre est cassée", "un bris", "selon la saison"],
               ["Le miroir reste embué une heure", "un excès d'humidité", "peut attendre"],
               ["Le robinet goutte", "une fuite", "peut attendre"],
               ["La musique jusqu'à deux heures", "un trouble de voisinage", "à documenter"]],
              cle=1,
              note="« À documenter » veut dire : notez les dates et les heures avant de vous "
                   "plaindre. Un trouble de voisinage ne se règle pas sur un seul incident.",
              notes="Insister sur la dernière ligne : c'est le sujet complet de la séance D2.")

    d.piege('Signaler',
            "Ce n'est pas assez grave pour déranger.",
            "Je le signale par écrit, même si ça peut attendre.",
            "Un problème non signalé qui empire devient votre responsabilité, pas celle de "
            "la propriétaire. Une petite tache signalée par courriel en novembre reste son "
            "problème en mars ; la même tache jamais signalée devient discutable. Signaler "
            "n'oblige personne à venir le jour même — ça met simplement une date sur le "
            "problème.",
            notes="Relier explicitement au billet de sortie de A1 : « je ne veux pas "
                  "déranger » est la phrase à défaire pendant tout ce module.")

    d.billet(
        "Classez le problème que vous avez décrit à la séance A1.",
        exemples=[
            "Trois choses : son type · urgent ou non · dans mon logement ou dans l'immeuble.",
            "Exemple : « une fuite · peut attendre · dans mon logement ».",
        ],
        notes="Rendre les billets de A1 en début de séance pour que chacun retrouve sa phrase. "
              "Fin du bloc A : le groupe est prêt pour la tâche 1.")

    return d.save(dossier)
