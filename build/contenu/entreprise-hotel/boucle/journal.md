# Journal de révision — réception de l'Hôtel Rive-Claire (étapes 1 et 2)

Boucle didactique, quatre tours, le 25 septembre 2026. Deux regards indépendants
par tour : le contenu (trois langues) et la page servie et jouée (375 et 1280 px).

| Tour | Bloquants | Majeurs | Mineurs | Critères les plus touchés |
|---|---|---|---|---|
| 1 | 1 | 15 | 24 | D4 (distracteurs), A3 (alignement), E1 (rétroaction), G1 |
| 2 | 0 | 5 | 31 | E1, A2, D1, A3, D4 |
| 3 | 0 | 2 | 23 | A2 (heures dites), D4 |
| 4 | 0 | 0 | 11 | E1, D4, A1 — sortie de boucle |

## Ce qui a changé, et pourquoi

| Tour | Où | Avant | Après | Critères |
|---|---|---|---|---|
| 1 | Pièges | le faux ami montré seul (« a ticket » → contravention, vrai aussi) | posé dans une phrase de comptoir, qu'on entend | D4 bloquant |
| 1 | Ce que le client veut | 8 demandes, nuits toujours dites | 12, dont 4 où l'on compte les nuits à partir des dates | A3 (O1) |
| 1 | Ce que je réponds | 6 items, aucun sur les frais, bandeau qui soufflait la réponse O4 | 12 puis 13 items : 3 frais, 4 relais au gérant, règle dite avant, promesse = échec | A3, E2 |
| 1 | Ce que je réponds | la bonne toujours la plus longue (18/18) | distracteurs de même intention, longueurs à ±20 % vérifiées au build | D4 |
| 1 | Nouvelle famille | aucune production | « Je le dis » : situation → dire → modèle | D1 |
| 1 | Épeler | voix lente, 8 noms « propres » | assemblé lettre par lettre, noms accentués/composés, téléphone | D2 |
| 1 | Nombres | « Essayez encore » | rétroaction par nature d'erreur, phrase montrée après deux essais | E1 |
| 1 | Lexique | « a full bed » | « a double bed » | A2 |
| 1 | Images | lits jumeaux ensemble | groupes jamais ensemble | D4 |
| 1 | Accès | images sans nom, bouton qui déborde à 375 px | alt = le sens ; bouton pleine largeur | G1 |
| 2 | Nombres | voisines communes aux 3 langues | voisines et rétroactions par langue apprise | E1 |
| 2 | r11 | « je ne peux pas l'enlever » | « les enlever … votre demande » | A2 |
| 2 | Je le dis | sans contexte, client lu | contexte affiché, client entendu | D1 |
| 2 | Promesse | frontière variable | toute promesse que l'hôtel ne peut tenir | A3 |
| 2 | Pièges | 3e choix tiré au hasard, absurde | second distracteur écrit à la main | D4 |
| 2 | Sons | K espagnol de 12 s (Kowalski 28 s) | refait ; garde-fou de durée sur les lettres | D2 |
| 3 | Heures | « le français compte sur 24 h » | « du soir », « du matin » (n9, n10), heure ambiguë (r13) ; 24 h = notation | A2 |
| 3 | Pièges | « un crayon », « le déjeuner » justes dans une variété | « un formulaire », « la collation » | D4 |
| 3 | Places | jamais deux fois la même (tour 2) : un indice | tirées sans règle | D4 |
| 3 | Promesse | « c'est au gérant » après « ni le gérant » | « sans en avoir le pouvoir » | E1 |

## Mineurs consignés en sortie de boucle (tour 4)

Voir `audit4-contenu.json` et `audit4-page.json`, et la page
`assets/presentations/hotellerie-audit-4.html`. Les principaux : les rétroactions
d'heure encore imprécises (n6, « a.m. », « du soir » qui livre n10), la
promesse qui n'est pas annoncée comme éliminatoire avant la série, l'indice
« la seule réplique qui pose une question » dans Ce que je réponds, les places
comptables en fin de série, l'explication des pièges qui nomme la bonne dès le
premier essai.

## Ce que la boucle ne vérifie pas

La justesse linguistique finale (un locuteur de l'anglais et un de l'espagnol
doivent relire), l'essai auprès de vrais réceptionnistes (le pilote), l'effet
au comptoir.

## Test — révision après le tour 3 de son audit (0/3/6)

| Constat | Avant | Après | Code |
|---|---|---|---|
| B refuse des réponses justes | chiffres tapés comparés tels quels (« 239.00 », « 175.4 », « 5:15 pm » refusés) | la VALEUR : prix numérique (cents facultatifs, virgule ou point, « 175 40 ») ; heure 24 h, ou 12 h avec pm, ou 12 h seule quand la voix apprise compte sur 12 (en, es) ; « am » refusé | F1 |
| Saisie ignorée en silence | aucune lettre ou aucun chiffre → rien | « Tapez le nombre en chiffres » / « le nom en lettres » | E1 |
| Code contourné | historique par paire parle-apprend : changer l'interface ouvrait un historique vide | historique par langue APPRISE ; trois essais, puis une minute d'attente | F3 |
| Voix cachées au rechargement en D | chargées seulement pour une passation finie | rechargées aussi en reprenant une passation en cours | G3 |
| Note de langue seule ignorée | `palierDe` ne comptait que les gestes | toute note compte : un oral noté en partie n'est plus « non noté » | F1 |
| Confirmer sans noter l'oral efface les voix | un clic | avertissement, puis second clic | G3 |
| Voix des passations jamais confirmées | gardées sans fin | purgées à la passation suivante et après 30 jours (Loi 25) | G3 |
| Réécoute unique rendue au rechargement | non gardée | gardée avec la passation en cours | F1 |
| Passation précédente invisible | — | affichée sous les résultats, pour comparer entrée et sortie | F2 |
| es forme 2 : heure plus dure | « un cuarto para las siete de la tarde » | « las seis cuarenta y cinco de la tarde » (voix refaite) | F2 |

**Limite assumée** : un code écrit dans la page se lit dans sa source. C'est un
frein contre l'employé pressé, pas une serrure. La serrure viendra du serveur,
à l'étape 4. Idem : l'historique vit sur l'appareil ; une tablette partagée
mêle les employés (le guide du formateur le dira).

## Test — sortie de boucle (tour 4 : 0/0/6), mineurs traités le 25 sept. 2026

- Prix suivi d'un mot ou d'une ponctuation (« 239 dollars », « dlls », « 239. ») : accepté (F1). La consigne ne demande plus 24 h et virgule : « comme au comptoir ».
- Compteur d'essais du code : oublié après une minute (G2).
- REGLE_RELAIS : « un document faux (facture, date, mode de paiement) ne se fait jamais » — c5 et c11 sont désormais couverts par la règle affichée (D4).
- « Refaire » avertit si la passation n'est pas confirmée ; la passation précédente affichée est la dernière confirmée, sinon marquée « non confirmé » ; « voix effacée » après 30 jours (F1).
- Confirmation : l'avertissement paraît dès qu'une réponse n'a pas ses deux lignes, micro ou non ; une notation à moitié faite affiche « oral en cours de notation » (A3).
- Changer la langue apprise remet la passation à zéro (F1).
