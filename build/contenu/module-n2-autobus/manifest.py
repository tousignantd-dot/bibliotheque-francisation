# -*- coding: utf-8 -*-
"""Identité de module-n2-autobus — « Prendre l'autobus » (niveau 2).

Deuxième module court : huit séances, deux défis. Distinct de
`module-deplacement` (niveau 4), qui porte sur le trajet complet et le métro ;
ici, on demande son chemin et on lit un horaire d'autobus.
"""

MANIFESTE = {
    'slug': 'module-n2-autobus',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Déplacement dans une ville',

    'accent': '#A83A22',
    'accent_doux': '#FBEAE4',

    'ia_oral': "L'élève demande son chemin ou une information sur un autobus : "
               "il dit où il veut aller, comprend une direction simple, "
               "demande l'arrêt, l'heure du prochain passage et la "
               "correspondance.",

    'jr_cas': 'chemin',
    'jr_role': 'passager',
    'jr_scenario': 'autobus',
    'ia_jeu_de_role': "L'élève cherche son chemin dans une ville qu'il connaît "
                      "mal : il demande où se trouve un lieu, quel autobus "
                      "prendre, et à quelle heure il passe.",

    'bravo': "🎉 Bravo, tu as terminé le module « Prendre l\\'autobus » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
