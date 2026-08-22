# -*- coding: utf-8 -*-
"""Identité de module-n3-loisirs — « Choisir une activité au centre » (niveau 3).

Le slug porte le niveau : `module-activite` est déjà pris par le niveau 4, qui
traite la même situation du programme mais bien plus loin — le dépliant, les
consignes du moniteur, le formulaire d'inscription rempli au comptoir.

Ce que `build/cadre.py 3 "Participation à une activité culturelle ou
sportive"` donne au niveau 3 est plus étroit et plus parlé : une intention de
production orale — « demander et comprendre des renseignements pour choisir
une activité » —, la même en compréhension orale, et deux lectures nommées,
« lire une brève description de film dans un téléhoraire » et « lire une
recette », dont les consignes se comprennent aussi à l'oral. D'où trois
défis : se renseigner, choisir un film, suivre une recette. On ne s'inscrit
jamais.
"""

MANIFESTE = {
    'slug': 'module-n3-loisirs',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Participation à une activité culturelle ou sportive',

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève se renseigne sur une activité de loisir dans un centre "
               "communautaire : il dit quelle activité l'intéresse, puis il "
               "demande le jour et l'heure, le tarif, et ce qu'il faut "
               "apporter. Il répète ce qu'on lui répond pour vérifier. Il ne "
               "s'inscrit pas : il se renseigne avant de choisir.",

    'jr_cas': 'badminton',
    'jr_role': 'visiteur',
    'jr_scenario': 'loisirs',
    'ia_jeu_de_role': "L'élève se renseigne au comptoir d'un centre "
                      "communautaire pour choisir une activité : il nomme "
                      "l'activité, demande le jour, l'heure, le prix et ce "
                      "qu'il faut apporter, et il fait répéter ce qu'il n'a "
                      "pas compris.",

    'bravo': "🎉 Bravo, tu as terminé le module « Choisir une activité au centre » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
