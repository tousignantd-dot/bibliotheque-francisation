# -*- coding: utf-8 -*-
"""B4 · L'affiche du comptoir.
Bloc B « Défi 1 · Prévenir avant » · couleur acier · 60 min.
Source : exercices `t1phrases` et `t1b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre="L'affiche du comptoir",
        chapeau="Ce qui est écrit au mur du secrétariat répond déjà à la "
                "moitié des questions. Encore faut-il savoir le lire — et "
                "comprendre ce que la secrétaire dit.",
        duree='60 minutes')

    d.titre(notes="Séance de compréhension. Si votre centre a une vraie affiche au "
                  "comptoir, la photographier et la projeter à côté de celle-ci : la "
                  "comparaison vaut tout le reste de la séance.")

    d.objectifs([
        "lire une affiche de renseignements administratifs ;",
        "comprendre les phrases courantes de la secrétaire ;",
        "trouver ce qu'il faut faire selon la situation ;",
        "distinguer une absence prévue d'une absence imprévue.",
    ])

    d.tableau('Lecture', "Affiche posée au comptoir du secrétariat",
              ["Situation", "Ce qu'il faut faire"],
              [["Heures d'ouverture", "du lundi au vendredi, de 7 h 45 à 15 h 30"],
               ["Une absence prévue", "venez le dire au comptoir avant la journée manquée"],
               ["Une absence imprévue", "téléphonez au 514 555-0142 avant 9 h"],
               ["Un papier", "billet de clinique ou de garderie : apportez l'original"]],
              cle=1,
              note="La suite de l'affiche est sur la diapositive suivante.",
              notes="Diapo à photographier. Une affiche de huit lignes ne se lit pas de "
                    "loin : c'est pour ça qu'elle est coupée en deux.")

    d.tableau('Lecture', "Affiche du comptoir (suite)",
              ["Situation", "Ce qu'il faut faire"],
              [["Un arrêt du cours", "se déclare en personne, au comptoir"],
               ["Attestation de fréquentation", "à demander 3 jours avant votre départ"]],
              cle=1,
              note="Deux lignes qui annoncent le défi 3 : arrêter se dit en "
                   "personne, et le papier se demande avant.",
              notes="Ne pas développer ici : ces deux lignes seront le sujet entier du "
                    "bloc D. Les faire seulement remarquer.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'affiche.", [
        ("Le secrétariat est ouvert le samedi.", "faux — du lundi au vendredi"),
        ("Pour une absence prévue, on va au comptoir avant.", "vrai"),
        ("Pour une absence imprévue, on peut téléphoner.", "vrai"),
        ("Il faut téléphoner avant midi.", "faux — avant 9 h"),
        ("On peut annoncer un arrêt du cours par téléphone.", "faux — en personne"),
        ("L'attestation se demande trois jours avant le départ.", "vrai"),
    ], corrige=True,
       notes="Faire retrouver la ligne exacte de l'affiche pour chaque réponse. C'est "
             "la stratégie de lecture qu'on enseigne, pas la réponse.")

    d.regle("Prévue ou imprévue : deux chemins",
            "au comptoir avant  ·  au téléphone le matin même",
            precision="Une grippe qui commence un dimanche soir ne se prévoit "
                      "pas. C'est pour ça que l'affiche donne un numéro : "
                      "téléphoner tôt le matin vaut mieux que ne rien dire du "
                      "tout.",
            notes="Diapo à photographier. Donner le vrai numéro de votre centre et le "
                  "faire enregistrer dans les téléphones, séance tenante. Cinq minutes "
                  "qui servent toute la session.")

    d.pratique('Compréhension', "Ce que la secrétaire veut dire",
               "Associez chaque phrase à son sens.", [
        ("« Votre nom et votre groupe ? »", "on doit savoir qui vous êtes avant d'écrire"),
        ("« Toute la journée ou l'avant-midi ? »", "combien de temps dure l'absence"),
        ("« J'inscris l'absence au dossier. »", "c'est écrit, l'enseignante le verra"),
        ("« Absence prévenue. »", "vous êtes venu le dire avant"),
        ("« Demandez à une camarade. »", "quelqu'un de la classe vous dira ce qui a été fait"),
    ], corrige=True,
       notes="Reprend l'exercice 4 du module interactif. Faire jouer les cinq phrases "
             "avec l'intonation d'une vraie personne pressée : c'est ainsi qu'elles "
             "s'entendront.")

    d.cartes("Après une absence, deux gestes", "Que personne ne fait spontanément", [
        ("Demander à une camarade",
         "Ce qui a été fait, la page du cahier, le devoir. Trois minutes avant le cours "
         "suffisent, et personne ne le refuse."),
        ("Passer voir l'enseignante",
         "Elle dira ce qu'il faut reprendre. Elle a vu l'absence au dossier, mais elle "
         "ne sait pas si vous avez rattrapé."),
    ], notes="Faire nommer par chacun la personne de la classe à qui il demanderait. "
             "Ceux qui ne trouvent personne sont exactement ceux dont il faut "
             "s'occuper.")

    d.billet(
        "Notez le numéro du secrétariat dans votre téléphone.",
        exemples=[
            "Enregistrez-le sous « Centre — secrétariat ».",
            "Écrivez aussi le nom d'une camarade à qui demander.",
        ],
        notes="Fin du défi 1. Vérifier que le numéro est bien enregistré : un devoir "
              "qu'on ne vérifie pas n'est fait par personne.")

    return d.save(dossier)
