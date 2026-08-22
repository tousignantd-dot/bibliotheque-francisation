# -*- coding: utf-8 -*-
"""Identité de module-n1-inscription — « Je remplis ma fiche » (niveau 1).

Deuxième module du niveau 1, deuxième module court : huit séances, deux
défis. Le stade reste celui du grand débutant — les dialogues font six à huit
répliques, et les phrases, trois à sept mots.

Le scénario, inventé de bout en bout
------------------------------------
Yusuf Daoud, 34 ans, arrivé du Soudan il y a cinq semaines, se présente à la
table d'inscription du Centre Bellerive un mardi matin. **Madame Côté**, la
commis, lui tend une fiche de huit cases et les lui demande une par une.
**Carlos**, assis à côté, remplit la sienne en même temps et se trompe de
case : c'est lui qui porte les erreurs que l'élève va apprendre à éviter.

Rien de tout cela ne vient d'un manuel. Le programme donne la spécification —
deux intentions, un lexique de onze entrées — et rien d'autre.

Ce que ce module fait, et que `module-n1-presenter` ne fait pas
---------------------------------------------------------------
Le premier module du niveau apprend à **dire** son nom et à l'épeler. Celui-ci
apprend à l'**écrire** dans une case, avec ce qui l'accompagne sur une fiche :
la civilité, le sexe, la date de naissance dans l'ordre jour-mois-année,
l'adresse et ses abréviations (app., av., boul., QC), le code postal, le
téléphone et le courriel. La fiche est l'objet du module, du premier écran au
dernier.

Il ne recoupe pas non plus `module-n2-inscription` (niveau 2), qui part d'une
petite annonce de cours et va jusqu'à la case « scolarité » et la signature :
ici, on ne quitte jamais la table, et on ne demande jamais rien — on répond.
"""

MANIFESTE = {
    'slug': 'module-n1-inscription',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Inscription',

    # Framboise : la couleur du niveau 1. Elle ne se choisit pas.
    'accent': '#A5335F',
    'accent_doux': '#FCE9F0',

    'ia_oral': "L'élève répond aux questions d'une fiche d'inscription : il "
               "donne son nom de famille et son prénom, il les épelle, il dit "
               "sa date de naissance dans l'ordre jour, mois, année, son "
               "adresse, son numéro de téléphone et son courriel. Il demande "
               "de répéter plus lentement quand c'est trop vite.",

    'jr_cas': 'table',
    'jr_role': 'eleve',
    'jr_scenario': 'fiche',
    'ia_jeu_de_role': "L'élève est assis à une table d'inscription. Une "
                      "personne lui demande les cases de sa fiche, une à la "
                      "fois : le nom, le prénom, la date de naissance, "
                      "l'adresse, le téléphone, le courriel.",

    'bravo': '🎉 Bravo, tu as terminé le module « Je remplis ma fiche » !',
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
