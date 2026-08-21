# -*- coding: utf-8 -*-
"""Identité de module-n2-bonjour — « Bonjour, ça va ? » (niveau 2).

Quatrième module court du dépôt, troisième du niveau 2 : huit séances, deux
défis. La situation du programme est « Relations sociales ». Ses cinq
intentions tiennent l'ensemble : comprendre une demande d'aide (CO), décrire
ses activités quotidiennes (PO), comprendre des souhaits ou des remerciements
et choisir une carte de vœux (CE), rédiger des souhaits et des remerciements
simples (PE).

Distinct de `module-n1-presenter` (niveau 1), qui apprend à dire son nom, et
de `module-relations` (niveau 4), qui tient une conversation suivie et raconte
au passé : ici on entre dans un échange de deux ou trois répliques avec
quelqu'un qu'on recroisera demain matin dans l'entrée de l'immeuble.
"""

MANIFESTE = {
    'slug': 'module-n2-bonjour',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Relations sociales",

    'accent': '#A83A22',
    'accent_doux': '#FBEAE4',

    'ia_oral': "L'élève salue un voisin qu'il croise souvent : il dit bonjour, "
               "demande comment ça va, répond, dit deux ou trois choses qu'il "
               "fait dans sa journée, puis prend congé. Phrases très courtes, "
               "au présent. Le vouvoiement doit être tenu du début à la fin.",

    'jr_cas': 'entree',
    'jr_role': 'moi',
    'jr_scenario': 'bonjour',
    'ia_jeu_de_role': "L'élève croise une voisine dans son immeuble : il salue, "
                      "répond à « ça va ? », dit ce qu'il fait de sa journée, "
                      "comprend une demande d'aide, remercie et prend congé.",

    'bravo': "🎉 Bravo, tu as terminé le module « Bonjour, ça va ? » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
