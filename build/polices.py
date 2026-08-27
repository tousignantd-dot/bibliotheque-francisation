#!/usr/bin/env python3
"""« Même mot, autre police » — atelier de niveau 1, généré.

Le programme du niveau 1 demande, en toutes lettres, de « comprendre des mots
écrits en caractères d'imprimerie différents » (savoir n1-s32, Éléments de
graphie). Aucun des quatre modules du niveau ne peut le drainer : chacun est
happé par sa situation, et tous affichent leurs mots dans la même Nunito. Un
élève qui reconnaît `Toilettes` dans son cahier ne reconnaît pas `TOILETTES`
sur la porte — or c'est la porte qu'il doit lire.

L'atelier montre donc le **même mot** dans six écritures, chacune nommée par
l'endroit où l'élève la rencontre pour vrai : mon cahier, un livre, le
panneau, le formulaire, la main, les lettres détachées. C'est ce nom de lieu
qui fait la leçon — sans lui, ce ne serait qu'une vitrine de polices.

    python3 build/polices.py             → réécrit l'activité
    python3 build/polices.py --verifier  → dit si elle est à jour, n'écrit rien

N'ÉDITEZ PAS LE HTML PRODUIT : le prochain passage l'écraserait. Les mots
vivent dans `assets/interactive/polices-n1/mots.json` ; tout le reste vit ici.

Les cinq polices d'emprunt
--------------------------
Le système de design n'a qu'une police, Nunito, et il n'en aura pas d'autre :
`assets/design-system/tokens/fonts.css` reste intouché. Les cinq familles
supplémentaires sont importées **par cette activité seule**, depuis Google
Fonts — la même source que Nunito, déjà autorisée dans le projet. Chaque
famille porte une pile de repli système, parce qu'une classe hors ligne verra
les replis : l'exercice reste juste, les six écritures restent distinctes,
elles sont seulement moins typées. C'est un écart accepté, pas un défaut à
corriger en embarquant cinq fichiers de police dans le dépôt.
"""
import io
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOSSIER = ROOT / 'assets/interactive/polices-n1'
CIBLE = DOSSIER / 'polices-n1-activite-interactive.html'
CLE = 'francisationPolicesN1MaitriseV1'

# Le haut-parleur du système de design, recopié tel quel — on ne le redessine
# pas (même source que build/vocab_flash.py).
SPEAKER = ('<svg viewBox="0 0 50 50" fill="currentColor" aria-hidden="true">'
           '<path d="M27 6.5c0-1.2-1.4-1.9-2.4-1.1L13.8 14H6c-1.1 0-2 .9-2 2v18c0 1.1.9 2 2 2h7.8l10.8 8.6c1 .8 2.4.1 2.4-1.1V6.5z"/>'
           '<path d="M33.4 17.6c-.7-.6-1.8-.5-2.4.2-.6.7-.5 1.8.2 2.4 1.6 1.4 2.6 3.4 2.6 5.7s-1 4.3-2.6 5.7c-.7.6-.8 1.7-.2 2.4.6.7 1.7.8 2.4.2 2.3-2 3.7-5 3.7-8.3s-1.4-6.3-3.7-8.3z"/>'
           '<path d="M38.5 11.2c-.7-.5-1.8-.4-2.3.4-.5.7-.4 1.8.4 2.3 3.6 2.6 5.9 6.9 5.9 11.6s-2.3 9-5.9 11.6c-.8.5-.9 1.6-.4 2.3.5.8 1.6.9 2.3.4C43 36.7 46 31.1 46 25s-3-11.7-7.5-13.8z"/>'
           '</svg>')

# Les six écritures. `lieu` est la moitié pédagogique de l'affaire : l'élève
# n'apprend pas « une police condensée », il apprend « c'est écrit comme ça
# sur le panneau ». `casse` dit comment le mot se présente à cet endroit-là —
# un formulaire crie en majuscules, un cahier reste en minuscules.
VARIANTES = [
    {'cle': 'cahier',     'lieu': 'dans mon cahier',      'casse': 'min'},
    {'cle': 'livre',      'lieu': 'dans un livre',        'casse': 'min'},
    {'cle': 'panneau',    'lieu': 'sur le panneau',       'casse': 'maj'},
    {'cle': 'formulaire', 'lieu': 'sur le formulaire',    'casse': 'maj'},
    {'cle': 'main',       'lieu': 'écrit à la main',      'casse': 'cap'},
    {'cle': 'detachees',  'lieu': 'en lettres détachées', 'casse': 'min'},
]

