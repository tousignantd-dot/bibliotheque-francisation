# -*- coding: utf-8 -*-
"""B1 · Quelle taille ?
Bloc B « Défi 1 · Demander ce qu'on cherche » · couleur acier · 75 min.
Source : dialogue `t1`, exercice `t1vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-vetements/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre='Quelle taille ?',
        chapeau="Le chiffre qu'on connaissait dans son pays ne se traduit "
                "pas. Ici, trois lettres suffisent — P, M, G — et une "
                "quatrième chose : essayer.",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 1. Demander qui connaît sa taille ici, et qui "
                  "achète encore « au jugé ». Les deux réponses sont fréquentes.")

    d.objectifs([
        "comprendre la question « vous portez quelle taille ? » ;",
        "répondre P, M ou G, ou dire qu'on ne sait pas ;",
        "demander où se trouve la cabine d'essayage ;",
        "dire ce qui ne va pas : trop serré, trop long.",
    ])

    d.declencheur(
        'Observation', "Que dit cette étiquette ?",
        image=IMG + 'etiquette-taille.jpg',
        pistes=[
            "Où se trouve-t-elle sur le vêtement ?",
            "Qu'est-ce qui est écrit dessus, d'habitude ?",
            "Connaissez-vous votre taille ici ?",
            "Et dans votre pays d'origine ?",
        ],
        notes="Faire circuler un vêtement réel si possible : l'étiquette de taille est "
              "cousue dans le col, celle d'entretien juste en dessous ou sur le côté.")

    d.dialogue('Dialogue · 1 de 3', "Je ne sais pas", [
        ("JOCELYNE", "Vous portez quelle taille ?", True),
        ("FARIDA", "Je ne sais pas. Dans mon pays, c'est un autre système.", True),
        ("JOCELYNE", "Ici, c'est petit, moyen ou grand. Sur l'étiquette : P, M ou G.", True),
        ("FARIDA", "Je pense que je suis moyenne.", False),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Farida dit franchement qu'elle ne sait pas. C'est la bonne réponse, et elle "
             "n'embarrasse personne.")

    d.dialogue('Dialogue · 2 de 3', "La cabine", [
        ("JOCELYNE", "Voici un moyen bleu foncé. Vous voulez l'essayer ?", True),
        ("FARIDA", "Oui, s'il vous plaît. Où est la cabine ?", True),
        ("JOCELYNE", "Au fond, à droite, derrière les chandails.", True),
    ], notes="Trois repères dans la réponse : au fond, à droite, derrière les chandails. "
             "Faire relever les trois.")

    d.dialogue('Dialogue · 3 de 3', "Ce qui ne va pas", [
        ("FARIDA", "Madame ? Le moyen est trop serré aux épaules.", True),
        ("JOCELYNE", "Trop serré ? Alors essayez le grand. Je le décroche du cintre.", True),
        ("FARIDA", "Le grand est parfait. Mais les manches sont un peu longues.", True),
        ("JOCELYNE", "Un peu longues, ce n'est pas grave l'hiver.", True),
    ], notes="Farida nomme l'endroit : « aux épaules ». C'est ce qui permet à la "
             "conseillère de choisir quoi rapporter.")

    d.tableau('Analyse', "Quatre phrases, quatre moments",
              ['Le moment', 'Ce qu\'on dit'],
              [["On vous demande votre taille", "« Du moyen » ou « je ne sais pas »"],
               ["On vous propose un vêtement", "« Je peux l'essayer ? »"],
               ["Vous cherchez la cabine", "« Où est la cabine d'essayage ? »"],
               ["Le vêtement ne fait pas", "« C'est trop serré aux épaules. »"]],
              cle=0,
              note="Quatre phrases suffisent pour tout l'essayage.",
              notes="Diapo à photographier. C'est le script complet du défi 1.")

    d.regle("Nommer l'endroit, pas seulement le problème",
            "« C'est trop serré <b>aux épaules</b>. »",
            precision="« Serré » tout seul ne dit pas s'il faut une taille au-dessus ou un "
                      "autre modèle. Serré aux épaules et bien ailleurs : c'est la coupe. "
                      "Serré partout : c'est la taille. La conseillère décide à partir de "
                      "l'endroit que vous nommez.",
            notes="Diapo à photographier. Faire nommer les parties du corps utiles : les "
                  "épaules, la taille, les manches, les jambes.")

    d.piege("Acheter sans essayer",
            "Ça devrait faire.",
            "Je peux l'essayer ?",
            "Un manteau d'hiver se porte par-dessus un chandail : essayé en t-shirt, il "
            "paraîtra parfait et sera trop serré en janvier. Essayer avec ce qu'on porte "
            "l'hiver est la seule vérification qui vaille.",
            notes="Conseil très concret. Beaucoup d'élèves achètent un manteau en octobre, "
                  "en chandail léger, et ne peuvent plus le fermer en décembre.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Ici, les tailles sont petit, moyen et grand.", "vrai"),
        ("Farida connaît sa taille dès le début.", "faux — elle ne la connaît pas"),
        ("La cabine d'essayage est au fond, à droite.", "vrai"),
        ("Le manteau moyen est trop grand.", "faux — trop serré"),
        ("Le moyen est trop serré aux épaules.", "vrai"),
        ("Farida prend le grand.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.billet(
        "Écrivez les quatre phrases de l'essayage, de mémoire.",
        exemples=[
            "Celles du tableau : la taille, l'essai, la cabine, le problème.",
            "Puis dites-les à voix haute, sans regarder.",
        ],
        notes="Devoir de mémorisation. Ces quatre phrases sont réutilisées telles quelles "
              "au jeu de rôle de E1.")

    return d.save(dossier)
