# -*- coding: utf-8 -*-
"""Identité de module-n3-pharmacie — « Aller à la pharmacie » (niveau 3).

La situation du programme est « Consultation en pharmacie ». Au niveau 3, elle
tient en **trois intentions**, et c'est `build/cadre.py 3` qui les donne :
« décrire un problème de santé courant » et « demander le renouvellement de
l'ordonnance d'un médicament » en production orale, « lire une posologie » en
compréhension écrite. Les trois défis du module sont ces trois intentions,
dans cet ordre — le module ne se bâtit pas sur autre chose.

Le lexique que le programme rattache à cette situation est, lui aussi, très
précis : les principales parties du corps, les prépositions de temps (dans,
depuis, ça fait, il y a, voilà, pendant), les marqueurs de fréquence, les
expressions reliées à la posologie (de plus de, de moins de), et onze verbes —
tousser, avoir de la fièvre, se couper, s'étouffer, se faire mal, consulter,
questionner, administrer, persister, rincer. Tout le module s'y tient.

C'est ce qui le sépare de `module-consultation` (activité 45, niveau 4), qui
mêle la pharmacie au rendez-vous médical : là, on choisit le bon endroit où
consulter, on raconte l'histoire de son mal à un médecin, on remplit des
formulaires, on comprend un suivi. Ici, il n'y a ni médecin, ni salle
d'attente, ni papier à remplir : il y a deux comptoirs, une carte d'assurance
maladie, un pharmacien qui pose des questions et une étiquette à lire.

Les faits québécois du module sont vérifiés, pas inventés : le pharmacien peut
prolonger une ordonnance qui vient à échéance sans dépasser un an (loi 31,
en vigueur depuis 2021) ; il tient un dossier des médicaments de chaque
personne ; on présente sa carte d'assurance maladie ; le régime public laisse
à la charge une franchise et une coassurance ; certains médicaments se vendent
sans ordonnance mais restent derrière le comptoir, sous le jugement du
pharmacien.
"""

MANIFESTE = {
    'slug': 'module-n3-pharmacie',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Consultation en pharmacie',

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève parle au pharmacien : il salue, il dit ce qui ne va "
               "pas, il dit depuis quand ça dure, il répond aux questions du "
               "pharmacien, puis il demande combien de fois par jour prendre "
               "le médicament.",

    'jr_cas': 'toux',
    'jr_role': 'client',
    'jr_scenario': 'pharmacie',
    'ia_jeu_de_role': "L'élève parle au comptoir des ordonnances d'une "
                      "pharmacie : il décrit ce qui ne va pas et depuis "
                      "quand, il fait renouveler une ordonnance ou il fait "
                      "expliquer la posologie de son médicament.",

    'bravo': "🎉 Bravo, tu as terminé le module « Aller à la pharmacie » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
