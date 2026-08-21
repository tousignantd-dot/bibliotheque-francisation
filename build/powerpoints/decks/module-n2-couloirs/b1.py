# -*- coding: utf-8 -*-
"""B1 · Le plan du centre.
Bloc B « Défi 1 · Le plan et les numéros » · couleur acier · 75 min.
Source : dialogue `t1`, exercices `t1vf` et `t1plan`.

C'est la séance de compréhension écrite du module, et l'intention du
programme la nomme exactement : comprendre le plan d'un établissement de
formation. Un plan n'est pas un texte — il se lit par blocs, par étages, par
colonnes — et c'est justement ce qui le rend lisible à un débutant.

Le plan projeté est celui du Centre Bellevue, inventé pour le module. La
séance se termine devant le vrai plan du vrai centre.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-couloirs/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Le plan du centre",
        chapeau="Lire le plan affiché près de l'accueil et y trouver un "
                "endroit sans demander à personne.",
        duree='75 minutes')

    d.titre(notes="Deuxième bloc. Apporter une copie papier du vrai plan du centre, une "
                  "par élève : la séance se termine dessus.")

    d.objectifs([
        "reconnaitre ce qu'est un plan d'établissement ;",
        "trouver un étage sur un plan ;",
        "trouver un endroit à partir de son nom ;",
        "répondre par vrai ou faux à des questions sur un plan.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce que ce panneau au mur ?",
        image=IMG + 'comptoir-accueil.jpg',
        pistes=[
            "Où est-ce qu'on trouve ce genre de panneau ?",
            "Qu'est-ce qu'il montre ?",
            "Est-ce qu'on lit un plan comme on lit une lettre ?",
            "Qu'est-ce qu'on cherche en premier, sur un plan ?",
        ],
        notes="La troisième piste est celle qui compte : un plan ne se lit pas ligne "
              "par ligne. On cherche d'abord son étage, ensuite son endroit.")

    d.dialogue('Dialogue', "Vincent montre le plan à Soraya", [
        ("SORAYA", "Vincent, c'est quoi, ce grand papier ?", True),
        ("VINCENT", "C'est le plan du centre. Regarde.", True),
        ("SORAYA", "Il y a trois étages.", True),
        ("VINCENT", "Oui. Et le premier chiffre dit l'étage.", True),
        ("SORAYA", "Alors le 214, c'est au deuxième étage ?", True),
        ("VINCENT", "C'est ça. Et le 108, c'est au premier.", True),
    ], consigne="Écoutez deux fois, puis dites ce que Soraya vient de comprendre.",
       notes="Six répliques, et une règle découverte par l'élève elle-même. Ne pas "
             "donner la règle : la faire formuler par le groupe.")

    d.tableau('Lecture · 1 de 2', "PLAN DU CENTRE BELLEVUE - les trois étages",
              ["Étage", "Ce qu'on y trouve"],
              [["Rez-de-chaussée", "l'accueil (001), le secrétariat (005)"],
               ["Rez-de-chaussée", "la cafétéria (012), les casiers (015)"],
               ["Premier étage", "la bibliothèque (108), les locaux 110 à 118"],
               ["Deuxième étage", "les locaux 210 à 218, le 214 au bout à droite"]],
              cle=1,
              notes="Diapositive à photographier, et la plus importante du bloc. La "
                    "laisser affichée pendant tout l'exercice qui suit.")

    d.tableau('Lecture · 2 de 2', "PLAN DU CENTRE BELLEVUE - les repères",
              ["Repère", "Où il est"],
              [["Escalier et ascenseur", "au milieu du corridor, à chaque étage"],
               ["Toilettes", "à chaque étage, en face de l'ascenseur"],
               ["Sortie", "à côté de l'accueil, au rez-de-chaussée"]],
              cle=1,
              note="Le même plan est dans le bandeau noir de l'exercice 3, en ligne.",
              notes="Ces trois repères se retrouvent partout dans le bâtiment : les "
                    "apprendre une fois sert à tous les étages.")

    d.regle("On cherche l'étage avant de chercher la porte",
            "Deux gestes, dans cet ordre, et jamais l'inverse.",
            precision="Un plan de bâtiment est fait d'<b>étages</b>. On repère d'abord "
                      "le sien, puis on cherche son endroit à l'intérieur. Chercher un "
                      "numéro dans tout le plan à la fois est le meilleur moyen de ne "
                      "pas le trouver.",
            notes="Diapositive à photographier. Le montrer avec le doigt sur le plan "
                  "projeté, lentement, deux fois.")

    d.pratique('Compréhension écrite', "Vrai ou faux, d'après le plan",
               "Répondez en regardant le plan de la diapositive précédente.", [
        ("Le secrétariat est au rez-de-chaussée.", "vrai"),
        ("La bibliothèque est au deuxième étage.", "faux - elle est au premier"),
        ("Il y a des toilettes à chaque étage.", "vrai"),
        ("L'escalier est au bout du corridor.", "faux - il est au milieu"),
        ("Le local 214 est au bout du corridor, à droite.", "vrai"),
        ("La sortie est à côté de l'accueil.", "vrai"),
    ], corrige=True, cols=1,
       notes="Six énoncés, faits d'abord seul, puis corrigés à deux devant le plan. "
             "C'est l'exercice de compréhension écrite du programme.")

    d.pratique('Pratique · sur le vrai plan', "Le plan de notre centre",
               "Avec la copie papier distribuée au début de la séance.", [
        ("Étape 1", "Chacun trouve son propre local sur le plan."),
        ("Étape 2", "Chacun trouve les toilettes de son étage."),
        ("Étape 3", "Chacun trouve la cafétéria et la sortie."),
        ("Étape 4", "Le groupe descend voir le vrai plan affiché au mur."),
    ], cols=1,
       notes="Vingt minutes. L'étape 4 vaut toutes les autres : beaucoup d'élèves "
             "passent devant ce panneau depuis des semaines sans l'avoir regardé.")

    d.billet(
        "Écrivez à quel étage sont trois endroits de notre centre.",
        exemples=[
            "Mon local : au deuxième étage",
            "Les toilettes : au deuxième étage",
            "La cafétéria : au rez-de-chaussée",
        ],
        notes="Devoir court. Il prépare directement la séance B2, où le numéro seul "
              "suffira à répondre.")

    return d.save(dossier)
