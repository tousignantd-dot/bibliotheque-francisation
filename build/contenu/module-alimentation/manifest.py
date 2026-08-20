# -*- coding: utf-8 -*-
"""Identité de module-alimentation — « Faire l'épicerie »"""

MANIFESTE = {
    'slug': 'module-alimentation',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # Les apostrophes sont échappées : le gabarit place ce jeton dans une
    # chaîne JavaScript à guillemets simples.
    'theme': "Achat d\\'aliments ou de produits d\\'entretien",

    # Teal : le violet est passé à la marque SAAF, qui le veut exclusif. Les
    # voisins immédiats sont vert (13) et acier (15) ; le teal se distingue des
    # deux.
    'accent': '#8C6A07',
    'accent_doux': '#F7F0DA',

    'ia_oral': "L'élève commande un produit à un comptoir d'épicerie ou "
               "s'informe sur un aliment : il nomme le produit, donne une "
               "quantité avec la bonne unité, emploie les partitifs (du, de "
               "la, des) et le pronom en, et pose une question sur la "
               "provenance ou la conservation.",

    'jr_cas': 'boucherie',
    'jr_role': 'client',
    'jr_scenario': 'epicerie',
    'ia_jeu_de_role': "L'élève commande à un comptoir d'épicerie : il demande "
                      "un produit, précise la quantité, s'informe sur la "
                      "provenance ou la conservation, et vérifie le prix avant "
                      "de repartir.",

    'bravo': "🎉 Bravo, tu as terminé le module « Faire l\\'épicerie » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
