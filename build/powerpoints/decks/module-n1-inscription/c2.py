# -*- coding: utf-8 -*-
"""C2 · Dire un numéro, un code, un courriel.
Bloc C « Défi 2 » · couleur ambre · 60 min.
Source : mini-leçon `t2tel`, exercice `t2tel`, dialogue `appli`.

Dernière séance avant « Je me lance ». Elle réunit le point de phonétique de
A2 et les cases du bas de la fiche : c'est là qu'on se fait le plus souvent
répéter, et c'est normal.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Dire un numéro, un code, un courriel',
        chapeau="Trois suites de caractères qui ne se disent pas comme des "
                "mots : un par un, lentement, avec des pauses.",
        duree='60 minutes')

    d.titre(notes="Prévoir le son : la séance est surtout orale. Demander à chacun d'avoir "
                  "son vrai numéro de téléphone écrit devant lui.")

    d.objectifs([
        "dire un numéro de téléphone chiffre par chiffre ;",
        "dire un code postal ;",
        "dire un courriel avec « point » et « arobase » ;",
        "demander de répéter plus lentement.",
    ])

    d.dialogue('Dialogue', "Je relis votre fiche", [
        ("MADAME CÔTÉ", "Quel est votre code postal ?", True),
        ("YUSUF", "H, deux, K. Un, N, quatre.", True),
        ("MADAME CÔTÉ", "Merci. Et votre courriel ?", True),
        ("YUSUF", "Pardon ? Plus lentement, s'il vous plaît.", True),
        ("MADAME CÔTÉ", "Votre courriel. Votre adresse pour les messages.", True),
        ("YUSUF", "Ah oui. yusuf point daoud, arobase, courriel point c a.", True),
        ("MADAME CÔTÉ", "Parfait. Votre fiche est complète. Bienvenue !", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Yusuf ne comprend pas « courriel » et le dit. Madame Côté ne répète pas plus "
             "fort : elle explique avec d'autres mots. Faire remarquer les deux.")

    d.tableau('Analyse', "Trois suites, trois façons de les dire",
              ['On écrit', 'On dit'],
              [["514 555 0198", "cinq · un · quatre — cinq · cinq · cinq — zéro…"],
               ["H2K 1N4", "H · deux · K — un · N · quatre"],
               ["@", "arobase"],
               [".", "point"]],
              cle=2,
              note="Un caractère à la fois, avec une pause entre les groupes.",
              notes="Diapo à photographier. Lire la première ligne en entier à voix haute, "
                    "lentement, avant de passer à la suite.")

    d.regle("Un par un, jamais deux par deux",
            "Cinq, un, quatre — pas « cinq cent quatorze ».",
            precision="Le numéro de téléphone a <b>dix chiffres</b> en trois groupes. Les "
                      "trois premiers sont l'indicatif de la région : 514 et 438 à "
                      "Montréal, 450 autour, 418 à Québec. En France on regroupe les "
                      "chiffres deux par deux ; ici, un par un, toujours.",
            notes="Diapo à photographier. Les élèves venus d'Europe francophone entendront "
                  "la différence tout de suite : la nommer, plutôt que de la corriger.")

    d.cartes("Le code postal", "Six caractères, deux groupes", [
        ("Trois, puis trois",
         "Lettre, chiffre, lettre — espace — chiffre, lettre, chiffre. H2K 1N4."),
        ("La première lettre dit la région",
         "H sur l'île de Montréal, G du côté de Québec, J dans les environs."),
        ("Jamais un mot",
         "Un code postal ne se prononce pas : il s'épelle, comme un nom."),
        ("À faire confirmer",
         "« H, comme dans hôpital ? » — la même astuce que pour épeler son nom."),
    ], notes="Diapo à photographier. Faire trouver à chacun sa première lettre : elle "
             "correspond presque toujours au quartier.")

    d.pratique('Pratique', "Complétez",
               "Les cases du bas de la fiche.", [
        ("Un numéro de téléphone a ___ chiffres.", "dix"),
        ("Un code postal a trois lettres et trois ___ .", "chiffres"),
        ("Dans H2K 1N4, la première lettre est ___ .", "H"),
        ("Le signe @ se dit ___ .", "arobase"),
        ("On dit les chiffres un par ___ .", "un"),
    ], corrige=True, cols=1,
       notes="Ce sont les cinq énoncés de l'exercice `t2tel`.")

    d.piege("Ne pas oser faire répéter",
            "Faire oui de la tête et écrire un chiffre au hasard.",
            "« Pardon ? Pouvez-vous répéter le dernier chiffre ? »",
            "Un chiffre mal noté, et l'appel du centre ne vous arrive jamais : ni le "
            "rappel du cours, ni la convocation, ni le message de l'enseignante. Faire "
            "répéter prend cinq secondes et se fait à chaque fois qu'il le faut.",
            notes="C'est le piège le plus utile du module. Le relier au « plus lentement, "
                  "s'il vous plaît » du module précédent.")

    d.pratique('Pratique · à deux', "Dictée de coordonnées",
               "L'un dicte, l'autre écrit, puis on vérifie caractère par caractère.", [
        ("Tour 1", "un numéro de téléphone"),
        ("Tour 2", "un code postal"),
        ("Tour 3", "un courriel, avec « point » et « arobase »"),
        ("Tour 4", "les trois de suite, sans s'arrêter"),
    ], cols=1,
       notes="Vingt minutes. Interdire d'écrire pendant qu'on dicte au tour 4 : il faut "
             "écouter en entier, puis demander de répéter. C'est la vraie situation.")

    d.billet(
        "Écrivez vos trois coordonnées, puis dites-les à voix haute.",
        exemples=[
            "Votre numéro de téléphone, en trois groupes.",
            "Votre code postal, en deux groupes.",
            "Votre courriel, si vous en avez un.",
        ],
        notes="Ce billet est le brouillon de la fiche écrite de la séance E1. Le rendre "
              "corrigé au début de E1.")

    return d.save(dossier)
