# -*- coding: utf-8 -*-
"""C1 · Où mettre l'argent qui reste
Bloc C « Défi 2 · Faire travailler l'argent » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf` et son bandeau de quatre mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Où mettre l'argent qui reste",
        chapeau="Six mille deux cents dollars dorment dans un compte chèque. "
                "La première question de la planificatrice n'a rien de "
                "financier : quand en aurez-vous besoin ?",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc C. Rappeler la fin du bloc B : la carte est réglée "
                  "par un prêt à 11,20 %, et le compte chèque est toujours là.")

    d.objectifs([
        "dire pourquoi la date du projet choisit le produit ;",
        "distinguer un abri fiscal d'un placement ;",
        "dire jusqu'où les dépôts sont protégés, et par qui ;",
        "employer quatre mots de l'épargne avec leur article.",
    ], notes="Le deuxième objectif dissipe la confusion la plus courante du domaine, et "
             "il faut l'énoncer plusieurs fois dans le bloc.")

    d.declencheur(
        'Observation', "De l'argent qui dort dans un compte, est-ce que ça coûte "
                       "quelque chose ?",
        pistes=[
            "Est-ce qu'il perd de la valeur avec le temps ?",
            "Et si on doit de l'argent à côté, à un taux élevé ?",
            "Pourquoi les gens gardent-ils quand même de l'argent liquide ?",
            "Combien de temps peux-tu t'en passer, toi ?",
        ],
        notes="La dernière question est celle du bloc entier, et elle est personnelle. "
              "Ne demander à personne de chiffrer à voix haute.")

    d.dialogue('Dialogue · 1 de 3', "Quand en avez-vous besoin ?", [
        ("NATHALIE", "Ces six mille deux cents dollars sont dans un compte chèque. Vous savez ce qu'ils vous rapportent ?", True),
        ("MARLÈNE", "Rien du tout, je pense.", True),
        ("NATHALIE", "Il y a trois façons de les faire travailler, et le choix dépend d'une seule chose : quand est-ce que vous en avez besoin ?", True),
        ("MARLÈNE", "Dans deux ans. Jessie commence le cégep en août dans deux ans.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer l'ordre : la conseillère demande la date avant de nommer "
             "un seul produit. C'est le signe d'un bon conseil.")

    d.dialogue('Dialogue · 2 de 3', "Un abri, pas un placement", [
        ("MARLÈNE", "Le CELI, je n'ai jamais compris si c'est un compte ou un placement.", True),
        ("NATHALIE", "Le CELI n'est pas un placement : c'est un abri. Ce qui pousse à l'intérieur n'est pas imposé.", True),
        ("MARLÈNE", "Donc je peux mettre un dépôt à terme dans un CELI ?", True),
        ("NATHALIE", "Vous pouvez, et c'est souvent ce qu'on fait pour un projet à deux ans.", True),
    ], notes="Diapositive à commenter longuement. C'est la distinction que le bloc "
             "entier travaille, et elle est dite ici en deux répliques.")

    d.dialogue('Dialogue · 3 de 3', "Si la caisse tombe", [
        ("MARLÈNE", "Et si la caisse fait faillite, moi, je perds mon argent ?", True),
        ("NATHALIE", "Non. Les dépôts sont protégés par l'Autorité des marchés financiers, jusqu'à cent mille dollars par catégorie de dépôts.", True),
        ("MARLÈNE", "Cent mille. Je suis loin du compte.", True),
        ("NATHALIE", "Et si quelqu'un vous appelle pour un placement garanti à douze pour cent, c'est une fraude.", True),
    ], notes="La dernière réplique ouvre le bloc D. La laisser sans commentaire ici : "
             "elle sera reprise en D1.")

    d.tableau('Analyse', "Trois produits, trois questions",
              ['Le produit', 'La question à lui poser'],
              [['le compte épargne', "puis-je le reprendre demain ?"],
               ['le dépôt à terme', "quel taux, et jusqu'à quand ?"],
               ['le CELI', "l'impôt en prend-il une part ?"],
               ['le REER', "quand paierai-je l'impôt ?"]],
              cle=0,
              note="Le calendrier du projet répond avant le rendement.",
              notes="Diapositive à photographier. Elle prépare le travail de lecture de "
                    "C2, où le document répond aux quatre questions.")

    d.vocabulaire('Vocabulaire', "Quatre mots de l'épargne", [
        ("un placement", "De l'argent mis quelque part pour qu'il rapporte, au lieu de dormir dans un compte."),
        ("le rendement", "Ce que rapporte l'argent placé, sur une période donnée."),
        ("un dépôt à terme", "De l'argent laissé à l'institution pour une durée fixée, à un taux connu dès le départ."),
        ("l'assurance-dépôts", "La protection publique qui rembourse l'argent déposé si l'institution fait faillite."),
    ], notes="« L'assurance-dépôts » ne se demande pas et ne se paie pas. Le dire en "
             "présentant le mot : c'est la seule chose que les élèves doivent en "
             "retenir.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la rencontre avec madame Pomerleau.", [
        ("La conseillère demande d'abord quand l'argent sera nécessaire.", "vrai"),
        ("Un projet à deux ans permet des placements qui montent et qui descendent.", "faux - il n'y aurait pas le temps de se refaire"),
        ("Le CELI est lui-même un placement.", "faux - c'est un abri fiscal"),
        ("On peut mettre un dépôt à terme dans un CELI.", "vrai"),
        ("Le REER efface l'impôt sur l'argent qu'on y met.", "faux - il le déplace"),
        ("Les dépôts sont protégés jusqu'à cent mille dollars par catégorie.", "vrai"),
    ], corrige=True,
       notes="Le cinquième est le plus important : le REER déplace l'impôt, il ne "
             "l'efface pas. Le faire redire par trois élèves.")

    d.billet("Écris en une phrase ce que tu demanderais en premier si tu avais deux "
             "mille dollars à placer.",
             exemples=["Je demanderais quand je peux le reprendre.",
                       "Je demanderais si l'argent est protégé."],
             notes="Deux minutes. Les billets qui parlent du rendement avant la date "
                   "montrent que le message du jour n'est pas passé : y revenir en C2.")

    return d.save(dossier)
