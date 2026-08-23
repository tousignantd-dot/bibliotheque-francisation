# -*- coding: utf-8 -*-
"""B2 · Lire la fiche à l'envers
Bloc B « Défi 1 · Emprunter moins cher » · couleur ambre · 90 min.
Source : exercice `t1doc` (type texte) et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Lire la fiche à l'envers",
        chapeau="Ce qui est en gros attire, ce qui est en petit coûte. Un "
                "document de produit financier se lit en commençant par les "
                "notes.",
        duree='90 minutes')

    d.titre(notes="Séance de lecture. Distribuer la fiche des trois façons d'emprunter "
                  "avant de projeter quoi que ce soit : le groupe lit d'abord, on "
                  "commente ensuite.")

    d.objectifs([
        "poser trois questions à n'importe quel produit de crédit ;",
        "distinguer un achat d'une avance de fonds ;",
        "dire ce que la loi impose comme paiement minimum ;",
        "repérer la phrase qui limite dans un document.",
    ], notes="Le deuxième objectif est celui que personne ne connaît, et il coûte de "
             "l'argent tous les mois à ceux qui l'ignorent.")

    d.declencheur(
        'Observation', "Dans un dépliant de banque, qu'est-ce qui est écrit en gros ?",
        pistes=[
            "Le taux, ou les conditions ?",
            "Où sont les astérisques et les parenthèses ?",
            "Qu'est-ce que « sous réserve d'approbation » veut dire ?",
            "Par quoi commencerais-tu, maintenant ?",
        ],
        notes="Apporter un vrai dépliant si possible, de n'importe quelle institution. "
              "Le groupe trouve les petits caractères en trente secondes.")

    d.regle("Trois questions, et elles suffisent",
            "Quel est le taux, et est-il fixe ou variable ? Quand les frais "
            "commencent-ils ? Que se passe-t-il si je rembourse plus vite ?",
            precision="Aucun document sérieux ne refuse d'y répondre, et les trois "
                      "réponses tiennent en trois lignes. Un conseiller qui esquive "
                      "l'une des trois vous dit quelque chose sur le produit.",
            notes="Diapositive à photographier. Faire copier les trois questions dans "
                  "le cahier : elles servent au jeu de rôle de E1.")

    d.tableau('Analyse', "Ce que dit la fiche",
              ['La ligne', 'Ce que ça change pour vous'],
              [['19,90 % sur les achats', 'environ 1 800 $ par année sur 9 000 $'],
               ['appliqué chaque jour', 'payer trois jours plus tôt coûte moins'],
               ['taux variable', 'il peut monter pendant que vous payez'],
               ['fixe pour la durée', 'votre versement ne bougera pas'],
               ['aucune pénalité', 'vous pouvez finir plus vite gratuitement']],
              cle=0,
              notes="Diapositive à photographier. Ces cinq lignes sont celles que "
                    "l'exercice du module fait cliquer dans le document.")

    d.piege('Le piège', "une avance de fonds est un retrait comme un autre",
            "une avance de fonds est un emprunt qui commence le jour même",
            "Sur un achat, aucuns frais ne courent tant que le solde est payé en entier "
            "avant l'échéance. Sur une avance de fonds, les frais commencent le jour "
            "où elle est prise, même remboursée la semaine suivante. Retirer cent "
            "dollars au guichet avec une carte de crédit coûte donc de l'argent.",
            notes="C'est la ligne la moins connue de toute la carte de crédit. "
                  "Demander au groupe qui le savait : en général, personne.")

    d.regle("Le paiement minimum a un plancher légal",
            "Au Québec, il ne peut pas être inférieur à cinq pour cent du solde à la "
            "fin de la période.",
            precision="Ce plancher protège le consommateur : il empêche une dette de "
                      "rester ouverte indéfiniment. Il ne sort personne de sa dette "
                      "pour autant. Cinq pour cent, c'est un plancher, pas un plan.",
            notes="Fait vérifié auprès de l'Office de la protection du consommateur. "
                  "Le dire au groupe : ce chiffre n'est pas une invention du module.")

    d.pratique('Lecture', "Cherchez la réponse dans la fiche",
               "Une question, un passage. Soulignez-le au crayon.", [
        ("Quel est le taux annuel de la carte ?", "19,90 % sur les achats"),
        ("Quelle part du solde le minimum représente-t-il ?", "5 %, plancher fixé par la loi"),
        ("Quand n'y a-t-il aucuns frais sur un achat ?", "solde payé en entier avant l'échéance"),
        ("Qu'est-ce qui change avec une avance de fonds ?", "les frais courent dès le jour même"),
        ("Sur quelle partie la marge applique-t-elle son taux ?", "sur la partie utilisée seulement"),
        ("Que se passe-t-il si on rembourse le prêt plus vite ?", "aucune pénalité"),
    ], corrige=True,
       notes="Faire souligner sur le papier avant de corriger. La séance porte sur "
             "l'endroit où se trouve la réponse autant que sur la réponse.")

    d.regle("La phrase qui limite n'est pas une négation",
            "« On ne paie de l'intérêt que sur la partie utilisée » veut dire : on "
            "paie, mais seulement là-dessus.",
            precision="« Ne... que » est la tournure la plus fréquente des documents "
                      "financiers et l'une des plus mal comprises. Elle limite, elle ne "
                      "nie pas. Le remplacer mentalement par « seulement » rend la "
                      "phrase claire du premier coup.",
            notes="Diapositive à photographier. La tournure revient en B4, dans "
                  "l'exercice de comparaison. La poser ici, l'exercer là.")

    d.billet("Recopie la phrase de la fiche qui t'aurait échappé, et écris ce qu'elle "
             "veut dire.",
             exemples=["« les frais courent à compter du jour où elle est prise » : une "
                       "avance de fonds coûte tout de suite."],
             notes="Trois minutes. Les billets disent quelle ligne du document résiste, "
                   "et c'est presque toujours la même.")

    return d.save(dossier)
