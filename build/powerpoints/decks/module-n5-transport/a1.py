# -*- coding: utf-8 -*-
"""A1 · « Trois mots sur dix »
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-transport/images/')


def img(nom):
    """Le chemin d'une illustration, ou None si elle n'a pas encore été
    produite. Les images de ce module viennent de fal.ai, dont le compte
    était verrouillé le jour de la production : les séances se construisent
    sans elles et les reprennent d'elles-mêmes à la reconstruction."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="« Trois mots sur dix »",
        chapeau="Tereza Nogueira part de Longueuil tous les matins à six "
                "heures cinquante et traverse l'île pour se rendre à son "
                "atelier de Saint-Laurent. La radio est ouverte, la chronique "
                "de circulation commence — et depuis quatre ans, elle n'en "
                "comprend que trois mots sur dix.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir en faisant écouter un vrai bulletin "
                  "de circulation de trente secondes, sans rien expliquer, puis demander "
                  "au groupe ce qui a été compris. La réponse est presque toujours : le "
                  "nom d'une route, et rien d'autre. C'est exactement le point de départ. "
                  "Ne pas dédramatiser trop vite : c'est réellement difficile, et c'est "
                  "pour cela que le module existe.")

    d.objectifs([
        "nommer l'état d'une route avec les mots du bulletin ;",
        "savoir quelles quatre informations un bulletin donne toujours ;",
        "distinguer un ralentissement, un bouchon et une route fermée ;",
        "comprendre ce qu'est une entrave, et ce qu'est un accotement.",
    ], notes="Le deuxième objectif est le plus important des quatre : savoir qu'il y a "
             "quatre informations, et lesquelles, transforme une écoute au hasard en une "
             "écoute qui attend quelque chose. Tout le bloc A tient là-dessus.")

    d.declencheur(
        'Observation', "Une file d'autos arrêtées, un matin. Qu'est-ce que "
                       "vous voulez savoir en premier ?",
        image=img('autoroute-bouchon.jpg'),
        pistes=[
            "Qu'est-ce qui bloque, à votre avis ?",
            "Où faudrait-il le savoir, exactement ?",
            "Depuis quand est-ce que ça dure ?",
            "Combien de temps encore ? Qui peut vous le dire ?",
        ],
        notes="Les quatre pistes sont les quatre informations du bulletin, posées avant "
              "d'être nommées. Les écrire au tableau dans cet ordre et les y laisser "
              "toute la séance : on y reviendra à chaque exercice du module.")

    d.dialogue('Dialogue · 1 de 3', "Il a dit quoi, exactement ?", [
        ("TEREZA", "Amine, arrête deux secondes. Il vient de dire quelque "
                   "chose sur la 40.", True),
        ("AMINE", "Il parle vite, hein ? Moi non plus, les premières années, "
                  "je ne comprenais rien.", True),
        ("TEREZA", "J'ai entendu « ralentissement », j'ai entendu "
                   "« accotement », et après, plus rien.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la réplique d'Amine : lui non plus ne comprenait rien les "
             "premières années. C'est une information utile pour le groupe, et elle est "
             "vraie de tout le monde, y compris des gens nés ici quand ils déménagent "
             "dans une autre ville.")

    d.dialogue('Dialogue · 2 de 3', "Ça avance, ou ça n'avance plus", [
        ("AMINE", "Un ralentissement, c'est quand ça avance, mais lentement. "
                  "Ce n'est pas arrêté.", True),
        ("TEREZA", "Et quand c'est arrêté ?", True),
        ("AMINE", "Là, c'est un bouchon. Ou un embouteillage, si tu veux le "
                  "mot poli.", True),
    ], notes="La distinction ralentissement / bouchon est le cœur de la séance. Elle "
             "n'est pas décorative : elle décide si l'on part quand même ou si l'on "
             "change de chemin. Faire donner des exemples vécus par le groupe.")

    d.dialogue('Dialogue · 3 de 3', "L'accotement, et l'entrave", [
        ("AMINE", "L'accotement, c'est la bande sur le bord de la route, en "
                  "dehors des voies. On s'arrête là quand on tombe en panne.", True),
        ("TEREZA", "Et une entrave, c'est quoi ? Il dit ça tout le temps.", True),
        ("AMINE", "Tout ce qui empêche de passer normalement : des travaux, "
                  "un accident, une voie fermée. C'est le mot général.", False),
    ], notes="« Entrave » est le mot le plus fréquent du bulletin et le plus opaque pour "
             "un élève. Le faire répéter, et faire trouver au groupe trois choses qui "
             "sont des entraves. La formule « aucune entrave à signaler » s'apprend d'un "
             "bloc, comme une expression figée.")

    d.regle("Un bulletin dit toujours les mêmes quatre choses",
            "Ce qui bloque, où, depuis quand, et pour combien de temps "
            "encore. Toujours dans cet ordre.",
            precision="Quand on sait qu'il y en a quatre, on cesse d'écouter des "
                      "mots au hasard : on attend les quatre, l'une après l'autre.",
            notes="Diapositive à photographier. Elle reviendra à chaque séance du module, "
                  "et c'est elle qu'il faut avoir en tête pendant le jeu de rôle de E1.")

    d.cartes("Quatre états", "Le vocabulaire de la route", [
        ("Un ralentissement",
         "Ça avance, mais lentement. On part quand même."),
        ("Un bouchon",
         "Ça ne bouge presque plus. On cherche un autre chemin."),
        ("Une entrave",
         "Tout ce qui empêche de circuler normalement."),
        ("L'accotement",
         "La bande sur le bord, en dehors des voies."),
    ], notes="Faire répéter avec l'article. Insister sur « accotement » : c'est un mot "
             "qu'on n'apprend nulle part ailleurs et qui revient tous les matins. "
             "Demander qui a déjà eu besoin de s'arrêter sur l'accotement.")

    d.tableau('Deux états', "Ça avance, ou ça n'avance plus",
              ['Un ralentissement', 'Un bouchon'],
              [["Ça roule au ralenti", "Ça ne bouge presque plus"],
               ["Trente à l'heure", "Dix mètres à la minute"],
               ["Vingt minutes de plus", "Personne ne sait"],
               ["On y va quand même", "On change de chemin"]],
              cle=1,
              notes="Faire compléter la colonne de droite par le groupe avant de "
                    "l'afficher. C'est la distinction la plus rentable de la séance.")

    d.piege("Croire qu'il faut tout comprendre du premier coup",
            "Je n'ai rien compris, ça ne sert à rien d'écouter.",
            "J'attrape le nom de ma route, et j'écoute le bulletin suivant.",
            "Le bulletin repasse toutes les dix minutes, avec la même voix et les "
            "mêmes routes. Personne ne le comprend en entier du premier matin, "
            "même les gens d'ici.",
            notes="Ce piège décourage plus d'élèves que n'importe quelle difficulté de "
                  "grammaire. Le dire clairement : la répétition du bulletin est un "
                  "cadeau, pas une contrainte.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Tereza fait la route avec Amine depuis deux ans.", "vrai"),
        ("Amine a tout de suite compris les bulletins.", "faux — lui non plus, les premières années"),
        ("Un ralentissement veut dire que les autos sont arrêtées.", "faux — ça avance, mais lentement"),
        ("On peut s'arrêter sur l'accotement en cas de panne.", "vrai"),
        ("Le mot « entrave » couvre les travaux et les accidents.", "vrai"),
        ("Le bulletin change de voix et de routes chaque jour.", "faux — c'est ce qui le rend apprenable"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. La dernière prépare "
             "le travail d'écoute de tout le bloc C.")

    d.billet(
        "Écrivez le nom de la route, du pont ou de la ligne d'autobus que vous prenez le matin.",
        exemples=[
            "Ajoutez dans quel sens vous allez : vers le nord, vers le centre-ville.",
            "Si vous ne prenez pas la route, écrivez le trajet de quelqu'un que vous connaissez.",
        ],
        notes="Ramasser les billets : ils serviront en C4, où chacun doit dire si une "
              "entrave le concerne. Un trajet réel vaut mieux qu'un exemple inventé.")

    return d.save(dossier)
