# -*- coding: utf-8 -*-
"""Identité de module-n7-logement — « Rester locataire ou devenir propriétaire ».

Niveau 7, situation « Location **ou achat** d'un logement », domaine
« Habitation et déplacement ». Activité 111, module 4 du niveau 7. Vague 7.

Ce que `python3 build/cadre.py 7 "Location ou achat"` donne
-----------------------------------------------------------
**Deux intentions, et les deux sont orales** — c'est le fait marquant de cette
situation au niveau 7 :

  · CO/PO — négocier entre propriétaire et locataire ;
  · CO/PO — s'informer pour acheter une habitation.

Aucune intention de compréhension ni de production écrite n'est rattachée à la
situation. La compréhension écrite du module (les deux exercices de type
`texte`) et la production écrite de « Je me lance » se tirent donc des
**attentes de fin de cours** du niveau 7, qui, elles, les portent :

  · CE — « il interprète un message écrit se rapportant à un sujet d'intérêt
    général » ;
  · PO — « il expose les avantages et les inconvénients de deux situations ou
    contextes pour prendre une décision durant une négociation » ;
  · PE — « il rédige un texte formel simple », « à l'aide d'un modèle, il
    rédige une lettre d'affaires courantes », « il organise ses idées à l'aide
    de paragraphes, entre lesquels il établit des liens au moyen de
    connecteurs ».

C'est écrit ici pour que le relecteur suivant ne prenne pas ces tâches pour une
invention hors programme et ne les retire pas.

Ce qui distingue ce module de ses quatre voisins de situation
--------------------------------------------------------------
En une phrase, comme la vague 7 le demande : **c'est le seul module du dépôt
où quelqu'un achète** — le niveau 4 (`module-logement`) visite et compare, le
niveau 3 (`module-n3-loyer`) paie son loyer, le niveau 5
(`module-n5-logement`) téléphone et lit son bail, le niveau 6
(`module-n6-logement`) suit un texte de droits sur la sous-location, et
celui-ci **négocie d'égal à égal, puis s'informe pour acheter**. L'achat
n'existe à aucun niveau inférieur, et il apporte avec lui un monde entier que
personne n'a encore rencontré : la courtière, la promesse d'achat, l'inspection
préachat, la préautorisation hypothécaire, le notaire.

La grille : `GRILLE_3_DEFIS`, et le test des trois entrées
-----------------------------------------------------------
Réservée dans `docs/vagues-suivantes.md`, et le test du pilote du niveau 6 la
confirme : on nomme bien trois façons distinctes d'entrer dans la situation,
chacune avec son dialogue et ses cinq ou six exercices.

  · Défi 1 — **l'avis du propriétaire**. Une hausse de loyer annoncée par
    écrit, un délai d'un mois pour répondre, une négociation où l'on demande
    au lieu d'exiger.
  · Défi 2 — **la visite avec la courtière**. S'informer pour acheter, c'est
    d'abord savoir à qui l'on parle et poser les questions que personne ne
    pose. La courtière du vendeur ne représente pas l'acheteur ; le module en
    fait un savoir, pas une méfiance.
  · Défi 3 — **la promesse d'achat**. Les conditions, le financement,
    l'inspection — et la décision : rester ou acheter.

Les trois se suivent dans le temps d'un même dossier, celui de Sokhna Diagne.

Les faits québécois, vérifiés le 22 août 2026
----------------------------------------------
Rien de ce qui suit n'est deviné ; le détail des sources est au journal de la
vague 7, dans `docs/vagues-suivantes.md`.

  · Tribunal administratif du logement — pour un bail de douze mois ou plus,
    l'avis de modification des conditions du bail se donne **de trois à six
    mois** avant la fin du bail ; le locataire a **un mois** à compter de sa
    réception pour répondre ; **son silence vaut acceptation** ; s'il refuse,
    le locateur a **un mois** pour s'adresser au Tribunal en fixation de
    loyer, faute de quoi le bail est reconduit aux mêmes conditions.
  · OACIQ — un courtier lié par un contrat de courtage avec le vendeur **ne
    représente pas l'acheteur** ; il doit néanmoins traiter équitablement
    l'acheteur non représenté et lui communiquer objectivement l'information
    utile. La rétribution du courtier du vendeur n'est jamais réclamée à
    l'acheteur.
  · L'inspection préachat **n'est pas obligatoire par la loi**, mais le
    courtier doit la recommander, et un acheteur qui y renonce le fait
    inscrire à sa promesse d'achat.
  · Mise de fonds minimale : **5 %** jusqu'à 500 000 $, **10 %** sur la part
    au-delà. Sous 20 %, le prêt doit être **assuré** (SCHL, Sagen).
  · Le **notaire** est obligatoire pour l'acte hypothécaire et fait l'examen
    des titres. Les **droits de mutation** — la « taxe de bienvenue » — se
    paient à la municipalité par le nouveau propriétaire.

Tout le reste — les personnes, l'immeuble de la rue Bourdages, les montants,
les dates, la caisse, l'agence — est inventé, comme partout dans ce dépôt.

Un mot sur les personnages
---------------------------
Quatre, et aucun n'existe ailleurs dans `build/contenu/` — vérifié par grep
avant de les nommer, comme le pilote du niveau 6 l'a écrit après avoir trouvé
trois Marisol au même niveau.

  · **Sokhna Diagne**, 43 ans, arrivée du Sénégal il y a onze ans, préposée
    aux bénéficiaires dans un CHSLD de Saint-Hyacinthe. Locataire du 5 ½ du
    2 de la rue Bourdages depuis sept ans.
  · **Gérald Lheureux**, 66 ans, son propriétaire, six logements, pas
    méchant, pas généreux non plus.
  · **Josiane Bourbonnais**, courtière immobilière, agence de la rive.
  · **Farah Zaoui**, conseillère hypothécaire à la caisse.

Le module **vouvoie** partout : Sokhna ne tutoie ni son propriétaire, ni la
courtière, ni la conseillère, et l'écran de fin vouvoie aussi.
"""

