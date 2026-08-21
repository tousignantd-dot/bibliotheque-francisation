# -*- coding: utf-8 -*-
"""C1 · La page qu'on ne lit pas de haut en bas.
Bloc C « Défi 2 · L'écran » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2vf`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-services/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="La page qu'on ne lit pas de haut en bas",
        chapeau="Une page de service public n'est pas faite pour être lue : "
                "elle est faite pour qu'on y cherche une réponse. Et "
                "l'encadré « avant de vous déplacer » évite plus de "
                "voyages inutiles que tout le reste de la page.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 2. Ramasser les feuilles d'appel du devoir B4 et en "
                  "regarder trois au projecteur, avec l'accord des élèves. C'est le "
                  "meilleur bilan possible du défi 1.")

    d.objectifs([
        "trouver une information précise dans une page officielle ;",
        "lire la colonne des matières refusées avant celle des acceptées ;",
        "repérer l'encadré qui conditionne tout le reste ;",
        "comprendre les petits mots qui restreignent le sens.",
    ])

    d.declencheur(
        'Observation', "Par où commenceriez-vous à lire cette page ?",
        image=IMG + 'formulaire-ecran.jpg',
        pistes=[
            "En haut, comme un livre ?",
            "Où sont vos yeux allés en premier ?",
            "Qu'est-ce qu'un encadré veut dire ?",
            "Combien de temps avant d'abandonner ?",
        ],
        notes="Beaucoup d'élèves lisent ces pages de haut en bas et se découragent avant "
              "la moitié. Nommer cette fatigue : elle vient de la méthode, pas du niveau "
              "de français.")

    d.dialogue('Dialogue · 1 de 3', "Deux colonnes, et la bonne à lire d'abord", [
        ("LEÏLA", "Pierre-Luc, viens voir. J'ai trouvé la page dont tu m'avais "
                  "parlé, mais je ne comprends pas la moitié.", True),
        ("PIERRE-LUC", "Montre. Ah oui, c'est la page de l'écocentre. Elle est "
                       "longue, mais elle est bien faite.", True),
        ("LEÏLA", "Il y a deux colonnes. « Matières acceptées » et « Matières "
                  "refusées ». Ça, ça va.", True),
        ("PIERRE-LUC", "Lis la deuxième. C'est celle qui cause des problèmes : les "
                       "gens chargent leur auto et ils repartent avec.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Le conseil de Pierre-Luc est contre-intuitif et c'est ce qui le rend "
             "mémorable : on lit d'abord ce qui est refusé, parce que c'est ce qui coûte "
             "un déplacement.")

    d.dialogue('Dialogue · 2 de 3', "Un mot change tout", [
        ("LEÏLA", "« Matières refusées : les matières dangereuses non identifiées, "
                  "les pneus de camion, les déchets qui viennent d'un chantier "
                  "commercial. »", True),
        ("PIERRE-LUC", "Ta peinture, elle est encore dans son pot d'origine ?", True),
        ("LEÏLA", "Oui, avec l'étiquette.", True),
        ("PIERRE-LUC", "Alors elle passe. C'est ce que veut dire « non "
                       "identifiées » : un bidon sans étiquette, ils ne le prennent "
                       "pas.", True),
    ], notes="Deux mots — « non identifiées » — décident du sort de toute la phrase. "
             "C'est l'exemple parfait des mots qui restreignent ; l'écrire au tableau.")

    d.dialogue('Dialogue · 3 de 3', "L'encadré, et « en vigueur »", [
        ("LEÏLA", "Et là, le petit encadré gris, en haut à droite ?", True),
        ("PIERRE-LUC", "« Avant de vous déplacer. » C'est toujours l'encadré le "
                       "plus important d'une page comme celle-là.", True),
        ("LEÏLA", "Il y a un mot que je ne connais pas : « en vigueur ». "
                  "« Tarifs en vigueur au 1er avril ».", True),
        ("PIERRE-LUC", "Ça veut dire : les prix qui s'appliquent aujourd'hui. Une "
                       "loi, un tarif, un horaire : ce qui est en vigueur, c'est ce "
                       "qui compte maintenant.", True),
    ], notes="« En vigueur » sert bien au-delà de ce module : lois, tarifs, horaires, "
             "règlements d'immeuble. Le dire, c'est un mot pour la vie.")

    d.regle("L'encadré « avant de vous déplacer » se lit en premier",
            "Trois phrases qui conditionnent tout le reste de la page.",
            precision="Ce qu'il faut apporter, ce qu'il faut vérifier, ce qui est limité. "
                      "Si vous ne lisez qu'un bloc de la page, c'est celui-là — et il est "
                      "presque toujours en haut, à droite, sur fond gris.",
            notes="Diapositive à photographier. Faire chercher le même encadré sur une "
                  "autre page officielle au projecteur : il y est presque toujours.")

    d.tableau('Les mots qui restreignent', "Petits, et ils retournent la phrase",
              ['Le mot', 'Ce qu\'il fait'],
              [["sauf", "retire un cas de ce qui vient d'être dit"],
               ["non identifié", "ajoute une condition : il faut une étiquette"],
               ["limité à", "il y a un nombre maximum, souvent par année"],
               ["le cas échéant", "seulement si cela s'applique à vous"]],
              cle=0,
              note="« Gratuit pour les résidents, sauf pour les résidus de construction. »",
              notes="Diapositive à photographier. Faire relire la phrase de la note sans "
                    "le « sauf », puis avec : le sens bascule.")

    d.piege("Lire la colonne des matières acceptées en premier",
            "Je vérifie que mon objet est dans la liste de gauche.",
            "Je lis d'abord ce qui est refusé.",
            "Un objet peut être absent des deux colonnes : la liste des acceptées n'est "
            "jamais complète. La liste des refusées, elle, est faite pour être complète — "
            "c'est elle qui vous évite le déplacement.",
            notes="Le raisonnement est fin et il vaut la peine de le développer lentement. "
                  "Il s'applique à toutes les listes officielles, pas seulement ici.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Pierre-Luc conseille de lire d'abord les matières acceptées.", "faux — les refusées"),
        ("Une peinture dans son pot d'origine avec étiquette est acceptée.", "vrai"),
        ("« Non identifiées » veut dire : sans étiquette.", "vrai"),
        ("L'encadré gris s'intitule « Avant de vous déplacer ».", "vrai"),
        ("Le nombre de visites gratuites est illimité.", "faux — il est limité par année"),
        ("« En vigueur » veut dire : qui s'applique en ce moment.", "vrai"),
        ("Les déchets d'un chantier commercial sont acceptés.", "faux — refusés"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la phrase exacte du dialogue. Les élèves "
             "doivent apprendre à citer, pas à se souvenir.")

    d.billet(
        "Trouvez une page de service public et repérez-y trois choses.",
        exemples=[
            "L'encadré le plus important, un mot qui restreint, une date « en vigueur ».",
            "Ville, école, RAMQ, SAAQ — n'importe laquelle. Apportez l'adresse de la page.",
        ],
        notes="Devoir de repérage, sans lecture intégrale : c'est exactement la compétence "
              "visée. Insister sur ce point, sinon les élèves liront tout et s'épuiseront.")

    return d.save(dossier)
