#!/usr/bin/env python3
"""Flash vocabulaire par thème : deux activités, un seul gabarit.

`vocab-flash-sante` et `vocab-flash-conso` ne différaient que par sept lignes
— le titre, le thème, la liste de mots, la clé de stockage. Les deux fichiers
ont donc divergé au premier correctif appliqué à un seul. On les génère
maintenant depuis ce script, à partir du gabarit ci-dessous et de la liste de
mots posée dans `assets/interactive/<slug>/mots.json`.

  python3 build/vocab_flash.py             → réécrit les deux activités
  python3 build/vocab_flash.py --verifier   → dit qui est à jour, n'écrit rien

N'ÉDITEZ PAS LE HTML PRODUIT : le prochain passage l'écraserait. Le contenu
pédagogique (mots, définitions, exemples, expressions) vit dans mots.json ;
tout le reste vit ici.
"""
import io
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTER = ROOT / 'assets/interactive'

# Le thème sert au repérage et au titre. La clé de stockage garde la
# progression de l'élève séparée d'un thème à l'autre : deux thèmes, deux
# barres de maîtrise.
THEMES = [
    {'slug': 'vocab-flash-sante', 'theme': 'Santé et clinique', 'niveau': 4,
     'cle': 'francisationFlashSanteMasteryV1'},
    {'slug': 'vocab-flash-conso', 'theme': 'Consommation',      'niveau': 4,
     'cle': 'francisationFlashConsoMasteryV1'},
]

# Le haut-parleur du système de design (assets/interactive/module-travail/
# icons/speaker.svg), recopié tel quel — on ne le redessine pas.
SPEAKER = ('<svg viewBox="0 0 50 50" fill="currentColor" aria-hidden="true">'
           '<path d="M27 6.5c0-1.2-1.4-1.9-2.4-1.1L13.8 14H6c-1.1 0-2 .9-2 2v18c0 1.1.9 2 2 2h7.8l10.8 8.6c1 .8 2.4.1 2.4-1.1V6.5z"/>'
           '<path d="M33.4 17.6c-.7-.6-1.8-.5-2.4.2-.6.7-.5 1.8.2 2.4 1.6 1.4 2.6 3.4 2.6 5.7s-1 4.3-2.6 5.7c-.7.6-.8 1.7-.2 2.4.6.7 1.7.8 2.4.2 2.3-2 3.7-5 3.7-8.3s-1.4-6.3-3.7-8.3z"/>'
           '<path d="M38.5 11.2c-.7-.5-1.8-.4-2.3.4-.5.7-.4 1.8.4 2.3 3.6 2.6 5.9 6.9 5.9 11.6s-2.3 9-5.9 11.6c-.8.5-.9 1.6-.4 2.3.5.8 1.6.9 2.3.4C43 36.7 46 31.1 46 25s-3-11.7-7.5-13.8z"/>'
           '</svg>')

GABARIT = r'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Flash vocabulaire — @@THEME@@</title>
<link rel="stylesheet" href="/assets/design-system/styles.css">
<style>
/* ══════════════════════════════════════════════════════════════════════
   Flash vocabulaire · surcouche du système de design
   FICHIER GÉNÉRÉ — build/vocab_flash.py. Ne modifiez pas ce HTML.
   Ce qui suit ne couvre que les objets propres à l'activité : la planche
   image-mot, les quatre onglets, la table de maîtrise. Aucune couleur en
   dur : uniquement des jetons de assets/design-system/tokens/.
   ══════════════════════════════════════════════════════════════════════ */
body { --sec: var(--green-600); --sec-soft: var(--green-100); }

/* ── Bandeau clair (jamais foncé, jamais coloré en aplat) ───────────── */
.vf-band { padding: var(--sp-5) 0; }
.vf-band__in { max-width: var(--content-max); margin: 0 auto; padding: 0 var(--gutter);
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--sp-4); }
.vf-band__t { font-size: var(--fs-h2); font-weight: var(--fw-black);
  letter-spacing: var(--ls-title); line-height: var(--lh-title); margin-top: var(--sp-2); }
.vf-band__a { display: flex; flex-wrap: wrap; gap: var(--sp-2); }

/* ── Barre de parcours : les quatre étapes de l'activité ────────────── */
.vf-steps__in { max-width: var(--content-max); margin: 0 auto;
  padding: var(--sp-3) var(--gutter); display: flex; flex-wrap: wrap; gap: var(--sp-2); align-items: center; }
.step { font-family: var(--font-sans); cursor: pointer; }
.step[aria-selected="true"] { background: var(--sel-bg); border-color: var(--sel-line); color: var(--sel-ink); }

.vf-wrap { max-width: var(--content-max); margin: 0 auto; padding: var(--sp-8) var(--gutter) var(--sp-12); }
.view { display: none; }
.view.is-on { display: block; }

/* ── Onglet « Découvrir » ───────────────────────────────────────────── */
.vf-layout { display: grid; grid-template-columns: 260px minmax(0, 1fr); gap: var(--sp-5); align-items: start; }
.vf-mots { display: flex; flex-direction: column; gap: var(--sp-2); }
.vf-mot-btn { display: flex; align-items: center; gap: var(--sp-3); width: 100%; text-align: left;
  min-height: var(--tap-min); padding: var(--sp-2) var(--sp-4);
  border: 1px solid var(--border); border-radius: var(--r-md); background: var(--surface-card);
  color: var(--text-strong); font-family: var(--font-sans); font-size: var(--fs-body-sm);
  font-weight: var(--fw-semi); line-height: 1.35; cursor: pointer;
  transition: background var(--dur) var(--ease), border-color var(--dur) var(--ease), color var(--dur) var(--ease); }
.vf-mot-btn:hover { background: var(--paper-100); }
.vf-mot-btn[aria-current="true"] { background: var(--sel-bg); border-color: var(--sel-line); color: var(--sel-ink); }
/* Le mot déjà vu porte un glyphe, jamais la seule couleur. */
.vf-mot-btn__e { flex-shrink: 0; width: 16px; font-weight: var(--fw-black); }

