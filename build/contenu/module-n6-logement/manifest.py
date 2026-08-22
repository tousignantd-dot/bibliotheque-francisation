# -*- coding: utf-8 -*-
"""Identité de module-n6-logement — « Six mois ailleurs ».

Niveau 6, situation « Location d'un logement », domaine « Habitation et
déplacement ». Activité 105, module 8 du niveau. Vague 6. Le pilote du niveau
(activité 99, `module-n6-actualite`) a écrit ce qui résiste au stade
intermédiaire ; sa note est dans `docs/vagues-suivantes.md`.

Ce que `python3 build/cadre.py 6 "Location d'un logement"` donne
----------------------------------------------------------------
**Une seule intention**, et elle est de compréhension écrite :

  · CE — s'informer sur ses droits et ses obligations en consultant un
    site Web.

Rien d'autre. Ni compréhension orale, ni production orale, ni production
écrite rattachées à la situation. Le module part donc de là et de rien
d'autre : l'élève consulte un site officiel, il y suit un texte de droits, et
il retrouve ensuite la même règle sous deux écrits qui ne s'accordent pas.

**D'où viennent les productions de « Je me lance ».** Puisque la situation n'a
aucune intention productive, elles se tirent des **attentes de fin de cours**
du niveau, qui, elles, sont productives — comme l'a fait le pilote :

  · PO — « il décrit les étapes d'une démarche administrative en donnant les
    détails nécessaires » ;
  · PE — « il rédige un court texte en organisant ses idées à l'aide de
    paragraphes » et « dans ses relations professionnelles, il rédige un
    courriel ou une lettre en respectant les conventions habituelles ».

C'est écrit ici pour que le relecteur suivant ne prenne pas ces deux tâches
pour une invention hors programme et ne les retire pas.

La grille : deux défis, et pourquoi pas trois
---------------------------------------------
`GRILLE_2_DEFIS` — huit séances hors bloc final, réparties 4-5-5-2. Le test du
pilote est celui-ci : peut-on nommer trois façons distinctes d'entrer dans la
situation, chacune avec son dialogue et ses exercices ? Ici, deux tiennent
debout et la troisième ne tient pas.

  · Défi 1 — **ce que dit le site**. Un texte informatif public, écrit pour
    tout le monde, organisé en intertitres et en puces, avec un encadré et une
    date de mise à jour. On y cherche une règle qui ne parle de personne en
    particulier.
  · Défi 2 — **l'avis et la réponse**. Deux lettres privées, adressées, datées,
    signées, qui parlent d'un seul cas et qui ne disent pas la même chose. On
    y cherche ce que la règle devient quand elle tombe sur un dossier.

Le troisième défi aurait été l'audience au Tribunal. Il a été écarté pour deux
raisons : c'est un **autre travail** — parler devant un tribunal, ce n'est plus
s'informer sur ses droits —, et c'est le terrain de « Problèmes reliés à
l'habitation » (activité 106), qui suit dans la même vague. Le remplir ici
aurait voulu dire faire relire à l'élève une troisième lettre du même dossier :
inventer une séance sans contenu reste pire que de n'en pas avoir.

Le fil, et le travail
---------------------
Le niveau 6 est le niveau de la **cohésion** : le 5 raconte, le 7 démasque, le
6 suit un fil. Les deux défis sont deux retours sur le **même dossier** — le
projet de sous-location du logement de Farida Belkacem — sous deux genres qui
n'ont ni la même mise en page, ni le même destinataire, ni les mêmes marques
de reprise. Le site écrit « le locataire » et « celui-ci » ; la lettre écrit
« vous » et « votre logement ». Reconnaître la même règle sous les deux, c'est
exactement ce que la situation demande.

Deux exercices du type `texte` au Défi 2, un au Défi 1
------------------------------------------------------
`t1page`, `t2avis` et `t2reponse` sont des exercices `texte` — le type versé au
moteur le 22 août 2026 pour les niveaux 6 à 8. C'est l'endroit juste :
l'intention du programme porte sur un **site Web**, donc sur un texte suivi,
pas sur des phrases isolées. L'élève doit pouvoir cliquer *dans* la page pour
montrer le passage qui répond, et garder le texte sous les yeux pendant qu'il
répond — c'est tout l'intérêt du type.

Les dix savoirs retenus
-----------------------
Sur les cinquante-quatre du niveau, par la question du pilote — « est-ce que ce
savoir sert à suivre un texte ? » : la formation des mots et la nominalisation
(louer → la location, céder → la cession) ; la graphie-phonie (ch qui dit k, x
qui dit s, sh et sch qui disent ch) ; la présentation matérielle et la mise en
page, appliquées à une page Web ; les connecteurs d'exemplification et de point
de vue ; la reprise de l'information par « en » et par « le » ; la relative en
« où », complément de lieu ou de temps ; le passé simple, reconnu à la
3e personne et associé au passé composé ; le plus-que-parfait d'antériorité ;
le subjonctif présent après verbe introducteur usuel, avec la distinction
verbe + de / verbe + que ; l'hypothèse réaliste avec « si » ; et la disposition
d'un courriel formel. Les trois savoirs de grammaire du texte — connecteurs,
reprise, présentation matérielle — sont là tous les trois.

Le passé simple se travaille en **`match`** (`t1ps`), jamais en `write` : le
programme demande de le *reconnaître*. Tous les exercices de grammaire du texte
sont en `cols:1` — leurs items font deux phrases, et `cols:2` les rendrait
illisibles.

Le lexique
----------
La situation, elle, a un savoir lexical, ce qui est rare : « vocabulaire lié
aux droits et aux obligations du locataire : délai, résiliation,
renouvellement, défaut de paiement, dommages, compensation, avis, locateur,
indemnité, clauses, cession, sous-location ». Les seize mots du module en
sortent presque tous — c'est la seule liste du module, et « Je retiens des
mots » n'a pas d'autre source.

Le droit du Québec : vérifié, et tenu à l'écart de l'invention
--------------------------------------------------------------
Le Tribunal administratif du logement existe. Il a remplacé la Régie du
logement le 31 août 2020, et la Régie avait elle-même été créée en 1980. Les
règles nommées dans le module sont celles du Code civil du Québec sur la
sous-location, et elles sont stables :

  · le locataire qui veut sous-louer son logement doit en aviser le locateur
    **par écrit**, en lui indiquant le nom et l'adresse de la personne
    proposée ;
  · le locateur a **quinze jours** pour répondre, et s'il ne répond pas dans
    ce délai il est réputé avoir consenti ;
  · il ne peut refuser que pour un **motif sérieux** ;
  · il peut demander le remboursement des **dépenses raisonnables** que la
    sous-location lui occasionne ;
  · en sous-location, le locataire **reste responsable** de son bail envers le
    locateur — c'est la différence avec la cession, qui transfère le bail pour
    de bon.

Le module s'en tient là. Il ne dit rien des règles qui ont changé récemment
sur le refus d'une **cession** : la cession n'est nommée que pour la
distinguer de la sous-location, et jamais pour en décrire la procédure. Tout
ce qui est nommé est vérifiable ; tout le reste est inventé — Farida Belkacem,
Gilles Bédard, Lucien Tardif, Mylène Poitras, Nicolas Trudel, l'immeuble de la
rue de la Canardière, les dates, les montants, le numéro de dossier et la page
Web citée, dont la forme imite un site officiel sans en reprendre le texte.
Prêter à un tribunal réel une page qu'il n'a pas écrite en ferait un faux
document : la page du module est présentée à l'élève comme un **exemple**, et
le Défi 1 le dit en toutes lettres.

Les voisins, et ce qui l'en sépare
----------------------------------
Trois modules occupent déjà la même situation, plus bas. Ce qui change n'est
pas le sujet, c'est le **travail** — et les trois cherchent un logement, alors
qu'ici le logement est trouvé depuis trois ans.

· `module-n3-loyer` (81, niveau 3) lit six lignes de petite annonce,
  téléphone pour prendre rendez-vous et pose trois questions sur place. Sa
  langue est celle de la première fois : on ne connaît ni le logement, ni la
  personne, ni les mots.
· `module-logement` (44, niveau 4) visite deux logements et les compare pour
  choisir : décrire, peser, préférer. Rien n'y est écrit.
· `module-n5-logement` (58, niveau 5) fait la démarche entière — l'appel avec
  prise de notes, la visite, le bail et l'avis de renouvellement. C'est le
  voisin le plus proche, et la différence tient en une phrase : il **lit son
  bail** pour savoir à quoi il s'est engagé, quand ce module **cherche une
  règle qu'il ne connaît pas encore** sur un site public, puis la voit se
  heurter à un cas. Le bail de Farida n'est presque pas ouvert ici : il ne dit
  rien de la sous-location, et c'est précisément le point de départ.

Adresse
-------
Le module **vouvoie l'élève** partout, y compris dans l'écran de fin — le
contraire de `module-n6-emploi`, qui tutoie. Ce n'est pas un caprice : tout ce
que l'élève écrit ici part chez un locateur ou dans un site officiel, et le
vouvoiement est la forme du dossier. Dans les dialogues, Farida tutoie Gilles,
son collègue de cuisine depuis trois ans, et vouvoie Mylène Poitras, Lucien
Tardif et Nicolas Trudel. Le contraste est de la matière : « saisir les
rapports entre des interlocuteurs » est un savoir du cours, et il n'apparaît
qu'au niveau 6.
"""

