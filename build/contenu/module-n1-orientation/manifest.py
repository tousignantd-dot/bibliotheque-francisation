# -*- coding: utf-8 -*-
"""Identité de module-n1-orientation — « Je lis les panneaux du centre » (niveau 1).

Activité 97, troisième module du niveau 1. Format court : huit séances, deux
défis (`GRILLE_COURTE`). Le stade est celui du grand débutant qui n'a pas
encore l'alphabet ; les dialogues font six à huit répliques et les phrases
trois à six mots.

Le cadre ministériel
--------------------
`python3 build/cadre.py 1 "Orientation dans l’établissement"` : la situation
n'a **qu'une seule** intention de communication, et elle est en compréhension
écrite — *décoder des panneaux avec ou sans pictogrammes*. Son lexique tient
en une ligne : *noms des lieux : toilettes, cafétéria, service de garde*. Tout
le module tient donc dans un geste unique : lever les yeux, voir un dessin,
lire le mot écrit à côté, et savoir si c'est là qu'on va.

Les savoirs du niveau qui portent le module viennent tous du même endroit du
programme — les « éléments de graphie » et le lexique :

  · décoder des syllabes graphiques simples ;
  · distinguer lettres majuscules et lettres minuscules ;
  · comprendre des mots écrits en caractères d'imprimerie différents ;
  · reconnaître le présentatif « c'est » et l'employer dans des énoncés à
    mémoriser ;
  · distinguer la phrase négative de la phrase déclarative par (ne)… pas ;
  · reconnaître quelques verbes à l'impératif, 2e personne du pluriel.

Ce qui le sépare de `module-n2-couloirs`
----------------------------------------
Les deux modules travaillent la même situation du programme et se passent
dans le même genre de bâtiment ; ils ne demandent pas le même geste.

  · `module-n2-couloirs` (niveau 2, activité 90) fait **circuler** : lire le
    plan mural, comprendre qu'un 214 veut dire deuxième étage, demander son
    chemin à quelqu'un et le lui indiquer à son tour. C'est de la
    compréhension orale et de la production orale, avec des nombres à trois
    chiffres, la gauche, la droite et le bout du corridor.
  · Ici, au niveau 1, l'élève ne demande rien à personne et ne va nulle part
    tout seul : il **lit une porte**. Un dessin, un mot, une réponse — c'est
    là, ou ce n'est pas là. Aucun nombre à trois chiffres, aucun plan, aucune
    indication de direction à produire, aucun itinéraire. Le mot le plus long
    du module fait quatre syllabes et il est écrit sur la porte à côté du
    dessin qui le dit déjà.

Quatre mots se recoupent — toilettes, cafétéria, accueil, sortie — parce que
ce sont ceux que le programme nomme lui-même au niveau 1. Le traitement, lui,
ne se recoupe pas : au niveau 2 ce sont des destinations qu'on cherche, ici
ce sont des mots écrits qu'on reconnaît.

Le scénario, inventé
--------------------
Rosa Quiñónez est arrivée du Guatemala il y a cinq semaines avec sa fille
Lucía, quatre ans. Premier jour au centre Saint-Elzéar. Elle ne lit pas
encore le français, mais elle lit très bien les dessins ; Kofi, de sa classe,
arrivé un mois avant elle, lui montre que le mot est toujours écrit à côté du
dessin. Madame Paré tient l'accueil.
"""

MANIFESTE = {
    'slug': 'module-n1-orientation',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Orientation dans l’établissement',

    # Framboise : la couleur du niveau 1 dans l'arc-en-ciel des niveaux
    # (`--niv-1-line` / `--niv-1-bg` de colors.css). Elle ne se choisit pas.
    'accent': '#A5335F',
    'accent_doux': '#FCE9F0',

    'ia_oral': "L'élève nomme cinq panneaux de son centre : il dit ce que "
               "montre le dessin, il lit le mot écrit à côté, et il dit ce "
               "qu'on fait à cet endroit. Il emploie « c'est » et le bon "
               "article : « C'est la cafétéria. »",

    'jr_cas': 'toilettes',
    'jr_role': 'eleve',
    'jr_scenario': 'orientation',
    'ia_jeu_de_role': "L'élève cherche un endroit dans le centre et vérifie "
                      "sur un panneau qu'il est au bon endroit : il nomme le "
                      "dessin qu'il voit, il lit le mot, et il demande « c'est "
                      "ici ? ».",

    'bravo': '🎉 Bravo, tu as terminé le module « Je lis les panneaux du centre » !',
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
