#!/usr/bin/env python3
"""Famille C — construire une phrase. Un générateur, deux modes, sept ateliers.

La forme : **des morceaux à mettre en place**, et jamais plus de sept mots.
C'est la longueur de phrase du niveau 1, et c'est aussi la limite au-delà de
laquelle un débutant manipule des tuiles sans plus lire ce qu'il compose.

    python3 build/phrase.py             → réécrit les sept ateliers
    python3 build/phrase.py possessifs  → seulement celui-là
    python3 build/phrase.py --verifier  → dit qui est à jour, n'écrit rien

N'ÉDITEZ PAS LE HTML PRODUIT : le prochain passage l'écraserait. Le contenu
vit dans `assets/interactive/<slug>/contenu.json`, dont le contrat est écrit
dans `docs/schemas-banque-n1.md`.

Les deux modes
--------------
`ordre` — la phrase est en tuiles mélangées, l'élève les remet en place.
`choix` — la phrase a un trou, l'élève choisit parmi deux à quatre réponses.

Pourquoi `syllabes-n1` est ici et pas dans une famille à lui
------------------------------------------------------------
Assembler `ma` + `ti` + `n` pour faire « matin » est exactement le mode
`ordre`, à un niveau plus bas : des morceaux, un ordre, une seule bonne
réponse. Le plan prévoyait un générateur `graphie.py` pour toute la famille D ;
deux de ses quatre exercices sont retombés dans des formes qui existaient
déjà — les syllabes ici, les lettres majuscule/minuscule dans
`build/appariement.py`. Trois générateurs suffisent donc là où le plan en
annonçait quatre, et c'est une meilleure nouvelle qu'un générateur de plus.

Le contrôle qui compte
----------------------
En mode `choix`, `avant` + `ok` + `apres` doit redonner `phrase` **exactement**.
Sans ce contrôle au build, un espace en trop passe inaperçu et l'élève voit une
phrase corrigée qui ne ressemble pas à celle qu'il vient de composer.
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
GENERATEUR = 'phrase'

# Les ateliers de la famille. Le numéro est réservé dans
# docs/deux-agents-en-parallele.md ; il ne sert pas au build.

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
   Famille C · construire une phrase
   FICHIER GÉNÉRÉ — build/phrase.py. Ne modifiez pas ce HTML.
   Aucune couleur en dur : uniquement des jetons du système de design.
   Le repérage est celui du niveau 1 — framboise.
   ══════════════════════════════════════════════════════════════════════ */
body { --sec: var(--niv-@@NIVEAU@@-line); --sec-soft: var(--niv-@@NIVEAU@@-bg); }

.ph-band { padding: var(--sp-5) 0; }
.ph-band__in { max-width: var(--content-max); margin: 0 auto; padding: 0 var(--gutter);
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--sp-4); }
.ph-band__t { font-size: var(--fs-h2); font-weight: var(--fw-black);
  letter-spacing: var(--ls-title); line-height: var(--lh-title); margin-top: var(--sp-2); }
.ph-band__a { display: flex; flex-wrap: wrap; gap: var(--sp-2); }

.ph-steps__in { max-width: var(--content-max); margin: 0 auto;
  padding: var(--sp-3) var(--gutter); display: flex; flex-wrap: wrap; gap: var(--sp-2); align-items: center; }
.step { font-family: var(--font-sans); cursor: pointer; }
.step[aria-selected="true"] { background: var(--sel-bg); border-color: var(--sel-line); color: var(--sel-ink); }

.ph-wrap { max-width: var(--content-max); margin: 0 auto; padding: var(--sp-8) var(--gutter) var(--sp-12); }
.view { display: none; }
.view.is-on { display: block; }

.ph-lbl { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); margin-bottom: var(--sp-3); }
.ph-barre { padding: var(--sp-3) var(--sp-6); border-bottom: 1px solid var(--border);
  display: flex; align-items: center; gap: var(--sp-4);
  font-size: var(--fs-ui-sm); font-weight: var(--fw-bold); color: var(--text-muted); }
.ph-pied { padding: var(--sp-4) var(--sp-6); border-top: 1px solid var(--border);
  display: flex; flex-wrap: wrap; gap: var(--sp-3); align-items: center; justify-content: space-between; }

/* ── L'aire de composition ──────────────────────────────────────────── */
.ph-jeu { padding: var(--sp-6); }
.ph-consigne { font-size: var(--fs-body); font-weight: var(--fw-semi); color: var(--text-muted);
  margin-bottom: var(--sp-5); text-align: center; }

/* La ligne où la phrase se construit. Elle garde sa hauteur même vide :
   sinon la page saute d'un cran à chaque tuile posée, et l'élève de niveau 1
   perd le fil de ce qu'il vient de faire. */
.ph-ligne { min-height: 92px; display: flex; flex-wrap: wrap; gap: var(--sp-2);
  align-items: center; justify-content: center;
  padding: var(--sp-4); border: 2px dashed var(--border); border-radius: var(--r-md);
  background: var(--surface-sunken); margin-bottom: var(--sp-5); }
.ph-ligne.is-ok { border-style: solid; border-color: var(--ok-line); background: var(--ok-bg); }
.ph-ligne.is-no { border-style: solid; border-color: var(--no-line); background: var(--no-bg); }
.ph-vide { font-size: var(--fs-body-sm); color: var(--text-muted); font-style: italic; }

.ph-banc { display: flex; flex-wrap: wrap; gap: var(--sp-3); align-items: center; justify-content: center;
  min-height: 72px; }

.ph-tuile { font-family: var(--font-sans); font-size: clamp(19px, 2.2vw, 26px);
  font-weight: var(--fw-bold); line-height: 1.2;
  padding: var(--sp-3) var(--sp-5); min-height: var(--tap-min);
  border: 1px solid var(--border); border-radius: var(--r-md); background: var(--surface-card);
  color: var(--text-strong); cursor: pointer; white-space: nowrap;
  transition: background var(--dur) var(--ease), border-color var(--dur) var(--ease),
              transform var(--dur) var(--ease); }
.ph-tuile:hover:not(:disabled) { background: var(--paper-100); border-color: var(--sec); }
.ph-tuile:disabled { opacity: .35; cursor: default; }
.ph-tuile--posee { background: var(--sel-bg); border-color: var(--sel-line); color: var(--sel-ink); }

/* ── Mode « choix » : la phrase à trou ──────────────────────────────── */
.ph-phrase { font-family: var(--font-sans); font-size: clamp(22px, 2.8vw, 34px);
  font-weight: var(--fw-bold); line-height: 1.45; text-align: center;
  margin-bottom: var(--sp-5); }
.ph-trou { display: inline-block; min-width: 112px; padding: 0 var(--sp-3);
  border-bottom: 3px solid var(--sec); color: var(--sec); }
.ph-trou.is-vide { color: var(--text-muted); }

.ph-choix { display: flex; flex-wrap: wrap; gap: var(--sp-3); justify-content: center; }
.ph-choix .ph-tuile.is-ok { border-color: var(--ok-line); background: var(--ok-bg); }
.ph-choix .ph-tuile.is-no { border-color: var(--no-line); background: var(--no-bg); }

.ph-sens { margin-top: var(--sp-4); font-size: var(--fs-body-sm); color: var(--text-muted);
  text-align: center; min-height: 24px; }
.ph-retour { margin-top: var(--sp-4); min-height: 28px; text-align: center; }

/* ── Je regarde : le banc de modèles ────────────────────────────────── */
.ph-modeles { display: grid; grid-template-columns: repeat(auto-fit, minmax(272px, 1fr)); gap: var(--sp-4); }
.ph-modele { padding: var(--sp-5); border: 1px solid var(--border); border-radius: var(--r-md);
  background: var(--surface-card); display: flex; flex-direction: column; gap: var(--sp-3); }
.ph-modele__p { font-family: var(--font-sans); font-size: clamp(19px, 2vw, 24px);
  font-weight: var(--fw-bold); line-height: 1.3; }
.ph-modele__s { font-size: var(--fs-body-sm); color: var(--text-muted); }
.ph-modele__a { align-self: flex-start; }

/* ── Où j'en suis ───────────────────────────────────────────────────── */
.ph-bilan { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: var(--sp-4);
  margin-bottom: var(--sp-6); }
.ph-chiffre { font-size: clamp(30px, 3.4vw, 42px); font-weight: var(--fw-black); line-height: 1; }
.ph-table { width: 100%; border-collapse: collapse; font-size: var(--fs-body-sm); }
.ph-table th, .ph-table td { padding: var(--sp-3) var(--sp-4); border-bottom: 1px solid var(--border);
  text-align: left; }
.ph-table th { font-size: var(--fs-label); font-weight: var(--fw-black); letter-spacing: var(--ls-label);
  text-transform: uppercase; color: var(--text-muted); }
.ph-etat { font-weight: var(--fw-bold); white-space: nowrap; }

.ph-sortie { display: none; position: fixed; top: var(--sp-4); right: var(--sp-4); z-index: 50; }
.is-presentation .ph-band, .is-presentation .ph-steps { display: none; }
.is-presentation .ph-sortie { display: inline-flex; }
.is-presentation .ph-tuile { font-size: clamp(26px, 3vw, 38px); }
.is-presentation .ph-phrase { font-size: clamp(30px, 4vw, 48px); }

@media (max-width: 640px) {
  .ph-band__in, .ph-steps__in, .ph-wrap { padding-left: var(--sp-5); padding-right: var(--sp-5); }
  .ph-bilan { grid-template-columns: 1fr 1fr; }
  .ph-jeu { padding: var(--sp-5) var(--sp-4); }
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

<header class="band ph-band">
  <div class="ph-band__in">
    <div>
      <p class="band__eyebrow">@@EYEBROW@@</p>
      <h1 class="ph-band__t">@@TITRE@@</h1>
    </div>
    <div class="ph-band__a">
      <button type="button" class="btn btn--ghost btn--sm" id="profToggle" aria-pressed="false">Mode enseignant</button>
      <button type="button" class="btn btn--ghost btn--sm" id="presToggle" aria-pressed="false">Présentation</button>
    </div>
  </div>
</header>

<nav class="steps ph-steps" aria-label="Étapes de l'activité">
  <div class="steps__inner ph-steps__in" role="tablist">
    <button type="button" class="step" role="tab" aria-selected="true"  data-vue="vueJeu"><span class="step__dot"></span>@@ETAPE1@@</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueModeles"><span class="step__dot"></span>Je regarde les modèles</button>
    <button type="button" class="step" role="tab" aria-selected="false" data-vue="vueMaitrise"><span class="step__dot"></span>Où j'en suis</button>
  </div>
</nav>

<button type="button" class="btn btn--pri btn--sm ph-sortie" id="sortiePres">Quitter la présentation</button>

<main class="ph-wrap" id="app">

  <section class="view is-on" id="vueJeu">
    <div class="card card--flush">
      <div class="ph-barre">
        <span id="score">0 point</span>
        <span id="serie"></span>
        <span id="avance"></span>
      </div>
      <div class="ph-jeu">
        <p class="ph-consigne">@@CONSIGNE@@</p>
        <div id="aire"></div>
        <p class="ph-sens" id="sens"></p>
        <div class="ph-retour"><p class="fb" id="retour"></p></div>
      </div>
      <div class="ph-pied">
        <div class="ph-band__a">
          <button type="button" class="btn btn--audio btn--sm" id="ecouter">@@SPEAKER@@Écouter</button>
          <button type="button" class="btn btn--ghost btn--sm" id="effacer">Effacer</button>
        </div>
        <button type="button" class="btn btn--pri btn--sm" id="suivantJeu">Suivant</button>
      </div>
    </div>
  </section>

  <section class="view" id="vueModeles">
    <p class="ph-lbl">Les phrases de cet atelier</p>
    <div class="ph-modeles" id="modeles"></div>
  </section>

  <section class="view" id="vueMaitrise">
    <div class="ph-bilan">
      <div class="card"><p class="ph-lbl">Points</p><p class="ph-chiffre" id="bXp">0</p></div>
      <div class="card"><p class="ph-lbl">Série</p><p class="ph-chiffre" id="bSerie">0</p></div>
      <div class="card"><p class="ph-lbl">Meilleure série</p><p class="ph-chiffre" id="bMeilleure">0</p></div>
      <div class="card"><p class="ph-lbl">Sûres</p><p class="ph-chiffre" id="bSurs">0</p></div>
    </div>
    <div class="card card--flush">
      <table class="ph-table">
        <thead><tr><th>Phrase</th><th>Ce que ça dit</th><th>Où j'en suis</th></tr></thead>
        <tbody id="corpsTable"></tbody>
      </table>
    </div>
    <p style="margin-top:var(--sp-5)">
      <button type="button" class="btn btn--ghost btn--sm" id="resetMaitrise">Tout recommencer</button>
    </p>
  </section>

  <aside class="card" id="panneauProf" style="display:none;margin-top:var(--sp-6)">
    <p class="ph-lbl">Mode enseignant</p>
    @@NOTE_PROF@@
    <p><strong>Les tuiles ne se traînent pas, elles se cliquent.</strong> Le
    glisser-déposer demande une motricité fine à la souris que tous les élèves
    n'ont pas, et il est franchement pénible au doigt sur une tablette. Un
    clic pose la tuile, un autre la reprend.</p>
    <p><strong>Une phrase fausse n'est jamais effacée toute seule.</strong>
    L'élève la voit à côté de la bonne, le temps qu'il veut. C'est là que la
    leçon se fait — pas au moment du clic.</p>
  </aside>

</main>

<script>
const CONTENU = @@CONTENU@@;
const items = CONTENU.items;
const MODE = CONTENU.mode;
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
    return '<tr><td><strong>' + esc(x.phrase) + '</strong></td><td>' + esc(x.sens || '') + '</td>'
      + '<td class="ph-etat"><span aria-hidden="true">' + glyphe + '</span> ' + mot + '</td></tr>';
  }).join('');
}

/* ── L'ordre de passage ─────────────────────────────────────────────── */
/* Les phrases défilent dans un ordre mélangé une fois pour toutes, plutôt
   qu'au hasard à chaque tour : sans ça, l'élève retombe trois fois sur la
   même et n'en voit jamais d'autres. */
let ordre = melanger(items.map((_, i) => i));
let rang = 0, courant = null, iCourant = 0, repondu = false;

function itemCourant(){
  iCourant = ordre[rang % ordre.length];
  courant = items[iCourant];
  return courant;
}

/* ── Mode « ordre » : les tuiles ────────────────────────────────────── */
let posees = [];

function rendreOrdre(){
  const x = courant;
  const restantes = x.mots.map((m, i) => ({ m, i })).filter(t => !posees.includes(t.i));
  $('#aire').innerHTML =
    '<div class="ph-ligne" id="ligne"></div><div class="ph-banc" id="banc"></div>';

  const ligne = $('#ligne');
  if (!posees.length) {
    ligne.innerHTML = '<span class="ph-vide">Cliquez les mots, dans le bon ordre.</span>';
  } else {
    posees.forEach((idx, pos) => {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'ph-tuile ph-tuile--posee';
      b.textContent = x.mots[idx];
      b.disabled = repondu;
      b.onclick = () => { posees.splice(pos, 1); rendreOrdre(); };
      ligne.appendChild(b);
    });
  }
  if (repondu) ligne.classList.add(estJuste() ? 'is-ok' : 'is-no');

  const banc = $('#banc');
  melangeStable(restantes).forEach(t => {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'ph-tuile';
    b.textContent = t.m;
    b.disabled = repondu;
    b.onclick = () => {
      posees.push(t.i);
      if (posees.length === x.mots.length) verifier();
      else rendreOrdre();
    };
    banc.appendChild(b);
  });
}

/* Le banc garde le même désordre tant qu'on est sur la même phrase : le
   remélanger à chaque tuile posée ferait danser les mots sous le doigt. */
let melangeCourant = [];
function melangeStable(restantes){
  return restantes.slice().sort((a, b) => melangeCourant.indexOf(a.i) - melangeCourant.indexOf(b.i));
}

/* La justesse se juge sur les MOTS composés, jamais sur l'ordre des tuiles.
   « J'ai un stylo et un livre » porte deux tuiles « un » : comparer les
   indices y refuse une phrase parfaitement juste, selon laquelle des deux
   l'élève a cliquée en premier. C'est le contrôle du build qui a signalé le
   cas — en refusant le contenu, alors que c'était la méthode qui était
   fausse. */
function estJuste(){
  if (posees.length !== courant.mots.length) return false;
  return posees.map(i => courant.mots[i]).join(' ') === courant.mots.join(' ');
}

/* ── Mode « choix » : la phrase à trou ──────────────────────────────── */
let choisi = null;

function rendreChoix(){
  const x = courant;
  const rempli = choisi !== null ? esc(choisi) : '?';
  $('#aire').innerHTML =
    '<p class="ph-phrase">' + esc(x.avant || '')
    + '<span class="ph-trou' + (choisi === null ? ' is-vide' : '') + '">' + rempli + '</span>'
    + esc(x.apres || '') + '</p>'
    + '<div class="ph-choix" id="choix"></div>';
  const zone = $('#choix');
  melangeCourant.forEach(c => {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'ph-tuile';
    b.textContent = c;
    b.disabled = repondu;
    if (repondu && c === x.ok) b.classList.add('is-ok');
    if (repondu && c === choisi && c !== x.ok) b.classList.add('is-no');
    b.onclick = () => { choisi = c; verifier(); };
    zone.appendChild(b);
  });
}

/* ── Le tour ────────────────────────────────────────────────────────── */
/* Ne touche PAS à la rétroaction : `verifier()` la pose, puis rappelle
   `rendreJeu()` pour griser les tuiles. Une remise à zéro ici effaçait le
   retour dans la milliseconde qui suivait — l'élève ne voyait jamais si
   c'était juste. Le nettoyage appartient à `nouveauTour()`. */
function rendreJeu(){
  $('#avance').textContent = (rang % items.length + 1) + ' / ' + items.length;
  $('#ecouter').style.display = courant.audio ? '' : 'none';
  $('#effacer').style.display = (MODE === 'ordre' && !repondu) ? '' : 'none';
  if (MODE === 'ordre') rendreOrdre(); else rendreChoix();
}

function nouveauTour(){
  itemCourant();
  repondu = false; posees = []; choisi = null;
  $('#retour').textContent = ''; $('#retour').className = 'fb';
  $('#sens').textContent = '';
  melangeCourant = MODE === 'ordre'
    ? melanger(courant.mots.map((_, i) => i))
    : melanger(courant.choix.slice());
  rendreJeu();
}

function verifier(){
  repondu = true;
  const juste = MODE === 'ordre' ? estJuste() : choisi === courant.ok;
  const retour = $('#retour');
  if (juste) {
    retour.className = 'fb fb--ok';
    retour.textContent = 'Juste. ' + courant.phrase;
    ajouter(iCourant, 10);
    jouer(courant.audio, $('#ecouter'));
  } else {
    retour.className = 'fb fb--no';
    retour.textContent = 'On dit : ' + courant.phrase;
    ajouter(iCourant, -3);
  }
  $('#sens').textContent = courant.sens || '';
  rendreJeu();
  lmsTrack('exercise_attempted', { correct: juste ? 1 : 0 });
}

$('#suivantJeu').onclick = () => { rang++; nouveauTour(); };
$('#effacer').onclick = () => { posees = []; rendreOrdre(); };
$('#ecouter').onclick = () => jouer(courant.audio, $('#ecouter'));

/* ── Je regarde les modèles ─────────────────────────────────────────── */
function rendreModeles(){
  $('#modeles').innerHTML = items.map((x, i) =>
    '<div class="ph-modele"><p class="ph-modele__p">' + esc(x.phrase) + '</p>'
    + '<p class="ph-modele__s">' + esc(x.sens || '') + '</p>'
    + (x.audio ? '<button type="button" class="btn btn--audio btn--sm ph-modele__a" data-i="' + i
        + '">@@SPEAKER@@Écouter</button>' : '')
    + '</div>').join('');
  $$('.ph-modele__a').forEach(b => b.onclick = () => jouer(items[b.dataset.i].audio, b));
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
rendreModeles();
rendreMaitrise();
lmsTrack('file_opened');
</script>
</body>
</html>
'''

COMMUNS = {'slug', 'niveau', 'generateur', 'titre', 'eyebrow', 'cle', 'consigne',
           'note_prof', 'savoirs', 'mode', 'items'}


def controler(slug, c):
    """Ce que le build refuse de laisser passer.

    Les trois contrôles ci-dessous attrapent des fautes qui ne lèvent aucune
    erreur : l'exercice s'affiche, et c'est l'élève qui découvre qu'il est
    injouable. C'est la leçon de l'`imgmatch` mort de `CLAUDE.md`.
    """
    manquants = COMMUNS - set(c)
    if manquants:
        sys.exit('!! %s : champs manquants — %s' % (slug, ', '.join(sorted(manquants))))
    if c['slug'] != slug:
        sys.exit('!! %s : le slug du contenu dit « %s »' % (slug, c['slug']))
    if c['mode'] not in ('ordre', 'choix'):
        sys.exit('!! %s : mode inconnu « %s »' % (slug, c['mode']))

    vus = set()
    for it in c['items']:
        s = it.get('slug')
        if not s or s in vus:
            sys.exit('!! %s : slug d\'item manquant ou en double — %r' % (slug, s))
        vus.add(s)
        if not it.get('phrase'):
            sys.exit('!! %s / %s : pas de phrase' % (slug, s))

        if c['mode'] == 'ordre':
            mots = it.get('mots') or []
            # La limite de tuiles suit le niveau : sept mots sont la phrase du
            # débutant et la limite au-delà de laquelle il manipule des tuiles
            # sans plus lire ce qu'il compose. Un élève du niveau 5 lit ce
            # qu'il compose bien plus loin.
            haut = 7 if c['niveau'] <= 2 else (10 if c['niveau'] <= 4 else 12)
            if not 2 <= len(mots) <= haut:
                sys.exit('!! %s / %s : %d tuiles — le niveau %d en veut de 2 à %d'
                         % (slug, s, len(mots), c['niveau'], haut))
            # Pas de refus des tuiles identiques : « J'ai un stylo et un
            # livre » en porte deux, et c'est une phrase du niveau. Le moteur
            # juge sur les mots composés, pas sur l'ordre des tuiles — il
            # accepte donc les deux façons de la cliquer. La première version
            # comparait les indices et refusait cette phrase-là ; le contrôle
            # a été retiré en même temps que la cause.
        else:
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
            # Le contrôle qui compte : la phrase reconstituée doit être celle
            # qu'on montre en correction, à l'espace près.
            recompose = (it.get('avant') or '') + it['ok'] + (it.get('apres') or '')
            if recompose != it['phrase']:
                sys.exit('!! %s / %s : avant+ok+apres ne redonne pas la phrase\n'
                         '   composé : %r\n   attendu : %r' % (slug, s, recompose, it['phrase']))


def rendre(slug):
    fichier = INTER / slug / 'contenu.json'
    if not fichier.exists():
        sys.exit('!! %s introuvable' % fichier)
    c = json.loads(io.open(fichier, encoding='utf-8').read())
    controler(slug, c)
    etape1 = 'Je remets en ordre' if c['mode'] == 'ordre' else 'Je choisis'
    return (GABARIT
            .replace('@@SPEAKER@@', SPEAKER)
            .replace('@@NIVEAU@@', str(c['niveau']))
            .replace('@@TITRE@@', c['titre'])
            .replace('@@EYEBROW@@', c['eyebrow'])
            .replace('@@CONSIGNE@@', c['consigne'])
            .replace('@@ETAPE1@@', etape1)
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