MANIFESTE = {
    'slug': 'module-n6-logement',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': "Location d\\'un logement",

    # Acier : la couleur du niveau 6. Elle ne se choisit pas — voir
    # `build/couleurs_niveau.py`.
    'accent': '#1D6B8F',
    'accent_doux': '#E7F0F6',

    'ia_oral': "L'élève décrit à quelqu'un les étapes de la démarche de "
               "sous-location, telle qu'il l'a lue sur le site officiel. Il "
               "dit d'abord de quoi il s'agit et où il l'a lu, il énumère "
               "ensuite les étapes dans l'ordre avec les détails nécessaires "
               "— l'avis écrit, le nom et l'adresse de la personne, les "
               "quinze jours, le motif sérieux, le consentement présumé —, il "
               "annonce au moins un exemple par « par exemple » ou "
               "« notamment », il distingue ce que le site écrit de ce qu'il "
               "en pense, et il termine par ce qu'il compte faire. Il vouvoie "
               "son interlocuteur.",

    'jr_cas': 'projet',
    'jr_role': 'farida',
    'jr_scenario': 'souslocation',
    'ia_jeu_de_role': "L'élève annonce à son locateur un projet de "
                      "sous-location et le défend : il expose la démarche "
                      "dans l'ordre, il nomme la personne proposée, il donne "
                      "les dates, il répond aux objections sans se fâcher, il "
                      "distingue ce que le site officiel écrit de ce qu'il en "
                      "pense, et il emploie « si » pour poser une hypothèse "
                      "réaliste. Il vouvoie son interlocuteur du début à la "
                      "fin.",

    'bravo': "🎉 Bravo, vous avez terminé le module « Six mois ailleurs » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
