# -*- coding: utf-8 -*-
"""E1 · L'appel pour de vrai, et le récit au médecin.
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : bloc `appli` — jeu de rôle `rendezvous` et production orale.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="L'appel pour de vrai, et le récit au médecin",
        chapeau="Deux productions orales dans la même séance : un appel "
                "mené du début à la fin, puis une minute de récit — trois "
                "mois racontés à quelqu'un qui ne vous connaît pas.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Rendre les messages de D2 corrigés et en lire "
                  "deux à voix haute, sans nommer les auteurs. Le groupe dit lequel il "
                  "rappellerait, et pourquoi.")

    d.objectifs([
        "mener un appel du menu jusqu'à la confirmation ;",
        "poser les questions qu'on n'ose pas poser ;",
        "raconter un problème qui dure, en une minute et en quatre temps ;",
        "s'écouter et se corriger avant d'envoyer.",
    ])

    d.declencheur(
        'Écoute', "Une minute pour raconter trois mois à quelqu'un qui ne vous "
                  "connaît pas. Par quoi commencez-vous ?",
        image=IMG + 'salle-attente.jpg',
        pistes=[
            "Par ce qui fait le plus mal ?",
            "Par le début, avec une date ?",
            "Par ce que vous avez arrêté de faire ?",
            "Combien de phrases avez-vous, en une minute ?",
        ],
        notes="La bonne réponse est la deuxième, mais laisser le groupe défendre les "
              "autres : c'est en les comparant qu'on voit pourquoi le début l'emporte.")

    d.regle("Quatre temps, une minute, aucun mot savant",
            "Le début · le décor à l'imparfait · ce qui a changé au passé composé · aujourd'hui.",
            precision="Puis deux questions à vous. Un récit organisé vaut infiniment mieux "
                      "qu'un vocabulaire médical approximatif : personne ne vous demande "
                      "de nommer une maladie, on vous demande de raconter ce qui vous "
                      "arrive.",
            notes="Diapositive à photographier, et à laisser affichée pendant les "
                  "enregistrements.")

    d.cartes("Le jeu de rôle, en trois situations", "L'assistant joue l'agente", [
        ("Le premier rendez-vous",
         "Des étourdissements depuis trois mois. Vous voulez votre médecin, pas le sans-rendez-vous."),
        ("Le rendez-vous qui ne marche plus",
         "Votre horaire a changé. Vous voulez garder le rendez-vous, mais à un autre moment."),
        ("L'annulation de dernière minute",
         "C'est demain et votre enfant est malade. Annuler sans être noté absent, puis en reprendre un."),
        ("Ce qu'il faut savoir",
         "L'agente ne donne jamais un renseignement avant qu'on le lui demande. Comme au vrai téléphone."),
    ], notes="Faire essayer les deux rôles à ceux qui vont vite : jouer l'agente oblige à "
             "poser les questions, ce qui apprend à les entendre.")

    d.tableau('Les sept choses à faire pendant l\'appel',
              "La liste que porte le module",
              ['Moment', 'Ce qu\'on dit'],
              [["Ouvrir", "pourquoi vous appelez, en une phrase"],
               ["S'identifier", "le nom, épelé, et le numéro de carte"],
               ["Le motif", "ce que vous avez, et depuis quand"],
               ["Conclure", "l'heure d'arrivée, ce qu'il faut apporter, le délai, et répéter"]],
              cle=0,
              notes="Les sept items complets sont à l'écran dans le module. Ici, on garde "
                    "les quatre moments : c'est ce qu'on retient en jouant.")

    d.pratique('Production orale', "Racontez, en quatre temps",
               "Une minute. Écoutez-vous ensuite comme si vous étiez le médecin.", [
        ("TEMPS 1 · Le problème et depuis quand.", "« J'ai des étourdissements depuis le mois de mars. »"),
        ("TEMPS 2 · Le décor, et à quel moment ça arrive.", "« Je me levais et tout tournait. Ça m'arrive en me levant. »"),
        ("TEMPS 3 · Ce qui a changé.", "« Au début, une fois par semaine. La semaine dernière, j'ai dû m'asseoir. »"),
        ("TEMPS 4 · Vos deux questions.", "« Est-ce que je dois arrêter de travailler ? Et si ça empire ? »"),
    ], corrige=True,
       notes="Chacun s'enregistre dans le module, s'écoute, corrige, puis envoie. Le "
             "deuxième enregistrement est presque toujours meilleur : exiger qu'on "
             "s'écoute avant d'envoyer.")

    d.piege("Réciter une liste de symptômes",
            "« Étourdissements, fatigue, ça tourne, mal de tête. »",
            "« Ça a commencé en mars. Je me levais et tout tournait… »",
            "Une liste dit ce qu'on a ; un récit dit comment ça évolue. C'est l'évolution "
            "qui permet de décider quoi chercher, et elle ne tient pas dans une "
            "énumération.",
            notes="Rejouer les deux versions à voix haute si le groupe hésite : la "
                  "différence s'entend en dix secondes.")

    d.billet(
        "Écoutez votre enregistrement une dernière fois, puis répondez en une phrase.",
        exemples=[
            "Le médecin saurait-il quand ça a commencé, à quel moment ça arrive, et si ça empire ?",
            "Si une des trois manque, refaites-le avant d'envoyer.",
        ],
        notes="Le contrôle est le même que celui de la mini-leçon du module. Il rend "
              "l'élève capable de se corriger seul, ce qui est le but de la séance.")

    return d.save(dossier)