GABARIT = r'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Même mot, autre police — Niveau 1</title>
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" type="image/svg+xml" href="/assets/design-system/marque-francis-favicon.svg">
<style>
/* Les cinq polices d'emprunt. @import en tête du bloc, comme la spécification
   l'exige. Nunito est déjà chargée par le système de design. */
@import url("https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=Courier+Prime:wght@400;700&family=Libre+Baskerville:wght@400;700&family=Oswald:wght@500&family=Patrick+Hand&display=swap");

/* ══════════════════════════════════════════════════════════════════════
   Même mot, autre police · surcouche du système de design
   FICHIER GÉNÉRÉ — build/polices.py. Ne modifiez pas ce HTML.
   Aucune couleur en dur hors des six écritures : uniquement des jetons de
   assets/design-system/tokens/. La couleur de repérage est celle du
   niveau 1 — framboise --niv-1-line / --niv-1-bg.
   ══════════════════════════════════════════════════════════════════════ */
body { --sec: var(--niv-1-line); --sec-soft: var(--niv-1-bg); }

/* ── Bandeau clair (jamais foncé, jamais coloré en aplat) ───────────── */
.pl-band { padding: var(--sp-5) 0; }
.pl-band__in { max-width: var(--content-max); margin: 0 auto; padding: 0 var(--gutter);
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--sp-4); }
.pl-band__t { font-size: var(--fs-h2); font-weight: var(--fw-black);
  letter-spacing: var(--ls-title); line-height: var(--lh-title); margin-top: var(--sp-2); }
.pl-band__a { display: flex; flex-wrap: wrap; gap: var(--sp-2); }

.pl-steps__in { max-width: var(--content-max); margin: 0 auto;
  padding: var(--sp-3) var(--gutter); display: flex; flex-wrap: wrap; gap: var(--sp-2); align-items: center; }
.step { font-family: var(--font-sans); cursor: pointer; }
.step[aria-selected="true"] { background: var(--sel-bg); border-color: var(--sel-line); color: var(--sel-ink); }

.pl-wrap { max-width: var(--content-max); margin: 0 auto; padding: var(--sp-8) var(--gutter) var(--sp-12); }
.view { display: none; }
.view.is-on { display: block; }

/* ── Colonne des mots ───────────────────────────────────────────────── */
.pl-layout { display: grid; grid-template-columns: 260px minmax(0, 1fr); gap: var(--sp-5); align-items: start; }
.pl-mots { display: flex; flex-direction: column; gap: var(--sp-2); }
.pl-mot-btn { display: flex; align-items: center; gap: var(--sp-3); width: 100%; text-align: left;
  min-height: var(--tap-min); padding: var(--sp-2) var(--sp-4);
  border: 1px solid var(--border); border-radius: var(--r-md); background: var(--surface-card);
  color: var(--text-strong); font-family: var(--font-sans); font-size: var(--fs-body-sm);
  font-weight: var(--fw-semi); line-height: 1.35; cursor: pointer;
  transition: background var(--dur) var(--ease), border-color var(--dur) var(--ease), color var(--dur) var(--ease); }
.pl-mot-btn:hover { background: var(--paper-100); }
.pl-mot-btn[aria-current="true"] { background: var(--sel-bg); border-color: var(--sel-line); color: var(--sel-ink); }
/* Le mot déjà vu porte un glyphe, jamais la seule couleur. */
.pl-mot-btn__e { flex-shrink: 0; width: 16px; font-weight: var(--fw-black); }
.pl-lbl { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); margin-bottom: var(--sp-3); }

.pl-piste { display: flex; align-items: center; gap: var(--sp-4);
  padding: var(--sp-3) var(--sp-6); border-bottom: 1px solid var(--border); }
.pl-track { flex: 1; height: 6px; border-radius: 3px; background: var(--paper-200); overflow: hidden; }
.pl-track span { display: block; height: 100%; background: var(--accent); transition: width var(--dur) var(--ease); }
.pl-piste__n { font-size: var(--fs-ui-sm); font-weight: var(--fw-bold); color: var(--text-muted); white-space: nowrap; }

/* ── L'en-tête du mot : le terme tel que le module l'enseigne ────────── */
.pl-tete { padding: var(--sp-6) var(--sp-6) var(--sp-4); display: flex; flex-wrap: wrap;
  align-items: center; justify-content: space-between; gap: var(--sp-4); }
