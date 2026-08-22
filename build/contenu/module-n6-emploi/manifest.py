# -*- coding: utf-8 -*-
"""Identité de module-n6-emploi — « Le poste affiché à l'interne ».

Niveau 6, situation « Emploi », domaine « Éducation et monde du travail ».
Activité 100, module 3 du niveau. Vague 6. Le pilote du niveau (activité 99,
`module-n6-actualite`) a écrit ce qui résiste au stade intermédiaire ; sa note
est dans `docs/vagues-suivantes.md`, section « Le pilote du niveau 6 ».

Ce que `python3 build/cadre.py 6 "Emploi"` donne, et rien d'autre : **cinq
intentions**, et c'est la situation la mieux fournie du niveau.

  · CO — comprendre des explications sur les étapes d'une démarche
    administrative ;
  · PO — décrire les étapes d'une démarche administrative ;
  · CE — lire de la documentation interne reliée à son emploi ;
  · CE — lire un compte rendu ;
  · PE — rédiger un courriel dans le contexte de relations professionnelles.

D'où vient chaque morceau du module
-----------------------------------
Contrairement au pilote, **les deux productions de « Je me lance » viennent de
la situation elle-même**, pas des attentes de fin de cours : la production
orale est l'intention PO mot pour mot (« décrire les étapes d'une démarche
administrative »), la production écrite l'intention PE (« rédiger un courriel
dans le contexte de relations professionnelles »). Les attentes de fin de
cours ne servent ici qu'à fixer le niveau d'exigence — « il décrit les étapes
d'une démarche administrative en donnant les détails nécessaires », « dans ses
relations professionnelles, il rédige un courriel ou une lettre en respectant
les conventions habituelles », « il rédige un court texte en organisant ses
idées à l'aide de paragraphes ».

Les trois défis sont **trois retours sur le même dossier**, sous trois genres,
selon la formule du pilote : le niveau 6 n'est pas un niveau 7 facile, c'est
le niveau de la cohésion. Le dossier est une candidature à un poste affiché à
l'interne. Défi 1, on la lui explique de vive voix (CO). Défi 2, elle la
retrouve écrite dans la documentation interne — note de service et politique
(CE). Défi 3, elle la relit dans le compte rendu de la rencontre
d'information (CE). Rien ne se répète : ce qui change à chaque retour, c'est
le genre, sa mise en page et les marques de cohésion qu'il emploie.

Les neuf savoirs retenus, sur les cinquante-quatre du niveau, le sont par la
question du pilote — « est-ce que ce savoir sert à suivre un texte ? » :
formation des mots et nominalisation ; graphie-phonie (ch qui dit k, x qui dit
s, sh et sch qui disent ch) ; l'ordre des étapes d'une consigne à partir
d'indices autres que les connecteurs de temps ; le subjonctif présent après
verbe introducteur ; la reprise de l'information par « le », « en » et « y » ;
la présentation matérielle et la mise en page ; la relative en « où »,
complément de lieu ou de temps ; le plus-que-parfait d'antériorité ; le passé
simple reconnu à la 3e personne et associé au passé composé ; l'hypothèse
réaliste avec « si » ; et la disposition d'un courriel formel. Les trois
savoirs de grammaire du texte — connecteurs, reprise, présentation matérielle
— sont là tous les trois, comme le pilote le recommande.

Le passé simple se travaille en **`match`** (`t3ps`), jamais en `write` : le
programme demande de le *reconnaître*, et faire écrire un passé simple à un
élève de niveau 6 est exactement ce qu'il ne faut pas. Les exercices de
grammaire du texte sont tous en `cols:1` : leurs items font deux phrases.

Le lexique de la situation est vide, comme presque partout. Les seize mots
sont composés à partir des savoirs lexicaux **du niveau** qui la nomment :
« vocabulaire lié au milieu du travail : notes de service, collaborateurs,
personnel, ordre du jour, etc. » et, pour ce qui touche aux conditions,
« mots servant à la description des conditions de travail : salaire, horaire,
tâches, exigences, compétences, qualifications professionnelles, formation,
disponibilité, avantages sociaux ».

Deux exercices de type `texte`
------------------------------
`t2note` et `t2polit` sont des exercices `texte` — le type versé au moteur le
22 août 2026 pour les niveaux 6 à 8, à la demande du pilote. C'est l'endroit
juste : l'intention « lire de la documentation interne » porte sur un texte
suivi, pas sur des phrases isolées, et l'élève doit pouvoir cliquer **dans**
la note de service pour montrer le passage qui répond. Un `vf` aurait rendu
les mêmes questions en séparant l'élève de son texte.

Les voisins, et ce qui l'en sépare
----------------------------------
· `module-travail` (39, niveau 4) est le module de l'absence : prévenir son
  superviseur, justifier un retard, écrire un courriel d'excuse. On y parle à
  son patron d'un empêchement. Ici, personne n'est absent et rien ne va mal :
  le module est celui d'une démarche qu'on entreprend soi-même, avec des
  étapes, des délais et des documents.
· `module-n3-horaire` (84, niveau 3) tient debout pendant le quart : lire son
  horaire, demander une permission, comprendre une consigne, noter une
  directive. Sa langue est celle de l'instant — l'heure, la tâche, la question
  qu'on ose poser. Ici on ne travaille pas : on lit trois documents qui
  parlent du même dossier et on suit ce que chacun reprend de l'autre.
· `module-n6-recherche` (59, même niveau) cherche un emploi qu'on n'a pas
  encore : l'offre, la demande, l'entrevue devant un employeur inconnu. Ici
  l'emploi est acquis depuis deux ans, l'employeur connaît la candidate, et
  toute la difficulté est ailleurs — dans une procédure interne écrite, dans
  des documents qu'il faut savoir lire, et dans des délais qui courent.
· `module-n5-travail` (67, niveau 5) traite des relations d'équipe, et
  `module-n8-emploi` (61, niveau 8) d'une erreur de paie et d'une réunion où
  il faut tenir son bout. Ni l'un ni l'autre ne lit de documentation interne.

Tout est inventé, et la politique de dotation aussi
---------------------------------------------------
Le pilote a dû vérifier des faits de droit auprès de l'Office de la protection
du consommateur. Ici, **rien n'est présenté comme la loi** : la démarche
décrite est la procédure interne d'une entreprise fictive, écrite par elle.
Les dix jours ouvrables d'affichage, le formulaire RH-04, le comité de deux
personnes, la période d'essai de trente jours travaillés, le droit de retour
au poste antérieur, la réponse écrite dans les cinq jours — ce sont des règles
d'employeur, jamais des articles de loi, et le module le dit à l'élève en
toutes lettres au Défi 2. Yaneth Mosquera, Ghislain Tanguay, Marie-Soleil
Grenon, Patrice Léveillé, l'usine « Emballages Bocage » de Saint-Hyacinthe,
son babillard et sa cafétéria sont inventés. Prêter une politique inventée à
une entreprise réelle en ferait un faux document.

Le module **tutoie l'élève** partout, comme le pilote. Dans les dialogues,
Yaneth tutoie Ghislain, son chef d'équipe depuis deux ans, et vouvoie
Marie-Soleil des ressources humaines, qu'elle rencontre pour la première fois :
c'est l'usage de l'usine, et le contraste est lui-même une matière du niveau
(« respecter les conventions de la communication » et « saisir les rapports
entre des interlocuteurs » sont deux savoirs du cours).
"""

