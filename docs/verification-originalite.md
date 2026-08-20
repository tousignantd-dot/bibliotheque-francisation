# Relevé d'originalité des modules

Mesure produite le **20 août 2026** par
`~/.claude/skills/module-parite/scripts/verifier_copie.py`, qui compare les
énoncés visibles par l'élève (`EXOS`) de la version actuelle au plus ancien
état du fichier dans l'historique git — c'est-à-dire au contenu dérivé de la
Collection Connexion (SOFAD) d'avant la réécriture.

Seuils du vérificateur : 🟢 < 10 %, 🟠 10–20 %, 🔴 ≥ 20 %.

| Module | Énoncés | Identiques | % | Verdict |
|---|---|---|---|---|
| module-consultation | 94 | 0 | 0 % | 🟢 |
| module-sante | 24 | 0 | 0 % | 🟢 |
| module-meteo | 90 | 0 | 0 % | 🟢 |
| module-pub | 71 | 0 | 0 % | 🟢 |
| module-logement | 86 | 0 | 0 % | 🟢 |
| module-banque | 101 | 0 | 0 % | 🟢 |
| module-urgence | 98 | 1 | 1 % | 🟢 |
| module-procedure | 71 | 1 | 1 % | 🟢 |
| module-probleme | 141 | 2 | 1 % | 🟢 |
| module-nouvelles | 85 | 5 | 6 % | 🟢 |
| module-travail | 110 | 12 | 11 % | 🟠 |

## Nature des coïncidences

Elles ont été relevées une à une, pas seulement comptées. La quasi-totalité
sont des **consignes génériques** d'exercice, pas du contenu narratif :
« Qui appelle qui ? », « Quel est le but de l'appel ? », « La formule de
politesse », « Qui ? (les personnes concernées) ». Ce sont les formes
standard d'un exercice de compréhension orale, imposées par le type de tâche
et par le vocabulaire du programme ministériel.

Deux exceptions notées :

- `module-nouvelles` — une question porte sur une expression précise du texte
  source (« un franc succès »). À reformuler à la prochaine touche.
- `module-probleme` — deux phrases de contenu banales (« Le robinet de la
  cuisine coule depuis deux jours. »), sur 141 énoncés.

## Suite

- `module-travail` : varier les 12 consignes pour descendre sous 5 %. Aucune
  urgence, mais à faire avant une éventuelle diffusion élargie.
- **Les modules produits à partir de maintenant ne sont plus des réécritures.**
  Ils sont écrits à partir de `~/Claude/programme/programme-francisation.json`
  — le programme d'études officiel du MEQ — sans source antérieure. Le
  vérificateur n'a plus d'objet pour eux : il n'existe pas de version d'origine
  à laquelle les comparer.
