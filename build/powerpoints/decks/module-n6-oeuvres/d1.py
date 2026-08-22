# -*- coding: utf-8 -*-
"""D1 · Ce que la critique dit vraiment
Bloc D « Défi 3 · La critique et le résumé » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf`, `t3texte` et `t3adj`, et leurs
mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Ce que la critique dit vraiment",
        chapeau="Charbonneau n'a pas écrit que la voisine est inutile : il a "
                "écrit qu'elle arrive trop tard. Ce n'est pas la même chose, "
                "et c'est beaucoup plus difficile à contredire.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 3. Distribuer la critique imprimée et la "
                  "faire lire en silence avant tout commentaire. Demander ensuite, à "
                  "main levée, qui est d'accord : la moitié du groupe l'est.")

    d.objectifs([
        "repérer dans une critique le reproche exact, et non sa version grossie ;",
        "reconnaître les guillemets qui mettent un mot à distance ;",
        "distinguer un reproche vérifiable d'une impression ;",
        "savoir qu'un grand film et un film grand ne disent pas la même chose.",
    ], notes="Le premier objectif est le geste de la séance. Les trois autres sont les "
             "outils qui le rendent possible.")

    d.declencheur(
        'Observation', "Qu'est-ce qu'il reproche exactement au film ?",
        pistes=[
            "Écris sa critique en une phrase, de mémoire.",
            "Retourne au texte et retrouve la phrase exacte.",
            "Est-ce que ta phrase était plus dure que la sienne ?",
            "Sur quoi porte chacun de ses trois reproches ?",
        ],
        notes="Faire écrire de mémoire d'abord. L'écart entre la version retenue et le "
              "texte exact est presque toujours dans le même sens : plus dur. C'est la "
              "démonstration de la séance.")

    d.dialogue('Dialogue · 1 de 3', "Trois reproches", [
        ("BRUNO", "Tiens, la critique a paru ce matin dans L'Écho de la Magog. Léo Charbonneau. Il n'a pas aimé.", True),
        ("THÉRÈSE", "Il a le droit. Qu'est-ce qu'il reproche ?", True),
        ("BRUNO", "Trois choses. Que le film soit trop lent dans sa première demi-heure. Que les retours en arrière soient mal annoncés. Et que le personnage de la voisine ne serve à rien.", True),
        ("THÉRÈSE", "La voisine ? C'est elle qui donne la lettre. Sans elle, il n'y a pas de film.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Bruno lui-même résume la critique de façon un peu trop dure. Le faire "
             "remarquer : même quelqu'un d'expérimenté grossit en résumant.")

    d.dialogue('Dialogue · 2 de 3', "Ce qu'il dit, et ce qu'on croit", [
        ("BRUNO", "Mais attention : il ne dit pas qu'elle est inutile, il dit qu'elle arrive trop tard. Ce n'est pas la même chose, et c'est plus difficile à contredire.", True),
        ("THÉRÈSE", "Alors je dois lire ce qu'il dit vraiment, pas ce que je crois qu'il dit.", True),
        ("BRUNO", "Toujours. Et regarde comment il écrit son avis. Il écrit : « un film qu'on dit ambitieux, faute de savoir quoi en dire ».", True),
        ("THÉRÈSE", "Les guillemets autour d'ambitieux, ils veulent dire qu'il n'y croit pas.", True),
    ], notes="La phrase de Thérèse est l'objectif 2 atteint. La faire répéter, puis "
             "chercher deux autres exemples de guillemets dans la critique.")

    d.dialogue('Dialogue · 3 de 3', "Accorder un point", [
        ("THÉRÈSE", "Moi, je ne suis pas d'accord avec lui, mais pas complètement non plus.", True),
        ("BRUNO", "Voilà la phrase que j'attendais depuis le début de l'année. Continue.", True),
        ("THÉRÈSE", "La première demi-heure est lente, c'est vrai. J'ai regardé l'heure deux fois. Mais je pense que c'est voulu : trois jours pour vider une maison, ça ne peut pas être rapide.", True),
        ("BRUNO", "Tu viens de faire quelque chose que peu de gens font : tu lui accordes un point avant de lui répondre. Ça donne du poids à ce qui suit.", True),
    ], notes="C'est la charnière du module. La quatrième réplique annonce D2, où le "
             "geste devient une leçon. Ne pas l'expliquer ici, seulement la nommer.")

    d.tableau('Analyse', "Ce qu'il écrit, ce qu'on croit qu'il écrit",
              ['La version rapide', 'Le texte exact'],
              [["c'est un mauvais film", "un film qu'on dit « ambitieux »"],
               ["le début est ennuyant", "avance à la vitesse d'un déménagement"],
               ["c'est une maladresse", "ce n'est pas une maladresse : c'est un parti pris"],
               ["la voisine est inutile", "le personnage de la voisine arrive trop tard"],
               ["il a détesté", "un beau film qui a manqué d'être un grand film"]],
              cle=0,
              note="Cinq fois, la version retenue est plus dure que le texte.",
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "Défi 3 : il revient en D2 et sert de contrôle avant d'écrire "
                    "en E2.")

    d.regle("Trois façons de dire du mal sans le dire",
            "Les guillemets, la comparaison, le compliment retourné.",
            precision="Un critique expérimenté évite les mots durs : ils sont trop "
                      "faciles à réfuter. Il met « ambitieux » entre guillemets, il "
                      "compare le rythme à un déménagement, et il termine par « un "
                      "beau film qui a manqué d'être un grand film ». Aucune de ces "
                      "phrases ne se renvoie telle quelle.",
            notes="Diapositive à photographier. Faire chercher les trois procédés dans "
                  "la critique, surlignés de trois couleurs.")

    d.regle("Un grand film, un film grand",
            "Avant le nom, l'adjectif juge ; après le nom, il décrit ce qui se mesure.",
            precision="Un grand film est important ; un homme grand se mesure en "
                      "centimètres. Une ancienne salle n'en est plus une ; une salle "
                      "ancienne est vieille. Un drôle de personnage est étrange ; un "
                      "personnage drôle fait rire. Cinq adjectifs seulement : grand, "
                      "ancien, drôle, propre, nouveau.",
            notes="Diapositive à photographier. « Sa propre règle », qu'on emploie "
                  "depuis B2, en est un exemple : ça ne veut pas dire que la règle "
                  "est bien nettoyée.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la critique et la discussion.", [
        ("Charbonneau reproche au film trois choses.", "vrai"),
        ("Il écrit que le personnage de la voisine est inutile.", "faux - qu'il arrive trop tard"),
        ("Il met « ambitieux » entre guillemets parce qu'il trouve le mot juste.", "faux - il ne le reprend pas à son compte"),
        ("Thérèse accorde que la première demi-heure est lente.", "vrai"),
        ("Selon Thérèse, cette lenteur est une maladresse.", "faux - un parti pris"),
        ("L'Écho de la Magog publie des réponses de lecteurs.", "vrai"),
    ], corrige=True,
       notes="Faire retrouver la phrase exacte pour les trois « faux ». C'est le même "
             "geste que le tableau d'analyse, appliqué une seconde fois.")

    d.billet(
        "Recopie le reproche de Charbonneau que tu trouves le plus juste.",
        exemples=[
            "Recopie-le exactement, sans le reformuler.",
            "Ajoute un mot pour dire pourquoi.",
        ],
        notes="Trois minutes. Exiger la citation exacte : les billets reformulés sont "
              "eux-mêmes la preuve du problème, et c'est un excellent départ pour D2.")

    return d.save(dossier)
