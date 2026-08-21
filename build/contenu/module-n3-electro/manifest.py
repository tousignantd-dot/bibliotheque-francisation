# -*- coding: utf-8 -*-
"""Identité de module-n3-electro — « Acheter un appareil » (niveau 3).

La situation du programme est « Achat de biens de consommation durables ».
Au niveau 3, elle n'a **qu'une seule intention de communication**, et elle est
en compréhension écrite : « Lire des circulaires, des catalogues, des
affichettes et des sites d'achats en ligne ». Le module est donc construit
autour du papier et de l'écran — la circulaire du mardi, l'affichette du
rayon, la fiche du site — et l'oral y sert à demander ce que le papier ne dit
pas : où est le rayon, combien ça coûte, quand ça se livre.

C'est ce qui le sépare de `module-achat` (niveau 4), qui fait comparer deux
appareils, lire une garantie et se faire rembourser. Ici : lire, trouver,
demander, payer, faire livrer.
"""

MANIFESTE = {
    'slug': 'module-n3-electro',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Achat de biens de consommation durables',

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève achète un appareil dans un magasin : il nomme "
               "l'appareil qu'il cherche, demande où est le rayon, demande le "
               "prix et s'il est en spécial, puis demande la livraison en "
               "donnant un jour.",

    'jr_cas': 'laveuse',
    'jr_role': 'client',
    'jr_scenario': 'electro',
    'ia_jeu_de_role': "L'élève achète un appareil au magasin : il dit quel "
                      "appareil il cherche, demande le rayon, demande le prix "
                      "et le spécial de la circulaire, puis demande la "
                      "livraison.",

    'bravo': "🎉 Bravo, tu as terminé le module « Acheter un appareil » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
