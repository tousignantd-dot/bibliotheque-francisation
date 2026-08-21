# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 75 min.
Source : jeu de rôle `poste`, production orale et production écrite du module,
dialogue `appli`, exercice `aQui`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre='Je me lance',
        chapeau="Tout le module tient dans un échange d'une minute : dire "
                "pourquoi on vient, demander le prix et le délai, dire ce "
                "qu'il y a dedans, choisir. Puis écrire une note.",
        duree='75 minutes')

    d.titre(notes="Séance d'évaluation formative. Prévoir les tablettes ou les portables "
                  "pour le jeu de rôle avec l'assistant, et un casque par élève si "
                  "possible.")

    d.objectifs([
        "tenir une démarche complète au comptoir ;",
        "poser ses questions avant de choisir ;",
        "s'enregistrer, s'écouter et se corriger ;",
        "écrire une courte note à glisser dans le colis.",
    ])

    d.regle("La règle du module, en une phrase",
            "demander avant de dire oui",
            precision="La préposée répond à ce qu'on lui demande, et à rien "
                      "d'autre. Le prix, le délai, ce qui est compris : rien de "
                      "tout cela ne s'annonce tout seul. Trois questions, et "
                      "vous choisissez en connaissance de cause.",
            notes="Diapo à photographier. C'est la phrase que Yassine dit à Denise à la "
                  "fin du module : « Il fallait juste demander avant de dire oui. »")

    d.tableau('Le jeu de rôle', "Trois situations au choix",
              ['La situation', 'Ce que vous venez faire'],
              [["Le colis pour Calgary",
                "un cadeau d'anniversaire pour votre frère, et vous ne savez ni le prix ni le délai"],
               ["Le carton dans la boîte aux lettres",
                "un avis de livraison à la main, et un colis qui vous attend"],
               ["Le déménagement du premier juillet",
                "faire suivre votre courrier à la nouvelle adresse, dans le même quartier"]],
              cle=0,
              note="Chacun choisit sa situation. Les trois demandent les mêmes formules polies.",
              notes="Les trois cas sont ceux du jeu de rôle du module interactif. Laisser "
                    "choisir : un élève qui a une vraie démarche à faire prendra celle-là.")

    d.cartes("La production orale, en trois temps", "Environ 45 secondes", [
        ("TEMPS 1 — Dire pourquoi vous venez",
         "« Bonjour. Je voudrais envoyer ce colis à Calgary, s'il vous plaît. » "
         "Une salutation, une phrase, et la destination."),
        ("TEMPS 2 — Demander le prix et le délai",
         "« Combien est-ce que ça coûte ? Et combien de temps est-ce que ça "
         "prend ? » Les deux questions ensemble, jamais l'une sans l'autre."),
        ("TEMPS 3 — Répondre et choisir",
         "« Il y a des vêtements et un livre, rien de fragile. Je vais le "
         "prendre. » Le contenu, puis le choix en trois mots."),
        ("Avant d'envoyer",
         "Écoutez-vous une fois. Est-ce que les deux questions y sont ? Est-ce "
         "que vous avez dit « rien de fragile » ? Recommencez si nécessaire."),
    ], notes="Les trois temps sont affichés dans le module interactif pendant "
             "l'enregistrement. Les projeter ici aussi : les élèves les regardent en "
             "parlant, et c'est voulu.")

    d.regle("La production écrite",
            "une note à glisser dans le colis",
            precision="De cinq à huit phrases, pour la personne qui va recevoir la "
                      "boîte. Dites ce qu'il y a dedans, quand le colis devrait "
                      "arriver, une chose à laquelle faire attention, et posez-lui "
                      "une question avec « est-ce que ».",
            notes="Diapo à photographier. Insister sur la dernière consigne : la "
                  "question est ce qui transforme la note en vraie communication, et "
                  "c'est un critère du programme.")

    d.tableau('La grille', "Ce que votre note doit contenir",
              ['À vérifier', 'Avec quels mots'],
              [["Ce qu'il y a dans le colis", "il y a, c'est, ce sont"],
               ["Le service choisi et le temps que ça prend", "standard, Xpresspost, une semaine"],
               ["Une chose à laquelle faire attention", "fragile, ne pas plier, rien de liquide"],
               ["Une question posée à la personne", "est-ce que…"]],
              cle=0,
              note="Attention aux petits mots : ce colis, cet avis, cette boîte, ces timbres.",
              notes="Diapo à photographier. C'est la grille exacte du module interactif : "
                    "l'élève la retrouve à l'écran, avec des cases à cocher.")

    d.dialogue('Pour finir', "Ça s'est bien passé ?", [
        ("DENISE", "Alors, ça s'est bien passé au bureau de poste ?", True),
        ("YASSINE", "Très bien. J'ai posé mes questions avant de choisir.", True),
        ("DENISE", "Et tu as pris quoi ?", False),
        ("YASSINE", "Le colis standard. Vingt-deux dollars, une semaine.", True),
        ("DENISE", "Tu vois ? Ce n'était pas si difficile.", True),
        ("YASSINE", "Non. Il fallait juste demander avant de dire oui.", True),
    ], notes="Ce dialogue ferme le module. Le faire écouter à la toute fin de la séance, "
             "après les enregistrements : les élèves y reconnaissent leur propre "
             "démarche, et la dernière réplique est le message du module entier.")

    d.pratique('Compréhension', "Yassine ou Denise ?",
               "Qui dit cette phrase ?", [
        ("« Alors, ça s'est bien passé au bureau de poste ? »", "Denise"),
        ("« J'ai posé mes questions avant de choisir. »", "Yassine"),
        ("« Le colis standard. Vingt-deux dollars, une semaine. »", "Yassine"),
        ("« C'est le bon choix pour un cadeau qui n'est pas pressé. »", "Denise"),
        ("« Il fallait juste demander avant de dire oui. »", "Yassine"),
    ], corrige=True, cols=2,
       notes="C'est l'exercice `aQui` du module. Court : il sert de retour au calme "
             "après les enregistrements.")

    d.billet(
        "Qu'est-ce que vous feriez autrement, la prochaine fois, au comptoir ?",
        exemples=[
            "Une question que vous avez oublié de poser ?",
            "Un mot que vous n'avez pas trouvé assez vite ?",
        ],
        notes="Ramasser. Ces billets disent ce qu'il faut reprendre en E2, et ils "
              "servent d'autoévaluation avant la révision du vocabulaire.")

    return d.save(dossier)
