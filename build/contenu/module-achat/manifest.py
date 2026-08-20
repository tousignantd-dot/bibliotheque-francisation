# -*- coding: utf-8 -*-
"""Identité de module-achat — « Acheter un appareil »"""

MANIFESTE = {
    'slug': 'module-achat',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Achat de biens de consommation durables',

    # Bleu : les voisins immédiats sont violet (14) et vert (13).
    'accent': '#8C6A07',
    'accent_doux': '#F7F0DA',

    'ia_oral': "L'élève s'informe sur un appareil ménager ou explique celui "
               "qu'il a choisi : il le décrit avec des adjectifs justes, "
               "compare deux modèles, pose des questions sur la garantie, le "
               "paiement et la livraison, et dit quand il sera livré.",

    'jr_cas': 'laveuse',
    'jr_role': 'acheteur',
    'jr_scenario': 'appareil',
    'ia_jeu_de_role': "L'élève s'informe sur un appareil dans un magasin : il "
                      "demande les dimensions, la capacité et la "
                      "consommation, compare deux modèles, puis pose ses "
                      "questions sur la garantie, le paiement et la livraison.",

    'bravo': '🎉 Bravo, tu as terminé le module « Acheter un appareil » !',
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
