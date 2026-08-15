# -*- coding: utf-8 -*-
"""A4 · Décider selon la météo.
Bloc A · couleur acier (compréhension et décision) · 60 min.
Source : exercice `aMeteo` — planifier une journée de travail extérieur.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='acier',
        titre='Décider selon la météo',
        chapeau="Écouter le bulletin ne sert à rien si on ne sait pas quoi en faire. "
                "Cette séance transforme une prévision en décision : on y va, on "
                "attend, ou on fait autre chose.",
        duree='60 minutes')

    d.titre(notes="Séance de mise en application. Demander d'entrée qui prend une "
                  "décision à cause de la météo, dans son travail ou sa vie. Presque "
                  "tout le monde.")

    d.objectifs([
        "traduire une prévision en décision concrète ;",
        "nommer les conditions qui rendent un travail dangereux ;",
        "savoir où vérifier avant de partir ;",
        "proposer une solution de rechange.",
    ])

    d.tableau('Analyse', "Quatre conditions et leur effet sur le travail",
              ['La condition', 'Ce qu\'elle empêche'],
              [["rafales de plus de 40 km/h", "tout travail en hauteur"],
               ["surface glacée", "monter sur un toit ou une échelle"],
               ["visibilité réduite", "conduire et manœuvrer de la machinerie"],
               ["froid ressenti sous moins 27", "rester dehors plus de trente minutes"]],
              cle=0, props=[0.4, 0.6],
              notes="Ces quatre conditions couvrent la grande majorité des annulations. "
                    "Les faire copier dans le cahier.")

    d.regle('La règle de la décision',
            "On regarde la condition, on cite la règle, on propose autre chose.",
            precision="« Les rafales dépassent quarante » — la condition. « Personne ne "
                      "monte » — la règle. « On rentre préparer le bardeau » — la "
                      "solution. Trois phrases, et la journée est réglée.",
            notes="C'est exactement la structure du dialogue de A1. Le faire remarquer : "
                  "Josée fait les trois en dix secondes.")

    d.cartes('Analyse', "Où vérifier avant de partir", [
        ("Le bulletin météo",
         "À la radio à l'heure juste, ou sur une application. Il donne les conditions "
         "générales de la région."),
        ("Les avertissements routiers",
         "Le site du ministère des Transports donne l'état de chaque autoroute. C'est "
         "plus précis que la météo pour la conduite."),
        ("La caméra routière",
         "Beaucoup de routes ont des caméras en direct. On voit la chaussée telle "
         "qu'elle est, pas telle qu'elle est prévue."),
        ("Le collègue déjà sur place",
         "Un appel de trente secondes vaut mieux que trois sites : quelqu'un qui est "
         "dehors sait ce qu'il en est."),
    ], notes="La quatrième carte est celle que les élèves emploient déjà. La valoriser : "
             "ce n'est pas moins sérieux que les trois autres.")

    d.pratique('Pratique · 1 de 4', "Peut-on travailler dehors ?",
               "Répondez oui ou non, et donnez la raison.", [
        ("Rafales de 60 km/h, ciel dégagé.", "non — au-dessus de 40, pas de travail en hauteur"),
        ("Moins dix degrés, vent faible, pas de précipitations.", "oui — conditions normales"),
        ("Pluie verglaçante en cours, mercure autour de zéro.", "non — surfaces glacées"),
        ("Poudrerie, visibilité à 200 mètres.", "non pour conduire, oui pour l'atelier"),
        ("Moins vingt-cinq, facteur éolien à moins trente-huit.", "non — froid ressenti trop bas"),
    ], corrige=True,
       notes="Le quatrième item est le plus intéressant : la réponse dépend de la tâche. "
             "Le faire remarquer.")

    d.pratique('Pratique · 2 de 4', "Nommez la condition dangereuse",
               "Deux conditions par situation.", [
        ("Un travail sur un toit en janvier.", "les rafales et la surface glacée"),
        ("Un déplacement en camionnette sur l'autoroute.",
         "la visibilité et la chaussée glissante"),
        ("Un travail au sol toute la journée en février.",
         "le froid ressenti et le temps d'exposition"),
        ("Un déchargement de camion à l'extérieur.", "le vent et la glace au sol"),
    ], corrige=True,
       notes="Faire chercher les conditions avant de donner les réponses. Le groupe en "
             "trouvera souvent plus de deux.")

    d.piege("Le piège de la prévision de la veille",
            "J'ai écouté le bulletin hier soir, ça devrait aller.",
            "Je vérifie le matin même, avant de partir.",
            "Une prévision faite douze heures à l'avance change souvent. Le verglas "
            "arrive plus tôt ou plus tard, le vent tourne, la température reste au-dessus "
            "de zéro. Le bulletin du matin est le seul qui compte pour la journée.",
            notes="Faire le lien avec le dialogue de A1 : Josée décide la veille, mais "
                  "elle prévoit de remonter si les conditions changent.")

    d.pratique('Pratique · 3 de 4', "Proposez une solution de rechange",
               "La journée dehors est annulée. Que fait-on ?", [
        ("Une équipe de couvreurs", "préparer le matériel, entretenir les outils à l'atelier"),
        ("Une équipe de paysagement", "réparer l'équipement, planifier les chantiers"),
        ("Une livraison en camion", "reporter à l'après-midi, prévenir les clients"),
        ("Un chantier de construction", "travailler à l'intérieur du bâtiment"),
    ], corrige=True,
       notes="Faire chercher des solutions dans les métiers réels du groupe. C'est plus "
             "utile que les exemples du cours.")

    d.pratique('Pratique · 4 de 4', "Six questions de planification",
               "Répondez comme si vous planifiiez une journée avec un collègue.", [
        ("Pourrait-on travailler dehors demain, selon les prévisions ?",
         "réponse justifiée par une condition"),
        ("Nommez deux conditions qui rendent un travail en hauteur dangereux.",
         "les rafales fortes et la glace sur les surfaces"),
        ("Comment savez-vous, le matin, si la route sera praticable ?",
         "le bulletin et les avertissements routiers"),
        ("Que feriez-vous si de la pluie verglaçante commençait en plein chantier ?",
         "descendre tout de suite et attendre à l'intérieur"),
        ("Quelle tâche à l'intérieur pourrait remplacer une journée annulée ?",
         "préparer le matériel ou entretenir les outils"),
        ("À quel moment de l'année la météo dérange-t-elle le plus votre travail ?",
         "réponse personnelle"),
    ], corrige=True,
       notes="La dernière question est personnelle : la laisser ouverte et faire circuler "
             "les réponses. Elles varient beaucoup selon les métiers.")

    d.billet(
        "Décrivez une journée où la météo a changé vos plans.",
        exemples=[
            "Trois phrases : la condition, la décision, ce que vous avez fait à la place.",
            "Au travail, à l'école, ou dans votre vie personnelle.",
        ],
        notes="Ramasser. Ces récits serviront en B5, où l'on expliquera une décision à "
              "voix haute.")

    return d.save(dossier)
