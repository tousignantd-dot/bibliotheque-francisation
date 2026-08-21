# -*- coding: utf-8 -*-
"""C4 · Qui prévenir, et comment l'écrire.
Bloc C « Défi 2 · La nouvelle adresse » · couleur ambre · 75 min.
Source : exercices `t2liste` et `t2courriel`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Qui prévenir, et comment l'écrire",
        chapeau="Ceux qui oublient la RAMQ s'en aperçoivent chez le médecin.",
        duree='75 minutes')

    d.titre(notes="Séance d'écriture. Elle produit un vrai courriel, réutilisable tel quel. "
                  "Reprendre en ouvrant la dernière réplique de Claudine, en C1.")

    d.objectifs([
        "nommer les huit organismes à prévenir d'un déménagement ;",
        "dire ce qui arrive quand on en oublie un ;",
        "écrire un courriel de changement d'adresse en cinq lignes ;",
        "employer une préposition de temps dans une démarche écrite.",
    ])

    d.tableau('La liste · 1 de 2', "Les services",
              ['Qui', "Si vous l'oubliez"],
              [["Hydro-Québec", "vous payez l'électricité de l'ancien locataire"],
               ["Postes Canada", "vos lettres restent à l'ancienne adresse"],
               ["Votre assureur", "vos affaires ne sont plus assurées où elles sont"],
               ["Votre banque", "vos relevés partent chez quelqu'un d'autre"]],
              cle=0,
              notes="Les quatre premiers se font dans la semaine du déménagement. "
                    "Hydro-Québec, avant même d'entrer.")

    d.tableau('La liste · 2 de 2', "Les organismes et l'entourage",
              ['Qui', "Si vous l'oubliez"],
              [["La RAMQ", "votre carte ne se rend pas ; vous le découvrez chez le médecin"],
               ["La SAAQ", "l'avis de renouvellement du permis n'arrive pas"],
               ["L'école", "l'autobus passe à l'ancienne adresse le matin de la rentrée"],
               ["Votre employeur", "le feuillet d'impôt de février va au mauvais endroit"]],
              cle=0,
              note="Faites-en une liste sur papier et cochez au fur et à mesure.",
              notes="Demander au groupe d'ajouter ce qui manque pour eux : garderie, "
                    "pharmacie, syndicat, organisme d'accueil.")

    d.regle("Un courriel de démarche tient en cinq lignes",
            "Qui vous êtes · l'ancienne adresse · la nouvelle · la date · une demande.",
            precision="Celui qui vous lit reçoit quarante courriels par jour. Le numéro de "
                      "dossier dans l'objet lui évite de chercher, et une question polie "
                      "à la fin obtient une réponse.",
            notes="Diapositive à photographier. Elle est le plan du courriel que les "
                  "élèves vont écrire dans dix minutes.")

    d.cartes("Les cinq morceaux", "Dans cet ordre, toujours", [
        ("L'objet",
         "Changement d'adresse — police 4471-882. Le numéro de dossier dès l'objet."),
        ("Qui vous êtes",
         "Nom complet et le numéro qui vous identifie chez eux. Sans lui, votre courriel attend."),
        ("Les deux adresses",
         "L'ancienne et la nouvelle, l'une après l'autre, même s'ils ont déjà la première."),
        ("La date",
         "À partir de quand la nouvelle s'applique. C'est ce qu'on oublie le plus."),
        ("La demande",
         "Pourriez-vous modifier mon dossier et me confirmer le changement ?"),
        ("La fin",
         "Merci de votre aide, votre nom, votre numéro de téléphone. Rien de plus."),
    ], cols=2,
       notes="Faire compter les morceaux sur les doigts. Cinq lignes, six morceaux : c'est "
             "court, et c'est le point.")

    d.pratique('Écriture', "Complétez le courriel d'Amadou",
               "L'enseignante lit la ligne ; chacun écrit le mot manquant.", [
        ("Objet : ___ d'adresse — police 4471-882", "Changement"),
        ("Je suis assuré chez vous ___ le numéro 4471-882.", "sous"),
        ("Mon ___ adresse était le 340, avenue Royale, à Beauport.", "ancienne"),
        ("Ma ___ adresse est le 1287, rue des Peupliers, appartement 4.", "nouvelle"),
        ("Le changement s'applique ___ premier juillet.", "à partir du"),
        ("Pourriez-vous modifier mon dossier et me ___ le changement ?", "confirmer"),
    ], corrige=True,
       notes="C'est l'exercice t2courriel. La cinquième ligne réemploie la préposition de "
             "C3 : le signaler.")

    d.piege("Écrire seulement la nouvelle adresse",
            "Bonjour, ma nouvelle adresse est le 1287, rue des Peupliers.",
            "Mon ancienne adresse était le 340, avenue Royale ; ma nouvelle est le 1287, "
            "rue des Peupliers.",
            "Sans l'ancienne adresse, l'employé ne peut pas retrouver votre dossier — "
            "surtout si votre nom s'écrit de plusieurs façons. Les deux adresses, "
            "toujours, et le numéro de dossier.",
            notes="Erreur très fréquente, et qui rallonge la démarche de deux semaines. "
                  "L'insister.")

    d.pratique('Production', "Écrivez le vôtre",
               "Choisissez un organisme de la liste et écrivez-lui, en cinq lignes.", [
        ("Objet", "Changement d'adresse — numéro de dossier"),
        ("Ligne 1", "Qui vous êtes et votre numéro"),
        ("Ligne 2", "L'ancienne adresse"),
        ("Ligne 3", "La nouvelle adresse"),
        ("Ligne 4", "La date à partir de laquelle elle s'applique"),
        ("Ligne 5", "Votre demande, sous forme de question polie"),
    ], corrige=False,
       notes="Vingt minutes d'écriture individuelle. Circuler et corriger les deux "
             "adresses et la date en priorité : le reste est du style.")

    d.billet(
        "Faites votre propre liste : qui devriez-vous prévenir si vous déménagiez demain ?",
        exemples=[
            "Reprenez les huit du tableau et ajoutez les vôtres.",
            "Notez à côté le numéro de dossier de chacun, si vous le connaissez.",
        ],
        notes="Le devoir a une valeur réelle hors du cours. Plusieurs élèves reviennent en "
              "disant qu'ils ont trouvé un organisme qu'ils avaient oublié depuis des "
              "années.")

    return d.save(dossier)
