# Système « Trame »

Le système de design de la maison — Trame, conception pédagogique pour la
formation en entreprise. Il part du logo dessiné le 6 septembre 2026 (le
tissage de quatre barres, le mot en Manrope) et de ce que ce logo affirme :
de la structure, pas de l'ornement.

- **`tokens.css`** — le livrable. Écru, encre, ocre (« trame »), indigo
  (« chaîne »), verdicts ; deux polices ; espacement base 4 ; trois rayons
  qui n'arrondissent pas ; une seule ombre ; le motif de fond ; le thème sombre.
- **`systeme.html`** — la documentation, écrite **avec** les jetons qu'elle
  documente. Le bandeau de tête est le logo posé sur son champ, sans une
  valeur en dur.

## Ce qu'il faut savoir

**Les jetons sont recopiés dans la page, pas importés** — un `@import` depuis
un `file://` échoue en silence. Après toute modification de `tokens.css` :

    python3 - <<'PY'
    import pathlib
    p = pathlib.Path(".")
    t = (p/"systeme.html").read_text(encoding="utf-8")
    d = t.index('<style id="jetons">')+len('<style id="jetons">')
    f = t.index("</style>", d)
    (p/"systeme.html").write_text(t[:d] + (p/"tokens.css").read_text(encoding="utf-8").strip() + t[f:], encoding="utf-8")
    PY

Puis recopier le dossier dans
`bibliotheque-francisation/assets/presentations/trame/`, d'où la page est servie.

**Les contrastes sont calculés, pas écrits.** Le nuancier lit les valeurs
réelles et affiche le rapport WCAG de chaque couleur sur son fond d'usage,
dans les deux thèmes. Les bordures sont exclues : aucun seuil ne s'applique
à une séparation.

**Le logo vit ailleurs.** Sa source est le canevas Claude Design
(https://claude.ai/code/artifact/831d3ab6-6539-40af-a741-37dbcd2d805b) et ses
fichiers de travail dans `~/Claude/assets/logo-trame/`. Le système en reprend
le SVG tel quel ; il ne le redessine pas.

## Ce qui a été décidé plutôt que relevé

Un logo donne quatre couleurs, une police et une attitude. Tout le reste —
les neutres intermédiaires, le thème sombre, la police de lecture, les
verdicts, le motif, les composants — a été décidé. Le § 6 de la page le
dit un par un.
