# -*- coding: utf-8 -*-
"""E2 · La lettre, et le bilan
Bloc E « Je me lance » · couleur framboise · production écrite · 75 min.
Source : section `appli` (production écrite) et « Je retiens des mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="La lettre, et le bilan",
        chapeau="Une lettre en colère se répond en une ligne. Une lettre qui "
                "cite l'annonce, concède un point et demande une chose "
                "précise se lit jusqu'au bout.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. Redistribuer les phrases de concession "
                  "écrites en C3 et les calculs de C4 : la lettre s'écrit avec les "
                  "deux sous les yeux.")

    d.objectifs([
        "écrire une lettre de réclamation en trois paragraphes ;",
        "citer l'annonce exactement, entre guillemets ;",
        "concéder un point sans renoncer à sa demande ;",
        "faire le bilan de ce qu'on sait maintenant repérer.",
    ], notes="Le troisième objectif est ce qui distingue une lettre de niveau 7 d'une "
             "lettre de niveau 5 : on ne se contente plus d'exposer, on argumente.")

    d.declencheur(
        'Préparation', "Que demandez-vous, et à qui ?",
        pistes=[
            "L'annulation, un remboursement, une correction de l'annonce ?",
            "Est-ce que votre demande est réaliste ?",
            "Quel délai accordez-vous pour la réponse ?",
            "Qu'est-ce que vous ferez si personne ne répond ?",
        ],
        notes="La dernière question amène la suite : la porte de l'organisme, vue en "
              "D1. Une lettre datée est la meilleure pièce du dossier suivant.")

    d.tableau('Analyse', "Trois paragraphes, trois travaux",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [["Les faits", "la date, le montant, ce que vous avez signé"],
               ["L'écart", "la phrase citée, et ce qui n'était pas dit"],
               ["La demande", "ce que vous voulez, et sous quel délai"]],
              cle=0,
              note="Dix à quatorze phrases en tout. Une lettre longue se lit en diagonale.",
              notes="Diapositive à photographier. La structure vaut pour toute lettre "
                    "de réclamation, quel que soit l'objet.")

    d.cartes('Analyse', "Huit exigences, tirées du module", [
        ("La date et le montant", "signé le 2 février, prélevé 189 $"),
        ("La citation exacte", "« neuf quatre-vingt-dix-neuf par semaine »"),
        ("Une concession", "bien que le tarif soit exact…"),
        ("Une restriction", "l'annonce ne donnait que le prix par semaine"),
        ("Deux conditionnels", "je souhaiterais, pourriez-vous"),
        ("Une reformulation", "autrement dit, en somme"),
        ("Une demande précise", "ce que vous voulez, exactement"),
        ("Un délai", "à la fin, en une phrase"),
    ], cols=1,
       notes="Les huit exigences sont celles du module. Les faire cocher une à une "
             "avant l'envoi : c'est la grille de correction.")

    d.piege('Écrit',
            "« Je trouve ça inacceptable et je veux mon argent. »",
            "« Je souhaiterais obtenir l'annulation sans frais, avant le 15 mars. »",
            "La première dit un sentiment ; la seconde dit une demande, une "
            "condition et une date. Un service à la clientèle ne peut rien "
            "faire d'un sentiment, et peut agir sur une demande. Ce n'est pas "
            "une question de politesse : c'est une question d'exécutabilité.",
            notes="Point de ton. Beaucoup d'élèves croient qu'une lettre ferme doit "
                  "être fâchée. C'est le contraire : la fermeté tient à la précision.")

    d.pratique('Production écrite', "Votre lettre",
               "Dix à quatorze phrases, en trois paragraphes.", [
        ("Paragraphe 1", "les faits, les dates, les montants"),
        ("Paragraphe 2", "la citation, la concession, ce qui n'était pas dit"),
        ("Paragraphe 3", "la demande, le délai, la formule de courtoisie"),
        ("Avant d'envoyer", "cochez les huit exigences, une par une"),
    ], corrige=False,
       notes="Le module corrige la lettre par l'assistant et permet de la déposer. En "
             "classe, faire relire par un pair avec la grille des huit exigences "
             "avant la correction automatique.")

    d.tableau('Bilan', "Ce que vous savez maintenant repérer",
              ['Le procédé', 'Le signe qui le trahit'],
              [["Une promesse vide", "le conditionnel : pourrait, pourraient"],
               ["Une comparaison sans terme", "un « plus » sans « que »"],
               ["Un prix rapetissé", "l'unité de temps la plus petite possible"],
               ["Une urgence fabriquée", "il ne reste que…"],
               ["Un auteur effacé", "une phrase passive sans « par »"],
               ["Une annonce déguisée", "aucune mention, et un code de réduction"]],
              cle=0,
              notes="Diapositive à photographier, et dernière du module. C'est la "
                    "grille que l'élève emporte : six lignes, et elles suffisent.")

    d.billet(
        "Qu'est-ce que vous regarderez autrement, la prochaine fois ?",
        exemples=[
            "Une chose, en une phrase.",
            "Nommez le procédé, pas seulement l'annonce.",
        ],
        notes="Billet de sortie du module. Les réponses valent d'être lues à voix "
              "haute à la fin : elles disent ce que seize séances ont réellement "
              "déposé.")

    return d.save(dossier)