MANIFESTE = {
    'slug': 'module-n7-logement',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Logement',

    # Indigo : la couleur du niveau 7. Elle ne se choisit pas —
    # `build/couleurs_niveau.py` la pose et la vérifie.
    'accent': '#3B49A0',
    'accent_doux': '#E8EAFA',

    'ia_oral': "L'élève expose les avantages et les inconvénients de deux "
               "options — rester locataire ou acheter — pour arriver à une "
               "décision : il annonce les deux options, donne pour chacune "
               "deux avantages et deux inconvénients avec un chiffre ou un "
               "fait à l'appui, les compare au moyen de « plus… que », "
               "« moins… que », « d'autant plus… que », puis tranche et dit "
               "à quelle condition il changerait d'avis. Il vouvoie son "
               "interlocuteur.",

    'jr_cas': 'avis',
    'jr_role': 'sokhna',
    'jr_scenario': 'louerouacheter',
    'ia_jeu_de_role': "L'élève négocie avec son propriétaire au sujet d'une "
                      "hausse de loyer : il dit d'abord de quoi il s'agit, "
                      "rappelle le délai d'un mois sans menacer, demande au "
                      "conditionnel au lieu d'exiger, met en relief ce qui "
                      "compte pour lui au moyen d'une phrase emphatique, "
                      "propose une contrepartie chiffrée et demande que "
                      "l'entente soit mise par écrit.",

    # L'apostrophe s'échappe dans `theme`, `bravo` et `relance` : les trois
    # valeurs sont injectées dans des chaînes JavaScript à guillemets simples.
    # Aucune des trois n'en porte ici, mais la règle se relit mal après coup.
    'bravo': "🎉 Bravo, vous avez terminé le module "
             "« Rester locataire ou devenir propriétaire » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
