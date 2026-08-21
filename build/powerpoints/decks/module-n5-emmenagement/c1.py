# -*- coding: utf-8 -*-
"""C1 · Le compte à mon nom.
Bloc C « Défi 2 · La nouvelle adresse » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-emmenagement/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Le compte à mon nom",
        chapeau="Une adresse, ce n'est pas une ligne sur une enveloppe : c'est "
                "une douzaine d'endroits où votre nom est écrit.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Demander qui, dans le groupe, a déjà payé "
                  "l'électricité de quelqu'un d'autre, ou reçu le courrier d'un ancien "
                  "locataire. Il y a presque toujours quelqu'un.")

    d.objectifs([
        "comprendre un appel à un service à la clientèle ;",
        "ouvrir un compte à son nom et fermer l'ancien ;",
        "donner une adresse et une date sans se faire répéter ;",
        "savoir ce qu'est un relevé de compteur.",
    ])

    d.declencheur(
        'Observation', "Le compteur est au sous-sol. Pourquoi vous demande-t-on de "
                       "le relever ?",
        image=IMG + 'compteur-electrique.jpg',
        pistes=[
            "Qui paie l'électricité avant votre arrivée ?",
            "Qui la paie après ?",
            "Comment fait-on la coupure ?",
            "Que se passe-t-il si personne ne relève rien ?",
        ],
        notes="La réponse est simple et rarement connue : le relevé sépare deux factures. "
              "Sans lui, on paie la consommation de quelqu'un d'autre.")

    d.dialogue('Dialogue · 1 de 3', "À partir de quelle date ?", [
        ("CLAUDINE", "Service à la clientèle, bonjour. Comment puis-je vous aider ?", True),
        ("AMADOU", "Bonjour. Je viens d'emménager et j'aimerais ouvrir un compte "
                   "d'électricité à mon nom.", True),
        ("CLAUDINE", "Certainement. Vous emménagez à quelle adresse, et à partir de "
                     "quelle date ?", True),
        ("AMADOU", "Au mille deux cent quatre-vingt-sept, rue des Peupliers, "
                   "appartement 4, à Québec. À partir du premier juillet.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire écrire l'adresse par le groupe pendant l'écoute. C'est un exercice de "
             "prise de notes autant qu'un dialogue.")

    d.dialogue('Dialogue · 2 de 3', "L'ancien se ferme, le nouveau s'ouvre", [
        ("CLAUDINE", "Je vous répète l'adresse : mille deux cent quatre-vingt-sept, "
                     "rue des Peupliers, appartement 4. C'est bien ça ?", True),
        ("AMADOU", "C'est bien ça.", True),
        ("CLAUDINE", "Il me faut aussi le relevé du compteur le jour de votre "
                     "entrée. Le compteur est habituellement au sous-sol.", True),
        ("AMADOU", "Je le trouverai. Est-ce que je dois faire quelque chose pour "
                   "mon ancienne adresse ?", True),
    ], notes="C'est l'agente qui répète l'adresse, pas l'élève. Faire remarquer que la "
             "vérification vient des deux côtés dans un vrai appel.")

    d.dialogue('Dialogue · 3 de 3', "Il faut prévenir bien du monde", [
        ("CLAUDINE", "Oui, et c'est le même appel : je ferme votre compte de "
                     "Beauport le trente juin, à minuit.", True),
        ("AMADOU", "Il faut que je prévienne bien du monde : la banque, l'école de "
                   "mon garçon, la SAAQ, la RAMQ.", True),
        ("CLAUDINE", "Faites-en une liste et cochez au fur et à mesure. Ceux qui "
                     "oublient la RAMQ s'en aperçoivent chez le médecin.", True),
        ("AMADOU", "Je note. Merci beaucoup, madame.", True),
    ], notes="La dernière réplique de Claudine annonce la séance C4. La reprendre "
             "textuellement en ouvrant celle-ci.")

    d.regle("Un seul appel ferme l'ancien compte et ouvre le nouveau",
            "L'ancien se ferme le 30 juin, le nouveau s'ouvre le 1er juillet.",
            precision="Beaucoup de gens font deux appels, ou n'en font qu'un et oublient "
                      "la fermeture. Résultat : deux comptes ouverts, ou la facture d'un "
                      "logement qu'on n'habite plus.",
            notes="Diapositive à photographier. Faire dire à voix haute les deux dates, "
                  "dans le bon ordre.")

    d.cartes("Ce qu'il faut avoir sous la main avant d'appeler", "Cinq minutes de préparation", [
        ("Les deux adresses",
         "L'ancienne au complet et la nouvelle, avec le numéro d'appartement."),
        ("Les deux dates",
         "Le jour où on quitte, le jour où on entre. Elles se suivent."),
        ("Le relevé de compteur",
         "Le nombre lu sur le cadran, le jour de l'entrée. Le compteur est au sous-sol."),
        ("Une pièce d'identité",
         "Nom complet, date de naissance, parfois un numéro de client existant."),
    ], notes="Faire préparer cette fiche par écrit : elle sert au jeu de rôle du bloc E "
             "et, plus tard, pour de vrai.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Amadou veut ouvrir un compte d'électricité à son nom.", "vrai"),
        ("L'agente lui répète l'adresse pour vérifier.", "vrai"),
        ("Le relevé de compteur n'est pas nécessaire.", "faux — il est demandé"),
        ("Il faudra un deuxième appel pour fermer l'ancien compte.",
         "faux — c'est le même appel"),
        ("Le réacheminement du courrier est un service de Postes Canada.", "vrai"),
        ("L'agente conseille de faire une liste et de cocher au fur et à mesure.", "vrai"),
        ("Amadou n'a personne d'autre à prévenir.",
         "faux — la banque, l'école, la SAAQ, la RAMQ"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique. Les deux « faux » du milieu "
             "sont les erreurs les plus coûteuses dans la vraie vie.")

    d.billet(
        "Écrivez votre adresse complète comme vous la diriez au téléphone.",
        exemples=[
            "Le numéro civique en toutes lettres, la rue, l'appartement, la ville.",
            "Dites-la à voix haute à quelqu'un : est-ce qu'il l'écrit correctement ?",
        ],
        notes="Le test du billet est celui de la vraie vie : une adresse mal dite est une "
              "facture qui n'arrive pas.")

    return d.save(dossier)
