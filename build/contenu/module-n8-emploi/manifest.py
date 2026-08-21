# -*- coding: utf-8 -*-
"""Identité de module-n8-emploi — « Tenir son bout au travail » (niveau 8).

Le slug porte le niveau et nomme le scénario plutôt que la situation du
programme. La situation, elle, est « Emploi » : la plus dense des six du
niveau 8, avec dix intentions de communication.

Nadia Kessab est adjointe administrative chez Portes et fenêtres Valmont, une
PME de Laval. Elle est déjà en poste — c'est ce qui sépare ce module de
`module-n6-recherche`, où l'on cherche encore un emploi.
"""

MANIFESTE = {
    'slug': 'module-n8-emploi',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Emploi',

    # Pourpre : la couleur du niveau 8. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#7E3F98',
    'accent_doux': '#F3E8F7',

    'ia_oral': "L'élève intervient dans une réunion de travail axée sur la "
               "prise de décision : il résume la proposition entendue, donne "
               "son avis en le justifiant par au moins deux arguments, "
               "nuance avec « cependant » ou « en revanche », puis propose un "
               "compromis chiffré. Il vouvoie ses interlocuteurs et emploie "
               "le conditionnel de proposition.",

    'jr_cas': 'paie',
    'jr_role': 'employe',
    'jr_scenario': 'emploi',
    'ia_jeu_de_role': "L'élève règle un problème administratif au téléphone "
                      "avec le service de la paie de son employeur : il "
                      "expose le problème avec des dates et des chiffres, "
                      "répond aux objections, cite la norme du travail qui "
                      "s'applique et obtient un engagement daté.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Tenir son bout au "
             "travail » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
