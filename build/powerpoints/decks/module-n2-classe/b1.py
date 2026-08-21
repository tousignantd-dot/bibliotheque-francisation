# -*- coding: utf-8 -*-
"""B1 · La consigne, et « je n'ai pas compris ».
Bloc B « Défi 1 · La consigne de l'enseignante » · couleur acier · 75 min.
Source : dialogues `t1` et `t1b`, exercices `t1imper`, `t1geste` et `t1b`.

La séance de compréhension orale du module, et la plus utile de toutes : huit
verbes à l'impératif suffisent à suivre une matinée entière de cours.

Les huit verbes sont ceux du programme — lisez, ouvrez, fermez, enlevez,
donnez, mettez, écoutez — repris avec les deux que la classe ajoute toujours,
« écrivez » et « effacez ».
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-classe/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="La consigne, et « je n'ai pas compris »",
        chapeau="Huit verbes suffisent à suivre une matinée de cours. Et une "
                "phrase suffit quand ils manquent.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 1. Prévenir le groupe : à partir "
                  "d'aujourd'hui, toutes les consignes du cours se donnent en français, "
                  "sans traduction. C'est possible parce que les huit verbes sont "
                  "affichés au tableau.")

    d.objectifs([
        "reconnaître huit consignes de classe ;",
        "faire le geste demandé sans traduire ;",
        "demander de répéter poliment ;",
        "demander le sens d'un seul mot.",
    ])

    d.declencheur(
        'Observation', "Que demande l'enseignante ?",
        image=IMG + 'pupitre-eleve.jpg',
        pistes=[
            "Écoutez : « Prenez une feuille. »",
            "Qu'est-ce que vous faites ?",
            "Écoutez : « Écrivez votre nom en haut. »",
            "Et si vous n'avez pas compris ?",
        ],
        notes="Donner les consignes pour vrai pendant l'observation : le groupe prend une "
              "feuille et écrit son nom. La séance commence par un geste, pas par une "
              "explication.")

    d.dialogue('Dialogue · 1 de 2', "Fermez votre cahier", [
        ("MADAME LEDUC", "Fermez votre cahier. Prenez une feuille.", True),
        ("TARIQ", "Une feuille blanche ?", True),
        ("MADAME LEDUC", "Oui, une feuille blanche. Écrivez votre nom en haut.", True),
        ("MYRIAM", "Madame, pouvez-vous répéter ?", True),
        ("MADAME LEDUC", "Écrivez votre nom en haut de la feuille.", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Remarquer que l'enseignante répète **les mêmes mots**, plus lentement. Elle "
             "ne reformule pas : reformuler donnerait une deuxième phrase inconnue à "
             "comprendre.")

    d.dialogue('Dialogue · 2 de 2', "Un mot qui bloque", [
        ("TARIQ", "Moi, je n'ai pas compris le mot « effacez ».", True),
        ("MYRIAM", "Effacer, c'est enlever avec la gomme.", True),
        ("TARIQ", "Ah ! D'accord. Merci, Myriam.", True),
        ("MADAME LEDUC", "Effacez. On efface avec la gomme. Comme ça.", True),
    ], notes="Deux aides de suite : le voisin d'abord, l'enseignante ensuite. Dire au "
             "groupe que demander à son voisin est permis, et même souhaitable.")

    d.tableau('Analyse', "Les huit consignes de la classe",
              ["Ce qu'on entend", "Ce qu'on fait"],
              [["Ouvrez · Prenez", "on sort le cahier, la feuille"],
               ["Écoutez · Regardez", "on arrête d'écrire, on lève les yeux"],
               ["Écrivez · Effacez", "le crayon, puis la gomme"],
               ["Fermez · Donnez", "on range, on remet son travail"]],
              cle=2,
              note="Huit mots. Une fois qu'ils sont là, la matinée se suit sans traduire.",
              notes="Diapositive à photographier, et à afficher au mur pour tout le "
                    "module. Les élèves la regardent pendant des semaines.")

    d.regle("Le verbe est seul, au début",
            "Une consigne n'a pas de « vous » devant.",
            precision="On dit « <b>Ouvrez</b> votre cahier », pas « vous ouvrez votre "
                      "cahier ». Avec « vous », ce n'est plus une consigne : c'est une "
                      "phrase qui raconte une habitude. Le verbe seul, en tête de "
                      "phrase, veut dire « faites-le maintenant ».",
            notes="Diapositive à photographier. Faire entendre les deux phrases à la "
                  "suite : la différence de sens est immédiate, même sans explication.")

    d.regle("« Pouvez-vous répéter ? »",
            "La phrase qui remplace toutes les traductions.",
            precision="Trois autres, aussi utiles : « <b>Plus lentement</b>, s'il vous "
                      "plaît. » « <b>Qu'est-ce que ça veut dire</b>, effacez ? » Et pour "
                      "vérifier : « Alors, j'ouvre à la page douze ? »",
            notes="Diapositive à photographier. Faire dire les quatre phrases par chaque "
                  "élève. Elles serviront tous les jours pendant deux ans.")

    d.pratique('Pratique', "La consigne et le geste",
               "Associez chaque consigne à ce que fait l'élève.", [
        ("Ouvrez votre cahier à la page douze.", "il cherche le numéro 12 en haut"),
        ("Prenez une feuille blanche.", "il sort un papier de son sac"),
        ("Effacez le mot.", "il enlève le mot avec sa gomme"),
        ("Regardez le tableau.", "il lève les yeux vers l'avant"),
        ("Donnez-moi votre feuille.", "il se lève et va porter son travail"),
        ("Fermez votre cahier.", "il arrête d'écrire et range son crayon"),
    ], corrige=True, cols=1,
       notes="Ce sont les six paires de l'exercice 4 du module en ligne. Les faire "
             "d'abord en gestes, sans lire : l'enseignante dit, la classe fait.")

    d.pratique('Pratique · en groupe', "Jacques a dit, version classe",
               "Debout. Une consigne, un geste. Qui se trompe s'assoit.", [
        ("Étape 1", "L'enseignante donne les huit consignes, dans le désordre."),
        ("Étape 2", "Elle accélère un peu, sans jamais changer les mots."),
        ("Étape 3", "Un élève prend sa place et donne les consignes."),
        ("Étape 4", "On ajoute : « pouvez-vous répéter ? » est permis, et fait gagner."),
    ], cols=1,
       notes="Vingt minutes, et c'est le moment le plus joyeux du module. L'étape 4 "
             "compte : elle récompense la demande d'aide au lieu de la punir.")

    d.billet(
        "Écrivez trois consignes, et à côté, ce que vous faites.",
        exemples=[
            "Ouvrez votre cahier. — J'ouvre mon cahier.",
            "Écoutez bien. — J'arrête d'écrire.",
            "Effacez le mot. — Je prends ma gomme.",
        ],
        notes="Devoir court. La deuxième colonne fait travailler « je » au présent, qui "
              "revient en C1 avec « est-ce que je peux ».")

    return d.save(dossier)
