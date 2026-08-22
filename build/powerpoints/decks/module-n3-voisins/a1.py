# -*- coding: utf-8 -*-
"""A1 · C'est vous, le nouveau du troisième ?
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-voisins/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="C'est vous, le nouveau du troisième ?",
        chapeau="On peut habiter deux ans dans un immeuble sans jamais parler "
                "à personne. La première conversation ne dure pas une minute, "
                "et c'est elle qui décide de toutes les autres.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander au groupe qui connaît le nom de "
                  "son voisin de palier. Les réponses — souvent aucune — ouvrent le "
                  "module mieux que n'importe quelle consigne.")

    d.objectifs([
        "nommer les lieux et les gens d'un immeuble ;",
        "comprendre une première conversation entre voisins ;",
        "se présenter : son nom, son étage, depuis quand ;",
        "présenter quelqu'un et dire le lien qui vous unit.",
    ])

    d.declencheur(
        'Observation', "Où est-ce qu'on se croise, dans un immeuble ?",
        image=IMG + 'escalier-exterieur.jpg',
        pistes=[
            "Dans quels endroits croisez-vous vos voisins ?",
            "Est-ce qu'on se dit bonjour, chez vous ?",
            "Connaissez-vous le nom de quelqu'un de votre immeuble ?",
            "Qu'est-ce qui empêche de parler à un voisin ?",
        ],
        notes="Laisser venir les réponses dans n'importe quelle langue, puis nommer les "
              "lieux en français au tableau : l'escalier, le palier, l'entrée, les "
              "boîtes aux lettres, la cour, la ruelle. C'est la liste de vocabulaire du "
              "module qui se construit toute seule.")

    d.dialogue('Dialogue · 1 de 3', "C'est vous, le nouveau du troisième ?", [
        ("MANON", "Bonjour ! C'est vous, le nouveau du troisième ?", True),
        ("RACHID", "Oui, c'est moi. Rachid Belkacem. Bonjour, madame.", True),
        ("MANON", "Manon Lachapelle, du deuxième. Bienvenue dans l'immeuble.", True),
        ("RACHID", "Merci beaucoup. Nous sommes arrivés il y a trois semaines.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Trois répliques, trois renseignements : le nom, l'étage, depuis quand. "
             "Faire remarquer que Manon donne les siens aussitôt après ceux de Rachid — "
             "c'est la règle non écrite de la présentation.")

    d.dialogue('Dialogue · 2 de 3', "Vous êtes plusieurs, chez vous ?", [
        ("MANON", "Nous ? Vous êtes plusieurs, chez vous ?", True),
        ("RACHID", "Ma femme, mon petit garçon et moi. Il a quatre ans.", True),
        ("MANON", "Quatre ans ! C'est le bel âge. Et vous travaillez dans le coin ?", True),
        ("RACHID", "Je suis électricien. Je pars tôt le matin, vers six heures.", True),
    ], notes="La profession et l'horaire arrivent sans qu'on les demande vraiment : "
             "c'est ainsi qu'une conversation d'escalier avance. Faire relever les deux "
             "liens familiaux nommés — ma femme, mon petit garçon.")

    d.dialogue('Dialogue · 3 de 3', "Je vous présente ma sœur", [
        ("LEILA", "Rachid, tu viens ? La porte est restée ouverte en haut.", True),
        ("RACHID", "Une minute. Madame Lachapelle, je vous présente ma sœur, Leïla.", True),
        ("LEILA", "Bonjour ! Enchantée.", True),
        ("MANON", "Enchantée. Si vous avez besoin de quelque chose, je suis au 2B.", True),
    ], notes="Le moment de la présentation d'un tiers. Faire remarquer l'ordre : on "
             "nomme d'abord la personne à qui on parle, puis on présente. Et la phrase "
             "de Manon à la fin : c'est une offre d'aide, elle appelle un merci.")

    d.tableau('Analyse', "Les lieux d'un immeuble",
              ["L'endroit", "Ce qu'on y fait"],
              [["l'escalier, le palier", "on se croise, on se salue en passant"],
               ["l'entrée, les boîtes aux lettres", "on prend son courrier, on lit les affiches"],
               ["la cour, la remise", "on range son vélo, on étend son linge"],
               ["la ruelle", "on passe en arrière, les enfants y jouent"]],
              cle=1,
              note="Ces endroits appartiennent à tout le monde en même temps — c'est "
                   "tout le sujet du défi 1.",
              notes="Diapo à photographier. Faire nommer chaque ligne par un élève "
                    "différent, avec l'article.")

    d.regle("Se présenter, en trois renseignements",
            "« Je m'appelle Rachid Belkacem, du troisième. »",
            precision="Le nom, l'étage, et souvent depuis quand on habite là. "
                      "Dans un immeuble, l'étage vaut presque autant que le nom : "
                      "c'est lui qui permet au voisin de vous replacer le lendemain.",
            notes="Diapo à photographier. Faire dire la phrase par chaque élève, avec "
                  "son vrai étage. Deux minutes, et tout le monde a parlé une fois.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Rachid habite au troisième depuis trois semaines.", "vrai"),
        ("Manon vient d'arriver dans l'immeuble, elle aussi.", "faux — elle est là depuis onze ans"),
        ("Rachid est électricien et il part travailler très tôt.", "vrai"),
        ("Leïla est la femme de Rachid.", "faux — c'est sa sœur"),
        ("Leïla habite dans le même immeuble que son frère.", "faux — elle habite à Longueuil"),
        ("Manon dit à Rachid où la trouver s'il a besoin d'aide.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. C'est l'exercice "
             "`pr1` du module interactif, mot pour mot.")

    d.billet(
        "Écrivez votre présentation en trois phrases.",
        exemples=[
            "Votre nom, votre étage, depuis quand vous habitez là.",
            "Et le nom d'une personne de chez vous, avec son lien.",
        ],
        notes="Devoir court. Il prépare la séance A4 sur les formules de présentation et "
              "donne à chacun sa phrase de départ pour le jeu de rôle.")

    return d.save(dossier)
