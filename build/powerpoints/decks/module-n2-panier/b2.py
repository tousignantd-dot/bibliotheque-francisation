# -*- coding: utf-8 -*-
"""B2 · Ma liste : un, une, des.
Bloc B « Défi 1 · Lire la circulaire » · couleur ambre · 75 min.
Source : dialogue `t1b`, exercice `t1des`, mini-leçon `t1des`.

La séance de grammaire du bloc B, et la seule production écrite avant le
bloc E. Les déterminants quantifiants indéfinis et le déterminant négatif
« de » sont au programme du niveau ; une liste d'épicerie est l'endroit le
plus naturel pour les employer.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-panier/images/')


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Ma liste : un, une, des",
        chapeau="Trois petits mots devant le produit — et un quatrième, "
                "quand on n'a plus rien.",
        duree='75 minutes')

    d.titre(notes="Séance d'écriture. Faire sortir une feuille dès le début : la liste "
                  "s'écrit pendant toute la séance, et pas seulement à la fin.")

    d.objectifs([
        "employer « un », « une », « des » ;",
        "employer « pas de » et « pas d' » ;",
        "écrire une courte liste d'épicerie ;",
        "dire ce qu'on n'a plus à la maison.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'il y a dans ce panier ?",
        image=IMG + 'panier-plein.jpg',
        pistes=[
            "Nommez trois choses que vous voyez.",
            "Combien y en a-t-il de chaque ?",
            "Qu'est-ce que vous mettez, vous, dans votre panier ?",
            "Qu'est-ce que vous n'achetez jamais ?",
        ],
        notes="Écrire au tableau ce que le groupe nomme, en gardant le petit mot devant : "
              "« un pain », « des pommes ». C'est le sujet de la séance et il apparaît "
              "tout seul.")

    d.dialogue('Dialogue', "Ma liste", [
        ("AMINATA", "J'écris ma liste. Un litre de lait, une douzaine d'œufs…", True),
        ("ROSE", "Et du riz ? Tu as encore du riz ?", True),
        ("AMINATA", "Non, je n'ai pas de riz. J'écris « un kilo de riz ».", True),
        ("ROSE", "Prends aussi des oranges. Elles sont en spécial.", True),
        ("AMINATA", "Des oranges, oui. Un sac de deux kilos.", True),
        ("ROSE", "Parfait. Ta liste est courte et claire.", True),
    ], consigne="Écoutez, puis comptez les petits mots : un, une, des, de.",
       notes="Faire relever les quatre formes au tableau, dans l'ordre où elles arrivent. "
             "Le « pas de » de la troisième réplique est celui qui surprend.")

    d.tableau('Analyse', "Les petits mots de la liste",
              ['Le petit mot', 'Quand ?'],
              [["<b>un</b>", "un seul, masculin : un litre, un kilo, un sac"],
               ["<b>une</b>", "une seule, féminin : une douzaine, une boîte"],
               ["<b>des</b>", "plusieurs : des pommes, des œufs"],
               ["<b>de</b> / <b>d'</b>", "après « pas » : pas de riz, pas d'œufs"]],
              cle=2,
              note="En français, un nom ne reste presque jamais seul. Il y a toujours un "
                   "petit mot devant.",
              notes="Diapositive à photographier. C'est le tableau que les élèves "
                    "consulteront tout le reste du niveau.")

    d.regle("À la forme négative, tout devient « de »",
            "Un, une, des, du, de la disparaissent après « pas ».",
            precision="« J'ai <b>du</b> riz » devient « je n'ai <b>pas de</b> riz ». "
                      "« J'ai <b>des</b> œufs » devient « je n'ai <b>pas d'</b>œufs ». Devant "
                      "une voyelle, « de » perd son e et devient <b>d'</b>.",
            notes="Diapositive à photographier. Faire transformer cinq phrases à l'oral, "
                  "en chaîne, chaque élève à son tour.")

    d.piege('Le piège', "je n'ai pas du riz", "je n'ai pas de riz",
            "C'est la faute la plus fréquente du niveau, et elle vient de ce que la phrase "
            "affirmative dit bien « j'ai <b>du</b> riz ». Après « pas », il ne reste que "
            "<b>de</b> : ni du, ni de la, ni des.",
            notes="Écrire la paire au tableau et la laisser toute la séance. Y revenir "
                  "chaque fois qu'elle réapparaît dans les productions.")

    d.pratique('Grammaire', "Complétez la liste d'Aminata",
               "Écrivez un, une, des, de ou d'.", [
        ("Je prends ___ litre de lait.", "un"),
        ("Je prends ___ douzaine d'œufs.", "une"),
        ("Je prends ___ oranges.", "des"),
        ("Je n'ai pas ___ riz.", "de"),
        ("Il n'y a pas ___ œufs dans le frigo.", "d'"),
    ], corrige=True, cols=1,
       notes="Faire d'abord à l'oral, en groupe. Les deux dernières lignes sont les "
             "seules qui posent problème.")

    d.pratique('Pratique · à deux', "Ce que j'ai, ce que je n'ai plus",
               "Deux par deux, chacun son tour.", [
        ("Étape 1", "Dites trois choses que vous avez à la maison : « J'ai du riz. »"),
        ("Étape 2", "Dites trois choses que vous n'avez plus : « Je n'ai pas de lait. »"),
        ("Étape 3", "Votre voisin écrit votre liste d'épicerie."),
        ("Étape 4", "Vérifiez ensemble les petits mots."),
    ], cols=1,
       notes="Vingt minutes. C'est l'étape 3 qui compte : écrire la liste de quelqu'un "
             "d'autre oblige à écouter le petit mot, pas seulement le produit.")

    d.billet(
        "Écrivez votre liste d'épicerie de la semaine, cinq lignes.",
        exemples=[
            "Je prends un litre de lait.",
            "Je prends une douzaine d'œufs.",
            "Je n'ai pas de riz : je prends un kilo de riz.",
        ],
        notes="Devoir court, et vraie liste : ils peuvent l'apporter à l'épicerie. C'est "
              "la meilleure preuve que le français sert à quelque chose.")

    return d.save(dossier)
