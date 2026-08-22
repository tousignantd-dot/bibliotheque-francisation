# -*- coding: utf-8 -*-
"""E1 · Décider devant Réjean, puis parler au groupe
Bloc E « Je me lance » · couleur teal · 75 min. Production orale.
Source : bloc « Je me lance » de l'activité interactive — jeu de rôle
`saisons` (trois situations) et message vocal laissé au groupe.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-saisons/images/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Décider devant Réjean, puis parler au groupe",
        chapeau="C'est à vous. Vous annoncez votre décision au coordonnateur "
                "du Centre et vous la défendez ; puis vous laissez au groupe "
                "un message que trente personnes écouteront une seule fois, "
                "sans pouvoir vous demander de répéter.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Elle se fait presque entièrement debout et à "
                  "deux. Prévoir des postes avec écouteurs pour le jeu de rôle, et un "
                  "coin calme pour l'enregistrement. Rendre au début les billets de C4 "
                  "et de D2 : chacun arrive avec son message et sa consigne déjà "
                  "écrits.")

    d.objectifs([
        "annoncer une décision d'un seul tenant, sans se faire arracher les mots ;",
        "la défendre avec l'avis, les chiffres et le calendrier ;",
        "laisser un message de quarante-cinq secondes qui n'oublie rien ;",
        "tenir le vouvoiement du début à la fin.",
    ], notes="Le premier objectif est le critère principal. Si le coordonnateur doit "
             "demander « et la nouvelle date ? », la décision n'était pas annoncée en "
             "entier — c'est ce que le niveau 5 appelle un discours suivi.")

    d.declencheur(
        'Observation', "Que diriez-vous à quelqu'un qui n'a pas écouté la radio ?",
        image=img('verglas-trottoir.jpg'),
        pistes=[
            "Quel avis est en vigueur, et lequel des deux mots porte-t-il ?",
            "Qu'est-ce que cinq millimètres de glace font à un trottoir ?",
            "Est-ce que ce sera encore comme ça samedi à treize heures ?",
            "Trente personnes attendent : par quoi commencez-vous ?",
        ],
        notes="Les quatre questions sont les quatre séances du module, dans l'ordre. "
              "Laisser répondre sans reprendre : le groupe s'entend savoir tout cela, "
              "et c'est le meilleur départ possible pour une séance de production.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("Le verglas de vendredi soir",
         "Avertissement de pluie verglaçante, trois à cinq millimètres de glace. "
         "Marche de samedi, trente personnes, dont huit ont plus de soixante-dix ans."),
        ("La crue printanière au Bic",
         "Les sentiers du bas du parc sont inondés, réouverture dans deux semaines. "
         "Visite dimanche, autobus réservé mais non payé, vingt-deux inscrits."),
        ("La chaleur extrême de la fin de semaine",
         "Trente-deux degrés, humidex de trente-neuf, indice UV de neuf. Tournoi de "
         "pétanque samedi à quatorze heures, en plein soleil."),
    ], cols=3, notes="Ce sont les trois situations de l'activité interactive. "
                     "L'assistant y joue Réjean, le coordonnateur : il conteste une "
                     "fois, poliment, et il attend la nouvelle date. Ce n'est ni une "
                     "panne ni de la mauvaise volonté — c'est ainsi qu'il fait "
                     "travailler la défense d'une décision.")

    d.tableau('Le jeu de rôle', "Huit sujets à couvrir",
              ["Le sujet", "Ce qu'on dit"],
              [["L'avis", "veille ou avertissement, et de quel phénomène"],
               ["Les trois données", "le phénomène, la région, le moment"],
               ["L'effet en chiffres", "millimètres de glace, degrés, indice UV"],
               ["La décision", "maintenue, reportée ou annulée"],
               ["La raison", "dans la même phrase, avec un connecteur"],
               ["La suite", "la nouvelle date, l'heure, le lieu"]],
              cle=1,
              notes="Six des huit sujets de la grille en ligne. Les deux autres — ce "
                    "que l'effet devient à l'heure exacte de l'activité, et ce qu'il "
                    "faudra apporter — sont ceux qu'on oublie : les écrire au tableau "
                    "à côté.")

    d.regle("Ce n'est pas la météo qui décide",
            "On reporte quand il y a une date de rechange, on annule quand il n'y en a pas.",
            precision="C'est la règle du Défi 2, et c'est elle que Réjean vérifie. Une "
                      "tempête n'annule rien par elle-même : c'est le calendrier qui "
                      "tranche entre reporter et annuler.",
            notes="Diapositive à photographier et à laisser projetée pendant tout "
                  "l'atelier. C'est la seule chose que le jeu de rôle sanctionne "
                  "vraiment.")

    d.pratique('Production orale', "Le message laissé au groupe",
               "Cinq temps, dans l'ordre. Écrivez, lisez à voix haute, puis "
               "enregistrez.", [
        ("TEMPS 1", "Bonjour à tous, c'est Marisol du Centre de la Pointe, au sujet de la marche de samedi."),
        ("TEMPS 2", "La sortie est reportée au samedi 22 février, à la même heure, au même endroit."),
        ("TEMPS 3", "Comme un avertissement de pluie verglaçante est en vigueur, il y aura de la glace au sol toute la journée."),
        ("TEMPS 4", "Apportez vos crampons et habillez-vous en trois couches : vous resterez confortable en enlevant une couche au café."),
        ("TEMPS 5", "Si la nouvelle date ne vous convient pas, appelez-moi avant jeudi. Merci, et à bientôt."),
    ], cols=1,
       notes="De trente à quarante-cinq secondes. Laisser recommencer autant de fois "
             "qu'il le faut : c'est l'écoute de soi qui fait progresser, jamais la "
             "première prise.")

    d.piege("Enregistrer sans avoir écrit",
            "J'improvise, c'est plus naturel.",
            "J'écris mes cinq temps, je les lis une fois, puis j'enregistre.",
            "Un message improvisé dure quatre-vingt-dix secondes et oublie deux "
            "choses : la nouvelle date et ce qu'il faut faire si elle ne convient "
            "pas. Ce sont justement les deux qui déclenchent trente appels.",
            notes="Insister : lire ses notes au téléphone n'a rien d'artificiel. Tout "
                  "le monde le fait, y compris les gens dont c'est la langue "
                  "maternelle.")

    d.pratique('Autoévaluation', "Réécoutez-vous comme si vous aviez soixante-quinze ans",
               "Répondez honnêtement avant d'envoyer.", [
        ("Sait-on qui parle et de quelle activité ?", "dès la première phrase"),
        ("La décision arrive-t-elle avant la météo ?", "sinon, on écoute vingt secondes pour rien"),
        ("La nouvelle date, l'heure et le lieu y sont-ils ?", "les trois, pas deux"),
        ("La raison tient-elle en une phrase ?", "une seule, la plus forte"),
        ("Dit-on ce qu'il faut apporter, et comment ?", "impératif, puis gérondif"),
        ("Le message dure-t-il moins de quarante-cinq secondes ?", "sinon, coupez les excuses"),
    ], corrige=True,
       notes="Faire faire l'autoévaluation avant l'envoi à l'enseignante, jamais "
             "après. Les élèves recommencent d'eux-mêmes une fois sur deux, et c'est "
             "exactement le but.")

    d.billet(
        "Après votre enregistrement : notez la chose que vous referiez autrement.",
        exemples=[
            "Une seule chose, la plus importante.",
            "Notez aussi ce qui a bien marché : ça se garde pour la prochaine fois.",
        ],
        notes="Ramasser les billets et les rendre en E2 avec la rétroaction de la "
              "production orale. La comparaison entre ce que l'élève a repéré "
              "lui-même et ce que dit la correction vaut mieux qu'une note.")

    return d.save(dossier)
