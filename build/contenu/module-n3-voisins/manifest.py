# -*- coding: utf-8 -*-
"""Identité de module-n3-voisins — « L'escalier de la rue Dézéry » (niveau 3).

La situation du programme est « Relations sociales », et c'est
`build/cadre.py 3 "Relations sociales"` qui a décidé de la forme du module.
Son verdict est l'inverse de celui de `module-n3-loyer` : **treize intentions
de communication, dont dix orales** — comprendre une invitation, comprendre
une demande de permission, comprendre l'information à l'occasion d'un
premier contact, comprendre des compliments, comprendre la description d'un
objet, d'une personne ou d'un problème ; donner une permission, se présenter
et présenter quelqu'un, complimenter, décrire, inviter. La compréhension
écrite n'en compte **qu'une** — lire une description — et la production
écrite deux : rédiger une invitation, décrire.

Le module est donc bâti sur des **conversations d'escalier**, et non sur des
papiers : les deux seuls écrits qu'on y produit sont un carton d'invitation
glissé sous une porte et une petite affiche de description punaisée dans
l'entrée. Chacun répond à une intention nommée par le programme ; aucun autre
document n'a été inventé, faute d'intention pour le porter.

Le lexique rattaché à la situation est généreux à ce niveau, et il a servi tel
quel plutôt que d'être réinventé : les liens familiaux, les prénoms, les
professions, les caractéristiques physiques, les traits de caractère, la
description d'un objet perdu, les adverbes d'intensité, les formes « chez
nous, chez vous, chez eux », les formules de compliments (« Ça te va bien ! »,
« Que c'est bon ! », « Tu cuisines bien ! ») et les quatre tournures de
l'invitation — « Qui vient ? », « La fête aura lieu… », « Confirmez SVP »,
« Apportez… ». Ces quatre-là sont à elles seules la matière du Défi 2.

**Trois voisins sur le même sujet, et rien qui se recoupe.** Au niveau 2,
`module-n2-bonjour` s'arrête au salut et au « ça va ? » dans une entrée
d'immeuble. Au niveau 4, `module-relations` donne des nouvelles et raconte au
passé une expérience vécue. Au niveau 5, `module-n5-voisinage` organise une
fête de ruelle, argumente un refus et laisse un message sur un répondeur. Ici,
au niveau 3, on tient le lien **court et régulier** de l'immeuble : on demande
la permission avant de prendre de la place, on invite pour un après-midi, on
remercie, et on décrit ce qui manque pour que l'autre le reconnaisse.

Le quartier, l'immeuble, les personnes, l'animal et les heures sont inventés.
"""

MANIFESTE = {
    'slug': 'module-n3-voisins',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Relations sociales',

    # Ambre : la couleur du niveau 3. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#B45309',
    'accent_doux': '#FBEEDC',

    'ia_oral': "L'élève parle à sa voisine d'immeuble : il salue, il dit en "
               "une phrase pourquoi il vient, il demande une permission "
               "poliment, il donne le jour, l'heure et l'endroit de son "
               "invitation, puis il remercie avant de partir.",

    'jr_cas': 'permission',
    'jr_role': 'voisine',
    'jr_scenario': 'voisins',
    'ia_jeu_de_role': "L'élève parle à la voisine du deuxième étage : il "
                      "demande la permission de ranger son vélo dans la "
                      "remise, ou il l'invite à prendre un café chez lui, ou "
                      "il décrit l'animal qu'il croit avoir aperçu dans la "
                      "ruelle.",

    'bravo': "🎉 Bravo, tu as terminé le module « L\\'escalier de la rue "
             "Dézéry » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
