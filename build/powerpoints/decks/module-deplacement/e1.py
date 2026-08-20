# -*- coding: utf-8 -*-
"""E1 · À toi : demander et expliquer.
Bloc E « Je me lance » · couleur teal · 90 min.
Source : dialogue `appli`, jeu de rôle et productions orale et écrite.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : demander et expliquer',
        chapeau="Trois productions, dans l'ordre : une conversation avec "
                "l'assistant, un trajet expliqué à voix haute, des indications "
                "écrites. La conversation sert de répétition aux deux autres.",
        duree='90 minutes')

    d.titre(notes="Séance de production. Prévoir les postes et les écouteurs. Rendre "
                  "d'abord les billets corrigés de B1, C1 et C2 : ce sont les brouillons.")

    d.objectifs([
        "demander mon chemin ou l'expliquer, à l'oral, avec un interlocuteur ;",
        "expliquer un trajet que je connais, en trois temps ;",
        "écrire des indications claires pour venir chez moi ;",
        "me relire et me corriger avant d'envoyer.",
    ])

    d.dialogue('Le modèle', 'Perdue au terminus', [
        ("NOUR", "Excusez-moi, je cherche le quai 12. Je tourne en rond depuis dix minutes.", True),
        ("GILLES", "Vous êtes au bon étage, mais du mauvais côté. Les quais 1 à 10 sont ici, les autres sont derrière.", False),
        ("NOUR", "Derrière ? Je passe par où ?", True),
        ("GILLES", "Passez par le corridor vitré, à votre gauche, et descendez l'escalier au bout.", False),
    ], consigne="Repérez tout ce que vous avez appris dans ces quatre répliques.",
       notes="Faire chercher : une formule d'ouverture, une question courte, deux "
             "impératifs, deux prépositions, deux repères. Tout le module y est.")

    d.cartes('Production 1 · Le jeu de rôle', "Comment ça marche", [
        ("Tu choisis la situation",
         "Au terminus, au coin de la rue, ou à pied jusqu'à un bureau. Trois situations "
         "ordinaires."),
        ("Tu choisis ton rôle",
         "La personne qui cherche, ou celle qui explique. Les deux sont à pratiquer : "
         "expliquer est plus difficile."),
        ("L'assistant ne donne pas tout d'un coup",
         "Une ou deux étapes à la fois, comme dans la vraie vie. À toi de demander la "
         "suite et de répéter pour vérifier."),
        ("Ton but",
         "Arriver à destination, et savoir combien de temps ça prend."),
    ], notes="Vingt-cinq minutes. Passer dans les rangées. Les élèves qui bloquent ont "
             "presque toujours oublié de dire d'où ils partent.")

    d.cartes('Production 2 · Le trajet expliqué', "Trois temps, quarante-cinq secondes", [
        ("Temps 1 · Le départ et l'arrivée",
         "« Tu pars de l'école et tu vas à la clinique, sur Chambly. »"),
        ("Temps 2 · Les étapes, à l'impératif",
         "« Sors par la porte principale, tourne à droite, marche jusqu'au feu. »"),
        ("Temps 3 · Les repères et la durée",
         "« C'est celui qui a une porte vitrée. Compte quinze minutes. »"),
    ], notes="Le trajet est libre : de chez soi à l'école, à l'épicerie, chez le médecin. "
             "Les billets de B1 et C1 contiennent déjà le matériel.")

    d.cartes('Production 3 · Les indications écrites', "Pour venir chez toi", [
        ("Ce qu'elles doivent contenir",
         "Le point de départ ; les étapes dans l'ordre ; deux repères visuels ; la durée."),
        ("Ce qu'on vérifie",
         "Au moins trois verbes à l'impératif, et une fois jusqu'à, vers ou par. "
         "Cinq à huit phrases."),
        ("Avant d'envoyer",
         "Relis-toi à voix basse. Vérifie le -s de l'impératif et chaque fusion : au, aux, "
         "du, des."),
    ], notes="Le billet de C2 — expliquer par téléphone sans dire « à droite » — est le "
             "brouillon de cette production.")

    d.regle("Avant d'envoyer",
            "Relis-toi une fois, à voix basse.",
            precision="Trois choses à vérifier, toujours les mêmes : le -s de l'impératif "
                      "à la forme tu, les fusions (au, aux, du, des), et la présence du "
                      "point de départ. Ce sont les trois fautes du module.",
            notes="Diapo à photographier. C'est la liste de vérification de tout le module.")

    d.piege("Oublier d'où l'autre part",
            "Tourne à droite, marche jusqu'au parc, c'est le troisième édifice.",
            "Tu pars de l'école ? Alors sors par la porte principale et tourne à droite.",
            "Un itinéraire sans point de départ n'est pas un itinéraire : c'est une suite "
            "d'ordres qui peut mener n'importe où. C'est la première question de Nour à "
            "Patrice, et c'est la première chose que l'assistant vous demandera.",
            notes="Faire trouver la faute par le groupe avant d'afficher la colonne de "
                  "droite.")

    d.cartes("Ce que l'enseignant reçoit", "Et ce qu'il ne reçoit pas", [
        ("Le trajet expliqué",
         "Ton enregistrement et sa transcription, si tu choisis de les envoyer. Rien ne "
         "part tant que tu n'as pas cliqué."),
        ("Les indications écrites",
         "Le texte que tu déposes, tel que tu l'as écrit. Tu peux le reprendre autant de "
         "fois que tu veux avant d'envoyer."),
        ("Ce qui n'est jamais conservé",
         "Les corrections de l'assistant et la conversation du jeu de rôle. Elles servent "
         "à t'entraîner, pas à t'évaluer."),
    ], notes="Le dire clairement. Plusieurs élèves n'osent pas se tromper devant l'assistant "
             "parce qu'ils croient que tout est vu. Ce n'est pas le cas.")

    d.billet(
        "Après avoir envoyé : notez une chose que vous corrigeriez si vous recommenciez.",
        exemples=[
            "Une seule chose, la plus importante pour vous.",
            "Exemple : « j'ai oublié de dire d'où on part ».",
        ],
        notes="Rendre annoté à la séance E2, où les élèves font leur autoévaluation.")

    return d.save(dossier)
