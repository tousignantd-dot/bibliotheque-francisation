#!/usr/bin/env python3
"""Famille D — écrire et copier. Le seul atelier de la banque où l'élève tape.

Partout ailleurs dans la banque, l'élève **choisit** : il clique une tuile, un
bouton, une lettre. Ici il **produit** — il recopie, caractère par caractère,
ce qu'il a sous les yeux. C'est le savoir `n1-s31` (« orthographier le
vocabulaire courant lié aux situations du cours ») et la moitié de `n1-s32`
(« écrire en lettres détachées », « utiliser les chiffres arabes »).

    python3 build/graphie.py             → réécrit l'atelier
    python3 build/graphie.py --verifier  → dit s'il est à jour, n'écrit rien

N'ÉDITEZ PAS LE HTML PRODUIT. Le contenu vit dans
`assets/interactive/<slug>/contenu.json`.

Ce que l'exercice pardonne, et ce qu'il ne pardonne pas
-------------------------------------------------------
Il **pardonne** les espaces du début et de la fin, et les espaces doubles à
l'intérieur : ce sont des accidents de clavier, pas des fautes de copie.

Il **ne pardonne pas** les accents, la casse ni la ponctuation — et c'est tout
l'objet. Un élève qui écrit « Montreal » sur un formulaire d'inscription voit
sa fiche revenir ; celui qui écrit « h2k 4j8 » aussi. Le jour où il remplit le
vrai formulaire, personne ne corrigera pour lui.

**La rétroaction montre le premier caractère qui diffère**, pas seulement
« c'est faux ». Recopier est une tâche de comparaison : dire *où* ça diverge
est la seule aide qui apprenne quelque chose. Un élève à qui l'on dit
seulement « non » relit son texte en entier et rate le même accent trois fois.
"""
import io
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTER = ROOT / 'assets/interactive'
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from banque import paires_pour, option_niveau  # noqa: E402

# Le nom de la famille dans le registre : c'est par lui que ce fichier
# retrouve ses ateliers, à tous les niveaux.
GENERATEUR = 'graphie'

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
@import url("https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap");

/* ══════════════════════════════════════════════════════════════════════
   Famille D · écrire et copier
   FICHIER GÉNÉRÉ — build/graphie.py. Ne modifiez pas ce HTML.
   ══════════════════════════════════════════════════════════════════════ */
body { --sec: var(--niv-@@NIVEAU@@-line); --sec-soft: var(--niv-@@NIVEAU@@-bg); }

.gr-band { padding: var(--sp-5) 0; }
.gr-band__in { max-width: var(--content-max); margin: 0 auto; padding: 0 var(--gutter);
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--sp-4); }
.gr-band__t { font-size: var(--fs-h2); font-weight: var(--fw-black);
  letter-spacing: var(--ls-title); line-height: var(--lh-title); margin-top: var(--sp-2); }
.gr-band__a { display: flex; flex-wrap: wrap; gap: var(--sp-2); }
.gr-steps__in { max-width: var(--content-max); margin: 0 auto;
  padding: var(--sp-3) var(--gutter); display: flex; flex-wrap: wrap; gap: var(--sp-2); align-items: center; }
.step { font-family: var(--font-sans); cursor: pointer; }
.step[aria-selected="true"] { background: var(--sel-bg); border-color: var(--sel-line); color: var(--sel-ink); }
.gr-wrap { max-width: var(--content-max); margin: 0 auto; padding: var(--sp-8) var(--gutter) var(--sp-12); }
.view { display: none; }
.view.is-on { display: block; }
.gr-lbl { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); margin-bottom: var(--sp-3); }
.gr-barre { padding: var(--sp-3) var(--sp-6); border-bottom: 1px solid var(--border);
  display: flex; align-items: center; gap: var(--sp-4);
  font-size: var(--fs-ui-sm); font-weight: var(--fw-bold); color: var(--text-muted); }
.gr-pied { padding: var(--sp-4) var(--sp-6); border-top: 1px solid var(--border);
  display: flex; flex-wrap: wrap; gap: var(--sp-3); align-items: center; justify-content: space-between; }
.gr-jeu { padding: var(--sp-6); }
.gr-consigne { font-size: var(--fs-body); font-weight: var(--fw-semi); color: var(--text-muted);
  margin-bottom: var(--sp-5); text-align: center; }

