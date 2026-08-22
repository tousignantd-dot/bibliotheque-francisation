# -*- coding: utf-8 -*-
"""C1 · Décrire quelqu'un assez bien pour qu'on le reconnaisse
Bloc C « Défi 2 · La personne à reconnaître » · couleur acier · 75 min.
Source : dialogue `t2` (trois pages de quatre répliques), exercice `t2vf` et
son bandeau de savoir, mots du Défi 2 de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Décrire quelqu'un assez bien pour qu'on le reconnaisse",
        chapeau="Décrire pour raconter et décrire pour retrouver, ce n'est "
                "pas le même métier. Dans un terminus, un beau sourire ne "
                "sert à rien.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 2. Commencer par un jeu : un élève décrit "
                  "quelqu'un de la classe, les autres devinent. On note au tableau les "
                  "détails qui ont permis de trouver — ce sont ceux qui se voient de "
                  "loin.")

    d.objectifs([
        "donner la silhouette avant le détail du visage ;",
        "nommer la forme d'un visage et le type de cheveux ;",
        "garder le signe particulier pour la fin ;",
        "employer les quatre mots du Défi 2 avec leur article.",
    ], notes="L'ordre est l'objectif principal. Une description juste mais désordonnée "
             "ne permet pas de trouver quelqu'un dans une salle d'attente.")

    d.declencheur(
        'Observation', "Comment décrirais-tu quelqu'un à un chauffeur de taxi ?",
        pistes=[
            "Par quoi commencerais-tu ?",
            "Qu'est-ce qui se voit de vingt pieds ?",
            "Qu'est-ce qui ne se voit pas du tout ?",
            "As-tu déjà attendu quelqu'un que tu n'avais jamais vu ?",
        ],
        notes="Beaucoup d'élèves ont vécu cette situation à leur arrivée au Québec. "
              "Les récits sont concrets et servent de matière pour toute la séance.")

    d.dialogue('Dialogue · 1 de 3', "Vous seriez libre vendredi ?", [
        ("MARISOL", "Ghislain, est-ce que vous seriez libre vendredi vers deux heures et demie ? Ousmane et sa sœur arrivent au terminus.", True),
        ("GHISLAIN", "Je peux y aller. Mais Ousmane, je l'ai vu deux fois il y a trois ans. Sa sœur, jamais.", True),
        ("MARISOL", "Ousmane, vous allez le reconnaître : il est très grand, mince, les épaules larges. Il a le crâne rasé maintenant.", True),
        ("GHISLAIN", "Bon. Grand, mince, crâne rasé. Et sa sœur ?", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire remarquer la reprise de Ghislain : il répète ce qu'il a compris. "
             "C'est la stratégie que les élèves devront employer en E1.")

    d.dialogue('Dialogue · 2 de 3', "Le visage et les cheveux", [
        ("MARISOL", "Elle est de taille moyenne, plutôt mince. Elle a le visage allongé, les pommettes hautes, et des cheveux ondulés attachés en arrière.", True),
        ("GHISLAIN", "Attachés comment ? En queue de cheval, en chignon ?", True),
        ("MARISOL", "En chignon bas, sur la nuque. Et elle a des lunettes rondes, à monture fine, dorée.", True),
        ("GHISLAIN", "Ça, c'est utile. Les lunettes, ça se voit de loin. Autre chose ?", True),
    ], notes="La question de Ghislain — attachés comment ? — est le modèle de la "
             "demande de précision. La faire répéter : c'est une compétence du niveau.")

    d.dialogue('Dialogue · 3 de 3', "Une grande valise, ou une grande femme ?", [
        ("GHISLAIN", "Une grande femme avec une grosse valise, ou une femme de taille moyenne avec une grosse valise ?", True),
        ("MARISOL", "Taille moyenne. Je me suis mal exprimée : quand j'ai dit une grande valise, je parlais de la valise, pas d'elle.", True),
        ("GHISLAIN", "C'est ce que je voulais vérifier. Et où est-ce que je me place ? Le terminus a deux portes.", True),
        ("MARISOL", "Près du banc où les gens attendent, celui qui est en face du guichet. C'est par là qu'ils vont sortir.", True),
    ], notes="Deux points d'un coup : l'ambiguïté d'un adjectif, corrigée par celle "
             "qui parle, et la relative avec où. Les deux reviennent en C3 et C4.")

    d.vocabulaire('Vocabulaire', "Les quatre mots du Défi 2", [
        ("une silhouette", "La forme générale d'une personne vue de loin : sa taille et sa carrure."),
        ("un visage allongé", "Un visage plus long que large, souvent avec un menton fin."),
        ("des cheveux ondulés", "Des cheveux qui font des vagues douces, ni raides ni frisés serré."),
        ("un signe particulier", "Un détail du corps qui n'appartient qu'à une personne."),
    ], notes="Faire décrire un visage rond, carré, ovale à côté d'allongé. Et faire "
             "distinguer raides, ondulés, frisés, crépus : quatre mots, quatre "
             "réalités.")

    d.tableau('Analyse', "Quatre temps, de loin vers près",
              ['Le temps', 'Ce qu\'on donne'],
              [["1. La silhouette", "taille, carrure, âge approximatif"],
               ["2. Les vêtements", "un foulard vert, une longue veste grise, une valise rouge"],
               ["3. Le visage", "visage allongé, cheveux ondulés, chignon bas, lunettes rondes"],
               ["4. Le signe", "une petite cicatrice au-dessus du sourcil gauche"]],
              cle=0,
              note="Le signe particulier vient en dernier : il sert à être sûr, pas à chercher.",
              notes="Diapositive à photographier. C'est le plan de la production orale "
                    "de E1 ; le dire dès maintenant.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation. Attention : Marisol se corrige une fois.", [
        ("Ghislain a déjà rencontré Ousmane deux fois.", "vrai"),
        ("Kadiatou est grande et costaude.", "faux - elle est de taille moyenne et mince"),
        ("Kadiatou porte ses cheveux en chignon bas.", "vrai"),
        ("Marisol conseille de chercher d'abord la cicatrice.", "faux - elle ne se voit pas de loin"),
        ("Kadiatou aura une valise rouge à roulettes.", "vrai"),
        ("Ghislain attendra près du banc qui fait face au guichet.", "vrai"),
    ], corrige=True,
       notes="Le deuxième énoncé vient de l'ambiguïté du dialogue. Faire retrouver la "
             "réplique où Marisol se corrige : c'est ce geste qu'on veut voir en E1.")

    d.billet(
        "Décris en deux phrases quelqu'un que le groupe pourrait reconnaître.",
        exemples=[
            "Commence par la silhouette.",
            "Ne dis pas son nom.",
        ],
        notes="Deux minutes, puis lecture de deux ou trois billets à voix haute : le "
              "groupe devine. On garde les autres pour C4.")

    return d.save(dossier)
