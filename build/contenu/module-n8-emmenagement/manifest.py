# -*- coding: utf-8 -*-
"""Identité de module-n8-emmenagement — « Ce qui est couvert, et ce qui se
défend » (niveau 8, activité 120, numéro 3 du niveau).

Le slug porte le niveau et nomme la situation du programme :
`module-n5-emmenagement` (63) occupe déjà le mot, et les dossiers de sortie
sont à plat.

CE QUE LE PROGRAMME DEMANDE
---------------------------
`python3 build/cadre.py 8 "Emménagement"` rend **une** intention, et pas une
de plus :

  · Compréhension orale — s'informer sur les assurances (vol, responsabilité,
                          incendie, dégâts, etc.)
  · Production orale    — la même.

Aucune compréhension écrite, aucune production écrite, aucun lexique : le
document de Laval ne couvre pas cette situation-là.

POURQUOI DEUX DÉFIS ET NON TROIS
--------------------------------
La règle de la vague 7 dit : trois défis quand la situation porte trois
intentions ou plus, deux quand elle n'en porte qu'une — et le vrai test est de
pouvoir nommer trois façons distinctes d'entrer dans la situation. Ici on n'en
nomme que deux, et ce n'est pas une pauvreté du scénario : ce sont les savoirs
du cours eux-mêmes qui déplient l'unique intention en exactement deux
conversations, et qui les nomment.

  · « Conversation portant sur le choix d'une police d'assurance » — cinq
    points de savoir : avantages et inconvénients (vol, incendie, dégâts,
    catastrophe naturelle) ; clauses (responsabilité, prime, franchise,
    condition, avenant, mise en garde, exclusion) ; vocabulaire spécialisé ;
    phrases clés pour résumer et faire le point ; phrases clés pour faire
    clarifier les points équivoques.  → **Défi 1 · Ce qui est couvert**
  · « Communication téléphonique avec un assureur pour effectuer une
    réclamation » — trois points : mots pour décrire un accident, un sinistre,
    un vol ou des dégâts ; phrases clés pour exprimer son accord ou son
    désaccord ; phrases clés pour exprimer un point de vue, défendre une
    opinion et réagir aux arguments d'autrui.  → **Défi 2 · Faire valoir sa
    réclamation**

Un troisième défi aurait fallu l'inventer hors situation. GRILLE_2_DEFIS donne
les mêmes seize séances, en deux blocs de cinq au lieu de trois blocs de
quatre.

D'OÙ VIENNENT LA LECTURE ET L'ÉCRITURE
--------------------------------------
Les trois exercices de type `texte` et le courriel de « Je me lance » ne
sortent pas de l'intention — elle est purement orale. Ils sortent des
**attentes de fin de cours** du niveau 8, qui demandent que l'adulte « rédige
des lettres ou des courriels d'affaires ayant des objectifs particuliers en
s'assurant que leur forme et leur contenu sont appropriés », qu'il « résume
les propos de son interlocuteur » et qu'il « négocie la solution d'un
problème, propose des compromis et donne son opinion en la justifiant à l'aide
d'arguments ». C'est le même mécanisme qu'aux niveaux 6 et 8 précédents, et il
faut le noter ici **et** dans `custom.js` : sans cela un relecteur retire la
tâche en la croyant hors programme.

CE QUI LE DISTINGUE DE SES DEUX VOISINS DE SITUATION
----------------------------------------------------
Écrit avant le scénario, en une phrase par voisin.

  · `je-demenage` (16, niveau 4) **cherche et visite** un logement, puis
    pend la crémaillère : le déménagement y est une fête.
  · `module-n5-emmenagement` (63) **organise** l'emménagement : réserver le
    camion, diriger les hommes, changer l'adresse, se présenter aux voisins.
    Tout y va bien ; ce qui s'apprend est une suite de démarches.
  · Celui-ci commence **le soir où ça a mal tourné**. Le camion est reparti,
    et il reste une rampe tordue, deux boîtes noyées et un vaisselier fendu.
    On ne décrit plus un déménagement : on **soutient une réclamation devant
    deux personnes qui ont chacune de bonnes raisons de dire non**, et le
    travail de langue est d'argumenter — concéder ce qui se concède, refuser
    ce qui ne se concède pas, et le mettre par écrit.

LE SCÉNARIO
-----------
Amira Benkirane, 41 ans, arrivée du Maroc il y a six ans, technicienne en
documentation dans un centre d'archives. Elle vient d'emménager au deuxième
étage d'un triplex de brique rouge de la rue Sainte-Ursule, à Trois-Rivières,
escalier extérieur en colimaçon. Le jour du déménagement, le camion de
Déménagement Ducharme et Fils a accroché la rampe, deux boîtes laissées sur le
balcon ont passé une averse, et le vaisselier de sa mère est arrivé fendu.
Denis Ducharme invoque la clause de son contrat de transport. Ghislain
Marcotte, courtier en assurance de dommages, lui explique ce que sa police
couvre vraiment et comment se déroule une réclamation. Véronique Chartier,
experte en sinistre, accepte une partie de la réclamation et en refuse une
autre — et c'est là que le module se joue.

Les personnes, l'entreprise de déménagement, le cabinet de courtage,
l'assureur, l'adresse et tous les montants sont inventés.

LES FAITS QUÉBÉCOIS, VÉRIFIÉS PLUTÔT QU'INVENTÉS
-------------------------------------------------
Ce qui est enseigné dans le module et qui n'est pas une invention : une
assurance habitation de locataire couvre trois choses distinctes — les biens,
la responsabilité civile et les frais de subsistance supplémentaires ; la
franchise est la part qui reste toujours à la charge de l'assuré et se
soustrait de l'indemnité ; « valeur à neuf » et « valeur au jour du sinistre »
sont deux modes d'indemnisation différents, le second tenant compte de la
dépréciation ; un avenant ajoute une protection que le contrat de base
n'offre pas ; les objets de grande valeur doivent être déclarés pour être
couverts au-delà d'un plafond ; les dommages causés par un transporteur
relèvent d'abord de la responsabilité de celui-ci, et l'assureur qui indemnise
peut se retourner contre lui (la subrogation) ; un assuré mécontent d'une
décision peut demander une révision écrite, puis s'adresser à l'Autorité des
marchés financiers. Les montants, les délais et les clauses citées dans les
documents du module sont, eux, fabriqués pour l'exercice.

LE VOUVOIEMENT
--------------
Le module vouvoie partout : trois conversations d'affaires, dont deux
téléphoniques, avec des gens qu'Amira ne connaît pas. L'écran de fin vouvoie
aussi.
"""