/* ── La case du formulaire, telle qu'elle est sur la vraie fiche ─────── */
.gr-case { max-width: 560px; margin: 0 auto var(--sp-5);
  border: 2px solid var(--text-strong); border-radius: var(--r-sm);
  background: var(--surface-card); overflow: hidden; }
.gr-case__l { padding: var(--sp-2) var(--sp-4); background: var(--surface-sunken);
  border-bottom: 1px solid var(--border);
  font-family: var(--font-sans); font-size: var(--fs-label); font-weight: var(--fw-black);
  letter-spacing: var(--ls-label); text-transform: uppercase; color: var(--text-muted); }
.gr-case__v { padding: var(--sp-4) var(--sp-5);
  font-family: "Courier Prime", ui-monospace, "Courier New", monospace;
  font-size: clamp(22px, 2.8vw, 32px); font-weight: 700; letter-spacing: .04em;
  word-break: break-word; }

.gr-flag { text-align: center; font-size: var(--fs-body-sm); color: var(--text-muted);
  margin-bottom: var(--sp-3); }

/* La zone de saisie porte la même police que le modèle : comparer deux
   textes composés différemment est un exercice de plus, et ce n'est pas
   celui-ci. */
.gr-saisie { display: block; width: 100%; max-width: 560px; margin: 0 auto;
  padding: var(--sp-4) var(--sp-5); min-height: var(--tap-min);
  border: 2px solid var(--border); border-radius: var(--r-md);
  background: var(--surface-card); color: var(--text-strong);
  font-family: "Courier Prime", ui-monospace, "Courier New", monospace;
  font-size: clamp(20px, 2.6vw, 30px); font-weight: 700; letter-spacing: .04em; }
.gr-saisie:focus { outline: 2px solid var(--sec); outline-offset: 2px; border-color: var(--sec); }
.gr-saisie.is-ok { border-color: var(--ok-line); background: var(--ok-bg); }
.gr-saisie.is-no { border-color: var(--no-line); background: var(--no-bg); }

/* ── La comparaison caractère par caractère ─────────────────────────── */
.gr-compare { max-width: 560px; margin: var(--sp-5) auto 0;
  font-family: "Courier Prime", ui-monospace, "Courier New", monospace;
  font-size: clamp(18px, 2.2vw, 24px); font-weight: 700; letter-spacing: .04em;
  line-height: 1.9; }
.gr-compare__l { font-family: var(--font-sans); font-size: var(--fs-label);
  font-weight: var(--fw-black); letter-spacing: var(--ls-label); text-transform: uppercase;
  color: var(--text-muted); }
.gr-c { padding: 1px 0; }
.gr-c--ok { color: var(--text-strong); }
/* Le caractère fautif porte un fond ET un soulignement : la couleur ne dit
   jamais l'information seule. */
.gr-c--no { background: var(--no-bg); color: var(--no-line);
  text-decoration: underline; text-decoration-thickness: 3px; }
.gr-c--vide { background: var(--no-bg); color: var(--no-line); }

.gr-aide { margin-top: var(--sp-4); font-size: var(--fs-body-sm); color: var(--text-muted);
  text-align: center; min-height: 24px; }
.gr-retour { margin-top: var(--sp-4); min-height: 28px; text-align: center; }

/* ── La fiche entière, en lecture ───────────────────────────────────── */
.gr-fiche { max-width: 620px; margin: 0 auto; border: 2px solid var(--text-strong);
  border-radius: var(--r-sm); overflow: hidden; }
.gr-ligne { display: grid; grid-template-columns: minmax(120px, 34%) minmax(0, 1fr);
  border-bottom: 1px solid var(--border); }
.gr-ligne:last-child { border-bottom: 0; }
.gr-ligne__l { padding: var(--sp-3) var(--sp-4); background: var(--surface-sunken);
  border-right: 1px solid var(--border);
  font-family: var(--font-sans); font-size: var(--fs-label); font-weight: var(--fw-black);
  letter-spacing: var(--ls-label); text-transform: uppercase; color: var(--text-muted); }
.gr-ligne__v { padding: var(--sp-3) var(--sp-4);
  font-family: "Courier Prime", ui-monospace, "Courier New", monospace;
  font-weight: 700; word-break: break-word; }

.gr-bilan { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: var(--sp-4);
  margin-bottom: var(--sp-6); }
.gr-chiffre { font-size: clamp(30px, 3.4vw, 42px); font-weight: var(--fw-black); line-height: 1; }
.gr-table { width: 100%; border-collapse: collapse; font-size: var(--fs-body-sm); }
.gr-table th, .gr-table td { padding: var(--sp-3) var(--sp-4); border-bottom: 1px solid var(--border);
  text-align: left; }
