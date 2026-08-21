# -*- coding: utf-8 -*-
"""C4 · « Du message au mot »
Bloc C « Défi 2 · Le message et le mot » · couleur ambre · 75 min.
Source : exercices `t2rap` et `t2note`, mini-leçon `t2rap`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-voisinage/images/')


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="« Du message au mot »",
        chapeau="Écouter un message est une chose. Le redire à quelqu'un "
                "d'autre en est une autre : il faut changer les personnes, "
                "changer l'ordre des mots dans les questions, jeter les "
                "bonjours et garder les chiffres.",
        duree='75 minutes')

    d.titre(notes="Séance la plus exigeante du module, et celle qui répond exactement à "
                  "une intention du programme : rédiger un mot avec les notes prises en "
                  "écoutant un message téléphonique. Prévoir de finir par l'écriture, pas "
                  "par la grammaire.")

    d.objectifs([
        "rapporter une affirmation avec « dit que » ;",
        "rapporter une question fermée avec « demande si » ;",
        "rapporter une question ouverte sans inversion ;",
        "écrire un mot de six lignes qu'un autre peut exécuter.",
    ], notes="Le troisième objectif est le plus contre-intuitif : après « elle demande "
             "quand », la phrase redevient une phrase ordinaire.")

    d.regle("Quatre transformations, et rien d'autre",
            "Une affirmation devient « dit que ». Une question fermée devient "
            "« demande si ». Une question ouverte garde son mot. Un ordre "
            "devient « de » plus l'infinitif.",
            precision="« Je ne peux pas venir » donne : elle dit qu'elle ne peut "
                      "pas venir. · « Est-ce que vous êtes libre ? » donne : elle "
                      "demande si vous êtes libre. · « Rappelez-moi » donne : elle "
                      "demande de la rappeler.",
            notes="Diapositive à photographier. Les quatre transformations couvrent tout "
                  "ce qu'un message de voisinage peut contenir.")

    d.tableau('Ce qui change', "Le message entendu, et le mot écrit",
              ['On entend', 'On écrit'],
              [["Je ne peux pas venir.", "Elle dit qu'elle ne peut pas venir."],
               ["Est-ce que vous êtes libre ?", "Elle demande si vous êtes libre."],
               ["Quand est-ce que vous partez ?", "Elle demande quand vous partez."],
               ["Rappelez-moi après trois heures.", "Elle demande de la rappeler."],
               ["N'appelez pas le matin.", "Elle demande de ne pas appeler le matin."]],
              cle=1,
              notes="Faire remarquer la troisième ligne : l'inversion disparaît. On "
                    "n'écrit jamais « elle demande quand partez-vous ». C'est l'erreur la "
                    "plus fréquente et la plus facile à corriger.")

    d.cartes("Ce qui disparaît, ce qui reste", "Un mot garde les faits", [
        ("Ce qui disparaît",
         "Les bonjour, les excusez-moi, les euh, les répétitions."),
        ("Ce qui reste toujours",
         "Qui, quand, quoi, les dates, et le numéro."),
        ("Ce qui change de personne",
         "« je » devient « elle », « mon » devient « son », « chez moi » devient « chez elle »."),
        ("Le test de Réjean",
         "Si quelqu'un d'autre lit ce papier, est-ce qu'il comprend ?"),
    ], notes="La troisième carte est celle qui demande la relecture : faire chercher les "
             "« je » oubliés dans un mot rapporté est un réflexe qui s'installe vite et "
             "qui règle presque tout.")

    d.pratique('Grammaire', "Rapportez ce que vous avez entendu",
               "Écrivez seulement le mot qui manque.", [
        ("« Je ne peux pas venir. » Elle dit ___ elle ne peut pas venir.", "qu'"),
        ("« Est-ce que vous êtes libre ? » Elle demande ___ vous êtes libre.", "si"),
        ("« Quand est-ce que vous partez ? » Elle demande ___ vous partez.", "quand"),
        ("« Rappelez-moi. » Elle demande ___ la rappeler.", "de"),
        ("« Qui va arroser les plantes ? » Elle demande ___ va arroser.", "qui"),
        ("« N'appelez pas le matin. » Elle demande de ___ pas appeler.", "ne"),
    ], corrige=True,
       notes="Exercice t2rap de l'activité. Faire dire la phrase entière à voix haute "
             "après chaque réponse : l'oreille attrape les « je » restés en place mieux "
             "que l'œil.")

    d.declencheur(
        'Écriture', "Le mot que Marisol laisse sur la table. Six lignes, "
                    "et tout doit y être.",
        image=IMG + 'mot-sur-frigo.jpg',
        pistes=[
            "Qui a appelé : le nom au complet, et l'étage.",
            "Quand : le jour et l'heure de l'appel.",
            "Ce qu'elle demande, et pour quelles dates.",
            "Le numéro, et le moment où l'on peut rappeler.",
        ],
        notes="Faire écrire le mot individuellement, sur papier, avant d'ouvrir "
              "l'exercice t2note. Ramasser deux ou trois versions et les lire à voix "
              "haute : le groupe repère tout de suite ce qui manque.")

    d.pratique('Écriture', "Le mot sur la table de la cuisine",
               "Complétez à partir du message entendu en C1.", [
        ("Qui a appelé : Ndeye ___ , la voisine du 3e.", "Faye"),
        ("Quand : message reçu ___ soir, vers 19 h.", "mardi"),
        ("Ce qu'elle demande : quelqu'un pour ___ ses plantes.", "arroser"),
        ("Dates : du 10 ___ 20 juillet.", "au"),
        ("Rappeler au 514 555- ___ .", "0148"),
        ("Quand rappeler : après ___ heures, pas avant.", "trois"),
    ], corrige=True,
       notes="Exercice t2note de l'activité. Faire remarquer que les dates de l'appel et "
             "les dates de la demande sont deux choses différentes : les mélanger est "
             "l'erreur classique, et elle rend le mot inutilisable.")

    d.piege("Garder « est-ce que » en rapportant",
            "Elle demande est-ce que vous êtes libre.",
            "Elle demande si vous êtes libre.",
            "« Est-ce que » n'existe que dans la question directe. Rapporté, il devient "
            "« si ».",
            notes="Faire dire les deux versions : la mauvaise s'entend mal, ce qui aide "
                  "plus que la règle.")

    d.billet(
        "Écrivez un mot de six lignes à partir d'un message que vous avez vraiment reçu.",
        exemples=[
            "Qui, quand, quoi, les dates, le numéro, le moment où rappeler.",
            "Faites lire votre mot par votre voisin de table : comprend-il tout ?",
        ],
        notes="Fin du bloc C. Le test par le voisin de table est le test de Réjean, rendu "
              "concret. C'est la meilleure façon de terminer la séance.")

    return d.save(dossier)
