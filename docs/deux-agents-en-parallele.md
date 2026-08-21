# Deux agents en parallèle — consignes

Ce fichier existe parce que quatre sessions ont travaillé dans ce dépôt le
20 août 2026 et que trois d'entre elles se sont nui sans le vouloir. Il dit ce
qu'il faut faire pour que deux agents produisent deux modules en même temps
sans se marcher dessus.

Il sert de deux façons : le **protocole** vaut pour n'importe quelle paire
d'agents, et la **répartition** en fin de fichier est celle du moment. Quand
la paire change, on réécrit la répartition, pas le protocole.


## La répartition en cours

| Qui | Module | Slug | Activité | Format |
|---|---|---|---|---|
| Session A | Niveau 7 · Suivi de l'actualité | `module-n7-actualite` | **60** | 16 séances |
| Session B | Niveau 8 · Emploi | `module-n8-emploi` | **61** | 16 séances |

C'est la vague 1 de `docs/vagues-suivantes.md`, lancée le 20 août 2026 pendant
que `module-n5-logement` finissait ses images — donc trois sessions dans le
dépôt un moment, une de plus que ce que ce fichier recommande. Raison assumée :
l'utilisateur est absent et le niveau 5 est à son dernier pas.

Les niveaux 5 et 6 de la répartition précédente sont livrés (activités 58 et
59). Les vingt-cinq consignes des vagues suivantes sont écrites d'avance dans
`docs/consignes-a-coller.md`, numéros d'activité réservés jusqu'à 86.

**Les numéros d'activité sont réservés d'avance, et c'est le point le plus
important de ce fichier.** Le numéro d'activité est la clé qui relie
`build/powerpoints/modules.py`, `data/activities.json` et le portail. Deux
agents qui prennent « le prochain numéro libre » à dix minutes d'intervalle
prennent le même.

Le format long, seize séances, se prend dans `build/powerpoints/modules.py` :
`GRILLE_3_DEFIS` (quatre séances par bloc, trois défis) ou `GRILLE_2_DEFIS`
(deux défis plus longs). `GRILLE_COURTE` est réservée aux niveaux 1 et 2.


## Les cinq règles

**1. `git add` avec des chemins explicites. Jamais `git add -A`, jamais
`git add .`.**

C'est la règle qui compte le plus. Le 19 août, trois commits d'affilée ont
emporté le travail non commité d'une autre session sous un message sans
rapport — 271 lignes de `forge.py` ont failli être perdues. Un `git status`
qui montre des fichiers que tu n'as pas écrits n'est pas une anomalie à
nettoyer : c'est le travail de quelqu'un d'autre.

**2. Commiter et pousser souvent, par petites tranches.**

Ce qui traîne non commité est ce qui se fait ramasser. Un module se pousse
très bien en quatre ou cinq commits : le contenu, les médias, les séances, la
livraison. N'attends pas d'avoir tout fini.

**3. `git pull` juste avant de toucher un fichier partagé.**

La liste est plus bas. Ce sont les seuls endroits où deux agents peuvent
vraiment entrer en collision, et ils sont peu nombreux.

**4. Ce qui doit survivre s'écrit dans le dépôt, pas dans un message.**

Une session meurt et emporte tout ce qu'elle savait. Le 20 août, une session a
travaillé toute sa durée en s'interdisant `build/gabarit.py` pour protéger une
greffe qui n'avait jamais été en danger ; elle est morte avant que la
correction ne lui parvienne. Une décision, une contrainte, un piège découvert :
ça va dans `CLAUDE.md` ou dans `docs/`. Un message à une session sœur ne sert
qu'à la prévenir qu'un fichier vient de changer.

**5. Les changements transversaux se font quand personne d'autre n'écrit.**

Refonte du gabarit, du moteur, du système de design, d'une règle de couleur :
ces changements touchent tous les modules à la fois. Le 20 août, la règle
« la couleur d'un module est celle de son niveau » a modifié 141 fichiers en
une fois. Si quelqu'un avait été au milieu d'un module, le conflit aurait été
pénible. Préviens et attends.


## Les fichiers partagés

Tout le reste est à toi seul. Le contenu d'un module est isolé — c'est ce qui
rend la parallélisation possible :

    build/contenu/<slug>/            à toi
    assets/interactive/<slug>/       à toi
    build/powerpoints/decks/<slug>/  à toi
    assets/powerpoints/<slug>/       à toi
    generer_audio_<slug>.py          à toi
    sons_<slug>.json                 à toi

Les fichiers ci-dessous sont **partagés**. Fais `git pull` juste avant, écris,
commite et pousse tout de suite — ne les garde pas ouverts une demi-journée.

| Fichier | Quand tu y touches | Risque |
|---|---|---|
| `build/powerpoints/modules.py` | une fois, pour inscrire ton module | deux entrées ajoutées au même endroit |
| `data/activities.json` | une fois, pour inscrire ton activité | idem, et le numéro d'activité |
| `data/sections.json` | à la livraison, via `python3 build/sections.py` | le script réécrit tout le fichier |
| `data/materiel.json` | à la livraison, via `python3 build/materiel.py` | idem |
| `server.py` | si ton module a besoin d'un scénario de jeu de rôle | deux ajouts dans le même dictionnaire |
| `CLAUDE.md`, `docs/` | quand tu documentes une décision | à écrire, jamais à réécrire |

