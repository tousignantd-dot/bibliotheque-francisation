# -*- coding: utf-8 -*-
"""A2 · La voix monte, la voix descend.
Bloc A « Je découvre » · couleur indigo · 75 min.
Source : exercice `prSons`, mini-leçon `prSons`.

La séance de phonétique du module. Le programme du niveau 2 demande de
reconnaître l'intonation montante de la question et l'intonation descendante
de l'énoncé — le premier savoir prosodique du niveau. « Ça va » l'offre tout
fait : les mêmes deux mots, deux sens, et rien d'autre à retenir.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-bonjour/images/')


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="La voix monte, la voix descend",
        chapeau="Les mêmes mots, deux sens. Ce qui décide, ce n'est pas le "
                "mot, c'est la fin de la phrase.",
        duree='75 minutes')

    d.titre(notes="Séance d'oreille avant tout. Parler peu, faire écouter beaucoup. "
                  "Certains élèves n'entendront pas la différence au premier cours : "
                  "c'est normal, elle vient avec la répétition.")

    d.objectifs([
        "entendre si la voix monte ou descend ;",
        "poser une question sans « est-ce que » ;",
        "répondre avec la voix qui descend ;",
        "renvoyer la question avec « et vous ? ».",
    ])

    d.declencheur(
        'Observation', "Est-ce qu'on demande, ou est-ce qu'on répond ?",
        image=IMG + 'entree-immeuble.jpg',
        pistes=[
            "Écoutez : « Ça va ? »",
            "Écoutez : « Ça va. »",
            "Est-ce que les mots changent ?",
            "Qu'est-ce qui change, alors ?",
        ],
        notes="Dire les deux phrases plusieurs fois, lentement, sans expliquer. Laisser "
              "le groupe chercher. La règle vient après l'oreille, jamais avant.")

    d.tableau('Analyse', "Deux mots, deux sens",
              ['Ce qu\'on entend', 'Ce que ça veut dire'],
              [["Ça va ?", "je demande — la voix monte"],
               ["Ça va.", "je réponds — la voix descend"],
               ["Tu travailles ?", "je demande — la voix monte"],
               ["Je travaille.", "je réponds — la voix descend"]],
              cle=2,
              note="Tout se joue sur la dernière syllabe. Le reste de la phrase ne "
                   "change pas.",
              notes="Diapositive à photographier. Faire dire les quatre lignes à voix "
                    "haute par chaque élève, une fois, sans correction serrée.")

    d.regle("La question sans « est-ce que »",
            "En français parlé, une voix qui monte suffit à poser une question.",
            precision="« Tu travailles ? », dit avec la voix qui monte, est une vraie "
                      "question, correcte et "
                      "courante. « Est-ce que tu travailles ? » n'est pas plus juste : "
                      "c'est seulement plus long. Au niveau 2, on garde la forme courte.",
            notes="Diapositive à photographier. Rassurer : beaucoup d'élèves croient "
                  "qu'une question exige « est-ce que ». Ce n'est pas le cas.")

    d.cartes("Trois fins de phrase", "Où va la voix ?", [
        ("Elle monte : c'est une question", "Ça va ? · Tu travailles ? · Vous allez bien ?"),
        ("Elle descend : c'est une réponse", "Ça va bien. · Je travaille. · Je vais bien."),
        ("Elle monte encore : on redemande", "Et toi ? · Et vous ?"),
    ], cols=3, notes="Diapositive à photographier. Faire lever la main quand la voix "
                     "monte, la baisser quand elle descend : le geste aide l'oreille.")

    d.pratique('Écoute', "Question ou réponse ?",
               "Écoutez chaque phrase et écrivez ce que vous entendez.", [
        ("Ça va ?", "question"),
        ("Ça va bien, merci.", "réponse"),
        ("Tu travailles ce soir ?", "question"),
        ("Je travaille ce soir.", "réponse"),
        ("Vous allez bien ?", "question"),
        ("Je vais bien.", "réponse"),
    ], corrige=True, cols=2,
       notes="Dire chaque phrase trois fois, dans le désordre. Ne pas montrer l'écriture "
             "pendant l'écoute : c'est l'oreille qui travaille.")

    d.piege('Le piège', "« Ça va ? » avec la voix qui descend",
            "« Ça va ? » avec la voix qui monte",
            "Une question dite avec la voix qui descend ne s'entend pas comme une "
            "question : la personne croit que vous répondez, et elle ne dit plus rien. "
            "Montez bien sur la dernière syllabe : ça <b>va</b> ?",
            notes="Faire répéter en chœur, lentement, puis à vitesse normale. C'est la "
                  "difficulté qui reste le plus longtemps.")

    d.pratique('Pratique · à deux', "Le ping-pong des questions",
               "Deux par deux, chacun son tour.", [
        ("Étape 1", "L'un pose une question courte : « Ça va ? »"),
        ("Étape 2", "L'autre répond, voix qui descend."),
        ("Étape 3", "Il ajoute « et toi ? », voix qui monte."),
        ("Étape 4", "Changez de rôle après quatre échanges."),
    ], cols=1,
       notes="Vingt minutes. Circuler et redire soi-même la phrase quand les deux élèves "
             "hésitent : ils ont besoin d'un modèle, pas d'un arbitre.")

    d.billet(
        "Dites ces trois phrases à voix haute, trois fois chacune.",
        exemples=[
            "Ça va ?",
            "Ça va bien, merci.",
            "Et vous ?",
        ],
        notes="Devoir d'oreille. Rappeler que la mini-leçon en ligne fait entendre chaque "
              "phrase autant de fois qu'on veut.")

    return d.save(dossier)
