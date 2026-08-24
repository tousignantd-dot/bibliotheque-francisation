#!/usr/bin/env python3
"""Famille B — discriminer à l'oreille. Un générateur, deux modes, cinq ateliers.

La forme : **on écoute, et on tranche.** C'est la famille la plus payante du
niveau 1 — la moitié de ses savoirs sont phonétiques — et la seule qui
n'existe pas sans audio. Les autres ateliers sont muets tant que les MP3 ne
sont pas produits ; ceux-ci n'ont simplement pas de contenu.

    python3 build/oreille.py             → réécrit les cinq ateliers
    python3 build/oreille.py voyelles    → seulement celui-là
    python3 build/oreille.py --verifier  → dit qui est à jour, n'écrit rien
    python3 build/oreille.py --audio     → dit lesquels ont leurs MP3

N'ÉDITEZ PAS LE HTML PRODUIT : le prochain passage l'écraserait. Le contenu
vit dans `assets/interactive/<slug>/contenu.json`, contrat dans
`docs/schemas-banque-n1.md`.

Les deux modes
--------------
`choisir` — un extrait joue, deux ou trois boutons, l'élève clique ce qu'il a
entendu. Les boutons portent du texte, ou des pictogrammes de
`build/pictos.py` quand `choix_type` vaut `"picto"` (les consignes de classe).

`barrer` — un extrait joue, la phrase est écrite, et l'élève **barre les e
qu'il n'entend pas**. C'est l'exercice le plus original de la banque : il
attaque de front l'écart entre ce qui est écrit et ce qui est dit, qui est la
première cause d'incompréhension orale chez un élève alphabétisé dans une
autre langue.

Pourquoi ces ateliers n'entrent pas au catalogue tout de suite
--------------------------------------------------------------
Un atelier de cette famille sans ses MP3 n'est pas « muet », il est
**injouable** : l'extrait *est* la question. Les inscrire dans
`data/activities.json` les rendrait visibles aux élèves dans le banc des
exercices libres, où ils sont toujours ouverts et sans date — donc offerts
cassés. `--audio` dit lesquels sont prêts ; ils entrent au catalogue quand ils
le sont, pas avant. Les cinq HTML sont livrés et poussés dès maintenant : ce
qui manque est le média, pas le travail.
"""
import io
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
INTER = ROOT / 'assets/interactive'

from pictos import TOUS as PICTOS

ATELIERS = [
    ('voyelles-n1',       140),
    ('consonnes-n1',      141),
    ('e-muet-n1',         142),
    ('intonation-n1',     143),
    ('formes-rapides-n1', 144),
    ('jean-dit-n1',       145),
]

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
<title>@@TITRE@@ — Niveau 1</title>
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-saaf.css">
<link rel="icon" type="image/svg+xml" href="/assets/design-system/marque-saaf-favicon.svg">
<style>
/* ══════════════════════════════════════════════════════════════════════
   Famille B · discriminer à l'oreille
   FICHIER GÉNÉRÉ — build/oreille.py. Ne modifiez pas ce HTML.
   Aucune couleur en dur : uniquement des jetons du système de design.
   Le repérage est celui du niveau 1 — framboise.
   ══════════════════════════════════════════════════════════════════════ */
body { --sec: var(--niv-1-line); --sec-soft: var(--niv-1-bg); }

.or-band { padding: var(--sp-5) 0; }
.or-band__in { max-width: var(--content-max); margin: 0 auto; padding: 0 var(--gutter);
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--sp-4); }
.or-band__t { font-size: var(--fs-h2); font-weight: var(--fw-black);
  letter-spacing: var(--ls-title); line-height: var(--lh-title); margin-top: var(--sp-2); }
.or-band__a { display: flex; flex-wrap: wrap; gap: var(--sp-2); }

.or-steps__in { max-width: var(--content-max); margin: 0 auto;
  padding: var(--sp-3) var(--gutter); display: flex; flex-wrap: wrap; gap: var(--sp-2); align-items: center; }
.step { font-family: var(--font-sans); cursor: pointer; }
.step[aria-selected="true"] { background: var(--sel-bg); border-color: var(--sel-line); color: var(--sel-ink); }

