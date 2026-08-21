# -*- coding: utf-8 -*-
"""Identité de module-n3-vetements — « Magasiner du linge » (niveau 3).

Le slug porte le niveau : `module-vetements` est déjà pris par le niveau 4,
qui traite la même situation du programme mais bien plus loin — essayage,
avis, entretien, échange et remboursement. Ici, les deux seules intentions
du niveau 3 sont « s'informer sur un vêtement » et « lire une étiquette » :
nommer, demander, comparer deux prix.
"""

MANIFESTE = {
    'slug': 'module-n3-vetements',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Achat de vêtements',

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève magasine du linge : il nomme le vêtement qu'il "
               "cherche, dit sa couleur et sa taille, demande à l'essayer, "
               "puis compare le prix de deux articles à voix haute.",

    'jr_cas': 'manteau',
    'jr_role': 'client',
    'jr_scenario': 'linge',
    'ia_jeu_de_role': "L'élève achète un vêtement dans un magasin : il dit ce "
                      "qu'il cherche, donne sa taille, demande où est la "
                      "cabine d'essayage et compare deux prix avant de "
                      "choisir.",

    'bravo': "🎉 Bravo, tu as terminé le module « Magasiner du linge » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
