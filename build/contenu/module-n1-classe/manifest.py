# -*- coding: utf-8 -*-
"""Identité de module-n1-classe — « Regardez le tableau » (niveau 1).

Deuxième module du niveau 1 : huit séances, deux défis, format court. La
situation du programme est « Salle de classe », et le niveau 1 n'en tire que
**deux intentions, toutes deux en compréhension orale** — comprendre de
l'information sur le fonctionnement de la classe, comprendre une consigne. Le
lexique du niveau donne deux entrées et pas une de plus : « objets courants et
routine dans la salle de classe », « heure, horaire ».

Le module s'y tient. L'élève n'explique rien, ne demande rien, ne négocie
rien : il écoute, il montre, il fait. Ce qu'il produit tient en un mot ou en un
chiffre — le nom d'un objet, une heure, un jour.

Distinct de `module-n2-classe` (activité 89), qui traite la même situation au
niveau 2 : là-bas l'élève lit une directive écrite, demande une permission,
annonce un retard et explique le fonctionnement de la classe à un nouveau. Ici
une consigne fait deux mots, la bonne réponse est souvent un geste, et le seul
texte lu est l'heure sur une horloge.
"""

MANIFESTE = {
    'slug': 'module-n1-classe',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Salle de classe",

    # Framboise : la couleur du niveau 1, posée par
    # `build/couleurs_niveau.py` d'après `--niv-1-line` / `--niv-1-bg`.
    'accent': '#A5335F',
    'accent_doux': '#FCE9F0',

    'ia_oral': "L'élève nomme cinq objets de sa salle de classe, dit à quelle "
               "heure son cours commence, à quelle heure il finit, et quel "
               "jour il n'y a pas de cours. Un mot ou une phrase de trois "
               "mots suffit : c'est le tout premier niveau du programme. "
               "Encourage chaque mot juste. Ne corrige ni les articles, ni "
               "les liaisons, ni l'ordre des mots — seulement ce qui empêche "
               "de comprendre.",

    'jr_cas': 'consigne',
    'jr_role': 'moi',
    'jr_scenario': 'classe1',
    'ia_jeu_de_role': "L'élève est assis en classe le premier jour. "
                      "L'enseignante donne une consigne de deux mots ; "
                      "l'élève montre l'objet, dit le mot, ou dit qu'il n'a "
                      "pas compris. On lui demande aussi l'heure et le jour.",

    'bravo': '🎉 Bravo, tu as terminé le module « Regardez le tableau » !',
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour écouter "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie',
                          'Beaulieu', 'tendinite', 'Consulter au bon endroit',
                          'physiothérapie'],
}