.pl-terme { font-size: clamp(28px, 3.4vw, 40px); font-weight: var(--fw-black);
  letter-spacing: var(--ls-title); line-height: 1.05; }
.pl-lieu { font-size: var(--fs-body-sm); font-weight: var(--fw-semi); color: var(--text-muted);
  margin-top: var(--sp-2); }

/* ── Les six écritures ──────────────────────────────────────────────── */
.pl-planche { display: grid; grid-template-columns: repeat(auto-fit, minmax(198px, 1fr));
  gap: 1px; background: var(--border); border-top: 1px solid var(--border); }
.pl-v { background: var(--surface-card); padding: var(--sp-4) var(--sp-5) var(--sp-6);
  display: flex; flex-direction: column; gap: var(--sp-3); min-height: 148px; }
.pl-v__l { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--sec); }
/* `display:block` pour que `ajuster()` puisse mesurer un débordement, et
   `overflow-wrap: normal` pour qu'un mot ne se coupe JAMAIS en deux : c'est
   `ajuster()` qui règle le corps, pas le navigateur qui casse le mot. */
.pl-v__m { display: block; font-size: clamp(26px, 3vw, 36px); line-height: 1.15;
  color: var(--text-strong); overflow-wrap: normal; }
/* Les mots longs — « date de naissance », « code postal » — passeraient sous
   la ligne du bas en Oswald ou en Caveat. On les descend d'un cran plutôt
   que de les tronquer : un mot coupé n'est plus le même mot. */
.pl-v__m.is-long { font-size: clamp(20px, 2.2vw, 27px); }

.pl-v--cahier .pl-v__m { font-family: var(--font-sans); font-weight: var(--fw-bold); }
.pl-v--livre .pl-v__m { font-family: "Libre Baskerville", Georgia, "Times New Roman", serif; font-weight: 400; }
.pl-v--panneau .pl-v__m { font-family: "Oswald", "Arial Narrow", "Helvetica Neue", sans-serif;
  font-weight: 500; letter-spacing: .06em; }
.pl-v--formulaire .pl-v__m { font-family: "Courier Prime", ui-monospace, "Courier New", monospace;
  font-weight: 700; letter-spacing: .04em; }
/* Caveat a une petite hauteur d'x : à taille égale elle paraît deux fois plus
   petite que les autres. Le facteur la remet au même niveau apparent. */
.pl-v--main .pl-v__m { font-family: "Caveat", "Segoe Script", "Bradley Hand", cursive;
  font-weight: 600; font-size: clamp(36px, 4.2vw, 50px); }
.pl-v--main .pl-v__m.is-long { font-size: clamp(28px, 3.1vw, 38px); }
.pl-v--detachees .pl-v__m { font-family: "Patrick Hand", "Comic Sans MS", "Segoe Print", cursive;
  font-weight: 400; }

.pl-pied { padding: var(--sp-4) var(--sp-6); border-top: 1px solid var(--border);
  display: flex; flex-wrap: wrap; gap: var(--sp-3); align-items: center; justify-content: space-between; }
.pl-nav { display: flex; gap: var(--sp-2); }

/* ── Je trouve le même mot ──────────────────────────────────────────── */
.pl-consigne { padding: var(--sp-6); text-align: center; border-bottom: 1px solid var(--border); }
.pl-consigne__c { font-size: var(--fs-body); font-weight: var(--fw-semi); color: var(--text-muted);
  margin-bottom: var(--sp-4); }
.pl-cible { display: inline-block; padding: var(--sp-4) var(--sp-6); border: 2px solid var(--sec);
  border-radius: var(--r-md); background: var(--sec-soft); color: var(--text-strong);
  font-size: clamp(30px, 3.6vw, 44px); line-height: 1.15; overflow-wrap: normal; }
.pl-cible.is-long { font-size: clamp(22px, 2.6vw, 32px); }
.pl-cible__ou { display: block; margin-top: var(--sp-2); font-family: var(--font-sans);
  font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--sec); }

.pl-reponses { padding: var(--sp-6); display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: var(--sp-3); }
.pl-rep { min-height: 84px; padding: var(--sp-3) var(--sp-4);
  border: 1px solid var(--border); border-radius: var(--r-md); background: var(--surface-card);
  color: var(--text-strong); font-size: clamp(22px, 2.4vw, 30px); line-height: 1.2; cursor: pointer;
  overflow-wrap: normal;
  transition: background var(--dur) var(--ease), border-color var(--dur) var(--ease); }
