# -*- coding: utf-8 -*-
"""B2 · Trois coordonnées, et rien d'autre
Bloc B « Défi 1 · Le bruit qu'il faut décrire » · couleur ambre · production
orale · 75 min.
Source : exercice `t1dire` et sa mini-leçon ; exercice `t1img`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Trois coordonnées, et rien d'autre",
        chapeau="« Ça marche mal » coûte deux heures de recherche. « Un "
                "cognement, à froid, au passage des rapports » fait ouvrir "
                "le capot au bon endroit.",
        duree='75 minutes')

    d.titre(notes="Séance de production orale, la première du module. Prévoir que "
                  "chacun décrive une panne devant deux personnes au moins. C'est "
                  "l'exercice qui prépare directement E1.")

    d.objectifs([
        "nommer un symptôme avec un mot précis ou une comparaison ;",
        "donner la condition qui déclenche le problème ;",
        "chiffrer la fréquence au lieu de dire « des fois » ;",
        "distinguer ce qui aide un mécanicien de ce qui ne l'aide pas.",
    ], notes="Le quatrième objectif est le plus court à enseigner et le plus long à "
             "installer : il demande de renoncer à donner son hypothèse, ce que tout "
             "le monde fait spontanément.")

    d.declencheur(
        'Mise en situation', "Pourquoi un garagiste facture-t-il une heure de diagnostic ?",
        pistes=[
            "Que fait-il pendant cette heure-là ?",
            "Que se passe-t-il s'il sait déjà où regarder ?",
            "Qui décide de la durée de la recherche : lui, ou le client ?",
            "Est-ce que donner votre hypothèse l'aide ou lui coûte du temps ?",
        ],
        notes="La dernière question dérange, et c'est voulu : une hypothèse oblige le "
              "mécanicien à la vérifier, même quand il sait déjà qu'elle est fausse. "
              "Laisser le groupe y arriver seul.")

    d.tableau('Analyse', "Les trois coordonnées d'une panne",
              ['La coordonnée', 'Ce qu\'on dit'],
              [["Le quoi", "cognement, grincement, sifflement, vibration"],
               ["Où", "à l'avant, à droite, sous le plancher"],
               ["Le quand", "à froid, en côte, au freinage, en tournant"],
               ["Le combien", "systématiquement, une fois sur trois"],
               ["Depuis quand", "la date, et ce qui a changé avant"]],
              cle=0,
              notes="Diapositive à photographier, et à laisser affichée pendant toute "
                    "la pratique orale. Elle remplace toute autre consigne.")

    d.cartes('Analyse', "Ce qui ne se dit pas, et par quoi le remplacer", [
        ("« Ça marche mal »", "quel bruit, ou quel symptôme, et où ?"),
        ("« Des fois »", "une fois sur trois, ou trois matins sur cinq"),
        ("« Depuis un bout de temps »", "depuis le 24 avril"),
        ("« Je pense que c'est le moteur »", "rien : décrire, et laisser conclure"),
    ], notes="Les quatre formules de gauche sont celles qu'on entend vraiment. Les "
             "écrire au tableau et les barrer une par une au fil de la séance.")

    d.regle("Dire quand ça n'arrive pas vaut autant que dire quand ça arrive",
            "Chaque « jamais » élimine une famille d'hypothèses.",
            precision="« Jamais le soir », « jamais sur le plat », « aucun témoin "
                      "lumineux ne s'est allumé » sont des informations complètes, et "
                      "elles ne coûtent rien à donner. C'est même l'une des rares "
                      "occasions où l'on rend service en disant ce qu'on n'a pas vu.",
            notes="Diapositive à photographier. Faire trouver au groupe trois « jamais » "
                  "utiles à partir du dialogue de B1 : le soir, après dix minutes, sur "
                  "le plat.")

    d.pratique('Production orale', "Est-ce que ça aide le garagiste ?",
               "Pour chaque phrase, dites : ça aide, ou ça n'aide pas.", [
        ("Ça marche mal depuis un bout de temps.", "ça n'aide pas : aucune coordonnée"),
        ("Un cognement sous le plancher, à droite, au passage des rapports.", "ça aide : trois coordonnées"),
        ("Ça fait un drôle de son des fois.", "ça n'aide pas : « des fois » ne se vérifie pas"),
        ("Le bruit apparaît à froid et disparaît après dix minutes.", "ça aide : la condition et sa limite"),
        ("Aucun témoin lumineux ne s'est allumé.", "ça aide : élimine tout l'électronique"),
        ("Je pense que c'est le moteur, ou peut-être autre chose.", "ça n'aide pas : une hypothèse à vérifier"),
    ], corrige=True,
       notes="Dix items dans le module ; en projeter six. Faire réécrire à voix haute "
             "les trois mauvais énoncés en bons énoncés : c'est là que l'apprentissage "
             "se fait.")

    d.pratique('Production orale', "Décrivez une panne, deux par deux",
               "L'un décrit, l'autre coche les trois coordonnées. Puis on échange.", [
        ("Une laveuse qui ne vidange plus", "symptôme, moment du cycle, fréquence"),
        ("Un four qui chauffe mal", "trop chaud ou pas assez, en combien de temps, en quel mode"),
        ("Une auto qui tire à droite", "à quelle vitesse, au freinage ou non, toujours ou parfois"),
        ("Un chauffe-eau qui manque d'eau chaude", "après combien de minutes, à quelle heure, chaque jour ou non"),
    ], corrige=True,
       notes="Quinze minutes, quatre situations, deux tours chacun. Circuler et "
             "n'intervenir que sur une chose : la fréquence, qui est toujours la "
             "coordonnée oubliée.")

    d.billet(
        "Réécris « ça marche mal » en trois coordonnées, pour un appareil de ton choix.",
        exemples=[
            "Le quoi, le quand, le combien.",
            "Une seule phrase, mais complète.",
        ],
        notes="Trois minutes. Ces billets se rendent en B4, où ils servent d'énoncés "
              "au passage du plus-que-parfait : on y ajoute ce qui s'était passé avant.")

    return d.save(dossier)
