# -*- coding: utf-8 -*-
"""B2 · Dans, d'ici, avant, à partir de.
Bloc B « Défi 1 » · couleur ambre · 75 min. Écriture.
Source : exercice `t1temps` et sa mini-leçon.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-rendezvous/images/')


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Dans, d'ici, avant, à partir de",
        chapeau="Sept petits mots décident du jour où vous vous "
                "présenterez. Les confondre ne rend pas la phrase fausse : "
                "ça vous fait venir le mauvais jour.",
        duree='75 minutes')

    d.titre(notes="Rendre les billets de B1. Écrire au tableau « dans trois jours » et "
                  "« en trois jours » et demander au groupe si c'est la même chose. La "
                  "classe se divise toujours — c'est le déclencheur de la séance.")

    d.objectifs([
        "distinguer « dans » et « d'ici » ;",
        "employer « avant » et « à partir de » pour poser une limite ou un début ;",
        "distinguer « en » (le temps qu'il faut) de « dans » (le moment) ;",
        "savoir que « vers » ne s'emploie jamais pour l'heure d'un rendez-vous.",
    ])

    d.declencheur(
        'Observation', "« Vous aurez le résultat dans trois jours » ou « d'ici trois "
                       "jours ». Est-ce pareil ?",
        image=IMG + 'calendrier-rendezvous.jpg',
        pistes=[
            "Si on est lundi, quel jour dans le premier cas ?",
            "Et dans le second ?",
            "Lequel des deux vous laisse attendre le moins ?",
            "Lequel une clinique dit-elle le plus souvent ?",
        ],
        notes="Faire poser les jours au tableau, avec les dates. La différence devient "
              "visible en dix secondes, et elle ne s'oublie plus.")

    d.regle("« dans » pose un point, « d'ici » ouvre une fenêtre",
            "« dans trois jours » = jeudi. « d'ici trois jours » = mardi, mercredi ou jeudi.",
            precision="C'est la différence la plus coûteuse du module : on attend un appel "
                      "jeudi alors qu'il pouvait arriver mardi, ou l'inverse. Les deux "
                      "s'entendent dans la même conversation.",
            notes="Diapositive à photographier. Faire répéter les deux phrases à voix "
                  "haute, avec les jours nommés.")

    d.cartes("Sept mots de temps", "Et ce que chacun fait", [
        ("dans + une durée",
         "Un moment futur, compté depuis aujourd'hui. « Le rendez-vous est dans trois semaines. »"),
        ("d'ici + un moment",
         "Avant la fin de ce délai. « Vous aurez le résultat d'ici vendredi. »"),
        ("avant",
         "La limite à ne pas dépasser. « Il faut annuler avant vingt-quatre heures. »"),
        ("à partir de",
         "Le moment où ça commence. « La clinique ouvre à partir de sept heures quinze. »"),
        ("vers",
         "Approximatif — pour votre arrivée à vous, jamais pour l'heure du rendez-vous."),
        ("pour + durée / en + durée",
         "Ce qui est réservé, et le temps qu'il faut. « une plage pour trente minutes »."),
    ], cols=3,
       notes="Les apprendre par paires opposées — dans / d'ici, avant / à partir de, "
             "en / dans — plutôt qu'en liste. C'est l'opposition qui se retient.")

    d.tableau('Le cas qui trompe tout le monde', "en trois jours, ou dans trois jours ?",
              ['La phrase', 'Ce que ça veut dire'],
              [["Le laboratoire donne le résultat en trois jours.", "ça lui prend trois jours"],
               ["Vous aurez le résultat dans trois jours.", "ce sera jeudi"],
               ["Vous l'aurez d'ici trois jours.", "jeudi au plus tard"],
               ["Vous l'aurez à partir de jeudi.", "pas avant jeudi"]],
              cle=0,
              notes="Les quatre phrases peuvent être dites dans le même appel. Faire "
                    "remarquer qu'aucune n'est fausse : elles disent des choses "
                    "différentes.")

    d.piege("Lire « avant vingt-quatre heures » comme une heure",
            "« Avant minuit, alors ? »",
            "« Plus de vingt-quatre heures avant le rendez-vous. »",
            "C'est un délai, pas une heure de la journée. Si le rendez-vous est jeudi à "
            "seize heures trente, la limite est mercredi à seize heures trente — et non "
            "mercredi soir.",
            notes="Faire calculer la limite pour deux rendez-vous inventés par le groupe. "
                  "Ça se fait de tête, et ça ancre la règle.")

    d.pratique('Écriture', "Complétez avec le mot juste",
               "dans · d'ici · avant · à partir de · vers · pour · en", [
        ("Le prochain rendez-vous libre est ___ trois semaines.", "dans"),
        ("Vous recevrez le résultat ___ vendredi, au plus tard.", "d'ici"),
        ("Il faut annuler ___ vingt-quatre heures.", "avant"),
        ("La docteure reçoit ___ sept heures quinze.", "à partir de"),
        ("Je pense arriver ___ seize heures quarante.", "vers"),
        ("Je vous réserve une plage ___ trente minutes.", "pour"),
        ("L'étourdissement passe ___ dix secondes.", "en"),
        ("Mon horaire change ___ lundi prochain.", "à partir de"),
    ], corrige=True, cols=2,
       notes="Les deux dernières sont les plus difficiles. Les faire justifier oralement "
             "avant d'afficher la correction.")

    d.billet(
        "Écrivez trois phrases sur votre semaine avec « dans », « d'ici » et « avant ».",
        exemples=[
            "« J'ai un rendez-vous dans… », « Je dois répondre d'ici… », « Il faut partir avant… »",
            "Des phrases vraies : vos vraies dates, votre vraie semaine.",
        ],
        notes="Ramasser. Les erreurs entre « dans » et « d'ici » se corrigent très vite "
              "quand elles portent sur la semaine de l'élève.")

    return d.save(dossier)
