# -*- coding: utf-8 -*-
"""A3 · Le nom caché sous le verbe
Bloc A « Je découvre » · couleur ambre · 75 min. Formation des mots.
Source : exercice `prMots` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre='Le nom caché sous le verbe',
        chapeau="Un relevé n'écrit pas « vous devez payer avant le douze ». "
                "Il écrit « échéance du paiement ». Retrouver le verbe sous "
                "le nom, c'est lire à la vitesse normale.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire lexicale. Elle a l'air technique et elle est "
                  "immédiatement utile : les mots vus ici sont ceux des documents des "
                  "blocs B, C et D.")

    d.objectifs([
        "reconnaître un nom formé sur un verbe ;",
        "former un nom en -ment, en -tion et en -ance ;",
        "donner le genre d'un nom d'après son suffixe ;",
        "revenir au verbe pour comprendre une ligne de document.",
    ], notes="Le quatrième objectif est le seul qui compte vraiment : la formation des "
             "mots n'est ici qu'un moyen de lire.")

    d.declencheur(
        'Observation', "Pourquoi les documents écrivent-ils des noms plutôt que des "
                       "verbes ?",
        pistes=[
            "« échéance du paiement » ou « vous devez payer avant le douze » ?",
            "Lequel des deux tient dans une colonne de tableau ?",
            "Lequel des deux dit qui fait l'action ?",
            "Lequel des deux se comprend le plus vite ?",
        ],
        notes="La bonne réponse à la troisième question est instructive : le nom permet "
              "de ne nommer personne. Ce n'est pas un hasard, et le groupe le sent.")

    d.tableau('Analyse', "Trois suffixes, trois genres",
              ['Suffixe', 'Ce que ça donne'],
              [['-ment', 'masculin : le remboursement, le placement'],
               ['-tion', 'féminin : une opération, une contestation'],
               ['-ance', "féminin : l'échéance, l'assurance"],
               ['aucun', 'masculin : un emprunt, un prêt, un retrait']],
              cle=0,
              note="Trois règles couvrent presque tout le vocabulaire financier.",
              notes="Diapositive à photographier. Faire chercher au groupe un cinquième "
                    "exemple pour chaque ligne avant de passer à la suite.")

    d.regle("Le suffixe donne le genre",
            "-ment fait un nom masculin ; -tion et -ance font un nom féminin.",
            precision="C'est une des rares règles de genre du français qui n'ait pas "
                      "d'exception utile. Elle vaut bien au-delà de la banque : "
                      "l'inscription, la réparation, le renseignement, le "
                      "déménagement.",
            notes="Diapositive à photographier. Insister : apprendre le suffixe évite "
                  "d'apprendre le genre mot par mot.")

    d.cartes('Vocabulaire', "Du verbe au nom", [
        ('rembourser', 'le remboursement'),
        ('placer', 'le placement'),
        ('prélever', 'le prélèvement'),
        ('contester', 'une contestation'),
        ('cotiser', 'une cotisation'),
        ('échoir', "l'échéance"),
        ('emprunter', 'un emprunt'),
        ('retirer', 'un retrait'),
    ], notes="« Échoir » est le seul verbe rare de la liste, et son nom est partout. Le "
             "dire : on n'a pas besoin de savoir employer le verbe pour comprendre le "
             "nom.")

    d.pratique('Application', "Complétez avec le nom de la même famille",
               "Le verbe est entre parenthèses.", [
        ("Elle rembourse chaque mois : le ___ dure quatre-vingts versements.", "remboursement"),
        ("L'argent est placé pour deux ans : c'est un ___ à court terme.", "placement"),
        ("Une somme est retirée chaque mois : c'est un ___ automatique.", "prélèvement"),
        ("Elle conteste le montant : sa ___ est ouverte le jour même.", "contestation"),
        ("Elle cotise à son régime : sa ___ est déductible.", "cotisation"),
        ("Le paiement échoit le douze : l'___ est donc le douze.", "échéance"),
        ("Elle emprunte douze mille dollars : son ___ dure six ans.", "emprunt"),
    ], corrige=True,
       notes="Faire dire le nom avec son article : c'est là que se voit la maîtrise du "
             "genre, pas dans le mot seul.")

    d.piege('Le piège', "la déduisation, le contestement",
            "la déduction, la contestation",
            "Un suffixe ne se colle pas au hasard sur un verbe : chaque famille a son "
            "nom, et il s'apprend avec elle. Le bon réflexe n'est pas d'inventer mais "
            "de relever le nom dans le document, où il est déjà écrit.",
            notes="Le dire clairement : on ne devine pas un nom, on le relève. C'est "
                  "une méthode de lecture, pas une règle de fabrication.")

    d.tableau('Application', "Ce que la ligne veut dire",
              ['Sur le document', 'Autrement dit'],
              [['le prélèvement automatique', "on vous prend l'argent chaque mois"],
               ["l'immobilisation des fonds", 'vous ne pouvez pas le reprendre'],
               ['la déduction du revenu', "on l'enlève de votre revenu imposable"],
               ['le remboursement anticipé', 'payer avant la date prévue'],
               ['la protection des dépôts', "l'argent est remboursé si tout tombe"]],
              cle=0,
              notes="Diapositive à photographier. Elle sert de corrigé au travail de "
                    "lecture du bloc C : les cinq lignes y reviennent telles quelles.")

    d.billet("Choisis trois verbes de la séance et écris leur nom avec son article.",
             exemples=["rembourser : le remboursement",
                       "contester : une contestation"],
             notes="Deux minutes. Vérifier surtout l'article : c'est lui qui prouve que "
                   "la règle du suffixe est passée.")

    return d.save(dossier)
