# -*- coding: utf-8 -*-
"""A1 · Il faut le dire au secrétariat.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Il faut le dire au secrétariat',
        chapeau="Manquer un cours arrive à tout le monde. Ce qui change "
                "tout, c'est de le dire — au bon endroit, à la bonne "
                "personne, avant plutôt qu'après.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander au groupe qui est déjà allé au "
                  "secrétariat depuis son inscription, et pourquoi. Les réponses donnent "
                  "des exemples réels pour toute la semaine — et révèlent souvent que "
                  "plusieurs n'y sont jamais entrés.")

    d.objectifs([
        "nommer le secrétariat, le comptoir, le groupe et le dossier ;",
        "comprendre une conversation entre camarades de classe ;",
        "savoir à qui s'adresse une absence ;",
        "dire la différence entre prévenir et ne rien dire.",
    ])

    d.declencheur(
        'Observation', "Vous ne pouvez pas venir demain. Vous faites quoi ?",
        pistes=[
            "À qui le dites-vous : à l'enseignante, au secrétariat, à personne ?",
            "Quand : avant ou en revenant ?",
            "Est-ce qu'il faut un papier ?",
            "Qu'est-ce qui arrive si on ne dit rien ?",
        ],
        notes="Laisser répondre sans corriger. Les usages varient beaucoup d'un pays à "
              "l'autre : dans plusieurs systèmes, on ne prévient personne. Noter les "
              "réponses au tableau, on y reviendra à la fin de la séance.")

    d.dialogue('Dialogue · 1 de 3', "Je ne serai pas là jeudi", [
        ("NAWEL", "Tariq, je ne serai pas là jeudi. Ma fille a un rendez-vous à la clinique.", True),
        ("TARIQ", "Tu l'as dit à l'enseignante ?", True),
        ("NAWEL", "Non, pas encore. Je vais lui dire jeudi matin, en arrivant.", True),
        ("TARIQ", "Jeudi matin, tu ne seras pas là ! Il faut le dire avant.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Toute la logique du module est dans la quatrième réplique. La faire "
             "reformuler par un élève avant d'aller plus loin : pourquoi jeudi matin, "
             "c'est trop tard ?")

    d.dialogue('Dialogue · 2 de 3', "Le bureau en bas", [
        ("NAWEL", "Avant ? À qui ?", True),
        ("TARIQ", "Au secrétariat. C'est le bureau en bas, à côté de la porte d'entrée.", True),
        ("NAWEL", "Le grand comptoir avec la dame ?", True),
        ("TARIQ", "Oui. La secrétaire s'appelle madame Cloutier. Elle est très gentille.", True),
    ], notes="Remplacer « en bas, à côté de la porte d'entrée » par le vrai chemin dans "
             "votre centre, et le faire répéter. Si possible, y descendre en groupe à la "
             "fin de la séance : cinq minutes qui valent une heure d'explication.")

    d.dialogue('Dialogue · 3 de 3', "Et je dis quoi ?", [
        ("NAWEL", "Et je dis quoi ?", True),
        ("TARIQ", "Ton nom, ton prénom, ton groupe, et le jour où tu vas être absente.", True),
        ("NAWEL", "Mon groupe… je suis dans le groupe 12, l'avant-midi.", True),
        ("TARIQ", "Elle écrit ton absence dans ton dossier et elle prévient l'enseignante.", True),
    ], notes="« Ton nom, ton prénom, ton groupe » est la formule à mémoriser du module. "
             "La faire dire à voix haute par chaque élève, avec ses vraies données.")

    d.tableau('Analyse', "Les mots du centre",
              ["Le mot", "Ce que c'est"],
              [["le secrétariat", "le bureau où on donne et où on demande les papiers"],
               ["le comptoir", "le meuble haut derrière lequel on est reçu"],
               ["la secrétaire", "la personne qui écrit dans les dossiers"],
               ["le groupe", "le numéro de votre classe : 12, 14, 21…"],
               ["le dossier", "vos papiers au centre : absences, résultats"]],
              cle=1,
              note="Ces cinq mots reviennent dans les quatre séances du module.",
              notes="Diapo à photographier. Faire dire à chacun son propre numéro de "
                    "groupe : c'est le renseignement qu'ils oublieront au comptoir.")

    d.regle("Prévenir, c'est parler avant",
            "« Jeudi, je vais être absente. »",
            precision="Une absence annoncée d'avance est notée comme prévenue. "
                      "Une absence sans nouvelle reste inscrite, mais sans "
                      "raison. Ce n'est pas la même chose au dossier, et ce "
                      "n'est pas la même chose pour l'enseignante.",
            notes="Diapo à photographier. Ne pas dramatiser : il n'y a pas de punition. "
                  "Ce qui se joue, c'est la confiance et la trace écrite.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Nawel ne pourra pas venir au cours jeudi.", "vrai"),
        ("Tariq dit que c'est une bonne idée d'attendre jeudi.", "faux — il faut le dire avant"),
        ("Le secrétariat est en bas, à côté de la porte d'entrée.", "vrai"),
        ("Nawel est dans le groupe 12, l'avant-midi.", "vrai"),
        ("Une absence sans nouvelle est la même chose qu'une absence annoncée.", "faux"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Écrivez votre nom, votre prénom et votre groupe sur une ligne.",
        exemples=[
            "Comme vous le direz au comptoir : « Nawel Belkacem, groupe 12. »",
            "Apprenez-la par cœur : elle sert à chaque séance du module.",
        ],
        notes="Devoir de trente secondes, et pourtant le plus utile du bloc A. Vérifier "
              "à l'entrée de A2 que chacun sait dire sa ligne sans regarder.")

    return d.save(dossier)
