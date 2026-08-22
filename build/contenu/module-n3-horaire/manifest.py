# -*- coding: utf-8 -*-
"""Identité de module-n3-horaire — « Mon quart de travail » (niveau 3).

La situation du programme est « Emploi », et c'est `build/cadre.py 3 "Emploi"`
qui a décidé de la forme du module. Son verdict est court et net : **six
intentions de communication, dont six orales sur huit** — demander une
permission et en comprendre la réponse, demander de l'aide ou un service et en
comprendre la réponse, comprendre une consigne, répondre à une demande de
service. La compréhension écrite n'en compte **qu'une** — lire des consignes
simples — et la production écrite une seule : prendre en note une directive ou
une information simple.

Le module est donc bâti sur ce qui se dit **debout, pendant un quart de
travail**, et non sur des documents : les deux seuls écrits qu'on y rencontre
sont l'horaire affiché au mur de la salle du personnel — qu'on lit — et le
petit mot laissé au chef d'équipe — qu'on écrit. Chacun répond à une intention
nommée par le programme ; aucun autre document n'a été inventé, faute
d'intention pour le porter.

Le lexique rattaché à la situation est généreux à ce niveau, et il a servi tel
quel plutôt que d'être réinventé : les « noms de tâches » d'abord, puis les
verbes que la Progression du lexique rattache à la situation — passer,
laisser, livrer, s'occuper de, offrir, s'absenter, justifier, oublier, devoir,
aviser, emprunter, prêter, éteindre — et les quatre tournures de la demande
d'aide : « Qu'est-ce qui se passe ? », « Pouvez-vous m'aider ? »,
« Passe-moi ton crayon », « Est-ce que tu peux m'aider ? ». Ces quatre-là sont
à elles seules la matière du Défi 2.

**Ce qui distingue ce module de son voisin du niveau 4.** Le module 4 du
niveau 4, `module-travail`, est celui de l'absence : on prévient son
superviseur, on justifie un retard, on écrit un courriel. Ici, au niveau 3, on
est **présent** et la journée se déroule : on lit son quart sur l'horaire, on
demande la permission d'en échanger un, on demande de l'aide quand on ne
comprend pas une consigne, et on dit où on en est dans sa tâche. Rien du
retard, rien de l'absence, rien du courriel.

Trois autres voisins de la même situation, et rien qui se recoupe. Au niveau 5,
`module-n5-travail` parle des relations d'équipe. Au niveau 8,
`module-n8-emploi` règle une erreur de paie et intervient en réunion. Au
niveau 3, on tient la **journée elle-même** : l'heure, la tâche, la question
qu'on ose poser.

Les grammaires exercées sont prises dans les savoirs du niveau 3, un ou deux
par défi : les prépositions de temps (de… à, jusqu'à, à partir de) et les mots
interrogatifs au Défi 1 ; les auxiliaires de modalité (pouvoir, devoir,
falloir) et la demande polie au Défi 2 ; l'impératif présent et les auxiliaires
d'aspect (venir de, être en train de, finir de) au Défi 3. La phonétique de
« Je découvre » oppose le son « ou » de *jour* au son « u » de *minute*, deux
sons que l'horaire fait se croiser à chaque phrase.

La résidence, la cafétéria, les personnes et les heures sont inventées.
"""

MANIFESTE = {
    'slug': 'module-n3-horaire',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Emploi',

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève parle à son chef d'équipe pendant son quart de "
               "travail : il salue, il dit en une phrase pourquoi il vient, "
               "il demande une permission ou de l'aide poliment, il redit "
               "l'heure ou la consigne pour vérifier qu'il a bien compris, "
               "puis il remercie avant de retourner à sa tâche.",

    'jr_cas': 'echange',
    'jr_role': 'employe',
    'jr_scenario': 'horaire',
    'ia_jeu_de_role': "L'élève parle au chef d'équipe de la cafétéria : il "
                      "demande d'échanger un quart de travail, ou il demande "
                      "de l'aide parce qu'il n'a pas compris une consigne, ou "
                      "il vient dire qu'il a terminé sa tâche et demande la "
                      "suivante.",

    'bravo': "🎉 Bravo, tu as terminé le module « Mon quart de travail » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
