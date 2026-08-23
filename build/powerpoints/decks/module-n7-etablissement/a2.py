# -*- coding: utf-8 -*-
"""A2 · Le « e » qu'on garde et le « e » qui tombe
Bloc A « Je découvre » · couleur indigo · 60 min. Graphie-phonie.
Source : exercice `prE` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le « e » qu'on garde et le « e » qui tombe",
        chapeau="Le français d'ici laisse tomber beaucoup de « e ». Deux "
                "règles disent où il se maintient toujours — et l'une des "
                "deux tient tout le conditionnel de politesse.",
        duree='60 minutes')

    d.titre(notes="Séance courte et très orale. Prévoir que le groupe répète à voix "
                  "haute au moins vingt fois : c'est une séance de bouche, pas de "
                  "cahier.")

    d.objectifs([
        "entendre si le « e » se prononce ou s'il disparaît ;",
        "garder le « e » devant un son « ri » ou « li » ;",
        "garder le « e » de la première syllabe après p, t, c, b, d, g ;",
        "dire « nous serions » et « vous feriez » en trois syllabes.",
    ], notes="Le quatrième objectif est le seul qui compte vraiment pour l'entrevue du "
             "bloc C : c'est le conditionnel de politesse, et il revient à chaque "
             "question.")

    d.declencheur(
        'Écoute', "Combien de syllabes entendez-vous ?",
        pistes=[
            "« une semaine » : deux ou trois ?",
            "« nous serions » : deux ou trois ?",
            "« samedi matin » : trois ou quatre ?",
            "« demander » : deux ou trois ?",
        ],
        notes="Faire lever la main pour chaque réponse avant de donner la règle. Les "
              "désaccords dans le groupe sont l'entrée de la séance.")

    d.regle("Le « e » se garde devant un son « ri » ou « li »",
            "Se-rions, fe-riez, ate-lier, ouv-rier : le « e » ne tombe jamais là.",
            precision="Sans lui, le mot devient imprononçable : essayez « nous "
                      "srions ». C'est la règle la plus utile du module, parce que le "
                      "conditionnel de politesse à « nous » et à « vous » revient à "
                      "chaque question d'entrevue.",
            notes="Diapositive à photographier. Faire essayer la forme fautive à voix "
                  "haute : le groupe entend tout de suite pourquoi la règle existe.")

    d.regle("Le « e » se garde après p, t, c, b, d, g",
            "Te-nir, de-mander, pe-tite, de-venir : première syllabe, consonne dure, "
            "le « e » reste.",
            precision="Ce sont des consonnes qui ferment complètement la bouche. Après "
                      "elles, enchaîner sans « e » est impossible à dire vite. Le "
                      "test : prononcez sans le « e » ; si la bouche bloque, il faut "
                      "le garder.",
            notes="Ne pas employer le mot « occlusive » avec le groupe sans le "
                  "montrer : faire toucher la bouche pendant qu'on dit « te », « pe », "
                  "« de ».")

    d.tableau('Analyse', "Où le « e » tombe, et où il reste",
              ['Le mot', 'Ce qui se passe'],
              [['nous serions', "il reste — suivi de « rions »"],
               ['un atelier', "il reste — suivi de « lier »"],
               ['tenir', "il reste — après un « t »"],
               ['demander', "il reste — après un « d »"],
               ['une semaine', "il tombe — « s » n'est pas une consonne dure"],
               ['je le dis', "il tombe — l'oral courant d'ici"],
               ['samedi', "il tombe — « sam'di »"]],
              cle=0,
              notes="Sept rangées, sans note au bas : le contrôle de densité de "
                    "theme.py l'accepte à cette condition. Faire lire chaque ligne à "
                    "voix haute par un élève différent.")

    d.pratique('Écoute', "Le « e » s'entend, ou il tombe ?",
               "Écoutez, puis dites ce qui se passe dans chaque mot.", [
        ("vous feriez", "le e s'entend"),
        ("un ouvrier", "le e s'entend"),
        ("petite", "le e s'entend"),
        ("une semaine", "le e tombe"),
        ("vous me rappelez", "le e tombe"),
        ("la fenêtre du bureau", "le e tombe"),
    ], corrige=True,
       notes="Dire chaque item deux fois, à débit normal. Ne pas ralentir : un « e » "
             "qui tombe se remet en place dès qu'on articule trop, et l'exercice perd "
             "son objet.")

    d.piege('Piège', "nous srions disponibles",
            "nous serions disponibles",
            "Pour aller vite, on avale le « e » du conditionnel — et le mot le plus "
            "poli de l'entrevue devient inaudible. Trois syllabes : se-ri-ons.",
            notes="Faire répéter la forme juste cinq fois, en chœur puis "
                  "individuellement. C'est la phrase qu'ils diront au bloc C.")

    d.billet("Écris trois mots où le « e » se garde et trois mots où il tombe.",
             exemples=["Il se garde : tenir, demander, nous serions.",
                       "Il tombe : semaine, samedi, je le dis."],
             notes="Ramasser les billets. Un élève qui met « semaine » dans la "
                   "première colonne n'a pas entendu la différence : le reprendre à "
                   "l'oral avant la séance suivante.")

    return d.save(dossier)