MANIFESTE = {
    'slug': 'module-n6-emploi',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Emploi',

    # Acier : la couleur du niveau 6. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#1D6B8F',
    'accent_doux': '#E7F0F6',

    'ia_oral': "L'élève décrit à quelqu'un les étapes d'une démarche "
               "administrative de son milieu de travail : poser sa "
               "candidature à un poste affiché à l'interne. Il dit d'abord de "
               "quoi il s'agit et où il l'a appris, il énumère ensuite les "
               "étapes dans l'ordre en donnant les détails nécessaires — le "
               "formulaire, le délai, le comité, la période d'essai —, il "
               "emploie au moins un connecteur d'exemplification pour "
               "illustrer un point, et il termine par ce qu'il compte faire. "
               "Il tutoie son interlocuteur.",

    'jr_cas': 'affichage',
    'jr_role': 'yaneth',
    'jr_scenario': 'demarcheinterne',
    'ia_jeu_de_role': "L'élève explique à un collègue les étapes de la "
                      "démarche interne : il résume ce que disent les "
                      "documents, il reprend les étapes dans l'ordre sans en "
                      "sauter, il répond aux objections sans se fâcher, il "
                      "distingue ce que la politique écrit de ce qu'il en "
                      "pense, et il emploie « si » pour poser une hypothèse "
                      "réaliste.",

    'bravo': "🎉 Bravo, tu as terminé le module « Le poste affiché à "
             "l\\'interne » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
