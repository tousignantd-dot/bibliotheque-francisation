# -*- coding: utf-8 -*-
"""B4 · Matin ou après-midi ?
Bloc B « Défi 1 · Mon quart commence à quelle heure ? » · couleur acier · 50 min.
Source : exercice `t1ecoute`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='acier',
        titre="Matin ou après-midi ?",
        chapeau="Une heure entendue au téléphone ou dans le bruit d'une "
                "cuisine se rattrape mal. Cette séance entraîne l'oreille "
                "à placer l'heure dans la journée, sans la voir écrite.",
        duree='50 minutes')

    d.titre(notes="Séance d'écoute, dernière du défi 1. Demander d'abord si quelqu'un a "
                  "posé une de ses questions de B3 au travail cette semaine — et ce que "
                  "la réponse a donné.")

    d.objectifs([
        "reconnaître une heure entendue et la placer dans la journée ;",
        "entendre la différence entre treize et trente, quinze et cinquante ;",
        "redire l'heure entendue pour la vérifier ;",
        "demander de répéter sans se sentir mal à l'aise.",
    ])

    d.pratique('Écoute', "Le matin, ou l'après-midi ?",
               "Écoutez chaque heure et placez-la dans la journée.", [
        ("six heures", "le matin"),
        ("quatorze heures", "l'après-midi"),
        ("sept heures et demie", "le matin"),
        ("seize heures", "l'après-midi"),
        ("onze heures et quart", "le matin"),
        ("quinze heures moins dix", "l'après-midi"),
        ("huit heures moins cinq", "le matin"),
        ("dix-sept heures", "l'après-midi"),
    ], corrige=True,
       notes="C'est l'exercice `t1ecoute` du module interactif, mot pour mot. Le faire "
             "livre fermé. Les heures au-dessus de douze sont faciles ; les autres "
             "demandent d'écouter jusqu'au bout de la phrase.")

    d.tableau('Analyse', "Les paires qui se confondent",
              ["On entend", "Ou bien"],
              [["treize heures", "trente"],
               ["quinze heures", "cinquante"],
               ["seize heures", "soixante"],
               ["deux heures", "douze heures"]],
              cle=1,
              note="C'est la fin du mot qui décide. En cas de doute, on "
                   "redit l'heure à voix haute : « treize heures, c'est bien "
                   "ça ? »",
              notes="Diapo à photographier. La dernière ligne est celle qui coûte le plus "
                    "cher : arriver à midi pour un quart de deux heures, ou l'inverse. "
                    "Insister.")

    d.regle("Redire pour vérifier",
            "— Vous commencez à six heures. — À six heures, c'est bien ça ?",
            precision="Trois secondes, et l'erreur est écartée. Ce n'est ni "
                      "impoli ni un aveu d'incompréhension : les employés "
                      "d'expérience le font tout le temps, dans toutes les "
                      "langues.",
            notes="Diapo à photographier. C'est le geste central du module, et il "
                  "reviendra au défi 3 avec les consignes. Le faire pratiquer à deux, "
                  "cinq minutes, sur des heures inventées.")

    d.pratique('Écoute', "Deux par deux : dites, redites, vérifiez",
               "L'un donne une heure, l'autre la redit pour vérifier.", [
        ("« Vous commencez à treize heures. »", "« À treize heures, c'est bien ça ? »"),
        ("« La pause est à onze heures et demie. »", "« Onze heures et demie, d'accord. »"),
        ("« Vous finissez à quinze heures. »", "« Quinze heures — trois heures, c'est ça ? »"),
        ("« Miguel entre à quatorze heures. »", "« Deux heures de l'après-midi ? »"),
        ("« Le four à onze heures. »", "« Onze heures pile ? »"),
    ], corrige=False, cols=1,
       notes="Quinze minutes, puis on inverse. Insister pour que celui qui répond "
             "reformule au lieu de répéter : « quinze heures — trois heures » montre "
             "qu'on a vraiment compris.")

    d.piege("Faire semblant d'avoir compris",
            "— Vous commencez à treize heures. — Oui, oui, d'accord.",
            "— Vous commencez à treize heures. — Excusez-moi, vous pouvez répéter ?",
            "Un « oui, oui » qui cache un doute coûte une journée de travail. "
            "Faire répéter coûte trois secondes. Personne, dans une cuisine, "
            "n'a jamais été renvoyé pour avoir demandé de répéter.",
            notes="Le dire franchement : beaucoup d'élèves ont peur de passer pour "
                  "quelqu'un qui ne comprend pas le français. C'est la peur qui fait "
                  "manquer les quarts, pas le niveau de langue.")

    d.billet(
        "Notez les heures de votre semaine, en lettres.",
        exemples=[
            "Sans regarder les chiffres pendant que vous écrivez.",
            "« Lundi : de six heures à deux heures de l'après-midi. »",
        ],
        notes="Devoir court. C'est le dernier travail du défi 1 : après ça, l'élève sait "
              "lire son horaire, le dire, et demander ce qu'il n'a pas compris.")

    return d.save(dossier)
