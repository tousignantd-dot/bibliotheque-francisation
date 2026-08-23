# -*- coding: utf-8 -*-
"""E2 · Votre lettre, et le bilan du module
Bloc E « Je me lance » · couleur framboise · 90 min. Production écrite.
Source : production écrite de « Je me lance » et exercices `t1lettre`, `t1plan`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Votre lettre, et le bilan du module',
        chapeau="Une page, trois paragraphes, et une question à laquelle "
                "personne ne vous demande de répondre : pourquoi vous, et "
                "pas la personne suivante ?",
        duree='90 minutes')

    d.titre(notes="Dernière séance. Elle se termine par l'autoévaluation du module : "
                  "prévoir vingt minutes pour elle, elle n'est pas décorative.")

    d.objectifs([
        "écrire une lettre de motivation en trois paragraphes ;",
        "remplacer chaque adjectif par un fait daté ;",
        "annoncer chaque sujet par un connecteur ;",
        "fermer par une formule de courtoisie qui laisse debout.",
    ], notes="Rappeler que la lettre s'écrit ici, en classe, et non à la maison : "
             "c'est la seule façon de corriger la structure pendant qu'elle se fait.")

    d.declencheur(
        'Observation', "Qu'est-ce que personne ne peut écrire à votre place ?",
        pistes=[
            "Une durée : depuis combien de temps ?",
            "Un lieu : où, exactement ?",
            "Un nombre : combien de personnes, de jours, de quarts ?",
            "Une chose déjà commencée : depuis quand ?",
        ],
        notes="Quatre questions, quatre réponses écrites au brouillon. C'est la "
              "matière du deuxième paragraphe, et elle est prête avant que la lettre "
              "commence.")

    d.tableau('Analyse', "Le plan, une dernière fois",
              ['Le paragraphe', 'Ce qu\'il contient'],
              [['paragraphe 1', "la demande, et pourquoi cet établissement-là"],
               ['paragraphe 2', "deux faits datés, et le trou expliqué en une phrase"],
               ['paragraphe 3', "l'après-diplôme, et ce qui est déjà commencé"],
               ['la fin', "les pièces jointes, puis la formule de courtoisie"]],
              cle=0,
              note="Un objet de six ou sept mots, sans verbe conjugué, au-dessus de "
                   "tout cela.",
              notes="Diapositive à laisser affichée pendant toute l'écriture. C'est le "
                    "seul soutien dont les élèves ont besoin.")

    d.regle("Une raison qui vaut pour tous ne vaut pour aucun",
            "« Votre établissement a une excellente réputation » se lit soixante-huit "
            "fois par jour.",
            precision="La raison propre au centre se trouve dans sa fiche : un stage "
                      "qui arrive tôt, un horaire particulier, un équipement, une "
                      "entrée en janvier. Dix minutes de lecture, une phrase que "
                      "personne d'autre n'écrira.",
            notes="Diapositive à photographier. Faire ouvrir la fiche du bloc A et "
                  "chercher la raison avant d'écrire la première phrase.")

    d.pratique('Écriture', "Le brouillon en six lignes",
               "Écrivez une phrase par case, avant de rédiger la lettre.", [
        ("Ce que je demande, et pour quand", "je pose ma candidature au programme, pour l'entrée d'août"),
        ("Pourquoi cet établissement-là", "une raison tirée de la fiche, pas une politesse"),
        ("Un premier fait daté", "une durée, un lieu, un nombre"),
        ("Un deuxième fait daté", "quelque chose que personne d'autre n'apporte"),
        ("Ce qui manque, en une phrase", "sans excuse, et suivi de ce que je fais déjà"),
        ("Où je vais après le diplôme", "l'étape d'après, nommée"),
    ], corrige=True,
       notes="Vingt minutes. Passer dans les rangées et corriger uniquement les "
             "adjectifs : chaque fois qu'on en voit un, demander la date ou le nombre "
             "qui va dessous.")

    d.piege('Piège', "J'aime beaucoup aider les gens depuis toujours.",
            "Depuis cinq ans, j'accompagne douze résidents à l'unité prothétique.",
            "La première phrase est vraie pour les soixante-sept autres candidatures. "
            "La seconde n'appartient qu'à une personne, et elle se vérifie.",
            notes="Dernier rappel de la règle du bloc B. Si une seule chose devait "
                  "rester du module, ce serait celle-là.")

    d.cartes('Relecture', "Quatre vérifications avant de remettre", [
        ("L'objet",
         "Six ou sept mots, sans verbe conjugué, sans point final."),
        ("Les adjectifs",
         "Chacun remplacé par une durée, un nombre ou un lieu."),
        ("Les paragraphes",
         "Trois, séparés par une ligne blanche, un par idée."),
        ("La formule finale",
         "Elle reprend exactement les mots de la formule d'appel."),
    ], notes="Faire relire la lettre du voisin avec ces quatre points, et rien "
             "d'autre. Dix minutes, et personne ne corrige l'orthographe : ce n'est "
             "pas l'objet.")

    d.billet("Note une chose que tu sais faire aujourd'hui et que tu ne savais pas "
             "faire au début du module.",
             exemples=["Je sais expliquer en une phrase ce qui manque à mon dossier.",
                       "Je sais finir un appel en proposant une date."],
             notes="Ramasser les billets et faire ensuite l'autoévaluation du module, "
                   "dans l'activité interactive. Les seize énoncés y sont, et ils "
                   "reprennent exactement les seize séances.")

    return d.save(dossier)
