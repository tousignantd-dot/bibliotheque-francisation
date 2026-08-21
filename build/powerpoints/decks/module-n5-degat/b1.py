# -*- coding: utf-8 -*-
"""B1 · L'appel au propriétaire.
Bloc B « Défi 1 · Le constat » · couleur acier · 75 min. Compréhension orale.
Source : dialogue `t1`, exercice `t1a`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-degat/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="L'appel au propriétaire",
        chapeau="Cinq minutes au téléphone, et l'ordre dans lequel on dit les "
                "choses compte autant que ce qu'on dit.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Demander qui a déjà appelé un propriétaire pour "
                  "un problème, et comment ça s'est passé. Les mauvaises expériences "
                  "servent : elles montrent presque toujours un appel mal ordonné.")

    d.objectifs([
        "reconnaître les cinq temps d'un appel de signalement ;",
        "donner son nom et situer son logement d'entrée de jeu ;",
        "répondre aux questions sur le rythme et la durée de la fuite ;",
        "fixer une suite avant de raccrocher.",
    ])

    d.declencheur(
        'Mise en situation', "Vous appelez votre propriétaire. Par quoi commencez-vous ?",
        image=IMG + 'chauffe-eau-sous-sol.jpg',
        pistes=[
            "Par votre nom, ou par le problème ?",
            "Est-ce qu'il sait dans quel logement vous êtes ?",
            "Racontez-vous toute l'histoire tout de suite ?",
            "Qu'est-ce que vous voulez obtenir avant de raccrocher ?",
        ],
        notes="La dernière question est la plus utile : presque personne n'y pense "
              "d'avance, et c'est elle qui décide si l'appel sert à quelque chose.")

    d.dialogue('Dialogue · 1 de 3', "Le fait, en une phrase", [
        ("MARIAMA", "Monsieur Cloutier ? Mariama Baldé, du logement 4, au "
                    "118 Sainte-Hélène.", True),
        ("RÉJEAN", "Bonjour, madame Baldé. Qu'est-ce que je peux faire pour vous ?", True),
        ("MARIAMA", "J'ai un dégât d'eau dans ma chambre. Le plafond a coulé "
                    "pendant la nuit.", True),
        ("RÉJEAN", "Coulé comment ? Une goutte de temps en temps, ou de l'eau "
                   "qui tombe ?", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Trois répliques et tout est posé : qui, où, quoi. Faire remarquer que "
             "Mariama ne raconte pas encore — elle annonce.")

    d.dialogue('Dialogue · 2 de 3', "Les questions du propriétaire", [
        ("MARIAMA", "De l'eau qui tombait vraiment. Quand je me suis levée à six "
                    "heures, il y en avait déjà partout sur le plancher.", True),
        ("RÉJEAN", "Et là, présentement, est-ce que ça coule encore ?", True),
        ("MARIAMA", "Ça a arrêté vers sept heures. Mais en revenant du travail, "
                    "j'ai vu que la tache avait doublé.", True),
        ("RÉJEAN", "Bon. Décrivez-moi les dommages, pièce par pièce.", True),
    ], notes="Trois questions, toujours les mêmes : à quel rythme, est-ce que ça coule "
             "encore, qu'est-ce qui est abîmé. Les écrire au tableau.")

    d.dialogue('Dialogue · 3 de 3', "La suite, et ce qu'elle coûte", [
        ("RÉJEAN", "Madame Nguyên m'a appelé aussi : c'est son chauffe-eau qui a "
                   "lâché. Le plombier est passé cet après-midi.", True),
        ("MARIAMA", "Donc la fuite est réparée. Mais chez moi, le dégât reste.", True),
        ("RÉJEAN", "Il reste, oui. J'envoie une compagnie d'assèchement demain "
                   "matin. Trois ou quatre jours d'appareils dans votre chambre.", True),
        ("MARIAMA", "Trois ou quatre jours pendant lesquels je ne peux pas "
                    "coucher dans ma chambre.", True),
    ], notes="La dernière réplique n'est pas une plainte : c'est la phrase qui prépare la "
             "demande du défi 3. Le dire au groupe, sans plus.")

    d.cartes("Les cinq temps d'un appel", "Dans cet ordre", [
        ("Se nommer et situer",
         "« Mariama Baldé, du logement 4, au 118 Sainte-Hélène. »"),
        ("Dire le fait en une phrase",
         "Le fait d'abord, les détails après. Jamais le récit en premier."),
        ("Répondre sans broder",
         "Le rythme, la durée, ce qui est abîmé. Trois réponses courtes."),
        ("Décrire pièce par pièce",
         "Le bâtiment d'abord, vos biens ensuite : c'est le bâtiment qu'il fait réparer."),
    ], notes="Il y en a un cinquième, sur la diapositive suivante : c'est celui qu'on "
             "oublie.")

    d.regle("Fixer une suite avant de raccrocher",
            "Un appel qui finit sans date est un appel à refaire.",
            precision="Avant de raccrocher, il faut trois choses : une date ou un délai, "
                      "un nom — l'entreprise, la personne qui viendra —, et un geste de "
                      "votre part. « Je vous envoie mes photos aujourd'hui. » Ce geste "
                      "vous donne une raison de rappeler si rien ne bouge.",
            notes="Diapositive à photographier. C'est la différence entre un appel qui "
                  "règle quelque chose et un appel qui rassure sur le moment.")

    d.pratique('Pratique · exercice t1a', "Vrai ou Faux — L'appel au propriétaire",
               "Écoutez le dialogue, puis répondez.",
               [("Mariama commence par donner son nom et son adresse.", "VRAI"),
                ("Le propriétaire demande si l'eau coule encore.", "VRAI"),
                ("La tache était plus petite au retour du travail.", "FAUX"),
                ("C'est le chauffe-eau de madame Nguyên qui a lâché.", "VRAI"),
                ("Le plombier viendra seulement la semaine prochaine.", "FAUX"),
                ("Le propriétaire lui demande d'envoyer ses photos.", "VRAI")],
               corrige=True,
               notes="Six des huit énoncés. Les deux autres se font dans l'activité "
                     "interactive.")

    d.piege("Raconter avant d'annoncer",
            "Ça a commencé hier soir, je m'étais couchée tôt parce que…",
            "J'ai un dégât d'eau dans ma chambre. Le plafond a coulé cette nuit.",
            "Le récit est nécessaire — c'est tout le défi 1 —, mais il vient en second. "
            "Une personne qui décroche a besoin de savoir en dix secondes de quoi il "
            "s'agit. Après, elle écoute l'histoire au complet.",
            notes="Faire refaire l'ouverture par deux élèves : d'abord à leur façon, puis "
                  "avec le fait en tête. La différence s'entend.")

    d.billet(
        "Écrivez la première phrase de votre appel.",
        exemples=[
            "Votre nom, votre logement, puis le fait en une phrase.",
            "« Bonjour, Ana Silva, du logement 2. J'ai un dégât d'eau dans ma cuisine. »",
        ],
        notes="Deux minutes. Ces phrases servent de départ au jeu de rôle de la "
              "séance E1.")

    return d.save(dossier)
