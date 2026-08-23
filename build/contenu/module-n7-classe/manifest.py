# -*- coding: utf-8 -*-
"""Identité de module-n7-classe — « Faire parler l'équipe » (niveau 7).

Situation « Salle de classe » du programme, domaine Éducation et monde du
travail. Cinq intentions, et elles se lisent comme un plan de travail :
comprendre de l'information reliée à un sujet de recherche (à l'oral), la
comprendre à l'écrit, faire un exposé sur un sujet concret, résumer un texte
relié à son champ d'intérêt, rédiger une lettre personnelle destinée à un
camarade de classe.

**Pourquoi trois défis.** La grille était « au choix » dans le tableau de la
vague 7. Cinq intentions ne suffisent pas à trancher — le test du pilote du
niveau 6 est de pouvoir nommer trois façons distinctes d'entrer dans la
situation, chacune avec son dialogue et ses six exercices, sans qu'aucune ne
soit « Je me lance » déguisé. Elles se nomment ici sans forcer :

· **écouter quelqu'un qui sait** — la personne-ressource invitée en classe,
  ses chiffres, ses estimations, le plan qu'elle annonce ;
· **lire, trier, résumer** — la documentation écrite, et le passage du texte
  long au résumé de dix lignes ;
· **faire parler l'équipe** — animer la rencontre, arbitrer un désaccord,
  reformuler, et rapporter ce que chacun a dit.

Le troisième défi n'empiète pas sur « Je me lance » : on y apprend à *conduire*
la parole des autres et à la *rapporter* (discours indirect au passé), alors
que « Je me lance » fait produire à l'élève son propre exposé et sa propre
lettre. Le piège relevé par `module-n6-classe` — le troisième défi qui répète
la section suivante — a été vérifié avant de trancher : ici, ce qui se
travaille au défi 3 est l'animation, et l'animation n'est nulle part ailleurs.

**Ce qui distingue ce module de ses trois voisins de situation**, en une
phrase, écrite avant que le scénario soit inventé : au niveau 1
(`module-n1-classe`) on comprend une consigne de deux mots ; au niveau 2
(`module-n2-classe`) on demande une permission ; au niveau 6
(`module-n6-classe`) Milagros **exécute** un travail de recherche qu'on lui
donne, avec ses trois sources et sa grille d'évaluation. Ici, Neusa **anime le
travail des autres** — elle fait parler, elle arbitre un désaccord entre deux
coéquipiers, et elle rend compte à celui qui n'était pas là. Le sujet de
recherche n'est pas l'objet du module : c'est le prétexte. L'objet, c'est la
conduite de la parole d'un groupe.

**D'où viennent les trois productions.** Elles ne s'inventent pas : trois des
cinq intentions de la situation sont productives, et les trois tâches de
« Je me lance » les reprennent une à une — « faire un exposé sur un sujet
concret » (la production orale), « rédiger une lettre personnelle destinée à
un camarade de classe » (la production écrite, adressée au coéquipier absent),
et le jeu de rôle qui sert de répétition à l'animation. Le résumé, quatrième
intention, est travaillé au défi 2 plutôt qu'en production finale : il est
l'outil de la lettre, pas sa concurrence.

**Les faits sont vérifiés, pas devinés** (23 août 2026), et la municipalité est
inventée. Les faits retenus sur le sujet de recherche de l'équipe sont
généraux, établis et enseignés partout : un **îlot de chaleur** est un secteur
dont la température de surface dépasse celle des secteurs voisins, parce que
l'asphalte et les toits sombres absorbent le rayonnement solaire et le
restituent en chaleur ; un arbre rafraîchit de deux façons, par l'**ombre**
qu'il porte et par l'**évapotranspiration**, l'eau qu'il rejette par ses
feuilles ; la **canopée** est la couverture formée par la cime des arbres, vue
d'en haut, et se mesure en pourcentage de la surface d'un territoire ; les
grandes chaleurs sont un risque de santé pour les personnes âgées, les jeunes
enfants et les personnes qui travaillent dehors ; un jeune arbre de rue a
besoin d'arrosage pendant ses premières années, et ses racines peuvent
soulever un trottoir si la fosse de plantation est trop étroite.

Mais **Rivière-Noire, son bulletin municipal, ses pourcentages, ses rues et
ses dates n'ont aucun modèle réel.** C'est le cran de prudence que
`module-n6-classe` a nommé le premier, et il vaut ici pour la même raison :
attribuer une page d'information fabriquée à une vraie ville produirait un faux
document, et un élève la citerait de bonne foi dans un vrai travail. Ici comme
là, la source inventée est le matériel même de l'exercice.

Tout le reste est inventé : les personnes — Neusa Marinho, Ghislaine Turcotte,
Perrine Auclair, Youssouf Bangoura, Miguel Ospina —, le Centre d'éducation des
adultes de la Pointe-aux-Ormes, l'organisme Vert-Rivière, la ville de
Rivière-Noire et tous ses chiffres.

**Le casting a été compté avant que les dialogues soient écrits**, comme le
demande le journal de l'activité 115 : le dépôt a quatre voix, deux féminines
et deux masculines, et deux personnages ne peuvent en partager une que s'ils ne
se répondent jamais dans un même extrait. Ce module a cinq personnages, et une
salle de classe en réunit naturellement trois ou quatre à la fois. Les quatre
dialogues ont donc été répartis pour ne jamais mettre trois voix du même genre
dans une même scène : prep et t1 et t2 font parler deux femmes et un homme, t3
une femme et deux hommes. C'est ce qui a décidé du genre de Miguel Ospina.
"""

MANIFESTE = {
    'slug': 'module-n7-classe',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`, source
    # unique. Les redéfinir ici arrête le build.

    'theme': 'Salle de classe',

    # Indigo : la couleur du niveau 7. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#3B49A0',
    'accent_doux': '#E8EAFA',

    'ia_oral': "L'élève fait un exposé de trois ou quatre minutes devant sa "
               "classe sur le sujet de recherche de son équipe : il annonce "
               "son plan, présente ce que l'équipe a trouvé, rapporte ce que "
               "les coéquipiers ont dit, puis conclut. Il emploie des "
               "connecteurs qui marquent les étapes (d'abord, ensuite, "
               "enfin, en somme), le discours indirect au passé pour "
               "rapporter les propos de l'équipe, et des phrases emphatiques "
               "pour mettre en relief ce qui compte. Il vouvoie son "
               "auditoire.",

    'jr_cas': 'desaccord',
    'jr_role': 'animateur',
    'jr_scenario': 'equipe',
    'ia_jeu_de_role': "L'élève anime une rencontre d'équipe en classe : il "
                      "ouvre la rencontre, donne la parole, fait préciser, "
                      "reformule ce qu'il vient d'entendre, arbitre un "
                      "désaccord sans donner raison trop vite, et termine en "
                      "résumant les décisions. Il emploie le conditionnel de "
                      "politesse, la concession (bien que, même si), les "
                      "connecteurs de topicalisation (quant à, en ce qui "
                      "concerne) et de reformulation (autrement dit, en "
                      "somme).",

    # L'apostrophe s'échappe : les deux valeurs sont injectées dans la même
    # chaîne JavaScript à guillemets simples.
    'bravo': "🎉 Bravo, vous avez terminé le module « Faire parler "
             "l\\'équipe » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
