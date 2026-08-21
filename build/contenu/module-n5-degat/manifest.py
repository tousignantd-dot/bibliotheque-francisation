# -*- coding: utf-8 -*-
"""Identité de module-n5-degat — « Un dégât d'eau » (niveau 5).

Le slug porte le niveau : `module-probleme` est pris par le niveau 4, qui
traite la même situation du programme d'une tout autre façon. Là-bas, on
signale un problème au propriétaire par téléphone et l'affaire s'arrête à la
promesse de réparation. Ici, on décrit un sinistre, on raconte au passé ce qui
s'est passé pendant la nuit, on lit l'avis de travaux affiché dans l'entrée —
la seule intention que le programme donne à cette situation au niveau 5 : lire
un avis — et on argumente jusqu'au bout : réduction de loyer et réclamation
d'assurance.
"""

MANIFESTE = {
    'slug': 'module-n5-degat',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Problèmes reliés à l\\'habitation",

    # Sarcelle : la couleur du niveau 5. Posée par build/couleurs_niveau.py,
    # qui la relit dans colors.css — ne pas la choisir à la main.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève raconte un dégât survenu chez lui : il dit ce qu'il a "
               "vu et quand, il relate au passé composé et à l'imparfait ce "
               "qui s'est passé, il nomme les dommages pièce par pièce, il "
               "dit ce qu'il a déjà fait, et il termine par une demande "
               "claire assortie d'une raison.",

    'jr_cas': 'plafond',
    'jr_role': 'locataire',
    'jr_scenario': 'degat',
    'ia_jeu_de_role': "L'élève signale un dégât d'eau et mène la démarche "
                      "jusqu'au bout : il décrit les dommages avec précision, "
                      "raconte ce qui s'est passé, dit ce qui est devenu "
                      "inutilisable, demande une date d'intervention et une "
                      "compensation, et justifie sa demande.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Un dégât d\\'eau » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
