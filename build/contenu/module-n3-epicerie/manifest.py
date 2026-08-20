# -*- coding: utf-8 -*-
"""Identité de module-n3-epicerie — « À l'épicerie » (niveau 3).

Le slug porte le niveau : la même situation du programme revient à plusieurs
niveaux, et `module-alimentation` est déjà pris par le niveau 4.
"""

MANIFESTE = {
    'slug': 'module-n3-epicerie',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Achat d\\'aliments ou de produits d\\'entretien",

    # Forêt : le module d'alimentation du niveau 4 est teal, et les deux
    # peuvent se retrouver côte à côte dans le catalogue.
    'accent': '#166534',
    'accent_doux': '#DCF0E1',

    'ia_oral': "L'élève cherche un produit dans une épicerie : il demande où "
               "il se trouve, demande de l'aide, s'informe sur un format ou "
               "un prix, et donne les renseignements qu'on lui demande à la "
               "caisse.",

    'jr_cas': 'farine',
    'jr_role': 'client',
    'jr_scenario': 'allees',
    'ia_jeu_de_role': "L'élève cherche un produit dans une grande épicerie : "
                      "il demande dans quelle allée il se trouve, fait "
                      "répéter s'il n'a pas compris, et s'informe sur le "
                      "format ou sur le prix.",

    'bravo': "🎉 Bravo, tu as terminé le module « À l\\'épicerie » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
