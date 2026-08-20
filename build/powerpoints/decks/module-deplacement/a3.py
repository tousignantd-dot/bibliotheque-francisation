# -*- coding: utf-8 -*-
"""A3 · Les repères de la rue.
Bloc A « Je découvre » · couleur teal · 60 min.
Source : exercices `prImg` et `prRepere`, cartes mémoire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-deplacement/images/')


def build(dossier):
    d = Deck(
        code='A3', section='teal',
        titre='Les repères de la rue',
        chapeau="Huit photos, huit repères. Mettre le mot juste sur chacun, "
                "c'est comprendre un itinéraire sans avoir à le faire répéter "
                "trois fois.",
        duree='60 minutes')

    d.titre(notes="Séance visuelle. Elle installe le vocabulaire dont tout le reste du "
                  "module a besoin.")

    d.objectifs([
        "nommer huit repères de la rue et du transport ;",
        "comprendre ce que chaque indication demande de faire ;",
        "distinguer une indication qui dirige d'une qui décrit ;",
        "employer l'article juste : un coin, le feu, la direction.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que c'est ? À quoi ça sert dans un itinéraire ?",
        image=IMG + 'feu.jpg',
        pistes=[
            "Comment s'appelle cet objet, en un mot précis ?",
            "« Continuez jusqu'au feu » : où faut-il s'arrêter, exactement ?",
            "Combien de feux y a-t-il entre chez vous et l'école ?",
            "Y a-t-il un autre repère plus visible que celui-là dans votre quartier ?",
        ],
        notes="Attendre « feu de circulation ». Le mot « feu » seul suffit dans un "
              "itinéraire : « jusqu'au feu ».")

    d.cartes('Les quatre repères de la rue', "Le mot et ce qu'il désigne", [
        ("un coin de rue",
         "L'endroit où deux rues se croisent. Sert aussi de mesure : « marchez deux coins "
         "de rue » veut dire deux intersections."),
        ("un feu de circulation",
         "Le signal lumineux. Repère très fiable : il se voit de loin et ne bouge pas."),
        ("un trottoir",
         "La partie réservée aux piétons. « Restez sur le trottoir » est une consigne de "
         "sécurité autant qu'une direction."),
        ("en face de",
         "De l'autre côté de la rue, vis-à-vis. Se fusionne : en face du parc, en face des "
         "escaliers."),
    ], notes="Faire répéter chaque mot avec son article. « Un coin de rue », jamais "
             "« coin de rue ».")

    d.cartes('Les quatre repères du transport', "Le mot et ce qu'il désigne", [
        ("un arrêt d'autobus",
         "Le poteau ou l'abribus où l'autobus s'arrête. Le même numéro d'autobus a un "
         "arrêt de chaque côté de la rue — un par direction."),
        ("un quai",
         "L'endroit où on attend, dans une station ou un terminus. Chaque quai porte un "
         "numéro."),
        ("un panneau",
         "L'affiche suspendue qui indique la direction. C'est lui qu'il faut lire avant de "
         "descendre l'escalier."),
        ("un escalier",
         "Souvent le point de décision : au bout du corridor, en bas, à droite. Les "
         "itinéraires en intérieur en sont pleins."),
    ], notes="La première carte contient l'erreur la plus fréquente du module : le même "
             "numéro d'autobus dans les deux sens. Elle reviendra en B4.")

    d.tableau('Analyse', "Ce que l'indication demande",
              ['Ce qu\'on dit', 'Ce que je fais'],
              [["Continuez tout droit", "je ne tourne nulle part"],
               ["Jusqu'au feu", "je marche puis j'arrête au feu"],
               ["Deux coins de rue", "je traverse deux fois"],
               ["En face de la pharmacie", "je change de côté de rue"],
               ["Au bout du corridor", "je vais tout au fond"]],
              cle=2,
              notes="La troisième ligne est celle qui trompe le plus : « deux coins de rue » "
                    "n'est pas une distance en mètres.")

    d.regle("Diriger ou décrire",
            "Un bon itinéraire alterne : une direction, un repère, une direction, un repère.",
            precision="« Tournez à gauche » dirige. « Vous allez passer devant une "
                      "pharmacie » décrit — ça ne dit pas où aller, mais ça confirme qu'on "
                      "est sur le bon chemin. Les deux sont nécessaires : l'un trace, "
                      "l'autre rassure.",
            notes="Reprendre le dialogue de A1 et faire classer chaque phrase : dirige ou "
                  "décrit ? Les deux familles alternent presque parfaitement.")

    d.piege('Le côté de qui ?',
            "C'est à droite. — À votre droite ou à la mienne ?",
            "C'est du côté de la pharmacie.",
            "« À droite » dépend de la personne qui marche, pas de celle qui parle. Quand "
            "vous expliquez un chemin, un repère fixe — la pharmacie, les numéros pairs, "
            "le parc — ne se trompe jamais de côté.",
            notes="Faire l'expérience : deux élèves face à face, l'un explique « à droite ». "
                  "La confusion est immédiate et mémorable.")

    d.pratique('Pratique', "Le mot juste",
               "Complétez avec le mot du vocabulaire.", [
        ("Descendez au ___ de la rue, là où les deux rues se croisent.", "coin"),
        ("Continuez tout droit jusqu'au ___ de circulation.", "feu"),
        ("Restez sur le ___ jusqu'au parc.", "trottoir"),
        ("Attendez sur le ___, derrière la ligne jaune.", "quai"),
        ("Le nom du terminus est écrit sur le ___, au-dessus.", "panneau"),
        ("Descendez l'___ au bout du corridor.", "escalier"),
    ], corrige=True,
       notes="Ces six mots sont dans le banc de vocabulaire. Les élèves peuvent les réviser "
             "seuls avec les cartes mémoire.")

    d.billet(
        "Décrivez en quatre phrases le chemin entre l'arrêt d'autobus et la porte de l'école.",
        exemples=[
            "Employez au moins deux repères vus aujourd'hui.",
            "Alternez : une direction, un repère, une direction, un repère.",
        ],
        notes="Garder les billets : ils serviront de brouillon à la production orale de E1.")

    return d.save(dossier)
