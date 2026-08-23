# -*- coding: utf-8 -*-
"""C1 · Deux portraits sur la table
Bloc C « Défi 2 · Lire un portrait de région » · couleur acier · 75 min.
Source : dialogue `t2` (répliques 1 à 9), exercice `t2vf`.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n7-recherche' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Deux portraits sur la table",
        chapeau="On ne décide pas en lisant, on décide en comparant. Trois "
                "questions posées à un document, une feuille à deux "
                "colonnes, et vingt minutes suffisent.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 2. Faire apporter à chacun le nom de la région "
                  "qu'il avait écrite au billet de A1 : la séance s'applique à sa "
                  "propre recherche, pas seulement à celle de Hafida.")

    d.objectifs([
        "poser trois questions à un portrait économique, et pas davantage ;",
        "trouver dans le texte ce qu'il dit, et savoir ce qu'il ne dit pas ;",
        "reconnaître les trois procédés qui rendent ces textes difficiles ;",
        "bâtir une feuille de comparaison à deux colonnes.",
    ], notes="Le troisième objectif annonce C2, C3 et C4 : la nominalisation, la "
             "phrase passive et le « ils » sans antécédent.")

    d.declencheur(
        'Observation', "À quoi ressemble un portrait économique ?",
        image=IMG + 'table-cv.jpg',
        pistes=[
            "Combien de pages, à votre avis ?",
            "Qu'est-ce qu'on y cherche quand on cherche un emploi ?",
            "Le liriez-vous du début à la fin ?",
            "Où iriez-vous en premier ?",
        ],
        notes="Réponse attendue à la dernière question : au tiers du texte, dans la "
              "partie sur les secteurs. Ne pas la donner : la séance y mène.")

    d.dialogue('Dialogue · 1 de 2', "Trois choses, pas davantage", [
        ("MARIE-ÈVE", "Vous avez imprimé les deux portraits ? Posez-les côte à côte sur la table.", True),
        ("HAFIDA", "Je les ai lus trois fois. Je comprends chaque phrase, mais je n'arrive pas à décider.", True),
        ("MARIE-ÈVE", "Ce n'est pas un problème de vocabulaire, c'est un problème de méthode.", True),
        ("MARIE-ÈVE", "Trois choses seulement, sinon vous vous noyez. Prenez une feuille et tracez deux colonnes.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="« Je comprends chaque phrase mais je n'arrive pas à décider » est la "
             "phrase la plus juste du module. La faire répéter : c'est la situation "
             "réelle de la plupart des élèves devant un document officiel.")

    d.dialogue('Dialogue · 2 de 2', "Ce que le portrait ne dira jamais", [
        ("HAFIDA", "Deuxième point : est-ce qu'il manque du monde ? Le portrait ne le dit pas.", True),
        ("MARIE-ÈVE", "Un portrait économique ne le dit jamais. Il décrit une structure, pas un manque.", True),
        ("MARIE-ÈVE", "Pour le manque, vous retournez à IMT en ligne et vous regardez les perspectives de votre profession.", True),
        ("MARIE-ÈVE", "Et la troisième colonne, aucun document ne la remplira à votre place.", True),
    ], notes="La dernière réplique parle de la famille. Ne pas la traiter à la légère : "
             "un déménagement en région est une décision de ménage, et plusieurs "
             "élèves en portent déjà le poids.")

    d.regle("Trois questions, et vingt minutes",
            "Est-ce que mon métier existe ici ? Est-ce qu'il y manque du "
            "monde ? Est-ce que ma famille pourrait y vivre ?",
            precision="Le portrait répond à la première, IMT en ligne à la deuxième, "
                      "et personne à la troisième. Confondre les trois est ce qui "
                      "fait relire cinq fois un document qui n'a jamais contenu la "
                      "réponse qu'on y cherchait.",
            notes="Diapositive à photographier. C'est la méthode de tout le bloc C, "
                  "et elle sert bien au-delà du module.")

    d.tableau('Analyse', "La structure d'un portrait, toujours la même",
              ['Partie', 'Ce qu\'on y trouve'],
              [["1. Le territoire", "population, superficie, rang parmi les régions"],
               ["2. L'économie d'ensemble", "produit intérieur brut, emploi total"],
               ["3. Les secteurs", "primaire, fabrication, construction, services"]],
              cle=0,
              note="Si vous cherchez un métier, votre information est dans la partie 3. Le reste est du contexte.",
              notes="Diapositive à photographier. Le dire franchement : on a le droit "
                    "de sauter deux pages d'un document officiel.")

    d.piege('Lecture',
            "lire le portrait du début à la fin",
            "aller directement à la partie qui vous concerne",
            "Deux pages de population et de superficie n'apprennent rien à "
            "quelqu'un qui cherche un laboratoire. Sauter n'est pas de la "
            "paresse : c'est ce que fait toute personne qui lit ces "
            "documents pour son travail.",
            notes="Objection fréquente : « je vais manquer quelque chose ». Répondre "
                  "qu'on peut toujours remonter, et qu'on ne remonte presque jamais.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Marie-Ève conseille de comparer trois choses seulement.", "vrai"),
        ("Hafida n'a lu les deux portraits qu'une seule fois.", "faux - trois fois"),
        ("Chaudière-Appalaches transforme surtout des aliments et du métal ouvré.", "vrai"),
        ("Un portrait économique dit toujours s'il manque de main-d'œuvre.", "faux - jamais"),
        ("Pour le manque, il faut consulter IMT en ligne.", "vrai"),
        ("La troisième colonne se remplit avec un document officiel.", "faux - elle se décide en famille"),
    ], corrige=True,
       notes="Exercice `t2vf` du module interactif. Le quatrième et le cinquième vont "
             "ensemble : c'est le point à retenir de la séance.")

    d.billet(
        "Tracez vos deux colonnes et remplissez la première ligne : est-ce que mon métier existe dans ces régions ?",
        exemples=[
            "Deux régions, une ligne chacune.",
            "Si vous ne savez pas, écrivez « à vérifier » : c'est une réponse.",
        ],
        notes="La feuille se poursuit en C4. Demander de la garder : elle devient "
              "le plan de l'exposé oral du bloc E.")

    return d.save(dossier)
