# Les banques des niveaux 2 à 8 — plan et journal

Écrit le 24 août 2026, le jour même où la banque du niveau 1 a été bâtie, et
complété le soir avec ce que la réalisation a démenti. L'état vivant se lit
avec `python3 build/banque.py --etat`, ou sur la page de chantier
(`assets/presentations/chantier-banques.html`) — jamais ici : un plan qu'on met
à jour à la main ment au premier oubli.

## Le constat de départ

Trois faits, vérifiés sur le disque avant d'écrire une ligne :

- **Les modules sont finis partout.** `build/bilan_programme.py` rendait
  « complet » pour les huit niveaux, 85 situations sur 85. Il n'y avait plus de
  cours à écrire, seulement des exercices.
- **Le niveau 1 était le seul à avoir une banque** — 21 ateliers. Les autres
  niveaux avaient exactement leur compte de modules et **zéro** atelier.
- **415 savoirs prescrits hors du niveau 1**, et rien pour les drainer sauf les
  situations.

## Ce qui a décidé du plan : le profil des savoirs bascule

| Niveau | savoirs | phonétique | phrase | lexique | texte |
|---|---|---|---|---|---|
| 1 | 32 | 4 | 19 | 8 | 1 |
| 2 | 49 | 4 | 26 | 15 | 4 |
| 3 | 59 | 4 | 36 | 15 | 4 |
| 4 | 60 | 4 | 35 | 17 | 4 |
| 5 | 78 | 2 | 37 | **34** | 5 |
| 6 | 54 | 3 | 30 | 16 | 5 |
| 7 | 57 | **1** | 25 | **26** | 5 |
| 8 | 58 | **1** | 27 | **26** | 4 |

La famille B du niveau 1 — discriminer à l'oreille, la moitié de ses savoirs —
**cesse de payer au-dessus du niveau 4** : un seul savoir phonétique aux
niveaux 7 et 8. Ce qui la remplace, c'est le lexique (× 3) et le texte (× 5).
Copier la banque du niveau 1 sept fois aurait produit sept banques mal
ajustées.

## Ce qui a été fait, dans l'ordre

### Temps 0 · Le registre commun

Les quatre générateurs du niveau 1 tenaient leur liste d'ateliers **écrite à la
main**, et le niveau 1 en dur dans leur gabarit — titre et couleur de repérage.

Un atelier se déclare maintenant lui-même, dans son `contenu.json` :

```json
"slug": "question-n1", "niveau": 1, "generateur": "phrase", "activite": 131
```

`build/banque.py` remplace `banque_n1.py` (devenu un renvoi) : le registre est
le balayage du disque, les quatre contrôles valent pour les huit niveaux, et
`--niveau N` restreint tout. La limite de tuiles de `phrase.py` suit désormais
le niveau — sept mots au débutant, douze à partir du niveau 5.

### Temps 1 · Deux formes neuves

- **`build/texte.py`** — famille E, *lire un texte*. Deux modes : `questions`
  (le texte reste à l'écran, la correction allume le passage qui portait la
  réponse) et `trous` (un texte troué de connecteurs, à remplir **dans l'ordre
  du texte**).
