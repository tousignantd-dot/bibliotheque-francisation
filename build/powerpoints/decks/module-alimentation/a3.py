# -*- coding: utf-8 -*-
"""A3 · Où regarder sur un emballage.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercice `prEtiqOu` et son encadré de savoir.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-alimentation/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Où regarder sur un emballage',
        chapeau="Un emballage porte quarante informations. Quatre seulement "
                "servent au moment d'acheter — et chacune est toujours au même "
                "endroit, quelle que soit la marque.",
        duree='60 minutes')

    d.titre(notes="Apporter trois emballages vides du même type de produit, de marques "
                  "différentes. La séance ne vaut que sur du vrai.")

    d.objectifs([
        "trouver le tableau de la valeur nutritive sur n'importe quel emballage ;",
        "trouver la provenance et la date ;",
        "comparer deux marques en regardant la bonne ligne ;",
        "employer le prix au kilo pour comparer deux formats.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui est écrit là ?",
        image=IMG + 'etiquette-dos.jpg',
        pistes=[
            "Où se trouve ce tableau, sur tous les produits ?",
            "Pourquoi est-il toujours en noir et blanc ?",
            "Quelle ligne regardez-vous, vous ?",
            "Y a-t-il une information que vous cherchez et que vous ne trouvez jamais ?",
        ],
        notes="Le noir et blanc et l'encadrement sont obligatoires au Canada : c'est ce "
              "qui rend le tableau reconnaissable d'un coup d'œil, même sans lire.")

    d.tableau('Analyse', "Quatre informations, quatre endroits",
              ['Ce que je cherche', 'Où je regarde'],
              [["La valeur nutritive", "au dos, encadré, en noir et blanc"],
               ["La provenance", "en petit, sous le code-barres"],
               ["La date", "en avant ou sur le dessus"],
               ["Le prix au kilo", "sur l'étiquette de la tablette, en petit"]],
              cle=0,
              note="Aucune ne change de place d'une marque à l'autre.",
              notes="Diapo centrale. Faire vérifier sur les trois emballages apportés : la "
                    "constance surprend.")

    d.regle('Le tableau ne bouge jamais',
            "Au dos, encadré, en noir et blanc. Sur tous les produits.",
            precision="C'est une obligation légale au Canada. Vous n'avez donc jamais à le "
                      "chercher : vous savez d'avance où il est et à quoi il ressemble. "
                      "C'est ce qui rend la comparaison rapide.",
            notes="Le dire : cette régularité est une aide, pas une contrainte. Elle vaut "
                  "pour tous les aliments emballés vendus ici.")

    d.regle('Le prix au kilo, pour comparer',
            "Deux formats différents ne se comparent que par le prix au poids.",
            precision="Un grand sac de riz de huit kilos et un petit sac de deux kilos : "
                      "seul le prix au kilo dit lequel est avantageux. Il est écrit en "
                      "petit sur l'étiquette de la tablette, à côté du prix total.",
            notes="Montrer une vraie étiquette de tablette si possible. Beaucoup d'élèves "
                  "ne l'ont jamais remarqué.")

    d.piege('Comparer deux prix totaux',
            "Le petit sac coûte 6 $, le grand 20 $. Le petit est moins cher.",
            "Le petit fait 2 kg (3 $/kg), le grand 8 kg (2,50 $/kg). Le grand est moins cher.",
            "Le prix total ne dit rien tant qu'on ne connaît pas la quantité. C'est le "
            "prix au kilo qui compare — et l'écart peut atteindre le double, comme dans le "
            "dialogue du riz au bloc C.",
            notes="Faire le calcul au tableau avec le groupe. C'est de l'arithmétique "
                  "simple qui économise chaque semaine.")

    d.pratique('Pratique · 1 de 2', "Où je regarde ?",
               "Dites où se trouve chaque information.", [
        ("Le nombre de calories", "au dos, dans le tableau encadré"),
        ("La quantité de sel", "au dos, à la ligne du sodium"),
        ("Le pays d'origine", "en petit, sous le code-barres"),
        ("La date « meilleur avant »", "en avant ou sur le dessus"),
        ("Le prix au kilo", "sur l'étiquette de la tablette, en petit"),
    ], corrige=True, cols=1,
       notes="Faire chercher pour de vrai sur les emballages apportés avant de corriger.")

    d.pratique('Pratique · 2 de 2', "Quel format est le plus avantageux ?",
               "Calculez le prix au kilo.", [
        ("Riz : 2 kg à 6 $ ou 8 kg à 20 $", "3 $/kg contre 2,50 $/kg — le grand"),
        ("Pâtes : 500 g à 2 $ ou 1 kg à 3,50 $", "4 $/kg contre 3,50 $/kg — le grand"),
        ("Café : 300 g à 9 $ ou 1 kg à 26 $", "30 $/kg contre 26 $/kg — le grand"),
        ("Yogourt : 500 g à 4 $ ou 750 g à 6,75 $", "8 $/kg contre 9 $/kg — le petit"),
    ], corrige=True, cols=1,
       notes="La dernière ligne est celle qui compte : le grand format n'est pas toujours "
             "le plus avantageux. C'est justement pour cela qu'on regarde.")

    d.cartes('Deux dates, deux sens', "À ne pas confondre", [
        ("« Meilleur avant »",
         "Une date de <b>qualité</b>. Après, le goût ou la texture changent, mais "
         "l'aliment n'est pas dangereux. On la trouve sur la plupart des produits."),
        ("« Date limite d'utilisation »",
         "Une date de <b>sécurité</b>. Après, on ne consomme pas. Elle est rare : surtout "
         "les préparations pour nourrissons et quelques produits frais."),
        ("Ce que ça change",
         "Confondre les deux fait jeter beaucoup de nourriture encore bonne — ou garder "
         "ce qui ne l'est plus."),
    ], notes="Ce point revient en D1. L'installer ici suffit ; ne pas développer.")

    d.billet(
        "Prenez trois emballages chez vous et notez, pour chacun, les quatre informations.",
        exemples=[
            "Valeur nutritive, provenance, date, format.",
            "Notez aussi le temps que ça vous a pris de les trouver.",
        ],
        notes="Devoir concret. Le temps noté diminue nettement du premier au troisième "
              "emballage : c'est encourageant à faire remarquer.")

    return d.save(dossier)
