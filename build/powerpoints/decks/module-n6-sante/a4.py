# -*- coding: utf-8 -*-
"""A4 · Ce qu'on met dans son sac la veille
Bloc A « Je découvre » · couleur ambre · 75 min. Préparation et écriture.
Source : exercice `prPapiers` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='ambre',
        titre="Ce qu'on met dans son sac la veille",
        chapeau="Un rendez-vous en spécialité, c'est un long silence suivi "
                "d'un très court moment. Ce qui se joue en vingt minutes se "
                "prépare la veille, en dix.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc A. Elle est très concrète et elle produit "
                  "un objet réel : la feuille que chaque élève repartira avec. "
                  "Prévoir vingt minutes d'écriture individuelle à la fin.")

    d.objectifs([
        "nommer les sept choses à apporter à un rendez-vous ;",
        "distinguer ce que l'hôpital a déjà de ce qu'il faut apporter ;",
        "écrire la liste de ce qu'on prend, y compris sans ordonnance ;",
        "écrire trois questions la veille plutôt que dix dans l'auto.",
    ], notes="Les deux derniers objectifs sont de l'écriture réelle. Ce n'est pas un "
             "exercice : c'est la feuille que la personne apportera à son prochain "
             "rendez-vous.")

    d.declencheur(
        'Observation', "Qu'est-ce qui manquait, la dernière fois ?",
        pistes=[
            "Vous a-t-on déjà demandé un papier que vous n'aviez pas ?",
            "Avez-vous déjà oublié une question, et vous en êtes souvenu dehors ?",
            "Est-ce que quelqu'un vous a déjà accompagné ? Est-ce que ça a aidé ?",
        ],
        notes="Trois minutes. Le deuxième cas est presque universel et il détend le "
              "groupe : oublier ses questions n'est pas de la nervosité, c'est "
              "l'effet normal d'être assis devant quelqu'un.")

    d.tableau('Analyse', "Sept choses, sept usages",
              ['Ce qu\'on apporte', 'Ce que ça sert à faire'],
              [["La carte", "se faire inscrire avant même d'avoir dit un mot"],
               ["La convocation", "retrouver l'heure, l'étage et le nom de la personne"],
               ["La liste des produits", "répondre sans deviner à la première question"],
               ["Les papiers d'ailleurs", "apporter ce que l'hôpital n'a pas"],
               ["Les trois questions", "ne pas sortir avec ce qu'on voulait demander"]],
              cle=0,
              note="Et deux choses de plus : la liste de ses antécédents, et un crayon.",
              notes="Diapositive à photographier. La note du bas porte les deux "
                    "dernières : le tableau refuse sept rangées avec une note, et la "
                    "diapositive resterait lisible mais serrée.")

    d.regle("Ne triez pas vos papiers d'avance",
            "Apportez tout, et laissez trier la personne dont c'est le métier.",
            precision="Vous ne pouvez pas savoir ce qui servira. Le papier que vous "
                      "jugez inutile — un vieux résultat, une lettre d'un autre "
                      "pays — est souvent celui qui explique tout. Trier prend "
                      "trente secondes à la personne en face ; deviner lui prend un "
                      "autre rendez-vous.",
            notes="Diapositive à photographier. Plusieurs élèves trient par politesse, "
                  "pour ne pas déranger. Nommer cette intention avant de la corriger : "
                  "elle est généreuse, et elle coûte cher.")

    d.cartes('Méthode', "Cinq questions à se poser la veille", [
        ("Où, exactement ?", "Le pavillon, l'étage, la salle. Vingt minutes de marge la première fois."),
        ("Qui je vais voir ?", "Le nom de famille est écrit avant le prénom sur une convocation."),
        ("Qu'est-ce que je prends ?", "Tout, y compris ce qui s'achète sans ordonnance."),
        ("Qu'est-ce qui manque au dossier ?", "Ce qui a été fait ailleurs qu'à cet hôpital."),
        ("Qu'est-ce que je veux savoir ?", "Trois questions écrites, dans l'ordre d'importance."),
        ("Et le crayon ?", "Pour noter les dates au lieu d'essayer de les retenir."),
    ], cols=2,
       notes="Une carte à la fois, avec un exemple demandé au groupe entre chaque. "
             "La cinquième prendra le plus de temps, et c'est normal.")

    d.piege('Préparation',
            "je ne prends rien",
            "rien d'ordonnance, mais des vitamines tous les jours l'hiver",
            "« Rien » est presque toujours faux, et ce n'est pas un mensonge : "
            "on ne compte pas ce qui s'achète à l'épicerie. Or la question sert "
            "à savoir ce qui circule dans le corps, pas à vérifier une "
            "ordonnance. Tisanes, vitamines, produits rapportés d'un voyage : "
            "tout se note.",
            notes="C'est la correction la plus utile de la séance. La faire "
                  "reformuler par deux élèves avant de passer à l'écriture.")

    d.pratique('Écriture', "Votre liste, en vrai",
               "Écrivez sur une feuille que vous garderez.", [
        ("Ligne 1 : tout ce que vous prenez, ordonnance ou non.", ""),
        ("Ligne 2 : vos antécédents, un par ligne.", ""),
        ("Ligne 3 : vos trois questions, dans l'ordre d'importance.", ""),
    ],
       notes="Vingt minutes, en silence. Passer dans les rangées. Ne pas corriger la "
             "langue à ce moment-ci : la feuille est un objet personnel, pas un "
             "devoir. On la corrigera si l'élève le demande.")

    d.billet(
        "Quelle est votre première question, celle qui passe avant les autres ?",
        exemples=[
            "Une seule phrase, la vôtre.",
            "Elle peut commencer par « je voudrais savoir ».",
        ],
        notes="Deux minutes. Garder les billets : ils serviront à ouvrir le Défi 2, "
              "où l'élève devra poser ses propres questions à la spécialiste.")

    return d.save(dossier)
