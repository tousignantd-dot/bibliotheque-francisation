# -*- coding: utf-8 -*-
"""A3 · Les mots de la fiche.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercices `prVocab`, `prImg` et `prCases`, cartes mémoire.

Dernière séance du bloc A. Elle ferme le vocabulaire du module : treize mots,
dont onze illustrés, tous repris dans les deux défis.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Les mots de la fiche',
        chapeau="Treize mots suffisent pour lire n'importe quelle fiche "
                "d'inscription — et ce sont les mêmes partout.",
        duree='60 minutes')

    d.titre(notes="Séance de vocabulaire. Reprendre la fiche vierge distribuée en A1 : "
                  "chaque mot vu ici se montre du doigt dessus.")

    d.objectifs([
        "nommer les huit cases d'une fiche ;",
        "dire ce qu'on écrit dans chacune ;",
        "reconnaître les mots à l'écrit ;",
        "demander « qu'est-ce que j'écris ici ? ».",
    ])

    d.vocabulaire('Vocabulaire', "La fiche et ses cases", [
        ("une inscription", "Le moment où on donne son nom pour entrer dans un cours."),
        ("une fiche", "La feuille de papier où on écrit ses renseignements."),
        ("une case", "Le petit rectangle où on écrit une seule chose."),
        ("remplir", "Écrire dans toutes les cases d'une feuille."),
        ("le nom de famille", "Le nom de vos parents, celui que toute la famille porte."),
        ("le prénom", "Le nom qu'on vous donne à la naissance, à vous seul."),
        ("la date de naissance", "Le jour, le mois et l'année où vous êtes né."),
    ], notes="Faire répéter chaque mot avec son article. Montrer la case correspondante "
             "sur la fiche vierge en même temps.")

    d.vocabulaire('Vocabulaire', "Où vous joindre", [
        ("l'année", "Douze mois. 1992, 2026 sont des années."),
        ("l'adresse", "Le numéro, la rue et la ville où vous habitez."),
        ("un appartement", "Un logement dans un immeuble. Il porte un numéro."),
        ("le code postal", "Six caractères qui disent au facteur où aller."),
        ("le téléphone", "L'appareil pour parler de loin. Son numéro a dix chiffres."),
        ("le courriel", "L'adresse pour recevoir des messages sur un écran."),
    ], notes="Ces six-là sont les cases du bas de la fiche : tout le défi 2 en dépend.")

    d.regle("Une case, un renseignement",
            "Jamais deux choses dans la même case.",
            precision="Le nom de famille dans la case du nom, le prénom dans la case du "
                      "prénom. Quand une case ne vous concerne pas, on écrit un trait : "
                      "<b>—</b>. Une case laissée vide fait croire à un oubli, et on vous "
                      "rappellera pour rien.",
            notes="Diapo à photographier. C'est la règle qui évite le plus de fiches "
                  "renvoyées.")

    d.tableau('Analyse · 1 de 2', "Les cases du haut",
              ['La case', 'Ce qu\'on y écrit'],
              [["NOM DE FAMILLE", "DAOUD"],
               ["PRÉNOM", "YUSUF"],
               ["SEXE", "H ou F"],
               ["DATE DE NAISSANCE", "12 / 03 / 1992"]],
              cle=2,
              note="Elles font le défi 1.",
              notes="Diapo à photographier. Montrer les quatre sur la fiche vierge.")

    d.tableau('Analyse · 2 de 2', "Les cases du bas",
              ['La case', 'Ce qu\'on y écrit'],
              [["ADRESSE", "3120, av. Papineau, app. 4"],
               ["VILLE, PROV.", "Montréal, QC"],
               ["TÉL.", "514 555 0198"],
               ["COURRIEL", "yusuf.daoud@courriel.ca"]],
              cle=2,
              note="Elles font le défi 2.",
              notes="Diapo à photographier. Ne pas expliquer les abréviations ici : elles "
                    "sont le sujet de la séance C1. Dire seulement qu'on y reviendra.")

    d.pratique('Pratique', "Qu'est-ce qu'on écrit ?",
               "Complétez d'après le dialogue de la séance A1.", [
        ("NOM DE FAMILLE : ___", "Daoud"),
        ("PRÉNOM : ___", "Yusuf"),
        ("Il y a huit ___ dans la fiche.", "cases"),
        ("Écrivez en lettres ___ .", "majuscules"),
    ], corrige=True, cols=1,
       notes="Ce sont les quatre énoncés de l'exercice `prCases`. Les faire au tableau, "
             "puis à l'ordinateur.")

    d.pratique('Pratique · à deux', "Montrez-moi la case",
               "L'un nomme un mot, l'autre montre la case sur la fiche.", [
        ("Tour 1", "une case · une fiche · remplir"),
        ("Tour 2", "le nom de famille · le prénom"),
        ("Tour 3", "la date de naissance · l'année"),
        ("Tour 4", "l'adresse · le téléphone · le courriel"),
    ], cols=1,
       notes="Quinze minutes. Les cartes mémoire de la section « Je retiens des mots » "
             "reprennent exactement ces treize mots, avec leur photo.")

    d.billet(
        "Écrivez trois mots de la fiche, avec leur article.",
        exemples=[
            "Un mot que vous connaissiez déjà.",
            "Un mot appris aujourd'hui.",
            "Un mot que vous trouvez difficile.",
        ],
        notes="Le troisième renseigne sur ce qu'il faudra reprendre en B1.")

    return d.save(dossier)