.vf-piste { display: flex; align-items: center; gap: var(--sp-4);
  padding: var(--sp-3) var(--sp-6); border-bottom: 1px solid var(--border); }
.vf-track { flex: 1; height: 6px; border-radius: 3px; background: var(--paper-200); overflow: hidden; }
.vf-track span { display: block; height: 100%; background: var(--accent); transition: width var(--dur) var(--ease); }
.vf-piste__n { font-size: var(--fs-ui-sm); font-weight: var(--fw-bold); color: var(--text-muted); white-space: nowrap; }

/* L'image passe en bandeau, sur toute la largeur de la carte, au lieu d'une
   colonne étroite de 38 %. Les photos du recueil vont du carré (900x900) au
   panoramique (1200x542) : dans une colonne, `contain` les réduisait à la
   largeur disponible et il ne restait qu'une vignette. En pleine largeur,
   la même règle `contain` les affiche entières et deux fois plus grandes,
   sans jamais les déformer ni les rogner. La fiche descend sous l'image et
   garde une colonne de texte lisible. */
.vf-planche { display: grid; grid-template-columns: 1fr; }
.vf-image { background: var(--surface-sunken); border-bottom: 1px solid var(--border);
  display: flex; flex-direction: column; }
.vf-image__l { padding: var(--sp-3) var(--sp-5); font-size: var(--fs-label); font-weight: var(--fw-black);
  letter-spacing: var(--ls-label); text-transform: uppercase; color: var(--sec);
  border-bottom: 1px solid var(--border); }
.vf-image img { width: 100%; height: clamp(320px, 54vh, 560px); object-fit: contain;
  display: block; padding: var(--sp-4); }

.vf-fiche { padding: var(--sp-6); display: flex; flex-direction: column; gap: var(--sp-4);
  width: 100%; max-width: 820px; margin: 0 auto; }
.vf-terme { font-size: clamp(32px, 4vw, 44px); font-weight: var(--fw-black);
  letter-spacing: var(--ls-title); line-height: 1.05; }
.vf-gram { font-size: var(--fs-body-sm); font-weight: var(--fw-bold); color: var(--text-muted); }
.vf-bloc { border-top: 1px solid var(--border); padding-top: var(--sp-4); }
.vf-lbl { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); margin-bottom: var(--sp-2); }
.vf-def { font-size: var(--fs-lead); font-weight: var(--fw-semi); line-height: var(--lh-loose); }
/* L'exemple garde son filet gauche de 4 px — le seul usage décoratif
   autorisé de la couleur de section. */
.vf-ex { font-size: var(--fs-body); font-weight: var(--fw-medium); font-style: italic;
  line-height: var(--lh-loose); color: var(--text-body);
  border-left: 4px solid var(--sec); padding-left: var(--sp-4); }
.vf-chips { display: flex; flex-wrap: wrap; gap: var(--sp-2); }
.vf-tag { padding: 6px var(--sp-3); border-radius: var(--r-pill);
  background: var(--surface-sunken); border: 1px solid var(--border);
  font-size: var(--fs-ui-sm); font-weight: var(--fw-semi); color: var(--text-body); }

/* Trois boutons dans une colonne étroite : ils se replient plutôt que de
   déborder, et leur libellé peut passer à la ligne. Un seul est en aplat
   rouge — celui du mot. Trois pavés rouges dans une carte feraient de la
   couleur d'alerte un décor ; les deux autres portent la même icône, en
   couleur de texte, comme le prévoit le système. */
.vf-audios { display: grid; grid-template-columns: repeat(auto-fit, minmax(132px, 1fr));
  gap: var(--sp-2); margin-top: auto; padding-top: var(--sp-4); }
.vf-audios .btn { min-width: 0; padding: 0 var(--sp-3); white-space: normal; line-height: 1.2; }
.vf-nav { display: flex; justify-content: space-between; gap: var(--sp-3); }

/* Masquage pédagogique. Le flou est remplacé par une plaque nommée : elle
   se dit aux lecteurs d'écran, et le texte masqué ne reste pas sélectionnable
   sous un simple filtre. */
.vf-masque { position: relative; }
.vf-masque > * { visibility: hidden; }
.vf-masque::after { content: "Masqué — cliquez pour afficher"; visibility: visible;
  position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
  border: 1px dashed var(--drop-line); border-radius: var(--r-sm); background: var(--drop-bg);
  font-size: var(--fs-ui-sm); font-weight: var(--fw-bold); color: var(--text-muted);
  cursor: pointer; text-align: center; padding: var(--sp-2); }
.vf-masque.is-shown > * { visibility: visible; }
.vf-masque.is-shown::after { display: none; }

.vf-prof { display: none; flex-wrap: wrap; gap: var(--sp-4); align-items: center;
  padding: var(--sp-4) var(--sp-6); background: var(--surface-sunken); border-top: 1px solid var(--border); }
.vf-prof.is-on { display: flex; }
.vf-prof label { display: flex; align-items: center; gap: var(--sp-2);
  font-size: var(--fs-ui-sm); font-weight: var(--fw-bold); cursor: pointer; }
.vf-prof input { width: 20px; height: 20px; accent-color: var(--accent); }
.vf-prof__k { margin-left: auto; font-size: var(--fs-ui-sm); font-weight: var(--fw-medium); color: var(--text-muted); }

/* ── Onglets de jeu ─────────────────────────────────────────────────── */
.vf-jeu__t { display: flex; flex-wrap: wrap; align-items: flex-start; justify-content: space-between;
  gap: var(--sp-4); border-bottom: 1px solid var(--border); padding-bottom: var(--sp-5); margin-bottom: var(--sp-6); }
.vf-jeu__t h2 { margin: var(--sp-1) 0 var(--sp-1); }
.vf-jeu__t p { font-size: var(--fs-body-sm); font-weight: var(--fw-medium); color: var(--text-muted); }
.vf-question { max-width: 860px; margin: 0 auto var(--sp-6); text-align: center;
  font-size: var(--fs-lead); font-weight: var(--fw-semi); line-height: var(--lh-loose); }
.vf-question img { width: 100%; height: clamp(300px, 48vh, 500px); object-fit: contain;
  border-radius: var(--r-sm); background: var(--surface-sunken); display: block; margin: 0 auto var(--sp-4); }