.pl-rep:hover:not(:disabled) { background: var(--paper-100); border-color: var(--sec); }
.pl-rep:disabled { cursor: default; }
.pl-rep.is-ok { border-color: var(--ok-line); background: var(--ok-bg); }
.pl-rep.is-no { border-color: var(--no-line); background: var(--no-bg); }
.pl-rep__e { display: block; font-family: var(--font-sans); font-size: var(--fs-label);
  font-weight: var(--fw-black); letter-spacing: var(--ls-label); text-transform: uppercase;
  color: var(--text-muted); margin-top: var(--sp-2); }
.pl-retour { padding: 0 var(--sp-6) var(--sp-6); min-height: 28px; }
.pl-barre { padding: var(--sp-3) var(--sp-6); border-bottom: 1px solid var(--border);
  display: flex; align-items: center; gap: var(--sp-4);
  font-size: var(--fs-ui-sm); font-weight: var(--fw-bold); color: var(--text-muted); }

/* ── Où j'en suis ───────────────────────────────────────────────────── */
.pl-bilan { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: var(--sp-4);
  margin-bottom: var(--sp-6); }
.pl-chiffre { font-size: clamp(30px, 3.4vw, 42px); font-weight: var(--fw-black); line-height: 1; }
.pl-table { width: 100%; border-collapse: collapse; font-size: var(--fs-body-sm); }
.pl-table th, .pl-table td { padding: var(--sp-3) var(--sp-4); border-bottom: 1px solid var(--border);
  text-align: left; }
.pl-table th { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); }
.pl-etat { font-weight: var(--fw-bold); white-space: nowrap; }

/* ── Mode présentation : le tableau de la classe ────────────────────── */
.pl-sortie { display: none; position: fixed; top: var(--sp-4); right: var(--sp-4); z-index: 50; }
.is-presentation .pl-band, .is-presentation .pl-steps, .is-presentation .pl-cote { display: none; }
.is-presentation .pl-sortie { display: inline-flex; }
.is-presentation .pl-layout { grid-template-columns: 1fr; }
.is-presentation .pl-v__m { font-size: clamp(34px, 4.4vw, 58px); }
.is-presentation .pl-v--main .pl-v__m { font-size: clamp(46px, 6vw, 76px); }

@media (max-width: 900px) {
  .pl-layout { grid-template-columns: 1fr; }
  .pl-band__in, .pl-steps__in, .pl-wrap { padding-left: var(--sp-5); padding-right: var(--sp-5); }
  .pl-bilan { grid-template-columns: 1fr 1fr; }
}
</style>
</head>
<body class="page">

<div class="fr-barre">
  <div class="fr-barre__in">
    <span class="fr-lockup">
      <span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span>
      <span class="fr-trait" aria-hidden="true"></span>
      <span class="fr-desc">Aide à l'apprentissage du français</span>
    </span>
  </div>
</div>

<header class="band pl-band">
  <div class="pl-band__in">
    <div>
      <p class="band__eyebrow">Francisation · Niveau 1 · Éléments de graphie</p>
      <h1 class="pl-band__t">Même mot, autre police</h1>
    </div>
    <div class="pl-band__a">
      <button type="button" class="btn btn--ghost btn--sm" id="profToggle" aria-pressed="false">Mode enseignant</button>
      <button type="button" class="btn btn--ghost btn--sm" id="presToggle" aria-pressed="false">Présentation</button>
    </div>
  </div>
</header>

<nav class="steps pl-steps" aria-label="Étapes de l'activité">
  <div class="steps__inner pl-steps__in" role="tablist">
    <button type="button" class="step" role="tab" aria-selected="true"  data-vue="vueRegarder"><span class="step__dot"></span>Je regarde</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueTrouver"><span class="step__dot"></span>Je trouve le même mot</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueMaitrise"><span class="step__dot"></span>Où j'en suis</button>
  </div>
</nav>

<button type="button" class="btn btn--pri btn--sm pl-sortie" id="sortiePres">Quitter la présentation</button>

