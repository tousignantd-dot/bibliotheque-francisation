# -*- coding: utf-8 -*-
"""C1 · Devant l'écran, à la cuisine
Bloc C « Défi 2 · Ce qui est écrit sur la région » · acier · 75 min.
Source : dialogue `t2`, exercice `t2a`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-quebec/vocab/')


def img(nom):
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Devant l'écran, à la cuisine",
        chapeau="Tout ce que Thuy doit savoir est écrit quelque part : "
                "l'heure des départs, la durée du trajet, ce qu'il y a dans "
                "le parc, ce que coûte une nuit. Mais le plus utile — qu'il "
                "fait cinq degrés la nuit fin septembre — n'est écrit nulle "
                "part.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 2. Le fil de tout le bloc tient dans une "
                  "réplique de Camille : « Ce n'est jamais écrit. C'est pour ça que tu "
                  "me demandes. » Lire vite un texte est une compétence ; savoir ce "
                  "qu'il ne dira pas en est une autre.")

    d.objectifs([
        "trouver dans un texte les cinq lignes qui nous concernent ;",
        "comprendre les mots du paysage employés dans une fiche de parc ;",
        "distinguer ce qui est écrit de ce qu'il faut demander ;",
        "comparer deux possibilités et dire laquelle on choisit, et pourquoi.",
    ], notes="Le troisième objectif est le plus transférable du module : il vaut pour un "
             "bail, un contrat de travail et une ordonnance. Le nommer comme tel.")

    d.declencheur(
        'Observation', "La fiche du parc dit : « caps, baies, anses, îles et "
                       "montagnes ». Qu'est-ce que vous comprenez ?",
        image=img('maree.jpg'),
        pistes=[
            "Combien de ces cinq mots connaissez-vous ?",
            "Est-ce que vous pouvez décider d'y aller sans les comprendre ?",
            "À qui pourriez-vous demander ?",
            "Qu'est-ce qu'une fiche officielle ne dit jamais ?",
        ],
        notes="C'est exactement la réaction de Thuy : « je ne connais pas la moitié de "
              "ces mots-là ». Normaliser cette réaction. On peut choisir un parc sans "
              "connaître le mot « anse » — mais pas décider quoi emporter.")

    d.dialogue('Dialogue · 1 de 3', "Un cap, une anse", [
        ("THUY", "C'est écrit : « caps, baies, anses, îles et montagnes, sur "
                 "trente-trois kilomètres carrés ». Je ne connais pas la "
                 "moitié de ces mots-là.", True),
        ("CAMILLE", "Un cap, c'est une pointe de roche qui avance dans l'eau. "
                    "Une anse, c'est un petit creux de la côte, où l'eau est "
                    "calme. Tu les verras, ça ira mieux.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="« Tu les verras, ça ira mieux » : Camille ne fait pas un cours de "
             "vocabulaire, elle rassure. C'est une bonne stratégie et elle mérite d'être "
             "dite au groupe — certains mots s'apprennent en les voyant.")

    d.dialogue('Dialogue · 2 de 3', "Ce qui n'est pas écrit", [
        ("THUY", "Pour dormir, il y a du camping. Et du prêt-à-camper.", True),
        ("CAMILLE", "Le prêt-à-camper, c'est déjà monté. Mais fin septembre, "
                    "la nuit, il fait cinq degrés au bord du fleuve.", True),
        ("THUY", "Cinq degrés ! Ce n'est pas écrit, ça.", True),
        ("CAMILLE", "Ce n'est jamais écrit. C'est pour ça que tu me "
                    "demandes.", True),
    ], notes="La réplique du module. La faire relire deux fois. Demander ensuite au "
             "groupe ce qui n'était écrit nulle part quand ils sont arrivés au Québec, "
             "et qui aurait été utile à savoir.")

    d.dialogue('Dialogue · 3 de 3', "Les heures de marée", [
        ("CAMILLE", "Une dernière chose qui n'est écrite nulle part : les "
                    "heures de marée. Regarde-les avant de marcher jusqu'à "
                    "l'île. Des gens se font prendre chaque été.", True),
        ("THUY", "Comment on les trouve ?", True),
        ("CAMILLE", "À l'accueil du parc, sur une feuille, chaque matin. "
                    "Demande-la.", False),
    ], notes="Point de sécurité réel : on marche jusqu'aux îles du Bic à marée basse et "
             "la mer remonte. Le dire sérieusement. C'est aussi l'exemple parfait d'une "
             "information qui existe, mais qu'il faut aller demander.")

    d.regle("Ce qui est écrit, et ce qui se demande",
            "L'écrit donne les heures, les prix et les distances. Il ne "
            "donne ni la température de la nuit, ni ce qui vaut la peine.",
            precision="Demander n'est pas un aveu d'ignorance : c'est la seule "
                      "façon d'obtenir ce qui n'est écrit nulle part.",
            notes="Diapositive à photographier. Elle justifie le défi 3 en entier : si "
                  "tout était écrit, on n'aurait pas besoin de parler aux gens.")

    d.tableau('Deux colonnes', "Où trouve-t-on quoi ?",
              ["Sur le site", "En demandant"],
              [["Les heures de départ", "S'il faut réserver d'avance"],
               ["Le prix de la nuit", "Si le quartier est tranquille"],
               ["La longueur du sentier", "S'il est difficile"],
               ["Les secteurs de camping", "S'il fait froid la nuit"]],
              cle=1,
              notes="Faire compléter la colonne de droite par le groupe avant de "
                    "l'afficher. C'est l'exercice le plus rentable de la séance.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le parc fait trente-trois kilomètres carrés.", "vrai"),
        ("Le sentier du bord de l'eau fait sept kilomètres.", "faux — cinq ; celui de la montagne fait sept"),
        ("Le gîte coûte le même prix toute l'année.", "faux — 110 $ en haute saison, 90 $ après le 15 septembre"),
        ("Thuy paiera le tarif de basse saison.", "vrai — elle arrive le 28"),
        ("Le train passe à Rimouski tous les jours.", "faux — mercredi, vendredi, dimanche"),
        ("Le train arrive à Rimouski en pleine nuit.", "vrai — départ de Montréal à 18 h 30"),
    ], corrige=True,
       notes="Faire justifier chaque réponse. La troisième et la quatrième vont "
             "ensemble : c'est un calcul, pas une lecture, et c'est ce que le défi 2 "
             "demande vraiment.")

    d.billet(
        "Notez une chose que vous avez déjà eu besoin de savoir et qui n'était écrite nulle part.",
        exemples=[
            "Au Québec ou dans votre pays, peu importe.",
            "Notez aussi à qui vous l'avez demandée, ou à qui vous auriez dû.",
        ],
        notes="Ramasser les billets et en lire deux ou trois au début de C2. Ce sont "
              "souvent les meilleurs moments du module.")

    return d.save(dossier)