.vf-question__c { font-size: var(--fs-body-sm); font-weight: var(--fw-medium); color: var(--text-muted); margin-top: var(--sp-2); }
.vf-trou { font-weight: var(--fw-black); letter-spacing: .06em; }

.vf-reponses { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: var(--sp-3); max-width: 760px; margin: 0 auto; }
.vf-rep { min-height: var(--tap-comfort); padding: var(--sp-3) var(--sp-4); text-align: left;
  border: 1px solid var(--border); border-radius: var(--r-md); background: var(--surface-card);
  color: var(--text-strong); font-family: var(--font-sans); font-size: var(--fs-body-sm);
  font-weight: var(--fw-semi); cursor: pointer;
  transition: background var(--dur) var(--ease), border-color var(--dur) var(--ease), color var(--dur) var(--ease); }
.vf-rep:hover:enabled { background: var(--paper-100); }
.vf-rep.is-ok { background: var(--ok-bg); border-color: var(--ok-line); color: var(--ok-ink); }
.vf-rep.is-ok::before { content: "✓ "; font-weight: var(--fw-black); }
.vf-rep.is-no { background: var(--no-bg); border-color: var(--no-line); color: var(--no-ink); }
.vf-rep.is-no::before { content: "✕ "; font-weight: var(--fw-black); }
/* Bonne réponse non choisie : filet pointillé, sans aplat — la forme du
   filet, et pas la seule couleur, dit où était le mot juste. */
.vf-rep.is-answer { background: var(--surface-card); border: 1px dashed var(--ok-line); color: var(--ok-line); }
.vf-rep:disabled { cursor: default; }

.vf-retour { min-height: 26px; text-align: center; margin: var(--sp-5) 0; }
.vf-jeu__a { display: flex; justify-content: center; flex-wrap: wrap; gap: var(--sp-3); }

/* ── Aide-mémoire des mots ──────────────────────────────────────────
   Le même appui que dans Cartes mémoire, transposé : ici la question est
   déjà à choix, la liste ne désigne donc rien — elle rappelle seulement
   les mots du thème pendant qu'on répond. Des pastilles, pas des
   boutons : on ne clique pas dedans. */
.vf-aide-mots { max-width: 560px; margin: var(--sp-5) auto 0; }
.vf-aide-mots__t { font-size: var(--fs-meta); font-weight: var(--fw-black);
  letter-spacing: .06em; text-transform: uppercase; color: var(--text-muted);
  text-align: center; margin-bottom: var(--sp-2); }
.vf-aide-mots__l { display: flex; flex-wrap: wrap; justify-content: center; gap: var(--sp-2); }
.vf-aide-mots__m { padding: 6px var(--sp-4); border-radius: var(--r-pill);
  border: 1px solid var(--border); background: var(--surface-sunken);
  font-size: var(--fs-ui-sm); font-weight: var(--fw-semi); color: var(--text-body); }

/* ── Onglet « Maîtrise » ────────────────────────────────────────────── */
.vf-bilan { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--sp-3); margin-bottom: var(--sp-6); }
.vf-tuile { background: var(--surface-sunken); border: 1px solid var(--border);
  border-radius: var(--r-sm); padding: var(--sp-4); text-align: center; }
.vf-tuile strong { display: block; font-size: var(--fs-h3); font-weight: var(--fw-black); }
.vf-tuile span { font-size: var(--fs-meta); font-weight: var(--fw-bold);
  letter-spacing: .06em; text-transform: uppercase; color: var(--text-muted); }

.vf-jalons { display: flex; flex-wrap: wrap; gap: var(--sp-2); margin-bottom: var(--sp-6); }
.vf-jalon { padding: var(--sp-2) var(--sp-4); border-radius: var(--r-pill);
  border: 1px solid var(--border); background: var(--surface-card);
  font-size: var(--fs-ui-sm); font-weight: var(--fw-bold); color: var(--text-muted); }
.vf-jalon.is-ok { background: var(--ok-bg); border-color: var(--ok-line); color: var(--ok-ink); }
.vf-jalon.is-ok::before { content: "✓ "; font-weight: var(--fw-black); }

.vf-table { display: flex; flex-direction: column; }
.vf-ligne { display: grid; grid-template-columns: minmax(160px, 1fr) minmax(0, 2fr) auto;
  gap: var(--sp-5); align-items: center; padding: var(--sp-4) 0; border-bottom: 1px solid var(--paper-200); }
.vf-ligne:last-child { border-bottom: none; }
.vf-ligne__m { font-size: var(--fs-body-sm); font-weight: var(--fw-black); }
/* La barre ne dit rien seule : l'état s'écrit à côté, en toutes lettres. */
.vf-ligne__e { font-size: var(--fs-ui-sm); font-weight: var(--fw-bold); color: var(--text-muted); white-space: nowrap; }
.vf-ligne__e.is-ok { color: var(--ok-ink); }

/* ── Modale des raccourcis ──────────────────────────────────────────── */
.vf-modale { display: none; position: fixed; inset: 0; z-index: 100;
  background: rgba(23, 24, 26, .55); align-items: center; justify-content: center; padding: var(--sp-5); }
.vf-modale.is-on { display: flex; }
.vf-modale__c { width: min(620px, 100%); background: var(--surface-card);
  border-radius: var(--r-lg); box-shadow: var(--sh-modal); padding: var(--sp-6); position: relative;
  max-height: 86vh; overflow-y: auto; }
.vf-modale__x { position: absolute; right: var(--sp-4); top: var(--sp-4); }
.vf-touches { display: grid; grid-template-columns: 130px minmax(0, 1fr);
  gap: var(--sp-3) var(--sp-4); align-items: center; margin-top: var(--sp-5); }
.vf-touches kbd { display: block; text-align: center; padding: var(--sp-2) var(--sp-3);
  border: 1px solid var(--border); border-radius: var(--r-sm); background: var(--surface-sunken);
  font-family: var(--font-sans); font-size: var(--fs-ui-sm); font-weight: var(--fw-black); color: var(--text-strong); }
