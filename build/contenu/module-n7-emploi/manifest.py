# -*- coding: utf-8 -*-
"""Identité de module-n7-emploi — « Présenter un projet au travail » (niveau 7).

Situation « Emploi » du programme, domaine « Éducation et monde du travail ».
Activité 109, module 2 du niveau 7. Vague 7.

Ce que `python3 build/cadre.py 7 "Emploi"` donne, et rien d'autre — quatre
intentions :

  · CO — comprendre la présentation d'un projet, d'une évaluation sommaire ou
    d'un problème ;
  · PO — présenter un projet, une évaluation sommaire ou un problème à ses
    collègues ;
  · PE — écrire une note de service ;
  · PE — rédiger une lettre d'affaires courantes.

Les deux productions de « Je me lance » sortent donc de la situation
elle-même, sans passer par les attentes de fin de cours : la production orale
est l'intention PO mot pour mot, la production écrite est la note de service
de la première intention PE, la lettre d'affaires étant travaillée au Défi 3
et offerte en variante. Les attentes de fin de cours ne servent qu'à fixer
l'exigence.

Ce qui distingue ce module de ses quatre voisins de situation, en une phrase
chacun — la discipline de la vague 7 :

- `module-travail` (39, niveau 4) **annonce** une absence au téléphone, à
  chaud, le matin même ;
- `module-n5-travail` (67) **suit** une procédure écrite et réclame une trace ;
- `module-n6-emploi` (100) **pose sa candidature** à un poste affiché à
  l'interne et se fait expliquer la démarche ;
- `module-n8-emploi` (61) **négocie** : il défend un point de vue contre un
  interlocuteur qui n'est pas d'accord.

Ici, personne ne s'oppose à personne, et il n'y a rien à réclamer : il faut
rendre compréhensible pour d'autres un projet qui n'existe encore que dans sa
tête. Le travail du niveau 7, à cette situation, c'est **exposer** — tenir un
discours long et structuré devant des collègues, puis le couler dans les deux
écrits formels du travail.

Le scénario
-----------
Aïcha Traoré, 43 ans, arrivée du Mali il y a cinq ans, est coordonnatrice
adjointe à l'expédition chez Meubles Rive-du-Nord, une usine de soixante-deux
personnes à Terrebonne. Le poste 4, celui de l'emballage, fait mal au dos de
trois de ses collègues : les caisses se soulèvent du sol, à bout de bras,
quatre-vingts fois par quart. Elle veut une table élévatrice et un
réaménagement du poste. Trois retours sur le même dossier : elle écoute
d'abord son chef de production présenter un autre projet (Défi 1), elle
présente le sien (Défi 2), elle l'écrit (Défi 3).

Personnages : Aïcha Traoré ; Renaud Cormier, chef de production ; Thérèse
Lapointe, représentante en santé et en sécurité élue par les travailleurs ;
Vincent Béliveau, conseiller chez Équipements Sorel.

Le vouvoiement est tenu partout sauf entre Aïcha et Thérèse, deux collègues du
même plancher qui se tutoient. Le module s'adresse à l'élève en le vouvoyant.

Les faits québécois, vérifiés le 22 août 2026 et non inventés
-------------------------------------------------------------
Auprès de la CNESST (cnesst.gouv.qc.ca) et de la Loi sur la santé et la
sécurité du travail :

- le Règlement sur les mécanismes de prévention et de participation en
  établissement est en vigueur depuis le 1er octobre 2025 ;
- un établissement de vingt travailleurs ou plus doit avoir un **programme de
  prévention**, élaboré, appliqué et **mis à jour annuellement**, un **comité
  de santé et de sécurité** et un **représentant en santé et en sécurité** ;
  un établissement de dix-neuf travailleurs ou moins a un **plan d'action** et
  un **agent de liaison** ;
- le comité est composé de représentants de l'employeur et des travailleurs,
  au moins la moitié des membres — dont le représentant en santé et en
  sécurité — représentant les travailleurs ;
- tous les trois ans, l'employeur transmet à la CNESST ses priorités d'action
  et le suivi des mesures, sur le formulaire prescrit ;
- **droit de refus** (art. 12 LSST) : un travailleur peut refuser d'exécuter
  un travail s'il a des motifs raisonnables de croire que son exécution
  l'expose à un danger pour sa santé, sa sécurité ou son intégrité, ou expose
  une autre personne à un danger semblable ;
- art. 13 : il ne peut pas refuser si le refus met en péril immédiat la vie,
  la santé, la sécurité ou l'intégrité d'une autre personne, ou si les
  conditions d'exécution sont normales pour ce genre de travail ;
- c'est l'**inspecteur de la CNESST** qui décide s'il existe ou non un danger
  justifiant le refus.

Meubles Rive-du-Nord, Équipements Sorel, les personnes, les chiffres et les
dates sont inventés. Les règles ci-dessus ne le sont pas.
"""

MANIFESTE = {
    'slug': 'module-n7-emploi',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Emploi',

    # Indigo : la couleur du niveau 7. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#3B49A0',
    'accent_doux': '#E8EAFA',

    'ia_oral': "L'élève présente un problème et son évaluation sommaire à ses "
               "collègues, en réunion : il annonce de quoi il s'agit, décrit "
               "le constat avec au moins deux chiffres, nomme la cause et la "
               "conséquence, chiffre ce que le problème coûte, propose un "
               "correctif avec une échéance, puis dit ce qu'il attend de la "
               "réunion. Il enchaîne avec des connecteurs — d'abord, "
               "ensuite, par conséquent, en somme — met en relief ce qui "
               "compte avec « ce qui… c'est », et vouvoie ses "
               "interlocuteurs.",

    'jr_cas': 'poste4',
    'jr_role': 'aicha',
    'jr_scenario': 'projet',
    'ia_jeu_de_role': "L'élève présente un projet de réaménagement à son chef "
                      "de production : il expose le problème avec des "
                      "chiffres, distingue ce qu'il a constaté de ce qu'il "
                      "suppose, propose un correctif chiffré et daté, répond "
                      "à l'objection du coût sans se braquer, et obtient une "
                      "suite précise — une inscription à l'ordre du jour, "
                      "une date, un document à produire.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Présenter un projet au "
             "travail » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
