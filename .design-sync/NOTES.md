# Notes de synchronisation — Francisation

## Ce qu'est ce dépôt pour /design-sync

Le système de design d'origine (`assets/design-system/`) est **du CSS pur** : aucun composant
JavaScript à compiler. `/design-sync` exige un paquet React. On a donc ajouté
`assets/design-system-react/` — 26 composants qui **n'appliquent que les classes du CSS
existant**. Aucune règle CSS n'y est écrite : `build-css.mjs` aplatit `assets/design-system/
styles.css` et sa chaîne d'`@import` en `dist/francisation.css`, qui devient `_ds_bundle.css`.

**Le CSS reste la seule source de vérité.** Si on ajoute une classe dans `assets/design-system/`,
il faut ajouter le composant React correspondant à la main — rien n'est automatique.

## Environnement (ce Mac, août 2026)

- Node n'était pas installé : `brew install node` (26.7.0). npm 11 bloque les scripts
  d'installation par défaut — l'avertissement `install-scripts` sur esbuild est bénin, le binaire
  fonctionne quand même.
- Playwright + Chromium installés dans `.ds-sync/node_modules` (cache dans
  `~/Library/Caches/ms-playwright`). Supprimer `.ds-sync/` les retire.
- Le dépôt n'est pas un paquet npm : `assets/design-system-react/node_modules/francisation-design`
  est un **lien symbolique vers `..`** (auto-référence). Sans lui, ni le convertisseur ni les
  vignettes ne résolvent `import { … } from 'francisation-design'`. **À recréer sur un nouveau
  clone** : `ln -sfn .. assets/design-system-react/node_modules/francisation-design`.

## Commandes

```sh
npm --prefix assets/design-system-react install     # une fois par clone
npm --prefix assets/design-system-react run build   # CSS aplati + tsc → dist/
node .ds-sync/resync.mjs --config .design-sync/config.json \
  --node-modules assets/design-system-react/node_modules \
  --entry assets/design-system-react/dist/index.js --out ./ds-bundle \
  --remote .design-sync/.cache/remote-sync.json
```

## Décisions prises

- **Groupes** = noms des dossiers de `src/` (boutons, cartes, exercices, formulaires,
  mise-en-page, retroaction). `Retroaction` tombait dans « general » parce que son nom est celui
  de son dossier : corrigé par `docsMap` → `docs/Retroaction.md`, un talon qui ne contient que
  `category: retroaction`. Ne pas supprimer ce fichier.
- `cardMode: "column"` pour `Exercice` et `Banniere` : leurs vignettes dépassaient la largeur
  d'une cellule de grille.
- **Correction de composant pendant la vérification** : `Etape` ne montrait pas la couleur de
  section sur sa pastille (le CSS utilise `currentColor`). Ajout d'un
  `style={{background:'var(--sec, currentColor)'}}` — c'est ce que faisait déjà `preview.html`
  en ligne. Le README du système exige que la pastille porte cette couleur.

## Avertissements connus au rendu

- `[FONT_REMOTE] "Nunito"` — attendu. La police vient d'un `@import` Google Fonts dans
  `tokens/fonts.css`. Aucun fichier de police n'est livré, et c'est voulu. **Ne pas** essayer de
  le résoudre avec `extraFonts`.
- `[DOCS_UNMAPPED]` sur 25 composants — attendu : il n'y a pas de dossier de documentation par
  composant, les `.prompt.md` sont synthétisés depuis les `.d.ts` + JSDoc + vignettes.

## Risques à la resynchronisation

- **Dérive CSS silencieuse.** `dist/francisation.css` est une **copie aplatie**. Si quelqu'un
  modifie `assets/design-system/` sans relancer `npm run build`, le paquet téléversé garde
  l'ancien CSS. Toujours relancer la construction avant `resync.mjs`.
- **Nouvelles classes sans composant.** Une classe ajoutée au CSS n'apparaîtra jamais dans
  Claude Design tant qu'un composant React ne l'applique pas. C'est le coût de l'approche.
- **Le lien symbolique disparaît au clone** (voir ci-dessus).
- **Nunito dépend du réseau** au moment de la capture. Si les captures ressortent en police
  système, c'est le réseau, pas le système de design.
- Les composants purement structurels (`Page`, `Conteneur`, `Pile`, `GrilleAuto`) n'ont l'air de
  rien seuls : leurs vignettes contiennent volontairement des cartes de démonstration. Ne pas les
  « simplifier ».