.vf-touches b { font-size: var(--fs-ui-sm); font-weight: var(--fw-semi); color: var(--text-body); }

.vf-aide { position: fixed; right: var(--sp-5); bottom: var(--sp-5); z-index: 90;
  width: var(--tap-min); height: var(--tap-min); border-radius: 50%;
  border: 1px solid var(--border); background: var(--surface-card); color: var(--text-strong);
  font-family: var(--font-sans); font-size: 19px; font-weight: var(--fw-black);
  cursor: pointer; box-shadow: var(--sh-raise); }

/* ── Mode présentation (projection en classe) ───────────────────────── */
.is-presentation .vf-band, .is-presentation .vf-steps, .is-presentation .vf-cote,
.is-presentation .vf-prof, .is-presentation .vf-piste, .is-presentation .vf-aide { display: none !important; }
.is-presentation .vf-wrap { padding: 0; max-width: none; }
.is-presentation .vf-layout { grid-template-columns: 1fr; gap: 0; }
.is-presentation .vf-image img { height: 52vh; }
.is-presentation .card { border: none; border-radius: 0; box-shadow: none; }
.is-presentation .vf-planche { min-height: 100vh; }
.is-presentation .vf-terme { font-size: clamp(48px, 6vw, 84px); }
.is-presentation .vf-def { font-size: 28px; }
.is-presentation .vf-ex { font-size: 24px; }
/* En bas à gauche : en haut à droite, le bouton passait par-dessus le mot
   projeté, qui est le seul objet de cet écran. */
.vf-sortie { display: none; position: fixed; bottom: var(--sp-5); left: var(--sp-5); z-index: 99; }
.is-presentation .vf-sortie { display: inline-flex; }

