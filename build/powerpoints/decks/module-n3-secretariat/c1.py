# -*- coding: utf-8 -*-
"""C1 · J'apporte mon billet.
Bloc C « Défi 2 · Le billet d'absence » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="J'apporte mon billet",
        chapeau="On ne peut pas toujours prévenir. Une grippe arrive un "
                "dimanche soir et dure trois jours : ce qui reste à faire, "
                "c'est de revenir avec le bon papier.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Demander qui a déjà reçu un billet d'une "
                  "clinique, et à quoi il ressemblait. Plusieurs en ont un dans leurs "
                  "papiers sans savoir qu'il servait à ça.")

    d.objectifs([
        "revenir au comptoir après une absence ;",
        "dire quelles journées ont été manquées ;",
        "présenter un billet et vérifier qu'il est complet ;",
        "demander à garder l'original.",
    ])

    d.declencheur(
        'Observation', "Vous avez manqué trois jours. Vous revenez. Et après ?",
        pistes=[
            "À qui parlez-vous en premier : l'enseignante ou le secrétariat ?",
            "Qu'est-ce qu'il faut dire exactement ?",
            "Est-ce qu'un papier est obligatoire ?",
            "Qu'est-ce qu'on fait du papier ensuite ?",
        ],
        notes="Recueillir avant le dialogue. La réponse « au secrétariat d'abord, à "
              "l'enseignante ensuite » n'est pas évidente : les deux sont utiles et "
              "l'ordre compte, parce que le dossier doit être à jour.")

    d.dialogue('Dialogue · 1 de 3', "Quelles journées avez-vous manquées ?", [
        ("NAWEL", "Bonjour, madame Cloutier. J'ai été absente la semaine passée.", True),
        ("GINETTE", "Bonjour. Votre nom et votre groupe, s'il vous plaît ?", True),
        ("NAWEL", "Nawel Belkacem, groupe 12.", True),
        ("GINETTE", "Quelles journées avez-vous manquées ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Le nom et le groupe reviennent en premier, comme au défi 1. C'est "
             "invariable : le faire remarquer plutôt que de le redire.")

    d.dialogue('Dialogue · 2 de 3', "Lundi, mardi et mercredi", [
        ("NAWEL", "Lundi, mardi et mercredi. J'avais la grippe.", True),
        ("GINETTE", "Trois journées. Vous avez un papier ?", True),
        ("NAWEL", "Oui, un billet de la clinique. Le voici.", True),
        ("GINETTE", "Voyons voir… Il y a la date, votre nom, la signature de la médecin. C'est complet.", True),
    ], notes="Trois choses font un billet complet : une date, un nom, une signature. "
             "Les faire compter sur les doigts par le groupe — c'est la liste de "
             "vérification du défi.")

    d.dialogue('Dialogue · 3 de 3', "Est-ce que je peux garder l'original ?", [
        ("NAWEL", "Est-ce que je peux garder l'original ?", True),
        ("GINETTE", "Bien sûr. Je fais une photocopie et je vous rends le papier.", True),
        ("NAWEL", "Merci. Et mon enseignante, est-ce qu'elle va le savoir ?", True),
        ("GINETTE", "Elle le verra dans le dossier. Passez la voir avant le cours.", True),
    ], notes="La question de l'original est celle que personne ne pense à poser. Un "
             "billet peut servir ailleurs — l'employeur, la garderie, un autre bureau. "
             "On ne donne jamais son seul papier.")

    d.tableau('Analyse', "Un billet complet, trois choses",
              ["Ce qu'on vérifie", "Pourquoi"],
              [["une date ou des dates", "sans elle, on ne sait pas ce qui est justifié"],
               ["votre nom", "le papier doit être le vôtre"],
               ["une signature", "quelqu'un répond du papier"]],
              cle=1,
              note="S'il manque quelque chose, la secrétaire le dit simplement et "
                   "demande de faire compléter le papier.",
              notes="Diapo à photographier. Regarder le billet AVANT de sortir de la "
                    "clinique : y revenir le lendemain coûte une demi-journée.")

    d.regle("On garde toujours l'original",
            "« Est-ce que je peux garder l'original ? »",
            precision="Le centre garde une photocopie ; le papier signé reste "
                      "à vous. Il peut servir à un employeur, à une garderie, "
                      "à un autre bureau. Une secrétaire ne garde jamais le "
                      "seul papier de quelqu'un.",
            notes="Diapo à photographier. Faire dire la question à voix haute par tout "
                  "le groupe : c'est une phrase que personne n'ose poser la première "
                  "fois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Nawel a manqué trois journées.", "vrai"),
        ("Elle avait un rendez-vous chez le dentiste.", "faux — elle avait la grippe"),
        ("Le billet porte une date, un nom et une signature.", "vrai"),
        ("La secrétaire garde l'original du billet.", "faux — elle fait une photocopie"),
        ("Nawel doit passer voir son enseignante avant le cours.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique. La dernière prépare le "
             "billet de sortie.")

    d.billet(
        "Racontez en trois phrases votre dernière absence.",
        exemples=[
            "Quelles journées, pourquoi, et si vous aviez un papier.",
            "Employez « la semaine passée » ou « du lundi au mercredi ».",
        ],
        notes="Devoir de préparation. Les phrases produites servent d'entrée à C2, où "
              "l'on travaille précisément ces marqueurs de temps.")

    return d.save(dossier)
