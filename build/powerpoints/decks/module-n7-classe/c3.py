# -*- coding: utf-8 -*-
"""C3 · Un nom à la place d'une phrase
Bloc C « Défi 2 » · couleur ambre · grammaire · 75 min.
Source : exercice `t2nom`, mini-leçon `t2nom`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Un nom à la place d'une phrase",
        chapeau="« La ville a planté quatre cents arbres » devient « la "
                "plantation de quatre cents arbres ». Sept mots gagnés, et "
                "la phrase ne ressemble plus à celle du texte de départ. Un "
                "seul geste règle les deux exigences du résumé.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, et l'outil numéro un du résumé. Le mot "
                  "« nominalisation » figure dans les consignes de travail que les "
                  "élèves recevront ailleurs : le leur donner sans en faire un "
                  "obstacle.")

    d.objectifs([
        "former le nom qui vient d'un verbe ;",
        "reconnaître les quatre familles de noms d'action ;",
        "raccourcir une phrase sans en changer le sens ;",
        "remettre la personne et la date que le nom efface.",
    ], notes="Le quatrième objectif est le garde-fou de la séance, et il est aussi "
             "important que les trois autres : un nom ne dit plus qui a agi.")

    d.declencheur(
        'Observation', "La même chose, deux longueurs",
        pistes=[
            "« La ville a planté quatre cents arbres l'an dernier. »",
            "« La plantation de quatre cents arbres. »",
            "Qu'est-ce qui a disparu entre les deux ?",
            "Est-ce grave ? Dans quel cas ?",
        ],
        notes="Les élèves voient tout de suite ce qui manque : la ville, et l'an "
              "dernier. C'est la moitié de la leçon, et elle vient d'eux.")

    d.tableau('Analyse', "Quatre familles de noms",
              ['La terminaison', 'Du verbe au nom'],
              [["en -tion",
                "planter donne la plantation, répartir donne la répartition"],
               ["en -ment",
                "remplacer donne le remplacement, déplacer le déplacement"],
               ["en -age",
                "arroser donne l'arrosage, abattre l'abattage"],
               ["rien du tout",
                "perdre donne la perte, choisir le choix, mesurer la mesure"]],
              cle=0,
              note="Les noms en -tion sont féminins, ceux en -ment et en -age sont masculins.",
              notes="Diapositive à photographier. La quatrième famille est la plus "
                    "économique et la moins connue : insister dessus.")

    d.pratique('Grammaire', "Trouvez le nom",
               "Écrivez le nom qui vient du verbe, avec son article.", [
        ("planter", "la plantation"),
        ("arroser", "l'arrosage"),
        ("abattre", "l'abattage"),
        ("mesurer", "la mesure"),
        ("perdre", "la perte"),
        ("choisir", "le choix"),
        ("répartir", "la répartition"),
        ("absorber", "l'absorption"),
    ], corrige=True,
       notes="Le dernier est le piège de la liste : absorber donne absorption, et "
             "non « absorbation ». Le faire écrire au tableau.")

    d.pratique('Production', "Récrivez avec un nom",
               "Remplacez le groupe souligné par le nom, sans changer le reste.", [
        ("La ville a planté quatre cents arbres.", "la plantation de quatre cents arbres"),
        ("Les résidents arrosent les jeunes arbres.", "l'arrosage des jeunes arbres"),
        ("Un arbre sur cinq meurt avant trois ans.", "la mort d'un arbre sur cinq"),
        ("On a mesuré la canopée par avion.", "la mesure de la canopée par avion"),
        ("L'équipe a choisi de noter l'ombre.", "le choix de noter l'ombre"),
        ("On a réparti les rôles au début.", "la répartition des rôles"),
    ], corrige=True,
       notes="Faire compter les mots avant et après : le gain est visible, et c'est "
             "ce qui convainc.")

    d.regle("Le nom efface qui, et efface quand",
            "« La plantation de quatre cents arbres » ne dit pas qui les a "
            "plantés ni en quelle année. La phrase de départ le disait.",
            precision="Dans un résumé, remettez-les quand ils comptent : la "
                      "plantation, par la ville, l'an dernier. Trois mots, et le "
                      "renseignement redevient citable.",
            notes="Diapositive à photographier. C'est la règle qui empêche le résumé "
                  "de devenir un texte sans personne, défaut fréquent au niveau 7.")

    d.piege('Écrit',
            "« La mesure de l'observation de la répartition des arbres. »",
            "« On a mesuré la répartition des arbres, et voici ce qu'on observe. »",
            "Trois noms d'action à la file rendent une phrase illisible. La "
            "nominalisation allège une phrase sur trois, pas les trois : "
            "elle vaut par contraste avec les phrases ordinaires autour.",
            notes="Piège d'écriture du niveau intermédiaire : l'élève qui vient "
                  "d'apprendre l'outil l'emploie partout. Une phrase sur trois est "
                  "la bonne mesure.")

    d.pratique('Production', "Deux lignes de votre propre résumé",
               "Prenez une phrase de votre source et récrivez-la avec un nom.", [
        ("La phrase du texte", "recopiez-la telle quelle, une seule"),
        ("Votre version", "avec un nom d'action, et sans les mots du texte"),
        ("Ce que vous avez remis", "la personne, la date, ou les deux"),
        ("Le compte", "combien de mots gagnés ?"),
    ], corrige=False,
       notes="Cœur de la séance. Passer dans les rangs : la difficulté n'est pas de "
             "former le nom, c'est de garder le sens. Vérifier phrase par phrase.")

    d.billet(
        "Récrivez en une ligne, avec un nom d'action, ce que votre équipe a fait cette semaine.",
        exemples=[
            "Commencez par un article : la, le, l'.",
            "Ajoutez qui, et quand.",
        ],
        notes="Billet de sortie. Les lignes reçues sont la première phrase du compte "
              "rendu du bloc D : les garder.")

    return d.save(dossier)
