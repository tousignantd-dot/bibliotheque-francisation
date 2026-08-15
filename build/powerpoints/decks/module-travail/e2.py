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

    d.vocabulaire('Vocabulaire · 1 de 3', "Les trois mots du module", [
        ("un retard", "Le fait d'arriver après un moment fixé."),
        ("une absence", "Le fait de ne pas se trouver à un endroit où on est attendu."),
        ("un abandon", "Le fait de renoncer à une chose : un cours, un travail."),
        ("prévenir", "Informer à l'avance."),
        ("justifier", "Donner la raison d'un retard ou d'une absence."),
        ("reprendre des heures", "Travailler plus tard pour remplacer les heures manquées."),
    ], notes="Cacher la colonne de droite et faire donner les définitions. Ces trois mots "
             "sont le cœur du module : personne ne doit les confondre en sortant.")

    d.vocabulaire('Vocabulaire · 2 de 3', "Les documents", [
        ("un billet médical", "Un document du médecin qui confirme une consultation."),
        ("une pièce d'identité", "Un document officiel qui prouve qui on est."),
        ("une preuve de résidence", "Un document qui prouve où on habite."),
        ("une attestation", "Un document qui confirme une présence ou des heures suivies."),
        ("un formulaire signé", "Un document rempli et signé, exigé pour une démarche."),
    ], notes="Faire dire, pour chaque document, où on l'obtient. C'est l'information qui "
             "manque le plus souvent.")

    d.vocabulaire('Vocabulaire · 3 de 3', "Le travail et le centre", [
        ("une superviseure", "La personne responsable des employés."),
        ("une boîte vocale", "Le système qui enregistre un message quand personne ne répond."),
        ("remplacer", "Prendre la place de quelqu'un."),
        ("le télétravail", "Travailler depuis la maison."),
        ("une entrevue d'embauche", "Une rencontre pour obtenir un emploi."),
        ("un dégât d'eau", "Un dommage causé par de l'eau dans un logement."),
    ], notes="Faire produire une phrase complète avec chaque mot, dans une situation de "
             "retard ou d'absence.")

    d.tableau('Révision · 1 de 2', "Les savoirs du module",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["é fermé et è ouvert", "à la fin d'un mot, presque toujours é", "A2"],
               ["Retard, absence, abandon", "la question est : est-ce que je reviens ?", "A3"],
               ["Le message téléphonique", "six parties, dans un ordre fixe", "B2"],
               ["Le pronom qui", "toujours suivi d'un verbe, accordé au groupe repris", "B3"],
               ["Et, ou, mais", "addition, choix, opposition", "C2"]],
              cle=0,
              notes="Faire retrouver la règle avant d'afficher la colonne du milieu. Ce "
                    "qui ne revient pas est ce qu'il faut retravailler.")

    d.tableau('Révision · 2 de 2', "Les savoirs du module, suite",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["Quel, quelle, quels", "le nom commande l'accord", "C3"],
               ["Le courriel", "cinq parties, le but d'abord", "D1"],
               ["Le registre", "il dépend de la relation", "D2"],
               ["Devoir et il faut", "devoir désigne, il faut non", "D2"]],
              cle=0, props=[0.3, 0.55, 0.15],
              note="Neuf savoirs pour un module. Chacun renvoie à une séance : c'est là "
                   "qu'il faut retourner si la règle ne revient pas.",
              notes="Insister sur la dernière colonne. Le module reste ouvert dans le "
                    "portail : chacun peut y revenir seul.")

    d.cartes('Les quatre gestes du module', "Ce qu'on sait faire maintenant", [
        ("Prévenir au bon moment",
         "Avant de partir, pas après être revenu. C'est la règle de la première séance "
         "et celle de tout le module."),
        ("Choisir le bon mot",
         "Retard, absence ou abandon. La question à se poser : est-ce que je reviens, "
         "et quand ?"),
        ("Laisser un message complet",
         "Six parties, trente secondes, le numéro répété deux fois, lentement."),
        ("Écrire un courriel professionnel",
         "Cinq parties, un objet précis, le but dès la première phrase, et une "
         "demande claire."),
    ], notes="Faire dire à chacun lequel des quatre lui paraît le plus solide, et lequel "
             "le moins. Personne ne doit répondre « tous ».")

    d.pratique('Bilan · 1 de 2', "Le vocabulaire, sans regarder",
               "Donnez le mot qui correspond à la définition.", [
        ("Le fait d'arriver après un moment fixé.", "un retard"),
        ("Le fait de renoncer à un cours ou à un travail.", "un abandon"),
        ("Informer à l'avance.", "prévenir"),
        ("Un document du médecin qui confirme une consultation.", "un billet médical"),
        ("Un document qui confirme les heures suivies.", "une attestation"),
        ("Le système qui enregistre un message téléphonique.", "une boîte vocale"),
    ], corrige=True,
       notes="Exercice individuel, cahier fermé, cinq minutes. Corriger ensemble sans "
             "compter les points.")

    d.pratique('Bilan · 2 de 2', "Autoévaluation",
               "Pour chaque énoncé : je sais faire, presque, ou pas encore.", [
        ("Je sais quand prévenir et à qui.", "séances A1, A3"),
        ("Je distingue un retard, une absence et un abandon.", "séance A3"),
        ("Je peux laisser un message complet dans une boîte vocale.", "séances B1, B2, B4"),
        ("Je peux expliquer un retard au téléphone.", "séances C1, C4"),
        ("Je peux écrire un courriel professionnel.", "séances D1, D2"),
        ("Je peux écrire un courriel d'abandon et demander une attestation.", "séance E1"),
    ], corrige=True,
       notes="La colonne de droite n'est pas une correction : c'est l'adresse où "
             "retourner. Le dire clairement au groupe.")

    d.billet(
        "Nommez une fois où vous avez prévenu quelqu'un en français, en dehors de la classe.",
        exemples=[
            "Au travail, à l'école de vos enfants, chez le médecin.",
            "S'il n'y en a aucune, nommez celle qui viendra bientôt.",
        ],
        notes="Fin du module. Ces billets disent ce qui est vraiment passé de la classe "
              "à la vie — c'est le seul bilan qui compte.")

    return d.save(dossier)
