# -*- coding: utf-8 -*-
"""Identité de module-n6-habitation — « Faire faire des travaux ».

Niveau 6, situation « Problèmes reliés à l'habitation », domaine « Habitation
et déplacement ». Activité 106, module 9 du niveau. Vague 6. Le pilote du
niveau (activité 99, `module-n6-actualite`) a écrit ce qui résiste au stade
intermédiaire ; sa note est dans `docs/vagues-suivantes.md`, section « Le
pilote du niveau 6 ».

Ce que `python3 build/cadre.py 6 "Problèmes reliés à l'habitation"` donne, et
rien d'autre : **une seule intention**, portée deux fois, en compréhension
orale et en production orale —

  · CO/PO — comprendre de l'information et poser des questions reliées à des
    travaux de réparation ou de rénovation.

C'est la situation la plus maigre du niveau avec « Location d'un logement » et
« Salle de classe ».

Trois défis, et pourquoi
------------------------
Le tableau du pilote réservait `GRILLE_2_DEFIS` à cette situation, une
intention valant deux défis. Le module en prend **trois**, et c'est le vrai
test du pilote qui tranche — « peut-on nommer trois façons distinctes d'entrer
dans la situation, chacune avec son dialogue et ses exercices ? ».

L'intention unique est elle-même **double** : *comprendre de l'information* et
*poser des questions*. Ce sont deux travaux, et ils ne se font pas dans la
même séance. S'y ajoute l'écrit, que la situation ne demande pas mais que les
attentes de fin de cours réclament.

  · **Défi 1 · Le diagnostic** — on comprend. Un homme de métier explique de
    vive voix ce qu'il a trouvé et pourquoi ça s'est produit. L'élève reçoit.
  · **Défi 2 · Les papiers du chantier** — on lit. Un rapport d'inspection et
    une soumission détaillée, deux exercices de type `texte`. Genre écrit,
    mise en page, langue administrative.
  · **Défi 3 · Quand le plan change** — on demande. Le chantier découvre autre
    chose que ce qui était prévu, quatre personnes en parlent en même temps, et
    c'est l'élève qui doit poser la question qui manque et décider.

Le troisième ne répète pas le deuxième : il change de genre (une rencontre à
quatre voix), de temps (le futur simple et l'hypothèse en « si », là où le
diagnostic était au plus-que-parfait) et de rôle — l'élève n'y reçoit plus de
l'information, il en réclame. Inventer une séance sans contenu reste pire que
de n'en pas avoir ; ici le contenu existe, et le laisser dehors aurait laissé
la moitié productive de l'intention sans défi à elle.

Les trois défis sont **trois retours sur le même dossier**, selon la formule
du pilote : le niveau 6 n'est pas un niveau 7 facile, c'est le niveau de la
cohésion. Le dossier est un seul chantier — aménager le sous-sol d'une petite
maison de 1961 pour y loger sa mère — repris sous trois genres.

D'où vient chaque morceau
-------------------------
La **production orale** de « Je me lance » vient de l'intention elle-même :
poser des questions reliées à des travaux de rénovation, et redire à quelqu'un
ce qu'un homme de métier a expliqué. La **production écrite**, elle, n'a
aucune intention dans cette situation : elle est tirée des **attentes de fin
de cours**, qui sont communes à tout le niveau — « l'adulte rédige un court
texte en organisant ses idées à l'aide de paragraphes » et « dans ses
relations professionnelles, il rédige un courriel ou une lettre en respectant
les conventions habituelles ». Le module écrit donc un courriel à
l'entrepreneur, en trois paragraphes. Ce n'est pas une tâche hors programme :
c'est une attente de fin de cours, et elle est nommée ici pour que personne ne
la retire en croyant bien faire.

Les deux exercices de type `texte` — `t2rapport` (le rapport d'inspection) et
`t2soum` (la soumission) — sont là pour la même raison : les attentes de
lecture du niveau portent sur un **texte suivi**, et le type a été versé au
moteur le 22 août 2026 pour les niveaux 6 à 8. Un `vf` aurait posé les mêmes
questions en séparant l'élève de son texte ; ici il clique **dans** le
rapport.

Les savoirs retenus
-------------------
Douze, sur les cinquante-quatre du niveau, choisis par la question du pilote —
« est-ce que ce savoir sert à suivre un texte ? » :

  · Je découvre — la graphie-phonie du niveau (ch qui dit k, x qui dit s, sh et
    sch qui disent ch) ; la formation des mots des travaux (préfixes ré- et
    dé-, suffixes -age, -ment, -tion, -able).
  · Défi 1 — la reprise de l'information par « le », « en » et « y » ; le
    plus-que-parfait d'antériorité ; les auxiliaires factitifs « faire » et
    « laisser » + infinitif, qui sont la grammaire même du titre du module.
  · Défi 2 — la présentation matérielle et la mise en page d'un écrit
    technique ; la subordonnée relative avec « où », complément de lieu ou de
    temps ; le subjonctif présent après verbe introducteur ; le passé simple
    reconnu à la 3e personne et associé au passé composé.
  · Défi 3 — l'hypothèse réaliste avec « si » ; la question précise (« quel »,
    « quelle », et la subordonnée infinitive interrogative) ; les connecteurs
    d'exemplification et de point de vue.

Les trois savoirs de grammaire du texte que le pilote juge indispensables au
niveau — connecteurs, reprise de l'information, présentation matérielle — y
sont tous les trois. Le **passé simple se travaille en `match`** (`t2ps`),
jamais en `write` : le programme demande de le *reconnaître*. Les exercices de
grammaire du texte sont en `cols:1`, leurs items faisant deux phrases.

Le lexique de la situation tient en une ligne dans le programme — « mots liés
aux travaux de réparation, de rénovation ou d'entretien : toiture, plancher,
béton, asphalte, etc. » — et les seize mots du module en sortent, complétés
par le savoir lexical « exploiter des champs lexicaux pour exprimer le détail
ou la nuance ».

Les voisins, et ce qui l'en sépare
----------------------------------
· `module-probleme` (45, niveau 4) est le module du **locataire qui signale** :
  le calorifère du 4B, les parties communes encombrées, l'insalubrité, l'avis
  écrit, le recours. Le rapport y est d'abord un rapport de force avec une
  propriétaire.
· `module-n5-degat` (62, niveau 5) est le module du **locataire qui raconte un
  sinistre** : l'eau tombée du plafond pendant la nuit, le constat, l'avis de
  travaux affiché dans l'entrée, la réclamation d'assurance et la réduction de
  loyer. Rien n'y est voulu ; tout y est subi.
· Ici, personne n'est locataire et rien n'est arrivé pendant la nuit. La
  maison appartient à celle qui parle, les travaux sont **voulus, choisis et
  payés** par elle, et il n'y a personne à convaincre : il y a un métier à
  comprendre. Toute la difficulté est de suivre une explication technique qui
  se tient, de lire deux écrits qui ne disent pas la même chose, et de poser
  la question qui manque avant de signer. C'est le seul des trois modules où
  l'élève est celui qui **décide et qui paie**.
· `module-n3-loyer` (81) et `module-n5-logement` (58) cherchent et louent un
  logement ; ils n'ont rien à voir avec un chantier.

Ce qui est vérifié, et ce qui est inventé
-----------------------------------------
Trois faits québécois sont **vérifiés**, pas devinés, et le module ne dit rien
d'autre au titre de la règle :

  1. Au Québec, un entrepreneur qui exécute ou fait exécuter des travaux de
     construction pour autrui doit détenir une **licence de la Régie du
     bâtiment du Québec**, et cette licence se vérifie dans le registre public
     des détenteurs de licence de la Régie.
  2. La plupart des municipalités exigent un **permis** pour certains travaux
     de rénovation. Les exigences varient d'une municipalité à l'autre : elles
     se demandent à sa propre municipalité, et à personne d'autre. Le module ne
     prête donc aucune règle chiffrée à une ville réelle.
  3. Avant de creuser, la localisation gratuite des infrastructures
     souterraines se demande à **Info-Excavation**.

Tout le reste est inventé, et devait l'être : Doïna Petrescu, son conjoint
Marius, sa mère Aurica, le voisin Léandre Bergevin, l'entrepreneur général
Fernand Trudelle et son entreprise, l'inspectrice en bâtiment Kettly Alcindor
et sa firme, Réjean Toupin du service des permis, la maison de 1961 de la rue
des Mésanges, les montants, les dates, les délais et les numéros de
soumission. Aucune soumission, aucun rapport et aucun avis du module ne porte
le nom d'une entreprise ou d'un organisme réels : ce serait un faux document.
Aucun montant du module ne prétend représenter un prix courant.

Le module **tutoie l'élève** partout. Dans les dialogues, Doïna tutoie son
voisin Léandre, qu'elle connaît depuis deux ans, et vouvoie Fernand Trudelle,
Kettly Alcindor et Réjean Toupin, qui travaillent pour elle ou pour la ville :
c'est l'usage, et le contraste est lui-même une matière du niveau
(« respecter les conventions de la communication » et « saisir les rapports
entre des interlocuteurs » sont deux savoirs du cours).
"""

