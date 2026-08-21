# -*- coding: utf-8 -*-
"""E2 · Le courriel au propriétaire, et le bilan.
Bloc E « Je me lance » · couleur framboise · 75 min. Dernière séance.
Source : production écrite de `custom.js`, `FC_CARDS`, autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Le courriel au propriétaire",
        chapeau="Trois jours après l'emménagement : confirmer l'entrée, "
                "signaler deux réparations, demander une date.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Production écrite d'abord, révision du "
                  "vocabulaire et autoévaluation ensuite.")

    d.objectifs([
        "écrire un courriel de démarche complet ;",
        "nommer et situer deux défauts relevés à l'état des lieux ;",
        "employer une préposition de temps à l'écrit ;",
        "faire le bilan de ce qu'on sait maintenant faire.",
    ])

    d.regle("Ce courriel réunit tout le module",
            "L'état des lieux de A4, les prépositions de C3, la forme du courriel de C4.",
            precision="Six à dix phrases. Un objet qui dit tout, votre nom et le numéro du "
                      "logement, deux défauts nommés et situés, une date, une demande "
                      "polie, une formule de fin.",
            notes="Diapositive à photographier. Les élèves y reviennent pendant qu'ils "
                  "écrivent.")

    d.tableau('Votre courriel · 1 de 2', "Qui, quoi, quand",
              ['Exigence', 'Exemple'],
              [["Nom, logement, date d'entrée",
                "Je suis Amadou Sow, le nouveau locataire du logement 4."],
               ["Deux défauts nommés et situés",
                "Une égratignure de 40 cm près de la fenêtre du salon."],
               ["Une préposition de temps",
                "J'ai emménagé à partir du premier juillet."]],
              cle=0,
              note="Nommez et situez, ne racontez pas.",
              notes="Ces exigences sont celles affichées dans l'activité interactive. Les "
                    "élèves les retrouveront à l'écran.")

    d.tableau('Votre courriel · 2 de 2', "La demande et la fin",
              ['Exigence', 'Exemple'],
              [["Une demande sous forme de question",
                "Pourriez-vous me dire quand la réparation pourrait se faire ?"],
               ["Une formule de fin et un numéro",
                "Merci de votre aide. Amadou Sow, 418 555-0142."]],
              cle=0,
              notes="Sans question, pas de réponse : c'est la règle du courriel de "
                    "démarche, déjà vue en C4.")

    d.piege("Écrire une lettre de plainte au lieu d'un courriel de démarche",
            "Je trouve inacceptable que le logement soit dans cet état.",
            "J'ai relevé deux choses à réparer, et je vous les signale.",
            "Un propriétaire qui reçoit un reproche se défend ; un propriétaire qui reçoit "
            "une liste répare. Le ton neutre n'est pas de la faiblesse : c'est ce qui "
            "obtient la date.",
            notes="Nuance importante pour des élèves qui ont parfois été mal reçus "
                  "ailleurs. Dire que la fermeté vient de la précision, pas du ton.")

    d.pratique('Écriture', "Écrivez votre courriel",
               "Trente minutes. Six à dix phrases, dans le cadre de l'activité.", [
        ("Objet", "Logement 4 — état des lieux et deux réparations"),
        ("Ouverture", "Qui vous êtes, votre logement, la date de votre entrée"),
        ("Défaut 1", "Nommé, situé, mesuré"),
        ("Défaut 2", "Nommé, situé, mesuré"),
        ("La demande", "Une question polie, qui appelle une date"),
        ("La fin", "Merci, votre nom, votre numéro"),
    ], corrige=False,
       notes="Circuler. Corriger en priorité : l'endroit du défaut, la préposition de "
             "temps, et la présence d'une vraie question. Le reste est du style.")

    d.vocabulaire('Révision', "Les mots à ne pas perdre", [
        ("l'état des lieux", "La liste écrite de ce qui est déjà abîmé le jour de l'entrée."),
        ("le temps de déplacement", "Le temps du camion pour venir et retourner, qu'on paie aussi."),
        ("un dépôt", "L'argent versé d'avance pour garder une date."),
        ("un relevé de compteur", "Le nombre lu sur l'appareil qui mesure l'électricité."),
        ("le réacheminement du courrier", "Le service qui fait suivre vos lettres."),
        ("le bac brun", "Le bac des restes de table et des pelures."),
        ("le déneigement", "Le travail qui consiste à enlever la neige des rues."),
    ], notes="Sept mots sur seize : ceux qui ne s'apprennent nulle part ailleurs. Les faire "
             "employer une dernière fois dans une phrase personnelle.")

    d.cartes("Ce que vous savez faire maintenant", "Quatre choses de plus qu'il y a un mois", [
        ("Réserver un camion",
         "Donner votre situation, aller chercher le vrai prix, verser un dépôt."),
        ("Diriger une journée de déménagement",
         "Dire où va chaque chose en trois mots, à l'affirmative et à la négative."),
        ("Changer votre adresse partout",
         "Ouvrir un compte, fermer l'ancien, prévenir huit organismes, écrire le courriel."),
        ("Parler à vos voisins",
         "Vous excuser en racontant, demander les usages, répondre à une invitation."),
    ], notes="Faire l'autoévaluation du module tout de suite après, aux postes. Les douze "
             "énoncés reprennent ces quatre blocs.")

    d.billet(
        "Une chose que vous ferez autrement à votre prochain déménagement.",
        exemples=[
            "Un appel à faire plus tôt, un papier à écrire, une question à poser.",
            "Écrivez-la et gardez-la : c'est ce module en une phrase.",
        ],
        notes="Dernier billet du module. Les lire à voix haute, sans nom, à la séance "
              "suivante : c'est la meilleure synthèse que le groupe puisse produire.")

    return d.save(dossier)
