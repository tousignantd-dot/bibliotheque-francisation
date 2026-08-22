# -*- coding: utf-8 -*-
"""A1 · Une veille, ce n'est pas un avertissement
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
import os
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-saisons/images/')


def img(nom):
    """Le chemin d'une illustration, ou None si elle n'a pas encore été
    produite. Les séances se construisent sans les images et les reprennent
    d'elles-mêmes à la reconstruction, une fois `gen_images.py` passé."""
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Une veille, ce n'est pas un avertissement",
        chapeau="Marisol Quintero anime les sorties du Centre communautaire "
                "de la Pointe, à Rimouski : une par mois, une trentaine de "
                "personnes. Jeudi soir, une alerte apparaît sur son "
                "téléphone — et trente personnes attendent qu'elle décide.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir en montrant une vraie alerte "
                  "d'Environnement Canada sur un téléphone, sans rien expliquer, et "
                  "demander au groupe ce qu'elle veut dire. La réponse est presque "
                  "toujours « il va faire mauvais » — ce qui ne permet de décider de "
                  "rien. C'est exactement le point de départ du module.")

    d.objectifs([
        "distinguer une veille d'un avertissement, et savoir ce que chacun dit ;",
        "reconnaître le bulletin météorologique spécial, le plus faible des trois ;",
        "noter les trois choses qu'un avis donne toujours ;",
        "dire quand on répondra, quand on ne peut pas encore répondre.",
    ], notes="Le premier objectif est le plus rentable des quatre : il change la façon "
             "de lire une alerte pour le reste de la vie de l'élève. Le quatrième est "
             "celui que les gens oublient — annoncer le moment de sa réponse est déjà "
             "une réponse.")

    d.declencheur(
        'Observation', "Un trottoir couvert de glace. Qu'est-ce que vous "
                       "voulez savoir avant de sortir ?",
        image=img('verglas-trottoir.jpg'),
        pistes=[
            "Qu'est-ce qui est annoncé, exactement ?",
            "Pour quelle région ? Pour quel moment ?",
            "Est-ce que c'est certain, ou seulement possible ?",
            "Qu'est-ce que ça change à ce que vous aviez prévu ?",
        ],
        notes="Les quatre pistes sont l'ossature du module : le phénomène, la région, le "
              "moment, et la décision. Les écrire au tableau dans cet ordre et les y "
              "laisser toute la séance ; on y reviendra à chaque exercice.")

    d.dialogue('Dialogue · 1 de 3', "Une alerte sur le téléphone", [
        ("MARISOL", "Réjean, j'ai reçu une alerte. C'est écrit « veille de "
                    "tempête hivernale ». Est-ce que la sortie de samedi "
                    "tombe à l'eau ?", True),
        ("RÉJEAN", "Pas encore. Une veille, ça veut dire que les conditions "
                   "sont favorables. Le phénomène est possible, il n'est pas "
                   "certain.", True),
        ("MARISOL", "Alors quand est-ce qu'il devient certain ?", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire écouter deux fois avant d'afficher. À la deuxième écoute, demander "
             "seulement le mot qui pose problème : « veille ». Personne ne le connaît, "
             "et c'est normal — il ne s'apprend nulle part ailleurs qu'ici.")

    d.dialogue('Dialogue · 2 de 3', "Le mot qui change", [
        ("RÉJEAN", "Quand Environnement Canada change le mot. Une veille "
                   "devient un avertissement quand le phénomène est imminent "
                   "ou qu'il a déjà commencé.", True),
        ("MARISOL", "Deux mots pour la même chose, mais pas au même moment.", True),
        ("RÉJEAN", "C'est exactement ça. Avec une veille, on surveille. Avec "
                   "un avertissement, on décide.", False),
    ], notes="« Avec une veille, on surveille ; avec un avertissement, on décide » est la "
             "phrase à retenir de la séance. La faire répéter, l'écrire au tableau, y "
             "revenir en A4.")

    d.dialogue('Dialogue · 3 de 3', "Trente personnes attendent", [
        ("MARISOL", "Trente personnes attendent ma réponse. Je ne peux pas "
                    "leur dire « c'est possible ».", True),
        ("RÉJEAN", "Non. Mais tu peux leur dire quand tu vas répondre : "
                   "« Je vous confirme vendredi à midi. »", True),
        ("MARISOL", "Donc j'écoute le bulletin jusqu'à vendredi, et vendredi "
                    "je tranche.", False),
    ], notes="Cette réplique de Réjean est la solution pratique la plus utile du module. "
             "Demander au groupe qui a déjà eu à répondre « je ne sais pas encore » à "
             "quelqu'un — et comment ça s'est passé.")

    d.regle("Trois avis, trois degrés de certitude",
            "Bulletin spécial : quelque chose s'en vient. Veille : c'est "
            "possible. Avertissement : c'est imminent, ou c'est commencé.",
            precision="Le plus fort des trois est l'avertissement, pas le bulletin "
                      "« spécial » — le mot trompe presque tout le monde.",
            notes="Diapositive à photographier. Elle reviendra en A4 et en B4, et c'est "
                  "elle qu'il faut avoir en tête pendant le jeu de rôle de E1.")

    d.cartes("Trois avis", "Le vocabulaire de l'alerte", [
        ("Un bulletin météorologique spécial",
         "Un temps inhabituel s'en vient. On lit, on note, on attend."),
        ("Une veille",
         "Les conditions sont favorables. C'est possible, pas certain."),
        ("Un avertissement",
         "Le phénomène est imminent ou déjà commencé. On décide."),
        ("En vigueur · levé",
         "L'avis compte encore · l'avis a été retiré."),
    ], notes="Faire répéter avec l'article. « En vigueur » et « levé » ne sont pas "
             "décoratifs : c'est le second qui dit qu'on peut maintenir la sortie, et "
             "personne ne pense à l'attendre.")

    d.tableau('Deux avis', "Ce qu'on fait devant chacun",
              ['Une veille', 'Un avertissement'],
              [["C'est possible", "C'est imminent ou commencé"],
               ["Émise d'avance, parfois deux jours", "Émis quelques heures avant"],
               ["Peut être levée sans rien", "Le phénomène arrive presque toujours"],
               ["On surveille et on prépare", "On décide et on prévient"]],
              cle=1,
              notes="Faire compléter la colonne de droite par le groupe avant de "
                    "l'afficher. C'est la distinction la plus rentable de la séance, et "
                    "elle se joue en quatre lignes.")

    d.piege("Croire que « spécial » veut dire « grave »",
            "Un bulletin météorologique spécial : c'est le plus sérieux.",
            "Un bulletin spécial : c'est le plus faible des trois avis.",
            "Le mot « spécial » veut seulement dire que le temps sort de "
            "l'ordinaire. Le service ne sait pas encore de quoi il s'agit ni "
            "combien il en tombera.",
            notes="Ce piège fait annuler des activités pour rien. Il vient du mot "
                  "lui-même, pas d'une difficulté de langue : le signaler franchement.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Une veille veut dire que le phénomène est certain.", "faux — il est possible"),
        ("Un avertissement est émis quand c'est imminent ou commencé.", "vrai"),
        ("Le bulletin spécial est le plus fort des trois avis.", "faux — c'est le plus faible"),
        ("Marisol doit répondre à une trentaine de personnes.", "vrai"),
        ("Réjean conseille d'annoncer tout de suite quand on répondra.", "vrai"),
        ("La région annoncée n'a pas vraiment d'importance.", "faux — la moitié des annulations viennent de là"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue. La "
             "dernière prépare le travail de repérage de tout le bloc B.")

    d.billet(
        "Écrivez une activité que vous avez déjà dû reporter ou annuler à cause du temps.",
        exemples=[
            "Dites en une phrase ce qui était annoncé ce jour-là.",
            "Si ce n'est jamais arrivé, écrivez une activité qui pourrait l'être.",
        ],
        notes="Ramasser les billets : ils serviront en C2, où chacun doit dire s'il "
              "fallait maintenir, reporter ou annuler. Une situation vécue vaut mieux "
              "qu'un exemple inventé.")

    return d.save(dossier)
