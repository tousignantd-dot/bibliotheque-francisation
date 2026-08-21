# -*- coding: utf-8 -*-
"""B1 · Lire un prix, et le dire.
Bloc B « Défi 1 · Lire la circulaire » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1prix`, mini-leçon `t1prix`.

La séance qui porte l'intention du programme : repérer des indications de
prix. Tout se joue sur trois écritures — le prix simple, le prix d'une
mesure, le « 2 pour ». La troisième est celle qui trompe le plus.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-panier/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Lire un prix, et le dire",
        chapeau="Une virgule, deux nombres. Et une barre oblique qui change "
                "tout.",
        duree='75 minutes')

    d.titre(notes="Séance de chiffres. Prévoir d'écrire beaucoup au tableau et de faire "
                  "dire beaucoup à voix haute : un prix se retient par la bouche, pas "
                  "par les yeux.")

    d.objectifs([
        "lire un prix écrit avec une virgule ;",
        "dire un prix à voix haute, en deux formes ;",
        "comprendre « 3,99 $ / kg » ;",
        "comprendre un spécial « 2 pour 9 $ ».",
    ])

    d.declencheur(
        'Observation', "Combien coûtent ces pommes ?",
        image=IMG + 'balance-fruits.jpg',
        pistes=[
            "Que fait cette balance ?",
            "Si l'affichette dit « 3,99 $ / kg », combien coûte ce sac ?",
            "Faut-il payer 3,99 $ ?",
            "Qu'est-ce qu'il manque pour répondre ?",
        ],
        notes="Le groupe répondra souvent « 3,99 $ ». C'est exactement le piège de la "
              "séance : il manque le poids. Ne pas donner la réponse tout de suite.")

    d.dialogue('Dialogue · 1 de 2', "Deux pour neuf dollars", [
        ("AMINATA", "Rose, je lis « 2 pour 9 $ ». Je ne comprends pas.", True),
        ("ROSE", "Tu achètes deux paquets. Tu payes neuf dollars.", True),
        ("AMINATA", "Et un seul paquet ?", True),
        ("ROSE", "Un seul paquet, c'est six dollars. Deux, c'est moins cher.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Écrire au tableau : 1 paquet = 6 $, 2 paquets = 9 $. Faire calculer "
             "l'économie ensemble : trois dollars. C'est concret et ça reste.")

    d.dialogue('Dialogue · 2 de 2', "Trois dollars quatre-vingt-dix-neuf", [
        ("AMINATA", "D'accord. Et ici : « 3,99 $ le kilo » ?", True),
        ("ROSE", "Trois dollars quatre-vingt-dix-neuf pour un kilo de pommes.", True),
        ("AMINATA", "Trois dollars quatre-vingt-dix-neuf. C'est ça ?", True),
        ("ROSE", "C'est ça. Tu lis bien !", True),
    ], notes="Faire remarquer ce que fait Aminata à la troisième réplique : elle répète le "
             "prix. C'est le geste que le module apprend, et il revient partout.")

    d.tableau('Analyse', "Trois écritures, trois sens",
              ['Ce qui est écrit', 'Ce que ça veut dire'],
              [["3,99 $", "le prix du produit"],
               ["3,99 $ / kg", "le prix d'<b>un kilo</b> seulement"],
               ["2 pour 9 $", "deux produits ensemble pour 9 $"],
               ["1,29 $ ch.", "« ch. » = chacun, le prix d'un seul"]],
              cle=2,
              note="La barre oblique et l'unité disent que le prix vaut pour une mesure. "
                   "Un sac de deux kilos coûte donc deux fois ce prix.",
              notes="Diapositive à photographier. Revenir sur la question du déclencheur : "
                    "le sac de pommes coûte le poids fois 3,99 $.")

    d.regle("Dire un prix",
            "On ne dit jamais la virgule.",
            precision="On écrit <b>3,99 $</b>. On dit « <b>trois dollars quatre-vingt-"
                      "dix-neuf</b> », ou, plus court, « <b>trois quatre-vingt-dix-neuf</b> ». "
                      "À la caisse, c'est presque toujours la forme courte qu'on entend.",
            notes="Diapositive à photographier. Faire dire cinq prix au groupe, en chœur, "
                  "d'abord la forme longue puis la courte.")

    d.cartes("Cinq prix à dire", "Longue forme, forme courte", [
        ("3,99 $", "trois dollars quatre-vingt-dix-neuf · trois quatre-vingt-dix-neuf"),
        ("1,29 $", "un dollar vingt-neuf · un vingt-neuf"),
        ("12,50 $", "douze dollars cinquante · douze cinquante"),
        ("0,89 $", "quatre-vingt-neuf cents"),
        ("24,15 $", "vingt-quatre dollars quinze · vingt-quatre quinze"),
    ], cols=1, notes="Diapositive à photographier. Sous un dollar, on dit « cents » ; "
                     "au-dessus, le mot disparaît presque toujours.")

    d.pratique('Compréhension', "D'après le dialogue",
               "Complétez avec un nombre ou un mot.", [
        ("« 2 pour 9 $ » : je prends ___ paquets.", "deux"),
        ("« 2 pour 9 $ » : je paye ___ dollars.", "neuf"),
        ("Un seul paquet coûte ___ dollars.", "six"),
        ("« 3,99 $ / kg » est le prix d'un ___ .", "kilo"),
    ], corrige=True, cols=1,
       notes="Faire d'abord à l'oral. Les nombres écrits en lettres viendront plus tard "
             "dans le niveau : ici, le chiffre suffit.")

    d.pratique('Pratique · à deux', "La circulaire à voix haute",
               "Deux par deux, avec la circulaire de la semaine.", [
        ("Étape 1", "Chacun choisit cinq produits dans la circulaire."),
        ("Étape 2", "Dites le prix de chacun à voix haute, forme longue."),
        ("Étape 3", "Redites-les en forme courte."),
        ("Étape 4", "Trouvez ensemble un prix écrit « / kg » ou « 2 pour »."),
    ], cols=1,
       notes="Vingt-cinq minutes. C'est la pratique centrale du module : ne pas l'écourter "
             "pour finir la diapositive suivante.")

    d.billet(
        "Écrivez trois prix de la circulaire, en chiffres et en mots.",
        exemples=[
            "3,99 $ — trois dollars quatre-vingt-dix-neuf",
            "1,29 $ — un dollar vingt-neuf",
            "2 pour 9 $ — deux paquets pour neuf dollars",
        ],
        notes="Devoir court. Leur demander de dire les trois prix à voix haute avant "
              "d'aller dormir : c'est ce qui les fixe.")

    return d.save(dossier)
