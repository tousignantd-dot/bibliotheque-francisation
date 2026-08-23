# -*- coding: utf-8 -*-
"""Identité de module-n7-achat — « Réclamer après l'achat ».

Niveau 7, situation « Achat de biens de consommation durables », domaine
« Consommation et environnement ». Activité 113, module 6 du niveau 7. Vague 7.

Ce que `python3 build/cadre.py 7 "Achat de biens de consommation durables"`
donne
---------------------------------------------------------------------------
**Trois intentions, et elles se lisent comme un plan de module** — c'est le cas
de figure que `module-n7-recherche` a nommé : au niveau 7 la situation peut
être plus nette que le niveau, et les défis *sont* alors les intentions.

  · CO/PO — comprendre des renseignements et décrire un problème portant sur
    le fonctionnement d'un électroménager ou d'un véhicule ;
  · CO/PO — faire une réclamation ;
  · PE — rédiger une lettre de réclamation.

Une intention par défi, et rien à choisir avant de les avoir posées. Les
savoirs du niveau viennent ensuite se ranger dessous.

Ce qui distingue ce module de ses deux voisins de situation
-------------------------------------------------------------
En une phrase, comme la vague 7 le demande : **ici le bien est déjà payé, et
il brise.** `module-n3-electro` (76) lit la circulaire, trouve le rayon et fait
livrer ; `module-achat` (17, niveau 4) compare deux modèles, lit la garantie et
le mode d'emploi **avant** de signer. Tout ce module-ci se passe après la
vente : décrire une panne assez précisément pour qu'on vous croie, puis
réclamer. Et c'est le seul module du dépôt qui porte sur un **véhicule** plutôt
que sur un électroménager — la situation nomme pourtant les deux depuis le
début.

Deux voisinages plus lointains, écartés exprès. `module-n6-actualite` (99)
suit une histoire de garantie légale **à travers cinq genres de médias** : son
travail est la cohésion d'un texte suivi, pas la réclamation. Et
`module-probleme` (10) réclame auprès d'un propriétaire de logement, pas d'un
commerçant : ni garantie, ni contrat de crédit, ni Office de la protection du
consommateur.

La grille : `GRILLE_3_DEFIS`, et le test des trois entrées
-----------------------------------------------------------
« Au choix » dans le tableau de la vague 7 : c'est donc le cadre qui décide, et
le test du pilote du niveau 6 qui tranche. Trois façons distinctes d'entrer
dans la situation, chacune avec son dialogue et ses cinq exercices :

  · Défi 1 — **décrire la panne**. Un bruit, un moment, une fréquence. Ce
    n'est pas de la mécanique : c'est de la langue, et c'est ce qui décide
    si le garagiste cherche ou hausse les épaules.
  · Défi 2 — **réclamer au comptoir**. Trois garanties se superposent sur la
    même auto et on n'en connaît qu'une, celle qu'on a payée. Faire une
    réclamation, c'est d'abord savoir laquelle invoquer.
  · Défi 3 — **écrire**. La mise en demeure : les faits, la demande, le
    délai, et rien d'autre.

Les trois se suivent dans le temps du même dossier, celui d'Ernestine Kabuya.
Le troisième défi ne répète pas le deuxième : au comptoir on parle, dans la
lettre on écrit — et c'est l'intention de production écrite du programme.

Les faits québécois, vérifiés le 23 août 2026
----------------------------------------------
Rien de ce qui suit n'est deviné. Sources : Office de la protection du
consommateur, Loi sur la protection du consommateur. Le détail est au journal
de la vague 7, dans `docs/vagues-suivantes.md`.

  · **Garantie de bon fonctionnement** d'une auto d'occasion vendue par un
    commerçant, pour un contrat conclu depuis le 5 avril 2024 :
    catégorie A — 4 ans ou moins et au plus 80 000 km — **6 mois ou
    10 000 km** ; catégorie B — 5 ans ou moins et au plus 100 000 km —
    **3 mois ou 5 000 km** ; catégorie C — 7 ans ou moins et au plus
    120 000 km — **1 mois ou 1 700 km** ; catégorie D — plus de 7 ans ou plus
    de 120 000 km — **aucune garantie de bon fonctionnement**. La première
    limite atteinte met fin à la garantie. Elle commence à la livraison,
    couvre les pièces **et** la main-d'œuvre, et se prolonge des jours
    d'immobilisation.
  · **Étiquette obligatoire** sur chaque véhicule d'occasion offert par un
    commerçant : description complète, kilométrage à l'odomètre et
    kilométrage réel s'il diffère, **catégorie aux fins de la garantie**,
    mention du droit d'obtenir le nom du dernier propriétaire, usages
    antérieurs particuliers (taxi, école de conduite, location, police,
    ambulance, démonstration), réparations faites depuis que le commerçant a
    le véhicule. Elle est remise au consommateur et **fait partie du
    contrat**, sauf le prix et les caractéristiques de la garantie.
  · **Garantie légale** (art. 37 et 38 LPC) : le bien doit servir à l'usage
    normal auquel il est destiné et servir **pendant une durée raisonnable**,
    compte tenu du prix payé, du contrat et des conditions d'utilisation.
    Elle ne s'achète pas et s'ajoute aux autres.
  · **Article 228.1 LPC** : avant de proposer une garantie supplémentaire
    payante, le commerçant doit informer le consommateur **verbalement et par
    écrit** de l'existence et du contenu de la garantie légale des art. 37 et
    38, et verbalement de la garantie du fabricant offerte gratuitement.
    Celui qui ne le fait pas est réputé passer sous silence un fait important
    — une pratique interdite au sens de l'art. 228.
  · **Droit de résolution d'une garantie supplémentaire : 10 jours** suivant
    la conclusion du contrat, par avis écrit au commerçant. Le délai court à
    compter du lendemain de l'achat, et il est reporté au jour ouvrable
    suivant s'il tombe une fin de semaine ou un jour férié. Le remboursement
    est dû dès la réception de l'avis.
  · **Contrat de crédit** (vente à tempérament) : le contrat doit indiquer le
    prix de vente au comptant, l'acompte, le capital net, le **taux de
    crédit** exprimé en pourcentage annuel, les **frais de crédit**, le
    montant et l'échéance des versements, et l'**obligation totale** du
    consommateur — le montant financé plus les frais de crédit. Le
    consommateur peut payer d'avance sans frais ni pénalité.
  · **Mise en demeure** : la lettre expose ce qu'on reproche et accorde un
    délai raisonnable, **généralement dix jours**, pour corriger la
    situation.
  · **Division des petites créances** : la réclamation doit être de
    **15 000 $ ou moins** ; on s'y représente soi-même.

Tout le reste — Ernestine Kabuya, Autos Bulstrode, le Garage Ducharme, les
personnes, les montants, les dates, la berline 2019 — est inventé, comme
partout dans ce dépôt.

Un mot sur les personnages
---------------------------
Cinq, et aucun n'existe ailleurs dans `build/contenu/` — vérifié par grep avant
de les nommer.

  · **Ernestine Kabuya**, 41 ans, arrivée de la République démocratique du
    Congo il y a cinq ans, éducatrice spécialisée dans une école primaire de
    Victoriaville. Sans auto, elle ne peut pas travailler : l'école est à
    dix-huit kilomètres et aucun autobus n'y monte le matin.
  · **Jean-Rock Vachon**, vendeur chez Autos Bulstrode. Ni malhonnête ni
    scrupuleux : il vend vite, il explique peu, et il ne dit pas ce qu'on ne
    lui demande pas.
  · **Wilfrid Frigon**, conseiller au service du Garage Ducharme, un garage
    indépendant. C'est lui qui apprend à Ernestine à décrire une panne.
  · **Maryse Turgeon**, directrice du service à la clientèle d'Autos
    Bulstrode. Elle n'est pas l'ennemie : elle applique ce qu'on lui a appris,
    et « usure normale » est la phrase qu'elle a apprise.
  · **Édith Vanasse**, agente de renseignements à l'Office de la protection
    du consommateur. Elle ne règle rien à la place d'Ernestine : elle lui dit
    quelles règles s'appliquent et ce qu'une lettre doit contenir.

Le module **vouvoie** partout : Ernestine vouvoie le vendeur, le garagiste, la
directrice et l'agente, et l'écran de fin vouvoie aussi.
"""