.gr-table th { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); }
.gr-etat { font-weight: var(--fw-bold); white-space: nowrap; }

.gr-sortie { display: none; position: fixed; top: var(--sp-4); right: var(--sp-4); z-index: 50; }
.is-presentation .gr-band, .is-presentation .gr-steps { display: none; }
.is-presentation .gr-sortie { display: inline-flex; }

@media (max-width: 640px) {
  .gr-band__in, .gr-steps__in, .gr-wrap { padding-left: var(--sp-5); padding-right: var(--sp-5); }
  .gr-bilan { grid-template-columns: 1fr 1fr; }
  .gr-jeu { padding: var(--sp-5) var(--sp-4); }
  .gr-ligne { grid-template-columns: 1fr; }
  .gr-ligne__l { border-right: 0; border-bottom: 1px solid var(--border); }
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

<header class="band gr-band">
  <div class="gr-band__in">
    <div>
      <p class="band__eyebrow">@@EYEBROW@@</p>
      <h1 class="gr-band__t">@@TITRE@@</h1>
    </div>
    <div class="gr-band__a">
      <button type="button" class="btn btn--ghost btn--sm" id="profToggle" aria-pressed="false">Mode enseignant</button>
      <button type="button" class="btn btn--ghost btn--sm" id="presToggle" aria-pressed="false">Présentation</button>
    </div>
  </div>
</header>

<nav class="steps gr-steps" aria-label="Étapes de l'activité">
  <div class="steps__inner gr-steps__in" role="tablist">
    <button type="button" class="step" role="tab" aria-selected="true"  data-vue="vueJeu"><span class="step__dot"></span>Je recopie</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueFiche"><span class="step__dot"></span>Je regarde la fiche</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueMaitrise"><span class="step__dot"></span>Où j'en suis</button>
  </div>
</nav>

<button type="button" class="btn btn--pri btn--sm gr-sortie" id="sortiePres">Quitter la présentation</button>

<main class="gr-wrap" id="app">

  <section class="view is-on" id="vueJeu">
    <div class="card card--flush">
      <div class="gr-barre">
        <span id="score">0 point</span>
        <span id="serie"></span>
        <span id="avance"></span>
      </div>
      <div class="gr-jeu">
        <p class="gr-consigne">@@CONSIGNE@@</p>
        <div class="gr-case">
          <div class="gr-case__l" id="etiquette"></div>
          <div class="gr-case__v" id="modele"></div>
        </div>
        <p class="gr-flag">Écrivez exactement la même chose, ci-dessous.</p>
        <input type="text" class="gr-saisie" id="saisie" autocomplete="off"
               autocapitalize="off" autocorrect="off" spellcheck="false"
               aria-label="Recopiez la valeur ci-dessus">
        <div id="compare"></div>
        <p class="gr-aide" id="aide"></p>
        <div class="gr-retour"><p class="fb" id="retour"></p></div>
      </div>
      <div class="gr-pied">
        <div class="gr-band__a">
          <button type="button" class="btn btn--audio btn--sm" id="ecouter">@@SPEAKER@@Écouter</button>
          <button type="button" class="btn btn--ghost btn--sm" id="verifier">Vérifier</button>
        </div>
        <button type="button" class="btn btn--pri btn--sm" id="suivantJeu">Suivant</button>
      </div>
    </div>
  </section>

  <section class="view" id="vueFiche">
    <p class="gr-lbl">@@FICHE_TITRE@@</p>
    <div class="gr-fiche" id="fiche"></div>
  </section>

  <section class="view" id="vueMaitrise">
    <div class="gr-bilan">
      <div class="card"><p class="gr-lbl">Points</p><p class="gr-chiffre" id="bXp">0</p></div>
      <div class="card"><p class="gr-lbl">Série</p><p class="gr-chiffre" id="bSerie">0</p></div>
      <div class="card"><p class="gr-lbl">Meilleure série</p><p class="gr-chiffre" id="bMeilleure">0</p></div>
      <div class="card"><p class="gr-lbl">Sûres</p><p class="gr-chiffre" id="bSurs">0</p></div>
    </div>
    <div class="card card--flush">
      <table class="gr-table">
        <thead><tr><th>Case</th><th>Ce qu'il faut écrire</th><th>Où j'en suis</th></tr></thead>
        <tbody id="corpsTable"></tbody>
      </table>
    </div>
    <p style="margin-top:var(--sp-5)">
      <button type="button" class="btn btn--ghost btn--sm" id="resetMaitrise">Tout recommencer</button>
    </p>
  </section>

  <aside class="card" id="panneauProf" style="display:none;margin-top:var(--sp-6)">
    <p class="gr-lbl">Mode enseignant</p>
    @@NOTE_PROF@@
    <p><strong>Ce que l'exercice pardonne</strong> : les espaces du début et de
    la fin, et les espaces doubles à l'intérieur. Ce sont des accidents de
    clavier, pas des fautes de copie.</p>
    <p><strong>Ce qu'il ne pardonne pas</strong> : les accents, les majuscules
    et la ponctuation. C'est tout l'objet. « Montreal » sur un formulaire
    d'inscription fait revenir la fiche, et le jour où l'élève remplit la
    vraie, personne ne corrigera pour lui.</p>
    <p><strong>La rétroaction montre le premier caractère qui diffère</strong>,
    et pas seulement « c'est faux ». Recopier est une tâche de comparaison :
    dire <em>où</em> ça diverge est la seule aide qui apprenne quelque chose.
    Un élève à qui l'on dit juste « non » relit tout et rate le même accent
    trois fois de suite.</p>
  </aside>

</main>

<script>
const CONTENU = @@CONTENU@@;
const items = CONTENU.items;
const CLE = CONTENU.cle;

const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

/* Ce qui est pardonné se décide ici, une fois. */
function normaliser(s){ return String(s).trim().replace(/\s+/g, ' '); }

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
    return '<tr><td><strong>' + esc(x.etiquette) + '</strong></td><td>' + esc(x.valeur) + '</td>'
      + '<td class="gr-etat"><span aria-hidden="true">' + glyphe + '</span> ' + mot + '</td></tr>';
  }).join('');
}