.or-wrap { max-width: var(--content-max); margin: 0 auto; padding: var(--sp-8) var(--gutter) var(--sp-12); }
.view { display: none; }
.view.is-on { display: block; }

.or-lbl { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); margin-bottom: var(--sp-3); }
.or-barre { padding: var(--sp-3) var(--sp-6); border-bottom: 1px solid var(--border);
  display: flex; align-items: center; gap: var(--sp-4);
  font-size: var(--fs-ui-sm); font-weight: var(--fw-bold); color: var(--text-muted); }
.or-pied { padding: var(--sp-4) var(--sp-6); border-top: 1px solid var(--border);
  display: flex; flex-wrap: wrap; gap: var(--sp-3); align-items: center; justify-content: space-between; }
.or-jeu { padding: var(--sp-6); }
.or-consigne { font-size: var(--fs-body); font-weight: var(--fw-semi); color: var(--text-muted);
  margin-bottom: var(--sp-5); text-align: center; }

/* ── Le gros bouton d'écoute : c'est lui, la question ────────────────── */
.or-ecoute { display: flex; justify-content: center; margin-bottom: var(--sp-6); }
.or-ecoute .btn { font-size: var(--fs-h3); padding: var(--sp-4) var(--sp-8); min-height: 72px; }
.or-ecoute .btn svg { width: 28px; height: 28px; }

/* ── Mode « choisir » ───────────────────────────────────────────────── */
.or-choix { display: flex; flex-wrap: wrap; gap: var(--sp-4); justify-content: center; }
.or-rep { font-family: var(--font-sans); font-size: clamp(21px, 2.6vw, 32px);
  font-weight: var(--fw-bold); line-height: 1.2;
  padding: var(--sp-4) var(--sp-6); min-height: var(--tap-min); min-width: 148px;
  border: 1px solid var(--border); border-radius: var(--r-md); background: var(--surface-card);
  color: var(--text-strong); cursor: pointer;
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: var(--sp-2);
  transition: background var(--dur) var(--ease), border-color var(--dur) var(--ease); }
.or-rep:hover:not(:disabled) { background: var(--paper-100); border-color: var(--sec); }
.or-rep:disabled { cursor: default; }
.or-rep.is-ok { border-color: var(--ok-line); background: var(--ok-bg); }
.or-rep.is-no { border-color: var(--no-line); background: var(--no-bg); }
.or-rep svg { width: 100%; max-width: 116px; height: auto; display: block; }

/* ── Mode « barrer » ────────────────────────────────────────────────── */
.or-phrase { font-family: var(--font-sans); font-size: clamp(26px, 3.4vw, 42px);
  font-weight: var(--fw-bold); line-height: 1.6; text-align: center;
  margin-bottom: var(--sp-6); }
/* Un e cliquable ne doit pas déformer le mot. Le premier essai lui donnait
   4 px de part et d'autre : « L'entré e est à gauch e. » — un élève qui
   apprend à reconnaître la forme des mots y perd plus qu'il ne gagne en
   confort de clic. Le repère est donc un filet pointillé sous la lettre, qui
   ne prend aucune place, et la cible du doigt est agrandie par-dessous avec
   un pseudo-élément qui ne pousse rien. */
.or-e { display: inline-block; padding: 0 1px; border-radius: var(--r-sm);
  border-bottom: 2px dotted var(--border); cursor: pointer; position: relative;
  transition: background var(--dur) var(--ease), color var(--dur) var(--ease); }
.or-e::after { content: ''; position: absolute; left: -6px; right: -6px; top: -8px; bottom: -8px; }
.or-e:hover { background: var(--sec-soft); }
.or-e.is-barre { color: var(--text-muted); text-decoration: line-through;
  text-decoration-thickness: 3px; }
/* Après correction : ce qui était juste, ce qui était barré pour rien, et ce
   qui a été oublié. Trois états, trois couleurs — mais chacun porte aussi une
   marque de forme, parce que la couleur ne dit jamais l'information seule. */
.or-e.is-juste { background: var(--ok-bg); color: var(--ok-line); }
.or-e.is-trop { background: var(--no-bg); color: var(--no-line); }
.or-e.is-oubli { background: var(--no-bg); color: var(--no-line);
  text-decoration: underline wavy; text-decoration-thickness: 2px; }