<main class="pl-wrap" id="app">

  <!-- ── Je regarde ───────────────────────────────────────────────── -->
  <section class="view is-on" id="vueRegarder">
    <div class="pl-layout">
      <aside class="pl-cote">
        <p class="pl-lbl">Les mots <span id="vus"></span></p>
        <div class="pl-mots" id="listeMots"></div>
      </aside>

      <div class="card card--flush">
        <div class="pl-piste">
          <div class="pl-track"><span id="barreVus"></span></div>
          <div class="pl-piste__n" id="compteVus"></div>
        </div>

        <div class="pl-tete">
          <div>
            <div class="pl-terme" id="terme"></div>
            <p class="pl-lieu" id="lieu"></p>
          </div>
          <button type="button" class="btn btn--audio" id="ecouter">@@SPEAKER@@Écouter le mot</button>
        </div>

        <div class="pl-planche" id="planche"></div>

        <div class="pl-pied">
          <p class="pl-lieu">C'est six fois le même mot.</p>
          <div class="pl-nav">
            <button type="button" class="btn btn--ghost btn--sm" id="precedent">Précédent</button>
            <button type="button" class="btn btn--pri btn--sm" id="suivant">Suivant</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Je trouve le même mot ────────────────────────────────────── -->
  <section class="view" id="vueTrouver">
    <div class="card card--flush">
      <div class="pl-barre">
        <span id="scoreTrouver">0 point</span>
        <span id="serieTrouver"></span>
      </div>
      <div class="pl-consigne">
        <p class="pl-consigne__c">Ce mot est écrit autrement, plus bas. Trouvez-le.</p>
        <div class="pl-cible" id="cible"></div>
      </div>
      <div class="pl-reponses" id="reponses"></div>
      <div class="pl-retour"><p class="fb" id="retour"></p></div>
      <div class="pl-pied">
        <button type="button" class="btn btn--audio btn--sm" id="ecouterCible">@@SPEAKER@@Écouter</button>
        <button type="button" class="btn btn--pri btn--sm" id="suivantTrouver">Mot suivant</button>
      </div>
    </div>
  </section>

  <!-- ── Où j'en suis ─────────────────────────────────────────────── -->
  <section class="view" id="vueMaitrise">
    <div class="pl-bilan">
      <div class="card"><p class="pl-lbl">Points</p><p class="pl-chiffre" id="bXp">0</p></div>
      <div class="card"><p class="pl-lbl">Série</p><p class="pl-chiffre" id="bSerie">0</p></div>
      <div class="card"><p class="pl-lbl">Meilleure série</p><p class="pl-chiffre" id="bMeilleure">0</p></div>
      <div class="card"><p class="pl-lbl">Mots sûrs</p><p class="pl-chiffre" id="bSurs">0</p></div>
    </div>
    <div class="card card--flush">
      <table class="pl-table">
        <thead><tr><th>Mot</th><th>Où on le voit</th><th>Où j'en suis</th></tr></thead>
        <tbody id="corpsTable"></tbody>
      </table>
    </div>
    <p style="margin-top:var(--sp-5)">
      <button type="button" class="btn btn--ghost btn--sm" id="resetMaitrise">Tout recommencer</button>
    </p>
  </section>

  <!-- ── Panneau enseignant ───────────────────────────────────────── -->
  <aside class="card" id="panneauProf" style="display:none;margin-top:var(--sp-6)">
    <p class="pl-lbl">Mode enseignant</p>
    <p>Le programme du niveau 1 demande de « comprendre des mots écrits en
    caractères d'imprimerie différents » (Éléments de graphie). C'est le seul
    objet de cet atelier : l'élève ne lit pas de nouveaux mots, il relit ceux
    des quatre modules du niveau dans les six écritures où il va les
    rencontrer.</p>
    <p><strong>Les six écritures et leur nom :</strong> dans mon cahier ·
    dans un livre · sur le panneau · sur le formulaire · écrit à la main ·
    en lettres détachées. Le nom du lieu est la leçon — dites-le à voix haute
    avec l'élève avant de le laisser à « Je trouve le même mot ».</p>
    <p><strong>Les pièges de l'exercice ne sont pas des mots au hasard :</strong>
    ce sont les confusions réelles du niveau — <em>nom</em> et <em>non</em>,
    <em>prénom</em> et <em>pronom</em>, <em>accueil</em> et son orthographe
    fautive <em>acceuil</em>, <em>code postal</em> et <em>carte postale</em>.
    Un élève qui les rate ne confond pas des formes, il confond des mots :
    reprenez-les à l'oral.</p>
    <p><strong>Hors ligne</strong>, les cinq polices d'emprunt tombent sur
    leurs replis système. Les six écritures restent distinctes et l'exercice
    reste juste ; elles sont seulement moins typées.</p>
  </aside>

