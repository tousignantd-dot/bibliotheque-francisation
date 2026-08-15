# -*- coding: utf-8 -*-
"""A2 · Les deux façons de dire « eu » : [ø] et [œ].
Bloc A · couleur violet (graphie-phonie) · 60 min.
Source : mini-leçon `prPhon`, exercice `prPhon`, phrases porteuses du module.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='violet',
        titre="Les deux façons de dire « eu »",
        chapeau="Le vocabulaire du logement est saturé de mots en -eur et en -eux : "
                "une odeur, la chaleur, un couvreur, coûteux, dangereux. Deux sons "
                "se cachent derrière ces deux lettres, et c'est la fin du mot écrit "
                "qui dit lequel prononcer.",
        duree='60 minutes')

    d.titre(notes="Séance de graphie-phonie. Prévoir de faire beaucoup répéter : "
                  "c'est une séance où l'on parle plus qu'on n'écrit.")

    d.objectifs([
        "entendre la différence entre le [ø] de « deux » et le [œ] de « peur » ;",
        "prononcer correctement les mots du logement qui finissent en -eur et en -eux ;",
        "savoir lequel des deux sons dire en regardant seulement la fin du mot écrit.",
    ])

    d.declencheur('Écoute', "Est-ce que ces deux mots riment ?", pistes=[
        "dangereux",
        "couvreur",
        "Les deux s'écrivent avec « eu ». Est-ce qu'ils se prononcent pareil ?",
        "Écoutez encore une fois. Où sentez-vous votre bouche s'ouvrir davantage ?",
    ], notes="Prononcer les deux mots lentement, deux fois. Ne pas donner la réponse : "
             "laisser le groupe hésiter. Beaucoup de langues n'ont qu'un seul de ces "
             "deux sons — l'hésitation est normale et vaut la peine d'être nommée.")

    d.regle('La règle',
            "C'est la fin du mot écrit qui décide, pas l'oreille.",
            precision="Regardez la dernière lettre prononcée. Si le son « eu » est le dernier "
                      "son du mot, c'est [ø], bouche presque fermée. S'il reste une consonne à "
                      "prononcer après, c'est [œ], bouche nettement plus ouverte. Cette règle "
                      "règle à elle seule la grande majorité des cas.",
            notes="Écrire les deux terminaisons au tableau et les y laisser toute la séance.")

    d.tableau('Analyse', "Le son fermé [ø]",
              ['Fin du mot', 'Se dit', 'Comme dans'],
              [['-eu', '[ø]', 'peu'],
               ['-eux', '[ø]', 'deux, dangereux, coûteux'],
               ['-ieu', '[ø]', 'milieu, vieux']],
              note="Astuce : les adjectifs en -eux tombent tous dans cette famille. "
                   "Dangereux, coûteux, silencieux, ennuyeux — tous en [ø].",
              cle=1,
              notes="Faire répéter la colonne de droite trois fois, de plus en plus vite. "
                    "Insister sur la bouche presque fermée et les lèvres avancées.")

    d.tableau('Analyse', "Le son ouvert [œ]",
              ['Fin du mot', 'Se dit', 'Comme dans'],
              [['-eur', '[œ]', 'odeur, chaleur, ascenseur, couvreur'],
               ['-euf', '[œ]', 'neuf'],
               ['-eul', '[œ]', 'seul'],
               ['-eu + consonne', '[œ]', 'immeuble, jeune']],
              note="La terminaison -eur est partout dans le vocabulaire du logement : elle "
                   "sert aux métiers (un couvreur, un ascenseur) comme aux sensations "
                   "(une odeur, la chaleur, la peur).",
              cle=1,
              notes="Faire exagérer l'ouverture de la bouche. C'est le son le plus difficile "
                    "des deux pour la plupart des groupes.")

    d.piege('Prononciation',
            "dangereux et couvreur riment.",
            "dangereux se dit [ø], couvreur se dit [œ].",
            "Les deux mots s'écrivent avec « eu », mais dans dangereux le x est muet — plus "
            "aucune consonne ne se prononce, donc [ø]. Dans couvreur, le r se prononce, "
            "donc [œ]. Même orthographe, deux sons différents : c'est la consonne finale "
            "qui tranche, jamais l'orthographe des lettres « eu » elles-mêmes.",
            notes="C'est le point à retenir de toute la séance. Le faire dire par trois élèves.")

    d.cartes('Prononciation', "Comment placer sa bouche", [
        ("Le [ø] de « deux »",
         "Bouche presque fermée. Les lèvres s'arrondissent et avancent, comme pour siffler. "
         "La langue reste en avant. Le son est court et tenu."),
        ("Le [œ] de « peur »",
         "Bouche nettement plus ouverte, d'environ un doigt. Les lèvres restent arrondies "
         "mais moins avancées. La mâchoire descend."),
        ("L'exercice du miroir",
         "Dites « deux — peur — deux — peur » devant un miroir. Vous devez voir votre "
         "mâchoire descendre à chaque « peur »."),
        ("Si vous hésitez à l'oral",
         "Pensez au mot écrit. Vous n'avez pas besoin d'entendre la différence pour la "
         "produire : il suffit de regarder la fin du mot."),
    ], notes="Faire faire l'exercice du miroir avec la main sous le menton, à défaut de "
             "miroir : on sent la mâchoire descendre.")

    d.pratique('Pratique', '[ø] ou [œ] ?',
               "Écoutez le mot, puis indiquez le son que vous entendez.", [
        ("deux", "[ø] — rien ne se prononce après"),
        ("odeur", "[œ] — le r se prononce"),
        ("dangereux", "[ø] — le x est muet"),
        ("chaleur", "[œ] — le r se prononce"),
        ("immeuble", "[œ] — le b et le l se prononcent"),
        ("milieu", "[ø] — rien ne se prononce après"),
    ], corrige=True, cols=2,
       notes="Prononcer chaque mot deux fois, sans le montrer. Le groupe répond à main levée "
             "avant l'affichage de la correction.")

    d.pratique('Pratique', 'Suite',
               "Même consigne. Ces six mots sont plus difficiles.", [
        ("ascenseur", "[œ]"),
        ("coûteux", "[ø]"),
        ("couvreur", "[œ]"),
        ("peu", "[ø]"),
        ("jeune", "[œ]"),
        ("vieux", "[ø]"),
    ], corrige=True, cols=2,
       notes="« Jeune » surprend souvent : il n'y a ni -eur ni -eux, mais deux consonnes se "
             "prononcent après le « eu », donc [œ].")

    d.pratique('Pratique', 'Des phrases entières',
               "Lisez la phrase à voix haute. Attention aux mots soulignés par le contexte.", [
        ("Le couvreur répare la toiture.", "couvr[œ]r"),
        ("Ce genre de travaux est coûteux.", "coût[ø]"),
        ("Une odeur monte par l'escalier.", "od[œ]r"),
        ("Le disjoncteur est arrêté au milieu.", "disjonct[œ]r, mili[ø]"),
        ("Ce fil électrique est dangereux.", "dangere[ø]"),
        ("L'ascenseur est en panne depuis lundi.", "ascens[œ]r"),
    ], corrige=True,
       notes="Chaque phrase est lue par un élève différent, puis par le groupe entier. "
             "Ce sont les phrases porteuses du module : elles reviendront dans les "
             "exercices en ligne.")

    d.billet(
        "Écrivez deux mots du logement : un qui se dit [ø], un qui se dit [œ].",
        exemples=[
            "Soulignez la terminaison qui vous a permis de décider.",
            "Vous n'avez pas le droit d'utiliser « deux » ni « peur ».",
        ],
        notes="Les billets révèlent immédiatement qui a compris la règle écrite et qui devine "
              "encore à l'oreille.")

    return d.save(dossier)