.or-legende { display: flex; flex-wrap: wrap; gap: var(--sp-4); justify-content: center;
  font-size: var(--fs-ui-sm); color: var(--text-muted); margin-top: var(--sp-4); }

.or-indice { margin-top: var(--sp-4); font-size: var(--fs-body-sm); color: var(--text-muted);
  text-align: center; min-height: 24px; }
.or-dit { margin-top: var(--sp-2); font-size: var(--fs-body); font-weight: var(--fw-bold);
  text-align: center; min-height: 26px; }
.or-retour { margin-top: var(--sp-4); min-height: 28px; text-align: center; }

/* ── Je regarde les extraits ────────────────────────────────────────── */
.or-liste { display: grid; grid-template-columns: repeat(auto-fit, minmax(258px, 1fr)); gap: var(--sp-4); }
.or-carte { padding: var(--sp-5); border: 1px solid var(--border); border-radius: var(--r-md);
  background: var(--surface-card); display: flex; flex-direction: column; gap: var(--sp-3); }
.or-carte__p { font-family: var(--font-sans); font-size: clamp(19px, 2vw, 24px);
  font-weight: var(--fw-bold); line-height: 1.3; }
.or-carte__s { font-size: var(--fs-body-sm); color: var(--text-muted); }
.or-carte__a { align-self: flex-start; }

/* ── Où j'en suis ───────────────────────────────────────────────────── */
.or-bilan { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: var(--sp-4);
  margin-bottom: var(--sp-6); }
.or-chiffre { font-size: clamp(30px, 3.4vw, 42px); font-weight: var(--fw-black); line-height: 1; }
.or-table { width: 100%; border-collapse: collapse; font-size: var(--fs-body-sm); }
.or-table th, .or-table td { padding: var(--sp-3) var(--sp-4); border-bottom: 1px solid var(--border);
  text-align: left; }
.or-table th { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); }
.or-etat { font-weight: var(--fw-bold); white-space: nowrap; }

.or-sortie { display: none; position: fixed; top: var(--sp-4); right: var(--sp-4); z-index: 50; }
.is-presentation .or-band, .is-presentation .or-steps { display: none; }
.is-presentation .or-sortie { display: inline-flex; }
.is-presentation .or-rep { font-size: clamp(28px, 3.4vw, 44px); }
.is-presentation .or-phrase { font-size: clamp(34px, 4.6vw, 60px); }

@media (max-width: 640px) {
  .or-band__in, .or-steps__in, .or-wrap { padding-left: var(--sp-5); padding-right: var(--sp-5); }
  .or-bilan { grid-template-columns: 1fr 1fr; }
  .or-jeu { padding: var(--sp-5) var(--sp-4); }
  .or-rep { min-width: 120px; }
}
</style>
</head>
<body class="page">

<header class="band or-band">
  <div id="hdr">
    <div class="saaf-bandeau">
      <span class="saaf-lockup">
        <span class="saaf-pilule"><span class="saaf-nom">SAAF</span></span>
        <span class="saaf-filet" aria-hidden="true"></span>
        <span class="saaf-desc">Système d'aide à l'apprentissage du français</span>
      </span>
    </div>
  </div>
  <div class="or-band__in">
    <div>
      <p class="band__eyebrow">@@EYEBROW@@</p>
      <h1 class="or-band__t">@@TITRE@@</h1>
    </div>
    <div class="or-band__a">
      <button type="button" class="btn btn--ghost btn--sm" id="profToggle" aria-pressed="false">Mode enseignant</button>
      <button type="button" class="btn btn--ghost btn--sm" id="presToggle" aria-pressed="false">Présentation</button>
    </div>
  </div>
</header>

<nav class="steps or-steps" aria-label="Étapes de l'activité">
  <div class="steps__inner or-steps__in" role="tablist">
    <button type="button" class="step" role="tab" aria-selected="true"  data-vue="vueJeu"><span class="step__dot"></span>J'écoute</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueListe"><span class="step__dot"></span>Je regarde les extraits</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueMaitrise"><span class="step__dot"></span>Où j'en suis</button>
  </div>
</nav>

