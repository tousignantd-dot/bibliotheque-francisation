# -*- coding: utf-8 -*-
"""B1 · Écoutez, regardez.
Bloc B « Défi 1 · La consigne » · couleur acier · 75 min.
Source du module : dialogue `t1`, exercices `t1vf`, `t1imper` et `t1geste`,
mini-leçon `t1imper`.

C'est la première des deux intentions du programme pour cette situation au
niveau 1 : comprendre une consigne. Toute la séance se fait debout autant
qu'assis — une consigne comprise se voit à un geste, pas à une réponse.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n1-classe/images/')


def photo(nom):
    """Le chemin de l'image, ou rien si elle n'est pas encore produite."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Écoutez, regardez',
        chapeau="Une consigne de classe fait deux mots et commence par un "
                "verbe. Le premier mot est le plus important.",
        duree='75 minutes')

    d.titre(notes="Ouvrir la séance sans un mot d'explication : donner trois consignes "
                  "en les mimant, et laisser le groupe suivre. Expliquer après.")

    d.objectifs([
        "comprendre quatre consignes de classe ;",
        "faire le geste demandé ;",
        "reconnaître le verbe au début de la phrase ;",
        "dire « Pardon ? » quand on n'a pas compris.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que l'enseignante demande ?",
        image=photo('tableau-blanc.jpg'),
        pistes=[
            "Elle montre le tableau. Que faut-il faire ?",
            "Elle montre le livre. Que faut-il faire ?",
            "Combien de mots dit-elle ?",
            "Faut-il répondre, ou faire quelque chose ?",
        ],
        notes="La dernière piste est la clé du défi : une consigne demande un geste, pas "
              "une phrase. Y revenir à la fin de la séance.")

    d.dialogue('Dialogue · 1 de 2', "La consigne", [
        ("MADAME CYR", "Écoutez bien. Ouvrez le livre.", True),
        ("BOPHA", "Pardon ?", True),
        ("MADAME CYR", "Ou-vrez le livre. Comme ça.", True),
        ("BOPHA", "Ah ! Oui.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Madame Cyr redit les mêmes mots, plus lentement. Elle ne reformule pas : "
             "c'est ce qui aide un débutant, et c'est le contraire de l'intuition.")

    d.dialogue('Dialogue · 2 de 2', "Je ne comprends pas", [
        ("MADAME CYR", "Bien. Maintenant, regardez le tableau.", True),
        ("IVAN", "Madame, je ne comprends pas.", True),
        ("MADAME CYR", "Regardez. Le tableau, devant.", True),
        ("IVAN", "Ah, le tableau. Merci.", True),
    ], notes="Faire remarquer qu'Ivan est arrivé trois semaines plus tôt et qu'il ne "
             "comprend pas non plus. Cela vaut mieux qu'un discours d'encouragement.")

    d.regle("Le premier mot",
            "Une consigne commence par le verbe.",
            precision="« <b>Ouvrez</b> le livre. » « <b>Regardez</b> le tableau. » Ni "
                      "« je », ni « vous » : le verbe tout de suite. Dès que vous l'avez "
                      "entendu, vous savez quoi faire.",
            notes="Diapositive à photographier. Le dire, puis donner cinq consignes de "
                  "suite pour le vérifier tout de suite.")

    d.tableau('Analyse', "Les quatre verbes du matin",
              ['Le verbe', 'Ce que je fais'],
              [["Écoutez", "les oreilles, sans parler"],
               ["Regardez", "les yeux vers le devant"],
               ["Ouvrez", "le livre, le sac, la porte"],
               ["Fermez", "le contraire d'ouvrir"]],
              cle=2,
              note="Toutes finissent par le son « é ». C'est lui qui dit : à vous de le "
                   "faire.",
              notes="Diapositive à photographier. Trois des quatre se font avec une "
                    "partie du corps : les oreilles, les yeux, les mains.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après les deux dialogues.", [
        ("Madame Cyr dit d'ouvrir le livre.", "vrai"),
        ("Bopha comprend tout de suite.", "faux — elle dit « Pardon ? »"),
        ("Madame Cyr répète plus lentement.", "vrai"),
        ("Ivan dit qu'il ne comprend pas.", "vrai"),
    ], corrige=True, cols=1,
       notes="Reprendre l'énoncé 3 : elle répète avec les mêmes mots, pas d'autres.")

    d.pratique('Pratique · debout', "Le jeu des consignes",
               "Tout le groupe debout. L'enseignante donne, le groupe fait.", [
        ("Tour 1", "Écoutez. Regardez le tableau. Ouvrez le livre. Fermez le livre."),
        ("Tour 2", "Plus vite, dans le désordre."),
        ("Tour 3", "Un élève donne les consignes à sa place."),
        ("Tour 4", "Sans montrer : seulement la voix."),
    ], cols=1,
       notes="Vingt minutes, et c'est la partie la plus utile de la séance. Au tour 4, "
             "le geste ne peut plus être copié sur le voisin.")

    d.billet(
        "Écrivez les quatre verbes de consigne.",
        exemples=[
            "Écoutez, regardez, ouvrez, fermez.",
            "À côté de chacun, dessinez ou écrivez ce que vous faites.",
        ],
        notes="Le dessin est accepté et même souhaité : plusieurs écrivent difficilement "
              "et comprennent parfaitement.")

    return d.save(dossier)
