# -*- coding: utf-8 -*-
"""B1 · Cent quarante-cinq de l'heure.
Bloc B « Défi 1 · Le camion » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-emmenagement/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Cent quarante-cinq de l'heure",
        chapeau="Un appel de quatre minutes décide du prix, de la date et de "
                "ce qui arrivera si un meuble est abîmé.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Demander qui a déjà appelé une compagnie de "
                  "déménagement, et combien ça a coûté. L'écart entre les réponses est "
                  "le sujet de la séance.")

    d.objectifs([
        "comprendre un appel à une compagnie de déménagement ;",
        "repérer les chiffres, les dates et les conditions ;",
        "donner sa situation en quelques phrases suivies ;",
        "répéter une date et une heure pour les confirmer.",
    ])

    d.declencheur(
        'Observation', "Vous appelez pour un camion. Qu'est-ce qu'on va vous "
                       "demander en premier ?",
        image=IMG + 'camion-demenagement.jpg',
        pistes=[
            "La date ? L'adresse ?",
            "L'étage, et s'il y a un ascenseur ?",
            "Combien de boîtes ?",
            "Et vous, qu'est-ce que vous voulez savoir ?",
        ],
        notes="Faire deux colonnes au tableau : ce qu'elle demande, ce que je demande. La "
              "deuxième colonne est presque toujours vide au départ — c'est le point de "
              "la séance.")

    d.dialogue('Dialogue · 1 de 3', "Il me reste des camions le matin", [
        ("PATRICIA", "Déménagement Cap-Rouge, bonjour.", True),
        ("AMADOU", "Bonjour. J'appelle pour faire déménager mes affaires le "
                   "premier juillet. Est-ce qu'il vous reste de la place ?", True),
        ("PATRICIA", "Le premier juillet, il me reste des camions le matin "
                     "seulement. Vous partez d'où et vous allez où ?", True),
        ("AMADOU", "Je pars d'un trois et demie à Beauport et je m'en vais rue des "
                   "Peupliers, à Limoilou.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Amadou donne les deux adresses en une seule phrase suivie. C'est le niveau "
             "attendu au 5 : plus de questions-réponses en mots isolés.")

    d.dialogue('Dialogue · 2 de 3', "L'étage et l'escalier", [
        ("PATRICIA", "Vous êtes à quel étage, des deux côtés ?", True),
        ("AMADOU", "Au rez-de-chaussée à Beauport, et au deuxième rue des "
                   "Peupliers. Il n'y a pas d'ascenseur, et l'escalier est en "
                   "dehors.", True),
        ("PATRICIA", "Bon à savoir. Un escalier extérieur qui tourne, ça ralentit "
                     "toujours un peu. Combien de boîtes, à peu près ?", True),
        ("AMADOU", "Une quinzaine de boîtes, un divan, un lit, une table et quatre "
                   "chaises.", True),
    ], notes="Faire remarquer qu'Amadou donne l'escalier sans qu'on le lui demande. C'est "
             "ce qui évite une mauvaise surprise le jour même.")

    d.dialogue('Dialogue · 3 de 3', "Le tarif, et ce qui s'ajoute", [
        ("PATRICIA", "Je vous mets deux hommes et un camion : c'est cent "
                     "quarante-cinq dollars de l'heure, minimum trois heures.", True),
        ("AMADOU", "Cent quarante-cinq de l'heure. Est-ce qu'il y a autre chose "
                   "qui s'ajoute ?", True),
        ("PATRICIA", "Oui, une heure de déplacement. C'est le temps que le camion "
                     "met pour sortir du garage et pour y revenir.", True),
        ("AMADOU", "Donc, si ça prend quatre heures, je paie cinq heures. Ça fait "
                   "sept cent vingt-cinq dollars.", True),
    ], notes="La question d'Amadou — « est-ce qu'il y a autre chose qui s'ajoute ? » — est "
             "la phrase la plus rentable du module. L'écrire au tableau et la faire "
             "répéter par tout le groupe.")

    d.regle("Répéter le chiffre avant de continuer",
            "« Cent quarante-cinq de l'heure. » Puis la question suivante.",
            precision="Répéter sert à deux choses : vérifier qu'on a bien entendu, et se "
                      "donner le temps d'écrire. Au téléphone, personne ne trouve ça "
                      "impoli — au contraire.",
            notes="Faire écouter à nouveau le dialogue en comptant combien de fois Amadou "
                  "répète un chiffre. Trois fois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Il reste des camions toute la journée du premier juillet.",
         "faux — le matin seulement"),
        ("Le tarif est de 145 $ l'heure pour deux hommes et un camion.", "vrai"),
        ("Le minimum est de deux heures.", "faux — trois heures"),
        ("Une heure de déplacement s'ajoute au total.", "vrai"),
        ("Un troisième homme coûte quarante-cinq dollars l'heure.", "vrai"),
        ("L'assurance de base coûte quarante-cinq dollars.",
         "faux — elle est comprise ; c'est la protection complète qui coûte 45 $"),
        ("Le dépôt de 100 $ est remboursé si on annule sept jours d'avance.", "vrai"),
    ], corrige=True,
       notes="La sixième ligne est celle qui piège : l'assurance de base est comprise, la "
             "protection complète est en plus. Y revenir en B2.")

    d.billet(
        "Écrivez les six renseignements qu'une compagnie va vous demander.",
        exemples=[
            "Deux adresses, une date, un étage, un escalier, une liste de meubles.",
            "Préparez-les avant d'appeler : l'appel dure deux fois moins longtemps.",
        ],
        notes="Devoir de préparation. Il sert directement au jeu de rôle du bloc E.")

    return d.save(dossier)
