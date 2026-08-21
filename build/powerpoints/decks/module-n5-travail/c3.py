# -*- coding: utf-8 -*-
"""C3 · D'abord, ensuite, puis, enfin
Bloc C « Défi 2 » · couleur ambre · 75 min. Les marqueurs de temps.
Source : exercice `t2ordre`, mini-leçon `t2ordre`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="D'abord, ensuite, puis, enfin",
        chapeau="Écrivez « Refermez la porte. Tirez la feuille. » et "
                "quelqu'un refermera la porte avant de tirer la feuille — "
                "parce que c'est écrit dans cet ordre, et qu'on lit vite.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire du texte. Commencer par l'expérience du chapeau : "
                  "projeter les deux phrases sans marqueur et demander au groupe ce qu'il "
                  "ferait en premier. La moitié se trompe, et la démonstration est faite "
                  "en trente secondes.")

    d.objectifs([
        "ordonner une marche à suivre avec d'abord, ensuite, puis, enfin ;",
        "employer « une fois que » et « après avoir » pour un geste qui en attend un autre ;",
        "placer un avertissement avec « avant de » ;",
        "mettre la virgule au bon endroit.",
    ])

    d.regle("Les marqueurs rendent une marche à suivre illisible à l'envers",
            "Ils coûtent trois mots et ils empêchent une erreur de geste.",
            precision="Deux systèmes existent : les mots — d'abord, ensuite, puis, "
                      "enfin — ou les nombres — premièrement, deuxièmement, "
                      "troisièmement. On en choisit un et on le tient jusqu'à la "
                      "dernière ligne.",
            notes="Le mélange des deux systèmes est la faute la plus visible d'une note "
                  "de travail : le lecteur cherche alors s'il a sauté une étape.")

    d.tableau('La file simple', "Quatre gestes, quatre places",
              ['Le marqueur', 'La place'],
              [["D'abord", "le premier geste, toujours"],
               ["Ensuite", "un geste du milieu"],
               ["Puis", "un autre geste du milieu"],
               ["Enfin", "le dernier geste"],
               ["Finalement", "le dernier aussi, un peu plus lourd"]],
              cle=0,
              notes="« Puis » et « ensuite » sont interchangeables : le dire, sinon les "
                    "élèves cherchent une différence qui n'existe pas. C'est la répétition "
                    "qu'on évite en alternant les deux.")

    d.cartes("Un geste qui en attend un autre", "Trois façons de le dire", [
        ("Une fois que + une phrase",
         "Une fois que l'écran est vert, appuyez sur Démarrer."),
        ("Après avoir + participe passé",
         "Après avoir choisi le format, appuyez sur Confirmer."),
        ("Lorsque, quand + une phrase",
         "Lorsque la copie est sortie, reprenez votre original."),
        ("La différence qui compte",
         "« Après avoir » exige la même personne pour les deux gestes ; "
         "« une fois que », non — on peut attendre que l'appareil ait fini."),
    ], notes="La quatrième carte explique pourquoi « après avoir attendu que l'écran soit "
             "vert » sonne mal : ce n'est pas vous qui rendez l'écran vert.")

    d.regle("Avant de, pour les avertissements",
            "Avant de tirer la feuille, ouvrez la porte de côté.",
            precision="Dans un avertissement, l'ordre des mots compte autant que les "
                      "mots : ce qui est écrit en premier est ce qui sera lu avant le "
                      "geste. « Ouvrez la porte avant de tirer » est déjà trop tard "
                      "pour quelqu'un qui lit vite.",
            notes="Comparer les deux versions au tableau et demander laquelle protège "
                  "vraiment. C'est une leçon de rédaction, pas seulement de grammaire.")

    d.piege("Oublier la virgule",
            "D'abord levez le couvercle.",
            "D'abord, levez le couvercle.",
            "Un marqueur en tête de phrase prend une virgule après lui. Placé au "
            "milieu, il n'en prend pas : « Levez ensuite le couvercle. »",
            notes="Le programme du niveau 5 nomme la ponctuation dans ses savoirs. "
                  "C'est l'occasion la plus concrète de la travailler.")

    d.pratique('Marqueurs', "Complétez la marche à suivre",
               "Employez d'abord, ensuite, puis, enfin, avant de, une fois.", [
        ("___ , levez le couvercle et posez votre feuille face vers le bas.", "D'abord"),
        ("___ , choisissez le nombre de copies avec le clavier.", "Ensuite"),
        ("___ , appuyez sur le gros bouton vert.", "Puis"),
        ("___ , reprenez votre original sous le couvercle.", "Enfin"),
        ("___ tirer la feuille coincée, ouvrez la porte de côté.", "Avant de"),
        ("___ que l'écran est redevenu vert, vous pouvez recommencer.", "Une fois"),
        ("___ avoir choisi le format, appuyez sur Confirmer.", "Après"),
        ("D'abord, ___ , puis, enfin : quatre mots pour quatre gestes.", "ensuite"),
    ], cols=2, corrige=True,
       notes="Les huit énoncés sont ceux de l'exercice interactif. Accepter « puis » et "
             "« ensuite » l'un pour l'autre aux rangées 2 et 3.")

    d.pratique('Production', "Trois marches à suivre",
               "Écrivez chacune en quatre gestes, avec des marqueurs.", [
        ("Faire une copie.",
         "lever le couvercle · placer la feuille · choisir le nombre · appuyer · reprendre l'original"),
        ("Remplir le bac à papier.",
         "vérifier le format · ouvrir le bac · poser la pile bien à plat · refermer sans forcer"),
        ("Régler un bourrage de papier.",
         "ouvrir la porte de côté · tirer lentement, d'un seul mouvement · refermer bien"),
    ], corrige=True,
       notes="Faire écrire en équipes de deux, puis échanger les feuilles : chaque équipe "
             "exécute la marche à suivre de l'autre, en mimant. Les étapes manquantes "
             "sautent aux yeux.")

    d.billet(
        "Écrivez en cinq gestes une marche à suivre de votre vie quotidienne.",
        exemples=[
            "Employez d'abord, ensuite, puis, enfin, et un « avant de » pour un avertissement.",
            "Prendre l'autobus, payer au terminal, faire fonctionner la machine à laver.",
        ],
        notes="Les meilleures seront relues en C4, où l'on choisira entre l'impératif et "
              "l'infinitif de consigne. Demander aux élèves de garder leur billet.")

    return d.save(dossier)
