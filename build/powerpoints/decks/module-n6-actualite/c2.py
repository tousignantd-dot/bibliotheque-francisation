# -*- coding: utf-8 -*-
"""C2 · Le plus-que-parfait : ce qui s'était passé avant
Bloc C « Défi 2 · L'entrevue et le documentaire » · couleur ambre · 75 min.
Source : exercice `t2pqp` et sa mini-leçon « Le plus-que-parfait : ce qui
s'était passé avant ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Le plus-que-parfait : ce qui s'était passé avant",
        chapeau="« Ils avaient jeté l'appareil avant de nous appeler. » "
                "D'abord jeter, ensuite appeler - et pourtant c'est appeler "
                "qui porte le récit. Un seul auxiliaire change tout l'ordre "
                "des événements.",
        duree='75 minutes')

    d.titre(notes="Deuxième séance du Défi 2. Commencer par relire la première page de "
                  "l'entrevue et faire compter les plus-que-parfaits : il y en a "
                  "quatre. Le groupe les a entendus sans les voir.")

    d.objectifs([
        "reconnaître un plus-que-parfait à l'oral ;",
        "le former avec avoir ou être à l'imparfait et un participe passé ;",
        "reconnaître les mots qui l'annoncent : déjà, avant, la veille ;",
        "rétablir l'ordre réel des événements dans un récit.",
    ], notes="Le quatrième objectif est le seul qui compte vraiment pour la "
             "compréhension. Les trois autres le servent.")

    d.declencheur(
        'Observation', "Qu'est-ce qui est arrivé en premier ?",
        pistes=[
            "« Ils avaient jeté l'appareil avant de nous appeler. »",
            "Jeter ou appeler : lequel vient d'abord ?",
            "« Ils l'avaient remplacé, ils avaient payé deux fois. »",
            "Quel mot, dans la phrase, dit que c'était déjà fait ?",
        ],
        notes="La quatrième question n'a pas de réponse simple : aucun mot ne le dit, "
              "c'est le temps du verbe. C'est exactement pourquoi ce temps est "
              "difficile à entendre.")

    d.tableau('Analyse', "Deux temps, deux moments",
              ['La phrase', 'Ce qui s\'est passé quand'],
              [["Ils ont appelé l'Office.", "l'action que le récit raconte"],
               ["Ils avaient jeté l'appareil.", "avant l'appel, et déjà terminé"],
               ["Elle était partie avant l'audience.", "avant l'audience, et déjà terminé"],
               ["Elle est partie après l'audience.", "après, dans la suite du récit"]],
              cle=0,
              note="Le plus-que-parfait recule d'un cran : il dit ce qui était déjà fait au moment raconté.",
              notes="Diapositive à photographier. Dessiner une ligne du temps au tableau "
                    "avec deux points : c'est plus efficace que n'importe quelle "
                    "explication verbale.")

    d.regle("Comment il se forme",
            "Avoir ou être à l'imparfait, plus le participe passé.",
            precision="J'avais compris. Elle était partie. Nous avions écrit. "
                      "L'auxiliaire ne change jamais de camp : si tu dis « je suis "
                      "parti », tu diras « j'étais parti » ; si tu dis « j'ai écrit », "
                      "tu diras « j'avais écrit ». Il n'y a donc rien de nouveau à "
                      "apprendre, sinon l'imparfait de deux verbes.",
            notes="Diapositive à photographier. Rassurer le groupe : c'est le temps "
                  "composé le moins coûteux à apprendre, puisque tout est déjà connu.")

    d.cartes("Les mots qui l'annoncent", "Dès que tu les entends, attends-toi au plus-que-parfait", [
        ("déjà",
         "« ils avaient déjà payé » : l'action est terminée avant le récit."),
        ("avant, avant de",
         "« avant de nous appeler » : ce qui précède est au plus-que-parfait."),
        ("la veille, l'année d'avant",
         "un repère de temps qui recule d'un cran."),
        ("jusque-là, auparavant",
         "plus écrits, très fréquents dans les entrevues et les documentaires."),
    ], notes="Quatre cartes, à copier. Ce sont des indices d'écoute : l'élève n'a pas à "
             "analyser le verbe s'il a entendu l'un de ces mots.")

    d.pratique('Grammaire', "Mettez le verbe au plus-que-parfait",
               "Le verbe entre parenthèses recule d'un cran.", [
        ("Ils l'ont remplacé parce qu'ils ... (renoncer) à se plaindre.", "avaient renoncé"),
        ("Elle a téléphoné à l'Office, mais elle ... (jeter) l'appareil la veille.", "avait jeté"),
        ("Le commerçant a rappelé six jours après qu'il ... (recevoir) la lettre.", "avait reçu"),
        ("Nadège ne savait pas ce que Raphaël lui ... (expliquer) le matin même.", "avait expliqué"),
        ("Elle a gagné son point parce qu'elle ... (garder) toutes ses preuves.", "avait gardé"),
        ("Ils ont payé deux fois : ils ... (acheter) un appareil neuf avant d'appeler.", "avaient acheté"),
    ], corrige=True, cols=2,
       notes="Tous prennent avoir. Prévoir une question sur le participe accordé : ici "
             "il n'y en a aucun, et le dire évite qu'on en invente.")

    d.piege("Entendre un passé composé à la place",
            "Il a payé la facture avant de nous appeler.",
            "Il avait payé la facture avant de nous appeler.",
            "Les deux phrases ne diffèrent que par deux syllabes, et pourtant l'ordre "
            "des événements n'est pas le même. Le plus-que-parfait n'ajoute aucun mot : "
            "il change seulement l'auxiliaire de temps. C'est ce qui le rend si "
            "difficile à entendre - et c'est pourquoi les mots comme « déjà » ou "
            "« avant » sont plus utiles que le verbe lui-même.",
            notes="Faire écouter les deux phrases lues à voix haute, deux fois chacune, "
                  "sans dire laquelle est laquelle. Le groupe doit les distinguer à "
                  "l'oreille avant de les analyser.")

    d.pratique('Compréhension', "Qu'est-ce qui est arrivé en premier ?",
               "Dites quelle action précède l'autre.", [
        ("Ils avaient jeté l'appareil avant de nous appeler.", "jeter, puis appeler"),
        ("Le commerçant a rappelé six jours après avoir reçu la lettre.", "recevoir, puis rappeler"),
        ("Quand les chercheurs ont publié, l'entente avait fini depuis longtemps.", "l'entente finit, puis la publication"),
        ("Elle a gardé la facture, puis elle a écrit sa lettre.", "garder, puis écrire"),
        ("Le technicien est reparti : la pièce n'était pas encore arrivée.", "la pièce n'arrive pas, puis il repart"),
    ], corrige=True,
       notes="Exercice de compréhension pure, sans conjugaison. C'est celui qui compte "
             "pour l'écoute : le faire lentement, en dessinant chaque fois la ligne du "
             "temps au tableau.")

    d.billet(
        "Écris une phrase avec « avant de » et un plus-que-parfait.",
        exemples=[
            "Sur ta propre semaine, si tu veux.",
            "Par exemple : « J'avais déjà mangé avant de partir. »",
        ],
        notes="Deux minutes. C'est le temps qu'on retrouve dans le compte rendu oral de "
              "E1, dès qu'un élève raconte ce qu'il avait fait avant d'écouter la "
              "chronique.")

    return d.save(dossier)
