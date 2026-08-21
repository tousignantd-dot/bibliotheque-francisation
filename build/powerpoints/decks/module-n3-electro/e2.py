# -*- coding: utf-8 -*-
"""E2 · Je retiens des mots.
Bloc E « Je me lance » · couleur framboise · 60 min.
Source : banc `FC_CARDS`, cartes mémoire et autoévaluation du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E2', section='framboise',
        titre='Je retiens des mots',
        chapeau="Seize mots, quatre familles, et une question : qu'est-ce que "
                "je suis maintenant capable de faire dans un magasin "
                "d'appareils ?",
        duree='60 minutes')

    d.titre(notes="Dernière séance du module. Prévoir les cartes mémoire du module "
                  "interactif : la révision se fait à l'écran, en paires.")

    d.objectifs([
        "revoir les seize mots du module, par familles ;",
        "employer chaque mot dans une phrase ;",
        "évaluer ce qu'on est capable de faire ;",
        "nommer ce qui reste à travailler.",
    ])

    d.cartes("Les appareils", "Sept mots", [
        ("une laveuse, une sécheuse",
         "Les deux grosses machines du linge. Elles vont souvent ensemble, et le magasin "
         "les vend en paire."),
        ("un réfrigérateur, une cuisinière",
         "Le froid et la chaleur. Dans beaucoup de logements d'ici, ces deux-là sont "
         "fournis avec le loyer."),
        ("un micro-ondes, un aspirateur",
         "Les petits appareils : ils se transportent à la main et coûtent moins de deux "
         "cents dollars."),
        ("un ordinateur portable",
         "L'appareil de l'école et des démarches. Il s'achète aussi en ligne, sur le "
         "site du magasin."),
    ], notes="Faire dire chaque mot avec son article, puis dans une phrase complète.")

    d.cartes("La circulaire et le magasin", "Neuf mots", [
        ("une circulaire, un spécial",
         "Le papier du mardi, et le prix plus bas de la semaine."),
        ("le prix régulier, la marque, le modèle",
         "Ce qu'on relève avant de partir : le prix des autres semaines, le nom de la "
         "compagnie, les lettres et les chiffres de l'appareil."),
        ("le rayon, une affichette",
         "L'endroit où sont les appareils, et le petit carton posé devant."),
        ("la livraison, un bon de livraison",
         "Le camion, et le papier à garder jusqu'à son passage."),
    ], notes="Faire retrouver chaque mot dans une circulaire réelle. Ce qui ne se "
             "retrouve pas se réexplique.")

    d.pratique('Vocabulaire', "Le mot juste",
               "Complétez avec un mot du module.", [
        ("Le papier du magasin qui arrive le mardi est la ___ .", "circulaire"),
        ("Un prix plus bas pendant quelques jours est un ___ .", "spécial"),
        ("L'endroit du magasin où sont les laveuses est le ___ .", "rayon"),
        ("Le petit carton devant l'appareil est une ___ .", "affichette"),
        ("Le camion qui apporte l'appareil fait la ___ .", "livraison"),
        ("Le papier à garder jusqu'au camion est le ___ de livraison.", "bon"),
    ], corrige=True,
       notes="Exercice d'entrée. Il reprend exactement l'exercice 2 de « Je me lance » "
             "du module interactif.")

    d.tableau('Analyse', "Ce que le module a appris à faire",
              ['Compétence', 'Ce qu\'on sait faire'],
              [["Lire", "trouver un prix, un modèle et des dates dans une circulaire"],
               ["Écouter", "comprendre un vendeur qui donne un prix et une mesure"],
               ["Parler", "poser quatre questions et conclure un achat"],
               ["Écrire", "un court message de demande de livraison"]],
              cle=1,
              note="La lecture est l'intention que le programme donne à cette "
                   "situation au niveau 3 ; les trois autres la servent.",
              notes="Diapo à photographier. C'est la carte du module entier, et le "
                    "point de départ de l'autoévaluation.")

    d.pratique('Autoévaluation', "Qu'est-ce que je suis capable de faire ?",
               "Pour chaque énoncé : pas encore, un peu, ou oui.", [
        ("Je peux nommer les appareils de la maison.", ""),
        ("Je trouve le prix et les dates dans une circulaire.", ""),
        ("Je peux lire et écrire un prix de trois ou quatre chiffres.", ""),
        ("Je peux demander où est le rayon d'un appareil.", ""),
        ("Je peux montrer un appareil et demander son prix.", ""),
        ("Je peux demander la livraison et donner un jour.", ""),
    ], corrige=False,
       notes="Les mêmes énoncés que dans le module interactif. Les élèves répondent à "
             "l'écran ; la diapositive sert à la mise en commun.")

    d.regle("Ce qui reste à faire, chacun le nomme",
            "« La prochaine fois, je vais demander… »",
            precision="Une seule chose, écrite en une phrase, au futur proche. "
                      "C'est le dernier emploi du point de langue de D2, et "
                      "c'est ce qui reste du module dans un mois.",
            notes="Faire dire la phrase à voix haute par chaque élève, en tour de table. "
                  "Cinq minutes, et le module se ferme sur du concret.")

    d.billet(
        "Écrivez la phrase de votre prochaine fois.",
        exemples=[
            "« La prochaine fois, je vais demander le format avant de payer. »",
            "Gardez-la dans votre cahier.",
        ],
        notes="Fin du module. Rappeler que les cartes mémoire restent accessibles et "
              "que le jeu de rôle peut se refaire autant de fois qu'on veut.")

    return d.save(dossier)