<button type="button" class="btn btn--pri btn--sm or-sortie" id="sortiePres">Quitter la présentation</button>

<main class="or-wrap" id="app">

  <section class="view is-on" id="vueJeu">
    <div class="card card--flush">
      <div class="or-barre">
        <span id="score">0 point</span>
        <span id="serie"></span>
        <span id="avance"></span>
      </div>
      <div class="or-jeu">
        <p class="or-consigne">@@CONSIGNE@@</p>
        <div class="or-ecoute">
          <button type="button" class="btn btn--audio" id="ecouter">@@SPEAKER@@Écouter</button>
        </div>
        <div id="aire"></div>
        <p class="or-dit" id="dit"></p>
        <p class="or-indice" id="indice"></p>
        <div class="or-retour"><p class="fb" id="retour"></p></div>
      </div>
      <div class="or-pied">
        <button type="button" class="btn btn--ghost btn--sm" id="verifier">Vérifier</button>
        <button type="button" class="btn btn--pri btn--sm" id="suivantJeu">Suivant</button>
      </div>
    </div>
  </section>

  <section class="view" id="vueListe">
    <p class="or-lbl">Tous les extraits de cet atelier</p>
    <div class="or-liste" id="liste"></div>
  </section>

  <section class="view" id="vueMaitrise">
    <div class="or-bilan">
      <div class="card"><p class="or-lbl">Points</p><p class="or-chiffre" id="bXp">0</p></div>
      <div class="card"><p class="or-lbl">Série</p><p class="or-chiffre" id="bSerie">0</p></div>
      <div class="card"><p class="or-lbl">Meilleure série</p><p class="or-chiffre" id="bMeilleure">0</p></div>
      <div class="card"><p class="or-lbl">Sûrs</p><p class="or-chiffre" id="bSurs">0</p></div>
    </div>
    <div class="card card--flush">
      <table class="or-table">
        <thead><tr><th>Extrait</th><th>Où j'en suis</th></tr></thead>
        <tbody id="corpsTable"></tbody>
      </table>
    </div>
    <p style="margin-top:var(--sp-5)">
      <button type="button" class="btn btn--ghost btn--sm" id="resetMaitrise">Tout recommencer</button>
    </p>
  </section>

  <aside class="card" id="panneauProf" style="display:none;margin-top:var(--sp-6)">
    <p class="or-lbl">Mode enseignant</p>
    @@NOTE_PROF@@
    <p><strong>Cet atelier ne se fait pas sans le son.</strong> L'extrait
    <em>est</em> la question : il n'y a rien à lire qui la remplace. Si les
    boutons d'écoute restent muets, c'est que les extraits ne sont pas encore
    produits — l'atelier n'est pas cassé, il est en attente.</p>
    <p><strong>Faites-le écouter deux fois avant de laisser répondre.</strong>
    La première écoute sert à reconnaître qu'il se passe quelque chose, la
    deuxième à entendre quoi. Un élève qui répond après une seule écoute
    devine.</p>
  </aside>

</main>

<script>
const CONTENU = @@CONTENU@@;
const PICTOS = @@PICTOS@@;
const items = CONTENU.items;
const MODE = CONTENU.mode;
const PICTO = CONTENU.choix_type === 'picto';
const CLE = CONTENU.cle;

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
  if (n >= 4) return ['Sûr', '✓✓'];
  if (n >= 2) return ['Ça vient', '✓'];
  if (n >= 0) return ['À revoir', '·'];
  return ['Difficile', '!'];
}
function libelle(x){ return x.dit || x.phrase || x.slug; }
function rendreMaitrise(){
  $('#bXp').textContent = maitrise.xp;
  $('#bSerie').textContent = maitrise.serie;
  $('#bMeilleure').textContent = maitrise.meilleure;
  $('#bSurs').textContent = maitrise.items.filter(n => n >= 4).length + ' / ' + items.length;
  $('#score').textContent = maitrise.xp + (maitrise.xp > 1 ? ' points' : ' point');
  $('#serie').textContent = maitrise.serie > 1 ? 'Série de ' + maitrise.serie : '';
  $('#corpsTable').innerHTML = items.map((x, i) => {
    const [mot, glyphe] = etat(maitrise.items[i] || 0);
    return '<tr><td><strong>' + esc(libelle(x)) + '</strong></td>'
      + '<td class="or-etat"><span aria-hidden="true">' + glyphe + '</span> ' + mot + '</td></tr>';
  }).join('');
}

