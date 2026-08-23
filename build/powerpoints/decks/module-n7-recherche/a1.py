# -*- coding: utf-8 -*-
"""A1 · Le Québec n'est pas un marché du travail, c'en est dix-sept
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

import pathlib

# Chemin déduit du fichier, jamais écrit en dur : le dépôt est aussi construit
# depuis un worktree git, où un chemin absolu vers la copie principale
# pointerait sur des images qui n'y sont pas encore.
IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-recherche' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Chercher là où l'on cherche tous",
        chapeau="Trente-quatre candidatures, trois refus. Le problème n'est "
                "pas toujours le curriculum vitæ : il est parfois dans la "
                "carte du Québec, où dix-sept marchés du travail ne se "
                "ressemblent pas.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "combien de candidatures avez-vous envoyées cette année, et où ? "
                  "Les chiffres sortent vite et ils sont souvent élevés. C'est la "
                  "matière du module.")

    d.objectifs([
        "nommer les outils gratuits de la recherche d'emploi au Québec ;",
        "dire ce qu'une évaluation comparative fait, et ce qu'elle ne fait pas ;",
        "comprendre qu'un métier ne se cherche pas de la même façon partout ;",
        "employer les premiers mots du dossier : le marché du travail, une "
        "perspective d'emploi.",
    ], notes="Le troisième objectif est le cœur du module et il ne sera pas atteint "
             "aujourd'hui. Le poser quand même : tout le reste y revient.")

    d.declencheur(
        'Observation', "Où avez-vous cherché du travail ?",
        image=IMG + 'salle-ordinateurs.jpg',
        pistes=[
            "Dans quelle ville, dans quelle région ?",
            "Combien de candidatures, et combien de réponses ?",
            "Avez-vous déjà travaillé dans un autre métier que le vôtre ?",
            "Connaissez-vous quelqu'un qui est parti en région pour un emploi ?",
        ],
        notes="Question sans mauvaise réponse. Beaucoup d'élèves n'ont cherché que "
              "dans un rayon de vingt kilomètres, et n'ont jamais pensé qu'ils "
              "avaient le choix. Ne pas conclure à leur place : la séance le fera.")

    d.dialogue('Dialogue · 1 de 3', "La salle est gratuite, et moi aussi", [
        ("SYLVAIN", "Bonjour. Vous cherchez un poste libre à l'ordinateur, ou vous avez une question ?", True),
        ("HAFIDA", "Les deux, je pense. C'est la première fois que je viens ici. On m'a dit que la salle était gratuite.", True),
        ("SYLVAIN", "Elle l'est, et pour tout le monde. Vous avez les ordinateurs, l'imprimante, le téléphone, et moi.", True),
        ("HAFIDA", "Hafida Zerouali. Je travaille dans un centre de la petite enfance. Je suis préposée à l'entretien depuis quatre ans.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Insister sur « et pour tout le monde » : plusieurs élèves croient ces "
             "services réservés aux prestataires d'aide sociale. Ils ne le sont pas.")

    d.dialogue('Dialogue · 2 de 3', "Ce que l'avis dit, et ne dit pas", [
        ("HAFIDA", "J'ai demandé l'évaluation comparative il y a deux ans. Mais j'ai compris que ça ne valait pas grand-chose.", True),
        ("SYLVAIN", "Ça vaut quelque chose, mais pas ce que les gens croient. C'est un avis d'expert du gouvernement du Québec.", True),
        ("SYLVAIN", "Ce n'est pas une équivalence, et ça ne remplace jamais un permis d'exercice.", True),
        ("SYLVAIN", "Ce n'est pas un laissez-passer, c'est un traducteur : l'employeur ne sait pas lire votre relevé de notes.", True),
    ], notes="Point de vérité factuelle, à ne pas arrondir : l'évaluation comparative "
             "n'est ni une équivalence ni un permis. Plusieurs élèves ont payé pour "
             "elle en croyant le contraire, et la déception est réelle.")

    d.dialogue('Dialogue · 3 de 3', "Dix-sept marchés, pas un seul", [
        ("HAFIDA", "J'ai envoyé trente-quatre candidatures depuis janvier. Trois réponses. Toutes négatives.", True),
        ("SYLVAIN", "Trente-quatre où ?", True),
        ("HAFIDA", "Ici. Longueuil, Montréal, la Rive-Sud.", True),
        ("SYLVAIN", "Voilà. Le Québec, ce n'est pas un seul marché du travail : c'en est dix-sept, et ils ne se ressemblent pas.", True),
    ], notes="La réplique de la fin est la thèse du module. L'écrire au tableau et "
             "l'y laisser jusqu'à la séance E2.")

    d.tableau('Analyse', "Trois outils gratuits, trois usages",
              ['Outil', 'Ce qu\'il fait'],
              [["La salle multiservice",
                "ordinateurs, imprimante, téléphone, documentation — et un agent"],
               ["IMT en ligne",
                "les salaires et les perspectives de plus de 500 métiers, par région"],
               ["L'évaluation comparative",
                "traduit un diplôme étranger en niveau d'études québécois"],
               ["Le portrait économique",
                "décrit, chiffres à l'appui, de quoi vit un territoire"]],
              cle=0,
              note="Aucun des quatre ne coûte un sou, et aucun ne remplace les trois autres.",
              notes="Diapositive à photographier. Vérifier que chacun sait où se trouve "
                    "le bureau de Services Québec le plus proche de l'école.")

    d.regle("Un avis, pas une équivalence",
            "L'évaluation comparative dit à quel niveau d'ici votre diplôme "
            "se compare. Elle ne le transforme pas en diplôme d'ici.",
            precision="Elle aide un employeur ou un ordre professionnel à comprendre "
                      "un parcours qu'il ne connaît pas. La décision d'embaucher ou "
                      "d'admettre reste entière : l'avis ne l'a jamais prise à leur "
                      "place, et ne remplace aucun permis d'exercice.",
            notes="Diapositive à photographier. Question fréquente : « à quoi ça sert, "
                  "alors ? » Répondre par l'image du traducteur, du dialogue.")

    d.vocabulaire('Vocabulaire', "Six mots pour commencer", [
        ("le marché du travail", "L'ensemble des postes offerts et des personnes qui les cherchent, dans un territoire."),
        ("la salle multiservice", "La pièce d'un bureau public où l'on met gratuitement à votre disposition des postes de travail."),
        ("une évaluation comparative", "L'avis officiel qui dit à quel niveau d'études d'ici se compare un diplôme obtenu ailleurs."),
        ("une perspective d'emploi", "Ce qu'on prévoit des chances de trouver du travail dans un métier, pour les années à venir."),
        ("un curriculum vitæ", "Le document d'une ou deux pages qui résume la formation et l'expérience d'une personne."),
        ("une lettre d'accompagnement", "La lettre jointe à une candidature, qui explique pourquoi ce poste et pourquoi soi."),
    ], notes="Faire répéter avec l'article. « Curriculum vitæ » ne prend pas de « s » "
             "au pluriel : des curriculum vitæ.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Hafida a travaillé neuf ans comme technicienne de laboratoire.", "vrai"),
        ("La salle multiservice est réservée aux personnes sans emploi.", "faux - elle est ouverte à tous"),
        ("L'évaluation comparative est une équivalence de diplôme.", "faux - c'est un avis d'expert"),
        ("Hafida a envoyé trente-quatre candidatures depuis janvier.", "vrai"),
        ("Elle a cherché du travail dans plusieurs régions du Québec.", "faux - seulement autour de Montréal"),
        ("Sylvain conseille à Hafida de déménager tout de suite.", "faux - de regarder avant de décider"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le dernier est "
             "important : personne ne dit à Hafida de partir.")

    d.billet(
        "Dans quelle région du Québec aimeriez-vous savoir s'il y a du travail pour vous ?",
        exemples=[
            "Nommez-en une, même sans raison précise.",
            "Qu'est-ce que vous en savez déjà ?",
        ],
        notes="Devoir concret. Les réponses servent de matière première au bloc B : "
              "chaque élève arrive avec une région à examiner.")

    return d.save(dossier)
