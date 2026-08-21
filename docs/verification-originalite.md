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
| module-n5-urgence | 283 | 0 | 0 % | 🟢 |

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

`module-n5-urgence` (activité 66), mesuré le 21 août 2026 : ses 283 énoncés
visibles de plus de douze caractères — consignes, titres d'exercices, intitulés
de bandeau noir compris, donc un relevé plus sévère que celui du module
précédent — ont été comparés aux 6 001 des vingt-trois autres modules de
`build/contenu/`. Première mesure : 16 identiques, soit 5,7 %, toutes des
consignes génériques (« Le mot et sa définition », « Écoutez le dialogue du
Défi 1, puis répondez. ») ou des intitulés de règle (« La forme négative »).
Elles ont été reformulées avec les mots du module — « Réécoutez l'appel de deux
heures du matin, puis répondez. » — ce qui ramène la mesure à **0 identique**.

L'opération est sans risque à condition de vérifier une chose : ni les `sub` ni
les `tit` d'un exercice n'entrent dans le relevé des sons. Le manifeste des 183
extraits est resté identique avant et après, donc aucun MP3 n'a été à refaire.

`module-n3-restaurant` (activité 77), mesuré le 21 août 2026 : ses **139**
énoncés visibles de plus de vingt-cinq caractères ont été comparés à ceux des
vingt-cinq autres modules de `build/contenu/`. **Aucun n'est identique.**

Le relevé large — 225 chaînes, consignes, titres d'exercices et mots du banc
compris — rend 17 coïncidences, soit 7,6 %. Elles ont été regardées une à une :
ce sont les six consignes que le moteur impose à ses types d'exercice
(« Le mot et sa définition », « Écoute de nouveau le dialogue, puis
réponds. », « Glisse chaque photo sur la phrase qui la décrit. »,
« Complète avec « ce », « cet », « cette » ou « ces ». »…) et **quatre mots du
lexique** — *la caisse*, *un accompagnement*, *le poulet*, *une minute* — qui
appartiennent au programme et qu'on ne va pas renommer pour éviter un doublon.
Rien de narratif, aucun énoncé de contenu.

La leçon de `module-n5-urgence` tient toujours : reformuler une consigne avec
les mots du module est sans risque, puisque ni les `sub` ni les `tit` n'entrent
dans le relevé des sons. Ici, elle n'a pas été appliquée aux quatre mots de
lexique — les renommer aurait éloigné le module du programme, qui est la seule
source.

`module-n5-travail` (activité 67), mesuré le 21 août 2026 : ses **203** énoncés
visibles de plus de douze caractères — `txt`, `q`, `a`, `sub` et `tit`, donc le
relevé large — ont été comparés aux 4 687 des vingt-six autres modules de
`build/contenu/`. Première mesure : **3 identiques, soit 1,5 %**, toutes des
consignes que le moteur impose à ses types d'exercice (« Chaque mot, sa
définition », « Prenez un mot, puis glissez dessus la définition qui lui va »,
« Faites glisser chaque photo vers la phrase qui lui correspond »). Elles ont
été reformulées avec les mots du module — « Les seize mots du poste »,
« Prenez un mot du bureau… », « Faites glisser chaque photo du bureau vers la
phrase qui la décrit » — ce qui ramène la mesure à **0 identique**.

La leçon de `module-n5-urgence` a été appliquée dans l'ordre qu'elle recommande :
**le contrôle d'originalité passe avant la génération des MP3, pas après.** Les
trois reformulations ne touchent que des `sub` et des `tit`, qui n'entrent pas
dans le relevé des sons ; aucun extrait n'a été payé puis jeté.

`module-n2-couloirs` (activité 90), mesuré le 21 août 2026 : ses énoncés
visibles de plus de douze caractères — `txt`, `q`, `a`, `sub`, `tit`, plus les
mots et définitions du banc, donc le relevé large — ont été comparés à ceux des
vingt-huit autres modules de `build/contenu/`. Première mesure : **6 identiques
sur 113, soit 5,3 %**, toutes des consignes que le moteur impose à ses types
d'exercice (« Le mot et sa définition », « Écoute de nouveau le dialogue, puis
réponds. », « Glisse chaque photo sur la phrase qui la décrit. »). Reformulées
avec les mots du module — « Réécoute Soraya et Gilles dans le corridor, puis
réponds. », « Les seize mots du centre » —, la mesure retombe à **0 identique
sur 117**.

La mesure a été faite **avant** la génération des MP3, comme la nuit du 21 août
l'a établi : les 205 clés du relevé des sons sont restées identiques après
reformulation, puisque ni les `sub` ni les `tit` n'y entrent. Aucun extrait
n'a été payé deux fois.

`module-n3-pharmacie` (activité 78), mesuré le 21 août 2026 : ses **228**
énoncés visibles de plus de douze caractères — `txt`, `q`, `a`, `sub` et `tit`,
donc le relevé large — ont été comparés aux 6 312 des vingt-huit autres modules
de `build/contenu/`. Première mesure : **17 identiques, soit 7,5 %**, toutes
des consignes ou des titres que le moteur impose à ses types d'exercice (« Le
mot et sa définition », « Écoute de nouveau le dialogue, puis réponds. »,
« Glisse chaque photo sur la phrase qui la décrit. ») — plus quatre mots du
lexique. Dix reformulations avec les mots du module — « Les seize mots de la
pharmacie », « Réécoute la scène du renouvellement, puis réponds. », « Fais
glisser chaque photo de la pharmacie vers la phrase qui la décrit » — ramènent
la mesure à **4 identiques, soit 1,8 %**.

Les quatre qui restent sont des **mots du lexique du programme** — *une
ordonnance*, *la carte d'assurance maladie*, *une étiquette* — que
`module-n5-rendezvous` et `module-alimentation` emploient aussi. Les renommer
éloignerait le module du programme, qui est sa seule source. Rien de narratif,
aucun énoncé de contenu.

Le contrôle a été fait **avant la génération des MP3**, et les reformulations
ne touchent que des `sub` et des `tit`, qui n'entrent pas dans le relevé des
sons : les 231 clés de `sons_module_n3_pharmacie.json` sont restées les mêmes
avant et après.
