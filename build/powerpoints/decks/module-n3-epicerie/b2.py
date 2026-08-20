# -*- coding: utf-8 -*-
"""B2 · Dire où c'est.
Bloc B « Défi 1 » · couleur ambre · 60 min.
Source : mini-leçon `t1ou`, exercice `t1ou`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Dire où c'est",
        chapeau="Trois sortes de repères : le numéro de l'allée, la position "
                "dans le magasin, la hauteur de la tablette. Avec les mots "
                "des trois, on comprend n'importe quelle réponse.",
        duree='60 minutes')

    d.titre(notes="Séance de langue. Elle donne les mots que B1 a fait entendre.")

    d.objectifs([
        "employer dans, au fond, au bout ;",
        "employer à côté de, en face de, près de ;",
        "employer en haut, au milieu, en bas ;",
        "donner soi-même une indication complète.",
    ])

    d.declencheur(
        'Observation', "Ces trois réponses disent-elles la même chose ?",
        pistes=[
            "« C'est dans l'allée cinq. »",
            "« C'est au fond, à gauche. »",
            "« C'est en bas, à côté du vinaigre. »",
            "Laquelle vous aide le plus ?",
        ],
        notes="Les trois sont utiles, et elles ne se remplacent pas : la première dit où "
              "aller, la deuxième comment s'y rendre, la troisième où regarder une fois sur "
              "place.")

    d.tableau('Analyse', "Trois sortes de repères",
              ['La sorte', 'Les mots'],
              [["Le numéro", "dans l'allée cinq, allée douze"],
               ["La position", "au fond, près de l'entrée, en face des caisses"],
               ["La hauteur", "en haut, au milieu, en bas"]],
              cle=0,
              note="Une bonne réponse en contient souvent deux : le numéro, puis la hauteur.",
              notes="Diapo à photographier. Faire produire une indication à deux repères "
                    "par cinq élèves.")

    d.regle("Au fond, ou au bout ?",
            "Deux mots proches, deux endroits différents.",
            precision="<b>Au fond</b> parle du <b>magasin</b> : le mur le plus loin de la "
                      "porte d'entrée. <b>Au bout de l'allée</b> parle d'une <b>seule "
                      "rangée</b> : là où elle se termine. « Tout au fond » et « au bout de "
                      "l'allée cinq » n'envoient pas au même endroit.",
            notes="Diapo à photographier. La confusion est fréquente et fait perdre du "
                  "temps.")

    d.cartes("Les mots de position", "Trois paires", [
        ("Près de / loin de",
         "« Près de l'entrée », « loin des caisses ». Utile quand on ne connaît pas encore "
         "les numéros."),
        ("À côté de / en face de",
         "« À côté du vinaigre » : juste à droite ou à gauche, dans la même allée. « En "
         "face des caisses » : de l'autre côté, quand on se tourne."),
        ("À droite / à gauche",
         "Toujours du point de vue de celui qui avance dans l'allée. En cas de doute, "
         "demandez : « à droite en entrant ? »"),
    ], notes="La dernière précision évite beaucoup de malentendus.")

    d.tableau('Analyse', "La hauteur, et pourquoi",
              ['Le mot', 'Ce qui s\'y trouve'],
              [["en haut", "les formats rares, les marques moins vendues"],
               ["au milieu", "le format le plus vendu, à hauteur des yeux"],
               ["en bas", "les grands formats, les sacs lourds"]],
              cle=2,
              note="Le lourd est en bas : ce n'est pas un hasard, c'est plus sûr à porter.",
              notes="Rappel de A3. Le lien entre la hauteur et le format est ce qui rend la "
                    "règle facile à retenir.")

    d.piege("Chercher seulement à hauteur des yeux",
            "Il n'y en a plus, la tablette est vide.",
            "Baisser les yeux avant de conclure.",
            "Le grand format est en bas, et c'est souvent celui qu'on cherche quand on "
            "achète pour une famille. Une tablette vide à hauteur des yeux ne veut pas dire "
            "que le magasin n'en a plus.",
            notes="Erreur très fréquente, et facile à corriger une fois nommée.")

    d.pratique('Pratique · 1 de 2', "Complétez l'indication",
               "Employez le mot de lieu qui convient.", [
        ("L'huile est ___ l'allée cinq.", "dans"),
        ("Les produits du monde sont tout au ___ .", "fond"),
        ("L'huile est ___ côté du vinaigre.", "à"),
        ("Les grands sacs sont ___ bas.", "en"),
        ("La pharmacie est ___ face des caisses.", "en"),
        ("Le pain est ___ de l'entrée.", "près"),
    ], corrige=True,
       notes="Utiliser l'exercice 2 du module.")

    d.pratique('Pratique · 2 de 2', "À deux · donnez l'indication",
               "Un client demande, l'autre répond avec deux repères.", [
        ("Le client", "« Excusez-moi, je cherche le riz. »"),
        ("Le commis", "un numéro d'allée + une hauteur"),
        ("Le client", "vérifie le chiffre : « cinq ou quinze ? »"),
        ("On change de rôle", "après trois produits"),
    ], cols=1,
       notes="Vingt minutes. Circuler et relever deux bonnes indications à lire au groupe.")

    d.billet(
        "Écrivez où se trouvent cinq produits, chez vous ou à l'épicerie.",
        exemples=[
            "Deux repères par phrase : « dans le placard du haut, à côté du sucre ».",
            "Employez cinq mots de lieu différents.",
        ],
        notes="Ramasser et corriger l'emploi de « à côté du / de la ».")

    return d.save(dossier)
