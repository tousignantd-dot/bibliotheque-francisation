# -*- coding: utf-8 -*-
"""Identité de module-n7-banque — « Emprunter, épargner, se protéger ».

Niveau 7, situation « Transactions bancaires », domaine général de formation
« Consommation et environnement ». Activité 114, module 7 du niveau 7.
Vague 7.

Ce que `python3 build/cadre.py 7 "Transactions bancaires"` donne
-----------------------------------------------------------------
**Trois intentions, et c'est la même phrase répétée dans trois compétences** :

  · CO — s'informer sur des produits financiers liés au crédit ou à l'épargne ;
  · PO — s'informer sur des produits financiers liés au crédit ou à l'épargne ;
  · CE — s'informer sur des produits financiers reliés au crédit ou à
    l'épargne.

Aucune intention de production écrite n'est rattachée à la situation. La
lettre de « Je me lance » se tire donc des **attentes de fin de cours** du
niveau 7, qui, elles, la portent explicitement : « l'adulte rédige un texte
formel simple pour transmettre à différents destinataires un message parfois
complexe », « à l'aide d'un modèle, il rédige une lettre de réclamation ou
d'accompagnement, une note de service, une lettre d'affaires courantes ». La
production orale, elle, sort à la fois de l'intention PO et de l'attente
« il expose les avantages et les inconvénients de deux situations ou contextes
pour prendre une décision ». C'est écrit ici pour que le relecteur suivant ne
prenne pas ces tâches pour une invention hors programme et ne les retire pas.

Le savoir lexical propre à la situation, dans le programme, tient en trois
points : « Transactions bancaires, crédit, épargne » ; « Produits financiers,
placements, régime enregistré d'épargne-retraite (REER) » ; et —
c'est le plus intéressant — « **Expressions pour reprendre une partie d'un
discours et exprimer une incompréhension partielle** ». Ce troisième point
n'est pas du décor : c'est l'exercice `prReprise` et sa mini-leçon, et c'est
le geste que le module enseigne d'un bout à l'autre. Une conseillère qui
explique un produit financier emploie vingt mots que l'élève ne connaît pas ;
l'élève qui sait dire *lequel* des vingt il n'a pas compris obtient une
réponse, celui qui hoche la tête signe.

Ce qui distingue ce module de ses trois voisins de situation
--------------------------------------------------------------
En une phrase, écrite avant le scénario, comme la vague 7 le demande : **c'est
le seul module du dépôt où l'on achète quelque chose qu'on ne peut pas
regarder**. `module-n2-guichet` (93) retire de l'argent à un guichet et
libelle un chèque — un nombre, un impératif, une signature ;
`module-banque` (46), au niveau 4, ouvre un compte au comptoir et lit une
brochure de forfaits ; `module-procedure` (40), rattaché à la même situation
dans `build/bilan_programme.py`, suit une marche à suivre administrative.
Aucun des trois ne demande de **choisir entre deux produits dont le prix est
un pourcentage et le défaut, une clause**. Au niveau 7, on ne retire plus
d'argent : on comprend un produit, on le compare à un autre, et on conteste
ce qui ne va pas.

La grille : `GRILLE_3_DEFIS`, et le test des trois entrées
-----------------------------------------------------------
La vague laissait le choix (« au choix, 2 ou 3 défis »). Le test du pilote du
niveau 6 tranche : peut-on nommer trois façons distinctes d'entrer dans la
situation, chacune avec son dialogue et ses cinq ou six exercices ? Oui, et
elles sortent des deux mots de l'intention elle-même — *crédit* **ou**
*épargne* —, plus ce que le programme met autour :

  · Défi 1 — **emprunter moins cher**. Trois façons d'emprunter, trois coûts,
    et un dossier de crédit qui décide du taux qu'on vous offre. Compréhension
    orale : on écoute un conseiller.
  · Défi 2 — **faire travailler l'argent**. Trois façons d'épargner, trois
    règles fiscales, une protection publique. Compréhension écrite : on lit
    une documentation comparative.
  · Défi 3 — **une opération que je n'ai pas faite**. Ce que la loi rembourse,
    ce qu'elle ne rembourse pas, et comment on le demande — de vive voix puis
    par écrit. Production orale et écrite.

Trois défis, trois compétences, et le troisième ne répète pas le deuxième :
il porte sur le seul moment où le client parle plus que l'institution.

Les faits québécois, vérifiés le 23 août 2026
----------------------------------------------
Rien de ce qui suit n'est deviné. Le détail des sources est au journal de la
vague 7, dans `docs/vagues-suivantes.md`.

  · **Office de la protection du consommateur** — le paiement minimum exigible
    sur une carte de crédit ne peut être inférieur à **5 % du solde** à la fin
    de la période ; un solde remboursé en entier avant la date d'échéance
    n'entraîne **aucuns frais de crédit** ; une **avance de fonds** fait courir
    les frais **dès le jour où elle est prise**, même remboursée à temps ; en
    cas d'utilisation non autorisée d'une carte de crédit perdue, volée ou
    fraudée, la responsabilité du titulaire est **limitée à 50 $**, à condition
    qu'il avise l'émetteur **sans délai** — après l'avis, il n'est plus
    responsable de rien, et la négligence dans la protection du NIP peut lui
    coûter davantage.
  · **Autorité des marchés financiers** — l'**assurance-dépôts** couvre
    **100 000 $ par catégorie de dépôts**, par personne et par institution de
    dépôt autorisée, capital et intérêts courus compris ; elle est
    **automatique et gratuite** ; elle vise les dépôts payables au Québec —
    comptes chèque, comptes épargne, dépôts à terme et certificats de placement
    garanti. L'AMF tient aussi le **registre des entreprises et des individus
    autorisés à exercer** : avant d'investir, on y vérifie la personne qui
    offre le placement. « Un rendement élevé sans risque, ça n'existe pas » est
    sa formule, pas la nôtre.
  · **Agence du revenu du Canada** — le plafond du **CELI** est de **7 000 $
    pour 2026** ; les cotisations n'y sont **pas déductibles**, les retraits ne
    sont **pas imposables**, et le montant retiré est rendu aux droits de
    cotisation **le 1er janvier suivant** ; l'excédent est frappé d'un impôt de
    **1 % par mois**. Les cotisations à un **REER** sont **déductibles** du
    revenu, les retraits **imposables**, et le droit annuel vaut **18 % du
    revenu gagné de l'année précédente**, jusqu'à un plafond fixé par le
    fédéral — plafond dont le montant n'est **pas** écrit dans le module,
    faute d'avoir été vérifié pour 2026.
  · **Equifax Canada et TransUnion Canada** sont les deux agences d'évaluation
    du crédit au pays ; le pointage s'étend de **300 à 900** ; consulter son
    propre dossier est **gratuit** et **sans effet** sur le pointage.

**Aucun taux n'est inventé sans être marqué comme tel.** Les seuls
pourcentages du module qui ne viennent pas d'une source officielle sont ceux
que des institutions **inventées** offrent à un personnage **inventé** : la
carte de la Banque Norlande à 19,90 %, la marge de la Caisse Sainte-Praxède à
9,45 %, son prêt personnel à 11,20 %, son dépôt à terme à 3,10 %. Ni la
Banque Norlande, ni la Caisse Sainte-Praxède, ni la Fromagerie des Bois-Francs
n'existent, et le module le dit à l'élève dans les bandeaux de savoir des deux
exercices de type `texte` : « Ce document-ci est un exemple. »

Les personnages
----------------
Cinq, et aucun nom n'existe ailleurs dans `build/contenu/` — vérifié par grep
avant de les nommer.

  · **Marlène Saint-Preux**, 41 ans, arrivée d'Haïti il y a huit ans,
    technicienne au contrôle de la qualité à la Fromagerie des Bois-Francs, à
    Victoriaville. Neuf mille quatre cents dollars sur une carte de crédit,
    six mille deux cents dollars qui dorment dans un compte chèque, et une
    fille, Jessie, qui entre au cégep dans deux ans.
  · **Huguette Larochelle**, sa collègue de la salle de repos. Cinquante-huit
    ans, deux hypothèques payées, aucune patience pour les frais de crédit.
    Elles se **tutoient** — ce sont des collègues.
  · **Damien Rouillard**, conseiller en finances personnelles à la Caisse
    Sainte-Praxède.
  · **Nathalie Pomerleau**, planificatrice financière à la même caisse.
  · **Steve Dumouchel**, agent au service de la sécurité des cartes de la
    Banque Norlande.

Le module **vouvoie** partout sauf entre les deux collègues : Marlène vouvoie
le conseiller, la planificatrice et l'agent, et l'écran de fin vouvoie l'élève.
"""

