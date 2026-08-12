# Migration du module existant vers les jetons

Cible : `assets/interactive/module-travail/module-travail-activite-interactive.html`
(bloc `<style>`, lignes 10-313). À faire dans cet ordre — chaque étape est vérifiable seule.

## 0 · Brancher le système

```html
<link rel="stylesheet" href="../../francisation-design/styles.css">
```

Puis retirer du `<style>` local tout ce que le système fournit déjà (reset, `font-family`,
couleurs de fond). Ne gardez en local que ce qui est propre au module.

Et, ligne 4, rétablir le zoom :
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## 1 · Couleurs codées en dur → jetons

| Valeur dans le fichier | Rôle réel | Jeton |
|---|---|---|
| `#EDF6F4` fond de page | fond | `var(--surface-page)` (#F7F7F5) |
| `#123B32` texte | encre | `var(--text-strong)` |
| `#1D6B8F` accent global | **à supprimer comme accent** | `var(--accent)` ; ne garder `--acier-600` que pour le repérage de section |
| `#154F68`, `#12556B` | texte d'appui | `var(--text-body)` |
| `#5E8A82` (3.4:1 ✘) | texte secondaire | `var(--text-muted)` #6E7175 |
| `#8A8D91` (3.0:1 ✘) | texte secondaire | `var(--text-muted)` |
| `#94A3B8` (2.4:1 ✘) | placeholder, zone vide | `var(--text-muted)` |
| `#B7DED7`, `#DCEFEB`, `#CFE9E3` | filets | `var(--border)` |
| `#F1FBF9`, `#F0FAF7`, `#F8FDFC`, `#F7FCFB` | fonds creusés | `var(--surface-sunken)` |
| `#DC2626` bouton audio | audio | `var(--audio)` — **seul aplat rouge conservé** |

## 2 · Rétroaction : 39 valeurs → 12

| Ancien | Nouveau |
|---|---|
| `.fb-ok`, `.vf-opt.fb-ok`, `.blank.fb-ok`, `.imgzone.fb-ok`, `.f-vrai`, `.tv`, `.btn-lu.done` | `background:var(--ok-bg);border-color:var(--ok-line);color:var(--ok-ink)` |
| `.fb-no`, `.vf-opt.fb-no`, `.blank.fb-no`, `.imgzone.fb-no`, `.f-faux`, `.tf`, `.err` | `background:var(--no-bg);border-color:var(--no-line);color:var(--no-ink)` |
| `.timelbl`, `#sel-banner`, `.tile.sel`, `.ta` | `background:var(--warn-bg);border-color:var(--warn-line);color:var(--warn-ink)` |
| `.vf-opt.sel`, `.zone.filled`, `.blank.filled`, `.imgzone.filled` | `background:var(--sel-bg);border-color:var(--sel-line);color:var(--sel-ink)` — **plaque encre, plus de bleu** |
| `.zone.empty`, `.blank`, `.imgzone` | `background:var(--drop-bg);border-color:var(--drop-line);color:var(--text-muted)` |

Puis supprimer l'animation `shk` sur `.fb-no` / `.blank.fb-no` / `.imgzone.fb-no`, et ajouter les
glyphes : `.fb--ok::before{content:"✓ "}` / `.fb--no::before{content:"✕ "}`.

## 3 · Les couleurs injectées en JS

C'est la cause des 23 `!important` du bloc `#sec-prep`. Aux lignes ~1225, 1247, 1284-1299,
retirer `style="background:'+ex.color+'"` et `style="border-bottom-color:'+sec.color+'"`, et poser
la couleur une seule fois sur le conteneur de section :

```js
d.className = 'sec exo exo--' + sec.famille;   // orale · phonie · ecriture · ecoute · vocab
```

Tout ce qui est à l'intérieur lit alors `--sec` / `--sec-soft`. Une fois l'injection retirée, les
`!important` peuvent tomber un par un (garder ceux de la rétroaction, qui doivent gagner sur
l'état sélectionné).

## 4 · Cibles tactiles

| Ligne | Contrôle | Actuel | Correctif |
|---|---|---|---|
| 289 | bouton icône seule | 34 × 34 | `.btn-audio-round` (44) |
| 82 | `.word-chip .btn` | ≈ 26 | 40 × 40 minimum dans un chip serré |
| 228 | `.self-opts button` | 40 | 44 |
| 26 | `.tab` | ≈ 41 | `padding:11px 18px` |
| 162 | `#fc-reveal-btn` | ≈ 37 | `padding:12px 20px` |
| 236 | `.wbtn` | ≈ 41 | `padding:12px 16px` |

## 5 · Clavier et annonces

- Chaque tuile / zone / jeton : `role="button" tabindex="0"` + `onkeydown` sur Entrée et Espace.
- `.pron-fb`, `.wfb`, `.vf-summary`, `.fb`, `#prog-chip` : `aria-live="polite"`.
- Retirer les émojis des chaînes `intro` (lignes 412-421) : le titre de section porte déjà
  l'information et un lecteur d'écran les énonce.

## 6 · Bug de contenu à corriger au passage

Ligne 1261, le bandeau de l'encadré de savoir est écrit en dur — l'encadré de grammaire de la
Défi 1 affiche « PRONONCIATION », et `ex.savoir.h` n'est jamais rendu :

```js
h += '<div class="savoir' + (ex.savoir.speak ? ' savoir--pron' : '') + '">'
   + '<div class="card__band">'
   + esc(ex.savoir.h ? ex.savoir.h.replace(/^›\s*/, '') : 'Prononciation')
   + '</div>';
```