/* ── Le tour ────────────────────────────────────────────────────────── */
let rang = 0, repondu = false;
function courant(){ return items[rang % items.length]; }

function rendre(){
  const x = courant();
  $('#etiquette').textContent = x.etiquette;
  $('#modele').textContent = x.valeur;
  $('#avance').textContent = (rang % items.length + 1) + ' / ' + items.length;
  $('#ecouter').style.display = x.audio ? '' : 'none';
  $('#saisie').disabled = repondu;
  $('#verifier').style.display = repondu ? 'none' : '';
}

function nouveauTour(){
  repondu = false;
  $('#saisie').value = '';
  $('#saisie').className = 'gr-saisie';
  $('#compare').innerHTML = '';
  $('#retour').textContent = ''; $('#retour').className = 'fb';
  $('#aide').textContent = '';
  rendre();
  $('#saisie').focus();
}

/* La comparaison caractère par caractère, sur les chaînes normalisées. On
   marque tout ce qui diffère, pas seulement le premier écart : l'élève voit
   d'un coup si c'est un accent isolé ou une fin de mot entière. */
function comparer(attendu, ecrit){
  const a = [...attendu], b = [...ecrit];
  const n = Math.max(a.length, b.length);
  let out = '', premier = -1;
  for (let i = 0; i < n; i++) {
    const ca = a[i], cb = b[i];
    if (cb === undefined) { out += '<span class="gr-c gr-c--vide">_</span>'; if (premier < 0) premier = i; }
    else if (ca === cb) out += '<span class="gr-c gr-c--ok">' + esc(cb === ' ' ? ' ' : cb) + '</span>';
    else { out += '<span class="gr-c gr-c--no">' + esc(cb === ' ' ? ' ' : cb) + '</span>'; if (premier < 0) premier = i; }
  }
  return { html: out, premier: premier };
}

function verifier(){
  if (repondu) return;
  const x = courant();
  const attendu = normaliser(x.valeur), ecrit = normaliser($('#saisie').value);
  if (!ecrit) return;   // rien à juger : on ne punit pas une case vide
  repondu = true;
  const juste = ecrit === attendu;
  const i = rang % items.length;

  $('#saisie').className = 'gr-saisie ' + (juste ? 'is-ok' : 'is-no');
  const retour = $('#retour');
  retour.className = 'fb ' + (juste ? 'fb--ok' : 'fb--no');

  if (juste) {
    retour.textContent = 'Juste, caractère par caractère.';
    $('#compare').innerHTML = '';
  } else {
    const c = comparer(attendu, ecrit);
    retour.textContent = 'Regardez le caractère ' + (c.premier + 1) + '.';
    $('#compare').innerHTML =
      '<p class="gr-compare__l">Ce que vous avez écrit</p>'
      + '<div class="gr-compare">' + c.html + '</div>'
      + '<p class="gr-compare__l" style="margin-top:var(--sp-4)">Ce qu\'il fallait écrire</p>'
      + '<div class="gr-compare">' + esc(attendu).replace(/ /g, '&nbsp;') + '</div>';
  }
  $('#aide').textContent = x.aide || '';
  ajouter(i, juste ? 10 : -3);
  rendre();
  lmsTrack('exercise_attempted', { correct: juste ? 1 : 0 });
}

