# -*- coding: utf-8 -*-
"""Identité de module-n2-guichet — « Je retire de l'argent ».

Neuvième module court du dépôt, huitième du niveau 2. La situation du
programme est « Transactions bancaires ». Elle a exactement **deux**
intentions de communication, et ce sont elles qui découpent le module :
« Effectuer des opérations courantes au guichet » en compréhension écrite —
c'est le Défi 1 — et « Libeller un chèque » en production écrite — c'est le
Défi 2. Rien n'a été ajouté autour, et rien n'a été emprunté au niveau 4.

Distinct de `module-banque` (niveau 4), dont l'élève va **au comptoir**
parler à un conseiller, lit une brochure de forfaits et compare des taux :
ici, personne n'ouvre de compte et personne ne lit de dépliant. L'élève lit
six phrases sur un écran, entre quatre chiffres, prend ses billets et son
relevé, puis remplit les cinq cases d'un chèque. Tout le module tient dans un
nombre, un impératif et une signature.
"""

MANIFESTE = {
    'slug': 'module-n2-guichet',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Transactions bancaires',

    # Couleur du niveau 2, posée par `build/couleurs_niveau.py`.
    'accent': '#A83A22',
    'accent_doux': '#FBEAE4',

    'ia_oral': "L'élève explique un retrait au guichet automatique : il dit "
               "ce qu'il met dans le guichet, ce qu'il tape, ce qu'il "
               "choisit, le montant qu'il retire en dollars, et ce qu'il "
               "reprend avant de partir. Phrases très courtes, au présent, "
               "sans subordonnée. Les verbes utiles sont « je mets », "
               "« je tape », « je choisis », « je prends ». Le vouvoiement "
               "doit être tenu du début à la fin.",

    'jr_cas': 'retrait',
    'jr_role': 'moi',
    'jr_scenario': 'guichet',
    'ia_jeu_de_role': "L'élève demande de l'aide au guichet automatique : il "
                      "dit ce qu'il veut faire, il donne le montant en "
                      "dollars, il demande ce qu'il faut appuyer, il répète "
                      "le montant pour vérifier, il demande de répéter quand "
                      "ça va trop vite, et il remercie. Il ne dit jamais son "
                      "NIP à voix haute.",

    'bravo': "🎉 Bravo, tu as terminé le module « Je retire de l\\'argent » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
