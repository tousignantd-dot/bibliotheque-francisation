# -*- coding: utf-8 -*-
"""A1 · Devant les trois laveuses — mise en situation.
Bloc A « Je découvre » · couleur teal · 75 min.
Source du module : dialogue `prep`, exercices `prVocab` et `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-achat/images/')


def build(dossier):
    d = Deck(
        code='A1', section='teal',
        titre='Devant les trois laveuses',
        chapeau="Yin vient d'emménager et il lui faut une laveuse. Trois "
                "modèles presque identiques, et un vendeur qui s'approche — "
                "avec une question qu'elle n'attendait pas.",
        duree='75 minutes')

    d.titre(notes="Ouverture du module. Question d'entrée : « qui a déjà acheté un gros "
                  "appareil ici ? ». Souvent peu de mains — et beaucoup d'appréhension.")

    d.objectifs([
        "répondre à un vendeur qui aborde ;",
        "dire l'espace dont je dispose ;",
        "demander ce qu'un chiffre veut dire, quand je n'ai pas de point de comparaison ;",
        "comparer trois modèles sur trois critères.",
    ])

    d.declencheur(
        'Mise en situation', "Vous êtes devant ces trois modèles. Que faites-vous ?",
        image=IMG + 'rayon-laveuses.jpg',
        pistes=[
            "Comment choisissez-vous entre trois appareils qui se ressemblent ?",
            "Attendez-vous qu'un vendeur vienne, ou allez-vous le chercher ?",
            "Quelle est la première chose à savoir, selon vous ?",
            "Qu'est-ce qui vous inquiète le plus dans cet achat ?",
        ],
        notes="Cinq minutes. La troisième piste est la clé : ce n'est ni le prix ni la "
              "marque, c'est l'espace. Un appareil qui n'entre pas ne sert à rien.")

    d.cartes('La situation', "Ce qu'on sait de Yin", [
        ("D'où elle vient",
         "De Chine. Elle est au Québec depuis trois ans et vient d'emménager."),
        ("Ce qu'il lui faut",
         "Une laveuse, pour un local de sous-sol d'environ un mètre de large."),
        ("Ce qu'elle ne sait pas",
         "Ce que veut dire « capacité », ni si cinquante-deux décibels c'est beaucoup."),
        ("Ce qu'elle fait de bien",
         "Elle demande. « Cinquante-deux, c'est beaucoup ou peu ? » — la question qui "
         "transforme un chiffre en information."),
    ], notes="La quatrième carte est la leçon de la séance : un chiffre sans point de "
             "comparaison ne veut rien dire.")

    d.dialogue('Dialogue · 1 de 3', "La première question du vendeur", [
        ("MARTIN", "Bonjour ! Je peux vous aider ? Vous regardez les laveuses depuis un moment.", False),
        ("YIN", "Bonjour. Oui, je cherche une laveuse, mais je ne sais pas laquelle choisir.", True),
        ("MARTIN", "Vous avez quel espace chez vous ? C'est souvent ça qui décide en premier.", True),
        ("YIN", "Un petit local, dans le sous-sol. Un mètre de large, à peu près.", True),
    ], consigne="Écoutez d'abord l'enregistrement, diapo masquée. Lisez ensuite.",
       notes="Le vendeur ne demande ni le budget ni la marque : il demande l'espace. Le "
             "faire remarquer — c'est contre-intuitif et c'est juste.")

    d.dialogue('Dialogue · 2 de 3', "Le chiffre qui élimine", [
        ("MARTIN", "Alors celle-là est trop large : elle fait soixante-seize centimètres avec la porte ouverte.", True),
        ("YIN", "Et celle-ci ?", False),
        ("MARTIN", "Soixante-huit centimètres. Elle entre partout. C'est le modèle le plus vendu, justement pour ça.", True),
        ("YIN", "Elle est bruyante ?", False),
    ], notes="« Avec la porte ouverte » : la mesure que tout le monde oublie. L'écrire au "
             "tableau et la souligner.")

    d.dialogue('Dialogue · 3 de 3', "Beaucoup ou peu ?", [
        ("MARTIN", "Non, c'est une des plus silencieuses. Cinquante-deux décibels à l'essorage.", False),
        ("YIN", "Cinquante-deux, c'est beaucoup ou peu ?", True),
        ("MARTIN", "C'est peu. Une conversation normale, c'est soixante. Vous ne l'entendrez pas de l'étage.", True),
        ("YIN", "Nous en faisons trois. Je vais regarder les deux premières de plus près.", False),
    ], notes="Le cœur de la séance. Faire répéter la question par le groupe : « c'est "
             "beaucoup ou peu ? » s'emploie pour n'importe quel chiffre.")

    d.vocabulaire('Vocabulaire · 1 de 2', "L'appareil", [
        ("un électroménager", "Un gros appareil de la maison : laveuse, réfrigérateur, cuisinière."),
        ("une laveuse", "L'appareil qui lave le linge. En France : « machine à laver »."),
        ("la capacité", "La quantité de linge ou de nourriture qui entre dedans."),
        ("les dimensions", "La hauteur, la largeur, la profondeur."),
        ("économe", "Qui consomme peu d'eau ou d'électricité."),
    ], notes="« Laveuse » et « sécheuse » sont les mots d'ici. « Machine à laver » se "
             "comprend, mais sonne étranger.")

    d.vocabulaire('Vocabulaire · 2 de 2', "Les chiffres qu'on lit", [
        ("le décibel", "L'unité du bruit. Une conversation normale : 60 dB."),
        ("le kilowattheure", "L'unité d'électricité consommée en un an."),
        ("le litre par brassée", "La consommation d'eau d'un lavage."),
        ("la garantie", "La promesse de réparer sans frais pendant une période donnée."),
        ("un spécial", "Un rabais temporaire. « Le spécial finit dimanche. »"),
    ], notes="Ces unités reviennent sur toutes les étiquettes d'énergie. Les nommer une "
             "fois suffit à les rendre lisibles.")

    d.regle("Ce qu'il faut retenir",
            "Un chiffre sans point de comparaison ne veut rien dire.",
            precision="« Cinquante-deux décibels » n'apprend rien. « Une conversation "
                      "normale, c'est soixante » transforme le chiffre en information. La "
                      "question à poser tient en cinq mots : « c'est beaucoup ou peu ? »",
            notes="Faire répéter la question par deux élèves. C'est la diapo à "
                  "photographier.")

    d.piege("Mesurer sans la porte ouverte",
            "Mon local fait un mètre, la laveuse fait soixante-seize centimètres. Ça entre.",
            "Soixante-seize centimètres, c'est avec la porte ouverte. Il faut aussi l'espace pour l'ouvrir.",
            "Une laveuse frontale a besoin de place devant elle. La largeur seule ne suffit "
            "pas : il faut le dégagement de la porte, et la largeur du passage pour amener "
            "l'appareil jusque-là.",
            notes="Beaucoup d'achats ratés viennent de là. Insister.")

    d.billet(
        "Mesurez l'espace d'un appareil chez vous et notez les trois dimensions.",
        exemples=[
            "Hauteur, largeur, profondeur — et le dégagement devant.",
            "Mesurez aussi la porte de la pièce et celle de l'immeuble.",
        ],
        notes="Devoir concret. Le dernier point surprend toujours : un appareil qui entre "
              "dans la pièce mais pas dans l'escalier repart avec le camion.")

    return d.save(dossier)
