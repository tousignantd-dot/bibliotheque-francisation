# -*- coding: utf-8 -*-
"""E2 · La note remise au comptoir, et les seize mots
Bloc E « Je me lance » · couleur framboise · 75 min.
Production écrite, puis bilan du module.
Source du module : bloc « Je me lance » (la note remise au comptoir) et
« Je retiens des mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="La note remise au comptoir, et les seize mots",
        chapeau="Le message enregistré a prévenu ; la note, elle, justifie. "
                "C'est le papier que le secrétariat classe au dossier, et "
                "c'est lui qui fait passer une absence de « signalée » à "
                "« motivée ».",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Quarante-cinq minutes d'écriture, trente "
                  "de bilan. Rendre d'abord les billets annotés de D2 : chacun repart "
                  "d'un texte déjà relu une fois, et l'écriture démarre sans blocage.")

    d.objectifs([
        "écrire une note de six à neuf phrases, datée et signée ;",
        "employer le passé composé pour ce qui est arrivé, le futur pour la suite ;",
        "relire à voix haute avant de remettre ;",
        "réviser les seize mots et évaluer ce qu'on sait faire.",
    ], notes="Le troisième objectif est celui qu'on veut voir persister après le "
             "module. Le rappeler à voix haute avant l'écriture, pas après.")

    d.regle("Deux moitiés, pas une",
            "L'appel dit que vous avez prévenu. La note écrite dit pourquoi.",
            precision="C'est la règle de la première séance. Le module "
                      "entier tient entre les deux.",
            notes="Reprise de A1, à dessein. Demander au groupe qui s'en souvient. "
                  "C'est la seule phrase du module qu'on veut retrouver dans six mois.")

    d.tableau('Ce que la note doit contenir', "Sept points à cocher",
              ['La partie', 'Ce que vous écrivez'],
              [["Ligne du haut", "La ville et la date."],
               ["Destinataire", "Madame, Monsieur — ou le secrétariat."],
               ["Vous", "Nom complet et numéro de groupe."],
               ["Le jour", "La date exacte du retard, de l'absence ou de l'abandon."],
               ["Le motif", "Au passé composé, avec parce que ou à cause de."],
               ["La suite", "Au futur : je remettrai, je rattraperai, je serai."],
               ["Le bas", "La formule, votre nom, votre signature."]],
              cle=1,
              notes="Grille d'écriture, puis grille de relecture par le voisin. Sept "
                    "rangées sans note : c'est le maximum lisible de loin, et chaque "
                    "libellé de gauche tient sous vingt caractères.")

    d.cartes("Trois relectures", "Dans cet ordre, et pas un autre", [
        ("La première, à voix haute",
         "Elle attrape les accords qu'on n'entend pas en lisant des yeux."),
        ("La deuxième, sur les dates",
         "La date du haut, la date de l'absence, la date de la suite. Trois dates."),
        ("La troisième, sur la fin",
         "La formule, le nom écrit en toutes lettres, la signature à la main."),
        ("Et le geste final",
         "Une photo ou une photocopie, avant de descendre au comptoir."),
    ], notes="Faire faire les trois relectures pour vrai, chronomètre en main : deux "
             "minutes en tout. C'est court, et c'est ce qui manque à toutes les notes "
             "mal reçues.")

    d.pratique('Production écrite', "Votre note, en six à neuf phrases",
               "Reprenez votre billet de D2 et complétez-le.", [
        ("La ville et la date", "Laval, le (...) 2026."),
        ("Le destinataire", "Madame, Monsieur,"),
        ("Qui vous êtes", "Je suis (nom complet), du groupe (numéro), francisation."),
        ("Ce qui est arrivé", "J'ai été absent le (date) parce que (...)."),
        ("Ce que vous ferez", "Je rattraperai (...) et je vous remettrai (...)."),
        ("La fin", "Veuillez agréer mes salutations. (Nom, groupe, signature.)"),
    ], notes="Quarante-cinq minutes. Faire vérifier le texte dans le module, où "
             "l'assistant rend une rétroaction ; l'envoi à l'enseignant se fait ensuite, "
             "sur un geste de l'élève seulement.")

    d.piege("Signer d'un prénom",
            "Nourhane",
            "Nourhane Ouazzani, groupe 6, francisation de jour.",
            "Il y a plusieurs Nourhane dans un centre de mille élèves. Nom "
            "complet, groupe, et la signature en dessous : c'est ce qui fait "
            "arriver la note au bon dossier.",
            notes="Dernier piège du module, et le plus facile à corriger. Faire "
                  "vérifier la signature de chacun avant de ramasser : c'est un geste "
                  "de trente secondes pour tout le groupe.")

    d.vocabulaire("Bilan · 1", "Le téléphone et les motifs", [
        ("la boîte vocale", "Le service qui enregistre quand personne ne décroche."),
        ("le clavier", "Les touches numérotées du téléphone."),
        ("un poste", "Le numéro interne qui mène à une personne."),
        ("un retard", "Arriver après l'heure, mais venir quand même."),
        ("une absence", "Manquer un cours en entier."),
        ("un abandon", "Arrêter un cours avant la fin, et le dire officiellement."),
    ], notes="Six des seize mots, choisis parmi ceux qui reviendront le plus. Faire "
             "réviser les dix autres avec les cartes mémoire du module, qui donnent "
             "trois exercices sur la même liste.")

    d.vocabulaire("Bilan · 2", "Le message et le papier", [
        ("le signal sonore", "Le son qui dit que l'enregistrement commence."),
        ("les coordonnées", "Ce qui permet de vous joindre."),
        ("un empêchement", "Ce qui survient et vous empêche de venir."),
        ("une note", "Le court texte écrit et signé qu'on remet."),
        ("une signature", "Votre nom écrit de votre main."),
        ("une copie", "Le double qu'on garde quand on remet l'original."),
    ], notes="Faire dire chaque mot dans une phrase, sans article isolé. Les trois "
             "derniers sont ceux du bloc D et ils viennent d'être employés : ils "
             "sortent tout seuls.")

    d.tableau('Ce que je sais faire maintenant', "Bilan du module",
              ['La compétence', 'Où je l\'ai pratiquée'],
              [["Écouter un message", "Bloc C, trois messages, trois choses à noter."],
               ["Laisser un message", "Bloc B et séance E1, cinq morceaux."],
               ["Justifier par écrit", "Bloc D et séance E2, six lignes."],
               ["Nommer le motif", "Séance A4, trois mots, trois cases."],
               ["Téléphoner et répondre", "Séance E1, jeu de rôle au secrétariat."]],
              cle=1,
              notes="Cinq rangées sans note : le contrôle de densité refuse six rangées "
                    "avec note. Faire remplir l'autoévaluation du module en parallèle, "
                    "seize énoncés, trois choix chacun.")

    d.billet(
        "Écrivez la phrase du module que vous voulez garder.",
        exemples=[
            "Une seule phrase.",
            "Celle que vous direz vraiment, la prochaine fois.",
        ],
        notes="Ramasser et lire quelques billets à voix haute, anonymement. C'est la "
              "dernière minute du module : la phrase qui revient le plus est presque "
              "toujours celle de la première séance.")

    return d.save(dossier)