MANIFESTE = {
    'slug': 'module-n8-emmenagement',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Emménagement dans un nouveau logement",

    # Pourpre : la couleur du niveau 8. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#7E3F98',
    'accent_doux': '#F3E8F7',

    'ia_oral': "L'élève téléphone à l'entreprise de déménagement pour porter "
               "sa réclamation de vive voix : il annonce en une phrase "
               "l'objet de son appel, expose les faits dans l'ordre avec une "
               "date, une heure et un montant, concède ce qui doit l'être "
               "avec « certes… mais » ou « bien que », emploie au moins une "
               "hypothèse irréelle au conditionnel passé pour dire ce qui "
               "aurait pu être évité, met en relief sa demande par une "
               "phrase emphatique (« ce que je demande, c'est… »), puis "
               "annonce un délai sans menacer. Il vouvoie.",

    'jr_cas': 'vaisselier',
    'jr_role': 'assuree',
    'jr_scenario': 'sinistre',
    'ia_jeu_de_role': "L'élève défend sa réclamation au téléphone devant "
                      "l'experte en sinistre qui vient d'en refuser une "
                      "partie : il fait préciser le motif du refus et la "
                      "clause invoquée, distingue ce qu'il accepte de ce "
                      "qu'il conteste, appuie chaque point sur une pièce "
                      "datée, propose un compromis chiffré, et demande la "
                      "décision par écrit ainsi que la marche à suivre pour "
                      "en obtenir la révision.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Ce qui est couvert, et "
             "ce qui se défend » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie',
                          'Beaulieu', 'tendinite',
                          'Consulter au bon endroit', 'physiothérapie'],
}
