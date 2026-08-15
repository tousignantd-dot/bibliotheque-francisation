# -*- coding: utf-8 -*-
"""B1 · Le bulletin de six heures.
Bloc B · couleur acier (compréhension orale) · 75 min.
Source : bulletin `t1`, exercices `t1bulletin` et `t1semaine`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Le bulletin de six heures',
        chapeau="Six phrases, douze informations, et toute la journée décidée. Un "
                "bulletin météo est le texte le plus dense qu'on écoute chaque matin.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Prévenir : on écoutera trois fois, avec une "
                  "consigne différente chaque fois. C'est la seule façon de tenir cette "
                  "densité.")

    d.objectifs([
        "suivre un bulletin météo dans l'ordre du temps ;",
        "relever les chiffres : degrés, kilomètres à l'heure, centimètres ;",
        "distinguer ce qui se passe maintenant de ce qui est prévu ;",
        "en tirer une décision de travail.",
    ])

    d.regle("Comment un bulletin est construit",
            "Maintenant · l'avant-midi · l'après-midi · le soir · demain.",
            precision="Toujours dans cet ordre. Sachant cela, on peut écouter en "
                      "cherchant seulement le moment qui nous intéresse : celui où l'on "
                      "doit sortir.",
            notes="Écrire les cinq moments au tableau. C'est la grille d'écoute des trois "
                  "passages.")

    d.dialogue('Bulletin · 1 de 3', "Il est six heures", [
        ("LE MÉTÉOROLOGUE", "Il est six heures. Voici le bulletin spécial pour la "
                            "Montérégie : une pluie verglaçante recouvre déjà les routes "
                            "de la Rive-Sud.", True),
        ("LE MÉTÉOROLOGUE", "Le mercure se maintiendra autour de zéro degré jusqu'au "
                            "milieu de l'avant-midi, ce qui gardera la chaussée "
                            "glissante.", True),
    ], consigne="Première écoute : cherchez seulement ce qui se passe MAINTENANT.",
       notes="Passer l'audio du défi 1. Le mot « déjà » est la clé : il dit que le "
             "phénomène est en cours, pas prévu.")

    d.dialogue('Bulletin · 2 de 3', "Des rafales dès neuf heures", [
        ("LE MÉTÉOROLOGUE", "Des rafales de soixante kilomètres à l'heure balaieront la "
                            "région dès neuf heures, et la poudrerie réduira la "
                            "visibilité par moments.", True),
        ("LE MÉTÉOROLOGUE", "En après-midi, le vent tombera et le mercure descendra à "
                            "moins six degrés : la pluie verglaçante se changera alors "
                            "en neige.", True),
    ], consigne="Deuxième écoute : relevez tous les CHIFFRES.",
       notes="Cinq chiffres dans ces deux phrases : soixante, neuf heures, moins six. "
             "Faire noter chacun avec son unité.")

    d.dialogue('Bulletin · 3 de 3', "Demain samedi", [
        ("LE MÉTÉOROLOGUE", "Deux à quatre centimètres d'accumulation sont attendus "
                            "avant la fin de la soirée.", True),
        ("LE MÉTÉOROLOGUE", "Demain samedi, le ciel se dégagera et le vent sera faible : "
                            "une journée idéale pour les travaux en hauteur.", True),
    ], consigne="Troisième écoute : cherchez ce qui est prévu pour DEMAIN.",
       notes="La dernière phrase donne la décision : samedi, on monte. C'est ce que "
             "l'équipe attendait.")

    d.tableau('Analyse', "Le bulletin, heure par heure",
              ['Le moment', 'Ce qui est annoncé'],
              [["maintenant, 6 h", "pluie verglaçante sur les routes"],
               ["jusqu'au milieu de l'avant-midi", "mercure autour de zéro, chaussée glissante"],
               ["dès 9 h", "rafales de 60 km/h, poudrerie"],
               ["en après-midi", "le vent tombe, moins six, la pluie devient neige"],
               ["avant la fin de la soirée", "2 à 4 cm d'accumulation"],
               ["demain samedi", "ciel dégagé, vent faible"]],
              cle=0, props=[0.35, 0.65],
              notes="Six moments, six annonces. Faire remplir ce tableau par les élèves "
                    "pendant la troisième écoute, avant de l'afficher.")

    d.pratique('Pratique · 1 de 4', "Six questions sur le bulletin",
               "Répondez d'après vos notes.", [
        ("Quelle région ce bulletin concerne-t-il ?", "la Montérégie, sur la Rive-Sud"),
        ("Qu'est-ce qui recouvre déjà les routes ?", "de la pluie verglaçante"),
        ("Pourquoi la chaussée restera-t-elle glissante en avant-midi ?",
         "parce que le mercure se maintiendra autour de zéro"),
        ("À partir de quelle heure les rafales, et à quelle vitesse ?",
         "dès neuf heures, à 60 km/h"),
        ("Qu'est-ce qui réduira la visibilité ?", "la poudrerie"),
        ("Pourquoi samedi convient-il aux travaux en hauteur ?",
         "le ciel se dégagera et le vent sera faible"),
    ], corrige=True,
       notes="La troisième question demande une cause : c'est la plus difficile. Faire "
             "chercher le mot « ce qui » dans le texte.")

    d.pratique('Pratique · 2 de 4', "Les chiffres et leurs unités",
               "Chaque chiffre a une unité. Laquelle ?", [
        ("60", "kilomètres à l'heure — la vitesse du vent"),
        ("moins 6", "degrés — la température de l'après-midi"),
        ("2 à 4", "centimètres — l'accumulation de neige"),
        ("9", "heures — le début des rafales"),
        ("0", "degré — la température de l'avant-midi"),
    ], corrige=True,
       notes="Un chiffre sans unité ne veut rien dire. C'est l'erreur de prise de notes "
             "la plus fréquente : le signaler.")

    d.pratique('Pratique · 3 de 4', "Vrai ou faux",
               "D'après le bulletin.", [
        ("La pluie verglaçante tombe déjà au moment du bulletin.", "VRAI"),
        ("Le vent soufflera plus fort en après-midi qu'en avant-midi.",
         "FAUX — le vent tombera en après-midi"),
        ("La poudrerie nuira à la visibilité.", "VRAI"),
        ("Il tombera plus de dix centimètres de neige.", "FAUX — deux à quatre"),
        ("Samedi sera une journée favorable au travail sur les toits.", "VRAI"),
    ], corrige=True,
       notes="Le deuxième énoncé inverse le sens : « le vent tombera » veut dire qu'il "
             "diminue. C'est une expression, pas une chute.")

    d.piege("Le piège du « le vent tombe »",
            "« Le vent tombera » veut dire qu'il va y avoir plus de vent.",
            "« Tomber » veut dire ici diminuer, s'apaiser.",
            "Dans un bulletin météo, « le vent tombe » signifie qu'il faiblit. C'est une "
            "expression figée, et elle dit exactement le contraire de ce que le verbe "
            "laisse croire. Elle décide pourtant de la reprise du travail.",
            notes="Faire chercher d'autres expressions du bulletin : « le mercure "
                  "descend », « le ciel se dégage », « la neige s'accumule ».")

    d.pratique('Pratique · 4 de 4', "Prenez la décision",
               "D'après le bulletin, que fait l'équipe ?", [
        ("Ce matin, sur le toit ?", "non — pluie verglaçante et rafales à 60"),
        ("Ce matin, à l'atelier ?", "oui — travail intérieur possible"),
        ("Cet après-midi, sur le toit ?", "non — la neige commence et il fait moins six"),
        ("Demain samedi, sur le toit ?", "oui — ciel dégagé, vent faible"),
    ], corrige=True,
       notes="C'est le but de tout le module : transformer un bulletin en décision. Faire "
             "justifier chaque réponse par une phrase du bulletin.")

    d.billet(
        "Écoutez le bulletin de demain matin et notez-en cinq informations.",
        exemples=[
            "Le moment, le phénomène, le chiffre et son unité.",
            "Ajoutez une phrase : que feriez-vous de votre journée ?",
        ],
        notes="Ramasser à la séance suivante. C'est un devoir court et il ancre "
              "l'habitude d'écouter le bulletin.")

    return d.save(dossier)
