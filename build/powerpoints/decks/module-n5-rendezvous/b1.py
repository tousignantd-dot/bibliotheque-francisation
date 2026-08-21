# -*- coding: utf-8 -*-
"""B1 · L'appel, du menu jusqu'au numéro.
Bloc B « Défi 1 · L'appel à la clinique » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="L'appel, du menu jusqu'au numéro",
        chapeau="Au bout du fil, il n'y a pas un médecin : il y a une "
                "agente administrative. Elle ne soigne personne, mais "
                "c'est elle qui décide si votre rendez-vous durera quinze "
                "minutes ou trente.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Rendre les billets de A4 corrigés et faire lire "
                  "trois premières phrases d'appel. Le groupe dit laquelle est la plus "
                  "claire — sans nommer les auteurs.")

    d.objectifs([
        "reconnaître les sept moments d'un appel à une clinique ;",
        "dire en une phrase pourquoi on appelle ;",
        "donner son nom, l'épeler, et son numéro de carte ;",
        "comprendre pourquoi l'agente demande le motif.",
    ])

    d.declencheur(
        'Écoute', "« Pour prendre ou annuler un rendez-vous, faites le deux. » Et "
                  "ensuite ?",
        image=IMG + 'appel-carnet.jpg',
        pistes=[
            "Qu'est-ce qu'on dit en premier quand quelqu'un décroche ?",
            "Faut-il raconter tout son problème ?",
            "Qu'est-ce qu'on doit avoir dans la main avant d'appeler ?",
            "Qu'est-ce qu'on note pendant l'appel ?",
        ],
        notes="Laisser le groupe proposer, puis compter combien d'élèves ont répondu "
              "« un papier et un crayon ». C'est presque toujours zéro.")

    d.dialogue('Dialogue · 1 de 3', "Le menu, puis l'identification", [
        ("VOIX", "Vous avez joint la Clinique de la Rive. Pour prendre ou annuler un "
                 "rendez-vous, faites le deux.", False),
        ("MANON", "Clinique de la Rive, Manon à l'appareil.", True),
        ("RACHID", "Bonjour. J'aimerais prendre un rendez-vous avec la docteure "
                   "Fongang, s'il vous plaît.", True),
        ("MANON", "Certainement. Vous êtes inscrit chez elle ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire compter les mots de la deuxième réplique de Rachid : douze. C'est tout "
             "ce qu'il faut pour ouvrir un appel.")

    d.dialogue('Dialogue · 2 de 3', "Le motif, en deux phrases", [
        ("MANON", "Et qu'est-ce qui vous amène ? Je ne demande pas de détails, "
                  "seulement de quoi choisir la bonne durée.", True),
        ("RACHID", "J'ai des étourdissements le matin en me levant. Ça dure depuis "
                   "trois mois, et je suis fatigué tout le temps.", True),
        ("MANON", "D'accord. Trois mois, ce n'est pas rien. Je vous mets une plage de "
                  "trente minutes plutôt que quinze.", True),
        ("RACHID", "Vous avez quelque chose bientôt ?", False),
    ], notes="Le point capital de la séance : c'est la durée annoncée qui fait passer de "
             "quinze à trente minutes. Ne pas dire « trois mois », c'est se donner "
             "soi-même un rendez-vous trop court.")

    d.dialogue('Dialogue · 3 de 3', "Choisir, et expliquer pourquoi", [
        ("MANON", "J'ai le mardi 17 juin à quatorze heures dix, ou le jeudi 19 en fin "
                  "de journée, à dix-sept heures.", True),
        ("RACHID", "Je finis à seize heures. Le jeudi 19, ce serait plus simple.", True),
        ("MANON", "Jeudi 19 juin, dix-sept heures, avec la docteure Fongang. "
                  "Présentez-vous quinze minutes avant, à l'accueil.", True),
        ("RACHID", "Quinze minutes avant. Est-ce que je dois apporter quelque chose ?", True),
    ], notes="Faire remarquer que Rachid ne dit pas « non » : il explique sa contrainte. "
             "Une contrainte expliquée se contourne, un refus sec ne se contourne pas.")

    d.regle("Une contrainte s'explique, elle ne se refuse pas",
            "« Je finis à seize heures » ouvre une porte ; « ça ne marche pas » la ferme.",
            precision="L'agente ne connaît ni votre horaire, ni votre garderie, ni votre "
                      "autobus. Dire pourquoi un moment ne convient pas lui permet de "
                      "chercher au bon endroit du premier coup.",
            notes="Diapositive à photographier. Elle vaut bien au-delà de la clinique : "
                  "c'est la même mécanique au travail et à l'école.")

    d.cartes("Les sept moments de l'appel", "Dans cet ordre, toujours", [
        ("1 · Le menu, puis l'attente",
         "Une voix enregistrée, un choix à faire. On écoute et on appuie."),
        ("2 · Dire ce qu'on veut, en une phrase",
         "Pas son histoire : sa demande. Un verbe, une personne."),
        ("3 · S'identifier",
         "Nom, souvent épelé, et numéro de carte d'assurance maladie."),
        ("4 · Dire le motif en deux phrases",
         "Assez pour choisir la durée — pas un récit médical."),
        ("5 · Choisir un moment",
         "Ce qui est possible, et pourquoi le reste ne l'est pas."),
        ("6 · Poser ses questions",
         "Heure d'arrivée, quoi apporter, faut-il être à jeun."),
    ], cols=3,
       notes="Le septième moment — répéter pour confirmer — fait l'objet de la séance B4. "
             "L'annoncer sans le développer.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'appel.", [
        ("Le menu dit quoi faire si l'on croit vivre une urgence.", "vrai"),
        ("Rachid épelle son nom sans qu'on le lui demande.", "vrai"),
        ("Manon veut connaître tous les détails médicaux.", "faux — de quoi choisir la durée"),
        ("Manon réserve trente minutes à cause des trois mois.", "vrai"),
        ("Rachid choisit le mardi parce qu'il finit à midi.", "faux — il finit à seize heures"),
        ("Il faut se présenter quinze minutes avant.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Les élèves répondent "
             "souvent de mémoire plutôt que d'après le texte.")

    d.billet(
        "Écrivez la phrase par laquelle vous ouvrirez votre appel.",
        exemples=[
            "Une seule phrase : ce que vous voulez, et avec qui.",
            "Puis une deuxième : ce que vous avez, et depuis quand.",
        ],
        notes="Deux phrases, pas trois. Refuser gentiment les billets qui racontent toute "
              "une histoire : c'est précisément le travail de la séance.")

    return d.save(dossier)
