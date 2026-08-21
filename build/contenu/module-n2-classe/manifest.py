# -*- coding: utf-8 -*-
"""Identité de module-n2-classe — « Ouvrez votre cahier » (niveau 2).

Cinquième module court du dépôt, quatrième du niveau 2 : huit séances, deux
défis. La situation du programme est « Salle de classe ». Ses trois intentions
tiennent l'ensemble : comprendre une directive à l'oral (CO), comprendre une
directive à l'écrit (CE), et donner des renseignements sur le fonctionnement
de la classe et de l'établissement de formation (PO). La production écrite,
qu'aucune intention ne demande à ce niveau, se réduit à ce qu'un débutant écrit
vraiment : un petit mot d'absence de trois lignes.

Distinct de `module-n2-bonjour`, qui salue un voisin dans une entrée
d'immeuble, et de `module-procedure` (niveau 4), qui suit une marche à suivre
écrite de plusieurs étapes : ici, une consigne fait trois mots, commence par un
verbe à l'impératif, et la bonne réponse de l'élève est souvent « pouvez-vous
répéter ? ».
"""

MANIFESTE = {
    'slug': 'module-n2-classe',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Salle de classe",

    'accent': '#A83A22',
    'accent_doux': '#FBEAE4',

    'ia_oral': "L'élève explique le fonctionnement de sa classe à une personne "
               "qui arrive : l'heure du cours, l'heure de la pause, ce qu'il "
               "faut apporter, une chose permise et une chose interdite. "
               "Phrases très courtes, au présent ou à l'impératif. Le "
               "vouvoiement doit être tenu du début à la fin.",

    'jr_cas': 'consigne',
    'jr_role': 'moi',
    'jr_scenario': 'classe',
    'ia_jeu_de_role': "L'élève est en classe : il dit qu'il n'a pas compris, "
                      "demande de répéter, redit la consigne dans ses mots, "
                      "demande une permission et annonce une absence.",

    'bravo': "🎉 Bravo, tu as terminé le module « Ouvrez votre cahier » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
