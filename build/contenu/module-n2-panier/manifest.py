# -*- coding: utf-8 -*-
"""Identité de module-n2-panier — « Remplir mon panier » (niveau 2).

Troisième module court du dépôt, deuxième du niveau 2 : huit séances, deux
défis. La situation du programme est « Achat d'aliments ou de produits
d'entretien », dont l'unique intention est en compréhension écrite — lire une
circulaire, une étiquette, une affichette pour y repérer un prix et une
mesure.

Distinct de `module-n3-epicerie` (niveau 3), où l'on trouve, on choisit et on
paie, et de `module-alimentation` (niveau 4) : ici on ne parle presque pas, on
lit des chiffres et des formats avant de remplir son panier.
"""

MANIFESTE = {
    'slug': 'module-n2-panier',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Achat d\\'aliments ou de produits d\\'entretien",

    'accent': '#A83A22',
    'accent_doux': '#FBEAE4',

    'ia_oral': "L'élève fait ses courses : il demande où se trouve un produit, "
               "combien il coûte, dans quel format il est vendu, et il répète "
               "le prix qu'on lui dit pour vérifier. Phrases très courtes, au "
               "présent.",

    'jr_cas': 'trouver',
    'jr_role': 'client',
    'jr_scenario': 'panier',
    'ia_jeu_de_role': "L'élève cherche un produit dans une épicerie de "
                      "quartier : il demande l'allée, le prix et le format, "
                      "et il fait répéter au besoin.",

    'bravo': "🎉 Bravo, tu as terminé le module « Remplir mon panier » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