</main>

<script>
const items = @@ITEMS@@;
const VARIANTES = @@VARIANTES@@;
const CLE = '@@CLE@@';

const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const melanger = a => a.map(v => [Math.random(), v]).sort((x, y) => x[0] - y[0]).map(p => p[1]);
const LONG = 11;   // au-delà, le mot descend d'un cran de corps

/* Le mot tel qu'il se présente à cet endroit-là. Le formulaire et le panneau
   crient en majuscules, la main met une capitale, le cahier reste en bas de
   casse — c'est exactement ce que l'élève doit apprendre à traverser. */
function casser(mot, casse){
  if (casse === 'maj') return mot.toUpperCase();
  if (casse === 'cap') return mot.charAt(0).toUpperCase() + mot.slice(1);
  return mot.toLowerCase();
}

/* Le corps se réduit jusqu'à ce que le mot tienne dans sa case. Les classes
   CSS ne suffisent pas : « TOILETTES » en Courier espacé déborde là où
   « toilettes » en Nunito respire, et une classe posée sur la longueur en
   caractères ne peut pas le savoir. Pire, hors ligne les polices de repli
   n'ont pas les mêmes chasses — seule une mesure faite dans la page est
   juste. Sans cette fonction, « TOILETTES » sortait coupé en TOILETT / ES. */
function ajuster(el){
  el.style.fontSize = '';
  let t = parseFloat(getComputedStyle(el).fontSize);
  while (el.scrollWidth > el.clientWidth && t > 13) { t -= 1; el.style.fontSize = t + 'px'; }
}
function ajusterTous(){ $$('.pl-v__m').forEach(ajuster); }
// Les cinq polices arrivent après le premier rendu : sans ce rappel, la
// mesure porte sur les replis système et le corps reste faux.
if (document.fonts && document.fonts.ready) document.fonts.ready.then(ajusterTous);
let minuterieAjust = null;
addEventListener('resize', () => {
  clearTimeout(minuterieAjust); minuterieAjust = setTimeout(ajusterTous, 120);
});

let sonCourant = null, boutonCourant = null;
function jouer(src, bouton){
  if (!src) return;
  if (sonCourant) { sonCourant.pause(); sonCourant.currentTime = 0; }
  if (boutonCourant) boutonCourant.removeAttribute('aria-busy');
  sonCourant = new Audio(src); boutonCourant = bouton;
  bouton.setAttribute('aria-busy', 'true');
  const fini = () => bouton.removeAttribute('aria-busy');
  sonCourant.onended = fini; sonCourant.onerror = fini;
  sonCourant.play().catch(fini);
}

/* ── Maîtrise ───────────────────────────────────────────────────────── */
let maitrise = { xp: 0, serie: 0, meilleure: 0, mots: Array(items.length).fill(0) };
try {
  const brut = JSON.parse(localStorage.getItem(CLE) || 'null');
  if (brut && Array.isArray(brut.mots) && brut.mots.length === items.length) maitrise = brut;
} catch (e) {}
function sauver(){ try { localStorage.setItem(CLE, JSON.stringify(maitrise)); } catch (e) {} }
function ajouter(i, points){
  maitrise.xp = Math.max(0, maitrise.xp + points);
  maitrise.mots[i] = Math.max(-3, Math.min(6, (maitrise.mots[i] || 0) + (points > 0 ? 1 : -1)));
  if (points > 0) {
    maitrise.serie++;
    maitrise.meilleure = Math.max(maitrise.meilleure, maitrise.serie);
  } else maitrise.serie = 0;
  sauver(); rendreMaitrise();
}
function etat(n){
  if (n >= 4) return ['Sûr', '✓✓'];
  if (n >= 2) return ['Ça vient', '✓'];
  if (n >= 0) return ['À revoir', '·'];
  return ['Difficile', '!'];
}
function rendreMaitrise(){
  $('#bXp').textContent = maitrise.xp;
  $('#bSerie').textContent = maitrise.serie;
  $('#bMeilleure').textContent = maitrise.meilleure;
  $('#bSurs').textContent = maitrise.mots.filter(n => n >= 4).length + ' / ' + items.length;
  $('#scoreTrouver').textContent = maitrise.xp + (maitrise.xp > 1 ? ' points' : ' point');
  $('#serieTrouver').textContent = maitrise.serie > 1 ? 'Série de ' + maitrise.serie : '';
  $('#corpsTable').innerHTML = items.map((x, i) => {
    const [mot, glyphe] = etat(maitrise.mots[i] || 0);
    return '<tr><td><strong>' + esc(x.terme) + '</strong></td><td>' + esc(x.lieu) + '</td>'
      + '<td class="pl-etat"><span aria-hidden="true">' + glyphe + '</span> ' + mot + '</td></tr>';
  }).join('');
}