/* ── L'ordre de passage ─────────────────────────────────────────────── */
let ordre = melanger(items.map((_, i) => i));
let rang = 0, courant = null, iCourant = 0, repondu = false, melangeCourant = [];

/* ── Mode « choisir » ───────────────────────────────────────────────── */
let choisi = null;

function corpsChoix(v){
  if (!PICTO) return esc(v);
  const p = PICTOS[v];
  return p ? '<svg viewBox="0 0 100 100" role="img" aria-label="' + esc(v) + '">' + p + '</svg>'
           : esc(v);
}

function rendreChoisir(){
  const x = courant;
  $('#aire').innerHTML = '<div class="or-choix" id="choix"></div>';
  const zone = $('#choix');
  melangeCourant.forEach(c => {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'or-rep';
    b.innerHTML = corpsChoix(c);
    b.disabled = repondu;
    if (repondu && c === x.ok) b.classList.add('is-ok');
    if (repondu && c === choisi && c !== x.ok) b.classList.add('is-no');
    b.onclick = () => { choisi = c; verifier(); };
    zone.appendChild(b);
  });
}

/* ── Mode « barrer » ────────────────────────────────────────────────── */
/* `[e]` marque un e écrit qu'on n'entend pas. Tout autre `e` se prononce et
   ne doit pas être barré — c'est ce qui empêche l'exercice de dégénérer en
   « barre tous les e ». Les e accentués ne sont jamais cliquables : ils se
   prononcent toujours, et les rendre cliquables ajouterait du bruit. */
function parser(p){
  const out = []; let tampon = '';
  for (let i = 0; i < p.length; i++) {
    if (p[i] === '[' && p[i + 1] === 'e' && p[i + 2] === ']') {
      if (tampon) { out.push({ t: 'txt', v: tampon }); tampon = ''; }
      out.push({ t: 'e', muet: true }); i += 2;
    } else if (p[i] === 'e') {
      if (tampon) { out.push({ t: 'txt', v: tampon }); tampon = ''; }
      out.push({ t: 'e', muet: false });
    } else tampon += p[i];
  }
  if (tampon) out.push({ t: 'txt', v: tampon });
  return out;
}

let morceaux = [], barres = new Set();

function rendreBarrer(){
  $('#aire').innerHTML = '<p class="or-phrase" id="phrase"></p>'
    + '<div class="or-legende">'
    + '<span>Cliquez les <strong>e</strong> que vous n\'entendez pas.</span></div>';
  const p = $('#phrase');
  morceaux.forEach((m, i) => {
    if (m.t === 'txt') { p.appendChild(document.createTextNode(m.v)); return; }
    const s = document.createElement('span');
    s.className = 'or-e'; s.textContent = 'e';
    s.setAttribute('role', 'button'); s.tabIndex = repondu ? -1 : 0;
    if (barres.has(i)) s.classList.add('is-barre');
    if (repondu) {
      const barre = barres.has(i);
      if (m.muet && barre) s.classList.add('is-juste');
      else if (!m.muet && barre) s.classList.add('is-trop');
      else if (m.muet && !barre) s.classList.add('is-oubli');
    } else {
      const bascule = () => { barres.has(i) ? barres.delete(i) : barres.add(i); rendreBarrer(); };
      s.onclick = bascule;
      s.onkeydown = e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); bascule(); } };
    }
    p.appendChild(s);
  });
  if (repondu) {
    $('.or-legende').innerHTML =
      '<span><span class="or-e is-juste">e</span> bien barré</span>'
      + '<span><span class="or-e is-trop">e</span> barré pour rien</span>'
      + '<span><span class="or-e is-oubli">e</span> oublié</span>';
  }
}

function barrerJuste(){
  return morceaux.every((m, i) => m.t !== 'e' || m.muet === barres.has(i));
}

