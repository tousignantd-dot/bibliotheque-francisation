# -*- coding: utf-8 -*-
"""C1 · Au comptoir, chez Marcel.
Bloc C « Défi 2 · Commander au comptoir » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-restaurant/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Au comptoir, chez Marcel',
        chapeau="Quatorze répliques, une minute quarante. Voilà ce que dure "
                "une commande au comptoir — et c'est l'intention même que le "
                "programme donne à cette situation.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 2. C'est le cœur du module : « commander au "
                  "comptoir et comprendre l'information donnée par le préposé », en "
                  "compréhension orale comme en production orale.")

    d.objectifs([
        "suivre une commande complète du début à la fin ;",
        "repérer qui parle et à quel moment ;",
        "reconnaître les questions du préposé ;",
        "retenir un numéro de commande.",
    ])

    d.declencheur(
        'Observation', "Combien de temps ça prend, une commande ?",
        image=IMG + 'recu-numero.jpg',
        pistes=[
            "Qu'est-ce qu'il y a d'écrit sur un reçu ?",
            "À quoi sert le numéro ?",
            "Que se passe-t-il si on l'oublie ?",
            "Combien de phrases faut-il dire pour commander ?",
        ],
        notes="Faire estimer le nombre de phrases avant d'écouter le dialogue. Les "
              "élèves surestiment presque toujours : la commande réelle tient en cinq "
              "ou six phrases du client.")

    d.dialogue('Dialogue · 1 de 4', "Je voudrais un trio", [
        ("STEVE", "Bonjour ! Prochaine personne, s'il vous plaît.", True),
        ("YOLETTE", "Bonjour. Je voudrais un trio sandwich au poulet, s'il vous plaît.", True),
        ("STEVE", "Avec salade ou avec frites ?", True),
        ("YOLETTE", "Avec salade, s'il vous plaît.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="La deuxième réplique contient tout ce qui a été appris au bloc B : la "
             "formule polie, le trio, et « au poulet ». Le faire remarquer.")

    d.dialogue('Dialogue · 2 de 4', "Quel format ?", [
        ("STEVE", "Et comme breuvage ?", True),
        ("YOLETTE", "Un jus de pomme. Est-ce que je peux avoir une soupe aussi ?", True),
        ("STEVE", "Oui. Quel format ? Petit, moyen ou grand ?", True),
        ("YOLETTE", "Petit, s'il vous plaît. La soupe aux légumes.", True),
    ], notes="Le préposé pose ses questions une à la fois. Le signaler : c'est pour ça "
             "qu'il ne faut pas tout dire d'un coup au début.")

    d.dialogue('Dialogue · 3 de 4', "Pour ici ou pour emporter ?", [
        ("STEVE", "Parfait. Pour ici ou pour emporter ?", True),
        ("YOLETTE", "Pour ici.", True),
        ("STEVE", "Ça fait onze dollars et quarante. Débit ou comptant ?", True),
        ("YOLETTE", "Débit, s'il vous plaît.", True),
    ], notes="Les deux questions les plus déroutantes du module sont ici. Les faire "
             "répéter par tout le groupe avant de passer à la suite.")

    d.dialogue('Dialogue · 4 de 4', "Votre numéro est le 42", [
        ("STEVE", "Merci. Voici votre reçu. Votre numéro est le 42.", True),
        ("YOLETTE", "Le 42. Merci beaucoup.", True),
    ], notes="Yolette répète le numéro : c'est la stratégie à enseigner. Répéter un "
             "chiffre à voix haute est la façon la plus sûre de le retenir.")

    d.tableau('Analyse', "Qui parle, et pour dire quoi",
              ['Le préposé', 'Le client'],
              [["appelle la personne suivante", "salue et dit ce qu'il veut"],
               ["pose une question à la fois", "répond en deux mots"],
               ["donne le montant", "dit comment il paie"],
               ["donne le numéro", "répète le numéro"]],
              cle=0,
              note="Le client parle moins que le préposé : il répond surtout.",
              notes="Diapo à photographier. C'est la découverte de la séance et elle "
                    "rassure : commander, c'est surtout écouter et répondre court.")

    d.regle("Répéter le numéro à voix haute",
            "« — Votre numéro est le 42. — Le 42, merci. »",
            precision="Le numéro est aussi écrit sur le reçu. Le répéter sert à "
                      "deux choses : le retenir, et vérifier qu'on a bien "
                      "entendu. Dans le bruit d'un casse-croûte, l'un et "
                      "l'autre valent la peine.",
            notes="Diapo à photographier. Faire l'exercice en paires : un élève dit un "
                  "nombre entre 10 et 99, l'autre le répète. Trente secondes.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Yolette commande un trio sandwich au poulet.", "vrai"),
        ("Elle choisit les frites comme accompagnement.", "faux — la salade"),
        ("Elle prend une petite soupe aux légumes.", "vrai"),
        ("Elle emporte son repas au centre.", "faux — pour ici"),
        ("Son numéro de commande est le 42.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Écrivez la commande que vous feriez chez Marcel.",
        exemples=[
            "Commencez par « Bonjour. Je voudrais… »",
            "Quatre lignes suffisent.",
        ],
        notes="Devoir court. Il servira de point de départ à la séance C2, sur la "
              "formule polie.")

    return d.save(dossier)
