# -*- coding: utf-8 -*-
"""Identité de module-n8-oeuvres — « Ce que l'œuvre ne dit pas ».

Niveau 8, situation « Découverte d'œuvres littéraires, musicales,
cinématographiques et télévisuelles », domaine général de formation « Culture
et médias ». Activité 123, `numero` 6 du niveau. Slug et numéro réservés dans
`docs/vagues-suivantes.md`, vague 7.

**C'est le dernier module du programme.** Avec lui, les huit niveaux sont
couverts en entier : 123 activités, aucune situation sans son module.

Ce que `python3 build/cadre.py 8 "Découverte d’œuvres…"` donne, et rien
d'autre : **deux intentions, toutes deux de réception**.

  · CO — comprendre un film, une télésérie, un téléroman ou une pièce de
    théâtre ;
  · CE — comprendre une nouvelle ou un texte poétique.

C'est le cadre le plus maigre du niveau — deux intentions sur les vingt-cinq
du cours — et le niveau, lui, porte cinquante-huit savoirs. La note de
l'activité 119 (« la situation est maigre, le niveau est énorme, et les deux à
la fois ») décrit exactement ce module-ci, et son critère de tri s'y transpose
d'un mot : **« est-ce que ce savoir sert à tenir ensemble deux lectures
défendables du même passage ? »**

**Ni production orale ni production écrite dans la situation.** Les deux
tâches de « Je me lance » viennent donc des **attentes de fin de cours**, qui
sont productives et communes à tout le cours : à l'oral, « au cours d'une
discussion, il émet des commentaires sur un sujet en les justifiant » et « il
résume les propos de son interlocuteur » ; à l'écrit, « il rédige une lettre
destinée au courrier des lecteurs pour donner son opinion sur un évènement
tout en la justifiant » et « il résume un texte d'opinion ». La lettre au
courrier des lecteurs est nommée mot pour mot par le programme, et elle répond
ici à la critique lue au défi 3. C'est écrit ici **et** dans `custom.js` pour
qu'un relecteur ne retire pas ces tâches en les croyant hors programme.

**Ce qui distingue ce module de ses trois voisins de situation**, en une
phrase écrite avant le scénario : `module-n5-oeuvres` (73) **raconte** une
œuvre aimée devant un club qui écoute, `module-n6-oeuvres` (103) **résume** un
film et nuance son avis par écrit, `module-n7-oeuvres` (116) **défend un avis
devant quelqu'un qui ne le partage pas** — et ici on ne défend plus un avis,
on défend une **lecture** : deux personnes qui ont vu la même scène, qui
s'entendent sur tout ce qui s'y passe, et qui n'en tirent pas la même
histoire. C'est le seul module du dépôt où le désaccord ne porte pas sur le
goût mais sur le **sens**, et où l'on apprend qu'une interprétation se juge à
ce qu'elle laisse expliquer, jamais à la force avec laquelle on l'affirme.

Les dix savoirs retenus sur les cinquante-huit du niveau :

  · l'intonation expressive — surprise, admiration, déception,
    incompréhension : le **seul** savoir de phonétique du niveau, traité comme
    l'activité 119 l'a établi, en répliques entières et jamais en symboles
    (Je découvre) ;
  · la reprise de l'information et les connecteurs de reformulation —
    autrement dit, en d'autres termes, c'est-à-dire : dire ce qu'on a compris
    avec d'autres mots que ceux de l'autre (Je découvre) ;
  · l'indicatif conditionnel passé — « elle aurait pu détacher la corde » :
    le temps de ce qui ne s'est pas produit, et le premier outil de
    l'interprétation (Défi 1) ;
  · l'hypothèse irréelle du passé, si + plus-que-parfait / conditionnel passé
    (Défi 1) ;
  · les phrases emphatiques par clivage et pseudoclivage — « ce qui compte,
    c'est », « c'est la corde qui » : la forme même d'une lecture qu'on
    avance (Défi 1) ;
  · l'indicatif passé simple et l'indicatif plus-que-parfait — les deux temps
    du récit littéraire, qu'on ne parle pas mais qu'il faut lire (Défi 2) ;
  · le subjonctif présent après les déclencheurs du doute — il se peut que,
    il est possible que, bien que —, opposé à l'indicatif après « il me semble
    que » (Défi 2) ;
  · les subordonnées relatives à préposition — dont, ce dont, à quoi, auquel,
    sur lequel : citer un passage sans le répéter en entier (Défi 3) ;
  · la concession et l'opposition — bien que + subjonctif, même si +
    indicatif, quoique, alors que, en revanche (Défi 3) ;
  · la ponctuation du discours rapporté et la frontière entre citer, résumer
    et déformer (Défi 3).

**Aucune œuvre réelle n'est nommée nulle part**, et c'est la contrainte propre
à cette situation. La télésérie « Les eaux basses » et sa réalisatrice Solange
Béliveau-Trahan, la nouvelle « La chaise du fond » et son auteure Odile
Brassard-Vézina, le poème « Déneigement » de Régine Amyot, la pièce « Le
troisième rang » de Damien Larochelle, l'hebdomadaire « L'Écho des
Deux-Rives » et le critique Gaspard Thivierge sont **inventés de toutes
pièces**. Attribuer une fausse réplique, une fausse date ou une fausse
critique à une œuvre qui existe serait fabriquer un faux document. Les mots du
métier — une fin ouverte, un plan fixe, un recueil, une strophe, le courrier
des lecteurs — sont, eux, ceux qu'on emploie réellement au Québec.

Une œuvre inventée pour ce module-ci devait en plus **soutenir deux lectures
opposées**, ce qui ne s'improvise pas après coup : la dernière scène des
« eaux basses » a été écrite indice par indice, chacun rattachable à l'une ou
l'autre des deux lectures, et deux d'entre eux aux deux à la fois. C'est ce
qui rend l'exercice `t1deux` faisable, et c'est ce qui aurait manqué si
l'œuvre avait été esquissée en trois lignes.
"""