$('#verifier').onclick = verifier;
$('#saisie').addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); verifier(); } });
$('#suivantJeu').onclick = () => { rang++; nouveauTour(); };
$('#ecouter').onclick = () => jouer(courant().audio, $('#ecouter'));

function rendreFiche(){
  $('#fiche').innerHTML = items.map(x =>
    '<div class="gr-ligne"><div class="gr-ligne__l">' + esc(x.etiquette) + '</div>'
    + '<div class="gr-ligne__v">' + esc(x.valeur) + '</div></div>').join('');
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
rendreFiche();
rendreMaitrise();
lmsTrack('file_opened');
</script>
</body>
</html>
'''

CHAMPS = {'slug', 'titre', 'eyebrow', 'cle', 'consigne', 'fiche_titre', 'note_prof',
          'savoirs', 'items'}


def controler(slug, c):
    manquants = CHAMPS - set(c)
    if manquants:
        sys.exit('!! %s : champs manquants — %s' % (slug, ', '.join(sorted(manquants))))
    if c['slug'] != slug:
        sys.exit('!! %s : le slug du contenu dit « %s »' % (slug, c['slug']))
    vus = set()
    for it in c['items']:
        s = it.get('slug')
        if not s or s in vus:
            sys.exit('!! %s : slug d\'item manquant ou en double — %r' % (slug, s))
        vus.add(s)
        for champ in ('etiquette', 'valeur'):
            if not it.get(champ):
                sys.exit('!! %s / %s : pas de %s' % (slug, s, champ))
        # Une valeur qui se normalise autrement qu'elle-même serait
        # impossible à recopier exactement : l'élève taperait juste et se
        # ferait refuser sur un espace qu'il ne voit pas.
        nette = ' '.join(it['valeur'].split())
        if nette != it['valeur'].strip():
            sys.exit('!! %s / %s : la valeur porte des espaces doubles — %r'
                     % (slug, s, it['valeur']))


def rendre(slug):
    fichier = INTER / slug / 'contenu.json'
    if not fichier.exists():
        sys.exit('!! %s introuvable' % fichier)
    c = json.loads(io.open(fichier, encoding='utf-8').read())
    controler(slug, c)
    return (GABARIT
            .replace('@@SPEAKER@@', SPEAKER)
            .replace('@@NIVEAU@@', str(c['niveau']))
            .replace('@@TITRE@@', c['titre'])
            .replace('@@EYEBROW@@', c['eyebrow'])
            .replace('@@CONSIGNE@@', c['consigne'])
            .replace('@@FICHE_TITRE@@', c['fiche_titre'])
            .replace('@@NOTE_PROF@@', c['note_prof'])
            .replace('@@CONTENU@@', json.dumps(c, ensure_ascii=False)))


def main(argv):
    niveau, argv = option_niveau(argv)
    verifier = '--verifier' in argv
    ecart = 0
    for slug, num in paires_pour(GENERATEUR, niveau):
        if not (INTER / slug / 'contenu.json').exists():
            print('  · %-18s (activité %s) : contenu pas encore écrit' % (slug, num))
            continue
        cible = INTER / slug / ('%s-activite-interactive.html' % slug)
        neuf = rendre(slug)
        actuel = io.open(cible, encoding='utf-8').read() if cible.exists() else ''
        if actuel == neuf:
            print('  = %-18s (activité %s) : à jour' % (slug, num))
        elif verifier:
            print('  ≠ %-18s (activité %s) : à regénérer' % (slug, num)); ecart = 1
        else:
            cible.parent.mkdir(parents=True, exist_ok=True)
            io.open(cible, 'w', encoding='utf-8').write(neuf)
            print('  → %-18s (activité %s) : écrit (%d octets)' % (slug, num, len(neuf)))
    return ecart


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
