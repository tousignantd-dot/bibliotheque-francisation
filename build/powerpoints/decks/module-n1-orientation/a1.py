# -*- coding: utf-8 -*-
"""A1 · Le dessin et le mot.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `pr1` et `prImg`.

Troisième module du niveau 1 : le stade est celui du grand débutant, et
plusieurs élèves ne décodent pas encore une syllabe. Les diapositives portent
donc peu de mots, et tout ce qui est projeté est aussi montré du doigt dans le
corridor pendant la séance.

Aucune image dans ces huit séances : les vingt images du module ne sont pas
encore produites, et une diapositive qui appelle un fichier absent arrête la
construction. Les pictogrammes se montrent en vrai, sur les portes du centre —
ce qui vaut mieux qu'une projection.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Le dessin et le mot',
        chapeau="Un panneau dit deux fois la même chose : une fois en dessin, "
                "une fois en lettres. Savoir cela, c'est déjà savoir lire un "
                "bâtiment.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Commencer par une marche de dix minutes "
                  "dans le corridor, en groupe, sans rien expliquer : chacun montre du "
                  "doigt un panneau qu'il comprend déjà. Il y en a toujours.")

    d.objectifs([
        "reconnaître un panneau dans un bâtiment ;",
        "dire ce que montre le dessin ;",
        "comprendre que le mot écrit dit la même chose ;",
        "nommer quatre lieux du centre.",
    ])

    d.declencheur(
        'Observation', "Vous êtes déjà capables de lire cela",
        pistes=[
            "Un homme et une femme sur une porte : c'est quoi ?",
            "Une fourchette et un couteau : c'est quoi ?",
            "Une cigarette avec une barre rouge : c'est quoi ?",
            "Comment le savez-vous, sans lire les mots ?",
        ],
        notes="Laisser répondre dans la langue qu'on peut. Le point à faire ressortir : "
              "ils lisent déjà les panneaux. Ce qui est neuf, ce sont les mots écrits à "
              "côté — pas le sens.")

    d.dialogue('Dialogue · 1 de 2', "Deux portes", [
        ("ROSA", "Kofi ! Je cherche les toilettes.", True),
        ("KOFI", "Regarde le dessin, là-bas.", True),
        ("ROSA", "Il y a deux portes. Deux dessins.", True),
        ("KOFI", "Oui. Un dessin d'homme, un dessin de femme.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire écouter deux fois, diapositive masquée. Puis afficher et faire "
             "répéter réplique par réplique, en chœur.")

    d.dialogue('Dialogue · 2 de 2', "Le dessin et le mot", [
        ("ROSA", "Et le mot ? C'est écrit quoi ?", True),
        ("KOFI", "TOILETTES. Le même mot sur les deux portes.", True),
        ("ROSA", "Ah ! Le dessin dit qui. Le mot dit quoi.", True),
        ("KOFI", "C'est ça. Toujours.", True),
    ], notes="La phrase de Rosa est la phrase du module entier. L'écrire au tableau et "
             "l'y laisser les huit séances.")

    d.regle("Un panneau dit deux fois la même chose",
            "Le dessin, puis le mot.",
            precision="Le <b>dessin</b> se comprend tout de suite, dans toutes les "
                      "langues. Le <b>mot</b> écrit à côté dit exactement la même "
                      "chose, en français. Quand on ne lit pas encore, on regarde le "
                      "dessin — et on apprend le mot en même temps, gratuitement.",
            notes="Diapositive à photographier. C'est la seule règle de la séance, et "
                  "elle porte tout le module.")

    d.tableau('Analyse', "Six dessins qu'on lit déjà",
              ['Le dessin', 'Ce que ça veut dire'],
              [["un homme, une femme", "les toilettes"],
               ["une fourchette, un couteau", "la cafétéria"],
               ["un adulte, un enfant", "le service de garde"],
               ["quelqu'un qui court", "la sortie"],
               ["une cigarette barrée", "défense de fumer"],
               ["une flèche", "allez par là"]],
              cle=1,
              notes="Diapositive à photographier. Faire nommer chaque dessin à voix "
                    "haute avant d'afficher la deuxième colonne. Aucun de ces dessins "
                    "n'a besoin de mots pour se comprendre : le dire.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Rosa cherche les toilettes.", "vrai"),
        ("Il y a une seule porte.", "faux — il y en a deux"),
        ("Le même mot est écrit sur les deux portes.", "vrai"),
        ("Kofi ne sait pas lire le mot.", "faux — il le lit"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés : à ce stade, six seraient trop.")

    d.pratique('Pratique · debout', "La chasse aux panneaux",
               "En équipes de deux, dans le corridor. Quinze minutes.", [
        ("Étape 1", "Trouvez cinq panneaux."),
        ("Étape 2", "Pour chacun, dites ce que montre le dessin."),
        ("Étape 3", "Montrez le mot écrit à côté, avec le doigt."),
        ("Étape 4", "Revenez et nommez vos cinq panneaux au groupe."),
    ], cols=1,
       notes="Sortir vraiment de la salle. C'est la partie de la séance dont ils se "
             "souviendront. Circuler, ne rien corriger sauf le sens.")

    d.billet(
        "Dessinez un panneau que vous avez vu aujourd'hui.",
        exemples=[
            "Le dessin seulement, sans les mots.",
            "Écrivez en dessous ce que ça veut dire, dans la langue que vous voulez.",
        ],
        notes="Devoir minuscule. Il permet de vérifier, sans écriture, qui a compris "
              "le lien entre le dessin et le lieu.")

    return d.save(dossier)