/* ── Le tour ────────────────────────────────────────────────────────── */
function rendreJeu(){
  $('#avance').textContent = (rang % items.length + 1) + ' / ' + items.length;
  $('#verifier').style.display = (MODE === 'barrer' && !repondu) ? '' : 'none';
  if (MODE === 'barrer') rendreBarrer(); else rendreChoisir();
}

function nouveauTour(){
  iCourant = ordre[rang % ordre.length];
  courant = items[iCourant];
  repondu = false; choisi = null; barres = new Set();
  $('#retour').textContent = ''; $('#retour').className = 'fb';
  $('#indice').textContent = ''; $('#dit').textContent = '';
  if (MODE === 'barrer') morceaux = parser(courant.phrase);
  else melangeCourant = melanger(courant.choix.slice());
  rendreJeu();
  // L'extrait part tout seul : c'est la question, et la faire cliquer une
  // fois de plus n'apprend rien.
  jouer(courant.audio, $('#ecouter'));
}

function verifier(){
  repondu = true;
  const juste = MODE === 'barrer' ? barrerJuste() : choisi === courant.ok;
  const retour = $('#retour');
  retour.className = 'fb ' + (juste ? 'fb--ok' : 'fb--no');
  retour.textContent = juste ? 'Juste.' : 'Non. Écoutez encore.';
  $('#dit').textContent = courant.dit ? '« ' + courant.dit + ' »' : '';
  $('#indice').textContent = courant.indice || courant.sens || '';
  ajouter(iCourant, juste ? 10 : -3);
  rendreJeu();
  lmsTrack('exercise_attempted', { correct: juste ? 1 : 0 });
}

$('#verifier').onclick = verifier;
$('#suivantJeu').onclick = () => { rang++; nouveauTour(); };
$('#ecouter').onclick = () => jouer(courant.audio, $('#ecouter'));

