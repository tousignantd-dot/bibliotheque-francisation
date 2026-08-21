# -*- coding: utf-8 -*-
"""Identité de module-n2-couloirs — « Où est le local 214 ? » (niveau 2).

Sixième module court du dépôt, cinquième du niveau 2 : huit séances, deux
défis. La situation du programme est « Orientation dans l'établissement ».
Elle n'a que trois intentions, et elles disent toutes la même chose : se
renseigner sur la localisation (CO et PO), en donner (PO), comprendre le plan
d'un établissement de formation (CE). Le module tient donc entièrement sur les
repères du bâtiment. La production écrite, qu'aucune intention ne demande à ce
niveau, se réduit à ce qu'un débutant écrit vraiment : trois lignes pour dire
à quelqu'un où est son local.

Distinct de `module-n2-autobus` (57), qui est dehors et se repère à des noms
de rues et d'arrêts, et de `module-n2-classe` (89), qui ne quitte jamais une
seule salle — l'un occupe déjà la consigne d'enseignante, l'autre l'avis
affiché près de la porte. Ici, l'élève circule entre les deux : il monte un
étage, longe un corridor, cherche une porte. Et ce qui le guide n'est pas un
mot, c'est un chiffre.
"""

MANIFESTE = {
    'slug': 'module-n2-couloirs',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Orientation dans l\\'établissement",

    'accent': '#A83A22',
    'accent_doux': '#FBEAE4',

    'ia_oral': "L'élève explique le bâtiment du centre à une personne qui "
               "arrive : à quel étage est son local, où est l'escalier, où "
               "sont les toilettes, où est la cafétéria. Il donne l'étage "
               "d'abord, le côté ensuite. Phrases très courtes, au présent ou "
               "à l'impératif. Le vouvoiement doit être tenu du début à la "
               "fin.",

    'jr_cas': 'local',
    'jr_role': 'moi',
    'jr_scenario': 'couloirs',
    'ia_jeu_de_role': "L'élève cherche son chemin dans le centre : il demande "
                      "où est un local, il redit l'étage et le côté pour "
                      "vérifier, il fait répéter quand ça va trop vite, puis "
                      "il indique à son tour le chemin à quelqu'un.",

    'bravo': "🎉 Bravo, tu as terminé le module « Où est le local 214 ? » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