MANIFESTE = {
    'slug': 'module-n7-achat',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`.

    'theme': 'Achat de biens de consommation durables',

    # Indigo : la couleur du niveau 7. Elle ne se choisit pas —
    # `build/couleurs_niveau.py` la pose et la vérifie.
    'accent': '#3B49A0',
    'accent_doux': '#E8EAFA',

    'ia_oral': "L'élève fait une réclamation à un commerçant au sujet d'un "
               "bien qui a brisé : il annonce d'abord de quoi il s'agit avec "
               "la date et le montant, décrit le problème de fonctionnement "
               "en donnant le bruit, le moment et la fréquence, dit quelle "
               "garantie il invoque et pourquoi elle s'applique, exprime son "
               "mécontentement sans attaquer la personne, formule une demande "
               "précise au conditionnel, puis annonce ce qu'il fera si rien "
               "ne bouge, avec un délai. Il vouvoie son interlocuteur.",

    'jr_cas': 'transmission',
    'jr_role': 'ernestine',
    'jr_scenario': 'reclamation',
    'ia_jeu_de_role': "L'élève réclame auprès du commerçant qui lui a vendu "
                      "un bien qui a brisé : il dit d'abord la date d'achat "
                      "et le montant, décrit la panne avec un bruit, un "
                      "moment et une fréquence, invoque la garantie qui "
                      "s'applique au lieu de celle qu'il a payée, met en "
                      "relief ce qui compte au moyen d'une phrase emphatique, "
                      "demande au conditionnel une réparation sans frais, et "
                      "annonce un délai avant d'écrire.",

    # L'apostrophe s'échappe dans `theme`, `bravo` et `relance` : les trois
    # valeurs sont injectées dans des chaînes JavaScript à guillemets simples.
    'bravo': "🎉 Bravo, vous avez terminé le module « Réclamer après "
             "l\\'achat » !",
    'relance': "Vous pouvez revenir sur n\\'importe quel onglet pour "
               "pratiquer encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
