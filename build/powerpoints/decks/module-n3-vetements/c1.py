# -*- coding: utf-8 -*-
"""C1 · Lequel est le moins cher ?
Bloc C « Défi 2 · Comparer deux prix » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-vetements/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Lequel est le moins cher ?',
        chapeau="Deux paires de bottes côte à côte : 99 $ sur l'une, deux "
                "prix sur l'autre. Le moins cher n'est pas celui qu'on croit, "
                "et tout est écrit sur l'étiquette.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 2. Demander au groupe qui regarde les prix "
                  "avant d'acheter et qui compare deux articles. Presque tout le monde "
                  "compare — le problème est de le dire en français.")

    d.objectifs([
        "comprendre une étiquette qui porte deux prix ;",
        "distinguer le prix régulier et le prix d'aujourd'hui ;",
        "comprendre ce qu'est une liquidation ;",
        "dire lequel de deux articles coûte le moins cher.",
    ])

    d.declencheur(
        'Observation', "Pourquoi deux prix sur la même étiquette ?",
        image=IMG + 'etiquette-prix-reduit.jpg',
        pistes=[
            "Lequel des deux paie-t-on ?",
            "À quoi sert l'autre ?",
            "Pourquoi le magasin l'écrit-il quand même ?",
            "Avez-vous déjà été surpris à la caisse ?",
        ],
        notes="Le premier prix, barré ou écrit petit, est le prix régulier : il sert à "
              "montrer l'économie. Le second est celui qu'on paie.")

    d.dialogue('Dialogue · 1 de 3', "Deux prix", [
        ("FARIDA", "Celles-ci sont à quatre-vingt-dix-neuf dollars. Et celles-là ?", True),
        ("SAMIR", "Celles-là sont à cent trente dollars, mais elles sont en liquidation.", True),
        ("FARIDA", "Il y a deux prix. Je ne comprends pas.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Je ne comprends pas » est dit franchement. C'est ce qui déclenche "
             "l'explication : sans cette phrase, Samir serait passé à autre chose.")

    d.dialogue('Dialogue · 2 de 3', "L'explication", [
        ("SAMIR", "Le premier prix, c'est le prix régulier : cent trente. Le deuxième, c'est le prix d'aujourd'hui : soixante-cinq.", True),
        ("FARIDA", "Soixante-cinq ? Alors elles sont moins chères que les autres !", True),
        ("SAMIR", "Beaucoup moins chères. C'est cinquante pour cent de rabais.", True),
    ], notes="Farida fait le calcul elle-même et le dit à voix haute. Faire remarquer la "
             "structure « moins chères que ».")

    d.dialogue('Dialogue · 3 de 3', "Et la qualité ?", [
        ("FARIDA", "Et elles sont aussi chaudes ?", True),
        ("SAMIR", "Elles sont même plus chaudes. Elles sont doublées en laine.", True),
        ("FARIDA", "Alors pourquoi elles sont en liquidation ?", True),
        ("SAMIR", "Il reste seulement deux pointures.", True),
    ], notes="La bonne question : un bas prix a toujours une raison. Ici, ce n'est pas la "
             "qualité, c'est le choix de pointures.")

    d.tableau('Analyse', "Ce que dit une étiquette à deux prix",
              ['Ce qui est écrit', 'Ce que ça veut dire'],
              [["Prix régulier 130,00 $", "le prix des autres semaines"],
               ["65,00 $", "le prix qu'on paie aujourd'hui"],
               ["Liquidation", "les derniers articles, il n'y en aura plus"],
               ["50 % de rabais", "on enlève la moitié du prix régulier"]],
              cle=0,
              note="Le prix payé est toujours le plus bas des deux, et il est écrit en gros.",
              notes="Diapo à photographier. Apporter une vraie étiquette si possible.")

    d.regle("Un bas prix a toujours une raison",
            "Demandez laquelle avant d'acheter.",
            precision="Une liquidation ne veut pas dire que l'article est mauvais. Le plus "
                      "souvent, il ne reste que deux ou trois tailles, ou le magasin change "
                      "de modèle pour la saison suivante. Mais la question vaut la peine "
                      "d'être posée : « Pourquoi c'est en liquidation ? »",
            notes="Diapo à photographier. Faire répéter la question à voix haute.")

    d.cartes("Trois mots de rabais", "Ce qui les distingue", [
        ("Un rabais",
         "Un prix réduit pendant quelques jours ou quelques semaines. Après, le prix "
         "remonte. L'article reste au magasin."),
        ("Une liquidation",
         "Les derniers articles d'un modèle, à très bas prix. Quand il n'y en a plus, il "
         "n'y en a plus — le magasin ne le rachètera pas."),
        ("Une vente finale",
         "Un article qu'on ne peut ni rapporter ni échanger. Souvent écrit en petit sous "
         "le prix, et c'est ce qui compte le plus."),
    ], notes="La troisième carte est celle qui surprend : essayer avant d'acheter devient "
             "obligatoire quand la vente est finale.")

    d.piege("Comparer les prix affichés seulement",
            "99 $, c'est moins cher que 130 $.",
            "130 $ en liquidation à 65 $ : c'est 65 $ qu'on paie.",
            "Le grand chiffre n'est pas toujours le prix payé. Sur une étiquette à deux "
            "prix, il faut lire les deux lignes avant de comparer — sinon on choisit "
            "exactement le mauvais article.",
            notes="C'est le cœur du défi 2. Le faire refaire au tableau avec deux autres "
                  "exemples chiffrés.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Les premières bottes coûtent 99 $.", "vrai"),
        ("Les autres bottes ont un seul prix.", "faux — deux prix"),
        ("Leur prix régulier est de 130 $.", "vrai"),
        ("Avec la liquidation, elles coûtent 65 $.", "vrai"),
        ("Les bottes en liquidation sont moins chaudes.", "faux — plus chaudes"),
        ("Il reste beaucoup de pointures.", "faux — seulement deux"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Relevez deux prix d'un même article dans une circulaire ou en magasin.",
        exemples=[
            "Le prix régulier et le prix d'aujourd'hui.",
            "Calculez la différence en dollars.",
        ],
        notes="Devoir de calcul autant que de langue. Il donne des chiffres réels pour la "
              "séance C2.")

    return d.save(dossier)
