# -*- coding: utf-8 -*-
"""B1 · Dans quelle allée ?
Bloc B « Défi 1 · Trouver le produit » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1nombre`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Dans quelle allée ?',
        chapeau="« Allée cinq » ou « allée quinze » ? Un chiffre mal entendu, "
                "et on cherche dix minutes pour rien. Demander, comprendre, "
                "et savoir faire répéter.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc B. Demander au groupe qui a déjà cherché longtemps un "
                  "produit qui était juste à côté.")

    d.objectifs([
        "demander où se trouve un produit ;",
        "comprendre une réponse qui donne un numéro et une position ;",
        "faire répéter en donnant les deux possibilités ;",
        "vérifier avant de partir chercher.",
    ])

    d.declencheur(
        'Mise en situation', "On vous répond « allée cinq ». Vous n'êtes pas sûr. Que dites-vous ?",
        pistes=[
            "« Pardon ? »",
            "« Vous pouvez répéter ? »",
            "« Allée cinq ou allée quinze ? »",
            "Laquelle est la plus rapide ?",
        ],
        notes="La troisième. Les deux premières font redire la même phrase à la même "
              "vitesse ; la troisième obtient une réponse d'un seul mot.")

    d.dialogue('Dialogue · 1 de 3', "La demande", [
        ("MARISOL", "Excusez-moi. Je cherche l'huile.", True),
        ("ÉRIC", "L'huile, c'est allée cinq.", True),
        ("MARISOL", "Pardon ? Allée cinq ou allée quinze ?", True),
        ("ÉRIC", "Cinq. Un, deux, trois, quatre, cinq.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Le commis compte à voix haute : c'est une réponse fréquente et très efficace. "
             "Elle ne demande aucun effort de compréhension.")

    d.dialogue('Dialogue · 2 de 3', "Se repérer", [
        ("MARISOL", "Ah, cinq. Et c'est où, l'allée cinq ?", True),
        ("ÉRIC", "Vous voyez le grand panneau blanc ? C'est juste en dessous.", True),
        ("MARISOL", "D'accord. Et l'huile est en haut ou en bas ?", True),
        ("ÉRIC", "Au milieu. À côté du vinaigre.", True),
    ], notes="Marisol pose trois questions de suite, une à la fois. C'est le bon rythme : "
             "une question, une réponse.")

    d.dialogue('Dialogue · 3 de 3', "Remercier", [
        ("MARISOL", "Merci. Vous êtes gentil.", True),
        ("ÉRIC", "Ça me fait plaisir.", True),
    ], notes="« Ça me fait plaisir » et « bienvenue » sont les deux réponses les plus "
             "courantes ici à un merci. « Bienvenue » ne veut pas dire « entrez ».")

    d.tableau('Analyse', "Ce que contient une réponse",
              ['Le morceau', 'Un exemple'],
              [["Le numéro d'allée", "« allée cinq »"],
               ["Un repère visible", "« sous le grand panneau blanc »"],
               ["La hauteur", "« au milieu »"],
               ["Un produit voisin", "« à côté du vinaigre »"]],
              cle=0,
              note="Rarement les quatre d'un coup : on les obtient en posant des questions.",
              notes="Diapo à photographier. Faire remarquer que Marisol a posé trois "
                    "questions pour obtenir les quatre morceaux.")

    d.regle("Vérifier le chiffre",
            "« Allée cinq ou allée quinze ? »",
            precision="Répéter en donnant les <b>deux</b> possibilités transforme une "
                      "question difficile en question facile : la personne répond par un "
                      "seul mot. C'est plus rapide que « pardon ? », et cela ne demande "
                      "aucun effort à personne.",
            notes="Diapo à photographier. C'est la technique centrale du défi 1. Faire "
                  "pratiquer avec cinq paires de nombres.")

    d.piege("Partir sans le numéro",
            "« C'est par là. » — et on cherche dix minutes.",
            "« C'est quelle allée ? »",
            "Une direction du bras ne suffit pas dans un magasin de quinze rangées. Le "
            "numéro est ce qui fait gagner du temps : il est écrit en grand, visible des "
            "deux côtés, et impossible à manquer une fois qu'on le connaît.",
            notes="Faire pratiquer la question de relance : « C'est quelle allée ? »")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Marisol cherche l'huile.", "vrai"),
        ("L'huile est dans l'allée quinze.", "faux — l'allée cinq"),
        ("Marisol n'est pas sûre d'avoir bien entendu.", "vrai"),
        ("Le commis compte jusqu'à cinq pour être clair.", "vrai"),
        ("L'huile est sur la tablette du haut.", "faux — au milieu"),
        ("L'huile est à côté du vinaigre.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez trois demandes complètes.",
        exemples=[
            "« Excusez-moi, je cherche… »",
            "Puis la question de vérification : « … ou … ? »",
        ],
        notes="Ramasser. Ces phrases servent à la pratique orale de B4.")

    return d.save(dossier)
