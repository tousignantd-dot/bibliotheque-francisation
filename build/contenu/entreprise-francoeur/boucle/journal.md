# Journal de révision — Maison Francœur

## Tour 1 → révision des bloquants (24 septembre 2026)

Premier audit : **2 bloquants, 29 majeurs, 43 mineurs** (`audit1-contenu.json`,
`audit1-page.json`, page `assets/presentations/francoeur-audit-1.html`).
Critères les plus touchés : A3, E1, F1, D4, G1.

| Élément | Statut | Avant | Après | Critères | Pourquoi |
|---|---|---|---|---|---|
| Exercice 5 « Ce que le client veut » (20 demandes) | modifié | trois distracteurs qui changent chacun UN trait de la bonne carte (article, couleur ou taille) | carré latin : (A,C,T) (A,C′,T′) (A′,C,T′) (A′,C′,T) — chaque valeur deux fois ; sans taille, (A,C) (A,C′) (A′,C) (A′,C′) | D4 · bloquant | La bonne carte était la majoritaire sur chaque trait : 20 demandes sur 20 se réussissaient sans écouter. Désormais aucune carte n'est majoritaire ; seule la phrase désigne la bonne. |
| Test, partie B, crans 2 et 3 (9 items) | modifié | même règle ; au cran 3, trois cartes écrites à la main | même carré latin ; au cran 3 on écrit les valeurs que la phrase ÉCARTE (b31 : le chandail, b32 : le rose, b33 : le moyen, b34 : le noir), et le carré les place | F1 · bloquant | 9 items sur 14 se devinaient : le niveau proposé et l'écart entre deux passations étaient faussés. Le piège voulu (ce que le client nie ou reprend) est conservé. |
| Construction (`francoeur_planches.py`) | ajouté | — | `devinable()` : la construction s'arrête si une bonne carte est seule à réunir les valeurs les plus fréquentes | D4, F1 | Le contrôle qui manquait. Vu échouer sur l'ancien motif (vrai), et passer sur le carré (faux). |

Vérifié : 0 item devinable sur 20 (exercice) et sur 14 (test B) ; l'exercice et
le test se jouent au navigateur sans erreur.

**Reste à traiter** : les 29 majeurs, selon les décisions de Daniel sur la page
des constats — puis le tour 2 de l'audit, sur TOUTE la grille.

## Tour 1 → révision des majeurs (24 septembre 2026)

Les 29 majeurs, regroupés par chantier. Chaque ligne porte ses codes.

| Chantier | Statut | Avant | Après | Critères | Pourquoi |
|---|---|---|---|---|---|
| Accueil | modifié | un menu de six portes | la première fois, une tâche (un client dit « une tuque », on la touche) ; puis le chemin en cinq étapes avec « prochaine » et le rappel J+2 / J+7 / J+30 | B1, F3 | Commencer par faire, pas par choisir ; revenir au bon moment. |
| Objectifs et seuils | ajouté | aucun critère de réussite écrit | O1–O5 avec seuils (7/8, 6/8…) dans les bilans, le guide et le test (A 80 %, B 70 %, C 70 %) | A1, A3 | Un objectif sans critère ne dit pas quand on a fini. |
| Rétroaction | modifié | « Non » + la bonne réponse | on nomme ce qui a été choisi, ce qui diffère de la bonne carte, et l'explication de la réponse | E1 | « Faux » n'apprend rien ; dire pourquoi, si. |
| Pièges France/Québec | ajouté | notés sur la fiche, jamais pratiqués | série « Les pièges » (contrastes différents du test), piège toujours visible avec la langue d'appui, et l'autre mot à écouter | D4, C4 | Un état qui fait échouer se pratique avant. |
| Exemple travaillé | ajouté | on entrait au magasin sans modèle | « Les gestes du vendeur » : cinq dialogues modèles, phrase clé marquée, puis « Ce que je réponds » (8 cas, rétroaction par choix) | C4, E1 | Voir faire avant de faire. |
| Consignes de la gérante | ajouté | aucune pratique de la parole interne | exercice « La gérante » (16 consignes) | A2, A3 | L'écart visé comprend le travail entre collègues. |
| Test | modifié | une seule forme, la partie D absente | deux formes équivalentes alternées ; D = quatre gestes oraux notés par geste (« a fait le geste / a deviné ou promis / pas de réponse ») | F1, F2 | Une reprise ne se fait pas sur les mêmes items ; l'oral s'évalue au geste. |
| Magasin | modifié | débutant : trois clients ; bilan de grammaire seul | cinq clients au débutant ; « avant d'entrer » ; les phrases repliables pendant la visite ; humeur écrite sous le visage ; bilan par geste (fait / manque / inutile), rapporté au direct | A3, E1, E2, G1 | Le bilan doit porter sur l'objectif (les gestes), pas sur l'orthographe. |
| Fiche de poche à l'écran | ajouté | papier seulement | écran « Ma fiche de poche », six phrases avec voix et « quand » dans la langue d'appui | F2 | Sous la main au travail. |
| Lexique | modifié | veste, veston, denim, culotte… ambigus | notes nuancées ; « du jeans » ; autre mot pour culotte, fermeture, extensible | C3 | Le mot d'ici est celui que le client dira. |
| Boutons trop proches (remarque de Daniel) | modifié | 8 px, ou rien hors du jeu | 12 px partout, contrôle `window.__francoeur.espaces()` : 0 défaut sur 30 écrans à 375 et 1280 px | G1 | Un doigt qui touche le voisin. |
| Barre de marque (remarque de Daniel) | modifié | colonne de 1000 px, gouttière de 32 px, décalée du titre | même colonne que la page (1080 px, 16 px) : aligné au pixel à 375, 1100 et 1600 px | G1 | « francis » doit tomber sur la ligne du reste de la page. |

