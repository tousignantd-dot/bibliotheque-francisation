# -*- coding: utf-8 -*-
"""A1 · Je cherche un manteau.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-vetements/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Je cherche un manteau',
        chapeau="Le premier hiver est celui où l'on découvre qu'un manteau "
                "n'est pas un manteau : il y en a pour l'automne, pour "
                "janvier, avec ou sans capuchon. Avant de choisir, il faut "
                "savoir nommer.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander d'abord au groupe qui a déjà acheté "
                  "du linge d'hiver ici, et ce qui a été difficile. Les réponses ouvrent "
                  "la séance et donnent des exemples réels pour toute la semaine.")

    d.objectifs([
        "nommer les vêtements de l'hiver ;",
        "dire une couleur et un motif : pâle, foncé, uni, rayé ;",
        "comprendre les questions d'une conseillère ;",
        "demander ce que veut dire un mot qu'on ne connaît pas.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'il faut, pour passer un hiver ici ?",
        image=IMG + 'manteaux-suspendus.jpg',
        pistes=[
            "Combien de vêtements différents ?",
            "Lesquels ne se trouvent pas dans votre pays ?",
            "Lesquels sont les plus chers ?",
            "Par lequel commenceriez-vous ?",
        ],
        notes="Laisser venir les mots dans n'importe quelle langue, puis les traduire "
              "ensemble au tableau. C'est la liste de vocabulaire du module qui se "
              "construit toute seule.")

    d.dialogue('Dialogue · 1 de 3', "Pour quelle saison ?", [
        ("FARIDA", "Bonjour, madame. Je cherche un manteau.", True),
        ("JOCELYNE", "Bonjour ! Un manteau pour l'automne ou pour l'hiver ?", True),
        ("FARIDA", "Pour l'hiver. C'est mon premier hiver ici.", True),
        ("JOCELYNE", "Ah, bienvenue ! Alors il vous faut un manteau chaud.", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Farida dit ce qu'elle cherche en quatre mots. C'est assez : la conseillère "
             "pose les questions suivantes elle-même.")

    d.dialogue('Dialogue · 2 de 3', "Pâle ou foncé ?", [
        ("JOCELYNE", "Vous voulez quelle couleur ?", True),
        ("FARIDA", "Je ne sais pas. Bleu, peut-être. Ou noir.", True),
        ("JOCELYNE", "Bleu pâle ou bleu foncé ?", True),
        ("FARIDA", "Pardon ? Pâle, foncé… Qu'est-ce que ça veut dire ?", True),
        ("JOCELYNE", "Pâle, c'est clair, comme le ciel. Foncé, c'est presque noir.", True),
    ], notes="Le moment central de la séance : Farida ne fait pas semblant de comprendre. "
             "« Qu'est-ce que ça veut dire ? » est la phrase la plus utile du module.")

    d.dialogue('Dialogue · 3 de 3', "Uni, pas rayé", [
        ("FARIDA", "Alors foncé. Le pâle, ça salit vite.", True),
        ("JOCELYNE", "Regardez : celui-ci est bleu foncé. Et celui-là est noir, avec des rayures.", True),
        ("FARIDA", "Rayé ? Non, merci. Je préfère uni.", True),
    ], notes="« Celui-ci » et « celui-là » apparaissent ici pour la première fois. Ne pas "
             "les expliquer : ils reviennent au défi 2.")

    d.tableau('Analyse', "Trois questions, et ce qu'elles demandent",
              ['La conseillère demande', 'On répond avec'],
              [["Pour l'automne ou pour l'hiver ?", "la saison"],
               ["Vous voulez quelle couleur ?", "une couleur"],
               ["Pâle ou foncé ?", "une nuance"],
               ["Uni ou rayé ?", "un motif"]],
              cle=0,
              note="Quatre renseignements, et la conseillère sait quoi aller chercher.",
              notes="Diapo à photographier. C'est la carte de route de tout le module.")

    d.regle("Demander ce qu'un mot veut dire",
            "« Pardon ? Qu'est-ce que ça veut dire ? »",
            precision="Personne ne trouve étrange qu'on pose cette question, et une "
                      "conseillère répond en une phrase. Faire semblant de comprendre "
                      "coûte beaucoup plus cher : on repart avec un manteau pâle qu'on "
                      "ne voulait pas.",
            notes="Diapo à photographier. Faire répéter la phrase à voix haute par tout le "
                  "groupe, deux fois.")

    d.cartes("Les vêtements de l'hiver", "Quatre familles", [
        ("Sur le corps",
         "un manteau, un chandail, un pantalon. Le manteau se met par-dessus tout le reste."),
        ("Sur la tête et le cou",
         "une tuque, un foulard, un capuchon. La tuque couvre les oreilles — c'est ce qui "
         "gèle en premier."),
        ("Aux mains",
         "des mitaines ou des gants. Les mitaines sont plus chaudes : les doigts se "
         "réchauffent l'un l'autre."),
        ("Aux pieds",
         "des bottes et des bas de laine. Les bottes doivent être doublées, sinon elles "
         "ne servent à rien en janvier."),
    ], notes="Faire nommer chaque famille par un élève différent, avec l'article.")

    d.piege("Faire semblant de comprendre",
            "Oui, oui… (sans avoir compris « foncé »)",
            "Pardon, qu'est-ce que ça veut dire ?",
            "C'est le réflexe le plus courant, et le plus coûteux. Une question de deux "
            "secondes évite un achat qu'on regrettera tout l'hiver — et la conseillère "
            "préfère largement répondre que reprendre un vêtement une semaine plus tard.",
            notes="Ne pas moraliser : tout le monde le fait, y compris dans sa propre "
                  "langue. Le but est de rendre la question facile à dire.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Farida cherche un manteau d'hiver.", "vrai"),
        ("C'est son premier hiver au Québec.", "vrai"),
        ("Elle veut un manteau bleu pâle.", "faux — foncé, le pâle salit vite"),
        ("« Foncé » veut dire presque noir.", "vrai"),
        ("Elle préfère un manteau rayé.", "faux — uni"),
        ("La conseillère va lui montrer trois modèles.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez cinq vêtements que vous portez cet hiver.",
        exemples=[
            "Avec leur article : un manteau, une tuque, des bottes…",
            "Et leur couleur, si vous la connaissez.",
        ],
        notes="Devoir court. Il prépare la séance A4 sur le genre des vêtements et donne "
              "des exemples personnels pour le défi 1.")

    return d.save(dossier)