/* ── Je regarde les extraits ────────────────────────────────────────── */
function rendreListe(){
  $('#liste').innerHTML = items.map((x, i) =>
    '<div class="or-carte"><p class="or-carte__p">' + esc(libelle(x)) + '</p>'
    + '<p class="or-carte__s">' + esc(x.indice || x.sens || '') + '</p>'
    + '<button type="button" class="btn btn--audio btn--sm or-carte__a" data-i="' + i
    + '">@@SPEAKER@@Écouter</button></div>').join('');
  $$('.or-carte__a').forEach(b => b.onclick = () => jouer(items[b.dataset.i].audio, b));
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
rendreListe();
rendreMaitrise();
lmsTrack('file_opened');
</script>
</body>
</html>
'''

COMMUNS = {'slug', 'titre', 'eyebrow', 'cle', 'consigne', 'note_prof', 'savoirs', 'mode', 'items'}


def controler(slug, c):
    manquants = COMMUNS - set(c)
    if manquants:
        sys.exit('!! %s : champs manquants — %s' % (slug, ', '.join(sorted(manquants))))
    if c['slug'] != slug:
        sys.exit('!! %s : le slug du contenu dit « %s »' % (slug, c['slug']))
    if c['mode'] not in ('choisir', 'barrer'):
        sys.exit('!! %s : mode inconnu « %s »' % (slug, c['mode']))
    picto = c.get('choix_type') == 'picto'

    vus = set()
    for it in c['items']:
        s = it.get('slug')
        if not s or s in vus:
            sys.exit('!! %s : slug d\'item manquant ou en double — %r' % (slug, s))
        vus.add(s)
        if not it.get('audio'):
            sys.exit('!! %s / %s : pas de chemin audio' % (slug, s))

        if c['mode'] == 'choisir':
            for champ in ('dit', 'choix', 'ok'):
                if not it.get(champ):
                    sys.exit('!! %s / %s : pas de %s' % (slug, s, champ))
            if it['ok'] not in it['choix']:
                sys.exit('!! %s / %s : la bonne réponse n\'est pas dans les choix' % (slug, s))
            if not 2 <= len(it['choix']) <= 3:
                sys.exit('!! %s / %s : %d choix — on discrimine, il en faut 2 ou 3'
                         % (slug, s, len(it['choix'])))
            if len(set(it['choix'])) != len(it['choix']):
                sys.exit('!! %s / %s : deux choix identiques' % (slug, s))
            if picto:
                for v in it['choix']:
                    if v not in PICTOS:
                        sys.exit('!! %s / %s : pictogramme « %s » absent de build/pictos.py'
                                 % (slug, s, v))
        else:
            for champ in ('phrase', 'dit'):
                if not it.get(champ):
                    sys.exit('!! %s / %s : pas de %s' % (slug, s, champ))
            # La phrase sans ses crochets doit être le texte prononcé, à la
            # ponctuation près. Sans ce contrôle, l'élève barre les e d'une
            # phrase que l'extrait ne dit pas — et rien ne le signale.
            nue = it['phrase'].replace('[e]', 'e')
            if nue != it['dit']:
                sys.exit('!! %s / %s : la phrase sans crochets ne redonne pas « dit »\n'
                         '   sans crochets : %r\n   dit           : %r' % (slug, s, nue, it['dit']))
            if '[e]' not in it['phrase']:
                sys.exit('!! %s / %s : aucun e muet marqué, il n\'y a rien à barrer'
                         % (slug, s))


def rendre(slug):
    fichier = INTER / slug / 'contenu.json'
    if not fichier.exists():
        sys.exit('!! %s introuvable' % fichier)
    c = json.loads(io.open(fichier, encoding='utf-8').read())
    controler(slug, c)
    return (GABARIT
            .replace('@@SPEAKER@@', SPEAKER)
            .replace('@@TITRE@@', c['titre'])
            .replace('@@EYEBROW@@', c['eyebrow'])
            .replace('@@CONSIGNE@@', c['consigne'])
            .replace('@@NOTE_PROF@@', c['note_prof'])
            .replace('@@PICTOS@@', json.dumps(PICTOS, ensure_ascii=False))
            .replace('@@CONTENU@@', json.dumps(c, ensure_ascii=False)))


def etat_audio():
    """Qui est prêt à entrer au catalogue, et qui ne l'est pas.

    Un atelier de cette famille sans MP3 est injouable, pas muet. Ce relevé
    est ce qui décide de son inscription dans data/activities.json.
    """
    pret = 0
    for slug, num in ATELIERS:
        f = INTER / slug / 'contenu.json'
        if not f.exists():
            print('  · %-18s : pas de contenu' % slug); continue
        c = json.loads(io.open(f, encoding='utf-8').read())
        manquants = [it for it in c['items'] if not (INTER / slug / it['audio']).exists()]
        if manquants:
            print('  ✗ %-18s (activité %d) : %d extrait(s) manquant(s) sur %d — hors catalogue'
                  % (slug, num, len(manquants), len(c['items'])))
        else:
            print('  ✓ %-18s (activité %d) : %d extraits, prêt pour le catalogue'
                  % (slug, num, len(c['items']))); pret += 1
    print('\n%d atelier(s) sur %d prêt(s).' % (pret, len(ATELIERS)))
    print("Tant qu'un atelier n'est pas prêt, ne l'inscrivez pas dans")
    print("data/activities.json : le banc des exercices libres est toujours")
    print("ouvert, donc l'offrir cassé n'a aucune issue pour l'élève.")
    return 0


def main(argv):
    if '--audio' in argv:
        return etat_audio()
    verifier = '--verifier' in argv
    voulus = [a for a in argv if not a.startswith('--')]
    ecart = 0
    for slug, num in ATELIERS:
        if voulus and not any(v in slug for v in voulus):
            continue
        if not (INTER / slug / 'contenu.json').exists():
            print('  · %-18s (activité %d) : contenu pas encore écrit' % (slug, num))
            continue
        cible = INTER / slug / ('%s-activite-interactive.html' % slug)
        neuf = rendre(slug)
        actuel = io.open(cible, encoding='utf-8').read() if cible.exists() else ''
        if actuel == neuf:
            print('  = %-18s (activité %d) : à jour' % (slug, num))
        elif verifier:
            print('  ≠ %-18s (activité %d) : à regénérer' % (slug, num)); ecart = 1
        else:
            cible.parent.mkdir(parents=True, exist_ok=True)
            io.open(cible, 'w', encoding='utf-8').write(neuf)
            print('  → %-18s (activité %d) : écrit (%d octets)' % (slug, num, len(neuf)))
    return ecart


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
