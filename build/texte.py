#!/usr/bin/env python3
"""Famille E — lire un texte. Un générateur, deux modes.

La forme : **un texte sous les yeux, et des questions qui obligent à y
retourner.** C'est la famille que le niveau 1 n'avait pas besoin d'avoir et
que les niveaux 5 à 8 réclament : la catégorie `texte` du programme y compte
cinq savoirs, et la catégorie `phrase` y est faite de subordination, de
concordance et de marqueurs de relation — trois choses qui n'existent pas
dans une phrase de sept mots.

    python3 build/texte.py               → réécrit les ateliers de la famille
    python3 build/texte.py --niveau 7    → seulement ceux du niveau 7
    python3 build/texte.py actualite     → seulement celui-là
    python3 build/texte.py --verifier    → dit qui est à jour, n'écrit rien

N'ÉDITEZ PAS LE HTML PRODUIT : le prochain passage l'écraserait. Le contenu
vit dans `assets/interactive/<slug>/contenu.json`, contrat dans
`docs/schemas-banque.md`.

Les deux modes
--------------
`questions` — le texte est entier, l'élève répond à des questions sur ce
qu'il vient de lire. Chaque item peut nommer l'**extrait** qui porte la
réponse : à la correction, le passage s'allume dans le texte. C'est la
différence entre « tu as faux » et « c'était écrit là ».

`trous` — le texte est troué, et chaque trou attend un mot de liaison
(*pourtant*, *puisque*, *en revanche*). Les trous se remplissent dans
l'ordre, et le texte **reste lisible** entre deux réponses : on ne peut pas
choisir un marqueur sans avoir lu ce qui vient avant et ce qui vient après,
ce qui est exactement le savoir visé.

Ce que ce fichier refuse au build
---------------------------------
· un extrait qui ne se retrouve pas mot pour mot dans le texte — il ne
  s'allumerait jamais, et personne ne le verrait avant l'élève ;
· un trou déclaré dans les items sans marque `[[n]]` dans le texte, ou
  l'inverse ;
· une bonne réponse absente de ses propres choix.
"""
import io
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTER = ROOT / 'assets/interactive'
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from banque import paires_pour, option_niveau  # noqa: E402

# Le nom de la famille dans le registre : c'est par lui que ce fichier
# retrouve ses ateliers, à tous les niveaux.
GENERATEUR = 'texte'

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
<title>@@TITRE@@ — Niveau @@NIVEAU@@</title>
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" type="image/svg+xml" href="/assets/design-system/marque-francis-favicon.svg">
<style>
/* ══════════════════════════════════════════════════════════════════════
   Famille E · lire un texte
   FICHIER GÉNÉRÉ — build/texte.py. Ne modifiez pas ce HTML.
   Aucune couleur en dur : uniquement des jetons du système de design.
   Le repérage est celui du niveau de l'atelier.
   ══════════════════════════════════════════════════════════════════════ */
body { --sec: var(--niv-@@NIVEAU@@-line); --sec-soft: var(--niv-@@NIVEAU@@-bg); }

.tx-band { padding: var(--sp-5) 0; }
.tx-band__in { max-width: var(--content-max); margin: 0 auto; padding: 0 var(--gutter);
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--sp-4); }
.tx-band__t { font-size: var(--fs-h2); font-weight: var(--fw-black);
  letter-spacing: var(--ls-title); line-height: var(--lh-title); margin-top: var(--sp-2); }
.tx-band__a { display: flex; flex-wrap: wrap; gap: var(--sp-2); }

.tx-steps__in { max-width: var(--content-max); margin: 0 auto;
  padding: var(--sp-3) var(--gutter); display: flex; flex-wrap: wrap; gap: var(--sp-2); align-items: center; }
.step { font-family: var(--font-sans); cursor: pointer; }
.step[aria-selected="true"] { background: var(--sel-bg); border-color: var(--sel-line); color: var(--sel-ink); }

.tx-wrap { max-width: var(--content-max); margin: 0 auto; padding: var(--sp-8) var(--gutter) var(--sp-12); }
.view { display: none; }
.view.is-on { display: block; }

