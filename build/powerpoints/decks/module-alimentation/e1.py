# -*- coding: utf-8 -*-
"""E1 · À toi : commander et expliquer.
Bloc E « Je me lance » · couleur teal · 90 min.
Source : dialogue `appli`, jeu de rôle et productions orale et écrite.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='À toi : commander et expliquer',
        chapeau="Trois productions, dans l'ordre : une commande au comptoir "
                "avec l'assistant, un plat expliqué à voix haute, une liste "
                "d'épicerie écrite.",
        duree='90 minutes')

    d.titre(notes="Séance de production. Prévoir les postes et les écouteurs. Rendre "
                  "d'abord les billets corrigés de B2, C1 et C2 : ce sont les brouillons.")

    d.objectifs([
        "commander un produit à un comptoir, à l'oral, avec un interlocuteur ;",
        "expliquer ce qu'il faut acheter pour un plat, avec les quantités ;",
        "écrire une liste d'épicerie en phrases complètes ;",
        "me relire et me corriger avant d'envoyer.",
    ])

    d.dialogue('Le modèle', "Au comptoir de la charcuterie", [
        ("FARIDA", "Mince, s'il vous plaît. Deux cents grammes.", True),
        ("SIMON", "Deux cents grammes… ça vous en fait une douzaine de tranches. Ça va ?", True),
        ("FARIDA", "C'est parfait. Il vient d'où, celui-là ?", True),
        ("SIMON", "Du Québec. Il y en a un autre moins cher, mais il est plus salé.", False),
    ], consigne="Repérez tout ce que vous avez appris dans ces quatre répliques.",
       notes="Faire chercher : une quantité avec son unité, deux « en », une question sur "
             "la provenance, une comparaison. Tout le module y est.")

    d.cartes('Production 1 · Le jeu de rôle', "Comment ça marche", [
        ("Tu choisis le comptoir",
         "La boucherie, le poisson ou la charcuterie. Trois situations ordinaires."),
        ("Tu choisis ton rôle",
         "Le client, ou la personne au comptoir. Servir est plus difficile que commander."),
        ("L'assistant demande une chose à la fois",
         "Le produit, puis la quantité. Il ne dit pas d'où ça vient ni combien de temps ça "
         "se garde : c'est à toi de le demander."),
        ("Ton but",
         "Repartir avec la bonne quantité, en sachant la provenance, la conservation et le "
         "prix."),
    ], notes="Vingt-cinq minutes. Passer dans les rangées. Rappeler les quatre temps de la "
             "commande au tableau.")

    d.cartes('Production 2 · Un plat expliqué', "Trois temps, quarante-cinq secondes", [
        ("Temps 1 · Ce qu'il faut acheter",
         "« Il faut du bœuf haché, des oignons et de la pâte de tomate. »"),
        ("Temps 2 · Les quantités",
         "« Une livre de bœuf haché, deux oignons, une boîte de pâte de tomate. »"),
        ("Temps 3 · La préparation et la conservation",
         "« Ça se cuisine en trente minutes. Ça se garde trois jours au frigo. »"),
    ], notes="Le plat est libre. Les billets de B2 et B3 contiennent déjà les formes "
             "nécessaires : du/de la/des, et « ça se garde ».")

    d.cartes('Production 3 · La liste', "En phrases complètes", [
        ("Ce qu'elle doit contenir",
         "Six produits au moins ; une quantité pour chacun ; deux précisions — sorte, "
         "coupe, format ; et ce qu'il ne faut PAS prendre."),
        ("Ce qu'on vérifie",
         "du, de la et des au moins une fois chacun, et une phrase négative avec « pas "
         "de ». Cinq à huit phrases."),
        ("Pourquoi en phrases",
         "Une liste de mots ne se corrige pas. En phrases, chaque quantité et chaque "
         "article se vérifient — et la personne qui fait vos courses comprend mieux."),
    ], notes="La troisième carte justifie une consigne qui peut sembler artificielle. Le "
             "dire.")

    d.regle("Avant d'envoyer",
            "Relis-toi une fois, à voix basse.",
            precision="Trois choses à vérifier, toujours les mêmes : « de » après une "
                      "négation et après une quantité, la place de « en » devant le verbe, "
                      "et l'unité de chaque quantité. Ce sont les trois fautes du module.",
            notes="Diapo à photographier. C'est la liste de vérification de tout le module.")

    d.piege("Écrire une liste de mots",
            "poulet, riz, savon, jambon",
            "Il me faudrait du poulet — quatre poitrines. Prends du riz, mais pas de petit format.",
            "Une liste de mots ne dit ni la quantité, ni la sorte, ni ce qu'il ne faut pas "
            "prendre. En phrases, tout y est — et c'est exactement ce que le module a "
            "appris à dire.",
            notes="Faire comparer les deux à voix haute. La différence d'information est "
                  "frappante.")

    d.cartes("Ce que l'enseignant reçoit", "Et ce qu'il ne reçoit pas", [
        ("Le plat expliqué",
         "Ton enregistrement et sa transcription, si tu choisis de les envoyer. Rien ne "
         "part tant que tu n'as pas cliqué."),
        ("La liste écrite",
         "Le texte que tu déposes, tel que tu l'as écrit. Tu peux le reprendre autant de "
         "fois que tu veux."),
        ("Ce qui n'est jamais conservé",
         "Les corrections de l'assistant et la conversation du jeu de rôle. Elles servent "
         "à t'entraîner, pas à t'évaluer."),
    ], notes="Le dire clairement, comme dans les autres modules.")

    d.billet(
        "Après avoir envoyé : notez une chose que vous corrigeriez si vous recommenciez.",
        exemples=[
            "Une seule chose, la plus importante pour vous.",
            "Exemple : « j'ai oublié de demander combien de temps ça se garde ».",
        ],
        notes="Rendre annoté à la séance E2, où les élèves font leur autoévaluation.")

    return d.save(dossier)
