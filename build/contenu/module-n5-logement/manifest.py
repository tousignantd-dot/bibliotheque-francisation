# -*- coding: utf-8 -*-
"""Identité de module-n5-logement — « Louer un logement » (niveau 5).

Le slug porte le niveau : `module-logement` est pris par le niveau 4, qui
traite la même situation du programme d'une tout autre façon — là on visite et
on compare, ici on téléphone, on prend des notes et on lit son bail.
"""

MANIFESTE = {
    'slug': 'module-n5-logement',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Location d\\'un logement",

    # Sarcelle : la couleur du niveau 5. Posée par build/couleurs_niveau.py,
    # qui la relit dans colors.css — ne pas la choisir à la main.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève fait visiter un logement : il décrit les pièces, dit "
               "ce qui est inclus dans le loyer, répond aux questions sur le "
               "chauffage, le stationnement et la buanderie, et donne les "
               "conditions du bail sans qu'on ait à les demander deux fois.",

    'jr_cas': 'A',
    'jr_role': 'locataire',
    'jr_scenario': 'louer',
    'ia_jeu_de_role': "L'élève visite un logement ou le fait visiter : il "
                      "demande ou donne des renseignements précis sur le "
                      "loyer, le chauffage, les électroménagers, le "
                      "stationnement, les animaux, le bruit et la durée du "
                      "bail.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Louer un logement » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
