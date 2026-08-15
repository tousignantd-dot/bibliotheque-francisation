# -*- coding: utf-8 -*-
"""E1 · À toi : le téléphone et le courriel.
Bloc E · couleur teal (je me lance) · 90 min.
Source : dialogue `appli`, exercices `aQui` et `aComp`, jeu de rôle IA du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : le téléphone et le courriel',
        chapeau="Un dernier dialogue à analyser, puis c'est à vous : vous expliquez votre "
                "problème à l'oral, et vous écrivez le courriel qui garde une trace de "
                "votre demande.",
        duree='90 minutes')

    d.titre(notes="Séance de production. Prévoir la salle en binômes dès le départ. "
                  "Le module en ligne contient un jeu de rôle avec correction par IA : "
                  "le lancer si les postes sont disponibles.")

    d.objectifs([
        "mener au téléphone une conversation complète avec ma propriétaire ;",
        "poser les questions qui font avancer la réparation ;",
        "écrire un courriel de suivi qui garde une trace de ma demande ;",
        "réemployer tout ce que le module a installé, en situation.",
    ])

    d.dialogue('Dialogue · 1 de 3', "Une tache au plafond", [
        ("MME RIOUX", "Bonjour Oksana, j'ai bien reçu votre photo. Ça fait longtemps que la tache est là ?", False),
        ("OKSANA", "Ça fait deux semaines. Elle a doublé de grandeur depuis la pluie de dimanche.", True),
        ("MME RIOUX", "Je vais aller la voir moi-même demain avant-midi. Est-ce que dix heures vous convient ?", False),
        ("OKSANA", "Oui, parfait. Je commence à treize heures, je serai là.", True),
    ], consigne="Écoutez d'abord, diapo masquée. Comptez les structures du module que vous reconnaissez.",
       notes="Deux structures des séances précédentes : « ça fait deux semaines » (B3) et "
             "« depuis la pluie de dimanche » (B3). Faire trouver au groupe.")

    d.dialogue('Dialogue · 2 de 3', "La propriétaire cherche la cause", [
        ("MME RIOUX", "Est-ce qu'il y a de l'humidité ailleurs dans le logement ?", True),
        ("OKSANA", "Dans la salle de bain, oui. Le miroir reste embué très longtemps après la douche.", True),
        ("MME RIOUX", "Est-ce que vous avez un ventilateur dans cette pièce-là ?", False),
        ("OKSANA", "Non, il n'y en a pas. J'ouvre la fenêtre, mais en hiver, c'est difficile.", False),
    ], notes="Moment important : la propriétaire cherche la cause, pas seulement le "
             "symptôme. Oksana répond précisément et signale une contrainte réelle "
             "— l'hiver. C'est cette précision qui fera installer le ventilateur.")

    d.dialogue('Dialogue · 3 de 3', "Deux réparations au lieu d'une", [
        ("MME RIOUX", "Alors je vais faire installer un ventilateur en même temps que la réparation du plafond. C'est important : sans ventilation, la moisissure revient toujours.", True),
        ("OKSANA", "Merci beaucoup. Ça m'inquiétait pour la santé de ma fille.", True),
    ], notes="« Faire installer » — séance C3. Et le résultat : deux réparations obtenues "
             "au lieu d'une, parce qu'Oksana a répondu aux questions au lieu de se "
             "contenter de signaler.")

    d.pratique('Pratique', 'Qui parle ?',
               "La locataire ou la propriétaire ?", [
        ("Ça fait longtemps que la tache est là ?", "PROPRIÉTAIRE"),
        ("Elle a doublé de grandeur depuis la pluie de dimanche.", "LOCATAIRE"),
        ("Je vais aller la voir moi-même demain avant-midi.", "PROPRIÉTAIRE"),
        ("Je commence à treize heures, je serai là.", "LOCATAIRE"),
    ], corrige=True, cols=2)

    d.pratique('Pratique', 'Suite',
               "Même consigne.", [
        ("Est-ce qu'il y a de l'humidité ailleurs dans le logement ?", "PROPRIÉTAIRE"),
        ("Le miroir reste embué très longtemps après la douche.", "LOCATAIRE"),
        ("Je vais faire installer un ventilateur en même temps.", "PROPRIÉTAIRE"),
        ("Ça m'inquiétait pour la santé de ma fille.", "LOCATAIRE"),
    ], corrige=True, cols=2,
       notes="Faire remarquer la répartition : la propriétaire pose les questions, la "
             "locataire donne les détails. C'est exactement la répartition du jeu de rôle "
             "qui suit.")

    d.pratique('Pratique', 'Le mot juste',
               "Complétez chaque phrase avec le mot qui convient.", [
        ("Il y a une ___ d'eau sous l'évier : le tuyau goutte.", "fuite"),
        ("Chez moi, j'ai un ___ d'eau : le plancher est trempé.", "dégât"),
        ("Nous avons une ___ de fourmis dans la cuisine.", "invasion"),
        ("Le climatiseur ne fonctionne plus : il est ___.", "défectueux"),
        ("La vitre de la fenêtre est ___ depuis l'orage.", "brisée"),
        ("L'eau de pluie entre par le toit : c'est une ___.", "infiltration"),
    ], corrige=True, cols=2,
       notes="Dernière révision du vocabulaire avant la production. Si le groupe hésite, "
             "renvoyer aux cartes mémoire du module en ligne.")

    d.cartes('Le jeu de rôle', "Comment ça se passe", [
        ("En binômes",
         "Une personne joue la locataire, l'autre la propriétaire. On échange les rôles "
         "après cinq minutes. Chacun doit avoir joué les deux."),
        ("Votre situation",
         "Utilisez le problème que vous avez décrit à la séance A1 et complété aux séances "
         "C1 et D1. Vous connaissez déjà votre sujet — concentrez-vous sur la langue."),
        ("Si la personne propriétaire",
         "Posez des questions : depuis quand ? il fait combien ? avez-vous vérifié ? "
         "y a-t-il de l'humidité ailleurs ? Proposez une date et une solution temporaire."),
        ("Dans le module en ligne",
         "Un jeu de rôle avec réponse automatique est disponible : deux scénarios, trois "
         "cas, et vous pouvez jouer l'un ou l'autre des deux rôles."),
    ], notes="Circuler pendant l'exercice, noter les erreurs récurrentes sans interrompre. "
             "Faire la mise en commun des erreurs à la fin, jamais pendant.")

    d.tableau('Le jeu de rôle', "Ce que doit contenir votre appel",
              ['Moment', 'Ce que vous dites'],
              [["Se présenter", "votre nom et votre numéro de logement"],
               ["Nommer le problème", "l'appareil, la pièce, et depuis quand"],
               ["Donner un chiffre", "des degrés, une durée, une grandeur"],
               ["Dire ce que vous avez vérifié", "le panneau électrique, le thermostat"],
               ["Demander une solution temporaire", "en attendant la réparation"]],
              cle=1,
              note="Cinq moments, dans cet ordre.",
              notes="Laisser cette diapo projetée pendant les vingt minutes de jeu de rôle. "
                    "C'est un support, pas une évaluation.")

    d.tableau('Le courriel', "Ce que doit contenir votre message",
              ['Élément', 'Exemple'],
              [["La suite de l'appel", "faire suite à notre conversation du 4 novembre"],
               ["Le fait et la durée", "le calorifère ne chauffe plus depuis le 4 novembre"],
               ["L'effet sur vous", "il fait quatorze degrés chez moi"],
               ["La demande", "pourriez-vous faire venir un électricien ?"],
               ["La confirmation", "merci de me confirmer la réception de ce message"]],
              cle=1,
              note="Trois à cinq lignes suffisent : la date et la demande font tout.",
              notes="Production écrite individuelle, trente minutes. Ramasser les copies : "
                    "c'est la production évaluable du module.")

    d.regle('Avant de remettre votre courriel',
            "Relisez-le en cherchant une seule chose : est-ce qu'on sait clairement ce que vous demandez ?",
            precision="Si la réponse est non, ajoutez une phrase avec un verbe d'action et, "
                      "si possible, un délai. C'est la seule vérification qui compte "
                      "vraiment : tout le reste peut être imparfait, le message passera "
                      "quand même.",
            notes="Faire faire la relecture en binômes : chacun lit le courriel de l'autre "
                  "et répond à cette seule question.")

    d.billet(
        "En une phrase : qu'est-ce que vous saurez faire maintenant que vous ne saviez pas faire avant ce module ?",
        exemples=[
            "Pas de bonne réponse. C'est votre réponse qui compte.",
        ],
        notes="Billet de nature différente : il prépare l'autoévaluation de la séance E2. "
              "Le lire avant le dernier cours.")

    return d.save(dossier)
