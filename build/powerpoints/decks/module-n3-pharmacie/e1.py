# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle `pharmacie`, production orale et production écrite du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout le module tient dans un échange d'une minute : dire ce "
                "qui ne va pas, depuis quand, répondre aux questions, "
                "comprendre la posologie. Puis l'écrire.",
        duree='75 minutes')

    d.titre(notes="Séance d'évaluation formative. Prévoir les tablettes ou les portables "
                  "pour le jeu de rôle avec l'assistant, et un casque par élève si "
                  "possible.")

    d.objectifs([
        "mener un échange complet avec un pharmacien ;",
        "s'enregistrer, s'écouter et se corriger ;",
        "écrire une note claire de cinq à huit phrases ;",
        "déposer les deux productions à son enseignante.",
    ])

    d.tableau('Rappel', "Les trois moments de la production orale",
              ["Le moment", "Ce que vous dites"],
              [["1. Dire ce qui ne va pas", "« Je tousse et j'ai mal à la gorge. »"],
               ["2. Dire depuis quand", "« Ça dure depuis quatre jours. »"],
               ["3. Demander la posologie", "« Combien de fois par jour ? »"]],
              cle=0,
              note="Environ quarante-cinq secondes. On peut recommencer.",
              notes="Diapositive à photographier. C'est le plan exact du panneau "
                    "d'enregistrement du module interactif.")

    d.regle("Le jeu de rôle, d'abord",
            "L'assistant joue le pharmacien",
            precision="Il ne dit rien qu'on ne lui demande pas : ni le prix, ni "
                      "le délai, ni ce qu'il peut faire pour vous. Trois "
                      "situations au choix — la toux qui dure, l'ordonnance "
                      "finie, l'étiquette à comprendre — et deux rôles.",
            notes="Diapositive à photographier. Insister : c'est une répétition, pas un "
                  "examen. Un élève qui a fait le jeu de rôle deux fois réussit sa "
                  "production orale du premier coup.")

    d.cartes("Les trois situations du jeu de rôle", "À choisir", [
        ("La toux qui dure",
         "Vous toussez depuis quatre jours et vous ne dormez plus. Vous n'avez pas de "
         "médecin de famille. Vous venez demander un conseil."),
        ("L'ordonnance finie",
         "Il vous reste deux comprimés et votre ordonnance est finie. Votre rendez-vous "
         "est dans six semaines. Vous avez votre carte d'assurance maladie."),
        ("L'étiquette à comprendre",
         "Votre médicament est prêt. Sur l'étiquette : un comprimé, trois fois par "
         "jour, avec de la nourriture, pendant sept jours. Vous voulez être certain."),
        ("Les sept sujets à couvrir",
         "Saluer · dire ce qui ne va pas · dire depuis quand · répondre aux questions · "
         "sortir sa carte · demander la posologie · répéter avant de partir."),
    ], notes="Faire choisir une situation par élève, et changer de situation au second "
             "tour. Les trois se recoupent assez pour se renforcer.")

    d.tableau('Écriture', "La note pour votre voisine",
              ["Ce qu'elle doit contenir", "Exemple"],
              [["ce qu'il faut demander", "« Demande un renouvellement. »"],
               ["ce qu'il faut apporter", "« Apporte ma carte et le flacon vide. »"],
               ["une question au pharmacien", "« Est-ce que je peux le prendre le soir ? »"],
               ["la posologie", "« Un comprimé, trois fois par jour. »"]],
              cle=0,
              note="De cinq à huit phrases. Attention : mon, ma, mes, par, pendant.",
              notes="Diapositive à photographier. C'est la grille de la production "
                    "écrite du module ; l'élève la retrouve à l'écran.")

    d.pratique('Autocorrection', "Avant d'envoyer, vérifiez",
               "Relisez votre note et cochez.", [
        ("Ai-je dit ce qu'il faut demander ?", "un renouvellement, ou un conseil"),
        ("Ai-je dit ce qu'il faut apporter ?", "la carte, le flacon vide"),
        ("Ai-je posé une question avec « est-ce que » ?", "une seule suffit"),
        ("Mes petits mots sont-ils justes ?", "mon ordonnance, ma carte, mes comprimés"),
        ("Ma posologie est-elle complète ?", "combien, combien de fois, pendant combien de jours"),
    ], corrige=False,
       notes="Faire faire la vérification en paires avant l'envoi : l'élève voit mieux "
             "la note du voisin que la sienne.")

    d.billet(
        "Déposez votre enregistrement et votre note dans le module.",
        exemples=[
            "Le bouton « Envoyer à mon enseignant » est sous chaque production.",
            "Vous pouvez recommencer l'enregistrement autant de fois que vous voulez.",
        ],
        notes="Vérifier que chaque élève a bien déposé les deux productions avant la fin "
              "de la séance. Les corrections de l'assistant ne sont pas conservées : "
              "seul le dépôt l'est.")

    return d.save(dossier)