/* ── Je regarde ─────────────────────────────────────────────────────── */
let index = 0;
const vus = new Set();

function rendreListe(){
  const liste = $('#listeMots'); liste.innerHTML = '';
  items.forEach((item, i) => {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'pl-mot-btn';
    if (i === index) b.setAttribute('aria-current', 'true');
    // Le glyphe dit « vu », la couleur ne le dit jamais toute seule.
    b.innerHTML = '<span class="pl-mot-btn__e" aria-hidden="true">' + (vus.has(i) ? '✓' : '·') + '</span>'
      + '<span>' + esc(item.terme) + '</span>';
    b.onclick = () => { index = i; rendre(); };
    liste.appendChild(b);
  });
}

function rendre(){
  const x = items[index];
  $('#terme').textContent = x.terme;
  $('#lieu').textContent = 'Où je le vois : ' + x.lieu;
  $('#planche').innerHTML = VARIANTES.map(v =>
    '<div class="pl-v pl-v--' + v.cle + '">'
    + '<div class="pl-v__l">' + esc(v.lieu) + '</div>'
    + '<div class="pl-v__m' + (x.nu.length > LONG ? ' is-long' : '') + '">'
    + esc(casser(x.nu, v.casse)) + '</div></div>').join('');
  vus.add(index);
  $('#barreVus').style.width = (vus.size / items.length * 100) + '%';
  $('#compteVus').textContent = vus.size + ' / ' + items.length + ' mots vus';
  $('#vus').textContent = '(' + vus.size + ' / ' + items.length + ')';
  $('#precedent').disabled = index === 0;
  $('#suivant').textContent = index === items.length - 1 ? 'Recommencer' : 'Suivant';
  rendreListe();
  ajusterTous();
}

$('#ecouter').onclick = () => jouer(items[index].audio, $('#ecouter'));
$('#precedent').onclick = () => { index = Math.max(0, index - 1); rendre(); };
$('#suivant').onclick = () => { index = index === items.length - 1 ? 0 : index + 1; rendre(); };

/* ── Je trouve le même mot ──────────────────────────────────────────── */
let cibleCourante = null;

function batirTrouver(){
  const retour = $('#retour');
  retour.textContent = ''; retour.className = 'fb';

  cibleCourante = items[Math.floor(Math.random() * items.length)];
  const iCible = items.indexOf(cibleCourante);

  // L'énoncé et la bonne réponse ne portent JAMAIS la même écriture : sinon
  // l'élève apparie deux dessins identiques et n'a rien lu.
  const vEnonce = VARIANTES[Math.floor(Math.random() * VARIANTES.length)];
  // Cinq choix, cinq écritures : il reste exactement cinq variantes une fois
  // celle de l'énoncé retirée, on les distribue plutôt que de tirer au sort.
  // Deux boutons dans la même écriture invitaient à comparer des dessins.
  const dealt = melanger(VARIANTES.filter(v => v.cle !== vEnonce.cle));
  const vBonne = dealt[0];

  const cible = $('#cible');
  cible.className = 'pl-cible pl-v--' + vEnonce.cle + (cibleCourante.nu.length > LONG ? ' is-long' : '');
  cible.innerHTML = '<span class="pl-v__m' + (cibleCourante.nu.length > LONG ? ' is-long' : '') + '">'
    + esc(casser(cibleCourante.nu, vEnonce.casse)) + '</span>'
    + '<span class="pl-cible__ou">' + esc(vEnonce.lieu) + '</span>';

  // Deux pièges du mot lui-même — les confusions réelles du niveau — et deux
  // mots voisins de la liste. Cinq boutons en tout.
  const voisins = melanger(items.filter(x => x !== cibleCourante)).slice(0, 2).map(x => x.nu);
  const leurres = melanger([...cibleCourante.pieges, ...voisins]).slice(0, 4);
  const options = melanger([{ mot: cibleCourante.nu, bonne: true, v: vBonne },
    ...leurres.map((m, i) => ({ mot: m, bonne: false, v: dealt[i + 1] }))]);

  const zone = $('#reponses'); zone.innerHTML = '';
  options.forEach(opt => {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'pl-rep pl-v--' + opt.v.cle;
    if (opt.bonne) b.dataset.bonne = '1';
    b.innerHTML = '<span class="pl-v__m' + (opt.mot.length > LONG ? ' is-long' : '') + '">'
      + esc(casser(opt.mot, opt.v.casse)) + '</span>'
      + '<span class="pl-rep__e">' + esc(opt.v.lieu) + '</span>';
    b.onclick = () => {
      $$('#reponses .pl-rep').forEach(x => x.disabled = true);
      if (opt.bonne) {
        b.classList.add('is-ok');
        retour.className = 'fb fb--ok';
        retour.textContent = 'Juste. C\'est le même mot : ' + cibleCourante.terme + '.';
        ajouter(iCible, 10);
        jouer(cibleCourante.audio, $('#ecouterCible'));
      } else {
        b.classList.add('is-no');
        // Par la marque, jamais par le texte : « nombre » commence par
        // « nom », et deux boutons se seraient allumés en vert.
        const bonne = $('#reponses .pl-rep[data-bonne]');
        if (bonne) bonne.classList.add('is-ok');
        retour.className = 'fb fb--no';
        retour.textContent = 'Non. Le mot était : ' + cibleCourante.nu + '.';
        ajouter(iCible, -3);
      }
      lmsTrack('exercise_attempted', { correct: opt.bonne ? 1 : 0 });
    };
    zone.appendChild(b);
  });
  ajusterTous();
}
$('#suivantTrouver').onclick = batirTrouver;
$('#ecouterCible').onclick = () => cibleCourante && jouer(cibleCourante.audio, $('#ecouterCible'));

