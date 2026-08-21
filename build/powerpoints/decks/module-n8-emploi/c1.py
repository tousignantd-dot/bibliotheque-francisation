# -*- coding: utf-8 -*-
"""C1 · La réunion du mardi : deux fournisseurs, une décision.
Bloc C « Défi 2 · La réunion » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n8-emploi/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="La réunion du mardi",
        chapeau="Deux fournisseurs, quarante mille dollars d'écart, et une "
                "donnée que personne n'avait regardée. Dans une réunion de "
                "décision, celui qui parle le plus fort ne gagne pas.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 2. Demander qui assiste à des réunions au travail, "
                  "et qui y prend la parole. L'écart entre les deux réponses est le "
                  "sujet de tout le bloc.")

    d.objectifs([
        "suivre une discussion à trois voix sur un dossier chiffré ;",
        "distinguer l'argument de prix de l'argument de délai ;",
        "repérer le moment où le portrait change ;",
        "relever les décisions, les responsables et les échéances.",
    ], notes="L'objectif 4 annonce le compte rendu de C4. Prévenir dès maintenant que "
             "les élèves écriront ce compte rendu.")

    d.declencheur(
        'Observation', "Comment se prend une décision, chez vous ?",
        image=IMG + 'entrepot-quincaillerie.jpg',
        pistes=[
            "Qui décide vraiment ?",
            "Est-ce qu'on vous demande votre avis ?",
            "Est-ce qu'on écoute l'employé qui connaît le terrain ?",
            "Comment saurait-on que vous n'êtes pas d'accord ?",
        ],
        notes="La quatrième piste est celle qui compte. Beaucoup diront « on ne le "
              "saurait pas » : c'est exactement ce que le Défi 2 vient corriger.")

    d.dialogue('Dialogue · 1 de 3', "Le prix, d'abord", [
        ("MANON", "Notre fournisseur actuel augmente ses prix de neuf pour cent. J'ai une soumission qui arrive huit pour cent en bas.", True),
        ("YVES", "Moi je dis oui. Huit pour cent sur notre volume, c'est autour de quarante mille par année.", True),
        ("NADIA", "Si je résume ce que vous venez de dire : l'écart est réel. Cependant, il y a une donnée qui n'est pas dans la soumission.", True),
        ("NADIA", "Lachance livre en dix jours ouvrables ; Ferrico livre en quatre.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Nadia résume avant d'objecter. C'est ce qui fait qu'Yves l'écoute au lieu "
             "de se braquer. Faire relever la formule exacte.")

    d.dialogue('Dialogue · 2 de 3', "Le chiffre qui change tout", [
        ("YVES", "Dix jours ? Es-tu sûre de ton affaire ?", True),
        ("NADIA", "C'est écrit à la page quatre de leur soumission. J'ai vérifié deux fois.", True),
        ("YVES", "Ça me force à doubler mon stock. Donc je récupère du prix, mais je le remets en inventaire.", True),
        ("NADIA", "J'ai fait le calcul : le stock supplémentaire mangerait la moitié de l'économie. Il resterait vingt mille.", True),
    ], notes="Nadia répond à la mise en doute par une source, pas par une affirmation "
             "plus forte. « C'est écrit à la page quatre » clôt la question en cinq mots.")

    d.dialogue('Dialogue · 3 de 3', "Le compromis", [
        ("NADIA", "Je ne dis pas qu'il faut refuser. En revanche, on prendrait un risque qu'on n'a pas mesuré.", True),
        ("MANON", "C'est ma faute, j'ai fait circuler la soumission trop vite. Alors qu'est-ce que tu proposerais ?", True),
        ("NADIA", "Je proposerais un partage. Les pièces courantes chez l'un, l'urgent et les pièces rares chez l'autre.", True),
        ("NADIA", "C'est moi qui écoperais de ce travail, alors je le dis en connaissance de cause.", True),
    ], notes="La dernière réplique est la plus habile de la réunion : nommer son propre "
             "intérêt désamorce le soupçon. Y revenir en C2.")

    d.tableau('Analyse', "Ce qui a fait bouger la décision",
              ['Le moment', 'Ce qui change'],
              [["Yves donne le chiffre du prix", "l'écart devient concret : 40 000 $"],
               ["Nadia cite la page quatre", "une donnée absente entre dans la discussion"],
               ["Yves chiffre le stock doublé", "l'économie tombe de moitié"],
               ["Nadia propose un partage", "la question passe de oui/non à comment"]],
              cle=0,
              note="Personne n'a élevé la voix, et la décision a changé de nature.",
              notes="Diapositive à photographier. C'est la démonstration de ce que le "
                    "Défi 2 enseigne.")

    d.regle("Résumer avant d'objecter",
            "Si je résume ce que vous venez de dire…",
            precision="Trois effets en une formule. Vous vérifiez que vous avez compris ; "
                      "vous montrez à l'autre qu'il a été entendu, ce qui le désarme ; et "
                      "vous prenez la parole sans couper personne. Le programme du "
                      "niveau 8 la nomme explicitement : résumer les propos de son "
                      "interlocuteur pour confirmer l'information.",
            notes="Diapositive à photographier. C'est la première des sept formules "
                  "d'intervention de C2.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la réunion.", [
        ("Ferrico augmente ses prix de neuf pour cent.", "vrai"),
        ("Lachance livre plus vite que Ferrico.", "faux — dix jours contre quatre"),
        ("Le délai est écrit à la page quatre de la soumission.", "vrai"),
        ("Le stock supplémentaire mangerait la moitié de l'économie.", "vrai"),
        ("Nadia recommande de refuser Lachance.", "faux — elle propose un partage"),
        ("Yves trouve que deux fournisseurs simplifieraient son travail.", "faux — deux comptes, deux facturations"),
        ("La décision est prise à cette réunion.", "faux — reportée au seize"),
    ], corrige=True,
       notes="La réunion est longue et à trois voix : deux écoutes, la seconde en "
             "notant les chiffres.")

    d.billet(
        "Notez trois chiffres entendus dans la réunion, et ce qu'ils mesurent.",
        exemples=[
            "Lequel a fait changer la discussion ?",
            "Lequel n'était pas dans le document de départ ?",
        ],
        notes="Devoir d'écoute. Il prépare directement le compte rendu de C4.")

    return d.save(dossier)
