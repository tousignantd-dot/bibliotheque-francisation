# -*- coding: utf-8 -*-
"""Identité de module-n7-actualite — « Suivre l'actualité » (niveau 7).

Situation « Suivi de l'actualité » du programme, domaine Culture et médias.
Six intentions : deux en compréhension orale (le reportage informatif, la
chronique ou l'entrevue), trois en compréhension écrite (l'article informatif,
l'article d'opinion, la chronique pratique) et une en production écrite
(intervenir dans un blogue). L'intention hors situation « Échanger avec
quelqu'un sur l'actualité » porte le jeu de rôle et la production orale.

Le slug nomme le scénario et porte son niveau, comme tout le dépôt depuis les
niveaux 1 et 2.

Ce que ce module porte de particulier : les extraits sont **longs**. Au
niveau 7 la compétence vise des discours étendus, pas des dialogues de trois
répliques — d'où un reportage et une entrevue de radio de plus de vingt
répliques, travaillés en écoutes successives plutôt qu'en une fois.
"""

MANIFESTE = {
    'slug': 'module-n7-actualite',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Actualité',

    # Indigo : la couleur du niveau 7. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#3B49A0',
    'accent_doux': '#E8EAFA',

    'ia_oral': "L'élève fait le compte rendu d'un fait d'actualité à "
               "quelqu'un de son entourage : il rappelle de quoi il s'agit, "
               "donne les faits essentiels dans l'ordre, sépare clairement ce "
               "qui est confirmé de ce qui ne l'est pas, puis donne son "
               "opinion en la présentant comme une opinion. Il tutoie son "
               "interlocuteur.",

    'jr_cas': 'depot',
    'jr_role': 'citoyen',
    'jr_scenario': 'actualite',
    'ia_jeu_de_role': "L'élève échange avec quelqu'un sur un sujet "
                      "d'actualité : il résume la nouvelle, distingue le fait "
                      "de l'opinion, réagit à un avis contraire sans le "
                      "rejeter, et concède un point avant de donner le sien.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Suivre l'actualité » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
