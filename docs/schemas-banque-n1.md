# Les schémas de contenu de la banque du niveau 1

Un générateur par famille, un fichier de contenu par atelier. Ce document est
le contrat entre les deux : **le générateur ne lit rien d'autre que ça**, et il
s'arrête avec un message clair sur un champ manquant.

Chemin, toujours : `assets/interactive/<slug>/contenu.json`.

## Ce qui vaut pour tous les contenus

Champs communs, tous obligatoires :

| Champ | Rôle |
|---|---|
| `slug` | doit être identique au nom du dossier |
| `titre` | le `h1` et le `<title>` |
| `eyebrow` | « Francisation · Niveau 1 · <situation ou savoir> » |
| `cle` | clé `localStorage`, unique — `francisation<Nom>N1MaitriseV1` |
| `consigne` | une phrase, à l'impératif, adressée à l'élève |
| `note_prof` | le panneau « Mode enseignant », en `<p>` HTML |
| `savoirs` | les identifiants du programme, ex. `["n1-s02", "n1-s15"]` |
| `items` | la liste des exercices |

Chaque item porte un `slug` unique dans son atelier et un `audio` de la forme
`audio/<slug>.mp3` — **le fichier n'existe pas encore**, et c'est normal : les
MP3 sont produits plus tard par `generer_audio_banque_n1.py`. Le bouton
d'écoute reste en place et sans effet en attendant ; on ne masque jamais un
bouton pour cacher un média manquant.

## Les règles de contenu du niveau 1

Elles ne sont pas négociables — c'est le niveau qui les impose.

1. **Trois à sept mots par phrase.** Au-delà, ce n'est plus le niveau 1.
2. **Le vocabulaire est celui des quatre modules du niveau**, et rien d'autre :
   nom, prénom, adresse, pays, langue, métier, enfant, appartement, code
   postal, téléphone, courriel, date de naissance, fiche, case, inscription,
   livre, stylo, chaise, sac, porte, horloge, heure, midi, semaine, horaire,
   panneau, dessin, toilettes, cafétéria, flèche, accueil, entrée, sortie,
   vestiaire, service de garde, bonjour, merci, pardon, épeler, habiter,
   remplir, écouter, regarder, ouvrir, fermer.
3. **Rien ne se copie du manuel SOFAD.** Personnages, situations et phrases
   s'inventent. Le manuel est un modèle de progression, jamais une source.
4. **Les leurres sont des confusions réelles, jamais du hasard.** *nom* et
   *non*, *prénom* et *pronom*, *mon* et *ma*, *il est* et *elle est*. Un
   leurre tiré au sort rend l'exercice trivial et n'apprend rien.
5. **Le décor est québécois et nommé** — un centre de francisation, un
   guichet, une clinique de quartier. Jamais « une ville moderne ».

## Famille C — `build/phrase.py`

Deux modes, un par atelier. Le mode est déclaré à la racine : `"mode": "ordre"`
ou `"mode": "choix"`.

### `mode: "ordre"` — remettre les mots dans l'ordre

```json
{
  "slug": "je-suis-mecanicien",
  "mots": ["Je", "suis", "mécanicien"],
  "phrase": "Je suis mécanicien.",
  "sens": "Je dis mon métier.",
  "audio": "audio/je-suis-mecanicien.mp3"
}
```

- `mots` est la phrase **dans le bon ordre**, un mot par tuile, sans ponctuation.
  Le générateur mélange lui-même.
- `phrase` porte la majuscule et le point ; elle sert de correction.
- `sens` dit en une phrase courte ce que l'énoncé fait — pas une traduction,
  une intention (« Je dis mon métier », « Je réponds non »).
- **Trois à six tuiles.** Sept est déjà trop long à manipuler pour ce niveau.

### `mode: "choix"` — remplir le trou

```json
{
  "slug": "mon-nom",
  "avant": "",
  "apres": " nom, c'est Yusuf.",
  "choix": ["Mon", "Ma", "Ton"],
  "ok": "Mon",
  "phrase": "Mon nom, c'est Yusuf.",
  "sens": "« nom » est masculin : mon.",
  "audio": "audio/mon-nom.mp3"
}
```

- `avant` + le trou + `apres` doivent redonner `phrase` une fois `ok` posé.
  Le générateur le vérifie et s'arrête si ça ne colle pas.
- `choix` compte **deux à quatre** entrées, dont `ok`. Les autres sont des
  confusions réelles.
- `sens` explique **pourquoi**, en mots du niveau 1.

## Famille B — `build/oreille.py`

### `mode: "choisir"` — j'écoute, je choisis

```json
{
  "slug": "riz-roue",
  "audio": "audio/riz.mp3",
  "dit": "riz",
  "choix": ["riz", "roue"],
  "ok": "riz",
  "indice": "Les lèvres sont étirées."
}
```

- `dit` est le texte **exactement** tel qu'il sera synthétisé. C'est lui qui
  part chez ElevenLabs ; `ok` est ce que l'élève clique.
- `choix` : deux ou trois, jamais plus — on discrimine, on ne cherche pas.
- Les choix peuvent être des **pictogrammes** au lieu de mots : mettre
  `"choix_type": "picto"` à la racine et des noms de la bibliothèque de
  `build/appariement.py` dans `choix`.
- `indice` est une aide articulatoire courte, montrée après une erreur.

### `mode: "barrer"` — le e qu'on n'entend pas

```json
{
  "slug": "je-mappelle",
  "audio": "audio/je-mappelle.mp3",
  "phrase": "J[e] m'appell[e] Carolin[e].",
  "dit": "Je m'appelle Caroline.",
  "sens": "Trois e écrits, aucun entendu. Celui d'« appelle » s'entend."
}
```

- Dans `phrase`, **`[e]` marque un e écrit qu'on n'entend pas**. Tous les
  autres `e` sont prononcés et ne doivent pas être cliqués.
- `dit` est le texte envoyé à la synthèse, sans crochets.

**Une correction, parce que cet exemple était faux.** Il portait
`m'app[e]ll[e]` et disait « quatre e écrits, aucun entendu ». C'est inexact :
le e du milieu d'« appelle » **se prononce**, et le programme le transcrit
lui-même — *J(e) m'appelle* y vaut **[ʒ mapɛl]**. Ce n'est pas la consonne qui
précède qui décide dans ce cas, c'est celle qui **suit** : un e devant consonne
double se dit [ɛ], jamais schwa. La règle utile tient donc en deux temps :

1. un `e` **final** de mot tombe presque toujours (`port[e]`, `fich[e]`) ;
2. un `e` **intérieur** tombe s'il suit une seule consonne prononcée
   (`sam[e]di`, `s[e]maine`), **sauf** devant consonne double, où il se dit
   [ɛ] (*appelle*, *toilettes*, *belle*).

L'erreur a été trouvée par l'agent qui écrivait `e-muet-n1` : il a suivi le
programme contre ce document, et il a eu raison. Un exemple faux dans un
contrat de format enseigne une prononciation qui n'existe pas.

## Ce qu'un agent de contenu ne fait pas

- Il **ne lance aucun build** et ne touche à aucun fichier hors de son
  `contenu.json`.
- Il ne fait **ni `git add`, ni commit** : trois autres sessions travaillent
  dans ce dépôt et l'index est partagé.
- Il n'invente pas de champ : un champ de plus est un champ que le générateur
  ignore en silence.
