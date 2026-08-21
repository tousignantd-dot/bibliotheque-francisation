# -*- coding: utf-8 -*-
"""B1 · Le bulletin de sept heures.
Bloc B « Défi 1 · Le bulletin du matin » · couleur acier · 75 min.
Source : dialogues `t1` et `t1b`, exercices `t1vf`, `t1bul` et `t1b`.

C'est la séance qui porte **l'unique intention du programme** pour cette
situation : « comprendre un bulletin météo », en compréhension écrite. Tout le
module existe pour elle.

Un bulletin de radio dure vingt secondes et ne se répète pas. L'élève n'a pas
à tout comprendre : il a trois choses à attraper — la ville, le mot du temps,
le nombre de degrés. La séance fait donc écouter avant de faire lire, puis
donne la grille de la semaine à lire pour de vrai.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-neige/vocab/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Le bulletin de sept heures",
        chapeau="Attraper la ville, le temps et la température dans un bulletin météo.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 1. Faire écouter le vrai bulletin du matin sur "
                  "le téléphone, sans rien annoncer, puis demander ce que le groupe a "
                  "compris. Le peu qui remonte est exactement le sujet de la séance.")

    d.objectifs([
        "reconnaître le nom d'une ville dans un bulletin ;",
        "attraper le mot du temps : neige, pluie, soleil ;",
        "attraper le nombre de degrés et son signe ;",
        "lire une grille météo de la semaine.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on entend ici, le matin ?",
        image=IMG + 'bulletin-meteo.jpg',
        pistes=[
            "Qu'est-ce qu'il y a sur le comptoir ?",
            "Qu'est-ce qu'on écoute à sept heures du matin ?",
            "Est-ce que vous écoutez la météo ? Où ?",
            "À la radio, sur le téléphone, ou par la fenêtre ?",
        ],
        notes="La quatrième piste vaut la peine : beaucoup d'élèves regardent par la "
              "fenêtre et ne consultent jamais de bulletin. C'est justement ce que la "
              "séance vient changer.")

    d.dialogue('Dialogue · 1 de 2', "À Montréal, neige, moins huit", [
        ("VOIX", "Il est sept heures. Voici la météo.", True),
        ("VOIX", "À Montréal, neige. Moins huit degrés.", True),
        ("VOIX", "Demain, soleil. Moins deux degrés.", True),
        ("YOUSSEF", "Maman, il a dit quoi ?", True),
    ], consigne="Écoutez deux fois, sans regarder le texte.",
       notes="Faire écouter deux fois, diapositive masquée, crayon en main. Demander "
             "seulement trois choses : la ville, le temps, le nombre.")

    d.dialogue('Dialogue · 2 de 2', "Zina redit ce qu'elle a entendu", [
        ("ZINA", "Attends. Il a dit « neige ».", True),
        ("YOUSSEF", "Et les degrés ?", True),
        ("ZINA", "Moins huit. Il fait moins huit aujourd'hui.", True),
        ("YOUSSEF", "Moins deux, c'est moins froid. C'est bien !", True),
    ], notes="Zina ne comprend pas tout non plus : elle attrape deux choses et les "
             "redit. Le dire au groupe — c'est la stratégie qu'on enseigne, pas un "
             "défaut du personnage.")

    d.tableau('Analyse', "Trois choses à attraper, et rien d'autre",
              ["Ce qu'on cherche", "Ce qu'on entend"],
              [["La ville", "À Montréal… · À Québec… · En Gaspésie…"],
               ["Le temps", "neige · pluie · soleil · nuages · vent"],
               ["La température", "moins huit degrés · plus quatre degrés"],
               ["Et toujours demain", "le bulletin donne le lendemain juste après"]],
              cle=1,
              note="Un bulletin de vingt secondes tient en trois mots dans un carnet.",
              notes="Diapositive à photographier. Insister sur la quatrième rangée : "
                    "beaucoup d'élèves arrêtent d'écouter dès qu'ils ont aujourd'hui.")

    d.vocabulaire('Vocabulaire', "Les mots du bulletin", [
        ("un bulletin météo", "Le message qui dit le temps d'aujourd'hui et de demain."),
        ("un degré", "L'unité qui mesure le froid et le chaud."),
        ("une ville", "Un endroit avec beaucoup de maisons et beaucoup de monde."),
        ("l'hiver", "La saison de la neige et du froid, au Québec."),
    ], notes="Diapositive à photographier. Nommer trois ou quatre villes proches du "
             "centre : un élève doit reconnaître la sienne au milieu d'une liste.")

    d.tableau('Lecture', "MÉTÉO — Montréal, cette semaine",
              ["Jour", "Temps et température"],
              [["Lundi", "Neige · moins 8 degrés"],
               ["Mardi", "Soleil · moins 2 degrés"],
               ["Mercredi", "Nuages · zéro degré"],
               ["Jeudi", "Pluie · plus 4 degrés"],
               ["Vendredi", "Vent et neige · moins 14 degrés"]],
              cle=1,
              notes="Diapositive à photographier. C'est le texte de l'intention du "
                    "programme : la faire lire en silence, puis poser les questions "
                    "de la diapositive suivante sans y revenir.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la grille de la semaine.", [
        ("Lundi, il neige.", "vrai"),
        ("Mardi, il fait moins huit.", "faux - moins deux"),
        ("Mercredi, il y a des nuages.", "vrai"),
        ("Jeudi, il pleut.", "vrai"),
        ("Le jour le plus froid, c'est vendredi.", "vrai - moins 14"),
        ("Il fait plus chaud lundi que jeudi.", "faux - jeudi, il fait plus 4"),
    ], corrige=True, cols=2,
       notes="Les deux derniers demandent de comparer deux nombres négatifs. Les faire "
             "au tableau, avec une ligne graduée dessinée à la main.")

    d.pratique('Pratique · deux villes', "Deux par deux, debout",
               "Quinze minutes. Un élève lit Montréal, l'autre lit Québec.", [
        ("Étape 1", "A demande : « Il fait combien à Québec ce matin ? »"),
        ("Étape 2", "B répond, A répète le nombre pour vérifier."),
        ("Étape 3", "On compare : « À Québec, il fait plus froid. »"),
        ("Étape 4", "On échange les rôles avec deux autres villes."),
    ], cols=1,
       notes="Ouvrir le vrai bulletin de deux villes sur le téléphone. La différence "
             "entre Montréal et Québec est réelle et souvent grande : elle frappe.")

    d.billet(
        "Écoutez le bulletin de demain matin et notez trois choses.",
        exemples=[
            "Ville : Montréal",
            "Temps : neige",
            "Température : moins 8",
        ],
        notes="Devoir court, mais le plus utile du module : c'est la tâche de "
              "l'intention du programme, faite pour de vrai. Ramasser les carnets au "
              "début de B2.")

    return d.save(dossier)
