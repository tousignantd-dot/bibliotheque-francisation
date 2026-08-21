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

## Les modules neufs, mesurés autrement

Faute de version d'origine, un module écrit à partir du programme se mesure à
ses voisins : combien de ses énoncés visibles se retrouvent mot pour mot dans
un autre module du dépôt. Le seuil reste 5 %.

| Module | Énoncés | Communs | % | Nature |
|---|---|---|---|---|
| module-n6-recherche | 209 | 4 | 1,9 % | quatre consignes du gabarit |

Les quatre : « Le mot et sa définition », « Choisissez un mot, puis sa
définition. Six mots à la fois. », « Écoutez de nouveau le dialogue, puis
répondez. », « Glissez chaque photo sur la phrase qui la décrit. » Ce sont les
consignes que le moteur impose à ses types d'exercice — les faire varier pour
elles-mêmes nuirait à l'élève, qui les reconnaît d'un module à l'autre.

## Les modules neufs — mesure du 21 août 2026

Un module produit à partir du programme n'a **aucun antécédent SOFAD** : le
vérificateur de réécriture ne s'y applique pas, puisqu'il compare au plus
ancien état du fichier dans git — qui est déjà la version neuve. Le risque
change de nature : ce n'est plus la copie, c'est la **coïncidence avec les
modules déjà écrits**, sur les consignes génériques que le type de tâche
impose (« Écoutez de nouveau le dialogue, puis répondez. »).

La mesure est donc l'autre : on compare les énoncés visibles par l'élève
(`txt:` et `q:` de `exos.js`) à ceux de **tous** les autres modules générés.

| Module | Énoncés | Identiques ailleurs | % | Verdict |
|---|---|---|---|---|
| module-n5-logement | 162 | 0 | 0 % | 🟢 |
| module-n5-rendezvous | 136 | 0 | 0 % | 🟢 |

Comparé aux 1 949 énoncés des quatorze autres modules de `build/contenu/`.
Les consignes courtes (« Écoutez de nouveau le dialogue, puis répondez. »)
sont sous le seuil de longueur du relevé — elles se répètent d'un module à
l'autre et c'est voulu : une consigne d'exercice n'a pas à être originale, et
la varier pour la varier nuirait à l'élève, qui la reconnaît d'un module au
suivant.

`module-n5-rendezvous` (activité 65), mesuré le 21 août 2026 : ses 136 énoncés
visibles de 25 caractères ou plus ont été comparés aux 2 618 des vingt-deux
autres modules de `build/contenu/`. Aucun n'est identique. La situation du
programme ne fournissant aucun lexique, les seize mots du banc sont eux aussi
composés à partir des savoirs du niveau.
