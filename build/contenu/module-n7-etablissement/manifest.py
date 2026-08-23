# -*- coding: utf-8 -*-
"""Identité de module-n7-etablissement — « Entrer dans le programme ».

Niveau 7, situation « Communication avec le personnel de l'établissement »,
domaine général de formation « Éducation et monde du travail ». Activité 118,
module 11 du niveau 7 — le dernier, celui qui ferme le niveau. Vague 7.

Ce que `python3 build/cadre.py 7 "personnel"` donne
----------------------------------------------------
**Trois intentions, et elles se lisent comme un plan de module** :

  · CO et PO — participer à une entrevue de sélection pour suivre une
    formation ;
  · CO et PO — téléphoner après une entrevue pour faire un suivi ;
  · PE — rédiger une lettre de motivation en vue de participer à une
    formation.

C'est le cas de figure décrit par l'activité 110 et confirmé par l'activité
113 : **au niveau 7, la situation peut être plus nette que le niveau**. Il n'y
a rien à choisir parmi les cinquante-sept savoirs communs avant d'avoir posé
ces trois-là. Les défis *sont* les intentions, une par défi, et les savoirs
viennent ensuite se ranger dessous.

L'ordre est celui du calendrier réel d'une admission, pas celui du cadre :
on écrit d'abord (défi 1), on passe l'entrevue ensuite (défi 2), on relance
après (défi 3). Aucune tâche du module n'est hors programme : les trois
productions de « Je me lance » sont les trois intentions elles-mêmes.

Le savoir lexical rattaché à la situation, dans le programme, tient en trois
points : « phrases clés pour se présenter, exposer le motif de l'appel et
mettre fin à une conversation téléphonique » — c'est l'exercice `t3tel` et sa
mini-leçon, et c'est le squelette du défi 3 ; « vocabulaire en rapport avec
les objectifs de formation : choix de cours, motivation, profil, plan de
carrière » — les mots du défi 2 ; « vocabulaire en rapport avec la rédaction
d'une lettre : présentation, différentes formules de courtoisie » — ceux du
défi 1.

La grille : `GRILLE_3_DEFIS`, et le test des trois entrées
-----------------------------------------------------------
La vague 7 laissait le choix pour ce module. Le test du pilote du niveau 6
tranche sans forcer : peut-on nommer trois façons distinctes d'entrer dans la
situation, chacune avec son dialogue et ses cinq exercices ? Oui — et elles ne
diffèrent pas par le sujet mais par le **canal**, ce qui est plus solide :
l'écrit qu'on relit dix fois, le face à face où l'on n'a qu'un essai, et le
téléphone où l'on ne voit pas la personne à qui l'on demande. Trois canaux,
trois grammaires : la lettre travaille les connecteurs et la nominalisation,
l'entrevue le conditionnel, la mise en relief et la concession, l'appel le
discours indirect au passé et la restriction.

Ce qui distingue ce module de ses quatre voisins de situation
---------------------------------------------------------------
En une phrase, écrite avant le scénario, comme la vague 7 le demande : **c'est
le seul module du dépôt où l'établissement choisit, et où il peut dire non.**

  · `module-n3-secretariat` (86, niveau 3) informe le personnel d'une absence
    ou d'un abandon. On **informe** : une date, une raison, un papier.
  · `module-n5-ecole` (74, niveau 5) expose au centre une affaire qui dure et
    réclame une trace écrite. On **règle** un problème déjà là.
  · `module-n6-etablissement` (102, niveau 6) assemble de l'information venue
    de trois sources pour choisir un programme. On **décide**.
  · `module-n4-etablissement` (108, niveau 4) laisse un message le matin et en
    reçoit trois le soir : personne ne se parle, une machine répond. On
    **transmet**.

Dans les quatre, l'établissement sert : il inscrit, il renseigne, il traite.
Ici il **trie**. Soixante-huit demandes, vingt-quatre places, et un dossier
qui ne rentre dans aucune case — des études faites ailleurs et interrompues,
cinq ans d'expérience qu'aucun relevé n'atteste, un préalable manquant. Ce que
le niveau 7 ajoute à la situation n'est pas la longueur des phrases : c'est
qu'il n'y a plus de guichet. Personne, au centre, n'a pour tâche de faire
avancer un dossier sur une liste d'attente ; ce que Rania obtient au défi 3,
elle l'obtient en proposant quelque chose que le centre n'avait pas devant
lui, pas en demandant une place.

Les faits québécois, vérifiés le 23 août 2026
----------------------------------------------
Rien de ce qui suit n'est deviné ; le détail des sources est au journal de la
vague 7, dans `docs/vagues-suivantes.md`.

%%FAITS%%

**Ce qui est inventé l'est entièrement** : le Centre de formation
professionnelle du Ruisseau-Vert, le CHSLD des Quatre-Vents, toutes les
personnes, le nombre de demandes et de places, les dates, les rangs sur la
liste d'attente et le contenu de la lettre de décision. Les exercices de type
`texte` le disent à l'élève dans leur bandeau de savoir : le document est écrit
pour le module, et pour un vrai dossier ce sont les documents du centre de
services scolaire qu'il faut ouvrir.

Les personnages
----------------
Cinq, et aucun de ces noms ne paraît ailleurs dans `build/contenu/` —
vérifié par grep avant de les nommer.

  · **Rania Nassar**, 38 ans, arrivée de Syrie il y a cinq ans, préposée aux
    bénéficiaires au CHSLD des Quatre-Vents, à Granby. Deux ans d'études en
    soins infirmiers à Alep, interrompues sans diplôme.
  · **Ghyslaine Bilodeau**, sa collègue depuis vingt-deux ans dans le métier.
    Elles se **tutoient** — ce sont des collègues, et c'est le seul dialogue au
    tutoiement du module.
  · **Émilien Fiset**, conseiller pédagogique au Centre de formation
    professionnelle du Ruisseau-Vert. Il reçoit les dossiers, il siège au
    comité, et c'est lui qui rappelle au défi 3.
  · **Yvan Lemay**, infirmier auxiliaire depuis dix-neuf ans, enseignant du
    programme et second membre du comité de sélection.
  · **Nadine Beaudet**, technicienne en organisation scolaire au secrétariat.
    Elle ne peut rien dire de la liste d'attente, et elle le dit bien.

Le module **vouvoie** partout sauf entre les deux collègues, et l'écran de fin
vouvoie l'élève.

La contrainte de casting, comptée avant d'écrire les dialogues
----------------------------------------------------------------
Le dépôt a **quatre voix** — deux féminines, deux masculines. Les locuteurs
ont donc été comptés **par extrait**, comme l'activité 115 l'a appris à ses
dépens :

  · `prep` — Rania et Ghyslaine : deux femmes, deux voix féminines.
  · `t1` — Rania et Émilien.
  · `t2` — Rania, Émilien et Yvan : une femme, deux hommes, trois timbres.
  · `t3` — Rania, Nadine, puis Émilien : Nadine prend la voix de Ghyslaine,
    qu'elle ne rencontre jamais.

Aucun extrait ne réunit trois personnes du même genre, et c'est ce qui a fixé
le genre d'Yvan Lemay avant que la première réplique soit écrite.
"""

