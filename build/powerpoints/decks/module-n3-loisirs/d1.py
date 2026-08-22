# -*- coding: utf-8 -*-
"""D1 · Un pâté chinois pour quatre.
Bloc D « Défi 3 · La cuisine collective » · acier · 75 min.
Source du module : dialogue `t3`, exercices `t3vf` et `t3img`.
"""
import os

from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n3-loisirs/images/')


def img(nom):
    """Le chemin de la photo, ou None tant qu'elle n'existe pas.

    Voir la note de a1.py : les images sont produites par gen_images.py, et
    `theme.image()` ouvrirait un fichier absent.
    """
    chemin = IMG + nom
    return chemin if os.path.exists(chemin) else None


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Un pâté chinois pour quatre",
        chapeau="Quatre personnes, une recette, un gros chaudron. Chacun "
                "repart avec quatre portions pour deux dollars. Il reste à "
                "comprendre ce que la feuille demande — et ce que veulent "
                "dire « pelez », « égouttez », « 60 ml ».",
        duree='75 minutes')

    d.titre(notes="Première séance du défi 3. Si l'établissement a une cuisine, la "
                  "séance gagne à s'y faire : la recette se comprend en la faisant, et "
                  "les outils se nomment en les prenant dans la main.")

    d.objectifs([
        "comprendre ce qu'est une cuisine collective et comment elle marche ;",
        "nommer les outils d'une cuisine : le bol, le chaudron, l'économe ;",
        "suivre les consignes d'une recette dans l'ordre ;",
        "demander ce que veut dire un mot que je ne connais pas.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qui se passe dans cette cuisine ?",
        image=img('cuisine-collective.jpg'),
        pistes=[
            "Combien de personnes travaillent ensemble, et sur quoi ?",
            "Pourquoi cuisiner à plusieurs plutôt que chacun chez soi ?",
            "Qu'est-ce que chacun rapporte à la maison, à la fin ?",
            "Est-ce qu'il faut savoir cuisiner pour venir ?",
        ],
        notes="La dernière piste est la vraie question, et la réponse est non. La donner "
              "clairement : c'est ce qui décide de venir ou non, et beaucoup d'élèves "
              "s'en interdisent l'entrée pour rien.")

    d.dialogue('Dialogue · 1 de 3', "Quatre portions pour deux dollars", [
        ("DENIS", "Bienvenue à la cuisine collective ! Vous êtes Marisol ?", True),
        ("MARISOL", "Oui. C'est ma première fois. Qu'est-ce qu'on fait, aujourd'hui ?", True),
        ("DENIS", "Un pâté chinois. Quatre personnes, une recette, et chacun repart avec quatre portions.", True),
        ("MARISOL", "Quatre portions pour deux dollars ? C'est peu.", True),
        ("DENIS", "C'est le principe : on achète ensemble, donc ça coûte moins cher. Prenez un tablier.", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="Le principe économique de la cuisine collective tient dans la cinquième "
             "réplique. Le faire reformuler par un élève : « on achète ensemble, donc "
             "ça coûte moins cher ».")

    d.dialogue('Dialogue · 2 de 3', "Pelez ? Faites bouillir ?", [
        ("MARISOL", "Je lis la recette… « Pelez six pommes de terre. » Pelez ?", True),
        ("DENIS", "Enlevez la peau, avec l'économe. Ensuite, coupez-les en gros morceaux.", True),
        ("MARISOL", "« Faites bouillir vingt minutes. » Vingt minutes dans l'eau chaude ?", True),
        ("DENIS", "Dans l'eau qui bout, oui. Le gros chaudron est là, sur le rond arrière.", True),
    ], notes="Marisol demande le sens d'un mot en le répétant seul, avec une intonation "
             "de question : « Pelez ? ». C'est la technique la plus simple qui existe "
             "pour faire expliquer un mot, et elle marche partout. La faire pratiquer.")

    d.dialogue('Dialogue · 3 de 3', "Soixante millilitres", [
        ("MARISOL", "Après : « Ajoutez 60 ml de lait et une cuillère à soupe de beurre. »", True),
        ("DENIS", "La tasse à mesurer est dans l'armoire. Soixante millilitres, c'est le quart d'une tasse.", True),
        ("MARISOL", "Et « c. à soupe », c'est l'abréviation de cuillère à soupe ?", True),
        ("DENIS", "Exactement. « c. à thé », c'est la petite ; « c. à soupe », c'est la grande.", True),
    ], notes="Les abréviations sont travaillées en D2. Ici, seulement les faire "
             "entendre : « c. à soupe » se dit en entier quand on parle, jamais « cé à "
             "soupe ». C'est une abréviation d'écriture, pas de parole.")

    d.tableau('Analyse', "La recette, dans l'ordre",
              ["Le geste", "Ce qu'on fait"],
              [["Pelez", "enlevez la peau, avec l'économe"],
               ["Coupez", "faites de gros morceaux, pas des tranches"],
               ["Faites bouillir", "vingt minutes dans l'eau qui bout"],
               ["Égouttez", "jetez l'eau, gardez les pommes de terre"],
               ["Écrasez", "puis ajoutez le lait et le beurre"],
               ["Mélangez", "jusqu'à ce que ce soit lisse"]],
              cle=0,
              notes="Diapo à photographier. Chaque geste prépare le suivant : on ne "
                    "saute pas de ligne. Faire mimer les six gestes debout, sans "
                    "parler : c'est ridicule pendant trente secondes et ça retient les "
                    "verbes pour de bon.")

    d.vocabulaire('Vocabulaire', "Les outils de la cuisine collective", [
        ("un bol", "Le grand contenant rond et creux où l'on mélange."),
        ("un chaudron", "Le gros contenant de métal à deux poignées, pour faire bouillir."),
        ("une casserole", "Le contenant à un seul manche, pour de petites quantités."),
        ("une poêle", "Le plat rond et plat, à long manche, pour faire revenir."),
        ("un économe", "Le petit outil à lame qui enlève la peau des légumes."),
        ("une tasse à mesurer", "Le contenant transparent avec des traits sur le côté."),
    ], notes="Ces six mots viennent directement du programme de niveau 3, qui nomme "
             "« les outils de cuisine : bol, tasse à mesurer, poêle, casserole ». Les "
             "faire répéter avec leur article.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("À la cuisine collective, chacun repart avec quatre portions.", "vrai"),
        ("On cuisine ensemble parce que ça coûte moins cher.", "vrai"),
        ("« Peler » veut dire couper en gros morceaux.", "faux — c'est enlever la peau"),
        ("Les pommes de terre bouillent pendant vingt minutes.", "vrai"),
        ("Soixante millilitres, c'est le quart d'une tasse.", "vrai"),
        ("« c. à thé » est l'abréviation de cuillère à soupe.", "faux — de cuillère à thé"),
        ("Une recette ne peut jamais être changée.", "faux — on l'adapte, il suffit de le dire"),
    ], corrige=True,
       notes="C'est l'exercice t3vf du module. La dernière affirmation prépare la fin "
             "du dialogue, où Denis accepte de mettre le maïs dans deux portions "
             "seulement.")

    d.billet(
        "Écrivez le nom de trois outils de votre cuisine, avec leur article.",
        exemples=[
            "Ajoutez, pour chacun, ce qu'on fait avec.",
            "Exemple : un chaudron — on y fait bouillir de l'eau.",
        ],
        notes="Devoir court. Les objets nommés servent d'exemples en D2, quand les "
              "quantités et les abréviations arrivent.")

    return d.save(dossier)
