# -*- coding: utf-8 -*-
"""D1 · La chronique de samedi
Bloc D « Défi 3 · L'opinion » · couleur acier · 75 min.
Source : dialogue `t3`, exercices `t3vf` et `t3fo`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n7-actualite/images/')


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="La chronique de samedi",
        chapeau="Une chronique n'est pas une nouvelle : c'est quelqu'un qui "
                "pense tout haut et qui signe. Le piège, c'est qu'elle "
                "contient aussi des faits parfaitement exacts.",
        duree='75 minutes')

    d.titre(notes="Ouverture du Défi 3. Le bloc ne compte que deux séances : celle-ci "
                  "pour lire et trier, D2 pour répondre. Le dire d'emblée, le rythme "
                  "est serré.")

    d.objectifs([
        "reconnaître une chronique et ce qui la distingue d'un article ;",
        "trier les faits et les jugements à l'intérieur d'un même texte ;",
        "repérer un mot choisi pour juger sans en avoir l'air ;",
        "identifier le point sur lequel on est d'accord avec l'auteur.",
    ], notes="Le quatrième objectif prépare D2 : on ne peut pas concéder si on n'a pas "
             "d'abord trouvé quoi concéder.")

    d.declencheur(
        'Observation', "« Ce projet a été imposé au quartier. »",
        image=IMG + 'salle-conseil.jpg',
        pistes=[
            "Est-ce que c'est un fait ou un jugement ?",
            "Quel mot neutre pourrait remplacer « imposé » ?",
            "Le conseil a-t-il déjà voté ?",
            "Qu'est-ce que la conseillère avait dit à ce sujet ?",
        ],
        notes="Le groupe a vu en C1 que « recommandé n'est pas décidé ». La phrase de "
              "la chroniqueuse contredit donc un fait établi la séance précédente. "
              "Laisser le groupe le trouver.")

    d.dialogue('Dialogue · 1 de 3', "Le début et la fin ne vont pas ensemble", [
        ("FARIDA", "Suzie, j'ai lu la chronique de Thérèse Vaillancourt. Je l'ai lue trois fois et je ne sais pas si je suis d'accord.", True),
        ("FARIDA", "Elle écrit : « Bien que le projet parte d'une bonne intention, la Ville a encore une fois décidé sans nous. » Le début et la fin ne vont pas ensemble.", True),
        ("SUZIE", "Au contraire, c'est très bien construit. Elle accorde quelque chose avant de frapper. Ensuite elle attaque la façon de faire, pas l'idée.", True),
        ("FARIDA", "Pourquoi ne pas attaquer directement ?", True),
        ("SUZIE", "Parce que si tu attaques directement, celui qui n'est pas d'accord arrête de lire à la deuxième ligne. Tandis que si tu commences par lui donner raison sur un point, il continue.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="La dernière réplique est la justification de tout le Défi 3. L'écrire au "
             "tableau : elle sera la consigne d'écriture de E2.")

    d.dialogue('Dialogue · 2 de 3', "Une phrase qui a l'air d'un fait", [
        ("FARIDA", "Mais elle écrit aussi : « Ce projet a été imposé au quartier. » Ça, c'est faux. La conseillère a dit en entrevue que le conseil déciderait le 14 octobre, en séance publique.", True),
        ("SUZIE", "Ah. Là, tu viens de faire exactement ce qu'il faut faire. Tu as trouvé une phrase qui a l'air d'un fait et qui n'en est pas un.", True),
        ("FARIDA", "« Imposé », c'est un jugement.", True),
        ("SUZIE", "C'est un jugement. Et le mot est choisi. Elle aurait pu écrire « recommandé par le comité exécutif », ce qui est vrai et plate. Elle a écrit « imposé », ce qui est discutable et efficace.", True),
    ], notes="« Vrai et plate » contre « discutable et efficace » : la formule résume "
             "l'économie d'une chronique. Elle mérite d'être commentée.")

    d.dialogue('Dialogue · 3 de 3', "Le point où elle a raison", [
        ("FARIDA", "Dans le même paragraphe, elle donne des chiffres exacts. Cent quarante mètres carrés, deux places, quinze minutes. Tout ça est juste, j'ai vérifié.", True),
        ("SUZIE", "Bien sûr. Une bonne chroniqueuse ne se trompe pas sur les faits ; c'est ce qui lui donne le droit d'être dure sur le reste.", True),
        ("FARIDA", "Même si je trouve son ton un peu fort, il y a une chose sur laquelle elle a raison. Les heures d'ouverture. Personne ne les connaît, et pour moi c'est la vraie question.", True),
        ("SUZIE", "Ça, personne ne l'a demandé. Ni Ludovic, ni Thérèse, ni les commerçants. Alors écris-le.", True),
    ], notes="C'est ici que le module bascule : l'élève passe de lecteur à auteur. "
             "Farida a trouvé la question que personne n'a posée, et c'est ce qu'on "
             "demandera à chacun en E2.")

    d.regle("Les faits exacts servent le jugement",
            "Une chronique juste sur les faits a plus de force dans ses opinions.",
            precision="Le mélange est volontaire, et il n'est pas malhonnête : la "
                      "chroniqueuse annonce qu'elle donne un avis. Mais le lecteur "
                      "pressé voit un seul bloc, et prend le jugement pour de "
                      "l'information parce qu'il est entouré de chiffres vrais.",
            notes="Diapositive à photographier. C'est la conclusion du module tout "
                  "entier sur la lecture.")

    d.pratique('Tri', "Dans la chronique : fait ou jugement ?",
               "Les faits y sont exacts. Les jugements, eux, se discutent.", [
        ("« Le local fait cent quarante mètres carrés. »", "fait"),
        ("« Ce projet a été imposé au quartier. »", "jugement - « imposé » apprécie"),
        ("« Deux places seront réservées, quinze minutes. »", "fait"),
        ("« Quinze minutes : voilà bien une idée de bureau. »", "jugement"),
        ("« Personne ne connaît encore les heures d'ouverture. »", "fait"),
        ("« La Ville a encore une fois décidé sans nous. »", "jugement - « encore une fois » juge"),
        ("« Le conseil doit se prononcer le 14 octobre. »", "fait"),
        ("« Il serait temps qu'on écoute enfin les commerçants. »", "jugement"),
    ], corrige=True,
       notes="Boucle bouclée avec A4 : même exercice, texte plus difficile. Comparer "
             "les résultats avec ceux du bloc A si vous les avez gardés.")

    d.billet(
        "Sur quel point êtes-vous d'accord avec la chroniqueuse ?",
        exemples=[
            "Un seul point, même petit.",
            "Puis : sur quel point n'êtes-vous pas d'accord ?",
        ],
        notes="Deux minutes. Ces deux lignes sont la matière première de D2 et de E2 : "
             "les faire garder.")

    return d.save(dossier)