@media (max-width: 1040px) {
  /* En colonne, la liste des mots passe SOUS la carte : sinon l'élève
     déroule onze boutons avant d'atteindre le mot qu'il vient d'ouvrir. */
  .vf-layout { grid-template-columns: 1fr; }
  .vf-layout > .card { order: 1; }
  .vf-cote { order: 2; }
  .vf-mots { display: grid; grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 640px) {
  .vf-band__in, .vf-steps__in, .vf-wrap { padding-left: var(--sp-5); padding-right: var(--sp-5); }
  .vf-mots { grid-template-columns: 1fr; }
  .vf-audios, .vf-reponses, .vf-bilan { grid-template-columns: 1fr; }
  .vf-bilan { grid-template-columns: repeat(2, 1fr); }
  .vf-ligne { grid-template-columns: 1fr; gap: var(--sp-2); }
  .vf-fiche { padding: var(--sp-5); }
  .vf-image img { height: clamp(220px, 34vh, 320px); padding: var(--sp-3); }
  .vf-question img { height: clamp(200px, 32vh, 300px); }
}
</style>
</head>
<body class="page">

<header class="band vf-band">
  <div class="vf-band__in">
    <div>
      <p class="band__eyebrow">Francisation · Niveau @@NIVEAU@@ · @@THEME@@</p>
      <h1 class="vf-band__t">Flash vocabulaire</h1>
    </div>
    <div class="vf-band__a">
      <button type="button" class="btn btn--ghost btn--sm" id="profToggle" aria-pressed="false">Mode enseignant</button>
      <button type="button" class="btn btn--ghost btn--sm" id="presToggle" aria-pressed="false">Présentation</button>
      <button type="button" class="btn btn--ghost btn--sm" id="resetVus">Réinitialiser</button>
    </div>
  </div>
</header>

<nav class="steps vf-steps" aria-label="Étapes de l'activité">
  <div class="steps__inner vf-steps__in" role="tablist">
    <button type="button" class="step" role="tab" aria-selected="true"  data-vue="vueDecouvrir"><span class="step__dot"></span>Je découvre les mots</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vuePratiquer"><span class="step__dot"></span>Je m'entraîne</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueReviser"><span class="step__dot"></span>Défi de 10 questions</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueMaitrise"><span class="step__dot"></span>Où j'en suis</button>
  </div>
</nav>

<button type="button" class="btn btn--pri btn--sm vf-sortie" id="sortiePres">Quitter la présentation</button>

<main class="vf-wrap" id="app">

  <!-- ── Je découvre les mots ─────────────────────────────────────── -->
  <section class="view is-on" id="vueDecouvrir">
    <div class="vf-layout">
      <aside class="vf-cote">
        <p class="vf-lbl">Les mots du thème <span id="vus"></span></p>
        <div class="vf-mots" id="listeMots"></div>
      </aside>

      <div class="card card--flush">
        <div class="vf-piste">
          <div class="vf-track"><span id="barreVus"></span></div>
          <div class="vf-piste__n" id="compteVus"></div>
        </div>

        <div class="vf-planche">
          <div class="vf-image">
            <div class="vf-image__l">@@THEME@@</div>
            <img id="photo" alt="">
          </div>
          <div class="vf-fiche">
            <div>
              <div class="vf-terme" id="terme"></div>
              <div class="vf-gram" id="grammaire"></div>
            </div>

            <div class="vf-bloc">
              <p class="vf-lbl">Définition</p>
              <p class="vf-def" id="definition"></p>
            </div>

            <div class="vf-bloc">
              <p class="vf-lbl">Exemple</p>
              <p class="vf-ex" id="exemple"></p>
            </div>

            <div class="vf-bloc">
              <p class="vf-lbl">Expressions utiles</p>
              <div class="vf-chips" id="expressions"></div>
            </div>

            <div class="vf-audios">
              <button type="button" class="btn btn--audio" data-audio="mot">@@SPEAKER@@Le mot</button>
              <button type="button" class="btn btn--ghost" data-audio="definition">@@SPEAKER@@La définition</button>
              <button type="button" class="btn btn--ghost" data-audio="exemple">@@SPEAKER@@L'exemple</button>
            </div>

            <div class="vf-nav">
              <button type="button" class="btn btn--ghost" id="precedent">Précédent</button>
              <button type="button" class="btn btn--pri" id="suivant">Suivant</button>
            </div>
          </div>
        </div>

        <div class="vf-prof" id="panneauProf">
          <label><input type="checkbox" data-cache="terme"> Masquer le mot</label>
          <label><input type="checkbox" data-cache="definition"> Masquer la définition</label>
          <label><input type="checkbox" data-cache="exemple"> Masquer l'exemple</label>
          <label><input type="checkbox" data-cache="expressions"> Masquer les expressions</label>
          <span class="vf-prof__k">Clavier : flèches · 1 le mot · 2 la définition · 3 l'exemple</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Je m'entraîne ────────────────────────────────────────────── -->
  <section class="view" id="vuePratiquer">
    <div class="card">
      <div class="vf-jeu__t">
        <div>
          <p class="exo__eyebrow">Entraînement</p>
          <h2>Je m'entraîne</h2>
          <p>Choisissez le bon mot. Chaque bonne réponse fait monter votre maîtrise.</p>
        </div>
        <span class="score"><span id="pointsPratique">0</span>&nbsp;points</span>
      </div>
      <div class="vf-question" id="questionPratique"></div>
      <div class="vf-reponses" id="reponsesPratique"></div>
      <p class="vf-retour" id="retourPratique" aria-live="polite"></p>
      <div class="vf-jeu__a">
        <button type="button" class="btn btn--audio" id="ecouterPratique">@@SPEAKER@@Écouter</button>
        <button type="button" class="btn btn--ghost" id="motsBtnPratique"
                aria-expanded="false" aria-controls="motsBoxPratique">Voir les mots</button>
        <button type="button" class="btn btn--pri" id="suivantPratique">Question suivante</button>
      </div>
      <div class="vf-aide-mots" id="motsBoxPratique" hidden>
        <p class="vf-aide-mots__t">Les mots du thème</p>
        <div class="vf-aide-mots__l" id="motsLPratique"></div>
      </div>
    </div>
  </section>

  <!-- ── Défi de 10 questions ─────────────────────────────────────── -->
  <section class="view" id="vueReviser">
    <div class="card">
      <div class="vf-jeu__t">
        <div>
          <p class="exo__eyebrow">Défi</p>
          <h2>Dix questions</h2>
          <p>Une série de dix questions pour vérifier ce qui est acquis.</p>
        </div>
        <span class="score"><span id="scoreDefi">0</span>&nbsp;/ 10</span>
      </div>
      <div class="vf-track" style="margin-bottom:var(--sp-6)"><span id="barreDefi"></span></div>
      <div class="vf-question" id="questionDefi"></div>
      <div class="vf-reponses" id="reponsesDefi"></div>
      <p class="vf-retour" id="retourDefi" aria-live="polite"></p>
      <div class="vf-jeu__a">
        <button type="button" class="btn btn--ghost" id="motsBtnDefi"
                aria-expanded="false" aria-controls="motsBoxDefi">Voir les mots</button>
        <button type="button" class="btn btn--pri" id="lancerDefi">Commencer le défi</button>
      </div>
      <div class="vf-aide-mots" id="motsBoxDefi" hidden>
        <p class="vf-aide-mots__t">Les mots du thème</p>
        <div class="vf-aide-mots__l" id="motsLDefi"></div>
      </div>
    </div>
  </section>

  <!-- ── Où j'en suis ─────────────────────────────────────────────── -->
  <section class="view" id="vueMaitrise">
    <div class="card">
      <div class="vf-jeu__t">
        <div>
          <p class="exo__eyebrow">Progression</p>
          <h2>Où j'en suis</h2>
          <p>Chaque mot avance selon vos bonnes réponses.</p>
        </div>
        <span class="score" id="niveau">Niveau 1</span>
      </div>

      <div class="vf-bilan">
        <div class="vf-tuile"><strong id="totalPoints">0</strong><span>points</span></div>
        <div class="vf-tuile"><strong id="nbMaitrises">0</strong><span>mots maîtrisés</span></div>
        <div class="vf-tuile"><strong id="moyenne">0 %</strong><span>maîtrise moyenne</span></div>
        <div class="vf-tuile"><strong id="serie">0</strong><span>série actuelle</span></div>
      </div>

      <div class="vf-jalons" id="jalons"></div>
      <div class="vf-table" id="tableMaitrise"></div>
      <div class="vf-jeu__a" style="margin-top:var(--sp-6)">
        <button type="button" class="btn btn--ghost" id="resetMaitrise">Réinitialiser ma progression</button>
      </div>
    </div>
  </section>
</main>

<button type="button" class="vf-aide" id="boutonAide" aria-label="Afficher les raccourcis clavier">?</button>

<div class="vf-modale" id="modaleAide" role="dialog" aria-modal="true" aria-labelledby="titreAide" aria-hidden="true">
  <div class="vf-modale__c">
    <button type="button" class="btn btn--ghost btn--sm vf-modale__x" id="fermerAide">Fermer</button>
    <h2 id="titreAide">Raccourcis clavier</h2>
    <div class="vf-touches">
      <kbd>← / →</kbd><b>Mot précédent ou suivant</b>
      <kbd>1</kbd><b>Écouter le mot</b>
      <kbd>2</kbd><b>Écouter la définition</b>
      <kbd>3</kbd><b>Écouter l'exemple</b>
      <kbd>Espace</kbd><b>Rejouer le dernier son</b>
      <kbd>P</kbd><b>Entrer ou quitter la présentation</b>
      <kbd>Échap</kbd><b>Quitter la présentation</b>
      <kbd>F</kbd><b>Plein écran</b>
      <kbd>E</kbd><b>Mode enseignant</b>
    </div>
  </div>
</div>

<script>
const items = @@ITEMS@@;

const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
let index = 0, vus = new Set(), sonCourant = null, boutonCourant = null, dernierSon = null;
const caches = { terme: false, definition: false, exemple: false, expressions: false };

function jouer(src, bouton){
  if (sonCourant) { sonCourant.pause(); sonCourant.currentTime = 0; }
  if (boutonCourant) boutonCourant.removeAttribute('aria-busy');
  sonCourant = new Audio(src); boutonCourant = bouton; dernierSon = { src, bouton };
  bouton.setAttribute('aria-busy', 'true');
  const fini = () => bouton.removeAttribute('aria-busy');
  sonCourant.onended = fini; sonCourant.onerror = fini;
  sonCourant.play().catch(fini);
}

function rendreListe(){
  const liste = $('#listeMots'); liste.innerHTML = '';
  items.forEach((item, i) => {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'vf-mot-btn';
    if (i === index) b.setAttribute('aria-current', 'true');
    // Le glyphe dit « vu », la couleur ne le dit jamais toute seule.
    b.innerHTML = '<span class="vf-mot-btn__e" aria-hidden="true">' + (vus.has(i) ? '✓' : '·') + '</span>'
      + '<span>' + esc(item.term) + '</span>';
    b.onclick = () => { index = i; rendre(); };
    liste.appendChild(b);
  });
}

/* Masquage pédagogique : le bloc est couvert d'une plaque nommée, que
   l'élève ou l'enseignante découvre d'un clic. */
function appliquerCaches(){
  const carte = { terme: ['#terme', '#grammaire'], definition: ['#definition'],
                  exemple: ['#exemple'], expressions: ['#expressions'] };
  Object.entries(carte).forEach(([cle, sels]) => sels.forEach(sel => {
    const el = $(sel);
    el.classList.toggle('vf-masque', caches[cle]);
    el.classList.remove('is-shown');
    el.onclick = () => { if (caches[cle]) el.classList.toggle('is-shown'); };
  }));
}

function rendre(){
  const x = items[index];
  $('#photo').src = x.image; $('#photo').alt = x.term;
  $('#terme').textContent = x.term;
  $('#grammaire').textContent = x.grammar;
  $('#definition').textContent = x.definition;
  $('#exemple').textContent = x.example;
  $('#expressions').innerHTML = x.expressions.map(e => '<span class="vf-tag">' + esc(e) + '</span>').join('');
  vus.add(index);
  $('#barreVus').style.width = (vus.size / items.length * 100) + '%';
  $('#compteVus').textContent = vus.size + ' / ' + items.length + ' mots vus';
  $('#vus').textContent = '(' + vus.size + ' / ' + items.length + ')';
  $('#precedent').disabled = index === 0;
  $('#suivant').textContent = index === items.length - 1 ? 'Recommencer' : 'Suivant';
  rendreListe(); appliquerCaches();
}

$$('.vf-audios .btn').forEach(b => b.onclick = () => jouer(items[index].audio[b.dataset.audio], b));
$('#precedent').onclick = () => { index = Math.max(0, index - 1); rendre(); };
$('#suivant').onclick = () => { index = index === items.length - 1 ? 0 : index + 1; rendre(); };

$('#profToggle').onclick = () => {
  const on = $('#panneauProf').classList.toggle('is-on');
  $('#profToggle').setAttribute('aria-pressed', String(on));
};
function presentation(actif){
  document.body.classList.toggle('is-presentation', actif);
  $('#presToggle').setAttribute('aria-pressed', String(actif));
}
$('#presToggle').onclick = () => presentation(!document.body.classList.contains('is-presentation'));
$('#sortiePres').onclick = () => presentation(false);
$('#resetVus').onclick = () => { vus.clear(); rendre(); };

$$('#panneauProf input[type="checkbox"]').forEach(cb => cb.onchange = () => {
  caches[cb.dataset.cache] = cb.checked; appliquerCaches();
});

/* ── Raccourcis et aide ─────────────────────────────────────────────── */
function aide(force){
  const m = $('#modaleAide');
  const on = typeof force === 'boolean' ? force : !m.classList.contains('is-on');
  m.classList.toggle('is-on', on);
  m.setAttribute('aria-hidden', String(!on));
}
$('#boutonAide').onclick = () => aide();
$('#fermerAide').onclick = () => aide(false);
$('#modaleAide').onclick = e => { if (e.target === $('#modaleAide')) aide(false); };

async function pleinEcran(){
  try {
    if (!document.fullscreenElement) await document.documentElement.requestFullscreen();
    else await document.exitFullscreen();
  } catch (err) { console.warn('Plein écran non disponible', err); }
}

document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    if ($('#modaleAide').classList.contains('is-on')) aide(false);
    if (document.body.classList.contains('is-presentation')) presentation(false);
    return;
  }
  if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
  if (e.key === 'ArrowRight') { index = index === items.length - 1 ? 0 : index + 1; rendre(); }
  else if (e.key === 'ArrowLeft') { index = Math.max(0, index - 1); rendre(); }
  else if (e.key === '1') $$('.vf-audios .btn')[0].click();
  else if (e.key === '2') $$('.vf-audios .btn')[1].click();
  else if (e.key === '3') $$('.vf-audios .btn')[2].click();
  else if (e.code === 'Space' && dernierSon) { e.preventDefault(); jouer(dernierSon.src, dernierSon.bouton); }
  else if (e.key.toLowerCase() === 'p') presentation(!document.body.classList.contains('is-presentation'));
  else if (e.key.toLowerCase() === 'f') pleinEcran();
  else if (e.key.toLowerCase() === 'e') $('#profToggle').click();
  else if (e.key === '?') aide();
});

