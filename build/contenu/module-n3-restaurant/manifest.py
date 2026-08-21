# -*- coding: utf-8 -*-
"""Identité de module-n3-restaurant — « Commander au comptoir » (niveau 3).

La situation du programme est « Service de restauration ». Au niveau 3, elle
tient en **trois intentions**, et elles sont étroites : « commander au
comptoir et comprendre l'information donnée par le préposé » (en compréhension
orale comme en production orale) et « lire un menu simple » (en compréhension
écrite). Le lexique que le programme donne à cette situation tient lui aussi
en deux entrées : les **types de formats**, et les **ustensiles, serviettes de
table et condiments**.

Le module est donc bâti sur un comptoir de casse-croûte, jamais sur une salle
à manger : on lit le tableau au-dessus de la caisse, on commande un format, on
comprend ce que le préposé demande en retour — « pour ici ou pour emporter ? »
— et on demande ce qui manque sur le plateau.

C'est ce qui le sépare de `module-restaurant` (activité 53, niveau 4), qui
tient le repas complet : la table d'hôte, le service aux tables, ce qu'on
demande pendant le repas, l'addition, les taxes et le pourboire. Ici, il n'y a
ni serveur, ni addition, ni pourboire — il y a une file, un tableau, un
plateau et un numéro qu'on appelle.
"""

MANIFESTE = {
    'slug': 'module-n3-restaurant',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Service de restauration',

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève commande un repas au comptoir d'un casse-croûte : il "
               "salue, il nomme ce qu'il veut, il choisit un format, il "
               "répond à « pour ici ou pour emporter ? », puis il demande un "
               "condiment ou un ustensile qui manque.",

    'jr_cas': 'trio',
    'jr_role': 'client',
    'jr_scenario': 'comptoir',
    'ia_jeu_de_role': "L'élève commande au comptoir d'un casse-croûte : il "
                      "dit ce qu'il veut, il choisit un format, il répond aux "
                      "questions du préposé, puis il demande ce qui manque "
                      "sur son plateau.",

    'bravo': "🎉 Bravo, tu as terminé le module « Commander au comptoir » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