MANIFESTE = {
    'slug': 'module-n8-oeuvres',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    # L'apostrophe est échappée : le thème est injecté dans une chaîne
    # JavaScript à guillemets simples au moment du dépôt de la production.
    'theme': "Découverte d\\'œuvres",

    # Pourpre : la couleur du niveau 8. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#7E3F98',
    'accent_doux': '#F3E8F7',

    'ia_oral': "L'élève prend la parole deux ou trois minutes dans un cercle "
               "de lecture : il propose une lecture d'une œuvre qu'il a vue, "
               "lue ou entendue, dont la fin reste ouverte. Il distingue ce "
               "qui se passe dans l'œuvre de ce qu'il en comprend, il appuie "
               "sa lecture sur au moins deux détails précis, il nomme "
               "lui-même la lecture opposée et dit ce qu'elle explique mieux "
               "que la sienne, puis il conclut sans prétendre trancher. Il "
               "emploie une phrase emphatique pour mettre en relief l'indice "
               "qui compte le plus, une hypothèse irréelle du passé, et le "
               "subjonctif après « il se peut que ». Il vouvoie le cercle.",

    'jr_cas': 'finale',
    'jr_role': 'fatoumata',
    # Le scénario s'appelle « interpretation » : « oeuvres » est pris par
    # module-n5-oeuvres (73) et « avisoeuvre » par module-n7-oeuvres (116).
    # Une clé en double dans JEU_DE_ROLE_SCENARIOS ne lève AUCUNE erreur —
    # Python garde silencieusement la dernière, et le module jouerait le
    # scénario d'un autre niveau, avec des rôles qui ne sont pas les siens.
    'jr_scenario': 'interpretation',
    'ia_jeu_de_role': "L'élève discute d'une fin ouverte avec quelqu'un qui a "
                      "vu la même scène et n'en tire pas la même histoire. Il "
                      "commence par dire ce qui se passe, sans "
                      "l'interpréter ; il appuie chaque lecture sur un détail "
                      "qu'on peut montrer ; il reformule la lecture de "
                      "l'autre avant d'y répondre — autrement dit, si je vous "
                      "suis bien ; il concède avec « bien que » suivi du "
                      "subjonctif et oppose avec « même si » suivi de "
                      "l'indicatif ; il emploie une hypothèse irréelle du "
                      "passé et une phrase emphatique. Il ne cherche pas à "
                      "avoir raison : il cherche la lecture qui explique le "
                      "plus de détails.",

    # L'apostrophe s'échappe : les deux valeurs sont injectées dans la même
    # chaîne JavaScript à guillemets simples.
    'bravo': "🎉 Bravo, vous avez terminé le module "
             "« Ce que l\\'œuvre ne dit pas » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
