# -*- coding: utf-8 -*-
"""B1 · Ce que la lettre ne dit pas
Bloc B « Défi 1 · La lettre de motivation » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf` et son bandeau de quatre mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Ce que la lettre ne dit pas',
        chapeau="Le conseiller ne corrige pas les fautes de Rania. Il lui "
                "montre la question à laquelle sa lettre ne répond pas — et "
                "que personne n'écrit sur le formulaire.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Demander au groupe, avant tout : qu'est-ce "
                  "qu'un comité veut savoir qu'un formulaire ne demande pas ? Écrire "
                  "les réponses au tableau et y revenir à la fin.")

    d.objectifs([
        "comprendre à quelle question répond une lettre de motivation ;",
        "remplacer un adjectif par un fait daté ;",
        "expliquer un trou dans un parcours en une phrase ;",
        "nommer les quatre pièces d'un dossier de candidature.",
    ], notes="Le deuxième objectif est celui qui porte le bloc entier. Il se vérifie "
             "en une seconde : une phrase sans date ni nombre est un adjectif déguisé.")

    d.declencheur(
        'Observation', "Pourquoi vous, et pas la personne suivante ?",
        pistes=[
            "Qu'est-ce que vous faites que d'autres ne font pas ?",
            "Depuis combien de temps ? Où ? Avec qui ?",
            "Qu'est-ce que personne ne peut écrire à votre place ?",
            "Est-ce que ça se vérifie ?",
        ],
        notes="Question difficile, et c'est voulu. Laisser le silence : la plupart des "
              "gens répondent d'abord par un adjectif, et c'est ce qu'il faut "
              "entendre avant de donner la règle.")

    d.dialogue('Dialogue · 1 de 3', "Elle est bien écrite", [
        ("ÉMILIEN", "J'ai votre lettre devant moi. Merci de me l'avoir envoyée avant le dépôt.", True),
        ("RANIA", "Est-ce qu'elle est correcte ?", True),
        ("ÉMILIEN", "Elle est bien écrite. Ce n'est pas la question que je me poserais à votre place.", True),
        ("RANIA", "Quelle question, alors ?", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer que le conseiller ne parle jamais de fautes. Ce n'est "
             "pas un examen de français : c'est une candidature.")

    d.dialogue('Dialogue · 2 de 3', "Trois adjectifs", [
        ("ÉMILIEN", "Regardez votre deuxième paragraphe : « je suis responsable, patiente et à l'écoute ».", True),
        ("ÉMILIEN", "Trois adjectifs. Un comité en lit deux cents par année.", True),
        ("RANIA", "Qu'est-ce que je devrais écrire à la place ?", True),
        ("ÉMILIEN", "Ce qui les a produits. Vous êtes préposée depuis cinq ans, si je lis bien ?", True),
    ], notes="Écrire les trois adjectifs au tableau, puis les barrer un par un en "
             "demandant au groupe par quel fait les remplacer.")

    d.dialogue('Dialogue · 3 de 3', "Le trou du dossier", [
        ("RANIA", "Et pour mes deux années d'études en Syrie ? Je n'ai pas de diplôme.", True),
        ("ÉMILIEN", "Vous le dites comme vous venez de me le dire : deux années faites, l'école a fermé.", True),
        ("ÉMILIEN", "Ce qui inquiète un comité, ce n'est pas le trou, c'est de le découvrir tout seul.", True),
        ("RANIA", "Est-ce que ces deux années-là comptent pour quelque chose ?", True),
    ], notes="Réplique centrale du bloc. La faire répéter. Plusieurs élèves ont dans "
             "leur parcours une année qu'ils cachent depuis des années.")

    d.regle("Un fait daté vaut trois adjectifs",
            "« Je suis patiente » ne se vérifie pas ; « depuis cinq ans, à l'unité "
            "prothétique, j'accompagne douze résidents » se vérifie.",
            precision="Le comité ne peut rien faire d'une affirmation. Il peut faire "
                      "quelque chose d'une durée, d'un nombre et d'un lieu — les "
                      "trois se vérifient, et ils appartiennent à une seule personne.",
            notes="Diapositive à photographier. C'est la règle du bloc B, et elle "
                  "revient dans les quatre séances.")

    d.tableau('Analyse', "Les quatre pièces du dossier",
              ['La pièce', 'Ce qu\'elle fait'],
              [['le formulaire', "il identifie : nom, coordonnées, programme visé"],
               ['les relevés', "ils attestent ce qui a été fait à l'école"],
               ['les attestations', "elles prouvent ce qui a été fait ailleurs"],
               ['la lettre', "la seule page que la personne écrit elle-même"]],
              cle=0,
              note="Un dossier incomplet n'est pas refusé : il est mis de côté, ce qui "
                   "revient au même sans que personne l'annonce.",
              notes="Quatre rangées et une note : la densité tient. Insister sur la "
                    "note, qui est un fait administratif et non une opinion.")

    d.vocabulaire('Vocabulaire', "Quatre mots du dossier", [
        ("un dossier de candidature", "L'ensemble des documents qu'une personne dépose pour demander une place."),
        ("une lettre de motivation", "La lettre où l'on explique pourquoi on veut suivre une formation."),
        ("une pièce justificative", "Le papier qui prouve ce qu'on avance : un diplôme, une attestation."),
        ("une formule de courtoisie", "La phrase toute faite qui ouvre ou qui ferme une lettre formelle."),
    ], notes="Faire répéter avec l'article. « Une pièce justificative » est le terme "
             "exact du comptoir : l'élève l'entendra tel quel.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel entre Rania et le conseiller.", [
        ("Le conseiller trouve que la lettre est mal écrite.", "faux - elle est bien écrite"),
        ("Il lui reproche d'avoir employé des adjectifs à la place de faits.", "vrai"),
        ("Il conseille de cacher les deux années non terminées.", "faux - il faut les expliquer en une phrase"),
        ("Ce sont les préalables du secondaire d'ici qui décident de l'admission.", "vrai"),
        ("« Merci beaucoup pour votre temps » est une bonne formule de courtoisie.", "faux - c'est une formule de reconnaissance"),
        ("Le conseiller demande trois paragraphes, un par idée.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le troisième est "
             "celui qui compte : on n'efface pas un trou, on l'explique.")

    d.billet("Récris « je suis une personne responsable » avec un fait daté qui te "
             "concerne.",
             exemples=["Depuis quatre ans, j'ouvre le centre à six heures.",
                       "En trois ans, je n'ai manqué aucun quart."],
             notes="Ramasser les billets et en lire trois à la séance suivante. C'est "
                   "l'entrée directe de B2, où la lettre se construit.")

    return d.save(dossier)
