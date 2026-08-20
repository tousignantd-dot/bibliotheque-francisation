# -*- coding: utf-8 -*-
"""D2 · Un mode d'emploi en trois blocs.
Bloc D · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t3mode`, dialogue `t3b`, exercices `t3mode`, `t3bloc` et `t3b`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="Un mode d'emploi en trois blocs",
        chapeau="La dose en haut, les étapes au milieu, les avertissements en "
                "bas. Toujours dans cet ordre. Une fois qu'on le sait, on "
                "trouve ce qu'on cherche en cinq secondes.",
        duree='75 minutes')

    d.titre(notes="Apporter deux bouteilles de produit d'entretien vides. La séance se fait "
                  "sur du vrai, et le danger dont on parle est réel.")

    d.objectifs([
        "trouver la dose, les étapes et les avertissements sur une étiquette ;",
        "convertir millilitres et cuillères à soupe ;",
        "comprendre pourquoi il ne faut pas mélanger deux produits ;",
        "suivre un mode d'emploi du début à la fin.",
    ])

    d.dialogue('Dialogue', "Trente millilitres, c'est combien ?", [
        ("CLAUDE", "« Diluer trente millilitres dans quatre litres d'eau tiède. » Trente millilitres, c'est combien ?", True),
        ("FARIDA", "Deux cuillères à soupe, à peu près. Il y a un bouchon doseur sur la bouteille.", True),
        ("CLAUDE", "Et après ? Il faut rincer ?", False),
        ("FARIDA", "C'est écrit juste en dessous : « Rincer à l'eau claire. Ne pas mélanger avec un produit chloré. »", True),
    ], consigne="Écoutez, puis cherchez les trois blocs sur les bouteilles distribuées.",
       notes="Faire chercher immédiatement. Les trois blocs sont visibles d'un coup d'œil "
             "une fois qu'on sait qu'ils existent.")

    d.tableau('Analyse', "Les trois blocs",
              ['Bloc', 'Ce qu\'on y trouve'],
              [["1 · En haut", "la dose : combien de produit, dans combien d'eau"],
               ["2 · Au milieu", "les étapes, dans l'ordre"],
               ["3 · En bas", "les avertissements, souvent en gras"]],
              cle=2,
              note="Le troisième bloc est séparé du reste justement pour être trouvé vite.",
              notes="Diapo centrale. Faire recopier, puis vérifier sur les bouteilles "
                    "apportées.")

    d.tableau('Les mesures', "Quatre repères suffisent",
              ['Mesure', 'Équivalent'],
              [["30 ml", "≈ 2 cuillères à soupe"],
               ["15 ml", "≈ 1 cuillère à soupe"],
               ["250 ml", "≈ 1 tasse"],
               ["1 litre", "1000 ml"]],
              cle=0,
              note="Sans bouchon doseur, une cuillère à soupe de cuisine fait l'affaire.",
              notes="Ces repères ont déjà servi en C3. La répétition entre les blocs est "
                    "voulue.")

    d.regle('La dose est calculée',
            "En mettre plus ne nettoie pas mieux.",
            precision="Deux fois la dose laisse un film collant sur la surface, qui attire "
                      "la poussière et oblige à nettoyer plus souvent. C'est exactement ce "
                      "que faisait Farida avant de lire l'étiquette.",
            notes="Beaucoup d'élèves reconnaîtront l'habitude. Le dire sans reproche : "
                  "c'est un réflexe très répandu.")

    d.regle('Ne jamais mélanger deux produits',
            "Un nettoyant et de l'eau de Javel dégagent un gaz toxique.",
            precision="C'est l'accident domestique le plus fréquent avec les produits "
                      "d'entretien. L'avertissement figure sur presque toutes les "
                      "bouteilles, en bas, avec un triangle. Ce n'est pas une formalité "
                      "juridique.",
            notes="Diapo à photographier. C'est le point le plus important de toute la "
                  "séance, et il sauve des gens chaque année.")

    d.piege("Sauter les avertissements",
            "C'est en bas et en petit, ce n'est sûrement pas important.",
            "C'est en bas et séparé pour être trouvé vite.",
            "Les avertissements sont détachés du reste du texte précisément pour qu'on "
            "puisse les repérer d'un coup d'œil. Sur un produit qu'on ne connaît pas, "
            "c'est le premier bloc à lire, pas le dernier.",
            notes="Renverser l'ordre de lecture est un conseil pratique fort : sur un "
                  "produit inconnu, on commence par le bas.")

    d.pratique('Pratique · 1 de 2', "Dans quel bloc ?",
               "Dites où se trouve chaque phrase.", [
        ("« Diluer 30 ml dans 4 litres d'eau tiède. »", "la dose — en haut"),
        ("« Laisser agir deux minutes. »", "les étapes — au milieu"),
        ("« Rincer à l'eau claire. »", "les étapes — au milieu"),
        ("« Ne pas mélanger avec un produit chloré. »", "les avertissements — en bas"),
        ("« Tenir hors de la portée des enfants. »", "les avertissements — en bas"),
        ("« Utiliser le bouchon doseur fourni. »", "la dose — en haut"),
    ], corrige=True,
       notes="Faire vérifier sur les bouteilles réelles : les six phrases s'y retrouvent "
             "presque mot pour mot.")

    d.pratique('Pratique · 2 de 2', "Combien de produit ?",
               "Calculez la quantité.", [
        ("30 ml, sans bouchon doseur", "deux cuillères à soupe"),
        ("15 ml", "une cuillère à soupe"),
        ("60 ml", "quatre cuillères à soupe, ou un quart de tasse"),
        ("Un demi-litre d'eau", "500 ml, soit deux tasses"),
    ], corrige=True, cols=1,
       notes="Faire mesurer pour de vrai avec une cuillère si vous en avez une : "
             "l'équivalence devient concrète.")

    d.cartes("Un mode d'emploi complet", "Les six lignes types", [
        ("La dose",
         "« Diluer 30 ml dans 4 litres d'eau tiède. » · « Utiliser le bouchon doseur "
         "fourni. »"),
        ("Les étapes",
         "« Appliquer sur la surface. » · « Laisser agir deux minutes. » · « Rincer à "
         "l'eau claire. »"),
        ("Les avertissements",
         "« Ne pas mélanger avec un produit chloré. » · « Tenir hors de la portée des "
         "enfants. »"),
    ], notes="Faire lire les six lignes à voix haute, dans l'ordre. C'est le mode d'emploi "
             "type de n'importe quel nettoyant.")

    d.billet(
        "Prenez un produit d'entretien de chez vous et relevez ses trois blocs.",
        exemples=[
            "La dose exacte, les étapes, les avertissements.",
            "Notez si vous employiez la bonne dose jusqu'à maintenant.",
        ],
        notes="Devoir très concret. Beaucoup découvrent qu'ils employaient deux à quatre "
              "fois la dose recommandée.")

    return d.save(dossier)
