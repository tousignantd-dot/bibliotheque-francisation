# -*- coding: utf-8 -*-
"""C4 · Ce que la loi dit vraiment
Bloc C « Défi 2 · Le poste 4 » · couleur acier · 75 min.
Source du module : exercice `t2cnesst` (type texte), mini-leçon du même nom.

Les faits de cette séance sont vérifiés auprès de la CNESST le 22 août 2026 —
mécanismes de prévention et de participation en établissement, droit de refus
des articles 12 et 13 de la Loi sur la santé et la sécurité du travail. Ils ne
s'inventent pas. Meubles Rive-du-Nord, les personnes et les chiffres, oui.
"""
import pathlib

from theme import Deck

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-emploi' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre="Ce que la loi dit vraiment",
        chapeau="Deux sortes de textes vous concernent au travail : les "
                "politiques de l'employeur, qu'il écrit lui-même, et la loi, "
                "qui est la même partout au Québec et qu'aucun employeur ne "
                "peut réduire.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du bloc C, et la plus utile hors de la classe. "
                  "Tout ce qui est présenté ici se vérifie sur cnesst.gouv.qc.ca : le "
                  "dire au groupe et donner l'adresse. Un élève qui repart avec une "
                  "règle fausse est moins bien loti qu'un élève qui n'en a aucune.")

    d.objectifs([
        "distinguer une politique d'employeur d'une loi ;",
        "savoir ce qu'un établissement de vingt travailleurs ou plus doit avoir ;",
        "savoir qui élit le représentant en santé et en sécurité ;",
        "dire dans quels cas le droit de refus s'applique, et dans quels cas non.",
    ], notes="Le quatrième objectif se travaille dans les deux sens : ce que le droit "
             "de refus permet ET ce qu'il ne permet pas. Un élève qui n'apprend que la "
             "première moitié se met en difficulté.")

    d.declencheur(
        'Discussion', "Qui décide de ce qui est dangereux ?",
        image=IMG + 'transpalette.jpg',
        pistes=[
            "Vous trouvez qu'une tâche est dangereuse. Votre chef dit que non.",
            "Qui a raison ? Qui tranche ?",
            "Est-ce que vous pouvez refuser de la faire ?",
            "Est-ce que vous pouvez refuser n'importe quoi ?",
        ],
        notes="Recueillir les réponses sans corriger. Les deux erreurs habituelles "
              "sont opposées : « on ne peut rien refuser » et « on peut refuser ce "
              "qu'on veut ». Les deux se corrigent avec le tableau du droit de refus.")

    d.tableau('Analyse', "Deux régimes, selon la taille",
              ['La taille', 'Ce qu\'il faut avoir'],
              [["20 travailleurs et plus", "un programme de prévention"],
               ["", "un comité de santé et de sécurité"],
               ["", "un représentant en santé et en sécurité"],
               ["19 travailleurs et moins", "un plan d'action"],
               ["", "un agent de liaison en santé et en sécurité"]],
              cle=0,
              note="Règlement en vigueur depuis le 1er octobre 2025. Le seuil se compte par établissement, pas par entreprise.",
              notes="Diapositive à photographier. La note règle une question qui vient "
                    "toujours : une compagnie de deux cents personnes réparties en "
                    "trois petits ateliers relève du second régime pour chacun. "
                    "Vérifié sur cnesst.gouv.qc.ca le 22 août 2026.")

    d.regle("Le programme de prévention se met à jour chaque année",
            "Il s'élabore, s'applique et se met à jour annuellement.",
            precision="Ce n'est pas un document qu'on écrit une fois et qu'on range. "
                      "L'employeur doit y inscrire les risques de son établissement et "
                      "ce qu'il fait pour les enlever, puis le reprendre tous les ans. "
                      "Et tous les trois ans, il transmet à la CNESST ses priorités "
                      "d'action et le suivi de ses mesures, sur le formulaire prescrit.",
            notes="Diapositive à photographier. C'est le document qu'Aïcha ne "
                  "connaissait pas et qui parlait déjà de son problème. Demander au "
                  "groupe : savez-vous s'il en existe un chez vous ? Presque personne "
                  "ne le sait, et c'est le point de la séance.")

    d.cartes('Analyse', "Le représentant en santé et en sécurité", [
        ("Il est élu", "Par les travailleurs, pas nommé par la direction. C'est ce qui distingue Thérèse d'une gestionnaire."),
        ("Il siège au comité", "Où au moins la moitié des membres, dont lui, représentent les travailleurs."),
        ("On peut lui parler", "Sans passer par son supérieur. C'est tout l'intérêt d'une personne élue."),
        ("Le comité réunit les deux côtés", "Employeur et travailleurs. Le représentant, lui, est d'un seul côté, et c'est écrit dans la loi."),
    ], notes="Faire remarquer que Thérèse, dans les dialogues, ne demande jamais la "
             "permission de parler : elle intervient de plein droit. C'est ce que son "
             "rôle veut dire.")

    d.tableau('Analyse', "Le droit de refus, articles 12 et 13",
              ['La situation', 'Ce que dit la loi'],
              [["On peut refuser", "s'il y a des motifs raisonnables de croire à un danger"],
               ["Pour soi ou pour autrui", "un danger semblable pour une autre personne compte aussi"],
               ["On ne peut pas refuser", "si le refus met en péril immédiat une autre personne"],
               ["Ni refuser", "si les conditions sont normales pour ce genre de travail"],
               ["En cas de désaccord", "l'inspecteur de la CNESST décide s'il y a danger"]],
              cle=0,
              note="« Motifs raisonnables de croire » n'exige pas d'avoir raison : il exige d'avoir des raisons.",
              notes="Diapositive à photographier, et la plus importante du module hors "
                    "de la classe. La note est une nuance juridique réelle et elle "
                    "protège la personne de bonne foi. Loi sur la santé et la sécurité "
                    "du travail, articles 12 et 13, vérifiés le 22 août 2026.")

    d.pratique('Compréhension', "Le programme de prévention et la loi",
               "Répondez d'après le document projeté au module.", [
        ("À partir de combien de travailleurs un programme est-il obligatoire ?", "vingt"),
        ("À quelle fréquence se met-il à jour ?", "chaque année"),
        ("Qui élit le représentant en santé et en sécurité ?", "les travailleurs"),
        ("Dans quel cas peut-on refuser un travail ?", "motif raisonnable de croire à un danger"),
        ("Peut-on refuser si les conditions sont normales pour ce métier ?", "non - article 13"),
        ("Qui tranche s'il y a désaccord sur le danger ?", "l'inspecteur de la CNESST"),
    ], corrige=True,
       notes="Ouvrir l'exercice `t2cnesst` du module en parallèle : c'est un texte "
             "suivi avec passages cliquables, et les élèves y retrouvent les phrases "
             "exactes de la loi.")

    d.piege('Compréhension',
            "croire qu'une politique d'employeur est une loi",
            "demander où c'est écrit",
            "Une politique interne s'applique parce que l'employeur s'y engage. Elle "
            "peut être meilleure que la loi - jamais moins bonne. Savoir de quel texte "
            "vient une règle change tout : on négocie une politique, on n'en négocie "
            "pas une loi.",
            notes="Faire donner un exemple de chaque par le groupe. Les congés "
                  "supplémentaires d'une convention sont une politique ; le droit de "
                  "refus est une loi.")

    d.billet(
        "Cherchez si votre milieu de travail a un programme de prévention.",
        exemples=[
            "Combien de personnes travaillent dans votre établissement ?",
            "Y a-t-il un comité de santé et de sécurité ? Un représentant ?",
            "À qui poseriez-vous la question ?",
        ],
        notes="Devoir réel, à faire hors de la classe. Prévoir cinq minutes au début "
              "de la séance D1 pour les réponses : elles sont souvent surprenantes, y "
              "compris pour les élèves qui travaillent depuis des années au même "
              "endroit.")

    return d.save(dossier)
