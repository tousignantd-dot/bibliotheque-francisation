# -*- coding: utf-8 -*-
"""Identité de module-relations — « Des nouvelles à donner »

Tout ce qui n'est pas du contenu pédagogique et qui distingue ce module du
gabarit. Le contenu, lui, vit dans les fichiers `.js` de ce dossier.
"""

MANIFESTE = {
    'slug': 'module-relations',

    # `titre` et `niveau` ne sont PAS ici : ils viennent de
    # `build/powerpoints/modules.py`, qui est la source unique.

    # Thème envoyé au suivi LMS avec la production orale.
    'theme': 'Relations sociales',

    # Teal : la rotation à cinq couleurs du projet. Le voisin immédiat
    # (module-probleme) est violet, celui d'avant bleu.
    'accent': '#0D7A6F',
    'accent_doux': '#DCF2EF',

    # Consigne envoyée à l'IA pour corriger la production orale.
    'ia_oral': "L'élève raconte oralement une expérience personnelle "
               "marquante — une arrivée, un déménagement, un voyage, une "
               "naissance, un mariage : il plante le décor à l'imparfait, "
               "raconte les évènements au passé composé, et dit ce que ça a "
               "changé pour lui.",

    # Jeu de rôle : le cas de départ et le scénario que server.py doit jouer.
    'jr_cas': 'volleyball',
    'jr_role': 'nouveau',       # le rôle que l'élève joue au départ
    'jr_scenario': 'relations',
    'ia_jeu_de_role': "L'élève fait connaissance avec quelqu'un dans une "
                      "activité de loisir : il parle de ses activités de la "
                      "semaine, pose des questions sur celles de l'autre, "
                      "raconte une expérience personnelle au passé et propose "
                      "de se revoir.",

    # Écran de fin. Ce module tutoie l'élève — c'est un module sur l'échange
    # informel, et le tutoiement y est la forme juste.
    'bravo': '🎉 Bravo, tu as terminé le module « Des nouvelles à donner » !',
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    # Mots du gabarit qui ne doivent plus apparaître dans le module produit.
    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
