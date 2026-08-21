# -*- coding: utf-8 -*-
"""Identité de module-n6-recherche — « Chercher un emploi » (niveau 6).

Le slug porte le niveau, et il nomme le scénario plutôt que la situation du
programme : « Emploi » est la situation retenue pour le niveau 8, et
`module-n6-emploi` s'en serait trop rapproché.
"""

MANIFESTE = {
    'slug': 'module-n6-recherche',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Recherche d\\'emploi",

    # Acier : la couleur du niveau 6. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#1D6B8F',
    'accent_doux': '#E7F0F6',

    'ia_oral': "L'élève offre ses services à un employeur : il se présente, "
               "résume son parcours, décrit ses tâches passées avec des "
               "exemples précis, dit ce qu'il sait faire et pose une question "
               "sur le poste. Il vouvoie son interlocuteur.",

    'jr_cas': 'inventaire',
    'jr_role': 'candidat',
    'jr_scenario': 'entrevue',
    'ia_jeu_de_role': "L'élève passe une courte entrevue d'embauche : il "
                      "répond à des questions ouvertes sur son expérience et "
                      "sa formation, développe ses réponses avec des "
                      "exemples, et pose à son tour une question sur le "
                      "poste.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Chercher un emploi » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
