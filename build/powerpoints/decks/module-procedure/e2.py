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

    d.vocabulaire('Vocabulaire · 1 de 3', "La demande", [
        ("une procédure", "La façon officielle de faire une demande ou une tâche."),
        ("un remboursement", "L'argent qu'on redonne à quelqu'un pour une dépense."),
        ("un formulaire", "Un document à remplir avec des informations précises."),
        ("un reçu", "Le papier qui prouve un achat."),
        ("joindre", "Ajouter un document à un envoi."),
        ("approuver", "Donner son accord officiel à une demande."),
    ], notes="Cacher la colonne de droite et faire donner les définitions. Puis "
             "l'inverse.")

    d.vocabulaire('Vocabulaire · 2 de 3', "L'application et les délais", [
        ("un onglet", "Une section cliquable dans une application ou un site."),
        ("une catégorie", "Un groupe dans lequel on classe une dépense."),
        ("le statut", "L'état d'une demande : en attente, approuvée, refusée."),
        ("un jour ouvrable", "Un jour de la semaine où l'entreprise est ouverte."),
        ("un accusé de réception", "Le message qui confirme qu'une demande est arrivée."),
    ], notes="« Jour ouvrable » revient une dernière fois : faire refaire le calcul de "
             "dix jours sur un calendrier.")

    d.vocabulaire('Vocabulaire · 3 de 3', "Les directives", [
        ("une directive", "Une instruction précise à suivre."),
        ("signaler", "Faire savoir, informer quelqu'un d'un problème."),
        ("un bris d'équipement", "Un équipement qui casse ou cesse de fonctionner."),
        ("un véhicule de service", "Un véhicule de l'entreprise, utilisé pour le travail."),
        ("un superviseur", "La personne responsable d'une équipe de travail."),
    ], notes="Faire produire une phrase à l'impératif avec « signaler ». C'est la "
             "révision des deux savoirs à la fois.")

    d.tableau('Révision · 1 de 2', "Les savoirs du module",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["Trois sons", "ui collé, j ou g devant e-i-y, gn en un son", "A2"],
               ["Les verbes de bureau", "on apprend le verbe avec son complément", "A3"],
               ["Le pronom que", "après que, un sujet ; après qui, un verbe", "B2"],
               ["Les degrés d'obligation", "cherchez le verbe, pas le ton", "B3"],
               ["Pendant que", "deux personnes, deux actions, un moment", "C2"]],
              cle=0,
              notes="Faire retrouver la règle avant d'afficher la colonne du milieu. Ce "
                    "qui ne revient pas est ce qu'il faut retravailler.")

    d.tableau('Révision · 2 de 2', "Les savoirs du module, suite",
              ['Le savoir', 'La règle en une phrase', 'Séance'],
              [["Le gérondif", "même personne : quand, ou comment", "C3"],
               ["L'impératif", "la forme vous, sans le sujet", "C4"],
               ["Le pronom après", "impératif affirmatif : trait d'union", "C4"],
               ["Lire une directive", "fournir, se passer, quoi faire si ça bloque", "D1"]],
              cle=0, props=[0.28, 0.57, 0.15],
              note="Neuf savoirs pour un module. Chacun renvoie à une séance : c'est là "
                   "qu'il faut retourner.",
              notes="Insister sur la dernière colonne. Le module reste ouvert dans le "
                    "portail : chacun peut y revenir seul.")

    d.cartes('Les quatre gestes du module', "Ce qu'on sait faire maintenant", [
        ("Demander comment faire",
         "Trois questions : comment faire, qu'est-ce qui est obligatoire, combien de "
         "temps. Elles fonctionnent partout."),
        ("Suivre une explication orale",
         "Compter les verbes, pas les phrases. Noter l'ordre pendant l'écoute, pas "
         "après."),
        ("Lire une directive écrite",
         "Trois blocs : ce qu'il faut fournir, ce qui se passe, quoi faire si ça "
         "bloque."),
        ("Écrire une procédure",
         "Une étape par ligne, à l'impératif, numérotées, avec le délai et le recours."),
    ], notes="Faire dire à chacun lequel des quatre lui paraît le plus solide, et lequel "
             "le moins. Personne ne doit répondre « tous ».")

    d.pratique('Bilan · 1 de 2', "Le vocabulaire, sans regarder",
               "Donnez le mot qui correspond à la définition.", [
        ("La façon officielle de faire une demande.", "une procédure"),
        ("Ajouter un document à un envoi.", "joindre"),
        ("Donner son accord officiel.", "approuver"),
        ("Faire savoir qu'il y a un problème.", "signaler"),
        ("Un jour où l'entreprise est ouverte.", "un jour ouvrable"),
        ("Le message qui confirme qu'une demande est arrivée.", "un accusé de réception"),
    ], corrige=True,
       notes="Exercice individuel, cahier fermé, cinq minutes. Corriger ensemble sans "
             "compter les points.")

    d.pratique('Bilan · 2 de 2', "Autoévaluation",
               "Pour chaque énoncé : je sais faire, presque, ou pas encore.", [
        ("Je peux demander comment faire une démarche.", "séances B1, B4"),
        ("Je peux suivre une explication en cinq étapes.", "séances A4, C1"),
        ("Je sais distinguer ce qui est obligatoire de ce qui est conseillé.", "séance B3"),
        ("Je peux écrire une consigne à l'impératif.", "séance C4"),
        ("Je peux lire une directive et en tirer les exigences.", "séances D1, D2"),
        ("Je peux rédiger une procédure pour un collègue.", "séance E1"),
    ], corrige=True,
       notes="La colonne de droite n'est pas une correction : c'est l'adresse où "
             "retourner. Le dire clairement au groupe.")

    d.billet(
        "Nommez une procédure que vous comprenez mieux qu'au début du module.",
        exemples=[
            "Au travail, à l'école, à la banque, dans un bureau du gouvernement.",
            "S'il n'y en a aucune, nommez celle que vous irez comprendre cette semaine.",
        ],
        notes="Fin du module. Ces billets disent ce qui est vraiment passé de la classe "
              "à la vie — c'est le seul bilan qui compte.")

    return d.save(dossier)
