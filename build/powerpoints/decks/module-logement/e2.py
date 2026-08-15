# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E · couleur foret (vocabulaire et bilan) · 60 min.
Source : les cartes mémoire du module, révision des savoirs, autoévaluation.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='foret',
        titre='Je retiens des mots',
        chapeau="Dernière séance du module. On rassemble le vocabulaire, on revoit les "
                "savoirs, et chacun fait le point sur ce qu'il est maintenant capable "
                "de faire.",
        duree='60 minutes')

    d.titre(notes="Séance de bilan. Ton différent des autres : on ne présente rien de "
                  "nouveau. Laisser beaucoup de place aux questions restées en suspens.")

    d.objectifs([
        "revoir les mots essentiels du module ;",
        "retrouver les savoirs travaillés et savoir où chacun sert ;",
        "évaluer honnêtement ce que je suis capable de faire ;",
        "savoir où retourner chercher ce qui n'est pas encore acquis.",
    ])

    d.vocabulaire('Vocabulaire · 1 de 3', "Le contrat et les gens", [
        ("un bail", "Le contrat de location signé entre le locataire et le propriétaire."),
        ("le loyer", "La somme versée chaque mois pour habiter un logement."),
        ("un locataire", "La personne qui loue un logement et qui y habite."),
        ("un propriétaire", "La personne à qui appartient le logement loué."),
        ("l'état des lieux", "La description du logement au début du bail."),
        ("résilier un bail", "Y mettre fin avant la date prévue."),
    ], notes="Cacher la colonne de droite et faire donner les définitions. Puis "
             "l'inverse.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Le logement", [
        ("chauffé et éclairé", "Dont le chauffage et l'électricité sont compris."),
        ("insonorisé", "Protégé contre le bruit de la rue ou des voisins."),
        ("lumineux", "Qui reçoit beaucoup de lumière du jour."),
        ("la buanderie", "Le local où se trouvent la laveuse et la sécheuse."),
        ("les électroménagers", "Les gros appareils : réfrigérateur, cuisinière, laveuse."),
        ("le rez-de-chaussée", "L'étage au niveau de la rue, sans escalier à monter."),
    ], notes="Faire refaire le calcul du « ½ » : un 4 ½ a combien de chambres ? C'est le "
             "savoir le plus propre au Québec.")

    d.vocabulaire('Vocabulaire · 3 de 3', "Le déménagement", [
        ("emménager", "S'installer dans un nouveau logement."),
        ("déménager", "Quitter un logement pour aller dans un autre."),
        ("un quartier", "Une partie d'une ville, avec ses commerces et ses services."),
        ("un triplex", "Un immeuble de trois logements superposés."),
        ("sous-louer", "Laisser quelqu'un d'autre habiter le logement à sa place."),
    ], notes="Faire produire une phrase avec chaque mot, sur une situation réelle ou "
             "prévue.")

    d.tableau('Révision · 1 de 2', "Les savoirs du module",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["Le ½ des annonces", "le chiffre compte les pièces fermées", "A2"],
               ["Le vrai coût", "additionner ce qui n'est pas inclus", "A2"],
               ["Avant de signer", "douze sujets, la moitié se demande", "A3"],
               ["La question de reprise", "le nom devant, le pronom après", "B2"],
               ["Reprendre un nom", "changer le déterminant, pas le nom", "B3"]],
              cle=0,
              notes="Faire retrouver la règle avant d'afficher la colonne du milieu. Ce "
                    "qui ne revient pas est ce qu'il faut retravailler.")

    d.tableau('Révision · 2 de 2', "Les savoirs du module, suite",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["La phrase emphatique", "ce qui fait l'action prend qui", "C2"],
               ["Le bail", "ce qui n'est pas écrit n'existe pas", "C4"],
               ["Besoin ou préférence", "peut-on vivre sans ?", "D1"],
               ["CD ou CI", "la préposition décide", "D2"]],
              cle=0, props=[0.3, 0.55, 0.15],
              note="Neuf savoirs pour un module. Chacun renvoie à une séance : c'est là "
                   "qu'il faut retourner.",
              notes="Insister sur la dernière colonne. Le module reste ouvert dans le "
                    "portail : chacun peut y revenir seul.")

    d.cartes('Les quatre gestes du module', "Ce qu'on sait faire maintenant", [
        ("Lire une annonce",
         "Le nombre de pièces, ce qui est inclus, ce qu'il faut apporter, et le vrai "
         "coût mensuel."),
        ("Préparer et mener une visite",
         "Six questions écrites d'avance, avec une phrase de contexte devant les plus "
         "importantes."),
        ("Peser ce qui plaît et ce qui inquiète",
         "Trois choses qui plaisent, deux qui inquiètent, et une solution pour "
         "chacune."),
        ("Choisir et écrire",
         "Deux vrais besoins, une chose qui décide, et un message au propriétaire en "
         "trois paragraphes."),
    ], notes="Faire dire à chacun lequel des quatre lui paraît le plus solide, et lequel "
             "le moins. Personne ne doit répondre « tous ».")

    d.pratique('Bilan · 1 de 2', "Le vocabulaire, sans regarder",
               "Donnez le mot qui correspond à la définition.", [
        ("Le contrat de location.", "un bail"),
        ("Dont le chauffage et l'électricité sont compris.", "chauffé et éclairé"),
        ("Protégé contre le bruit.", "insonorisé"),
        ("Le local où se trouvent la laveuse et la sécheuse.", "la buanderie"),
        ("S'installer dans un nouveau logement.", "emménager"),
        ("Un immeuble de trois logements superposés.", "un triplex"),
    ], corrige=True,
       notes="Exercice individuel, cahier fermé, cinq minutes. Corriger ensemble sans "
             "compter les points.")

    d.pratique('Bilan · 2 de 2', "Autoévaluation",
               "Pour chaque énoncé : je sais faire, presque, ou pas encore.", [
        ("Je comprends une annonce de logement.", "séances A2, A4"),
        ("Je sais quoi vérifier avant de signer un bail.", "séances A3, C4"),
        ("Je peux poser six questions pendant une visite.", "séances B1, B4"),
        ("Je peux dire ce qui me plaît et ce qui m'inquiète.", "séances C2, C3"),
        ("Je distingue un besoin d'une préférence.", "séance D1"),
        ("Je peux écrire au propriétaire pour demander une visite.", "séance E1"),
    ], corrige=True,
       notes="La colonne de droite n'est pas une correction : c'est l'adresse où "
             "retourner. Le dire clairement au groupe.")

    d.billet(
        "Nommez une chose que vous vérifierez la prochaine fois que vous chercherez un logement.",
        exemples=[
            "Une seule, celle à laquelle vous n'auriez pas pensé avant ce module.",
            "Écrivez-la comme vous la demanderiez à une propriétaire.",
        ],
        notes="Fin du module. Ces billets disent ce qui est vraiment passé de la classe "
              "à la vie — c'est le seul bilan qui compte.")

    return d.save(dossier)