MANIFESTE = {
    'slug': 'module-n7-etablissement',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # L'apostrophe s'échappe : la valeur est injectée dans une chaîne
    # JavaScript à guillemets simples, et le build s'arrête sans cela.
    'theme': "Communication avec le personnel de l\\'établissement",

    # Indigo : la couleur du niveau 7. Elle ne se choisit pas —
    # `build/couleurs_niveau.py` la pose et la vérifie.
    'accent': '#3B49A0',
    'accent_doux': '#E8EAFA',

    'ia_oral': "L'élève présente son projet de formation comme on le fait "
               "devant un comité de sélection : il annonce le programme qu'il "
               "vise et depuis quand, il donne deux éléments de son parcours "
               "qui le préparent à cette formation-là — avec une durée ou un "
               "chiffre —, il nomme une aptitude et la prouve par un exemple "
               "précis plutôt que par un adjectif, il concède une difficulté "
               "avec « même si » ou « bien que » puis dit comment il "
               "l'organise, et il finit par son plan : le diplôme, puis "
               "l'étape d'après. Il met en avant l'essentiel par une phrase "
               "emphatique — « ce que je veux, c'est… », « c'est en "
               "travaillant de nuit que… ». Il vouvoie, il ne se diminue "
               "jamais et il ne récite pas.",

    'jr_cas': 'entrevue',
    'jr_role': 'rania',
    'jr_scenario': 'admission',
    'ia_jeu_de_role': "L'élève passe une entrevue de sélection pour entrer "
                      "dans une formation contingentée : il salue et se "
                      "présente, il répond de façon complète à des questions "
                      "ouvertes sur son parcours, ses motifs et ses projets, "
                      "il donne un exemple concret au lieu d'un adjectif, il "
                      "concède une difficulté sans s'excuser d'exister, il "
                      "pose au conditionnel les deux ou trois questions qu'il "
                      "a préparées — l'horaire, le stage, ce qui arrive s'il "
                      "n'est pas retenu —, et il demande avant de partir "
                      "quand la décision sera communiquée et par quel moyen.",

    # L'apostrophe s'échappe dans `theme`, `bravo` et `relance` : les trois
    # valeurs sont injectées dans des chaînes JavaScript à guillemets simples.
    'bravo': "🎉 Bravo, vous avez terminé le module "
             "« Entrer dans le programme » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
