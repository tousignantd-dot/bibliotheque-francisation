# -*- coding: utf-8 -*-
"""C2 · L'étiquette et l'affichette.
Bloc C « Défi 2 · L'étiquette et l'affichette » · couleur ambre · 60 min.
Source : dialogue `t2b`, exercices `t2mesure`, `t2etiq`, `t2b`.

La séance de lecture du module, et celle qui répond exactement à l'intention
du programme : repérer des indications de mesure et de prix. Les deux petits
papiers du magasin se lisent par repérage, pas par lecture suivie.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-panier/images/')


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="L'étiquette et l'affichette",
        chapeau="Deux petits papiers décident de tout : l'un donne le prix, "
                "l'autre donne le poids.",
        duree='60 minutes')

    d.titre(notes="Prévenir le groupe : on ne va pas comprendre tous les mots, et ce n'est "
                  "pas le but. Une étiquette se regarde ; elle ne se lit pas.")

    d.objectifs([
        "distinguer l'étiquette de l'affichette ;",
        "lire un poids et un volume ;",
        "dire « un kilo de riz », « un litre de lait » ;",
        "comprendre une date « meilleur avant ».",
    ])

    d.declencheur(
        'Observation', "Où est écrit le prix ?",
        image=IMG + 'produits-entretien.jpg',
        pistes=[
            "Le prix est-il sur la bouteille ou sur la tablette ?",
            "Qu'est-ce qui est écrit sur la bouteille, alors ?",
            "Comment savoir si c'est le grand ou le petit format ?",
            "Qu'est-ce qui change entre les deux ?",
        ],
        notes="La réponse est le cœur de la séance : le prix est sur la tablette "
              "(l'affichette), le format est sur le produit (l'étiquette). Les deux "
              "ensemble donnent l'information complète.")

    d.dialogue('Dialogue', "Un kilo ou un sac ?", [
        ("AMINATA", "Excusez-moi. Les oranges sont à quel prix ?", True),
        ("DENIS", "Il y a deux affichettes. Le sac ou le kilo.", True),
        ("AMINATA", "Le sac, c'est combien ?", True),
        ("DENIS", "Trois dollars quatre-vingt-dix-neuf. Deux kilos dans le sac.", True),
        ("AMINATA", "Et sur l'étiquette, ici ? « 908 g ».", True),
        ("DENIS", "Ça, c'est le poids. Neuf cent huit grammes, presque un kilo.", True),
    ], consigne="Écoutez, puis dites où est le prix et où est le poids.",
       notes="Faire compter les deux papiers : deux affichettes sur la tablette, une "
             "étiquette sur le produit. La confusion entre les deux est la difficulté "
             "réelle de la séance.")

    d.tableau('Analyse', "Que dit ce petit papier ?",
              ['Ce qui est écrit', 'Ce que ça veut dire'],
              [["908 g", "le poids : presque un kilo"],
               ["1 L", "un litre : du lait, du jus, de l'eau"],
               ["3,99 $ / kg", "le prix d'un seul kilo"],
               ["Meilleur avant : 12 mai", "la date : à manger avant ce jour"]],
              cle=2,
              note="La petite lettre après le nombre dit tout : g et kg pour le poids, "
                   "ml et L pour le liquide, $ pour le prix.",
              notes="Diapositive à photographier. Apporter quelques emballages vides et "
                    "les faire circuler : c'est plus efficace que n'importe quelle image.")

    d.regle("La mesure, puis « de », puis le produit",
            "Toujours les mêmes trois choses, dans le même ordre.",
            precision="un kilo <b>de</b> riz · un litre <b>de</b> lait · une douzaine "
                      "<b>d'</b>œufs · un sac <b>d'</b>oranges. Après « de », le produit "
                      "vient seul : on ne dit jamais « un litre de <b>le</b> lait ».",
            notes="Diapositive à photographier. Faire construire cinq quantités à l'oral, "
                  "en chaîne, à partir des produits de leur liste de B2.")

    d.cartes("Les trois familles de mesure", "Ce qui se pèse, se verse, se compte", [
        ("Ce qui se pèse", "le gramme (g), le kilo (kg) — mille grammes font un kilo"),
        ("Ce qui se verse", "le millilitre (ml), le litre (L)"),
        ("Ce qui se compte", "la douzaine, le paquet, le sac, la boîte"),
    ], cols=3, notes="Diapositive à photographier. Faire classer par le groupe cinq "
                     "produits de leur propre liste dans les trois familles.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Il y a deux affichettes pour les oranges.", "vrai"),
        ("Le sac d'oranges coûte 3,99 $.", "vrai"),
        ("« 908 g » est un prix.", "faux — c'est un poids"),
        ("908 grammes, c'est presque un kilo.", "vrai"),
    ], corrige=True, cols=1,
       notes="Quatre énoncés. La troisième ligne est celle qui sépare ceux qui ont compris "
             "la séance de ceux qui doivent la refaire en ligne.")

    d.pratique('Pratique · à deux', "Le poids et le prix",
               "Deux par deux, avec des emballages vides ou des photos.", [
        ("Étape 1", "Trouvez le poids ou le volume sur l'emballage."),
        ("Étape 2", "Dites-le à voix haute : « C'est un litre. »"),
        ("Étape 3", "Dites la quantité : « un litre de lait »."),
        ("Étape 4", "Cherchez une date « meilleur avant »."),
    ], cols=1,
       notes="Vingt minutes. Si aucun emballage n'est disponible, la circulaire du bloc A "
             "porte souvent les formats à côté des prix.")

    d.billet(
        "Écrivez cinq quantités, avec la mesure et « de ».",
        exemples=[
            "un litre de lait",
            "une douzaine d'œufs",
            "cent grammes de fromage",
        ],
        notes="Devoir court. Leur demander de vérifier le poids réel sur ce qu'ils ont "
              "dans leur cuisine : c'est là que la mesure devient concrète.")

    return d.save(dossier)