/* ── Maîtrise ───────────────────────────────────────────────────────── */
const CLE = '@@CLE@@';
let maitrise = JSON.parse(localStorage.getItem(CLE) || 'null')
  || { xp: 0, serie: 0, meilleure: 0, mots: Array(items.length).fill(0) };
function sauver(){ localStorage.setItem(CLE, JSON.stringify(maitrise)); }
function melanger(a){ return [...a].sort(() => Math.random() - .5); }
function esc(s){ return (s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

function ajouter(i, montant){
  maitrise.mots[i] = Math.max(0, Math.min(100, maitrise.mots[i] + montant));
  maitrise.xp += Math.max(0, montant);
  if (montant > 0) { maitrise.serie++; maitrise.meilleure = Math.max(maitrise.meilleure, maitrise.serie); }
  else maitrise.serie = 0;
  sauver(); rendreMaitrise();
}

// L'état s'écrit en toutes lettres à côté de la barre : la longueur seule
// ne dit rien à qui ne la voit pas.
function etatDe(v){
  if (v >= 100) return { t: 'Maîtrisé', ok: true };
  if (v >= 70)  return { t: 'Presque acquis', ok: false };
  if (v >= 35)  return { t: 'En cours', ok: false };
  if (v > 0)    return { t: 'À travailler', ok: false };
  return { t: 'Pas encore vu', ok: false };
}

function rendreMaitrise(){
  const moy = Math.round(maitrise.mots.reduce((a, b) => a + b, 0) / items.length);
  const acquis = maitrise.mots.filter(v => v >= 100).length;
  const niveau = Math.floor(maitrise.xp / 100) + 1;
  $('#totalPoints').textContent = maitrise.xp;
  $('#nbMaitrises').textContent = acquis;
  $('#moyenne').textContent = moy + ' %';
  $('#serie').textContent = maitrise.serie;
  $('#niveau').textContent = 'Niveau ' + niveau;

  const jalons = [
    { t: 'Premiers pas', ok: maitrise.xp >= 20 },
    { t: 'Série de 5', ok: maitrise.meilleure >= 5 },
    { t: 'Trois mots maîtrisés', ok: acquis >= 3 },
    { t: 'Thème maîtrisé', ok: acquis === items.length }
  ];
  $('#jalons').innerHTML = jalons.map(j =>
    '<span class="vf-jalon' + (j.ok ? ' is-ok' : '') + '">' + j.t + '</span>').join('');

  $('#tableMaitrise').innerHTML = items.map((item, i) => {
    const v = maitrise.mots[i], e = etatDe(v);
    return '<div class="vf-ligne">'
      + '<div class="vf-ligne__m">' + esc(item.term) + '</div>'
      + '<div class="vf-track"><span style="width:' + v + '%"></span></div>'
      + '<div class="vf-ligne__e' + (e.ok ? ' is-ok' : '') + '">' + e.t + ' · ' + v + ' %</div>'
      + '</div>';
  }).join('');
}

/* ── Onglets ────────────────────────────────────────────────────────── */
$$('.step').forEach(b => b.onclick = () => {
  $$('.step').forEach(x => x.setAttribute('aria-selected', String(x === b)));
  $$('.view').forEach(v => v.classList.toggle('is-on', v.id === b.dataset.vue));
  if (b.dataset.vue === 'vueMaitrise') rendreMaitrise();
});

/* Après une erreur, l'élève doit voir OÙ était le bon mot, pas seulement
   le lire dans la ligne de rétroaction. */
function marquerBonne(zone, terme){
  $$(zone + ' .vf-rep').forEach(x => { if (x.textContent === terme) x.classList.add('is-answer'); });
}

/* ── Aide-mémoire des mots ──────────────────────────────────────────
   Un même appui posé sous les deux jeux. Les mots sont rangés par ordre
   alphabétique : l'ordre de la liste ne doit rien dire de la question.
   L'état suit l'élève d'un onglet et d'un thème à l'autre — celui qui a
   besoin de la liste en a besoin partout. */
const CLE_MOTS = 'francisationFlashAideMots';
let motsOuverts = localStorage.getItem(CLE_MOTS) === '1';

function brancherAideMots(suffixe){
  const btn = $('#motsBtn' + suffixe), box = $('#motsBox' + suffixe), zone = $('#motsL' + suffixe);
  [...new Set(items.map(x => x.term))]
    .sort((a, b) => a.localeCompare(b, 'fr'))
    .forEach(term => {
      const m = document.createElement('span');
      m.className = 'vf-aide-mots__m';
      m.textContent = term;
      zone.appendChild(m);
    });
  btn.onclick = () => {
    motsOuverts = !motsOuverts;
    localStorage.setItem(CLE_MOTS, motsOuverts ? '1' : '0');
    majAideMots();
  };
  return { btn, box };
}

const aidesMots = ['Pratique', 'Defi'].map(brancherAideMots);

function majAideMots(){
  aidesMots.forEach(({ btn, box }) => {
    btn.setAttribute('aria-expanded', motsOuverts ? 'true' : 'false');
    btn.textContent = motsOuverts ? 'Cacher les mots' : 'Voir les mots';
    box.hidden = !motsOuverts;
  });
}
majAideMots();

/* ── Je m'entraîne ──────────────────────────────────────────────────── */
let ciblePratique = null, repondu = false;
function batirPratique(){
  repondu = false;
  const retour = $('#retourPratique');
  retour.textContent = ''; retour.className = 'vf-retour';
  ciblePratique = items[Math.floor(Math.random() * items.length)];
  const iCible = items.indexOf(ciblePratique);
  const type = ['image', 'definition', 'audio'][Math.floor(Math.random() * 3)];
  let enonce = '';
  if (type === 'image') {
    enonce = '<img src="' + ciblePratique.image + '" alt="">'
      + '<div>Quel mot correspond à cette image ?</div>';
  } else if (type === 'definition') {
    enonce = '<div>' + esc(ciblePratique.definition) + '</div>'
      + '<p class="vf-question__c">Quel est le mot ?</p>';
  } else {
    enonce = '<p class="vf-question__c">Écoutez, puis choisissez le mot entendu.</p>';
  }
  $('#questionPratique').innerHTML = enonce;

  const choix = melanger([ciblePratique, ...melanger(items.filter(x => x !== ciblePratique)).slice(0, 3)]);
  const zone = $('#reponsesPratique');
  zone.innerHTML = '';
  choix.forEach(opt => {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'vf-rep'; b.textContent = opt.term;
    b.onclick = () => {
      if (repondu) return;
      repondu = true;
      $$('#reponsesPratique .vf-rep').forEach(x => x.disabled = true);
      if (opt === ciblePratique) {
        b.classList.add('is-ok');
        retour.className = 'vf-retour fb fb--ok';
        retour.textContent = 'Juste. 10 points.';
        ajouter(iCible, 10);
        jouer(ciblePratique.audio.mot, $('#ecouterPratique'));
      } else {
        b.classList.add('is-no');
        marquerBonne('#reponsesPratique', ciblePratique.term);
        retour.className = 'vf-retour fb fb--no';
        retour.textContent = 'La bonne réponse est : ' + ciblePratique.term;
        ajouter(iCible, -3);
      }
      $('#pointsPratique').textContent = maitrise.xp;
    };
    zone.appendChild(b);
  });
  if (type === 'audio') setTimeout(() => jouer(ciblePratique.audio.mot, $('#ecouterPratique')), 250);
}
$('#ecouterPratique').onclick = () => ciblePratique && jouer(ciblePratique.audio.mot, $('#ecouterPratique'));
$('#suivantPratique').onclick = batirPratique;

/* ── Défi de 10 questions ───────────────────────────────────────────── */
let qDefi = 0, bonnesDefi = 0, cibleDefi = null;
function lancerDefi(){
  qDefi = 0; bonnesDefi = 0;
  $('#scoreDefi').textContent = '0';
  $('#lancerDefi').textContent = 'Recommencer';
  batirDefi();
}
function batirDefi(){
  const retour = $('#retourDefi');
  if (qDefi >= 10) {
    lmsTrack('exercise_completed', { score: bonnesDefi, total: 10 });
    $('#questionDefi').innerHTML = '<h3>Résultat : ' + bonnesDefi + ' / 10</h3>';
    $('#reponsesDefi').innerHTML = '';
    retour.className = 'vf-retour fb ' + (bonnesDefi >= 8 ? 'fb--ok' : bonnesDefi >= 5 ? 'fb--ok' : 'fb--warn');
    retour.textContent = bonnesDefi >= 8 ? 'Ces mots sont acquis.'
      : bonnesDefi >= 5 ? 'Bon travail. Continuez à vous entraîner.'
      : 'Retournez à « Je m\'entraîne » avant de refaire le défi.';
    $('#barreDefi').style.width = '100%';
    return;
  }
  retour.textContent = ''; retour.className = 'vf-retour';
  cibleDefi = items[Math.floor(Math.random() * items.length)];
  const iCible = items.indexOf(cibleDefi);
  const type = Math.floor(Math.random() * 3);
  let enonce = '';
  if (type === 0) {
    enonce = '<img src="' + cibleDefi.image + '" alt="">'
      + '<p class="vf-question__c">Choisissez le bon mot.</p>';
  } else if (type === 1) {
    enonce = '<div>' + esc(cibleDefi.definition) + '</div>'
      + '<p class="vf-question__c">Choisissez le bon mot.</p>';
  } else {
    const nu = cibleDefi.term.replace(/^(un|une|le|la|les)\s+/i, '');
    enonce = '<div>' + esc(cibleDefi.example).replace(new RegExp(nu, 'i'),
      '<span class="vf-trou">__________</span>') + '</div>'
      + '<p class="vf-question__c">Choisissez le mot qui manque.</p>';
  }
  $('#questionDefi').innerHTML = enonce;
  $('#barreDefi').style.width = (qDefi / 10 * 100) + '%';

  const choix = melanger([cibleDefi, ...melanger(items.filter(x => x !== cibleDefi)).slice(0, 3)]);
  const zone = $('#reponsesDefi');
  zone.innerHTML = '';
  choix.forEach(opt => {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'vf-rep'; b.textContent = opt.term;
    b.onclick = () => {
      $$('#reponsesDefi .vf-rep').forEach(x => x.disabled = true);
      if (opt === cibleDefi) {
        bonnesDefi++;
        b.classList.add('is-ok');
        retour.className = 'vf-retour fb fb--ok';
        retour.textContent = 'Juste.';
        ajouter(iCible, 15);
      } else {
        b.classList.add('is-no');
        marquerBonne('#reponsesDefi', cibleDefi.term);
        retour.className = 'vf-retour fb fb--no';
        retour.textContent = 'La bonne réponse est : ' + cibleDefi.term;
        ajouter(iCible, -5);
      }
      qDefi++;
      $('#scoreDefi').textContent = bonnesDefi;
      setTimeout(batirDefi, 850);
    };
    zone.appendChild(b);
  });
}
$('#lancerDefi').onclick = lancerDefi;
$('#resetMaitrise').onclick = () => {
  if (confirm('Réinitialiser toute la progression ?')) {
    maitrise = { xp: 0, serie: 0, meilleure: 0, mots: Array(items.length).fill(0) };
    sauver(); rendreMaitrise(); $('#pointsPratique').textContent = '0';
  }
};

function lmsTrack(event, data) {
  try { window.parent.postMessage(Object.assign({ lms: true, event: event }, data || {}), '*'); } catch (e) {}
  try {
    const up = new URLSearchParams(window.parent.location.search);
    const code = up.get('code'), actId = parseInt(up.get('activityId')) || null, title = up.get('title') || '';
    if (code && actId) {
      fetch('/api/student/progress', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(Object.assign({ code, activityId: actId, activityTitle: title, event }, data || {})),
      }).catch(() => {});
    }
  } catch (e2) {}
}

batirPratique();
rendreMaitrise();
rendre();
lmsTrack('file_opened');
</script>
</body>
</html>
'''


def rendre(theme):
    dossier = INTER / theme['slug']
    mots = json.loads(io.open(dossier / 'mots.json', encoding='utf-8').read())
    return (GABARIT
            .replace('@@THEME@@', theme['theme'])
            .replace('@@NIVEAU@@', str(theme['niveau']))
            .replace('@@CLE@@', theme['cle'])
            .replace('@@SPEAKER@@', SPEAKER)
            .replace('@@ITEMS@@', json.dumps(mots, ensure_ascii=False)))


def main(argv):
    verifier = '--verifier' in argv
    for theme in THEMES:
        cible = INTER / theme['slug'] / f"{theme['slug']}-activite-interactive.html"
        neuf = rendre(theme)
        actuel = io.open(cible, encoding='utf-8').read() if cible.exists() else ''
        if actuel == neuf:
            print(f"  = {theme['slug']} : à jour")
        elif verifier:
            print(f"  ≠ {theme['slug']} : à regénérer")
        else:
            io.open(cible, 'w', encoding='utf-8').write(neuf)
            print(f"  → {theme['slug']} : écrit ({len(neuf):,} octets)".replace(',', ' '))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
