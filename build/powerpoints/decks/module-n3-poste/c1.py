# -*- coding: utf-8 -*-
"""C1 · Qu'est-ce qu'il y a dans la boîte ?
Bloc C « Défi 2 · Dire ce qu'il y a dedans, et payer » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-poste/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Qu'est-ce qu'il y a dans la boîte ?",
        chapeau="La question vient chaque fois, et elle n'est pas une "
                "indiscrétion : la préposée doit savoir ce qui voyage. "
                "Trois mots suffisent à répondre.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Prévenir le groupe dès le début : cette question "
                  "surprend et gêne beaucoup de personnes nouvellement arrivées. Dire "
                  "tout de suite qu'elle est posée à tout le monde, sans exception.")

    d.objectifs([
        "comprendre pourquoi la préposée demande le contenu ;",
        "répondre à trois questions de sécurité ;",
        "annoncer son choix en trois mots ;",
        "acheter des timbres et des enveloppes au même comptoir.",
    ])

    d.declencheur(
        'Observation', "Pourquoi faut-il dire ce qu'il y a dedans ?",
        image=IMG + 'carnet-timbres.jpg',
        pistes=[
            "Est-ce que la préposée a le droit d'ouvrir la boîte ?",
            "Qu'est-ce qui ne peut pas voyager par avion ?",
            "Que se passe-t-il si l'objet casse pendant le voyage ?",
            "Est-ce que la question est la même pour tout le monde ?",
        ],
        notes="La réponse honnête : trois raisons — la sécurité, l'assurance en cas de "
              "casse, et les règles de l'avion pour les liquides. Le dire simplement "
              "enlève tout le malaise de la question.")

    d.dialogue('Dialogue · 1 de 3', "Rien de fragile", [
        ("CAROLE", "Qu'est-ce qu'il y a dans la boîte, monsieur ?", True),
        ("YASSINE", "Il y a des vêtements et un livre. Rien de fragile.", True),
        ("CAROLE", "Rien de liquide, rien de dangereux ?", True),
        ("YASSINE", "Non, rien. Juste des vêtements et un livre.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Les trois questions de sécurité — fragile, liquide, dangereux — reviennent "
             "à chaque envoi. Les faire répéter dans l'ordre : c'est une formule fixe.")

    d.dialogue('Dialogue · 2 de 3', "Je vais le prendre", [
        ("CAROLE", "Bon. Alors, standard ou Xpresspost ?", True),
        ("YASSINE", "Le standard. Je vais le prendre.", True),
        ("CAROLE", "Très bien. Il me faut l'adresse complète, avec le code postal.", True),
        ("YASSINE", "Je l'ai écrite sur la boîte. Est-ce que c'est correct ?", True),
    ], notes="« Je vais le prendre » est la phrase du défi 2. Trois mots, et le choix "
             "est fait. La séance C3 lui est entièrement consacrée : ne pas l'expliquer "
             "aujourd'hui, seulement la faire entendre.")

    d.dialogue('Dialogue · 3 de 3', "Autre chose ?", [
        ("YASSINE", "J'aimerais aussi des timbres pour des lettres.", True),
        ("CAROLE", "En carnet ou à l'unité ? Le carnet coûte moins cher.", True),
        ("YASSINE", "Donnez-moi un carnet, s'il vous plaît.", True),
        ("YASSINE", "Je vais en prendre trois. Ça fait combien en tout ?", True),
    ], notes="« Autre chose ? » est l'invitation à demander le reste. Beaucoup d'élèves "
             "partent sans avoir demandé ce dont ils avaient besoin : dire que cette "
             "question-là est faite pour ça.")

    d.tableau('Analyse', "Les trois questions de sécurité",
              ['Ce qu\'on demande', 'La réponse la plus simple'],
              [["Est-ce que c'est fragile ?", "« Rien de fragile. »"],
               ["Est-ce qu'il y a du liquide ?", "« Rien de liquide. »"],
               ["Est-ce qu'il y a quelque chose de dangereux ?", "« Rien de dangereux. »"]],
              cle=1,
              note="Si la réponse est oui, on le dit : la préposée met une étiquette et le prix change parfois.",
              notes="Diapo à photographier. Le mot « rien de » est celui de la séance C2. "
                    "Le faire entendre trois fois aujourd'hui, sans le décomposer.")

    d.regle("Ce qui ne voyage pas par la poste",
            "les liquides inflammables, les aérosols, les piles au lithium seules",
            precision="Un parfum, une bouteille de gaz pour briquet, une batterie "
                      "de téléphone envoyée seule : ces trois-là sont refusés ou "
                      "demandent un envoi spécial. Un appareil avec sa pile dedans, "
                      "lui, passe sans problème.",
            notes="Diapo à photographier. Question posée à chaque groupe : la pile du "
                  "téléphone. La réponse est celle-là — dans l'appareil, ça va ; toute "
                  "seule, non.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("La préposée demande ce qu'il y a dans la boîte.", "vrai"),
        ("Il y a de la vaisselle fragile dans le colis.", "faux — des vêtements et un livre"),
        ("Yassine choisit l'Xpresspost.", "faux — il prend le standard"),
        ("L'adresse de l'expéditeur va en haut à gauche.", "vrai"),
        ("Yassine achète un carnet de timbres.", "vrai"),
        ("Il prend trois enveloppes à deux dollars chacune.", "vrai"),
    ], corrige=True,
       notes="C'est l'exercice `t2vf` du module. Faire justifier chaque « faux » par la "
             "réplique exacte.")

    d.billet(
        "Écrivez ce qu'il y aurait dans votre boîte, et si c'est fragile.",
        exemples=[
            "Employez « il y a » et « rien de ».",
            "Deux phrases suffisent.",
        ],
        notes="Deux minutes. Ces billets deviennent les exemples de la séance C2, qui "
              "travaille exactement ces deux tournures.")

    return d.save(dossier)
