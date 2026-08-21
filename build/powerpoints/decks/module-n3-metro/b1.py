# -*- coding: utf-8 -*-
"""B1 · Quatre titres, quatre prix.
Bloc B « Défi 1 · Comprendre ce qu'on me répond » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Quatre titres, quatre prix',
        chapeau="Au comptoir, quatre prix se donnent en moins d'une minute. "
                "L'élève n'a rien à dire : il a seulement à comprendre.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1, qui est une compétence de compréhension orale. "
                  "Reprendre les billets de sortie de la séance A1 et écrire au tableau "
                  "ce que chacun paie par mois. Ces chiffres serviront toute la séance.")

    d.objectifs([
        "comprendre les quatre titres nommés au comptoir ;",
        "retenir un prix et une durée dits une seule fois ;",
        "comprendre la première question du préposé : combien de fois par semaine ;",
        "savoir dans quelle zone on se déplace.",
    ])

    d.declencheur(
        'Observation', "Quel titre coûte le moins cher pour cinq jours par semaine ?",
        pistes=[
            "Cinq jours aller-retour, combien de déplacements par semaine ?",
            "Et par mois, sur quatre semaines ?",
            "Est-ce qu'un titre de dix passages suffit pour une semaine ?",
            "Qu'est-ce qui coûte le plus cher : payer chaque fois, ou payer d'avance ?",
        ],
        notes="Faire calculer au tableau : cinq jours aller-retour font dix déplacements "
              "par semaine, donc plus de quarante par mois. À trois dollars soixante-"
              "quinze le passage, cela ferait cent cinquante dollars. Laisser le groupe "
              "trouver le chiffre avant de donner celui du mensuel.")

    d.dialogue('Dialogue · 1 de 3', "Vous vous déplacez combien de fois ?", [
        ("ROSARIO", "Bonjour. Mon ami dit que je paie trop cher. Je voudrais me renseigner.", True),
        ("LORRAINE", "Bonjour. Vous vous déplacez combien de fois par semaine ?", True),
        ("ROSARIO", "Cinq jours. Le matin et le soir. Des fois le samedi aussi.", True),
        ("LORRAINE", "Et vous restez dans l'île de Montréal ? C'est la zone A.", True),
        ("ROSARIO", "Oui. La maison, l'école, l'épicerie. Tout est à Montréal.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Deux questions, toujours les mêmes, et dans cet ordre : combien de fois, "
             "et dans quelle zone. Les faire mémoriser : un élève qui les attend "
             "comprend la moitié de la conversation d'avance.")

    d.dialogue('Dialogue · 2 de 3', "Trois dollars soixante-quinze", [
        ("LORRAINE", "Bon. Un passage tout seul coûte trois dollars soixante-quinze.", True),
        ("ROSARIO", "Et le dix passages ? C'est celui-là que j'achète.", True),
        ("LORRAINE", "Trente-cinq dollars. Ça revient à trois cinquante le passage.", True),
        ("ROSARIO", "D'accord. Et pour une semaine complète ?", True),
        ("LORRAINE", "L'hebdo est à trente-trois vingt-cinq. Il est bon du lundi au dimanche.", True),
    ], notes="Faire noter les prix au fur et à mesure, sur une feuille. C'est ce que "
             "fait n'importe qui au comptoir, et il faut le dire aux élèves : on a le "
             "droit d'écrire pendant qu'on écoute.")

    d.dialogue('Dialogue · 3 de 3', "Cent dix dollars pour le mois", [
        ("ROSARIO", "Trente-trois ? C'est moins cher que le dix passages !", True),
        ("LORRAINE", "Oui, et c'est illimité. Mais le mensuel est encore mieux pour vous.", True),
        ("ROSARIO", "Combien coûte le mensuel ?", True),
        ("LORRAINE", "Cent dix dollars pour le mois. Vous, vous payez à peu près cent quarante.", True),
        ("ROSARIO", "Cent dix… Je vais y penser. Merci beaucoup, madame.", True),
    ], notes="Le mot « illimité » est nouveau et important : il veut dire autant de fois "
             "qu'on veut. Le faire expliquer par un élève plutôt que par l'enseignante. "
             "Rosario économise trente dollars par mois sans changer ses habitudes.")

    d.tableau('Analyse', "Les quatre titres de la zone A",
              ["Le titre", "Le prix"],
              [["Un passage", "3,75 $"],
               ["Dix passages", "35,00 $"],
               ["Hebdo, du lundi au dimanche", "33,25 $"],
               ["Mensuel", "110,00 $"]],
              cle=1,
              note="Prix de la zone A, tarif ordinaire.",
              notes="Diapositive à photographier. Ce sont les vrais prix. Les faire "
                    "recopier dans le cahier : ils serviront jusqu'à la fin du module et "
                    "après, dans la vraie vie.")

    d.regle("Ce que le préposé demande toujours en premier",
            "« Vous vous déplacez combien de fois par semaine ? »",
            precision="Préparez la réponse avant d'arriver au comptoir. Elle "
                      "décide du titre qu'on vous proposera, et une réponse "
                      "claire fait gagner deux minutes à tout le monde. La "
                      "deuxième question est toujours la zone : restez-vous à "
                      "Montréal ?",
            notes="Diapositive à photographier. Faire répondre chaque élève à voix "
                  "haute, en une phrase complète : « Je me déplace dix fois par "
                  "semaine, dans la zone A. »")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Lorraine demande combien de fois par semaine Rosario se déplace.", "vrai"),
        ("Rosario sort de l'île de Montréal chaque jour.", "faux — tout est à Montréal"),
        ("Un passage tout seul coûte trois dollars soixante-quinze.", "vrai"),
        ("L'hebdo est bon du lundi au dimanche.", "vrai"),
        ("L'hebdo coûte plus cher que le dix passages.", "faux — 33,25 $ contre 35 $"),
        ("Le titre mensuel coûte cent dix dollars.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. Le cinquième "
             "énoncé demande une comparaison de deux prix : c'est le point du bloc D, "
             "annoncé ici sans être travaillé.")

    d.billet(
        "Écrivez le titre qui vous conviendrait le mieux, et pourquoi.",
        exemples=[
            "Je me déplace ___ fois par semaine.",
            "Le meilleur titre pour moi, c'est ___ parce que ___ .",
        ],
        notes="Devoir court. Les réponses préparent la séance B2, où chacun justifiera "
              "son choix devant le groupe.")

    return d.save(dossier)
