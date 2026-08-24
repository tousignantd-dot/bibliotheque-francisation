# La banque du niveau 1 — plan de production

Écrit le 24 août 2026, juste après la livraison de l'activité 124
(« Même mot, autre police »). Il y a une version à lire, publiée comme
artefact ; celle-ci est la trace qui survit à la session.

## Le constat

Le niveau 1 n'a que **quatre situations** au programme — Inscription,
Orientation dans l'établissement, Relations sociales, Salle de classe — et les
quatre ont déjà leur module (activités 56, 96, 97, 98). Un cinquième cours
referait ce qui existe.

La place qui reste est dans les **savoirs que les modules ne peuvent pas
drainer**. Le programme en met trente-deux au niveau 1, dont douze de
phonétique et de graphie (`n1-s21` à `n1-s32`), et chaque module est happé par
sa situation. Un module de huit séances est le bon prix pour une situation ;
c'est le mauvais prix pour faire distinguer `a`, `i` et `ou`.

**La réponse n'est pas une liste d'activités, qui s'épuiserait — ce sont quatre
générateurs.** Chacun tient une *forme* d'exercice ; chaque exercice n'est plus
qu'un fichier de contenu, comme `build/vocab_flash.py` sert deux thèmes et
`build/polices.py` un. Le vingt-troisième exercice devient une affaire de
minutes.

## Les quatre familles — 22 exercices, 30 des 32 savoirs

### A · Apparier des représentations — `build/appariement.py`

Une même chose, montrée de quatre ou six façons. **Aucun son requis.** Le
générateur est `build/polices.py` généralisé : il est écrit aux quatre
cinquièmes.

| Exercice | Savoir | État |
|---|---|---|
| Même mot, autre police | `n1-s32` | **livré** — activité 124 |
| L'heure, quatre horloges | `n1-s32` `s27` | à écrire |
| Les abréviations (`app.`, `boul.`, `QC`, `NAS`, `F/H`, `n°`) | `n1-s32` `s25` | à écrire |
| Trois façons d'écrire une date | `n1-s32` `s26` | à écrire |
| Le chiffre et le mot | `n1-s26` `s10` | à écrire |
| Le panneau et son dessin | `n1-s28` | à écrire |

### B · Discriminer à l'oreille — `build/oreille.py`

Un son joue, deux ou trois boutons. Mécanique déjà éprouvée dans `essai-brin/`
(brin contre brun). **Sans MP3 ces exercices ne sont pas muets : ils n'ont pas
de contenu.** Toute la famille attend le rechargement du compte ElevenLabs.

| Exercice | Savoir |
|---|---|
| a · i · ou | `n1-s22` |
| p/b · t/d · k/g | `n1-s23` |
| Le e qui tombe | `n1-s22` |
| Question ou phrase ? (intonation seule) | `n1-s21` `s03` |
| Chu · t'es · i'est | `n1-s11` `s16` |
| Jean dit (la consigne en gestes) | `n1-s17` `s04` |

« Chu · t'es · i'est » est la plus originale des vingt-deux : le programme
inscrit explicitement ces formes rapides (`Associer [ʃy] à je suis`,
`[te] à tu es`, `[je] à il est`) et personne ne les enseigne, alors que c'est
ce que l'élève entend au guichet dès le premier jour.

### C · Construire une phrase — `build/phrase.py`

Tuiles de mots à ordonner, ou case à remplir depuis un banc collant. Trois à
sept mots, la longueur du niveau. **Aucun son requis.**