$('#resetMaitrise').onclick = () => {
  if (confirm('Tout recommencer ?')) {
    maitrise = { xp: 0, serie: 0, meilleure: 0, mots: Array(items.length).fill(0) };
    sauver(); rendreMaitrise();
  }
};

/* ── Étapes, enseignant, présentation ───────────────────────────────── */
$$('.step').forEach(s => s.onclick = () => {
  $$('.step').forEach(x => x.setAttribute('aria-selected', String(x === s)));
  $$('.view').forEach(v => v.classList.toggle('is-on', v.id === s.dataset.vue));
  if (s.dataset.vue === 'vueTrouver' && !cibleCourante) batirTrouver();
});
$('#profToggle').onclick = () => {
  const p = $('#panneauProf');
  const on = p.style.display === 'none';
  p.style.display = on ? '' : 'none';
  $('#profToggle').setAttribute('aria-pressed', String(on));
};
function presentation(actif){
  document.body.classList.toggle('is-presentation', actif);
  $('#presToggle').setAttribute('aria-pressed', String(actif));
  ajusterTous();
}
$('#presToggle').onclick = () => presentation(!document.body.classList.contains('is-presentation'));
$('#sortiePres').onclick = () => presentation(false);
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') presentation(false);
});

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

rendre();
rendreMaitrise();
lmsTrack('file_opened');
</script>
</body>
</html>
'''


def rendre():
    mots = json.loads(io.open(DOSSIER / 'mots.json', encoding='utf-8').read())
    manquants = [m['slug'] for m in mots
                 if not {'slug', 'terme', 'nu', 'famille', 'lieu', 'pieges', 'audio'} <= set(m)]
    if manquants:
        sys.exit('!! mots.json : champs manquants pour %s' % ', '.join(manquants))
    return (GABARIT
            .replace('@@SPEAKER@@', SPEAKER)
            .replace('@@CLE@@', CLE)
            .replace('@@VARIANTES@@', json.dumps(VARIANTES, ensure_ascii=False))
            .replace('@@ITEMS@@', json.dumps(mots, ensure_ascii=False)))


def main(argv):
    verifier = '--verifier' in argv
    neuf = rendre()
    actuel = io.open(CIBLE, encoding='utf-8').read() if CIBLE.exists() else ''
    if actuel == neuf:
        print('  = polices-n1 : à jour')
    elif verifier:
        print('  ≠ polices-n1 : à regénérer')
        return 1
    else:
        io.open(CIBLE, 'w', encoding='utf-8').write(neuf)
        print(('  → polices-n1 : écrit (%d octets)' % len(neuf)).replace(',', ' '))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