.tx-lbl { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); margin-bottom: var(--sp-3); }
.tx-barre { padding: var(--sp-3) var(--sp-6); border-bottom: 1px solid var(--border);
  display: flex; align-items: center; gap: var(--sp-4);
  font-size: var(--fs-ui-sm); font-weight: var(--fw-bold); color: var(--text-muted); }
.tx-pied { padding: var(--sp-4) var(--sp-6); border-top: 1px solid var(--border);
  display: flex; flex-wrap: wrap; gap: var(--sp-3); align-items: center; justify-content: space-between; }

/* ── Les deux colonnes : le texte à gauche, la question à droite ─────── */
/* Sous 900 px elles s'empilent, le texte en premier. On ne réduit jamais le
   texte à un accordéon : un élève qui doit rouvrir le texte à chaque
   question répond de mémoire, ce qui n'est pas l'exercice. */
.tx-duo { display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, 1fr);
  gap: var(--sp-6); padding: var(--sp-6); align-items: start; }

.tx-doc { border: 1px solid var(--border); border-radius: var(--r-md);
  background: var(--surface-card); padding: var(--sp-5) var(--sp-6); }
.tx-doc__src { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--sec); margin-bottom: var(--sp-2); }
.tx-doc__t { font-size: var(--fs-h3); font-weight: var(--fw-black); line-height: var(--lh-title);
  letter-spacing: var(--ls-title); margin-bottom: var(--sp-3); }
.tx-doc__c { font-size: var(--fs-body); font-weight: var(--fw-semi); color: var(--text-muted);
  margin-bottom: var(--sp-4); }
.tx-doc p.tx-par { font-size: clamp(16px, 1.15vw, 18px); line-height: 1.72; margin-bottom: var(--sp-4); }
.tx-doc p.tx-par:last-child { margin-bottom: 0; }
.tx-extrait { background: var(--sel-bg); border-bottom: 2px solid var(--sel-line);
  border-radius: 3px; padding: 1px 2px; }

/* ── Le trou dans le texte ──────────────────────────────────────────── */
.tx-trou { display: inline-block; min-width: 92px; text-align: center;
  padding: 0 var(--sp-2); font-weight: var(--fw-bold);
  border-bottom: 3px solid var(--border-firm); color: var(--text-muted); }
.tx-trou.is-actif { border-color: var(--sec); color: var(--sec); }
.tx-trou.is-ok { border-color: var(--ok-line); color: var(--ok-line); }
.tx-trou.is-no { border-color: var(--no-line); color: var(--no-line); }

/* ── La question ────────────────────────────────────────────────────── */
.tx-q { position: sticky; top: var(--sp-4); }
.tx-q__n { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); margin-bottom: var(--sp-2); }
.tx-q__t { font-size: clamp(18px, 1.6vw, 23px); font-weight: var(--fw-bold);
  line-height: 1.4; margin-bottom: var(--sp-5); }
.tx-choix { display: flex; flex-direction: column; gap: var(--sp-3); }
.tx-choix button { font-family: var(--font-sans); text-align: left;
  font-size: clamp(15px, 1.2vw, 18px); font-weight: var(--fw-semi); line-height: 1.4;
  padding: var(--sp-3) var(--sp-4); min-height: var(--tap-min);
  border: 1px solid var(--border); border-radius: var(--r-md); background: var(--surface-card);
  color: var(--text-strong); cursor: pointer;
  transition: background var(--dur) var(--ease), border-color var(--dur) var(--ease); }
.tx-choix button:hover:not(:disabled) { background: var(--paper-100); border-color: var(--sec); }
.tx-choix button:disabled { cursor: default; }
.tx-choix button.is-ok { border-color: var(--ok-line); background: var(--ok-bg); }
.tx-choix button.is-no { border-color: var(--no-line); background: var(--no-bg); }
.tx-sens { margin-top: var(--sp-4); font-size: var(--fs-body-sm); color: var(--text-muted);
  min-height: 24px; }
.tx-retour { margin-top: var(--sp-3); min-height: 28px; }

