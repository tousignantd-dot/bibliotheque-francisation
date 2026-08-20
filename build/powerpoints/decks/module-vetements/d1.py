# -*- coding: utf-8 -*-
"""D1 · Échanger un article.
Bloc D « Défi 3 · Échanger, rembourser, mettre de côté » · acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3echange`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-vetements/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Échanger un article',
        chapeau="La facture, les étiquettes, la boîte, et le délai. Quatre "
                "conditions, et un comptoir qui n'est pas la caisse. Un "
                "échange bien préparé prend trois minutes.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc D. Demander qui a déjà fait un échange au Québec, et "
                  "comment ça s'est passé. Les récits sont souvent instructifs.")

    d.objectifs([
        "demander un échange au bon comptoir ;",
        "présenter la facture et expliquer le motif ;",
        "distinguer échange, remboursement et note de crédit ;",
        "connaître le délai et les exceptions.",
    ])

    d.declencheur(
        'Observation', "Où faut-il aller pour un échange ?",
        image=IMG + 'comptoir-service.jpg',
        pistes=[
            "Est-ce la même file que pour payer ?",
            "Qu'est-ce qu'il faut apporter ?",
            "Combien de temps a-t-on pour revenir ?",
            "Est-ce que tout s'échange ?",
        ],
        notes="Beaucoup de gens font la file à la caisse et sont renvoyés au fond du "
              "magasin. Le comptoir s'appelle « service à la clientèle ».")

    d.dialogue('Dialogue · 1 de 3', "La demande", [
        ("KOFI", "Bonjour. Je voudrais échanger ces bottes, s'il vous plaît.", True),
        ("RÉMI", "Bien sûr. Vous avez la facture ?", True),
        ("KOFI", "Oui, la voici. Je les ai achetées samedi.", True),
        ("RÉMI", "Parfait. Qu'est-ce qui ne va pas ?", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Je voudrais échanger… » : la formule d'ouverture. La facture arrive tout de "
             "suite après — c'est la première chose qu'on demande.")

    d.dialogue('Dialogue · 2 de 3', "Le motif", [
        ("KOFI", "Elles sont trop petites pour mon fils. Il fait du 4, pas du 3.", True),
        ("RÉMI", "D'accord. Est-ce qu'il les a portées dehors ?", True),
        ("KOFI", "Non, seulement essayées dans la maison. J'ai gardé la boîte.", True),
        ("RÉMI", "C'est ce qu'il fallait faire. Je vous cherche le 4.", True),
    ], notes="Trois choses le sauvent : pas portées dehors, la boîte gardée, la facture. "
             "Les faire nommer par le groupe.")

    d.dialogue('Dialogue · 3 de 3', "La différence de prix", [
        ("RÉMI", "Le 4 coûte cinq dollars de plus. Ça vous va ?", True),
        ("KOFI", "Oui, ça va. Je paie la différence où ?", True),
        ("RÉMI", "Ici, je m'en occupe. Gardez la nouvelle facture pour trente jours.", True),
        ("KOFI", "Merci beaucoup.", False),
    ], notes="« Je paie la différence où ? » : question pratique et fréquente. La nouvelle "
             "facture repart un nouveau délai.")

    d.tableau('Analyse', "Trois choses différentes",
              ['Le mot', "Ce qu'on reçoit"],
              [["un échange", "un autre article"],
               ["un remboursement", "son argent"],
               ["une note de crédit", "un crédit au magasin"],
               ["la mise de côté", "l'article gardé, contre un dépôt"]],
              cle=2,
              note="La note de crédit ne se dépense que dans ce magasin.",
              notes="Diapo à photographier. Beaucoup d'élèves demandent un remboursement et "
                    "acceptent une note de crédit sans comprendre la différence.")

    d.regle("Quatre conditions",
            "la facture, les étiquettes, l'état, le délai",
            precision="La <b>facture</b> prouve l'achat. Les <b>étiquettes</b> attachées "
                      "prouvent que l'article n'a pas servi. L'<b>état</b> doit être neuf — "
                      "des bottes portées dehors ne se reprennent pas. Le <b>délai</b> est "
                      "de quinze à trente jours selon le magasin, et il est écrit sur la "
                      "facture.",
            notes="Diapo à photographier. C'est la diapo centrale du bloc D.")

    d.cartes("Ce qui ne se reprend jamais", "Trois familles", [
        ("Les sous-vêtements et les maillots",
         "Pour des raisons d'hygiène. Aucun magasin ne fait exception."),
        ("Les articles en solde final",
         "« Vente finale », « solde final » : c'est écrit sur l'étiquette et sur la "
         "facture. Lire avant de payer."),
        ("Ce qui a servi",
         "Bottes portées dehors, vêtement lavé, étiquettes coupées. L'article est "
         "considéré comme utilisé."),
    ], notes="La deuxième famille cause le plus de mauvaises surprises : le rabais se paie "
             "par l'impossibilité de revenir.")

    d.piege("Jeter la facture",
            "Je l'ai mise à la poubelle avec le sac.",
            "La photographier tout de suite.",
            "Sans facture, la plupart des magasins refusent, ou offrent au mieux une note de "
            "crédit au prix le plus bas de la saison. Une photo prise dans le stationnement "
            "règle le problème pour toujours — le papier des reçus s'efface en quelques "
            "mois, même bien rangé.",
            notes="Faire prendre l'habitude : photo, puis le papier dans une enveloppe.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Kofi veut se faire rembourser.", "faux — il veut échanger"),
        ("Il a gardé la facture.", "vrai"),
        ("Les bottes ont été portées dehors.", "faux — essayées à la maison"),
        ("Il a gardé la boîte.", "vrai"),
        ("Le 4 coûte le même prix.", "faux — cinq dollars de plus"),
        ("Il doit garder la nouvelle facture.", "vrai — trente jours"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez la première phrase d'un échange, et le motif.",
        exemples=[
            "« Je voudrais échanger… parce que… »",
            "Trois situations différentes.",
        ],
        notes="Ramasser. Ces phrases servent au jeu de rôle de E1.")

    return d.save(dossier)
