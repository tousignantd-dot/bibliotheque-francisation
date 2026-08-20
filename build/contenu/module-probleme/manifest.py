# -*- coding: utf-8 -*-
"""Identité de module-probleme — « Pouvez-vous régler le problème ? »

Tout ce qui n'est pas du contenu pédagogique et qui distingue ce module du
gabarit. Le contenu, lui, vit dans les fichiers `.js` de ce dossier.
"""

MANIFESTE = {
    'slug': 'module-probleme',

    # `titre` et `niveau` ne sont PAS ici : ils viennent de
    # `build/powerpoints/modules.py`, qui est la source unique. Les redéfinir
    # ferait une source de plus, et le build refuserait la contradiction.

    # Thème envoyé au suivi LMS avec la production orale.
    'theme': 'Logement',

    # Couleur d'en-tête : violet graphie-phonie, distincte de module-logement
    # (acier) qui est son voisin immédiat, et du gabarit (acier).
    'accent': '#6B4FBB',
    'accent_doux': '#EFEAFA',

    # Consigne envoyée à l'IA pour corriger la production orale.
    'ia_oral': "L'élève explique oralement un problème dans son logement à sa "
               "propriétaire ou à son concierge : il nomme le problème, dit "
               "depuis quand il dure (depuis, depuis que, ça fait... que), en "
               "explique la conséquence, puis formule une demande.",

    # Jeu de rôle : le cas de départ et le scénario que server.py doit jouer.
    'jr_cas': 'chauffage',
    'jr_scenario': 'probleme',
    'ia_jeu_de_role': "L'élève joue un rôle au téléphone : il explique un "
                      "problème dans son logement à sa propriétaire, dit depuis "
                      "quand il dure (depuis, depuis que, ça fait... que), en "
                      "donne la conséquence et demande une réparation "
                      "(faire + infinitif).",

    # Écran de fin. Ce module vouvoie l'élève ; d'autres le tutoient.
    'bravo': '🎉 Bravo, vous avez terminé le module '
             '« Pouvez-vous régler le problème ? » !',
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    # Mots du gabarit qui ne doivent plus apparaître dans le module produit.
    # Le filet de sécurité du build s'arrête si l'un d'eux survit.
    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
