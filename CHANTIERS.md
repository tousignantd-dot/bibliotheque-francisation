# Chantiers en cours — tableau d'affichage

Plusieurs conversations travaillent sur ce dépôt en même temps. Ce fichier est
le **verrou** : on l'inscrit avant de toucher au code, on le raye en finissant.

## Les trois règles

1. **Un couloir par conversation.** Un couloir est une liste de fichiers ou de
   dossiers. Deux couloirs ouverts en même temps ne se croisent jamais.
2. **Les fichiers partagés ne se partagent pas.** `CLAUDE.md`,
   `assets/design-system/`, `index.html`, et toute greffe qui touche les 87
   modules d'un coup (`build/greffe_*.py`) : **une seule** conversation à la
   fois. Ces travaux-là se font en série.
3. **Un worktree par conversation, hors du dépôt.**

   ```
   git -C ~/Claude/bibliotheque-francisation worktree add ~/Claude/wt-<nom> -b couloir/<nom>
   ```

   Dans un couloir : commiter des **chemins explicites** (jamais `git add -A`,
   jamais `git checkout` d'une autre branche), et ne rien pousser. La fusion
   vers `main` — donc vers Railway — se fait depuis la session du répertoire
   principal, une branche à la fois.

## Couloirs ouverts

| Couloir | Répertoire | Fichiers tenus | État |
|---|---|---|---|
| `seance-sans-compte` | dépôt principal | `seance.html`, `feuille-seance.html`, `progression.html`, `qr.py`, `viewer.html`, `server.py`, `build/direct_atelier.py` + les 6 générateurs de la banque et les **63 ateliers générés** | fusionné dans `main` |
| `espace-enseignant` | dépôt principal | `enseignant.html`, `js/enseignant.js`, `direction.html`, `progression.html`, `js/prof.js`, `catalogue.html`, `reseau.html` | fusionné dans `main` |
| `tutoriels-remise-a-jour` | dépôt principal | `assets/outils/guide-espace-enseignant.html`, `build/tutoriels/`, `assets/presentations/guide-tutoriels-*`, `assets/presentations/mode-sans-assistance.html`, `presentations.html` | **fait — 4 septembre 2026.** Les dix capsules sont tournées et montées avec la voix Azure HD, le logotype en ouverture et un compte d'enseignante. La méthode a changé en cours de route : plus rien ne se tourne sans passer par **l'atelier du guide** (`python3 build/tutoriels/atelier.py <capsule>`, port 5322), qui écrit dans le manifeste. Le guide papier se refait avec elles. |
| `boutons-tutoriels-logo` | dépôt principal | `enseignant.html`, `assets/design-system/tokens/fonts.css`, `assets/design-system/marque-francis.css`, `presentations.html`, `assets/presentations/tutoriels-a-refaire.html`, `assets/outils/tutoriels-enseignant.html`, `assets/outils/guide-espace-enseignant.html`, `build/tutoriels/` | fusionné dans `main` — 2 septembre 2026. Les neuf boutons au fond blanc ; Nunito servie par le dépôt et le point du logotype centré sur sa lettre ; relevé de ce qui a vieilli dans les tutoriels (`assets/presentations/tutoriels-a-refaire.html`). Le tournage des capsules attend une décision sur la voix — `assets/design-system/` est rendu. |
| `jeu-de-role-design` | dépôt principal | `build/greffe_jeu_de_role.py`, `build/gabarit/module.html`, les 78 `module-*` à jeu de rôle et leurs `build/contenu/*/custom.js` | fusionné dans `main` |
| `typographie-des-fiches` | dépôt principal | `build/powerpoints/fiche.py`, `build/powerpoints/decks/module-sante/*.py`, `build/audit_renvois.py`, les 1 265 fiches de `assets/documents/` | **fait — 7 septembre 2026.** Espace insécable devant `? ! ; :` dans `esc()` : un « ? » se retrouvait seul sur la troisième ligne d'un titre. Et le relevé des renvois à ce que la feuille ne porte pas (5 + 19 + 160). |
| `micro-du-jeu-de-role` | dépôt principal | `build/gabarit/module.html`, `build/greffe_micro.py`, les 78 modules à jeu de rôle | **fait, poussé et confirmé à l'oreille — 7 septembre 2026.** `abort()` au lieu de `stop()` : le micro se rendait à `onend`, une seconde après, et le déclic de Chrome tombait sur le premier mot de l'assistant. `JR.sourd` se lève maintenant à la fermeture et retombe à la réouverture. Deuxième greffe le même jour : « J'ai fini — corrigez mes phrases » ferme le micro **pour de bon** (`jrMicroArreter()`, `JR.reprise` remis à faux), mais seulement après le refus « parle d'abord ». |
| `fiches-plus` | dépôt principal | `build/fiches_plus.py`, `assets/documents/plus/`, `assets/presentations/fiches-plus-niveau-6.html`, `presentations.html` | **fait et poussé — 7 septembre 2026.** Une seconde série des 160 fiches du niveau 6, avec la mini-leçon imprimée dans la fiche de sa séance, et la page à deux onglets pour comparer. `assets/documents/` n'est pas touché : la série d'essai vit dans son sous-dossier. |
| `bornage-par-niveau` | dépôt principal | `server.py` (bornage par niveau), `reseau.html`, `catalogue.html`, `build/controles/niveaux_acces.py` | **fait et poussé — 7 septembre 2026.** Le champ `niveaux` sur la ligne d'accès : une personne bornée au niveau 6 y a tout, et rien ailleurs. Quatre points d'application, un seul texte de refus, et le trou de `?catalogue=1` bouché. Éprouvé au bac d'essai (26 vérifications) et le contrôle vu échouer sur ses quatre écarts. Détail : `CLAUDE.md`, section « Le bornage par niveau ». |
| `validation` | `~/Claude/wt-validation` | `viewer.html`, `assets/design-system/ateliers-mobile.css`, `build/greffe_ateliers.py`, `build/greffe_transcription.py`, `build/module.py`, `server.py`, les 27 ateliers d'avant le système de design, les 87 `module-*` | fusionné dans `main` — le verrou de transcription attend son interrupteur dans `js/enseignant.js` (couloir `espace-enseignant`) |

## Couloirs fermés

| Couloir | Répertoire | Fichiers tenus | État |
|---|---|---|---|
| `migration-groupes` | dépôt principal | `server.py` (`migrate_multi_groupes`), `data/activities.json`, `build/controles/migration_groupes.py` | fermé — poussé dans `main` le 31 août 2026 (`d130fcdf7`) |

## Les tutoriels, au 4 septembre 2026 — fait

**Dix capsules, vingt minutes, tournées et livrées.** Les sept premières ont
été refaites avec la voix Azure HD ; trois s'y sont ajoutées le 4 septembre :
`08-seance` (la séance sans compte), `09-suivre` (suivre la classe) et
`10-dossier` (le dossier d'un élève). Le guide papier les suit —
`assets/presentations/tutoriel-espace-enseignant.pdf`, quarante pages, dix
chapitres, le même texte que les films.

Les deux questions restées ouvertes sont tranchées : l'ordre des capsules suit
l'ordre des gestes de l'enseignante (« Ouvrir un groupe » est passée devant
« Planifier »), et le suivi d'un élève a bien eu sa capsule à lui — deux, même,
le groupe puis l'élève.

Trois choses valent d'être sues avant de retoucher la chaîne, et chacune a
coûté une prise :

· **Une fenêtre surgissante vole la fenêtre du tournage.** Refermer un
  `target=_blank` laissait la page filmée en 756 × 469 : les plans suivants
  sortaient cadrés de travers, sans une erreur nulle part. `surveillerFenetres`
  repose la fenêtre, et `guide_captures.js` en profite aussi.
· **Un repère `apres` posé derrière une navigation est déjà passé.** Ces
  gestes-là n'en portent aucun : ils se jouent au plus tôt, ce qui est le bon
  moment.
· **Le compte « en ligne » du direct ne retient que dix minutes** et se lit sur
  les réponses, pas sur les accès. Le geste `rafraichir-direct`, dans le
  `prepare` des capsules 8 et 9, rejoue la boucle semée de `traces_demo.py` —
  mêmes lignes, réécrites, seule l'heure change.

Ce qui reste : les verdicts sur `assets/presentations/storyboard-tutoriels.html`
(66 étapes, avec sa case de dépôt et son micro), et **rien n'est poussé** —
pousser déploie.

## Ce qui s'est croisé, et comment ça s'est joué

**30 août 2026 — mesurer un arbre partagé, c'est mesurer le travail des
autres.** Une session a lancé le serveur local sur le dépôt principal pour
vérifier une page, pendant qu'une autre écrivait dedans. Elle a mesuré du
travail à moitié fini et y a vu un défaut qui n'existait pas. Ce qui l'a
sauvée est un détail d'adresse — un paramètre qui n'était pas dans son code.

**Le disque n'est pas ce qui est en ligne, et dans cet arbre-ci il n'est même
pas ce qu'on croit avoir écrit.** Pour vérifier une page : servir une **copie
de la version commitée**, ou interroger l'adresse de production, jamais
l'arbre partagé.



**30 août 2026, 20 h 25 — un couloir a emporté le travail d'un autre.** Le
commit `9cb85f9b2` (« La classe d'un coup d'œil s'affiche même sans module
choisi ») a publié, avec le sien, un correctif de `progression.html` qui
n'était pas encore commité : la tuile « Élèves actifs » qui affichait
« 2 / 1 ». Rien n'est perdu — le code et son commentaire sont partis entiers,
et la correction est en service. Ce qui est perdu, c'est **le message** : rien
dans l'historique ne dit pourquoi cette tuile a changé, et le commit dit autre
chose que ce qu'il fait.

Deux leçons, et la première n'est pas celle qu'on croit :

· `git add <fichier>` **ne suffit pas** quand deux sessions écrivent dans le
  même fichier. La règle du dépôt vise `git add -A` ; ici le chemin était
  explicite, et l'accident a eu lieu quand même, parce que l'index prend le
  **fichier tel qu'il est sur le disque**, pas le morceau qu'on croit
  ajouter. Deux sessions dans un même fichier ne se protègent qu'en n'y étant
  pas en même temps.
· `progression.html` était déclaré au couloir `espace-enseignant` et a été
  écrit depuis un autre. Un couloir ne vaut que si on le lit avant d'ouvrir un
  fichier — c'est tout ce que ce tableau sait faire.



**30 août 2026 — les ateliers, deux fois.** `seance-sans-compte` a instrumenté
les **63 ateliers générés** pour le direct de la classe pendant que
`validation` posait une greffe mobile sur ceux d'avant le système de design.
Les deux listes se sont trouvées **disjointes** — vérifié fichier par fichier,
avant de pousser. La leçon n'est pas qu'on a eu de la chance : c'est que
« les ateliers » n'est pas un couloir. `assets/interactive/` contient deux
familles qui ne se touchent jamais — ce qui sort de `build/banque.py`, et le
reste. **Un couloir se nomme par ce qui produit les fichiers, pas par le
dossier où ils tombent.**

`viewer.html` a bien été tenu par les deux, à un jour d'écart : la correction
`100dvh` est passée par `main` avant que `validation` n'ouvre sa branche, qui
l'a donc reprise sans le savoir. C'est le bon ordre, et c'est celui que la
règle 3 décrit — on part de `main`, on n'y revient qu'une branche à la fois.


**31 août 2026 — un garde qui regarde le mauvais endroit.**
`migrate_multi_groupes()` décidait de repartir ou non en demandant si
`data/schedule.json` existait **sur le disque**. En production, ce fichier
n'existe pas et n'existera jamais : `schedule.json` fait partie de
`db.DOCUMENTS`, la planification vit dans Postgres, et le fichier est dans
`.gitignore` — donc absent du dépôt que `init_storage` recopie sur le volume.
Le garde était ouvert en permanence, et la migration tournait à chaque
redémarrage : 177 activités datées au premier groupe, et la planification de
tous les autres remplacée d'un seul `save_schedule()`.

Trois leçons, et la première vaut au-delà de ce fichier :

· **Un garde doit interroger la couche qui détient la donnée**, jamais le
  support. Le jour où le stockage a changé, tous les `Path.exists()` posés sur
  des documents gérés par la base ont cessé de vouloir dire quelque chose —
  sans rien casser bruyamment, ce qui est le pire des cas.
· **Trois dates oubliées dans un fichier versionné suffisent à tout changer.**
  `data/activities.json` portait encore `dateVue`/`datePrevue` sur les modules
  4, 5 et 6 — le résidu de quelqu'un qui s'en était servi. Ces champs
  appartiennent au volume (`USER_FIELDS`), et il a fallu ces trois-là pour que
  toute installation neuve se fasse passer pour une installation historique.
· **Ce qui tourne à chaque démarrage se contrôle**, sinon rien ne le regarde
  jamais : `build/controles/migration_groupes.py` reprend les trois formes —
  installation neuve, forme Postgres, installation réellement historique.
