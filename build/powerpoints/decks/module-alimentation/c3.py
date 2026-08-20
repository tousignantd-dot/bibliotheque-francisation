# -*- coding: utf-8 -*-
"""C3 · Livres, kilos et grammes.
Bloc C · couleur ambre (écriture) · 60 min.
Source : mini-leçon `t2unite`, exercice `t2unite`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Livres, kilos et grammes',
        chapeau="Les étiquettes sont en grammes, la conversation en livres. "
                "Les deux cohabitent au même comptoir, et il faut savoir "
                "passer de l'un à l'autre.",
        duree='60 minutes')

    d.titre(notes="Séance de savoir pratique. Apporter une balance de cuisine si possible, "
                  "et quelques objets à peser : la conversion devient concrète en deux "
                  "minutes.")

    d.objectifs([
        "convertir approximativement livres et grammes ;",
        "commander dans l'unité que je maîtrise ;",
        "employer les mesures de liquide : litres, millilitres, tasses ;",
        "vérifier le poids et le prix affichés sur la balance.",
    ])

    d.tableau('Analyse', "Les repères à mémoriser",
              ['Quantité', 'Équivalent'],
              [["1 livre", "≈ 454 g — un peu moins qu'un demi-kilo"],
               ["1 kilo", "≈ 2,2 livres"],
               ["250 g", "≈ une demi-livre"],
               ["100 g", "une petite tranche de jambon"]],
              cle=0,
              note="Quatre repères suffisent pour tout le quotidien.",
              notes="Diapo à photographier. Faire recopier et garder dans le portefeuille "
                    "la première semaine.")

    d.regle('Deux systèmes, aucun conflit',
            "Commandez dans l'unité que vous connaissez.",
            precision="« Une livre » et « cinq cents grammes » sont tous les deux compris "
                      "et acceptés partout. La balance affiche les deux, et la personne au "
                      "comptoir fait la conversion sans y penser. Personne ne vous "
                      "corrigera.",
            notes="Le dire clairement : plusieurs élèves n'osent pas commander parce qu'ils "
                  "croient devoir employer la livre.")

    d.tableau('Les liquides', "Toujours en litres et millilitres",
              ['Mesure', 'Équivalent'],
              [["1 litre", "1000 ml"],
               ["1 tasse", "≈ 250 ml"],
               ["1 cuillère à soupe", "≈ 15 ml"],
               ["30 ml", "≈ 2 cuillères à soupe"]],
              cle=3,
              note="La dernière ligne est celle du mode d'emploi du nettoyant, au bloc D.",
              notes="Les recettes d'ici mélangent tasses et millilitres : ces quatre "
                    "repères permettent de passer de l'une à l'autre.")

    d.piege('Confondre livre et kilo',
            "Une livre de bœuf haché ? Je commande un kilo, c'est pareil.",
            "Une livre ≈ 454 g. Un kilo, c'est plus du double.",
            "Commander un kilo en pensant une livre double la quantité — et le prix. "
            "C'est l'erreur de conversion la plus coûteuse, et elle se fait en une "
            "seconde d'inattention.",
            notes="Faire le calcul au tableau avec un prix réel : l'écart parle de lui-même.")

    d.pratique('Pratique · 1 de 2', "Convertissez",
               "Donnez l'équivalent approximatif.", [
        ("Une livre, c'est environ…", "454 grammes"),
        ("Un kilo, c'est environ…", "2,2 livres"),
        ("Une livre et demie, c'est environ…", "680 grammes"),
        ("500 grammes, c'est environ…", "un peu plus d'une livre"),
        ("30 millilitres, c'est environ…", "deux cuillères à soupe"),
    ], corrige=True, cols=1,
       notes="Approximatif suffit : personne n'a besoin de la troisième décimale au "
             "comptoir.")

    d.pratique('Pratique · 2 de 2', "Commandez",
               "Écrivez la commande complète.", [
        ("Du poulet, quatre poitrines", "Je voudrais du poulet, s'il vous plaît. Quatre poitrines."),
        ("Du bœuf haché, une livre", "Je voudrais une livre de bœuf haché, s'il vous plaît."),
        ("Du jambon, 200 g, tranché mince", "Deux cents grammes de jambon, tranché mince, s'il vous plaît."),
        ("De la truite, deux filets", "Je voudrais de la truite, s'il vous plaît. Deux filets."),
    ], corrige=True, cols=1,
       notes="Vérifier le « de » après la quantité — c'est le rappel du bloc B, appliqué "
             "ici.")

    d.cartes('À la balance', "Trois choses à savoir", [
        ("Le poids exact est rarement celui demandé",
         "La personne coupe un peu plus ou un peu moins. C'est normal et attendu."),
        ("« Un peu plus, ça va ? »",
         "La question qu'on vous posera presque toujours. Répondre « oui, parfait » ou "
         "« un peu moins, s'il vous plaît » suffit."),
        ("L'affichage donne les deux",
         "Poids et prix. Vous pouvez le lire pendant qu'on emballe — et demander le total "
         "si vous ne l'avez pas vu."),
    ], notes="La deuxième carte est celle qui rassure le plus : cette question n'est pas un "
             "piège, c'est une politesse.")

    d.billet(
        "Écrivez les quantités que vous achetez habituellement, dans les deux unités.",
        exemples=[
            "Cinq produits : en livres et en grammes.",
            "Ajoutez deux mesures de liquide.",
        ],
        notes="Corriger les conversions approximatives sans sévérité : l'ordre de grandeur "
              "est ce qui compte.")

    return d.save(dossier)
