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
| `espace-enseignant` | dépôt principal | `enseignant.html`, `js/enseignant.js`, `direction.html`, `progression.html`, `js/prof.js`, `catalogue.html`, `reseau.html` | en cours |
| `validation` | `~/Claude/wt-validation` | `viewer.html`, `assets/design-system/ateliers-mobile.css`, `build/greffe_ateliers.py`, `build/greffe_transcription.py`, `build/module.py`, `server.py`, les 27 ateliers d'avant le système de design, les 87 `module-*` | fusionné dans `main` — le verrou de transcription attend son interrupteur dans `js/enseignant.js` (couloir `espace-enseignant`) |

## Couloirs fermés

| Couloir | Répertoire | Fichiers tenus | État |
|---|---|---|---|
| `migration-groupes` | dépôt principal | `server.py` (`migrate_multi_groupes`), `data/activities.json`, `build/controles/migration_groupes.py` | fermé — poussé dans `main` le 31 août 2026 (`d130fcdf7`) |

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
