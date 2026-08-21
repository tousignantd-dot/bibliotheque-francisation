# -*- coding: utf-8 -*-
"""A2 · Le son OU et le son U.
Bloc A « Je découvre » · couleur indigo (graphie-phonie) · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon` (cartes à écouter).

Les sons sont nommés par leurs lettres et par un mot repère — « le son OU,
comme dans soupe ». L'alphabet phonétique reste dans le module interactif :
sur une diapositive projetée, il ne servirait à personne.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre='Le son OU et le son U',
        chapeau="Soupe, poulet, pour ; jus, sucre, légumes. Deux sons faits au "
                "même endroit, avec les mêmes lèvres, et qui séparent pourtant "
                "« pour » de « pur ».",
        duree='60 minutes')

    d.titre(notes="Séance de phonétique. Prévoir les haut-parleurs : tout se joue à "
                  "l'oreille, et les élèves doivent entendre avant de voir écrit.")

    d.objectifs([
        "entendre la différence entre le son OU et le son U ;",
        "prononcer les deux sons en plaçant la langue ;",
        "reconnaître les mots du menu qui portent chacun des deux ;",
        "lire à voix haute les phrases du comptoir.",
    ])

    d.regle("Ce qui change, c'est la langue",
            "soupe  ·  jus",
            precision="Pour les deux sons, les lèvres sont rondes et avancées : "
                      "elles ne bougent pas. C'est la langue qui recule pour OU "
                      "et qui avance pour U. Beaucoup d'élèves cherchent la "
                      "différence dans les lèvres et ne la trouvent jamais.",
            notes="Diapo à photographier. Faire tenir un doigt devant la bouche : les "
                  "lèvres restent identiques d'un son à l'autre. C'est la démonstration "
                  "la plus convaincante de la séance.")

    d.tableau('Analyse', "Où va la langue ?",
              ['Le son', 'La langue', 'Mots repères'],
              [["OU", "tirée vers le fond de la bouche", "soupe, poulet, pour"],
               ["U", "poussée vers les dents du bas", "jus, sucre, légumes"]],
              cle=0,
              note="Les lèvres restent rondes pour les deux sons.",
              notes="Faire prononcer les deux sons lentement, l'un après l'autre, sans "
                    "rien changer aux lèvres. La langue se sent bouger.")

    d.tableau('Prononciation', "Le truc qui marche",
              ['Étape', "Ce qu'on fait"],
              [["1", "dire le son I, langue en avant, lèvres écartées"],
               ["2", "garder la langue exactement où elle est"],
               ["3", "arrondir seulement les lèvres"],
               ["4", "le son qui sort est le son U"]],
              cle=1,
              note="Quatre secondes, et le son est trouvé.",
              notes="Diapo à photographier. Le faire en groupe, lentement, deux fois. "
                    "C'est la méthode la plus rapide pour un élève dont la langue "
                    "maternelle n'a pas ce son.")

    d.pratique('Écoute', "OU ou U ?",
               "Écoutez le mot, puis dites quel son vous entendez.", [
        ("la soupe", "OU"),
        ("le jus", "U"),
        ("le poulet", "OU"),
        ("le sucre", "U"),
        ("pour emporter", "OU"),
        ("les légumes", "U"),
    ], corrige=True,
       notes="Dire chaque mot deux fois, sans le montrer. Les élèves lèvent une main pour "
             "OU, deux pour U : l'enseignante voit tout de suite qui hésite.")

    d.cartes("Les paires qui changent le sens", "Quatre paires", [
        ("pour / pur",
         "« Pour emporter » et « du sucre pur ». Le premier est dans toutes les "
         "commandes du module ; le second est sur les emballages."),
        ("dessous / dessus",
         "Le sac est dessous, le sel est dessus. Deux mots opposés qui ne se "
         "distinguent que par ce son-là."),
        ("la roue / la rue",
         "La roue du chariot, la rue du centre. La confusion se remarque tout de suite "
         "dans une phrase."),
        ("soupe / jus",
         "La paire à retenir : ce sont les deux mots du module, et ils reviennent dans "
         "chaque dialogue."),
    ], notes="Faire répéter chaque paire trois fois : d'abord lentement, puis vite, puis "
             "les yeux fermés pour la reconnaissance.")

    d.piege("Dire OU à la place de U",
            "un jous",
            "un jus",
            "C'est l'erreur la plus fréquente, et elle s'entend beaucoup. Elle vient "
            "d'un réflexe : arrondir les lèvres davantage au lieu d'avancer la langue. "
            "Les lèvres sont déjà bien placées ; c'est la langue qui doit venir en "
            "avant, contre les dents du bas.",
            notes="Faire dire « i - u - i - u » cinq fois de suite, lèvres arrondies en "
                  "permanence. L'élève sent la langue rester en place et la correction "
                  "se fait toute seule.")

    d.pratique('Lecture', "Lisez à voix haute",
               "Six phrases du comptoir. Marquez les sons OU et U.", [
        ("Une soupe au poulet, s'il vous plaît.", "OU trois fois"),
        ("Un jus, du sucre, une minute.", "U trois fois"),
        ("Pour emporter, avec un couvercle.", "OU quatre fois"),
        ("La soupe aux légumes est bonne.", "les deux sons dans la même phrase"),
        ("Douze dollars pour un menu.", "OU puis U"),
        ("Vous voulez du sucre dans votre café ?", "OU et U côte à côte"),
    ], corrige=True,
       notes="Faire lire chaque phrase par deux élèves différents. Corriger seulement les "
             "deux sons de la séance : le reste attendra.")

    d.billet(
        "Trouvez trois mots avec le son OU et trois mots avec le son U.",
        exemples=[
            "Dans le menu d'un endroit où vous mangez, si vous en avez un.",
            "Écrivez-les, et soulignez les lettres qui font le son.",
        ],
        notes="Devoir court. Rapporter un menu ou une photo de menu en classe si "
              "possible : il servira au bloc B.")

    return d.save(dossier)
