# -*- coding: utf-8 -*-
"""D1 · Au comptoir de la livraison.
Bloc D « Défi 3 · Payer et faire livrer » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3caisse`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-electro/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Au comptoir de la livraison',
        chapeau="Une laveuse ne rentre pas dans un autobus. Après la caisse, "
                "il reste un comptoir, un jour à choisir, une adresse à "
                "donner et un papier à garder.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 3. Demander qui a déjà fait livrer quelque chose "
                  "ici, et comment ça s'est passé. Les récits donnent les difficultés "
                  "réelles : l'attente, l'escalier, le téléphone.")

    d.objectifs([
        "comprendre les questions du comptoir de la livraison ;",
        "choisir un jour et une plage d'heures ;",
        "donner son adresse et son numéro de téléphone ;",
        "comprendre à quoi sert le bon de livraison.",
    ])

    d.declencheur(
        'Observation', "Comment l'appareil arrive-t-il chez vous ?",
        image=IMG + 'camion-livraison.jpg',
        pistes=[
            "Qui a une auto assez grande pour une laveuse ?",
            "Combien coûte une livraison, à votre avis ?",
            "Qui monte l'appareil dans l'escalier ?",
            "Qu'est-ce qu'on fait de l'ancien appareil ?",
        ],
        notes="Les quatre questions sont celles qu'il faut poser au comptoir. Les "
              "laisser sortir du groupe plutôt que de les donner.")

    d.dialogue('Dialogue · 1 de 3', "Jeudi ou samedi", [
        ("RACHID", "Bonjour. Vous avez payé à la caisse ?", True),
        ("MARISOL", "Oui. Voici le reçu.", True),
        ("RACHID", "Merci. Une laveuse Norlac. Vous voulez la livraison ?", True),
        ("MARISOL", "Oui, s'il vous plaît. Je n'ai pas d'auto.", True),
        ("RACHID", "La livraison coûte soixante dollars. On peut passer jeudi ou samedi.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La livraison se paie et se demande : elle n'est jamais automatique. Le "
             "faire remarquer, c'est éviter une attente inutile à la maison.")

    d.dialogue('Dialogue · 2 de 3', "Votre adresse", [
        ("MARISOL", "Samedi, c'est mieux. Je travaille jeudi.", True),
        ("RACHID", "Samedi, entre huit heures et midi. Votre adresse ?", True),
        ("MARISOL", "2140, rue des Trembles, appartement 3, à Saint-Hubert.", True),
        ("RACHID", "Et un numéro de téléphone ?", True),
        ("MARISOL", "555 0148.", True),
    ], notes="Faire remarquer l'ordre de l'adresse : le numéro, la rue, l'appartement, "
             "la ville. Faire dire son adresse à chaque élève, à voix haute.")

    d.dialogue('Dialogue · 3 de 3', "Gardez votre bon", [
        ("RACHID", "Parfait. Voici votre bon de livraison. Gardez-le : le camion va le demander.", True),
        ("MARISOL", "Est-ce que vous emportez la vieille laveuse ?", True),
        ("RACHID", "Oui, si vous la mettez près de la porte. C'est gratuit.", True),
        ("MARISOL", "Merci beaucoup. À samedi.", True),
    ], notes="Marisol pose la question du vieil appareil : personne ne la lui a "
             "proposée. C'est l'habitude à installer — demander ce qui n'est pas dit.")

    d.tableau('Analyse', "Ce que le comptoir demande",
              ['On vous demande', 'Vous donnez'],
              [["Vous voulez la livraison ?", "oui ou non, et pourquoi"],
               ["Quel jour ?", "un jour de la semaine"],
               ["Votre adresse ?", "numéro, rue, appartement, ville"],
               ["Un numéro de téléphone ?", "dix chiffres, lentement"]],
              cle=0,
              note="Quatre questions, quatre réponses courtes. Rien de plus.",
              notes="Diapo à photographier. Faire jouer l'échange deux par deux, une "
                    "fois chacun.")

    d.regle("Demander ce qui n'est pas dit",
            "« Est-ce que vous emportez la vieille laveuse ? »",
            precision="Beaucoup de magasins reprennent l'ancien appareil sans "
                      "rien charger, mais ne le proposent pas. Une question "
                      "évite d'avoir à s'en débarrasser soi-même.",
            notes="Diapo à photographier. C'est la même stratégie qu'en C3 : le vendeur "
                  "répond, il n'annonce pas.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Marisol a payé avant d'aller au comptoir.", "vrai"),
        ("La livraison est gratuite.", "faux — soixante dollars"),
        ("Le camion peut passer jeudi ou samedi.", "vrai"),
        ("Le bon de livraison se jette tout de suite.", "faux — le camion va le demander"),
        ("Le magasin emporte la vieille laveuse sans rien charger.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.pratique('Vocabulaire', "Qu'est-ce que ça veut dire ?",
               "Associez chaque phrase à son sens.", [
        ("« Débit ou crédit ? »", "on vous demande comment payer"),
        ("« Livraison en sus. »", "la livraison coûte en plus du prix"),
        ("« Gardez votre bon. »", "ce papier sert le jour du camion"),
        ("« On passe entre huit heures et midi. »", "il faut être là tout l'avant-midi"),
    ], corrige=True,
       notes="Ces quatre phrases sont celles qu'on entend vraiment. Les faire répéter "
             "avec l'intonation du comptoir.")

    d.billet(
        "Écrivez votre adresse complète et votre numéro de téléphone.",
        exemples=[
            "Numéro, rue, appartement, ville.",
            "Exercez-vous à les dire à voix haute, lentement.",
        ],
        notes="Devoir simple mais essentiel : beaucoup d'élèves hésitent sur l'ordre des "
              "éléments et sur la lecture des chiffres du téléphone.")

    return d.save(dossier)
