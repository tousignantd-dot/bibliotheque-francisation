# Système « BoucleDidactique »

Le système de design de la maison — BoucleDidactique, conception pédagogique
pour la formation en entreprise. Nom décidé le 1er octobre 2026 (il remplace
Trame, abandonné avec son système).

- **`tokens.css`** — le livrable : neutres froids, le bleu (marque), le
  graphite (action), deux verdicts, deux polices, espacement base 4, rayons,
  durées et courbes du mouvement.
- **`systeme.html`** — la documentation, écrite **avec** les jetons qu'elle
  documente ; elle recalcule les contrastes en direct et montre le mouvement.

## D'où il vient

Trois tours le 1er octobre 2026. Deux séries de pistes adaptées ont été
refusées (« trop français », puis « cherche encore »). Un mur de dix-huit
sites réels a tranché : Daniel aime Ramp, Brex, Quizlet, Figure 03 et surtout
**Agence Foudre** ; pour le mouvement, **GSAP** et **Lusion**. Une maquette aux
couleurs d'Agence Foudre a été jugée **trop vive** ; parmi quatre palettes
adoucies, il a retenu **graphite et bleu**. La maquette vit dans
`bibliotheque-francisation/assets/presentations/identite/boucledidactique-maquette.html`.

## Les règles

1. **Fond blanc, neutres froids.** Jamais de crème ni de papier chaud.
2. **Le bleu ne porte pas de petit texte.** `--bleu` (3,19:1) est aux
   formes, aux anneaux et aux titres de 24 px et plus. Le texte bleu prend
   `--bleu-texte`.
3. **Le graphite agit.** Les boutons principaux sont en graphite, texte
   blanc ou `--pale`. Un seul bouton plein par bloc.
4. **Des aplats, pas de dégradés ni d'ombres portées** (sauf ce qui flotte).
5. **Grande typographie.** Clash Grotesk très gras et serré pour les titres ;
   General Sans pour tout le reste, à 17 px au moins.
6. **Le mouvement sert la lecture** : un titre qui entre, un bloc qui monte
   au défilement, la boucle qui se trace, un chiffre qui compte. Jamais
   d'animation qui boucle sous un texte qu'on lit (sauf le bandeau défilant,
   qui ne porte que des mots-clés). Les anneaux 3D vivent dans l'accueil, nulle
   part ailleurs.
7. **`prefers-reduced-motion` coupe tout** : la page reste complète, immobile.
8. **Icônes : Tabler** (`bibliotheque-francisation/build/icone.py`), jamais
   dessinées.

## Polices et bibliothèques, en local

- `fonts/` — Clash Grotesk 500/600/700 et General Sans 400/500/600 en `.woff2`
  (licence ITF, voir `fonts/LICENCE.md`). `polices.css` porte les `@font-face` ;
  comme les jetons, on le **recopie** dans la page en ajustant le chemin.
- `vendor/` — GSAP 3.13 (gsap, ScrollTrigger, SplitText) et three.js r149
  (voir `vendor/LICENCES.md`).
- Pourquoi : une page ne doit rien demander au réseau. Et l'API Fontshare
  renvoyait parfois Satoshi à la place de General Sans dans une requête
  combinée — la maquette affichait alors la police système sans rien dire.

## Ce qui reste à faire

- Le **logo** est dessiné (`logo/`) ; un passage sur canevas pourra en affiner
  les proportions, sans en changer l'idée.
- Le **vrai site** : la maquette n'en est que la direction.

## Comme les autres systèmes

Les jetons sont **recopiés** dans la page, jamais importés. Après toute
modification de `tokens.css`, recopier le bloc dans `systeme.html`
(`<style id="jetons">`), puis recopier le dossier vers
`bibliotheque-francisation/assets/presentations/boucledidactique/`, d'où il est servi.
