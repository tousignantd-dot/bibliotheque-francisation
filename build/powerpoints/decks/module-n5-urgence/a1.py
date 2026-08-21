# -*- coding: utf-8 -*-
"""A1 · « Ce n'est rien, une grippe. »
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-urgence/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="« Ce n'est rien, une grippe. »",
        chapeau="Amparo a soixante et onze ans, elle fait de la fièvre "
                "depuis deux jours et elle répète que ce n'est rien. Sa "
                "fille Marisol hésite entre déranger l'hôpital et attendre "
                "demain. Il existe un numéro pour cette hésitation-là.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : la nuit, "
                  "quand quelqu'un ne va pas bien chez vous, qui appelez-vous ? Les "
                  "réponses vont de « personne » à « le 9-1-1 tout de suite », et l'écart "
                  "dit ce que le module va travailler. Ne juger aucune réponse.")

    d.objectifs([
        "décrire au téléphone l'état de quelqu'un d'autre ;",
        "comprendre les questions d'une infirmière d'Info-Santé ;",
        "savoir ce que le 8-1-1 fait et ce qu'il ne fait pas ;",
        "retenir les signes qui font composer le 9-1-1 sans rappeler.",
    ])

    d.declencheur(
        'Observation', "Trente-huit et six, deux jours de suite, chez une personne de "
                       "soixante et onze ans. On appelle ? Qui ?",
        image=IMG + 'thermometre.jpg',
        pistes=[
            "Est-ce que c'est grave ? Qui peut le dire ?",
            "Qu'est-ce qui empêche d'appeler quelqu'un, la nuit ?",
            "Que se passe-t-il si on attend jusqu'à demain matin ?",
            "Connaissez-vous un numéro entre « rien » et « l'ambulance » ?",
        ],
        notes="La dernière piste est la vraie question de la séance. Compter les mains "
              "levées à « connaissez-vous le 8-1-1 ? » : dans la plupart des groupes, "
              "moins de la moitié. C'est le service le plus utile et le moins connu.")

    d.dialogue('Dialogue · 1 de 3', "« Ne va pas déranger l'hôpital »", [
        ("MARISOL", "Maman, tu as encore de la fièvre. Trente-huit et six.", True),
        ("AMPARO", "Ce n'est rien, ma fille. Une grippe. Ça va passer.", True),
        ("MARISOL", "Ça fait deux jours. Et tu manges deux cuillerées de soupe "
                    "par repas.", True),
        ("AMPARO", "Je n'ai pas faim, c'est tout. Ne va pas déranger l'hôpital "
                   "pour une grippe.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="« Ne va pas déranger » revient dans presque tous les groupes. Demander qui "
             "a déjà entendu cette phrase à la maison — beaucoup de mains. C'est le "
             "premier obstacle du module, et il n'est pas linguistique.")

    d.dialogue('Dialogue · 2 de 3', "Ce que fait une infirmière au téléphone", [
        ("MARISOL", "Je ne parle pas de l'hôpital. Je parle du huit un un.", True),
        ("AMPARO", "Qu'est-ce que c'est encore, ça ?", True),
        ("MARISOL", "Une infirmière au téléphone. C'est gratuit, c'est ouvert jour "
                    "et nuit, et elle nous dira si ça peut attendre.", True),
        ("AMPARO", "Et elle va me donner un médicament par le téléphone ?", True),
    ], notes="Répondre à la question d'Amparo avec le groupe avant d'écouter la suite : "
             "non, l'infirmière ne prescrit rien. Ce n'est pas un manque du service, "
             "c'est sa définition.")

    d.dialogue('Dialogue · 3 de 3', "Les quatre signes à retenir", [
        ("PATRICK", "Écoutez-moi bien, c'est le plus important de l'appel. Vous "
                    "composez le neuf un un tout de suite, sans me rappeler, si elle "
                    "perd connaissance, si elle a de la difficulté à respirer, si "
                    "elle devient confuse, ou si elle tombe et qu'elle ne peut plus "
                    "se relever.", True),
        ("MARISOL", "Perdre connaissance, respirer mal, devenir confuse, tomber. "
                    "C'est bien ça ?", True),
        ("PATRICK", "C'est exactement ça. Le huit un un pour un doute, le neuf un un "
                    "pour ce qui ne peut pas attendre dix minutes.", False),
    ], notes="Faire remarquer que Marisol répète la liste. C'est le geste à copier : "
             "cette liste sert la nuit suivante, quand on est fatigué et inquiet.")

    d.regle("Le 8-1-1 pour un doute, le 9-1-1 pour ce qui ne peut pas attendre",
            "Une seule question tranche : est-ce que ça peut attendre dix minutes ?",
            precision="Le 8-1-1 est gratuit, ouvert jour et nuit, toute l'année, et on "
                      "peut appeler pour quelqu'un d'autre. Dans le doute entre les deux "
                      "numéros, on compose le 9-1-1 : personne ne reprochera d'avoir "
                      "appelé.",
            notes="Diapositive à photographier. C'est le savoir le plus utile du module, "
                  "et il tient en une phrase.")

    d.cartes("Ce que fait le 8-1-1", "Et ce qu'il ne fait pas", [
        ("Une infirmière, pas un médecin",
         "Elle écoute, elle pose des questions, elle dit où aller et quand."),
        ("Gratuit, jour et nuit",
         "Vingt-quatre heures sur vingt-quatre, toute l'année, partout au Québec."),
        ("Pour soi ou pour un proche",
         "Aucun médecin de famille n'est nécessaire pour y avoir droit."),
        ("Ni diagnostic ni ordonnance",
         "Elle ne nomme pas la maladie et ne prescrit aucun médicament."),
    ], notes="La quatrième carte évite la déception la plus fréquente : on n'appelle pas "
             "le 8-1-1 pour obtenir un traitement, mais pour savoir où aller.")

    d.tableau('Le bon numéro', "Cinq situations, une décision",
              ['La situation', 'Le numéro'],
              [["Une fièvre qui dure depuis deux jours", "8-1-1"],
               ["Une personne tombée qui ne se relève pas", "9-1-1"],
               ["Un comprimé pris deux fois par erreur", "8-1-1"],
               ["Une douleur à la poitrine depuis dix minutes", "9-1-1"],
               ["Je ne sais pas si c'est grave", "8-1-1 — et 9-1-1 si ça presse"]],
              cle=0,
              notes="Faire ajouter deux situations par le groupe et les faire classer. "
                    "C'est là que sortent les vraies hésitations, et souvent la peur du "
                    "coût de l'ambulance : la garder pour la séance A4.")

    d.piege("Décider soi-même que ce n'est rien",
            "Ne va pas déranger l'hôpital pour une grippe.",
            "Je ne dérange personne : le 8-1-1 existe pour cette question-là.",
            "Le service est fait pour les gens qui ne sont pas soignants. Appeler pour "
            "rien n'existe pas ; ne pas appeler quand il le fallait, oui.",
            notes="Amparo dit cette phrase mot pour mot. La faire retrouver dans le "
                  "dialogue, puis demander qui l'a déjà dite lui-même.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Amparo fait de la fièvre depuis deux jours.", "vrai"),
        ("Marisol veut emmener sa mère à l'hôpital tout de suite.", "faux — elle appelle le 8-1-1"),
        ("L'appel au 8-1-1 coûte quelques dollars.", "faux — il est gratuit"),
        ("L'infirmier demande comment la température a été prise.", "vrai"),
        ("Il prescrit un médicament au téléphone.", "faux — ce n'est pas son rôle"),
        ("Si Amparo perd connaissance, il faut d'abord rappeler le 8-1-1.", "faux — le 9-1-1, sans rappeler"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Écrivez les quatre signes qui font composer le 9-1-1 sans rappeler.",
        exemples=[
            "De mémoire d'abord, puis vérifiez dans le dialogue.",
            "Ajoutez en une phrase pourquoi celui-là ne peut pas attendre.",
        ],
        notes="Le billet sert de vérification de fin de séance. Le relire au début de A4, "
              "où la liste passera de quatre signes à cinq.")

    return d.save(dossier)
