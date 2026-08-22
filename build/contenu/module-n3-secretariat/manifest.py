# -*- coding: utf-8 -*-
"""Identité de module-n3-secretariat — « L'absence de Nawel » (niveau 3).

La situation du programme est « Communication avec le personnel de
l'établissement ». Au niveau 3, elle tient en **deux intentions**, et ce sont
les deux faces d'un même geste : « Informer le personnel d'une absence ou d'un
abandon », en production **orale** et en production **écrite**. Rien d'autre.
Le module dit donc une seule chose, mais des deux façons : on le dit au
comptoir, on l'écrit dans un courriel.

Le lexique du programme est minuscule et parfaitement clair — « formules
d'appel et de salutation », « avis d'abandon, justification d'absence : billet
d'absence ». Ces trois objets sont l'ossature des trois défis.

Ce qui le sépare de son voisin du niveau 4 : au 4, l'élève négocie avec
l'établissement — il demande un changement d'horaire, il explique un
empêchement, il argumente. Ici, au 3, il **informe** : une phrase, une date,
une raison, un papier. Le module apprend à dire une chose difficile en peu de
mots, et à ne rien oublier de ce que le comptoir a besoin de savoir.
"""

MANIFESTE = {
    'slug': 'module-n3-secretariat',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # L'apostrophe est échappée : le jeton %%THEME%% est posé dans une chaîne
    # JavaScript à guillemets simples, et le build refuse de continuer sans.
    'theme': "Communication avec le personnel de l\\'établissement",

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève se présente au comptoir du secrétariat : il salue, "
               "donne son nom, son prénom et son groupe, annonce son absence "
               "en une phrase au futur proche, donne le jour et le moment, "
               "dit la raison avec « parce que », puis demande s'il faut un "
               "papier.",

    'jr_cas': 'garderie',
    'jr_role': 'eleve',
    'jr_scenario': 'secretariat',
    'ia_jeu_de_role': "L'élève parle à la secrétaire du centre : il annonce "
                      "une absence ou un abandon, donne son nom et son "
                      "groupe, la date, la raison, et demande quel papier "
                      "apporter.",

    # `bravo` échappe son apostrophe au même titre que `relance` et `theme` :
    # le titre de ce module en contient une, et sans l'échappement le script
    # entier du module meurt sur une SyntaxError — plus un seul exercice ne
    # s'affiche, et la première personne à le voir serait l'élève.
    'bravo': "🎉 Bravo, tu as terminé le module « L\\'absence de Nawel » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
