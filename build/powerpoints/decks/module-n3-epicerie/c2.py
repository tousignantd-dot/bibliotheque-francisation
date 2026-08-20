# -*- coding: utf-8 -*-
"""C2 · Les mots qui mesurent.
Bloc C « Défi 2 » · couleur ambre · 60 min.
Source : mini-leçon `t2quantite`, exercice `t2quantite`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Les mots qui mesurent',
        chapeau="On n'achète pas « du riz » : on achète un sac de riz, un "
                "kilo de pommes, une bouteille d'huile. Le mot de quantité, "
                "puis « de » — toujours.",
        duree='60 minutes')

    d.titre(notes="Apporter si possible un paquet, une boîte de conserve et une bouteille. "
                  "Les faire nommer avant d'ouvrir la séance.")

    d.objectifs([
        "employer les mots de contenant ;",
        "distinguer la livre et le kilo ;",
        "employer « de » et « d' » après un mot de quantité ;",
        "composer une commande complète.",
    ])

    d.declencheur(
        'Écoute', "Laquelle de ces demandes est complète ?",
        pistes=[
            "« Du riz, s'il vous plaît. »",
            "« Un sac de riz, s'il vous plaît. »",
            "« Deux kilos de riz, s'il vous plaît. »",
            "Qu'est-ce qui manque à la première ?",
        ],
        notes="La première laisse la personne deviner la quantité. Les deux autres sont "
              "complètes : l'une par le contenant, l'autre par le poids.")

    d.tableau('Analyse', "Ce qui contient",
              ['Le mot', 'Pour quoi'],
              [["un paquet de", "pâtes, biscuits, café"],
               ["une boîte de", "conserve, céréales"],
               ["un sac de", "riz, farine, pommes"],
               ["une bouteille de", "huile, jus, vinaigre"]],
              cle=0,
              note="Le contenant donne la quantité, sans qu'on ait à peser.",
              notes="Diapo à photographier. Faire produire une phrase par ligne.")

    d.tableau('Analyse', "Deux cas à part",
              ['Le mot', 'Pour quoi'],
              [["un pot de", "confiture, yogourt"],
               ["une douzaine de", "œufs — c'est un nombre, pas un contenant"]],
              cle=1,
              note="« Une douzaine », c'est douze : le mot dit le nombre, pas la boîte.",
              notes="La deuxième ligne surprend souvent : « une douzaine » ne décrit pas "
                    "l'emballage.")

    d.regle("La livre et le kilo",
            "Les deux s'emploient ici, et ce n'est pas la même chose.",
            precision="Une <b>livre</b> pèse environ 450 grammes, un peu moins d'un "
                      "demi-kilo. La viande s'annonce souvent à la livre ; les fruits et "
                      "légumes, au kilo. Sur l'étiquette du rayon, les deux prix sont "
                      "souvent écrits : <b>3,99 $ / lb</b> et <b>8,80 $ / kg</b>.",
            notes="Diapo à photographier. C'est une particularité d'ici qui déroute "
                  "beaucoup de nouveaux arrivants.")

    d.regle("Toujours « de »",
            "un kilo de pommes, une bouteille d'huile",
            precision="Le mot de quantité est toujours suivi de <b>de</b> — et de rien "
                      "d'autre. Devant une voyelle, « de » devient <b>d'</b> : une "
                      "bouteille <b>d'</b>huile, une douzaine <b>d'</b>œufs. On ne dit "
                      "jamais « un kilo <s>des</s> pommes ».",
            notes="Diapo à photographier. C'est la seule vraie difficulté grammaticale de "
                  "la séance, et elle est sans exception.")

    d.cartes("Ce qui se verse, ce qui se compte", "Deux autres façons", [
        ("Ce qui se verse",
         "Un litre de lait, 500 millilitres de crème. Le contenant l'indique en chiffres, "
         "sur l'étiquette."),
        ("Ce qui se compte",
         "Six pommes, quatre morceaux de poulet. Sans mot de quantité : le nombre suffit."),
        ("Le nombre devant",
         "« Deux paquets de pâtes », « trois boîtes de tomates ». Le nombre se place avant "
         "le contenant, jamais après."),
    ], notes="La troisième carte évite « paquets deux », erreur d'ordre fréquente.")

    d.piege("Comparer une livre et un kilo",
            "3,99 $ la livre, c'est moins cher que 6,50 $ le kilo.",
            "Une livre pèse moins de la moitié d'un kilo.",
            "À 3,99 $ la livre, le kilo revient à près de 8,80 $ — donc plus cher que "
            "6,50 $. Pour comparer deux prix, il faut d'abord les ramener à la même unité.",
            notes="Faire le calcul au tableau. C'est le genre de comparaison qui revient "
                  "chaque semaine dans une circulaire.")

    d.pratique('Pratique · 1 de 2', "Le mot de quantité",
               "Complétez.", [
        ("Un ___ de pâtes, s'il vous plaît.", "paquet"),
        ("Deux ___ de conserve de tomates.", "boîtes"),
        ("Le poulet est à trois dollars la ___ .", "livre"),
        ("Une ___ d'huile, la grande.", "bouteille"),
        ("Une ___ d'œufs, ça fait douze.", "douzaine"),
        ("Un kilo ___ pommes.", "de"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module.")

    d.pratique('Pratique · 2 de 2', "Composez la commande",
               "Un produit, une quantité, une phrase complète.", [
        ("des pâtes", "un paquet de pâtes / deux paquets de pâtes"),
        ("du poulet", "une livre de poulet / quatre morceaux de poulet"),
        ("des pommes", "un kilo de pommes / six pommes"),
        ("de l'huile", "une bouteille d'huile / un litre d'huile"),
    ], corrige=True, cols=1,
       notes="Plusieurs réponses justes par ligne. Faire dire à voix haute, avec « s'il "
             "vous plaît ».")

    d.billet(
        "Reprenez votre liste d'épicerie et ajoutez les quantités.",
        exemples=[
            "Un mot de quantité pour chaque produit.",
            "Au moins un poids, un contenant et un nombre.",
        ],
        notes="Prolonge le billet de B4. La liste devient utilisable telle quelle.")

    return d.save(dossier)
