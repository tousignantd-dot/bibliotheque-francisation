# -*- coding: utf-8 -*-
"""C3 · Ce qu'on demande aux automobilistes
Bloc C « Défi 2 · Le bulletin de 6 h 50 » · couleur ambre · 75 min.
Source : exercice `t2dir` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Ce qu'on demande aux automobilistes",
        chapeau="Pendant cinquante secondes, le bulletin décrit. Et puis, "
                "deux ou trois fois, il s'adresse à vous. Ces phrases-là sont "
                "les seules qui vous demandent de faire quelque chose : les "
                "reconnaître au passage, c'est savoir quand il faut agir.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire de la consigne. Ouvrir en faisant réécouter le "
                  "bulletin de six heures cinquante et en demandant au groupe de lever "
                  "la main chaque fois qu'on lui parle. Il y a deux occurrences : "
                  "« Empruntez le pont Victoria » et « Prudence dans la voie de droite ».")

    d.objectifs([
        "reconnaître l'impératif du bulletin : empruntez, évitez, prévoyez ;",
        "comprendre les phrases impersonnelles : il faut, il est recommandé de ;",
        "comprendre « on demande aux automobilistes de » ;",
        "employer l'infinitif après « de ».",
    ], notes="Le quatrième objectif est le seul point de forme de la séance, et c'est "
             "l'erreur la plus fréquente : après « de », le verbe ne se conjugue jamais.")

    d.regle("Trois façons de dire la même consigne",
            "L'impératif commande. « Il est recommandé » conseille. « On "
            "demande aux automobilistes » rapporte.",
            precision="Quand vous répétez une directive à quelqu'un, la forme "
                      "rapportée est la plus naturelle : « Ils disent d'emprunter "
                      "le pont Victoria. »",
            notes="Diapositive à photographier. La forme rapportée servira en E1 : elle "
                  "dit clairement que la consigne ne vient pas de vous.")

    d.tableau('La même consigne', "De la plus forte à la plus indirecte",
              ['La forme', 'Ce que ça donne'],
              [["Impératif", "Évitez le secteur."],
               ["Il est recommandé de", "Il est recommandé d'éviter."],
               ["Il faut", "Il faut éviter le secteur."],
               ["On demande de", "On demande d'éviter le secteur."]],
              cle=1,
              notes="Faire dire les quatre à voix haute, l'une après l'autre. Le groupe "
                    "entend tout de suite que la première est un ordre et la dernière "
                    "une information.")

    d.cartes("Le « il » qui ne remplace personne", "Les phrases impersonnelles", [
        ("Il est recommandé de…",
         "Personne ne commande : c'est ce qui la rend polie."),
        ("Il faut prévoir…",
         "La consigne existe, sans auteur nommé."),
        ("Il y a un ralentissement",
         "Le même « il », comme dans « il pleut »."),
        ("Il reste une voie ouverte",
         "Encore lui : rien ne remplace ce « il »."),
    ], notes="Le « il » impersonnel surprend souvent : les élèves cherchent qui il "
             "désigne. Comparer avec « il pleut » règle la question en une phrase.")

    d.piege("Conjuguer le verbe après « de »",
            "On demande aux automobilistes de vous ralentissez.",
            "On demande aux automobilistes de ralentir.",
            "Après « de », le verbe reste à l'infinitif : de ralentir, d'éviter, "
            "de prévoir, de laisser passer. Aucune exception.",
            notes="Faire produire cinq phrases sur ce moule, à la chaîne, jusqu'à ce que "
                  "l'infinitif vienne tout seul. C'est mécanique, et ça s'automatise "
                  "vite.")

    d.piege("Comprendre « emprunter » au sens de l'argent",
            "Emprunter le pont, c'est payer pour passer ?",
            "Emprunter une route, c'est la prendre.",
            "C'est un mot du métier, comme « entrave » : il ne s'emploie presque "
            "jamais dans ce sens ailleurs. Le bulletin l'utilise tous les jours.",
            notes="Faux ami interne au français : le mot existe dans une autre "
                  "acception connue des élèves. Le signaler évite un contresens complet "
                  "sur la directive la plus importante du bulletin.")

    d.pratique('Transformation', "Récrivez la directive",
               "Employez la tournure demandée.", [
        ("Il faut emprunter le pont Victoria. (impératif)", "Empruntez le pont Victoria."),
        ("Il est recommandé d'éviter le secteur. (impératif)", "Évitez le secteur."),
        ("Prévoyez vingt minutes de plus. (il est recommandé de)", "Il est recommandé de prévoir vingt minutes de plus."),
        ("Réduisez votre vitesse. (on demande de)", "On demande aux automobilistes de réduire leur vitesse."),
        ("Laissez passer les véhicules d'urgence. (il faut)", "Il faut laisser passer les véhicules d'urgence."),
    ], corrige=True,
       notes="Faire remarquer le changement de possessif dans la quatrième : « votre » "
             "devient « leur », parce qu'on ne parle plus à la même personne. C'est "
             "subtil et personne ne le voit seul.")

    d.billet(
        "Écrivez une consigne de sécurité de votre travail, dans les trois formes.",
        exemples=[
            "Portez vos gants. Il faut porter des gants. On demande de porter des gants.",
            "N'importe quelle consigne fait l'affaire : la route n'est qu'un exemple.",
        ],
        notes="Ramasser les billets. Les trois formes servent partout — au travail, à "
              "l'école, dans un mode d'emploi — et c'est ce qui rend la séance "
              "rentable au-delà du module.")

    return d.save(dossier)
