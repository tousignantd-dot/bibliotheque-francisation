# -*- coding: utf-8 -*-
"""B1 · Quel est votre nom ?
Bloc B « Défi 1 · Le nom et la date de naissance » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1civil`.

Première séance du défi 1. Elle porte les quatre cases du haut de la fiche et
la forme de question qui les demande toutes.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Quel est votre nom ?',
        chapeau="Une question, une case, une réponse. On répond, on épelle, "
                "et on vérifie ce qui est écrit.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 1. Reprendre les billets de A3 : les mots "
                  "difficiles signalés hier se replacent ici, dans une phrase.")

    d.objectifs([
        "comprendre « quel est votre nom de famille ? » ;",
        "répondre et épeler ;",
        "distinguer le nom de famille du prénom ;",
        "comprendre madame, monsieur, F et H.",
    ])

    d.declencheur(
        'Écoute', "Qu'est-ce qu'on lui demande ?",
        pistes=[
            "Combien de questions entendez-vous ?",
            "Qu'est-ce qu'on lui fait faire après sa réponse ?",
            "Pourquoi lui demande-t-on d'épeler ?",
            "Quelle case coche-t-on à la fin ?",
        ],
        notes="Faire écouter le dialogue deux fois, diapo masquée, avant d'afficher quoi "
              "que ce soit.")

    d.dialogue('Dialogue · 1 de 2', "Le nom, puis le prénom", [
        ("MADAME CÔTÉ", "Quel est votre nom de famille ?", True),
        ("YUSUF", "Daoud. D - A - O - U - D.", True),
        ("MADAME CÔTÉ", "Merci. Et votre prénom ?", True),
        ("YUSUF", "Yusuf. Y - U - S - U - F.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire remarquer que Yusuf épelle sans qu'on le lui demande la deuxième "
             "fois : c'est ce qu'on veut leur faire prendre comme habitude.")

    d.dialogue('Dialogue · 2 de 2', "On vérifie, on coche", [
        ("MADAME CÔTÉ", "Monsieur Yusuf Daoud. C'est bien ça ?", True),
        ("YUSUF", "Oui, c'est ça.", True),
        ("MADAME CÔTÉ", "Je coche « H ». H pour homme, F pour femme.", True),
    ], notes="« C'est bien ça ? » est la phrase de vérification. La faire répéter : c'est "
             "celle qui permet de corriger un nom mal écrit avant qu'il entre au dossier.")

    d.tableau('Analyse', "Deux mots, deux cases",
              ['Le mot', 'Un exemple'],
              [["le nom de famille", "Daoud — celui de toute la famille"],
               ["le prénom", "Yusuf — le vôtre seulement"],
               ["ici, on écrit d'abord", "le prénom, puis le nom : Yusuf Daoud"]],
              cle=2,
              note="Sur la fiche, les deux cases sont séparées et nommées.",
              notes="Diapo à photographier. L'ordre prénom-nom n'est pas le même partout "
                    "dans le monde : le dire simplement, sans le commenter.")

    d.regle("Quel est votre… ?",
            "C'est la question de toutes les fiches.",
            precision="Elle revient à chaque case : « <b>quel</b> est votre nom de "
                      "famille ? », « <b>quel</b> est votre prénom ? », « <b>quelle</b> "
                      "est votre adresse ? ». À l'oreille, <b>quel</b> et <b>quelle</b> "
                      "se disent exactement pareil : vous n'avez rien à choisir en "
                      "parlant.",
            notes="Diapo à photographier. La différence à l'écrit est le sujet de B2 : ne "
                  "pas l'ouvrir ici.")

    d.cartes("Les mots courts de la fiche", "Quatre à reconnaître", [
        ("Madame · Monsieur",
         "Devant le nom d'une femme, devant celui d'un homme. Écrits en court : Mme, M."),
        ("F · H",
         "La case du sexe. F pour femme, H pour homme."),
        ("M · F",
         "Sur d'autres fiches : M pour masculin, F pour féminin. Même case, même réponse."),
        ("Attention au F",
         "Ici F veut dire femme, là F veut dire féminin. Ce n'est jamais « français »."),
    ], notes="Diapo à photographier. C'est le contenu de l'exercice `t1civil`. Montrer "
             "deux vraies fiches différentes si vous en avez.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le nom de famille de Yusuf est Daoud.", "vrai"),
        ("Son prénom est Yusuf.", "vrai"),
        ("Il n'épelle pas son nom.", "faux — il l'épelle deux fois"),
        ("Madame Côté coche « F ».", "faux — elle coche « H »"),
        ("« H » veut dire « homme ».", "vrai"),
    ], corrige=True, cols=1,
       notes="Cinq énoncés, comme dans l'exercice `t1vf`.")

    d.pratique('Pratique · à deux', "On remplit votre fiche",
               "L'un pose les questions, l'autre répond. Puis on échange.", [
        ("Question 1", "Quel est votre nom de famille ?"),
        ("Question 2", "Pouvez-vous l'épeler ?"),
        ("Question 3", "Quel est votre prénom ?"),
        ("Question 4", "Monsieur ou madame ? F ou H ?"),
    ], cols=1,
       notes="Vingt minutes, trois partenaires différents. Celui qui pose les questions "
             "écrit vraiment sur une fiche vierge — et la montre à la fin pour "
             "vérification.")

    d.billet(
        "Écrivez la question qu'on vous pose, puis votre réponse.",
        exemples=[
            "Quel est votre nom de famille ?",
            "Mon nom de famille est…",
            "Et épelez-le, à côté.",
        ],
        notes="Deux minutes. Relever surtout si « quel » est bien écrit en un seul mot.")

    return d.save(dossier)
