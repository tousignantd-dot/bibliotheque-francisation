# -*- coding: utf-8 -*-
"""A1 · Excusez-moi, je cherche… — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab` et `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-deplacement/images/')


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Excusez-moi, je cherche…',
        chapeau="Nour est arrivée de Syrie il y a huit mois. Elle a un "
                "rendez-vous au 340, rue Sainte-Hélène, et elle vient de "
                "descendre au mauvais coin de rue.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module. Commencer par une question au groupe : « qui s'est "
                  "déjà perdu en ville depuis son arrivée ? ». Presque toutes les mains se "
                  "lèvent — c'est le bon départ.")

    d.objectifs([
        "arrêter quelqu'un poliment dans la rue pour demander mon chemin ;",
        "comprendre un itinéraire donné à l'oral, du premier coup ;",
        "répéter ce qu'on m'a dit pour vérifier que j'ai bien compris ;",
        "nommer les repères de la rue : le coin, le feu, le trottoir.",
    ], notes="Le troisième objectif est le plus important du module. Y revenir souvent.")

    d.declencheur(
        'Mise en situation', "Vous êtes ici. Que faites-vous ?",
        image=IMG + 'coin.jpg',
        pistes=[
            "Vous cherchez une adresse et vous ne savez pas où aller. Qui arrêtez-vous ?",
            "Comment commencez-vous la phrase ?",
            "Que faites-vous si vous ne comprenez pas la réponse ?",
            "Est-ce impoli de faire répéter ? Pourquoi ?",
        ],
        notes="Cinq minutes en grand groupe. Beaucoup diront qu'ils préfèrent chercher "
              "seuls plutôt que de demander. Nommer cette gêne : elle coûte du temps et "
              "elle n'a pas lieu d'être.")

    d.cartes('La situation', "Ce qu'on sait de Nour", [
        ("D'où elle vient",
         "De Syrie. Elle est au Québec depuis huit mois."),
        ("Où elle doit aller",
         "Au 340, rue Sainte-Hélène. Elle a un rendez-vous et elle n'est jamais allée "
         "dans ce quartier."),
        ("Ce qui s'est passé",
         "Elle est descendue de l'autobus au mauvais coin de rue. Ça arrive à tout le "
         "monde, y compris aux gens d'ici."),
        ("Ce qu'elle fait de bien",
         "Elle arrête quelqu'un tout de suite, et surtout : elle répète l'itinéraire à la "
         "fin pour vérifier. C'est ce qui la sauve."),
    ], notes="La quatrième carte est la leçon de la séance. La souligner dès maintenant.")

    d.dialogue('Dialogue · 1 de 3', "La première phrase", [
        ("NOUR", "Excusez-moi, madame. Je cherche la rue Sainte-Hélène. C'est loin d'ici ?", True),
        ("MARIE-JOSÉE", "Sainte-Hélène… Non, c'est à dix minutes à pied. Vous êtes à pied ou en autobus ?", False),
        ("NOUR", "À pied. Je suis descendue de l'autobus au coin, là-bas.", False),
        ("MARIE-JOSÉE", "D'accord. Continuez tout droit jusqu'au feu, puis tournez à gauche sur Chambly.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="La première réplique est la formule complète : « Excusez-moi » + « je "
             "cherche » + le nom du lieu. La faire répéter par tout le groupe, deux fois.")

    d.dialogue('Dialogue · 2 de 3', "Les repères en chemin", [
        ("NOUR", "Jusqu'au feu, puis à gauche. Et après ?", True),
        ("MARIE-JOSÉE", "Après, marchez deux coins de rue. Vous allez passer devant une pharmacie et une caisse.", False),
        ("NOUR", "Une pharmacie et une caisse. D'accord.", True),
        ("MARIE-JOSÉE", "Sainte-Hélène est la rue juste après la caisse. Ne la manquez pas, elle est petite.", False),
    ], notes="Nour répète deux fois : « jusqu'au feu, puis à gauche » et « une pharmacie et "
             "une caisse ». C'est une technique, pas une hésitation. Le dire au groupe.")

    d.dialogue('Dialogue · 3 de 3', "Vérifier avant de partir", [
        ("NOUR", "Et le numéro 340, il est de quel côté ?", False),
        ("MARIE-JOSÉE", "Les numéros pairs sont du côté droit. Le 340 devrait être à votre droite.", True),
        ("NOUR", "Merci beaucoup. Alors : tout droit jusqu'au feu, à gauche, deux coins de rue, après la caisse.", True),
        ("MARIE-JOSÉE", "C'est exactement ça. Vous avez bien écouté.", False),
    ], notes="Le cœur de la séance : Nour redit tout l'itinéraire en une phrase. Faire faire "
             "la même chose à un élève, sans regarder la diapo.")

    d.vocabulaire('Vocabulaire · 1 de 2', "Les repères de la rue", [
        ("un coin de rue", "L'endroit où deux rues se croisent."),
        ("un feu de circulation", "Le signal lumineux rouge, jaune et vert."),
        ("un trottoir", "La partie de la rue réservée aux piétons."),
        ("traverser", "Passer d'un côté à l'autre d'une rue ou d'un parc."),
        ("en face de", "De l'autre côté, vis-à-vis."),
    ], notes="« Deux coins de rue » est une mesure de distance très employée ici. "
             "L'expliquer : ce n'est pas deux mètres, c'est deux intersections.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Lire une adresse", [
        ("le numéro civique", "Le nombre écrit avant le nom de la rue : 340, rue Sainte-Hélène."),
        ("un numéro pair", "2, 4, 340 — tous du même côté de la rue."),
        ("un numéro impair", "1, 3, 341 — de l'autre côté."),
        ("un appartement", "S'écrit après l'adresse : 340, rue Sainte-Hélène, app. 4."),
        ("une intersection", "Le mot officiel pour un coin de rue, sur les panneaux."),
    ], notes="L'ordre numéro-puis-rue surprend beaucoup d'élèves : dans plusieurs pays, "
             "c'est l'inverse. Faire écrire leur propre adresse au tableau.")

    d.regle("Ce qu'il faut retenir",
            "Répétez l'itinéraire à voix haute avant de partir. Toujours.",
            precision="C'est ce que fait Nour, et c'est pour ça qu'elle arrive. Répéter "
                      "n'est pas un signe qu'on a mal compris : c'est ce que font tous les "
                      "gens qui reçoivent une information importante, dans toutes les "
                      "langues.",
            notes="Faire répéter la phrase de la carte blanche par deux élèves. C'est la "
                  "diapo à photographier.")

    d.piege('Demander son chemin',
            "Où est la rue Sainte-Hélène ?",
            "Excusez-moi, madame. Je cherche la rue Sainte-Hélène.",
            "La question de gauche est correcte, mais elle arrive sans prévenir. « "
            "Excusez-moi » donne à l'autre personne une seconde pour s'arrêter et vous "
            "écouter. Sans ce mot, la moitié de votre phrase se perd.",
            notes="Ne pas présenter la gauche comme une faute de langue : c'est une "
                  "question d'efficacité, pas de grammaire.")

    d.billet(
        "Écrivez la phrase que vous emploierez la prochaine fois que vous chercherez une adresse.",
        exemples=[
            "Commencez par « Excusez-moi ».",
            "Nommez précisément ce que vous cherchez : une rue, un numéro, un édifice.",
        ],
        notes="Ramasser. Les meilleures formules serviront au jeu de rôle de E1.")

    return d.save(dossier)
