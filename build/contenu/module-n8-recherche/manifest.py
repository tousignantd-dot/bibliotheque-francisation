# -*- coding: utf-8 -*-
"""Identité de module-n8-recherche — « Passer au travers du processus »
(niveau 8, activité 119, numéro 2 du niveau).

Le slug porte le niveau et nomme la situation plutôt que le scénario :
`module-n8-emploi` (61) occupe déjà « Emploi », et les deux situations sont
voisines au point qu'un slug narratif les aurait mêlées.

CE QUE LE PROGRAMME DEMANDE
---------------------------
`python3 build/cadre.py 8 "Recherche"` rend **trois** intentions, et pas une
de plus :

  · Compréhension orale  — participer à une entrevue de sélection comportant
                           plusieurs étapes ; s'informer sur une entreprise
                           ou sur un emploi.
  · Production orale     — participer à une entrevue de sélection comportant
                           plusieurs étapes.
  · Compréhension écrite — s'informer sur une entreprise ou sur un emploi.

Un défi par intention. « S'informer » se dédouble parce que le programme le
dédouble lui-même : une fois en écoutant (défi 1), une fois en lisant
(défi 2). L'entrevue à plusieurs étapes prend le défi 3 à elle seule — un
processus en trois temps ne se joue pas en une séance.

**Aucune intention de production écrite.** Le courriel de suivi de « Je me
lance » vient donc des attentes de fin de cours du niveau 8, qui demandent que
l'adulte « rédige des lettres ou des courriels d'affaires ayant des objectifs
particuliers en s'assurant que leur forme et leur contenu sont appropriés » et
qu'il « résume les propos de son interlocuteur ». Le noter ici évite qu'un
relecteur retire une tâche qu'il croirait hors programme.

CE QUI LE DISTINGUE DE SES TROIS VOISINS DE SITUATION
-----------------------------------------------------
Écrit avant le scénario, en une phrase par voisin.

  · `module-n3-recherche-emploi` (83) **offre ses services de vive voix** au
    comptoir : on entre quelque part et on demande si ça engage.
  · `module-n6-recherche` (59) **répond à une offre précise** et passe une
    courte entrevue d'embauche.
  · `module-n7-recherche` (110) **s'oriente avant de postuler** : il lit
    l'économie d'une région pour décider où chercher.
  · Celui-ci se passe **pendant** le processus de sélection. L'offre est
    trouvée, la candidature est déposée, et le travail n'est plus de chercher
    mais de **soutenir sa candidature d'un bout à l'autre** — se renseigner
    avant de parler, faire valoir un parcours qui n'entre pas dans la case,
    répondre à l'objection qui n'est jamais formulée, et négocier ce qui n'est
    pas affiché.

Aucun recoupement non plus avec `module-n8-emploi` (61), le seul autre module
du niveau : « Recherche d'emploi », c'est avant l'embauche ; « Emploi », c'est
une fois en poste.

LE SCÉNARIO
-----------
Shirin Tabatabai, 46 ans, arrivée d'Iran il y a neuf ans, chef d'équipe au
contrôle de la qualité dans une usine agroalimentaire de Téhéran pendant onze
ans, aujourd'hui opératrice de production chez un sous-traitant de Sherbrooke.
Elle postule à un poste de superviseure de production chez Boréalis
Emballages, à Sherbrooke, et traverse un processus de sélection en trois
étapes. Alexandre Pouliot-Nadeau, ancien collègue devenu contremaître chez
Boréalis, lui décrit l'entreprise de l'intérieur ; Danielle Éthier,
conseillère en acquisition de talents, mène l'appel de présélection ; Réal
Bourbonnais, directeur de la production, présente l'entreprise aux candidats
retenus, puis siège au comité qui la reçoit.

Boréalis Emballages, les personnes, les adresses, les chiffres de l'entreprise
et le poste sont inventés. Ce qui ne l'est pas est vérifié — voir le journal
de la vague 7 dans `docs/vagues-suivantes.md` : l'article 18.1 de la Charte
des droits et libertés de la personne, les quatorze motifs de l'article 10, et
les durées de congé annuel de la Loi sur les normes du travail.

Le module **vouvoie partout**, y compris entre Shirin et Alexandre, qui se
connaissent pourtant : c'est le registre du processus, et le module travaille
justement la variété de langue.
"""

MANIFESTE = {
    'slug': 'module-n8-recherche',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Recherche d\\'emploi",

    # Pourpre : la couleur du niveau 8. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#7E3F98',
    'accent_doux': '#F3E8F7',

    'ia_oral': "L'élève répond à la question difficile d'une entrevue de "
               "sélection : il annonce d'abord en une phrase ce qu'il va "
               "raconter, puis expose la situation, ce qu'il a fait "
               "lui-même et le résultat obtenu, avec au moins un chiffre "
               "vérifiable. Il nuance avec « cependant » ou « en revanche », "
               "emploie au moins une hypothèse irréelle au conditionnel "
               "passé pour dire ce qu'il ferait autrement, et termine par une "
               "phrase emphatique qui met en relief ce qu'il apporte. Il "
               "vouvoie le comité.",

    'jr_cas': 'superviseure',
    'jr_role': 'candidate',
    'jr_scenario': 'selection',
    'ia_jeu_de_role': "L'élève passe la troisième étape d'un processus de "
                      "sélection : l'entrevue individuelle devant un comité. "
                      "Il répond à des questions ouvertes par des exemples "
                      "datés et chiffrés, fait valoir une expérience acquise "
                      "à l'étranger que personne ne compte, reconnaît sans "
                      "y répondre une question qui porte sur un motif "
                      "interdit, et négocie une condition qui n'est pas "
                      "affichée en proposant une contrepartie.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Passer au travers du "
             "processus » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie',
                          'Beaulieu', 'tendinite',
                          'Consulter au bon endroit', 'physiothérapie'],
}
