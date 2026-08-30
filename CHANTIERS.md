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
| `seance-sans-compte` | dépôt principal | `seance.html`, `feuille-seance.html`, `progression.html`, `qr.py` | en cours |
| `validation` | `~/Claude/wt-validation` | `viewer.html`, `build/greffe_ateliers.py`, les 27 ateliers d'avant le système de design | en cours — branche `couloir/validation` |

## Couloirs fermés

_(rien encore — y déplacer la ligne quand la branche est fusionnée dans `main`
et le worktree retiré par `git worktree remove`)_