- **`build/conjugaison.py`** — famille F, *conjuguer*. Deux modes : `ecrire`
  (l'élève tape, la correction compare caractère par caractère) et `choisir`
  (quand l'objet est de distinguer, non de produire).
- **`build/inscrire_ateliers.py`** — la fiche de catalogue déduite du contenu :
  couleur du niveau, savoirs en mots-clés. Sur une fiche existante il ne touche
  qu'au repérage et **ajoute** les savoirs manquants sans rien retirer.

Le lexique n'a pas eu de générateur neuf : `build/vocab_flash.py` existait, et
la famille A (appariement) s'est révélée capable de porter le registre
(activité 171) et les familles de mots (181).

### Temps 2 · Le contenu, six ateliers par niveau

| Niveau | Activités | Ce qui est couvert |
|---|---|---|
| 2 | 146-151 | déterminants, questions au guichet, impératif et négation, présent des huit irréguliers, avis affiché, pronoms de reprise |
| 3 | 156-161 | imparfait et futur, prépositions de lieu, connecteurs d'un courriel, accord des adjectifs, annonce de logement, abréviations de l'annonce |
| 4 | 206-211 | ponctuation, passé composé contre imparfait, coordination, relevé de compte, mots du guichet, prépositions de temps |
| 5 | 166-171 | subjonctif, négation complexe, accord du participe, questions polies, lettre administrative, trois registres |
| 6 | 176-181 | pronoms compléments, plus-que-parfait, indéfinis, offre d'emploi, récit d'un dégât, familles de mots |
| 7 | 186-191 | connecteurs, conditionnel, passive et emphatique, relatifs, article informatif, lettre de réclamation |
| 8 | 196-201 | irréel du passé, deux pronoms, texte d'opinion, subjonctif passé, compte rendu, expressions figées |

**Six par niveau, et non dix comme annoncé.** Le chiffre a été revu à la
première vague : à six ateliers, le niveau 2 touchait déjà 27 de ses 49
savoirs. Passer à dix aurait ajouté des ateliers sur des savoirs déjà couverts
par les modules — c'est-à-dire du remplissage.

## Ce que la réalisation a démenti

**1. Le nombre d'ateliers ne prédit pas la couverture.** Six ateliers couvrent
27 savoirs au niveau 2 et 17 au niveau 4. L'écart ne vient pas de la qualité :
il vient du nombre de modules (dix contre dix-huit) qui drainent déjà les
situations. Compter les ateliers ne dit rien ; `--etat` le dit.

**2. Le niveau 5 est le moins bien couvert des huit** — 18 savoirs sur 78 —
et c'est structurel : 34 de ses savoirs sont lexicaux, un par situation de vie.
Ils appellent des `vocab-flash`, pas des ateliers de grammaire. C'est le
premier chantier à reprendre.

**3. Aucun atelier d'écoute n'a été produit.** Le compte ElevenLabs est à zéro
depuis le 24 août ; les six ateliers du niveau 1 attendent toujours leurs
262 extraits (≈ 0,76 $). Les niveaux 2 et 3 ont chacun quatre savoirs
phonétiques qui resteront dehors tant que le compte n'est pas rechargé.

**4. Un contrôle a servi pour de bon.** L'extrait de la question des heures de
`offre-emploi-n6` vivait dans le chapeau, qui n'est pas surlignable : le build
a refusé l'atelier plutôt que de le livrer avec un surlignage qui n'apparaît
jamais. C'est exactement le genre de faute qui ne lève aucune erreur.

**5. Deux contenus d'appariement se résolvaient sans rien comprendre.** Dans
`abrev-annonce-n3`, la face « au téléphone » répétait le mot cherché. Réécrites.
À vérifier systématiquement : dans un appariement, **aucune face ne doit
contenir le mot d'une autre face**.

## Ce qui reste

| | État |
|---|---|
| Les ateliers d'écoute (niveaux 1, 2, 3) | attendent le rechargement du compte ElevenLabs |
| Le lexique du niveau 5 — 34 savoirs | à traiter en `vocab-flash`, pas en grammaire |
| Les quatre modèles du compositeur | jamais faits ; ils serviraient huit niveaux au lieu d'un |
| L'audio des 42 ateliers neufs | aucun n'en a ; tous sont jouables sans |
| Les invites de `server.py` | disent « niveau 4 » en dur — défaut transversal repéré le 20 août, toujours là |

Voir aussi : `docs/plan-exercices-niveau-1.md` (la banque d'origine),
`CLAUDE.md` section « Les ateliers générés », et
`assets/presentations/chantier-banques.html` pour l'état du jour.