/* ── Où j'en suis ───────────────────────────────────────────────────── */
.tx-bilan { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: var(--sp-4);
  margin-bottom: var(--sp-6); }
.tx-chiffre { font-size: clamp(30px, 3.4vw, 42px); font-weight: var(--fw-black); line-height: 1; }
.tx-table { width: 100%; border-collapse: collapse; font-size: var(--fs-body-sm); }
.tx-table th, .tx-table td { padding: var(--sp-3) var(--sp-4); border-bottom: 1px solid var(--border);
  text-align: left; }
.tx-table th { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); }
.tx-etat { font-weight: var(--fw-bold); white-space: nowrap; }

.tx-sortie { display: none; position: fixed; top: var(--sp-4); right: var(--sp-4); z-index: 50; }
.is-presentation .tx-band, .is-presentation .tx-steps { display: none; }
.is-presentation .tx-sortie { display: inline-flex; }
.is-presentation .tx-doc p.tx-par { font-size: clamp(19px, 1.7vw, 24px); }
.is-presentation .tx-q__t { font-size: clamp(24px, 2.4vw, 32px); }

@media (max-width: 900px) {
  .tx-duo { grid-template-columns: 1fr; }
  .tx-q { position: static; }
}
@media (max-width: 640px) {
  .tx-band__in, .tx-steps__in, .tx-wrap { padding-left: var(--sp-5); padding-right: var(--sp-5); }
  .tx-bilan { grid-template-columns: 1fr 1fr; }
  .tx-duo { padding: var(--sp-5) var(--sp-4); }
  .tx-doc { padding: var(--sp-4); }
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

<header class="band tx-band">
  <div class="tx-band__in">
    <div>
      <p class="band__eyebrow">@@EYEBROW@@</p>
      <h1 class="tx-band__t">@@TITRE@@</h1>
    </div>
    <div class="tx-band__a">
      <button type="button" class="btn btn--ghost btn--sm" id="profToggle" aria-pressed="false">Mode enseignant</button>
      <button type="button" class="btn btn--ghost btn--sm" id="presToggle" aria-pressed="false">Présentation</button>
    </div>
  </div>
</header>

<nav class="steps tx-steps" aria-label="Étapes de l'activité">
  <div class="steps__inner tx-steps__in" role="tablist">
    <button type="button" class="step" role="tab" aria-selected="true"  data-vue="vueJeu"><span class="step__dot"></span>@@ETAPE1@@</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueTexte"><span class="step__dot"></span>Le texte en entier</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueMaitrise"><span class="step__dot"></span>Où j'en suis</button>
  </div>
</nav>

<button type="button" class="btn btn--pri btn--sm tx-sortie" id="sortiePres">Quitter la présentation</button>

<main class="tx-wrap" id="app">

  <section class="view is-on" id="vueJeu">
    <div class="card card--flush">
      <div class="tx-barre">
        <span id="score">0 point</span>
        <span id="serie"></span>
        <span id="avance"></span>
      </div>
      <div class="tx-duo">
        <div class="tx-doc" id="doc"></div>
        <div class="tx-q">
          <p class="tx-q__n" id="numero"></p>
          <p class="tx-q__t" id="question"></p>
          <div class="tx-choix" id="choix"></div>
          <p class="tx-sens" id="sens"></p>
          <div class="tx-retour"><p class="fb" id="retour"></p></div>
        </div>
      </div>
      <div class="tx-pied">
        <div class="tx-band__a">
          <button type="button" class="btn btn--audio btn--sm" id="ecouter">@@SPEAKER@@Écouter le texte</button>
        </div>
        <button type="button" class="btn btn--pri btn--sm" id="suivantJeu">Suivant</button>
      </div>
    </div>
  </section>

  <section class="view" id="vueTexte">
    <p class="tx-lbl">Le texte, et ce que chaque question demandait</p>
    <div class="card"><div class="tx-doc" id="docPlein" style="border:0;padding:0"></div></div>
    <div class="card card--flush" style="margin-top:var(--sp-5)">
      <table class="tx-table">
        <thead><tr><th>Question</th><th>Réponse</th><th>Pourquoi</th></tr></thead>
        <tbody id="corpsReponses"></tbody>
      </table>
    </div>
  </section>

  <section class="view" id="vueMaitrise">
    <div class="tx-bilan">
      <div class="card"><p class="tx-lbl">Points</p><p class="tx-chiffre" id="bXp">0</p></div>
      <div class="card"><p class="tx-lbl">Série</p><p class="tx-chiffre" id="bSerie">0</p></div>
      <div class="card"><p class="tx-lbl">Meilleure série</p><p class="tx-chiffre" id="bMeilleure">0</p></div>
      <div class="card"><p class="tx-lbl">Sûres</p><p class="tx-chiffre" id="bSurs">0</p></div>
    </div>
    <div class="card card--flush">
      <table class="tx-table">
        <thead><tr><th>Question</th><th>Ce qu'elle demande</th><th>Où j'en suis</th></tr></thead>
        <tbody id="corpsTable"></tbody>
      </table>
    </div>
    <p style="margin-top:var(--sp-5)">
      <button type="button" class="btn btn--ghost btn--sm" id="resetMaitrise">Tout recommencer</button>
    </p>
  </section>

  <aside class="card" id="panneauProf" style="display:none;margin-top:var(--sp-6)">
    <p class="tx-lbl">Mode enseignant</p>
    @@NOTE_PROF@@
    <p><strong>Le texte ne disparaît jamais.</strong> Il reste à côté de la
    question, y compris après la réponse. Un élève qui doit rouvrir le texte
    pour vérifier répond de mémoire — ce n'est pas l'exercice.</p>
    <p><strong>La correction montre où c'était écrit.</strong> Quand une
    réponse est fausse, le passage qui la portait s'allume dans le texte. Le
    but n'est pas de dire « c'est faux », c'est de faire relire.</p>
  </aside>

</main>

<script>
const CONTENU = @@CONTENU@@;
const items = CONTENU.items;
const MODE = CONTENU.mode;
const CLE = CONTENU.cle;
const TEXTE = CONTENU.texte;

const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const melanger = a => a.map(v => [Math.random(), v]).sort((x, y) => x[0] - y[0]).map(p => p[1]);

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
let maitrise = { xp: 0, serie: 0, meilleure: 0, items: Array(items.length).fill(0) };
try {
  const brut = JSON.parse(localStorage.getItem(CLE) || 'null');
  if (brut && Array.isArray(brut.items) && brut.items.length === items.length) maitrise = brut;
} catch (e) {}
function sauver(){ try { localStorage.setItem(CLE, JSON.stringify(maitrise)); } catch (e) {} }
function ajouter(i, points){
  maitrise.xp = Math.max(0, maitrise.xp + points);
  maitrise.items[i] = Math.max(-3, Math.min(6, (maitrise.items[i] || 0) + (points > 0 ? 1 : -1)));
  if (points > 0) { maitrise.serie++; maitrise.meilleure = Math.max(maitrise.meilleure, maitrise.serie); }
  else maitrise.serie = 0;
  sauver(); rendreMaitrise();
}
function etat(n){
  if (n >= 4) return ['Sûre', '✓✓'];
  if (n >= 2) return ['Ça vient', '✓'];
  if (n >= 0) return ['À revoir', '·'];
  return ['Difficile', '!'];
}
function rendreMaitrise(){
  $('#bXp').textContent = maitrise.xp;
  $('#bSerie').textContent = maitrise.serie;
  $('#bMeilleure').textContent = maitrise.meilleure;
  $('#bSurs').textContent = maitrise.items.filter(n => n >= 4).length + ' / ' + items.length;
  $('#score').textContent = maitrise.xp + (maitrise.xp > 1 ? ' points' : ' point');
  $('#serie').textContent = maitrise.serie > 1 ? 'Série de ' + maitrise.serie : '';
  $('#corpsTable').innerHTML = items.map((x, i) => {
    const [mot, glyphe] = etat(maitrise.items[i] || 0);
    return '<tr><td><strong>' + esc(x.q || ('Le trou ' + x.numero)) + '</strong></td>'
      + '<td>' + esc(x.vise || '') + '</td>'
      + '<td class="tx-etat"><span aria-hidden="true">' + glyphe + '</span> ' + mot + '</td></tr>';
  }).join('');
}

/* ── Le texte ───────────────────────────────────────────────────────── */
/* Les trous sont écrits [[1]], [[2]]… dans les paragraphes. Le rendu les
   remplace par un gabarit ; le contenu d'un trou est réécrit à chaque
   réponse, sans toucher au reste du paragraphe. */
function paragraphe(p, opts){
  let h = esc(p);
  if (opts.extrait) {
    const e = esc(opts.extrait);
    if (h.indexOf(e) !== -1) h = h.split(e).join('<mark class="tx-extrait">' + e + '</mark>');
  }
  h = h.replace(/\[\[(\d+)\]\]/g, function(_, n){
    const it = items.find(x => String(x.numero) === n);
    const rep = reponses[n];
    let cls = 'tx-trou', txt = '·  ·  ·';
    if (rep) { cls += rep.juste ? ' is-ok' : ' is-no'; txt = rep.choisi; }
    else if (it && courant && String(courant.numero) === n) { cls += ' is-actif'; txt = '?'; }
    return '<span class="' + cls + '" data-trou="' + n + '">' + esc(txt) + '</span>';
  });
  return '<p class="tx-par">' + h + '</p>';
}

function rendreDoc(cible, opts){
  opts = opts || {};
  const src = TEXTE.source ? '<p class="tx-doc__src">' + esc(TEXTE.source) + '</p>' : '';
  const chap = TEXTE.chapeau ? '<p class="tx-doc__c">' + esc(TEXTE.chapeau) + '</p>' : '';
  cible.innerHTML = src
    + '<p class="tx-doc__t">' + esc(TEXTE.titre) + '</p>' + chap
    + TEXTE.paragraphes.map(p => paragraphe(p, opts)).join('');
}

/* ── L'ordre de passage ─────────────────────────────────────────────── */
/* En mode « trous », l'ordre est celui du texte : choisir un marqueur sans
   avoir lu ce qui précède n'a pas de sens. En mode « questions », l'ordre
   est mélangé une fois pour toutes, comme dans les autres familles. */
let ordre = MODE === 'trous' ? items.map((_, i) => i) : melanger(items.map((_, i) => i));
let rang = 0, courant = null, iCourant = 0, repondu = false, choisi = null;
let melangeCourant = [];
const reponses = {};   /* numéro de trou → {choisi, juste} */

function itemCourant(){
  iCourant = ordre[rang % ordre.length];
  courant = items[iCourant];
  return courant;
}

function rendreJeu(){
  $('#avance').textContent = (rang % items.length + 1) + ' / ' + items.length;
  $('#numero').textContent = MODE === 'trous'
    ? 'Le trou ' + courant.numero
    : 'Question ' + (rang % items.length + 1);
  $('#question').textContent = MODE === 'trous'
    ? (courant.q || 'Quel mot de liaison va dans ce trou ?')
    : courant.q;
  $('#ecouter').style.display = TEXTE.audio ? '' : 'none';
  rendreDoc($('#doc'), { extrait: repondu ? courant.extrait : null });

  const zone = $('#choix');
  zone.innerHTML = '';
  melangeCourant.forEach(c => {
    const b = document.createElement('button');
    b.type = 'button';
    b.textContent = c;
    b.disabled = repondu;
    if (repondu && c === courant.ok) b.classList.add('is-ok');
    if (repondu && c === choisi && c !== courant.ok) b.classList.add('is-no');
    b.onclick = () => { choisi = c; verifier(); };
    zone.appendChild(b);
  });
}

function nouveauTour(){
  itemCourant();
  repondu = false; choisi = null;
  $('#retour').textContent = ''; $('#retour').className = 'fb';
  $('#sens').textContent = '';
  melangeCourant = melanger(courant.choix.slice());
  rendreJeu();
}

function verifier(){
  repondu = true;
  const juste = choisi === courant.ok;
  if (MODE === 'trous') reponses[String(courant.numero)] = { choisi: choisi, juste: juste };
  const retour = $('#retour');
  if (juste) {
    retour.className = 'fb fb--ok';
    retour.textContent = 'Juste.';
    ajouter(iCourant, 10);
  } else {
    retour.className = 'fb fb--no';
    retour.textContent = 'La réponse était : ' + courant.ok;
    ajouter(iCourant, -3);
  }
  $('#sens').textContent = courant.sens || '';
  rendreJeu();
  lmsTrack('exercise_attempted', { correct: juste ? 1 : 0 });
}

$('#suivantJeu').onclick = () => { rang++; nouveauTour(); };
$('#ecouter').onclick = () => jouer(TEXTE.audio, $('#ecouter'));

/* ── Le texte en entier ─────────────────────────────────────────────── */
function rendreTexteComplet(){
  const garde = Object.assign({}, reponses);
  items.forEach(x => { if (MODE === 'trous') reponses[String(x.numero)] = { choisi: x.ok, juste: true }; });
  rendreDoc($('#docPlein'), {});
  Object.keys(reponses).forEach(k => delete reponses[k]);
  Object.assign(reponses, garde);
  $('#corpsReponses').innerHTML = items.map(x =>
    '<tr><td>' + esc(x.q || ('Le trou ' + x.numero)) + '</td>'
    + '<td><strong>' + esc(x.ok) + '</strong></td>'
    + '<td>' + esc(x.sens || '') + '</td></tr>').join('');
}

$('#resetMaitrise').onclick = () => {
  if (confirm('Tout recommencer ?')) {
    maitrise = { xp: 0, serie: 0, meilleure: 0, items: Array(items.length).fill(0) };
    sauver(); rendreMaitrise();
  }
};

$$('.step').forEach(s => s.onclick = () => {
  $$('.step').forEach(x => x.setAttribute('aria-selected', String(x === s)));
  $$('.view').forEach(v => v.classList.toggle('is-on', v.id === s.dataset.vue));
  if (s.dataset.vue === 'vueTexte') rendreTexteComplet();
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
}
$('#presToggle').onclick = () => presentation(!document.body.classList.contains('is-presentation'));
$('#sortiePres').onclick = () => presentation(false);
document.addEventListener('keydown', e => { if (e.key === 'Escape') presentation(false); });

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

nouveauTour();
rendreMaitrise();
lmsTrack('file_opened');
</script>
</body>
</html>
'''

COMMUNS = {'slug', 'niveau', 'generateur', 'titre', 'eyebrow', 'cle', 'consigne',
           'note_prof', 'savoirs', 'mode', 'texte', 'items'}
TROU = re.compile(r'\[\[(\d+)\]\]')


def controler(slug, c):
    """Ce que le build refuse de laisser passer.

    Les trois contrôles attrapent des fautes qui ne lèvent aucune erreur :
    l'atelier s'affiche, et c'est l'élève qui découvre qu'il est injouable.
    """
    manquants = COMMUNS - set(c)
    if manquants:
        sys.exit('!! %s : champs manquants — %s' % (slug, ', '.join(sorted(manquants))))
    if c['slug'] != slug:
        sys.exit('!! %s : le slug du contenu dit « %s »' % (slug, c['slug']))
    if c['mode'] not in ('questions', 'trous'):
        sys.exit('!! %s : mode inconnu « %s »' % (slug, c['mode']))

    t = c['texte']
    for champ in ('titre', 'paragraphes'):
        if not t.get(champ):
            sys.exit('!! %s : le texte n\'a pas de %s' % (slug, champ))
    plein = '\n'.join(t['paragraphes'])
    mots = len(plein.split())
    if mots < 60:
        sys.exit('!! %s : %d mots — ce n\'est pas un texte, c\'est une phrase'
                 % (slug, mots))

    vus, numeros = set(), set()
    for it in c['items']:
        s = it.get('slug')
        if not s or s in vus:
            sys.exit('!! %s : slug d\'item manquant ou en double — %r' % (slug, s))
        vus.add(s)
        for champ in ('choix', 'ok'):
            if not it.get(champ):
                sys.exit('!! %s / %s : pas de %s' % (slug, s, champ))
        if it['ok'] not in it['choix']:
            sys.exit('!! %s / %s : la bonne réponse n\'est pas dans les choix'
                     % (slug, s))
        if not 2 <= len(it['choix']) <= 4:
            sys.exit('!! %s / %s : %d choix — il en faut de 2 à 4'
                     % (slug, s, len(it['choix'])))
        if len(set(it['choix'])) != len(it['choix']):
            sys.exit('!! %s / %s : deux choix identiques' % (slug, s))

        if c['mode'] == 'questions':
            if not it.get('q'):
                sys.exit('!! %s / %s : pas de question' % (slug, s))
            # L'extrait doit se retrouver mot pour mot, sinon il ne
            # s'allumerait jamais et personne ne le verrait avant l'élève.
            if it.get('extrait') and it['extrait'] not in plein:
                sys.exit('!! %s / %s : l\'extrait n\'est pas dans le texte\n'
                         '   cherché : %r' % (slug, s, it['extrait']))
        else:
            n = it.get('numero')
            if not isinstance(n, int):
                sys.exit('!! %s / %s : un trou sans numéro' % (slug, s))
            if n in numeros:
                sys.exit('!! %s / %s : le trou %d est déclaré deux fois' % (slug, s, n))
            numeros.add(n)

    if c['mode'] == 'trous':
        # Les deux sens du contrôle : un trou déclaré sans marque dans le
        # texte ne se joue jamais ; une marque sans item reste vide à
        # l'écran, pour toujours.
        marques = {int(m) for m in TROU.findall(plein)}
        if marques != numeros:
            sys.exit('!! %s : les trous du texte %s ne sont pas ceux des items %s'
                     % (slug, sorted(marques), sorted(numeros)))
    else:
        if TROU.search(plein):
            sys.exit('!! %s : le texte porte des [[n]] alors que le mode est '
                     '« questions »' % slug)


def rendre(slug):
    fichier = INTER / slug / 'contenu.json'
    if not fichier.exists():
        sys.exit('!! %s introuvable' % fichier)
    c = json.loads(io.open(fichier, encoding='utf-8').read())
    controler(slug, c)
    etape1 = ('Je lis et je complète' if c['mode'] == 'trous'
              else 'Je lis et je réponds')
    return (GABARIT
            .replace('@@SPEAKER@@', SPEAKER)
            .replace('@@NIVEAU@@', str(c['niveau']))
            .replace('@@TITRE@@', c['titre'])
            .replace('@@EYEBROW@@', c['eyebrow'])
            .replace('@@ETAPE1@@', etape1)
            .replace('@@CONSIGNE@@', c['consigne'])
            .replace('@@NOTE_PROF@@', c['note_prof'])
            .replace('@@CONTENU@@', json.dumps(c, ensure_ascii=False)))


def main(argv):
    niveau, argv = option_niveau(argv)
    verifier = '--verifier' in argv
    voulus = [a for a in argv if not a.startswith('--')]
    ecart = 0
    for slug, num in paires_pour(GENERATEUR, niveau):
        if voulus and not any(v in slug for v in voulus):
            continue
        if not (INTER / slug / 'contenu.json').exists():
            print('  · %-20s (activité %s) : contenu pas encore écrit' % (slug, num))
            continue
        cible = INTER / slug / ('%s-activite-interactive.html' % slug)
        neuf = rendre(slug)
        actuel = io.open(cible, encoding='utf-8').read() if cible.exists() else ''
        if actuel == neuf:
            print('  = %-20s (activité %s) : à jour' % (slug, num))
        elif verifier:
            print('  ≠ %-20s (activité %s) : à regénérer' % (slug, num)); ecart = 1
        else:
            cible.parent.mkdir(parents=True, exist_ok=True)
            io.open(cible, 'w', encoding='utf-8').write(neuf)
            print('  → %-20s (activité %s) : écrit (%d octets)' % (slug, num, len(neuf)))
    return ecart


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
