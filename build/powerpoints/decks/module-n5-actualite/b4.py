# -*- coding: utf-8 -*-
"""B4 · « Un évènement, ou le décor ? »
Bloc B « Défi 1 · Ce qui est arrivé » · couleur ambre · 75 min.
Source : exercices `t1tri` et `t1red`, mini-leçon `t1tri`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='ambre',
        titre="Un évènement, ou le décor ?",
        chapeau="Le passé composé et l'imparfait ne se remplacent pas : ils "
                "se croisent. Ce n'est pas le verbe qui décide lequel "
                "employer, c'est ce que vous voulez dire. Deux questions "
                "suffisent à trancher, et cette séance ne fait que ça.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du défi 1. Elle réunit B2 et B3 et se termine par "
                  "le récit complet, en quatre temps. Prévoir la moitié du temps pour "
                  "l'écriture : c'est la production qui compte, le tri n'est qu'un "
                  "moyen.")

    d.objectifs([
        "trancher entre passé composé et imparfait avec deux questions ;",
        "reconnaître qu'un même verbe change de camp selon le sens ;",
        "raconter un fait divers en quatre temps ;",
        "terminer un récit par ce qui a changé pour les gens.",
    ], notes="Le troisième objectif est celui de l'évaluation. Projeter les quatre "
             "temps au tableau et les y laisser jusqu'à la fin de la séance.")

    d.regle("Première question : est-ce que ça a un début et une fin ?",
            "Si oui, c'est un évènement : passé composé. Si la chose "
            "était simplement là, c'est le décor : imparfait.",
            precision="Le feu a commencé. Les pompiers sont arrivés. La rue a été "
                      "fermée. — début et fin, donc évènements. Il ventait. La rue "
                      "était déserte. Tout le monde dormait. — rien ne commence, "
                      "donc décor.",
            notes="Diapositive à photographier. Faire poser la question à voix haute "
                  "sur cinq phrases avant de passer à la suivante : c'est un réflexe "
                  "à installer, pas une notion à comprendre.")

    d.regle("Deuxième question : est-ce que je peux compter combien de fois ?",
            "Il a cogné à quatre portes — on compte : passé composé. Il "
            "pleuvait depuis trois jours — on ne compte pas : imparfait.",
            precision="C'est le test le plus rapide des deux, et celui qui règle les "
                      "cas douteux. « Trois jours » n'est pas un nombre de fois : "
                      "c'est une durée, et une durée appelle l'imparfait.",
            notes="Le piège de « trois jours » revient chaque année. Le désamorcer "
                  "ici : on ne compte pas les répétitions, on mesure une durée.")

    d.tableau('Le même verbe', "Il change de camp selon ce qu'on veut dire",
              ['La phrase', 'Ce qu\'elle dit'],
              [["La police a fermé la rue à cinq heures.", "Un moment précis : évènement"],
               ["La rue était fermée toute la journée.", "Une situation qui durait : décor"],
               ["Il a plu trois heures.", "Un épisode qui a fini : évènement"],
               ["Il pleuvait depuis trois jours.", "Une durée qui continuait : décor"],
               ["Elle est sortie du sous-sol.", "Un mouvement, une fois : évènement"]],
              cle=1,
              notes="La leçon de la séance tient dans ce tableau : ce n'est pas le "
                    "verbe qui décide, c'est vous. Faire produire une sixième paire "
                    "par le groupe avant de passer à l'exercice.")

    d.pratique('Classement', "Un évènement, ou le décor ?",
               "Pour chaque phrase, dites ce qu'elle fait dans le récit.", [
        ("Le feu a éclaté vers quatre heures du matin.", "un évènement"),
        ("Il ventait fort cette nuit-là.", "le décor"),
        ("Un locataire a cogné à toutes les portes.", "un évènement"),
        ("L'immeuble avait quatre logements et un stationnement.", "le décor"),
        ("Les pompiers sont arrivés huit minutes plus tard.", "un évènement"),
        ("La rivière montait depuis trois jours.", "le décor"),
        ("La Ville a distribué des sacs de sable lundi.", "un évènement"),
        ("Les portes des cabanons n'étaient pas barrées.", "le décor"),
        ("La Croix-Rouge a hébergé onze personnes.", "un évènement"),
        ("Tout le monde dormait dans l'immeuble.", "le décor"),
    ], corrige=True,
       notes="Exercice t1tri de l'activité, à deux tuiles. Faire poser les deux "
             "questions à voix haute pour les trois premières, puis laisser le groupe "
             "aller seul : le réflexe s'installe vite.")

    d.tableau('Le plan du récit', "Quatre temps, et rien de plus",
              ['Le temps', 'Ce qu\'il contient'],
              [["Temps 1", "La nouvelle : ce qui est arrivé, où, quand"],
               ["Temps 2", "Le décor : l'heure, le temps, ce que les gens faisaient"],
               ["Temps 3", "Deux évènements qui se suivent, au passé composé"],
               ["Temps 4", "Ce qui reste : ce qui a changé pour les gens"]],
              cle=0,
              note="C'est le plan de l'exercice t1red, et c'est celui du récit oral "
                   "de la séance E1. Le faire recopier dans le cahier.",
              notes="Faire écrire les quatre phrases en classe, une par une, avec une "
                    "mise en commun après chaque temps. Écrire les quatre d'un coup "
                    "sans arrêt produit toujours un récit désordonné.")

    d.pratique('Écriture', "Racontez-le à quelqu'un qui n'a rien lu",
               "Une phrase complète par temps.", [
        ("TEMPS 1 — ce qui est arrivé, où, quand", "Un immeuble de quatre logements a passé au feu cette nuit, rue Alexandre."),
        ("TEMPS 2 — le décor", "Il était quatre heures du matin et tout le monde dormait."),
        ("TEMPS 3 — deux évènements qui se suivent", "Un locataire s'est réveillé, puis il a cogné à toutes les portes."),
        ("TEMPS 4 — ce qui reste", "Onze personnes n'ont plus de logement, et la Croix-Rouge les a hébergées."),
    ], corrige=True,
       notes="Exercice t1red de l'activité. Les quatre phrases du corrigé sont un "
             "modèle, pas une réponse attendue : chaque élève écrit les siennes. "
             "Faire lire deux récits complets à voix haute avant la fin.")

    d.piege("Raconter tout au passé composé",
            "Il était quatre heures. Le feu a éclaté. Les gens ont dormi. Les pompiers sont arrivés.",
            "Il était quatre heures et tout le monde dormait quand le feu a éclaté.",
            "Un récit tout au passé composé fait une liste : la personne en face "
            "entend des évènements sans arriver à se représenter la scène. Le décor "
            "n'est pas un ornement, c'est ce qui rend l'histoire visible.",
            notes="Faire entendre la version en liste, puis la version à deux temps. "
                  "La différence s'entend en trois secondes et elle vaut mieux que "
                  "toute explication.")

    d.billet(
        "Écrivez les quatre temps de votre récit, une phrase chacun.",
        exemples=[
            "La nouvelle de votre choix : celle du journal, ou une de votre quartier.",
            "Vérifiez qu'il y a au moins un imparfait et deux passés composés.",
        ],
        notes="Fin du défi 1. Ramasser : ces quatre phrases sont la base du récit "
              "oral de E1. Les rendre corrigées avant la séance E1, pas après.")

    return d.save(dossier)
