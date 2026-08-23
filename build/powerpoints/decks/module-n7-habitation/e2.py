# -*- coding: utf-8 -*-
"""E2 · Écris la lettre qui demande d'intervenir
Bloc E « Je me lance » · couleur framboise · production écrite et bilan ·
75 min.
Source : bloc `appli` de `custom.js` — production écrite — et la section
« Je retiens des mots ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre="Écris la lettre qui demande d'intervenir",
        chapeau="Dix à quatorze phrases, trois paragraphes, un objet, quatre "
                "dates et un délai. Puis on relit trois fois, et on enlève un "
                "adjectif à chaque fois.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du module. La tâche vient directement de la "
                  "troisième intention de la situation : rédiger une lettre pour "
                  "régler un problème.")

    d.objectifs([
        "écrire une mise en demeure en trois paragraphes ;",
        "poser un objet en huit à douze mots ;",
        "donner un délai précis à compter de la réception ;",
        "faire le bilan de ce qu'on est maintenant capable de faire.",
    ], notes="Le deuxième objectif se vérifie en dix secondes et il annonce la qualité "
             "de tout le reste : un objet qui plaide ferme le lecteur.")

    d.declencheur(
        'Préparation', "Que doit contenir la première phrase de ta lettre ?",
        pistes=[
            "Une date ? Un fait ? Une demande ?",
            "Est-ce qu'on commence par ce qu'on ressent ?",
            "Et par ce qu'on veut ?",
            "Relis la lettre de Ruslana : par quoi commence-t-elle ?",
        ],
        notes="La bonne réponse est le fait daté : « Depuis le 4 février, l'occupant "
              "du logement 6 fait fonctionner… » Le laisser venir du groupe.")

    d.tableau('Plan', "Trois paragraphes, un par idée",
              ['Paragraphe', 'Ce qu\'il contient'],
              [["1 · Ce qui se passe", "le fait, les heures, depuis quand, le registre"],
               ["2 · Ce que j'ai déjà fait", "la conversation, la date, ce qui a été tenu"],
               ["3 · Ce que je demande", "la demande précise, le délai, la suite annoncée"]],
              note="Un objet avant la formule d'appel, une salutation fermée après. "
                   "Dix à quatorze phrases en tout.",
              cle=0,
              notes="Diapositive à photographier. Faire écrire le plan avant la "
                    "première phrase : personne n'écrit trois paragraphes sans plan.")

    d.cartes('Exigences', "Huit choses à faire figurer", [
        ("Un objet", "Huit à douze mots, un groupe du nom, jamais une phrase complète."),
        ("Quatre dates", "Depuis le 4 février, le 19 février, le 26 février, au 12 mars."),
        ("Une conséquence", "Cela m'empêche de… ou cela m'oblige à…"),
        ("Une concession", "Bien que… ou même si…"),
        ("Une citation exacte", "Deux-points, guillemets, ses mots — ou pas de guillemets du tout."),
        ("Un connecteur d'annonce", "Quant à… ou en ce qui concerne…"),
        ("Une demande précise", "Ce que vous voulez, en une phrase qui se répond par oui ou non."),
        ("Un délai", "Dix jours à compter de la réception de la présente."),
    ], notes="Distribuer la liste sur papier : c'est la grille de correction, et les "
             "élèves la cochent eux-mêmes avant d'envoyer leur texte.")

    d.piege('Écriture',
            "Je suis épuisée et personne ne m'écoute",
            "Depuis le 26 février, je suis réveillée neuf matins sur quatorze",
            "Écrire la conséquence, pas l'émotion — c'est la règle du module, posée en "
            "A3 et redite par le médiateur en D1. Un sentiment se discute ; un fait "
            "daté ne se discute pas. Dernière relecture : trois passages, et un "
            "adjectif de moins à chaque fois.",
            notes="Faire compter les adjectifs dans la première version de deux ou "
                  "trois lettres. Le chiffre suffit à convaincre.")

    d.pratique('Écriture', "Relisez avant d'envoyer",
               "Six questions à se poser sur son propre texte.", [
        ("Mon objet fait-il moins de douze mots et aucune phrase complète ?", "sinon, le raccourcir"),
        ("Ai-je trois paragraphes séparés par un blanc ?", "sinon, découper"),
        ("Ai-je au moins quatre dates ou heures exactes ?", "sinon, en ajouter"),
        ("Ai-je écrit une conséquence plutôt qu'un sentiment ?", "sinon, réécrire la phrase"),
        ("Ma demande se répond-elle par oui ou par non ?", "sinon, la préciser"),
        ("Ai-je écrit un nombre de jours, à compter de la réception ?", "sinon, l'ajouter"),
    ], corrige=True,
       notes="Faire faire la relecture par un pair avant l'envoi dans le module. "
             "L'assistant corrige la langue ; la grille corrige la structure.")

    d.tableau('Bilan', "Ce que le module a travaillé, bloc par bloc",
              ['Bloc', 'Ce qu\'on sait faire'],
              [["A · Je découvre", "nommer le problème et dire sa conséquence"],
               ["B · Défi 1", "mener la conversation soi-même, sans reproche"],
               ["C · Défi 2", "rapporter fidèlement, et lire le règlement"],
               ["D · Défi 3", "écrire les deux lettres, et ne pas les confondre"],
               ["E · Je me lance", "faire les trois, pour de vrai"]],
              cle=1,
              notes="Diapositive de clôture. Faire l'autoévaluation du module dans la "
                    "section « Je retiens des mots » : seize énoncés, trois choix.")

    d.billet(
        "Qu'est-ce que tu ferais différemment, la prochaine fois qu'un voisin te dérange ?",
        exemples=[
            "Deux phrases suffisent.",
            "Pense à ce que tu ferais dès le troisième jour.",
        ],
        notes="Cinq minutes. Fin du module. La réponse la plus fréquente, et la "
              "meilleure : je noterais tout de suite, et je monterais lui parler avant "
              "d'écrire à qui que ce soit.")

    return d.save(dossier)