Les deux scripts `sections.py` et `materiel.py` **régénèrent le fichier
entier** à partir du disque. Si tu le lances alors que l'autre agent vient de
publier son module, tu inscris son module aussi — c'est sans danger, c'est même
souhaitable, mais dis-le dans ton message de commit pour que la ligne
supplémentaire ne surprenne pas.


## Un mot sur `server.py`

Le niveau 6 « Recherche d'emploi » n'a **pas** de scénario de jeu de rôle : les
douze scénarios existants sont `louer`, `probleme`, `relations`, `chemin`,
`activite`, `epicerie`, `appareil`, `restaurant`, `presenter`, `allees`,
`vetement`, `autobus`. Tu devras en ajouter un.

Deux pièges appris en le faisant pour le niveau 2 :

- Un module se construit **sans erreur** même si son `jr_scenario` n'existe pas
  dans `server.py`. Rien ne le vérifie. Le jeu de rôle échoue seulement à
  l'exécution, chez l'élève. Vérifie que la clé existe.
- Ne réutilise pas un scénario d'un autre niveau parce que le sujet ressemble.
  Ils portent leur niveau dans leur conduite : le scénario `chemin` du niveau 4
  donne six étapes et des noms de terminus, ce qui est ingérable au niveau 2. Un
  scénario, c'est un dictionnaire de cas et une entrée dans
  `JEU_DE_ROLE_SCENARIOS` — une trentaine de lignes.

Concrètement : `git pull`, ajoute ton dictionnaire de cas **juste avant**
`JEU_DE_ROLE_SCENARIOS`, ajoute ton entrée **en tête** du dictionnaire, commite,
pousse. Deux agents qui font ça chacun de leur côté fusionnent proprement.

Le niveau 5 « Location d'un logement » réutilisera le scénario `louer`, qui
existe déjà. La session A ne devrait donc pas toucher `server.py`, mais fais
quand même ton `git pull`.


## La méthode

Elle est écrite et elle ne s'invente pas : **la skill `module-neuf`**, avec ses
six références (`1-cadrer` … `6-livraison`). Suis-la. Elle couvre le cadrage
par le programme, l'invention du scénario, les sept fichiers de contenu, la
construction, les médias et la livraison.

Trois rappels qui viennent des modules livrés cette semaine :

- **Rien ne se copie du manuel SOFAD.** Le manuel est un modèle de structure et
  de progression grammaticale, jamais une source de texte. Le scénario, les
  personnages, les dialogues et les exercices s'inventent.
- **Un module neuf n'a aucune couleur à choisir.** La couleur de l'en-tête est
  celle de son niveau — le 6 est acier `#1D6B8F` / `#E7F0F6`. Il suffit de
  donner le niveau au registre : `build/couleurs_niveau.py` pose le reste. Et
  `sections.js` ne doit contenir ni `#166534` ni `#0F766E` : le vert est sorti
  du repérage.
- **La reprise réseau du générateur audio.** ElevenLabs coupe par
  intermittence, plusieurs fois par jour en ce moment. Copie la fonction
  `parle()` de `generer_audio_module_n2_autobus.py`, qui réessaie cinq fois en
  doublant l'attente et traite les 429 et les 5xx. Un échec réseau ne veut pas
  dire que l'extrait est en cause : relancer plus tard suffit, et le script est
  relançable — il saute ce qui existe déjà.


## Avant de publier

Les six contrôles sont réunis dans `CLAUDE.md`, section « Les contrôles avant
de publier un module ». C'est là qu'ils vivent, et c'est là qu'il faut les
relire : ils sortent tous en code 1 sur écart, donc ils s'enchaînent. Les
quatre premiers portent sur le module interactif, les deux derniers sur les
séances — un module n'est pas publié sans ses présentations et ses fiches.

Le déploiement se fait **sur `git push`** — Railway s'en charge, ne lance
jamais `railway up`. Compte quelques minutes avant que les médias neufs soient
servis, et vérifie en production plutôt qu'en local : une synchronisation de
volume s'est déjà arrêtée en cours de route et un module entier répondait 404.


## Ce qui a réellement mal tourné, le 20 août 2026

À lire une fois. Ce sont les quatre incidents qui ont produit les cinq règles.

1. **Trois commits ont emporté le travail d'une autre session** sous des
   messages sans rapport. Cause unique : `git add -A`.
2. **Une session s'est bridée pour rien** pendant toute sa durée, en
   s'interdisant `build/gabarit.py` au nom d'une contrainte qui n'existait pas.
3. **Une information périmée a circulé** d'une session à l'autre : un défaut
   déjà corrigé la veille a été signalé comme à corriger, parce que l'arbre
   local de l'émetteur n'était pas à jour. `git pull` avant de diagnostiquer.
4. **La session concernée est morte** avant de recevoir la correction. Ce qui
   se dit entre agents ne survit pas ; ce qui est écrit dans le dépôt, oui.

À quatre, la coordination a coûté plus de messages que de code. À deux, avec
ces règles, deux modules par jour sont un objectif raisonnable.
