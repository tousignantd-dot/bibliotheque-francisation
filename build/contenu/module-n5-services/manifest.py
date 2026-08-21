# -*- coding: utf-8 -*-
"""Identité de module-n5-services — « Utilisation des services publics » (niv. 5).

Le programme ne donne que trois intentions pour cette situation : comprendre et
demander des renseignements par téléphone (CO et PO), et comprendre de
l'information dans un formulaire complexe, une brochure ou un site Web (CE).
Le domaine général de formation est « Consommation et environnement » — d'où
l'angle municipal : la collecte, l'écocentre, le guichet de la Ville.

Ce que ce module N'EST PAS, et pourquoi :

- ce n'est pas `module-n5-emmenagement` (63), qui fait brancher l'électricité
  et changer l'adresse le jour du déménagement. Ici Leïla est installée depuis
  huit mois ; ce qu'elle apprend, c'est à se servir d'un service public qui
  existe déjà et qui a mal fonctionné ;
- le niveau 4 n'a aucun module sur cette situation. Le plus proche,
  « Quelle est la procédure ? » (40), reste dans l'établissement scolaire.

Les faits québécois du module ont été vérifiés sur les sites officiels le
21 août 2026 — voir le journal de docs/chantier-tous-niveaux.md.
"""

MANIFESTE = {
    'slug': 'module-n5-services',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Utilisation des services publics",

    # Sarcelle : la couleur du niveau 5. Posée par build/couleurs_niveau.py,
    # qui la relit dans colors.css — ne pas la choisir à la main.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    'ia_oral': "L'élève laisse un message dans la boîte vocale d'un service "
               "public : il se nomme, donne son numéro de requête, explique "
               "en deux ou trois phrases ce qu'il attend, laisse un numéro "
               "où le rappeler et dit à quel moment il est joignable. "
               "Vérifier que le message est complet, ordonné et audible du "
               "premier coup — on ne rappelle pas pour faire répéter.",

    'jr_cas': 'bac',
    'jr_role': 'citoyen',
    'jr_scenario': 'services',
    'ia_jeu_de_role': "L'élève téléphone à un service public de sa ville : il "
                      "explique sa demande, répond aux questions "
                      "d'identification (adresse, code postal, date), "
                      "demande des renseignements précis sur les délais et "
                      "sur ce qu'il doit apporter, note le numéro de requête "
                      "et le répète pour le confirmer avant de raccrocher.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Les services de ma "
             "ville » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