MANIFESTE = {
    'slug': 'module-n7-banque',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Transactions bancaires',

    # Indigo : la couleur du niveau 7. Elle ne se choisit pas —
    # `build/couleurs_niveau.py` la pose et la vérifie.
    'accent': '#3B49A0',
    'accent_doux': '#E8EAFA',

    'ia_oral': "L'élève expose les avantages et les inconvénients de deux "
               "produits financiers — par exemple une marge de crédit et un "
               "prêt personnel, ou un CELI et un dépôt à terme — pour arriver "
               "à une décision : il annonce les deux produits, donne pour "
               "chacun deux avantages et deux inconvénients avec un chiffre à "
               "l'appui, les compare au moyen de « plus… que », « moins… "
               "que », « ne… que » et « d'autant plus… que », puis tranche et "
               "dit à quelle condition il changerait d'avis. Il vouvoie son "
               "interlocuteur.",

    'jr_cas': 'marge',
    'jr_role': 'marlene',
    'jr_scenario': 'produitfinancier',
    'ia_jeu_de_role': "L'élève s'informe sur un produit financier auprès d'un "
                      "conseiller : il dit d'abord ce qu'il veut savoir, il "
                      "demande le taux et ce qu'il faut rembourser chaque "
                      "mois, il reprend une partie de ce qu'on vient de lui "
                      "dire pour signaler ce qu'il n'a pas compris — « quand "
                      "vous dites « capitalisé », ça veut dire quoi "
                      "exactement ? » —, il fait répéter un chiffre pour le "
                      "vérifier, il demande ce que ça coûte si l'on paie plus "
                      "vite que prévu, et il repart avec une réponse écrite "
                      "plutôt qu'avec une signature.",

    # L'apostrophe s'échappe dans `theme`, `bravo` et `relance` : les trois
    # valeurs sont injectées dans des chaînes JavaScript à guillemets simples.
    'bravo': "🎉 Bravo, vous avez terminé le module "
             "« Emprunter, épargner, se protéger » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