MANIFESTE = {
    'slug': 'module-n6-habitation',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Logement',

    # Acier : la couleur du niveau 6. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#1D6B8F',
    'accent_doux': '#E7F0F6',

    'ia_oral': "L'élève redit à quelqu'un ce qu'un homme de métier lui a "
               "expliqué au sujet de travaux de rénovation, puis pose les "
               "questions qui restent. Il nomme d'abord le problème et sa "
               "cause, il rapporte ensuite le diagnostic dans l'ordre — ce "
               "qui s'était produit avant, ce qu'on va faire faire, ce qu'on "
               "laisse sécher —, il donne au moins un chiffre précis (un "
               "montant, un délai, une mesure), il emploie un connecteur "
               "d'exemplification pour illustrer un point, puis il formule "
               "deux vraies questions, précises, du genre de celles qu'on "
               "pose avant de signer. Il tutoie son interlocuteur.",

    'jr_cas': 'diagnostic',
    'jr_role': 'doina',
    'jr_scenario': 'travauxrenovation',
    'ia_jeu_de_role': "L'élève mène l'échange avec un homme de métier : il "
                      "redit ce qu'il a compris pour le faire confirmer, il "
                      "pose des questions précises sur le prix, le délai, ce "
                      "qui est inclus et ce qui ne l'est pas, il demande "
                      "qu'on lui explique un mot technique au lieu de faire "
                      "semblant de le connaître, il pose une hypothèse "
                      "réaliste avec « si », et il distingue ce que la "
                      "soumission écrit de ce qui a seulement été dit de "
                      "vive voix.",

    'bravo': "🎉 Bravo, tu as terminé le module « Faire faire des travaux » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