Voix : 373 enregistrements Azure HD, retranscrits (22 douteux, 4 refaits).

**Reste** : le tour 2 de l'audit, sur TOUTE la grille, page servie et mesurée.

## Tour 2 → révision (24 septembre 2026)

Second audit (toute la grille, deux regards neufs, page servie à 375/1280) :
**0 bloquant, 8 majeurs, 41 mineurs** (`audit2-contenu.json`, `audit2-page.json`,
page `francoeur-audit-2.html`). Presque tous les majeurs venaient des
corrections du tour 1 — la seconde forme, l'exercice 7, le compteur d'essais.

| Élément | Statut | Avant | Après | Critères | Pourquoi |
|---|---|---|---|---|---|
| Seuils du test | modifié | taux brut de toutes les réponses contre 80 % / 70 % | objectif atteint quand le cran qui porte sa tâche est validé : A cran 3 (pièges), B et C cran 2 | F1 · majeur | Dans un test adaptatif, le taux dépend de l'ordre des erreurs : « O2 atteint » tombait sur un cran qui ne demande pas la taille. |
| Pièges dans les deux formes | modifié | six pièges en forme 1, aucun en forme 2 | trois pièges + trois items fins dans chaque forme | F1 · majeur | La passation finale ne mesurait plus les pièges. « Équivalentes » devient « parallèles » dans le guide et la démo, à vérifier au pilote. |
| Partie orale D | modifié / ajouté | la même aux deux formes, proche des modèles ; clé et grille sur l'écran de l'employé | D2 : quatre situations neuves (bas de chasse, bottes, robe de la vitrine, parka mis de côté) ; clé et notation derrière le code du formateur (dans le guide seulement) | F1 · majeur (deux fois) | L'employé voyait la réponse et pouvait se noter lui-même. |
| Distracteurs défendables | modifié | kangourou pour coton ouaté, tailleur pour habit | col roulé, veste de laine, t-shirt ; chemise, cravate, manteau ; « un sac » retiré face à la sacoche ; contrôle au build contre les notes du lexique (le sens de France d'un piège reste permis : c'est lui qu'on veut voir tomber) | D4 · majeur | Deux erreurs arrêtent la partie : un item défendable peut la couper. |
| « Ce que je réponds » | modifié / ajouté | bonne réponse souvent la plus longue ; « Oui. », « Non. » faux partout ; 8 items | longueurs nivelées (seule plus longue : 3 sur 10), mauvaises réponses polies qui font le mauvais geste, deux paires contrastées (dit vite / dit clairement ; sans reçu / avec reçu) | D4 · majeur | On faisait 5 sur 8 sans écouter. |
| Essais au direct | modifié | 1 au premier coup | 0 au premier coup (échecs antérieurs), comme les modules | A3 · majeur | Aucun « premier coup » ne paraissait au direct : la règle du pilote était illisible. |
| La taille décide | modifié | carré latin : article + couleur suffisaient toujours | un trait décisif varie seul, les deux autres ensemble ; les reprises nomment le leur ; la taille décide 10 demandes sur 22 (4 sur 4 aux reprises sur la taille) et 3 items sur 8 / 3 sur 7 au test ; contrôlé au build | A3, F1 · majeur | O2 dit article, couleur ET taille. |
| Mineurs rapides | modifiés | — | traduction blanche sous les boutons rouges ; codes « O1 » retirés de l'écran ; rayon vide → tous les rayons ; porte « La série des pièges » ; rétroaction du rayon au 1er essai ; « Je me souviens » hors seuil ; mot sans image parmi des mots écrits ; article marqué dans la transcription ; explication de la bonne réponse traduisible ; minuteries remplacées par un bouton ; tâche d'accueil sans la réponse au 1er essai ; menu et résumé à 44 px ; texte discret foncé (≥ 4,5:1) ; couleurs confondues jamais opposées ; `espaces()` sans les boutons repliés ; consigne du jeu de rôle réglée au palier ; guide juste sur l'oral et les données | E1, G1, G2, C5, D1, D3, A2 | — |

Voix : 14 nouvelles (Azure HD), retranscrites justes ; 381 en tout, 19 douteuses.
**Traductions en attente** : l'API Anthropic a atteint la limite d'usage fixée
au compte (retour le 1er octobre 2026). Les textes nouveaux ou changés restent en
français sous la langue d'appui ; les sept traductions devenues fausses ont été
retirées plutôt que laissées. Relancer `python3 build/francoeur_traductions.py
--interface` et `--ids veste` quand l'accès revient.

**Reste** : le tour 3 de l'audit, sur toute la grille.
