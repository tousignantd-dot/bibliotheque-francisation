# -*- coding: utf-8 -*-
"""Identité de module-n5-emmenagement — « Emménager dans un nouveau logement ».

La situation du programme est absente du niveau 4 : elle commence au 5. Elle ne
recoupe ni `module-n5-logement` (activité 58), qui s'arrête à la signature du
bail, ni `module-n5-degat` (62), qui répare un dégât. Ici le bail est signé et
tout ce qui suit reste à faire : le camion, l'adresse, les branchements,
l'état des lieux, les premiers mots aux voisins.
"""

MANIFESTE = {
    'slug': 'module-n5-emmenagement',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Emménagement dans un nouveau logement",

    # Sarcelle : la couleur du niveau 5. Posée par build/couleurs_niveau.py,
    # qui la relit dans colors.css — ne pas la choisir à la main.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève se présente à une nouvelle voisine le lendemain de son "
               "emménagement : il s'excuse du bruit de la veille en disant ce "
               "qui s'est passé, demande comment fonctionnent la salle de "
               "lavage, le bac brun et le stationnement dans l'immeuble, puis "
               "répond à l'invitation qu'on lui fait en acceptant ou en "
               "refusant avec une raison.",

    'jr_cas': 'troisdemie',
    'jr_role': 'client',
    'jr_scenario': 'demenagement',
    'ia_jeu_de_role': "L'élève appelle une compagnie de déménagement : il donne "
                      "la date, les deux adresses, l'étage et ce qu'il y a de "
                      "gros à transporter, puis va chercher le tarif, ce qui "
                      "s'ajoute au tarif, l'assurance et le dépôt, et répète la "
                      "date et l'heure avant de raccrocher.",

    'bravo': "🎉 Bravo, vous avez terminé le module "
             "« Emménager dans un nouveau logement » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
