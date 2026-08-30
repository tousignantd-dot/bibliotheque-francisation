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
| `espace-enseignant` | dépôt principal | `enseignant.html`, `js/enseignant.js`, `direction.html` | en cours |
| `validation` | `~/Claude/wt-validation` | `viewer.html`, `build/greffe_ateliers.py`, les 27 ateliers d'avant le système de design | en cours — branche `couloir/validation` |

## Couloirs fermés

_(rien encore — y déplacer la ligne quand la branche est fusionnée dans `main`
et le worktree retiré par `git worktree remove`)_

## Ce qui s'est croisé, et comment ça s'est joué

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
