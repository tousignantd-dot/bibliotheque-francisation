# -*- coding: utf-8 -*-
"""A2 · « Une minute » et « un rendez-vous ».
Bloc A « Je découvre » · couleur indigo · 75 min. Graphie-phonie.
Source : exercice `prPhon` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="« Une minute » et « un rendez-vous »",
        chapeau="Deux sons, une seule chose qui bouge — la langue, que "
                "personne ne voit. Au téléphone, c'est ce qui décide si "
                "l'on comprend votre nom du premier coup.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance. Commencer par ramasser le billet de sortie de A1 et "
                  "faire lire trois phrases de durée à voix haute. Elles contiennent déjà "
                  "les deux sons du jour : « depuis », « toujours », « une semaine ».")

    d.objectifs([
        "distinguer à l'oreille le son de « une » et celui de « vous » ;",
        "produire le son de « une » en partant du son « i » ;",
        "lire à voix haute les mots du module qui portent ces deux sons ;",
        "reconnaître les paires où le sens change complètement.",
    ])

    d.declencheur(
        'Écoute', "« Je suis sûr » ou « je suis sourd » ? Deux phrases, un seul son "
                  "de différence.",
        image=IMG + 'appel-carnet.jpg',
        pistes=[
            "Les dire l'une après l'autre, sans annoncer laquelle.",
            "Faire lever la main à chaque phrase.",
            "Y a-t-il un mot de la phrase qui aide à choisir ?",
            "Et au téléphone, sans voir la bouche ?",
        ],
        notes="Les faire deviner à l'aveugle avant d'expliquer quoi que ce soit. L'écart "
              "entre les mains levées est le meilleur argument de la séance.")

    d.regle("Ce n'est pas la bouche, c'est la langue",
            "Les lèvres sont rondes dans les deux cas. Seule la langue change de place.",
            precision="Pour « une », la langue est poussée vers l'avant, contre les dents "
                      "du bas. Pour « vous », elle recule au fond de la bouche. C'est le "
                      "seul mouvement à apprendre — et c'est le seul qu'on ne peut pas "
                      "voir chez quelqu'un d'autre.",
            notes="Diapositive à photographier. Faire faire le mouvement en même temps que "
                  "l'explication, deux ou trois fois, en silence.")

    d.cartes("La recette, en deux gestes", "Comment sortir chaque son", [
        ("Le son de « une »",
         "On dit « i ». On garde la langue exactement là. On arrondit les lèvres. Le son sort seul."),
        ("Le son de « vous »",
         "Lèvres arrondies aussi, mais la langue recule au fond. C'est le son le plus facile des deux."),
        ("L'écriture",
         "« une » s'écrit avec un u seul. « vous » s'écrit avec ou, deux lettres pour un son."),
        ("Le piège du q",
         "Dans quinze, quatre, question, le u ne se prononce pas. Il est là pour la lettre q."),
    ], notes="Partir de « i » et non de « ou » : c'est le chemin court, et il marche avec "
             "presque tous les élèves du premier coup.")

    d.vocabulaire('Les mots du module', "Neuf mots à classer à l'oreille", [
        ("vous", "le son de « vous » — langue au fond"),
        ("une", "le son de « une » — langue en avant"),
        ("un jour", "le son de « vous »"),
        ("la durée", "le son de « une »"),
        ("douze", "le son de « vous »"),
        ("une minute", "le son de « une », deux fois"),
        ("une urgence", "le son de « une »"),
        ("le rendez-vous", "le son de « vous », à la fin"),
    ], notes="Les faire répéter en série, puis en désordre. C'est exactement l'exercice "
             "prPhon du module : les élèves le retrouveront à l'écran.")

    d.tableau('Quatre paires', "Un son, deux mots différents",
              ['On entend', 'Ou bien'],
              [["je suis sûr", "je suis sourd"],
               ["la rue", "la roue"],
               ["je vous ai vu", "je vous ai vous"],
               ["dessus", "dessous"]],
              cle=0,
              notes="La troisième ligne est volontairement impossible : elle montre que le "
                    "contexte ne sauve pas toujours. Le faire remarquer.")

    d.piege("Allonger la voyelle pour insister",
            "« Uuune minute, s'il vous plaît. »",
            "« Une miNUTE, s'il vous plaît. »",
            "Le français n'allonge pas ses voyelles pour insister : il pose l'accent sur "
            "la dernière syllabe du groupe. Allonger la première fait entendre un accent "
            "étranger là où il n'y avait qu'une hésitation.",
            notes="Beaucoup d'élèves allongent par prudence, croyant se faire mieux "
                  "comprendre. Leur montrer que c'est l'inverse.")

    d.pratique('Prononciation', "Lisez à voix haute",
               "Une phrase par personne, lentement.", [
        ("Une minute, je vérifie vos disponibilités.", "trois fois le son de « une »"),
        ("Vous serez à jeun douze heures avant.", "trois fois le son de « vous »"),
        ("La durée du rendez-vous est de trente minutes.", "les deux dans la même phrase"),
        ("Le jour du rendez-vous, arrivez toujours quinze minutes avant.", "en alternance"),
        ("Je suis sûr que c'est le jeudi, pas le mardi.", "le son de « une » au milieu"),
        ("Vous pouvez me joindre au numéro sur la carte.", "en alternance"),
    ], corrige=True,
       notes="Ne pas corriger la première fois. Faire relire la même phrase après le tour "
             "complet : la deuxième lecture est presque toujours meilleure.")

    d.billet(
        "Enregistrez-vous en disant : « Une minute pour un rendez-vous, s'il vous plaît. »",
        exemples=[
            "Écoutez-vous ensuite. Est-ce que « une » et « vous » sonnent pareil ?",
            "Si oui, recommencez en partant du son « i » pour « une ».",
        ],
        notes="Le téléphone de l'élève suffit. Ceux qui n'en ont pas le disent à voix "
              "haute devant vous à la fin de la séance.")

    return d.save(dossier)
