# -*- coding: utf-8 -*-
"""A2 · 911, 811, clinique ou pharmacie ?
Bloc A « Je découvre » · couleur acier (compréhension orale) · 60 min.
Source du module : exercice `pr1`, cartes mémoire « Info-Santé », « une urgence ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='acier',
        titre='911, 811, clinique ou pharmacie ?',
        chapeau="Cinq portes d'entrée dans le système de santé québécois. Frapper à la "
                "bonne fait gagner des heures — parfois davantage.",
        duree='60 minutes')

    d.titre(notes="Reprendre les réponses notées au tableau en A1 : « qui appelle-t-on "
                  "en premier ? ». Cette séance y répond, et l'écart entre les deux est "
                  "le vrai contenu de la journée.")

    d.objectifs([
        "nommer les cinq ressources de santé et ce qu'elles font ;",
        "choisir la bonne ressource selon la situation ;",
        "reconnaître ce qui est une urgence et ce qui n'en est pas ;",
        "savoir qu'Info-Santé répond jour et nuit, gratuitement.",
    ])

    d.declencheur(
        'Question d\'ouverture', "Votre enfant a 39 de fièvre à deux heures du matin. Vous appelez qui ?",
        pistes=[
            "Est-ce que c'est une urgence ?",
            "Est-ce qu'il existe un service la nuit, autre que l'urgence ?",
            "Combien de temps attend-on à l'urgence pour une fièvre ?",
            "Que se passe-t-il si on ne sait pas quoi faire ?",
        ],
        notes="Laisser le désaccord s'installer, ne pas trancher. La bonne réponse est "
              "811 : une infirmière répond la nuit et dit s'il faut se déplacer. "
              "Beaucoup d'élèves ne connaissent pas ce service.")

    d.tableau('Analyse', "Les cinq portes d'entrée",
              ['La ressource', 'Quand on s\'en sert'],
              [["le 911", "une urgence grave : accident, difficulté à respirer, "
                          "perte de conscience"],
               ["Info-Santé (811)", "une question de santé, jour et nuit — une "
                                    "infirmière répond et conseille"],
               ["la clinique", "un rendez-vous avec son médecin, pour un problème "
                               "qui dure"],
               ["la clinique sans rendez-vous", "voir un médecin vite, sans avoir "
                                                "de rendez-vous"],
               ["la pharmacie", "acheter un médicament, poser une question sur un "
                                "traitement"]],
              cle=0,
              note="Les cinq sont gratuites ou couvertes, sauf les médicaments.",
              notes="Insister sur 811 : c'est le service le moins connu et le plus utile. "
                    "Il évite un déplacement inutile, et il oriente vers la bonne porte.")

    d.regle('La règle du choix',
            "Est-ce que ça peut attendre demain matin ?",
            precision="Si oui : la clinique ou la pharmacie. Si non, mais ce n'est pas "
                      "grave : 811 ou le sans rendez-vous. Si c'est grave : le 911.",
            notes="Une seule question à se poser, et elle sépare les cinq ressources en "
                  "trois groupes. C'est la diapositive à photographier.")

    d.pratique('Pratique · 1 de 3', "Où s'adresser ?",
               "Associez chaque situation à la bonne ressource.", [
        ("Une urgence grave (un accident).", "le 911"),
        ("Une question de santé, jour et nuit.", "Info-Santé (811)"),
        ("Acheter un médicament.", "la pharmacie"),
        ("Un rendez-vous avec son médecin.", "la clinique"),
        ("Voir un médecin vite, sans rendez-vous.", "la clinique sans rendez-vous"),
    ], corrige=True,
       notes="C'est l'exercice 1 du module. Le faire d'abord à l'oral, en groupe, avant "
             "de l'ouvrir dans l'activité interactive.")

    d.pratique('Pratique · 2 de 3', "Et dans ces cas-là ?",
               "Six situations qui ne sont pas dans le module. Discutez à deux.", [
        ("Vous toussez depuis trois jours, sans fièvre.",
         "la pharmacie d'abord, ou 811 si ça inquiète"),
        ("Votre voisin ne répond plus et respire mal.", "le 911, tout de suite"),
        ("Vous avez besoin d'un billet du médecin pour votre employeur.",
         "la clinique, avec rendez-vous"),
        ("Vous ne savez pas si votre médicament se prend avec du lait.",
         "la pharmacie — c'est gratuit et sans rendez-vous"),
        ("Vous vous êtes coupé le doigt, ça saigne mais peu.",
         "811 pour savoir s'il faut des points"),
        ("Votre fille a la même fièvre depuis quatre jours.",
         "la clinique ou le sans rendez-vous"),
    ], corrige=True,
       notes="La quatrième surprend toujours : on peut poser une question au pharmacien "
             "sans rien acheter et sans rendez-vous. Le dire explicitement.")

    d.piege("Le piège de l'urgence",
            "J'ai mal à la tête depuis deux semaines, je vais à l'urgence.",
            "J'ai mal à la tête depuis deux semaines, j'appelle la clinique.",
            "L'urgence est faite pour ce qui met la vie en danger maintenant. Un problème "
            "qui dure depuis deux semaines y sera classé en dernier : l'attente peut "
            "dépasser huit heures, et le médecin de la clinique aurait votre dossier.",
            notes="Point sensible : dans plusieurs pays, l'hôpital est la porte normale. "
                  "Dire que ce n'est pas un jugement, c'est une organisation différente.")

    d.pratique('Pratique · 3 de 3', "Votre carnet de numéros",
               "Écrivez les coordonnées de vos propres ressources.", [
        ("Ma clinique", "nom, adresse, numéro de téléphone"),
        ("Le sans rendez-vous le plus proche", "nom et heures d'ouverture"),
        ("Ma pharmacie", "nom et heures — plusieurs ouvrent le soir"),
        ("Info-Santé", "811, jour et nuit, gratuit"),
    ], corrige=False,
       notes="Vingt minutes, avec les téléphones. Faire chercher les vraies adresses du "
             "quartier. C'est la partie de la séance qui sert le plus vite.")

    d.billet(
        "Écrivez une situation vécue et la ressource que vous choisiriez aujourd'hui.",
        exemples=[
            "Une seule phrase pour la situation, un mot pour la ressource.",
            "Ce peut être une situation passée, avant de connaître les cinq portes.",
        ],
        notes="Ramasser et lire : les situations réelles du groupe alimentent la "
              "pratique 2 des prochaines cohortes.")

    return d.save(dossier)
