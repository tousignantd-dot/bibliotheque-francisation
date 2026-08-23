# -*- coding: utf-8 -*-
"""Identité de module-n4-etablissement — « Prévenir le centre » (niveau 4).

Situation du programme : « Communication avec le personnel de
l'établissement », domaine général de formation « Éducation et monde du
travail ». Activité 108, `numero` 17 du niveau 4, `GRILLE_3_DEFIS`.
C'était le **seul trou** du niveau 4 : les seize autres situations avaient
déjà leur module.

Ce que `python3 build/cadre.py 4 "Communication avec le personnel de
l'établissement"` donne, et rien d'autre — **trois intentions**, une par
compétence, sauf la lecture :

  · CO — écouter un message téléphonique ;
  · PO — justifier un retard, une absence ou un abandon ;
  · PE — justifier un retard, une absence ou un abandon.

C'est le cadre le plus étroit du niveau, et il est étroit d'une façon
particulière : **les trois intentions passent par un appareil**. On écoute
un message enregistré, on en laisse un, on remet une note. À aucun moment
le programme ne demande une conversation en face à face — et c'est
exactement ce qui sépare ce module de ses cinq voisins.

Le lexique, lui, n'est pas vide pour une fois. Trois entrées le nourrissent :
« Mots énonçant les motifs d'un retard, d'une absence ou d'un abandon »,
rattachée à la situation elle-même ; les verbes « raccrocher, décrocher,
peser, appuyer » ; et le « vocabulaire du téléphone : clavier, combiné,
ligne, boîte vocale », classé sous *Emploi* mais qui ne sert nulle part
aussi bien qu'ici. Les seize mots du banc en sortent.

La compréhension écrite n'a **aucune** intention dans cette situation. Le
module n'invente pas de tâche de lecture hors programme : les exercices de
lecture qu'il porte servent la production écrite (relire une note avant de
la remettre, repérer ce qui manque), et le module est catalogué CO · PO ·
CE · PE parce que le portail range les quatre compétences ensemble.

Ce qui distingue ce module de ses voisins — en une phrase
--------------------------------------------------------

**Ici, personne ne se parle : une machine répond, une machine enregistre,
et le papier finit le travail.**

Six modules occupent déjà cette situation ou la frôlent. Ce n'est pas le
sujet qui change, c'est le **travail** :

· `module-n2-inscription` (91, niveau 2) remplit un formulaire au comptoir.
  On **s'inscrit**.
· `module-n2-secretaire` (95, niveau 2) demande un renseignement en une
  phrase, au comptoir. On **demande**.
· `module-n2-couloirs` (niveau 2) cherche un local. On **s'oriente**.
· `module-n3-secretariat` (86, niveau 3) informe le personnel d'une absence,
  de vive voix puis par écrit. On **informe**, en présence.
· `module-travail` (39, niveau 4) téléphone à son superviseur le matin même.
  On **justifie**, mais à un employeur, et quelqu'un décroche.
· `module-procedure` (40, niveau 4) suit une marche à suivre écrite. On
  **exécute des étapes**.
· `module-n5-ecole` (74, niveau 5) expose au comptoir une affaire qui dure.
  On **règle** un problème déjà là.
· `module-n6-etablissement` (102, niveau 6) assemble de quoi choisir un
  programme. On **décide**.

Ici, il est sept heures dix, le centre n'ouvre qu'à huit heures, personne ne
décroche, et Nourhane Ouazzani a exactement une minute de boîte vocale pour
dire qui elle est, pourquoi elle ne viendra pas et quand elle reviendra.
Puis, le soir, ce sont trois messages qui l'attendent sur son propre
téléphone : elle n'a plus personne à qui poser une question, elle doit tout
prendre à l'écoute. Le module travaille donc **le message à sens unique**,
dans les deux directions — c'est ce que dit l'intention « écouter un
message téléphonique », et aucun autre module de la bibliothèque ne le fait.

Le scénario, entièrement inventé
--------------------------------

Nourhane Ouazzani, 36 ans, arrivée du Maroc il y a un an, suit la
francisation à temps plein le jour, groupe 6, au **Centre d'éducation des
adultes de la Pointe-aux-Ormes**, à Laval. Son fils Ilyes, cinq ans, fait
une otite un dimanche soir. Le lundi matin, elle doit rester avec lui ;
le mardi, la garderie n'ouvre qu'à huit heures et elle arrive en retard ;
et le jeudi, elle apprend qu'elle devra abandonner le cours d'informatique
du soir, qu'elle avait pris en plus. Trois motifs — un retard, une absence,
un abandon —, exactement les trois que le programme nomme.

Autour d'elle : **Wilner Céleste**, camarade de classe, qui la tutoie dans
le corridor ; **Murielle Sansregret**, secrétaire du centre, qui la vouvoie ;
**Fabien Corriveau**, l'enseignant du groupe 6 ; et une cinquième voix, celle
du **système téléphonique** du centre, qui ne répond à personne.

Le centre, les personnes, les numéros de téléphone et les dates sont
inventés. Ce qui est réel et se dit tel quel : depuis 2020, une commission
scolaire s'appelle un **centre de services scolaire** ; un centre
d'éducation des adultes offre la francisation à temps plein le jour et à
temps partiel le soir ; les élèves inscrits à temps plein doivent justifier
leurs absences pour garder leur allocation de participation — le module le
dit sans montant ni délai chiffré, parce que ces valeurs changent et qu'un
module ne doit pas les figer.

La progression grammaticale — neuf savoirs sur soixante
-------------------------------------------------------

Le niveau 4 porte soixante savoirs, dont trente-cinq en grammaire de la
phrase. Le critère de tri, ici : **est-ce que ce savoir sert à se faire
comprendre par quelqu'un qui ne peut pas demander de répéter ?** C'est la
contrainte de la boîte vocale, et elle retient d'un coup :

  1. la discrimination de « on », « an » et « in » — les trois voyelles
     nasales du programme, et les trois qui portent le vocabulaire du
     module : bonjour, absence, matin (`prPhon`) ;
  2. les verbes du téléphone et les mots des motifs (`prVocab`, `prMot`) ;
  3. les phrases impératives avec et sans pronom complément, plus la forme
     postverbale et son trait d'union — c'est la langue du menu automatisé
     et celle du message qu'on laisse (`t1imper`) ;
  4. les auxiliaires de modalité : `devoir` au présent, `falloir` au présent
     et au conditionnel de politesse (`t1devoir`) ;
  5. les marqueurs de temps de la progression chronologique — d'abord,
     ensuite, avant de + infinitif, après + infinitif passé (`t1ordre`) ;
  6. la cause, avec et sans marqueur : parce que, à cause de, grâce à
     (`t2cause`) ;
  7. les pronoms compléments `lui` et `leur` et leur référent (`t2lui`) ;
  8. le passé composé, dont l'accord du participe passé avec l'auxiliaire
     être (`t3pc`) ;
  9. le futur simple reconnu en contexte formel, et la présentation
     matérielle d'une note écrite (`t3futur`, `t3note`).

Chacun a son exercice **et** sa mini-leçon : un point de grammaire sans les
deux serait du décor.

D'où viennent les trois productions de « Je me lance »
------------------------------------------------------

Les deux premières sortent directement de la situation : « justifier un
retard, une absence ou un abandon », en production orale d'abord, en
production écrite ensuite. La troisième — le jeu de rôle — n'est pas une
intention du programme : c'est la **répétition** avant les deux autres, et
elle sert la même intention à l'oral, dans le seul cas où quelqu'un décroche.

Le scénario `repondeur` a été ajouté à `server.py` pour ce module. Aucun
scénario existant ne convenait : `secretariat` (niveau 3) et `ecole`
(niveau 5) se passent au comptoir, `conge` s'adresse à un chef d'équipe, et
`absence` (niveau 2) est un échange de quatre répliques avec l'enseignante.
Ici, l'élève téléphone, et la personne au bout du fil n'a **rien** sous les
yeux : ni le nom, ni le groupe, ni la date.

Le tutoiement et le vouvoiement
-------------------------------

Le module **vouvoie** l'élève d'un bout à l'autre, écran de fin compris :
tout s'y passe avec un secrétariat, un enseignant ou une machine. Le seul
tutoiement est celui de Wilner, dans le dialogue d'entrée, et il est là
exprès — pour que la bascule s'entende dès la première minute.
"""