| Exercice | Savoir |
|---|---|
| Qui fait quoi (sujet + prédicat) | `n1-s02` `s15` `s29` |
| La bonne question (*d'où · comment · où · combien*) | `n1-s03` `s19` `s13` |
| Oui ou non — `(ne)…pas` | `n1-s05` |
| Mon, ma, ton, ta | `n1-s09` |
| Il ou elle (féminin des métiers et nationalités) | `n1-s08` `s14` |
| J'ai deux enfants (numéraux + *et*) | `n1-s10` `s20` |

### D · Écrire et copier — `build/graphie.py`

La main, pas seulement l'œil. Trois exercices sur quatre sont sans audio.

| Exercice | Savoir | État |
|---|---|---|
| Grande et petite (`A` ↔ `a`) | `n1-s32` `s30` | à écrire |
| Ma-mi-mou (syllabes graphiques) | `n1-s24` `s32` | à écrire |
| Je recopie ma fiche | `n1-s25` `s31` | à écrire |
| J'épelle mon nom | `n1-s25` `s32` | attend l'audio |

« J'épelle mon nom » se sert de `assets/outils/reconnaissance-vocale.html`, qui
existe déjà, et fabrique son exercice à partir du **pseudo de l'élève** : ce
n'est pas un nom fictif qu'il épelle, c'est le sien.

### Ce que la banque ne couvre pas, et pourquoi

Deux savoirs sur trente-deux restent dehors, volontairement : les conventions
de la communication (`n1-s01`) et la phrase emphatique (`n1-s06`). Saluer,
remercier, se reprendre — ça se travaille en situation, dans un module. Les
isoler dans un exercice les viderait.

## L'intégration, en trois couches

**Aucune n'est une refonte.** Les trois se branchent sur ce qui existe.

### 1. Côté élève — un banc toujours ouvert

`eleve.html` range les ateliers en trois tas selon un seul champ :

```js
const DOMAINES_LIBRES = /^(vocabulaire|grammaire transversale|pratique orale libre)/i;
```

Ce qui passe ce test atterrit dans « Pour vous exercer seul » — **sans date,
sans état, toujours ouvert** (voir `eleve.html`, lignes 202-203 et 378-382).
Les vingt-deux exercices prennent donc un `domaineDeVie` transversal, et
l'expression gagne `graphie`. Une ligne. L'élève qui a fini a toujours où
aller, sans que personne ait planifié quoi que ce soit.

**Défaut à corriger en même temps** : l'activité 124 porte
`domaineDeVie: "Éducation et monde du travail"`. Elle tombe donc dans les
activités thématiques et réclame une `datePrevue` par groupe — le premier
exercice de la banque n'est pas dans la banque.

### 2. Côté enseignante — le portail nomme l'exercice

La vraie question n'est jamais « quelle activité ? » mais « cet élève n'entend
pas *a* de *ou*, je lui donne quoi ? ». Chaque exercice porte son savoir dans
son fichier de contenu ; il suffit de le remonter jusqu'au diagnostic
(`assets/outils/diagnostic-modules.html`), qui sait déjà dire ce qui coince.
Le savoir devient la clé de jointure entre le diagnostic et la banque.

### 3. Pour la suite — les modèles de la forge

C'est la couche qui rend « ne jamais être en manque » vrai au-delà d'une liste
fermée. `forge.py` et `assets/outils/compositeur-activite.html` produisent déjà
une activité complète à partir des critères du programme, par le CLI Claude Code
du poste, et la publient **en atelier**. Il manque quatre *modèles* — un par
famille — pour que l'enseignante compose « un exercice de discrimination,
niveau 1, sur p et b » et l'obtienne. La forge existe ; ce sont les moules qui
manquent.

## L'ordre de production

Dicté par une contrainte, pas par une préférence : **le compte ElevenLabs est à
zéro crédit** (401 `quota_exceeded`, constaté le 24 août 2026). Tout ce qui
s'entend attend ; tout ce qui se lit peut partir tout de suite.

1. **Famille A, les cinq restants.** Généraliser `polices.py` en
   `appariement.py`. Aucun média payant.
2. **Familles C et D (sans audio), neuf exercices.** Deux générateurs neufs.
   Aucun média payant. La banque passe de six à quinze.
3. **Les trois couches.** Touche `eleve.html`, le diagnostic et le compositeur —
   trois fichiers partagés, donc à faire quand personne d'autre n'écrit
   (règle 5 de `docs/deux-agents-en-parallele.md`).
4. **Famille B + « J'épelle mon nom », au retour des crédits.** ≈ 90 extraits,
   quelques dollars.

## À trancher

- **Le nom du domaine transversal.** « Graphie et sons » couvrirait A, B et D ;
  C irait sous « Grammaire transversale », qui existe déjà. Deux domaines
  valent mieux qu'un fourre-tout.
- **Le format.** Un exercice de banque ne fait aucune séance : il se prend en
  dix minutes, seul, autant de fois qu'on veut. Il n'entre donc ni dans le
  dépôt de matériel ni dans la grille des seize séances — aucun PowerPoint ne
  l'accompagne, et c'est voulu.

Voir aussi : `CLAUDE.md`, section « Les ateliers générés ».
