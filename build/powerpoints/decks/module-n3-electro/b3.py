# -*- coding: utf-8 -*-
"""B3 · Les mots de la circulaire.
Bloc B « Défi 1 · Lire la circulaire » · couleur teal · 60 min.
Source : exercices `t1circ` et `t1b` (l'encadré de la page 3).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='teal',
        titre='Les mots de la circulaire',
        chapeau="Prix régulier, en spécial, à partir de, quantité limitée : "
                "six expressions reviennent dans toutes les circulaires du "
                "Québec, et elles décident de ce qu'on paiera.",
        duree='60 minutes')

    d.titre(notes="Séance de compréhension écrite. C'est le cœur du programme pour cette "
                  "situation : l'unique intention de communication du niveau 3 est de "
                  "lire des circulaires, des catalogues et des affichettes.")

    d.objectifs([
        "comprendre six expressions de circulaire ;",
        "trouver une information précise dans un encadré ;",
        "reconnaître ce qui est écrit en petit et pourquoi ;",
        "dire à voix haute ce qu'on a compris d'un encadré.",
    ])

    d.tableau('Analyse', "Six expressions et ce qu'elles veulent dire",
              ['Ce qui est écrit', 'Ce que ça veut dire'],
              [["le prix régulier", "le prix des autres semaines"],
               ["en spécial", "à prix plus bas, quelques jours seulement"],
               ["le modèle", "les lettres et les chiffres de l'appareil"],
               ["la marque", "le nom de la compagnie qui le fabrique"]],
              cle=1,
              note="Ces quatre-là sont écrits en gros : ce sont les mots qui vendent.",
              notes="Diapo à photographier. Faire retrouver chacune de ces expressions "
                    "dans les circulaires rapportées en classe.")

    d.tableau('Analyse', "Deux expressions écrites en petit",
              ['Ce qui est écrit', 'Ce que ça change'],
              [["quantité limitée", "il y en a peu : quand c'est vendu, c'est fini"],
               ["à partir de 499 $", "c'est le moins cher du groupe ; les autres coûtent plus"],
               ["livraison en sus", "la livraison n'est pas comprise dans le prix"]],
              cle=1,
              note="Le gros chiffre attire l'œil ; ces trois lignes-là décident.",
              notes="Diapo à photographier. « À partir de » est le piège le plus courant : "
                    "la photo montre le gros modèle, le prix est celui du petit.")

    d.cartes("L'encadré de la page 3", "Ce que la circulaire dit de la laveuse", [
        ("Marque et modèle",
         "Laveuse Norlac, modèle LT 4200, blanche."),
        ("Les deux prix",
         "849 $ cette semaine. Prix régulier 1 049 $, barré."),
        ("Le format et les dates",
         "27 pouces de large. Du mardi 4 au dimanche 9 novembre."),
        ("Ce qui est écrit en petit",
         "Quantité limitée. Livraison en sus."),
    ], notes="C'est l'encadré de l'exercice 5 du module interactif. Le projeter, puis "
             "poser les questions de la pratique ci-dessous sans le montrer.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après l'encadré.", [
        ("La laveuse coûte 849 $ cette semaine.", "vrai"),
        ("Le magasin enlève 200 $ sur le prix régulier.", "vrai"),
        ("La laveuse fait 27 pouces de large.", "vrai"),
        ("La livraison est comprise dans le prix.", "faux — livraison en sus"),
        ("Il y a beaucoup de laveuses à ce prix-là.", "faux — quantité limitée"),
        ("Le spécial est encore bon le lundi 10 novembre.", "faux — il finit le 9"),
    ], corrige=True,
       notes="Faire justifier chaque réponse en montrant la ligne de l'encadré. C'est "
             "l'exercice d'évaluation de la compétence en lecture.")

    d.regle("Lire l'encadré dans l'ordre qui sert",
            "le nom, le prix, le format, les dates",
            precision="Quatre regards, quatre réponses. Le reste de l'encadré — "
                      "les caractéristiques, les étoiles, les mentions — ne "
                      "change rien à la décision d'y aller ou non.",
            notes="Diapo à photographier. Faire refaire les quatre regards sur une autre "
                  "circulaire, chronomètre en main : trente secondes suffisent.")

    d.piege("Se fier à la photo",
            "la grosse laveuse de la photo est à 499 $",
            "à partir de 499 $ : c'est le petit modèle",
            "Quand un encadré dit « à partir de », le prix est celui du modèle le moins "
            "cher du groupe, et ce n'est presque jamais celui de la photo. Le vérifier "
            "coûte une question au vendeur ; ne pas le vérifier coûte deux cents "
            "dollars de surprise.",
            notes="Chercher un « à partir de » dans les circulaires rapportées : il y en "
                  "a presque toujours un.")

    d.billet(
        "Choisissez un appareil dans votre circulaire et écrivez quatre lignes.",
        exemples=[
            "La marque et le modèle. Le prix de cette semaine.",
            "Le prix régulier. La date de fin.",
        ],
        notes="Devoir de lecture. Ces quatre lignes sont exactement ce qu'il faut "
              "apporter au magasin : le dire aux élèves.")

    return d.save(dossier)
