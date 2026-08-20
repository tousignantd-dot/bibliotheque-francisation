# -*- coding: utf-8 -*-
"""D2 · Au terminal.
Bloc D · couleur ambre (écriture) · 60 min.
Source : mini-leçon `t3addition`, dialogue `t3b`, exercices `t3b` et `t3calcul`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-restaurant/images/')


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Au terminal',
        chapeau="Le terminal demande le pourboire avant le code, et propose "
                "des pourcentages calculés après taxes. « Autre montant » "
                "permet de décider soi-même.",
        duree='60 minutes')

    d.titre(notes="Séance très concrète. Si vous avez un vieux terminal ou une capture "
                  "d'écran, projetez-la : l'ordre des écrans est ce qui déroute le plus.")

    d.objectifs([
        "connaître l'ordre des écrans du terminal ;",
        "calculer quinze pour cent de tête ;",
        "employer « autre montant » ;",
        "répondre aux questions du paiement.",
    ])

    d.declencheur(
        'Observation', "Que demande cet appareil, et dans quel ordre ?",
        image=IMG + 'terminal-pourboire.jpg',
        pistes=[
            "Qu'est-ce qui apparaît en premier ?",
            "Que veulent dire les pourcentages proposés ?",
            "Peut-on entrer un autre montant ?",
            "Qu'est-ce qui vous a déjà surpris avec ces appareils ?",
        ],
        notes="Beaucoup d'élèves ont déjà été surpris de voir le pourboire demandé avant le "
              "code. C'est l'ordre standard ici, et il n'est pas intuitif.")

    d.tableau('Analyse', "L'ordre des écrans",
              ['Écran', 'Ce qu\'il demande'],
              [["1", "débit ou crédit"],
               ["2", "le pourboire — pourcentage ou autre montant"],
               ["3", "le code, ou la puce sans contact"],
               ["4", "le reçu : papier, courriel, ou aucun"]],
              cle=1,
              note="Le pourboire vient AVANT le code. C'est ce qui surprend.",
              notes="Diapo à photographier. Faire recopier : connaître l'ordre évite la "
                    "panique devant l'appareil.")

    d.regle("Calculer quinze pour cent de tête",
            "Le dixième du montant, plus la moitié de ce dixième.",
            precision="50 $ › 5 + 2,50 = 7,50 $. 40 $ › 4 + 2 = 6 $. 80 $ › 8 + 4 = 12 $. "
                      "La méthode marche pour n'importe quel montant, en deux secondes, "
                      "sans calculatrice.",
            notes="Diapo à photographier. Faire pratiquer sur cinq montants au tableau : "
                  "après cinq fois, c'est automatique.")

    d.regle("« Autre montant »",
            "En bas de l'écran, pour entrer son propre chiffre.",
            precision="Les pourcentages proposés sont souvent calculés <b>après</b> taxes, "
                      "ce qui donne un montant plus élevé que 15 % du montant avant taxes. "
                      "« Autre montant » permet d'entrer exactement ce qu'on veut — et "
                      "personne ne le voit.",
            notes="Point pratique important. L'option existe sur tous les terminaux, mais "
                  "elle est écrite petit, en bas.")

    d.piege("Se sentir obligé par les pourcentages proposés",
            "Il propose 18, 20 et 25 %. Je prends 18 %.",
            "« Autre montant » : j'entre 15 % du montant avant taxes.",
            "Les pourcentages proposés sont un choix du commerçant, pas une règle. Ils "
            "partent souvent de 18 % et sont calculés après taxes. Vous n'êtes tenu à "
            "aucun d'eux — et le serveur ne voit pas ce que vous choisissez.",
            notes="Le dire clairement : beaucoup de gens se sentent observés et paient plus "
                  "qu'ils ne voulaient.")

    d.pratique('Pratique · 1 de 2', "Calculez le pourboire",
               "Quinze pour cent, de tête.", [
        ("20 $", "3 $ — 2 + 1"),
        ("40 $", "6 $ — 4 + 2"),
        ("50 $", "7,50 $ — 5 + 2,50"),
        ("60 $", "9 $ — 6 + 3"),
        ("80 $", "12 $ — 8 + 4"),
        ("100 $", "15 $ — 10 + 5"),
    ], corrige=True,
       notes="Faire faire le calcul à voix haute avant d'afficher. La méthode se voit mieux "
             "qu'elle ne s'explique.")

    d.pratique('Pratique · 2 de 2', "Que répondez-vous ?",
               "Le serveur ou le terminal pose la question.", [
        ("« Ensemble ou séparé ? »", "Séparément, s'il vous plaît. / Ensemble."),
        ("« Vous payez comment ? »", "Débit, s'il vous plaît."),
        ("« Vous voulez la facture ? »", "Oui, s'il vous plaît. / Non merci."),
        ("Le terminal propose 18, 20, 25 %", "« Autre montant », puis mon chiffre."),
        ("« Autre chose avec ça ? »", "Non merci, ça va."),
    ], corrige=True, cols=1,
       notes="Faire jouer les échanges à deux. Ce sont des phrases très courtes, faciles à "
             "installer.")

    d.cartes("Trois précautions", "Avant de payer", [
        ("Décider ensemble ou séparé avant de demander",
         "Une fois l'addition imprimée, la séparer prend plusieurs minutes — et parfois "
         "c'est refusé."),
        ("Vérifier le total",
         "Une ligne de trop arrive. Un coup d'œil de dix secondes suffit, et personne ne "
         "s'en offusque."),
        ("Garder la facture si c'est pour le travail",
         "« Vous voulez la facture ? » : dites oui. Sans elle, aucun remboursement n'est "
         "possible."),
    ], notes="La troisième carte est utile aux élèves qui travaillent : les repas d'affaires "
             "ou de déplacement se remboursent sur facture.")

    d.billet(
        "Écrivez l'échange complet de la fin d'un repas.",
        exemples=[
            "Vous demandez l'addition, le serveur répond, vous payez.",
            "Six répliques, et le calcul du pourboire à la fin.",
        ],
        notes="Bilan du bloc D. Cet échange est le cas « addition » du jeu de rôle de E1.")

    return d.save(dossier)
