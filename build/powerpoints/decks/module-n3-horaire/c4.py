# -*- coding: utf-8 -*-
"""C4 · Permission ou aide ?
Bloc C « Défi 2 · Est-ce que je peux vous demander ? » · couleur acier · 60 min.
Source : exercice `t2ecoute`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='acier',
        titre="Permission ou aide ?",
        chapeau="À l'oreille, les deux demandes se ressemblent : elles "
                "commencent toutes les deux par « est-ce que ». Ce qui les "
                "sépare tient en un mot — qui va faire la chose.",
        duree='60 minutes')

    d.titre(notes="Séance d'écoute, dernière du défi 2. Elle se joue sur un seul indice, "
                  "et il vaut la peine de laisser le groupe le trouver avant de le "
                  "nommer.")

    d.objectifs([
        "distinguer à l'oreille une permission d'une demande d'aide ;",
        "repérer qui fera la chose demandée ;",
        "répondre correctement à chacune ;",
        "employer les deux formes dans une même conversation.",
    ])

    d.regle("Qui va faire la chose ?",
            "Je peux… = moi. Vous pouvez… = vous.",
            precision="Une permission demande le droit de faire quelque "
                      "chose soi-même. Une demande d'aide demande à l'autre "
                      "de le faire. Le verbe est le même — « pouvoir » — "
                      "mais le sujet change, et c'est tout.",
            notes="Diapo à photographier. Poser la question « qui va le faire ? » après "
                  "chaque phrase entendue : c'est le seul raisonnement à installer, et il "
                  "marche à tous les coups.")

    d.pratique('Écoute', "Permission, ou aide ?",
               "Écoutez la phrase et dites ce qu'elle demande.", [
        ("Est-ce que je peux prendre ma pause maintenant ?", "une permission"),
        ("Est-ce que vous pouvez m'aider avec le chariot ?", "de l'aide"),
        ("Est-ce que je peux partir à midi jeudi ?", "une permission"),
        ("Qui peut m'aider à porter les boîtes ?", "de l'aide"),
        ("Est-ce que je pourrais échanger mon quart ?", "une permission"),
        ("Est-ce que tu peux me montrer le lave-vaisselle ?", "de l'aide"),
        ("Est-ce que je peux poser une question ?", "une permission"),
        ("Passe-moi ton crayon, s'il te plaît.", "de l'aide"),
    ], corrige=True,
       notes="C'est l'exercice `t2ecoute` du module interactif, mot pour mot. Le faire "
             "livre fermé. La dernière ligne n'a ni « est-ce que » ni « pouvoir » : c'est "
             "l'impératif entre collègues, et il demande quand même de l'aide.")

    d.tableau('Analyse', "À qui on adresse chaque demande",
              ["Ce qu'on demande", "À qui, le plus souvent"],
              [["une permission", "au chef d'équipe — lui seul peut la donner"],
               ["de l'aide sur une tâche", "à un collègue, d'abord"],
               ["un petit service", "à un collègue, sans formalité"],
               ["une explication", "à celui qui sait — collègue ou chef"]],
              cle=1,
              note="Demander une permission à un collègue fait perdre du "
                   "temps ; demander de l'aide au chef pour un crayon en "
                   "fait perdre aussi.",
              notes="Diapo à photographier. Savoir à qui s'adresser fait autant partie du "
                    "travail que savoir le dire. Beaucoup de nouveaux employés posent "
                    "toutes leurs questions à la même personne, par prudence.")

    d.pratique('Production', "Deux par deux : demandez, répondez",
               "L'un demande, l'autre répond — et dit ce qui a été demandé.", [
        ("Vous voulez prendre votre pause plus tôt.", "permission : « est-ce que je peux… ? »"),
        ("Le chariot est trop lourd pour vous seul.", "aide : « est-ce que vous pouvez… ? »"),
        ("Vous n'avez pas compris la consigne du chef.", "explication : « qu'est-ce qu'il faut faire ? »"),
        ("Vous voulez apprendre à partir le lave-vaisselle.", "permission : « est-ce que je peux regarder ? »"),
        ("Il vous manque un crayon pour noter.", "service : « passe-moi ton crayon, s'il te plaît »"),
    ], corrige=False, cols=1,
       notes="Quinze minutes, puis on inverse les rôles. Demander à celui qui répond de "
             "nommer le type de demande avant de répondre : c'est ce qui fixe la "
             "distinction.")

    d.piege("Demander une permission pour de l'aide",
            "Est-ce que je peux porter les boîtes avec vous ?",
            "Est-ce que vous pouvez m'aider à porter les boîtes ?",
            "La première phrase demande la permission de faire soi-même une "
            "chose que l'autre est en train de faire. Elle est correcte, "
            "mais elle ne demande pas ce qu'on veut : personne ne viendra "
            "aider.",
            notes="Le piège est fréquent chez ceux qui n'osent pas déranger : ils "
                  "transforment toute demande en permission. Le nommer doucement — c'est "
                  "de la politesse mal placée, pas une faute de langue.")

    d.billet(
        "Écrivez deux demandes : une permission, une demande d'aide.",
        exemples=[
            "Des situations vraies, de votre travail ou de votre école.",
            "Soulignez le sujet du verbe : je, ou vous.",
        ],
        notes="Devoir court. Souligner le sujet est ce qui rend la différence visible sur "
              "le papier : « je peux » d'un côté, « vous pouvez » de l'autre.")

    return d.save(dossier)