MANIFESTE = {
    'slug': 'module-n4-etablissement',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # L'apostrophe est échappée : le thème est injecté dans une chaîne
    # JavaScript à guillemets simples au moment du dépôt de la production
    # orale. Non échappée, elle ferme la chaîne et l'envoi meurt.
    'theme': "Communication avec le personnel de l\\'établissement",

    # Or : la couleur du niveau 4. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#8C6A07',
    'accent_doux': '#F7F0DA',

    'ia_oral': "L'élève laisse un message dans la boîte vocale du "
               "secrétariat d'un centre d'éducation des adultes pour "
               "justifier un retard, une absence ou un abandon. Personne ne "
               "peut lui demander de répéter : il se nomme et donne son "
               "groupe dès la première phrase, il dit clairement de quel "
               "jour il parle, il donne le motif en une seule phrase avec "
               "« parce que » ou « à cause de », il dit au futur simple ce "
               "qu'il fera — « je serai là demain », « je rapporterai le "
               "papier » — et il termine par son numéro de téléphone, dit "
               "lentement, chiffre par chiffre. Il vouvoie du début à la "
               "fin. Corrigez en priorité ce qui empêcherait la personne du "
               "secrétariat de comprendre à la première écoute : le nom, le "
               "groupe, la date et le numéro.",

    'jr_cas': 'garderie',
    'jr_role': 'eleve',
    'jr_scenario': 'repondeur',
    'ia_jeu_de_role': "L'élève téléphone au secrétariat d'un centre "
                      "d'éducation des adultes pour justifier un retard, une "
                      "absence ou un abandon. Cette fois, quelqu'un décroche. "
                      "Il se nomme et donne son groupe avant tout, il dit de "
                      "quel jour il parle, il donne son motif en une phrase, "
                      "il comprend ce qu'on lui demande de faire ensuite — un "
                      "papier, une note, un rappel — et il redit à voix haute "
                      "ce qu'il a compris avant de raccrocher.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Prévenir le centre » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie',
                          'Beaulieu', 'tendinite', 'Consulter au bon endroit',
                          'physiothérapie'],
}
