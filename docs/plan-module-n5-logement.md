# Plan — `module-n5-logement` · « Louer un logement » (niveau 5, activité 58)

Écrit avant le contenu, pour que le scénario survive à la session (règle 4 de
`deux-agents-en-parallele.md`).

## Le cadre ministériel

Niveau 5 · LAN-4059-8 · *Habitation et déplacement* · **Location d'un
logement**, 4 intentions — et le module les couvre toutes les quatre :

| Intention | Où elle s'exerce |
|---|---|
| CO — Comprendre des renseignements sur un logement pendant une visite | Défi 2 |
| PO — Donner des renseignements sur un logement pendant une visite | Défi 2 + jeu de rôle + production orale |
| CE — Lire un document concernant le bail ou le renouvellement d'un bail | Défi 3 |
| PE — Prendre en note des renseignements donnés au téléphone | Défi 1 + production écrite |

Le lexique du programme est vide pour cette situation : il est composé à partir
des intentions et des savoirs « Conversation téléphonique ou visite d'un
logement » et « locataire » du niveau 5.

## Le scénario

**Nadège** habite un 3 ½ à Fleurimont avec sa fille depuis deux ans. En
février, elle trouve dans sa boîte aux lettres un **avis de modification du
bail** : le loyer monte, et le stationnement disparaît. Elle a un mois pour
répondre. Sa fille a sept ans et dort dans le salon — elle décide de chercher
un 4 ½.

Le problème progresse d'un défi à l'autre : elle comprend l'avis, elle
téléphone, elle visite, elle lit le bail avant de signer.

Trois personnages, tous neufs (aucun nom déjà pris dans les onze modules) :

- **NADÈGE** — la locataire, préposée aux bénéficiaires au CHUS.
- **SAMUEL** — intervenant au comité logement de Sherbrooke. Ce n'est pas
  un collègue : entre collègues on se tutoie, et le module tient le
  vouvoiement d'un bout à l'autre.
- **HÉLÈNE** — la propriétaire du 4 ½ de la rue Bowen.

Vouvoiement tenu partout, y compris dans les consignes : au niveau 5, l'élève
s'adresse à un propriétaire, pas à un ami.

## Les sections

| Section | Titre | Ce qu'on y fait |
|---|---|---|
| `prep` | Je découvre | L'avis dans la boîte aux lettres, les mots du logement, les fusions de l'oral québécois |
| `t1` | Défi 1 · L'appel | Se renseigner par téléphone et prendre des notes |
| `t2` | Défi 2 · La visite | Comprendre les renseignements — et savoir les donner |
| `t3` | Défi 3 · Le bail | Lire le bail, l'annexe et l'avis de renouvellement |
| `appli` | Je me lance | Jeu de rôle `louer`, production orale, production écrite |
| — | Je retiens des mots | Les 16 mots de `FC_CARDS` |

16 séances, `GRILLE_3_DEFIS` (4-4-4-2-2).

## La progression grammaticale

Sept points, tous pris dans les savoirs du niveau 5, chacun avec son exercice
**et** sa mini-leçon (même clé dans `exos.js` et `plus.js`) :

| Clé | Point de langue | Section |
|---|---|---|
| `prPhon` | Les formes fusionnées de l'oral : *sur le* [sʏl], *dans la* [dã:], *à la* [a:], *dans un* [dœ̃] | prep |
| `t1indirect` | Le discours indirect au présent : *si*, *ce que*, *ce qui*, et les pronoms qui changent | t1 |
| `t1notes` | Les connecteurs énumératifs et les abréviations de la prise de notes | t1 |
| `t2relatifs` | Les pronoms relatifs *qui*, *que*, *où* pour décrire un logement | t2 |
| `t2gerondif` | Le gérondif *en + -ant* : la simultanéité et la manière | t2 |
| `t3futur` | Le futur simple : ce que le bail prévoit | t3 |
| `t3impersonnel` | *C'est + adjectif + que/de* et la chute du sujet de *falloir* | t3 |

## Les trois productions

1. **Jeu de rôle** — scénario `louer`, qui existe déjà dans `server.py` (cas
   A, B, C). Aucune écriture dans le fichier partagé.
2. **Production orale** — faire visiter son logement et donner les
   renseignements sans qu'on ait à les demander deux fois.
3. **Production écrite** — le courriel de notes après un appel : ce qu'on a
   demandé, ce qu'on a appris, ce qui reste à vérifier.

## Ce que la production a changé au plan

- **24 exercices**, et non 26 : `t1questions` et `t2decrire` ont absorbé ce qui
  était prévu en deux exercices chacun.
- Les huit cartes de `prPhon` portent une **phrase entière** et non le fragment
  (« sur le »). Un fragment envoyé seul à la synthèse ressort sur-articulé,
  c'est-à-dire le contraire exact de ce que la leçon fait entendre.
- Les clés de `carrier.js` sont les **mots littéraux** : le gabarit fait
  `CARRIER_PHRASES[w]` sans normaliser. Une clé en style de nom de fichier
  (`avis_modification`) n'est jamais trouvée, et le mot part seul à la synthèse.
- Le scénario `louer` de `server.py` a été **réutilisé tel quel**, avec ses cas
  A, B et C : aucune écriture dans le fichier partagé, comme prévu.
