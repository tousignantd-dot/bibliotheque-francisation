#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Les fiches élèves **avec la théorie du « En apprendre plus »**.

    python3 build/fiches_plus.py            # le niveau 6, au complet
    python3 build/fiches_plus.py --releve   # ce qui serait fait, sans écrire

Pourquoi ce fichier existe
--------------------------
Une fiche de séance porte la théorie de **sa** séance, et rien d'autre. La
mini-leçon — ce que le module explique à l'écran quand on clique « Ouvrir la
mini-leçon » — vit uniquement dans le module interactif. Sur papier, elle
n'existe que dans le manuel relié (`build/manuel_eleve.py`), en section à la
fin de chaque module, et seulement pour le niveau 4.

Ce script produit une **seconde série** de fiches où la mini-leçon descend
dans la fiche de sa séance. C'est un essai destiné à être comparé à l'autre,
en classe, avec un enseignant.

**Il n'écrit jamais dans `assets/documents/`.** La série d'origine ne bouge
pas : les fiches d'essai sortent dans `assets/documents/plus/`, sous le même
nom. Les sommaires suivent, et leurs liens — relatifs, entre voisins — pointent
donc d'eux-mêmes vers les fiches d'essai.

Comment on sait quelle mini-leçon va sur quelle fiche
------------------------------------------------------
On ne le devine pas : **chaque deck le dit déjà**. `decks/<slug>/a2.py` porte
en tête « Source : exercice `prGraphie` et sa mini-leçon », et `plus.js` est
justement indexé par ces identifiants d'exercice. Le rattachement est donc lu
dans le dépôt, pas inventé — et il est bon : 158 rattachements pour 151
mini-leçons distinctes sur 152, une seule orpheline.

Une mini-leçon nommée par deux fiches est posée sur les deux (7 cas sur 158) :
deux séances qui travaillent le même exercice méritent la même explication, et
la fiche doit se tenir seule — c'est une feuille volante, pas un chapitre.

La mise en page est celle du manuel
------------------------------------
`bloc_html()` de `build/manuel_eleve.py` est réemployé tel quel : ce qui
s'écoute à l'écran y est déjà devenu une phrase écrite, ce qui se clique un
tableau. En écrire une seconde version aurait donné deux mises en page d'une
même chose, qui divergeraient au premier correctif.

Son CSS est **porté sous `.plus-papier`** plutôt que recopié à plat : la fiche
et le manuel partagent des noms de classe (`.card`, `.note`, `.k`, `.cle`), et
un CSS à plat aurait repeint des blocs de la fiche d'origine. Les huit
variables de couleur, elles, portent les mêmes noms dans les deux feuilles et
n'ont rien demandé.
"""
import argparse
import glob
import importlib.util
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
DOCUMENTS = os.path.join(RACINE, 'assets', 'documents')
SORTIE = os.path.join(DOCUMENTS, 'plus')
DECKS = os.path.join(ICI, 'powerpoints', 'decks')

sys.path.insert(0, os.path.join(ICI, 'powerpoints'))


def _charger_manuel():
    """`manuel_eleve.py` n'est pas un paquet : on le charge par son chemin."""
    spec = importlib.util.spec_from_file_location(
        'manuel_eleve', os.path.join(ICI, 'manuel_eleve.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Le CSS des mini-leçons, repris de `manuel_eleve.CSS` et porté sous
# `.plus-papier`. Il ne définit aucune couleur : les huit variables
# (`--ink`, `--line`, `--muted`, `--tint`, `--soft`, `--rule`) existent déjà
# dans la fiche, sous les mêmes noms et avec les mêmes valeurs.
CSS_PLUS = """
/* ── « En apprendre plus », descendu dans la fiche ────────────────────
   Porté sous .plus-papier : la fiche a ses propres .card, .note, .k et
   .cle, et un CSS à plat aurait repeint ses blocs. */
.plus-papier{margin-top:10px; border-top:2.5px solid var(--rule); padding-top:9px}
.plus-papier > .lbl{font-size:9.5pt; font-weight:800; text-transform:uppercase;
  letter-spacing:.1em; color:var(--muted); margin-bottom:6px}
.plus-papier > .chapeau{font-weight:600; color:var(--soft); margin-bottom:9px;
  font-size:10.5pt}
.plus-papier .ml{margin-bottom:8px; break-inside:avoid; page-break-inside:avoid}
.plus-papier .ml > .eyebrow{font-size:9pt; font-weight:800; text-transform:uppercase;
  letter-spacing:.1em; color:var(--muted)}
.plus-papier .ml > h2{font-size:14pt; font-weight:900; color:var(--ink);
  margin:2px 0 7px}
.plus-papier h3{font-size:12.5pt; font-weight:900; color:var(--ink); margin-bottom:5px}
.plus-papier p.mp{font-weight:600; margin-bottom:7px}
.plus-papier .note{margin-top:6px}
.plus-papier table{width:100%; border-collapse:collapse}
.plus-papier table.ana td, .plus-papier table.ex2 td, .plus-papier table.labo td{
  padding:5px 8px 5px 0; border-top:1px solid var(--line); vertical-align:top;
  font-weight:600}
.plus-papier table.ana td:first-child, .plus-papier table.ex2 td:nth-child(2),
.plus-papier table.labo td:first-child{color:var(--muted); font-size:10pt; font-weight:800}
.plus-papier table.ana td.cle, .plus-papier table.labo td.cle{
  font-weight:900; color:var(--ink); font-size:11pt}
.plus-papier table.labo th{font-size:9pt; text-align:left; color:var(--muted);
  font-weight:800; padding-bottom:3px}
.plus-papier .tags{display:block; font-size:10pt; font-weight:800; color:var(--muted);
  margin-top:2px}
.plus-papier .dit{margin-top:8px; background:var(--tint); border-radius:9px;
  padding:7px 11px; font-weight:700; color:var(--ink)}
.plus-papier .dit .k{font-size:9pt; text-transform:uppercase; letter-spacing:.1em;
  color:var(--muted); margin-right:6px}
.plus-papier .pieges{display:grid; grid-template-columns:1fr 1fr 1fr; gap:9px}
.plus-papier .pg{border:1.5px dashed var(--muted); border-radius:12px; padding:9px 11px}
.plus-papier .pg .k{font-size:9pt; font-weight:800; text-transform:uppercase;
  letter-spacing:.1em; color:var(--muted); margin-top:5px}
.plus-papier .pg .k:first-child{margin-top:0}
.plus-papier .pg .ph{font-weight:800; color:var(--ink); font-size:10.5pt}
.plus-papier .pg .px{margin-top:6px; font-weight:600; font-size:10pt; color:var(--soft)}
.plus-papier ol.check{list-style:none; counter-reset:c; margin:0; padding:0}
.plus-papier ol.check li{counter-increment:c; position:relative; padding-left:9mm;
  margin-bottom:8px; break-inside:avoid}
.plus-papier ol.check li::before{content:counter(c); position:absolute; left:0; top:0;
  width:6mm; height:6mm; border-radius:50%; border:1.5px solid var(--rule);
  font-size:9.5pt; font-weight:800; color:var(--ink); display:flex;
  align-items:center; justify-content:center}
.plus-papier ol.check .q{font-weight:800; color:var(--ink)}
.plus-papier ul.opts{list-style:none; margin:3px 0 0; padding:0; display:flex;
  gap:10px; flex-wrap:wrap}
.plus-papier ul.opts li{font-weight:600; border:1px solid var(--line);
  border-radius:999px; padding:2px 11px; font-size:10.5pt}
.plus-papier .reps{margin-top:8px; border-top:1px solid var(--line); padding-top:6px;
  font-size:10pt; font-weight:600; color:var(--soft)}
@media print{ .plus-papier{break-before:auto} }
"""

CHAPEAU = (
    "Ce que le module explique à l’écran quand on clique « Ouvrir la mini-leçon » : "
    "la règle, ses cas particuliers, les pièges et de quoi vérifier qu’on a compris. "
    "Rien de tout cela n’est exigé en classe — c’est là pour la personne qui veut "
    "savoir pourquoi."
)


def modules_du_niveau(niveau):
    """Les slugs d'un niveau, dans l'ordre du registre — la seule source."""
    import modules as registre
    trouves = [(m.get('numero', 99), slug)
               for slug, m in registre.MODULES.items()
               if str(m.get('niveau')) in (str(niveau), 'Niveau %s' % niveau)]
    return [slug for _, slug in sorted(trouves)]


def cles_de_la_fiche(slug, code, plus):
    """Les mini-leçons que cette séance travaille, lues dans son deck.

    Le deck le dit en tête : « Source : exercice `prGraphie` et sa mini-leçon ».
    On ne retient que ce qui est **réellement** une clé de `plus.js` — un deck
    cite aussi des noms de tables (`FC_CARDS`) et des types de blocs (`texte`).
    L'ordre d'apparition est gardé, les répétitions non.
    """
    chemin = os.path.join(DECKS, slug, '%s.py' % code)
    if not os.path.exists(chemin):
        return []
    with open(chemin, encoding='utf-8') as f:
        tete = f.read(900)
    return list(dict.fromkeys(
        k for k in re.findall(r'`([A-Za-z][A-Za-z0-9_]*)`', tete) if k in plus))


def section_plus(manuel, plus, cles):
    """La section « En apprendre plus » d'une fiche, ou '' s'il n'y a rien."""
    if not cles:
        return ''
    lecons = []
    for cle in cles:
        ml = plus[cle]
        blocs = ''.join(manuel.bloc_html(b) for b in ml.get('blocs', []))
        if not blocs:
            continue
        lecons.append(
            '<section class="ml"><div class="eyebrow">%s</div><h2>%s</h2>%s</section>'
            % (manuel.e(ml.get('eye') or 'Mini-leçon'),
               manuel._riche(ml.get('tit') or ''), blocs))
    if not lecons:
        return ''
    return ('<div class="plus-papier"><div class="lbl">En apprendre plus</div>'
            '<p class="chapeau">%s</p>%s</div>' % (CHAPEAU, ''.join(lecons)))


def enrichir(html_source, section):
    """Pose le CSS avant `</head>` et la section avant le pied de page.

    Le pied est le dernier repère sûr d'une fiche : les blocs sont des
    `<section class="bloc …">` en enfilade, sans conteneur qui les ferme.
    """
    html_source = html_source.replace(
        '</style>', '</style>\n<style>%s</style>' % CSS_PLUS, 1)
    if '<footer>' in html_source:
        return html_source.replace('<footer>', section + '\n<footer>', 1)
    return html_source.replace('</body>', section + '\n</body>', 1)




GABARIT_PAGE = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fiches élèves du niveau 6 — l'essai « En apprendre plus »</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Nunito:wght@400;600;700;800&display=swap">
<style>
:root{
  --ground:#F7F7F5; --card:#FFFFFF; --sunken:#FBFBFA;
  --ink:#17181A; --body:#3A3D40; --muted:#6E7175;
  --line:#E4E4E0; --line-fort:#D2D2CD;
  --acier:#1D6B8F; --acier-bg:#E7F0F6;
  --fait:#0A8F5B; --fait-bg:#E6F5EE;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#151618; --card:#1D1F22; --sunken:#212326;
  --ink:#F2F2F0; --body:#CFD1D3; --muted:#94979B;
  --line:#2E3135; --line-fort:#3D4146;
  --acier:#6DAFD2; --acier-bg:#14242C;
  --fait:#4BC48D; --fait-bg:#12291F;
}}
:root[data-theme="dark"]{
  --ground:#151618; --card:#1D1F22; --sunken:#212326;
  --ink:#F2F2F0; --body:#CFD1D3; --muted:#94979B;
  --line:#2E3135; --line-fort:#3D4146;
  --acier:#6DAFD2; --acier-bg:#14242C;
  --fait:#4BC48D; --fait-bg:#12291F;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--body);
  font-family:Nunito,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
.doc{max-width:1280px;margin:0 auto;padding:26px 22px 60px}
.retour{display:inline-flex;gap:8px;font-size:13px;font-weight:700;color:var(--muted);
  text-decoration:none;margin-bottom:22px}
.retour:hover{color:var(--acier)}
.eyebrow{font-size:12px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;
  color:var(--acier);margin:0 0 10px}
h1{font-family:Newsreader,Georgia,serif;font-size:clamp(30px,4.6vw,44px);line-height:1.06;
  font-weight:500;letter-spacing:-.02em;color:var(--ink);margin:0 0 14px;text-wrap:balance}
.chapeau{font-size:17px;margin:0 0 8px;max-width:70ch}
.chapeau strong{color:var(--ink);font-weight:700}
.note{font-size:14px;color:var(--muted);margin:0 0 24px;max-width:74ch}
.note code{font-family:var(--mono);font-size:.88em;background:var(--sunken);
  border:1px solid var(--line);border-radius:4px;padding:1px 5px}

.plan{display:grid;grid-template-columns:270px 1fr;gap:18px;align-items:start}
@media (max-width:880px){.plan{grid-template-columns:1fr}}

.rail{background:var(--card);border:1px solid var(--line);border-radius:4px;
  overflow:hidden;position:sticky;top:14px}
@media (max-width:880px){.rail{position:static}}
.rail h2{font-size:11.5px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);margin:0;padding:12px 15px 8px;background:var(--sunken);
  border-bottom:1px solid var(--line)}
select.mod{width:100%;border:0;border-bottom:1px solid var(--line);background:var(--card);
  color:var(--ink);font:inherit;font-weight:700;padding:11px 14px;cursor:pointer}
select.mod:focus{outline:2px solid var(--acier);outline-offset:-2px}
ul.seances{list-style:none;margin:0;padding:0;max-height:62vh;overflow-y:auto}
ul.seances li{border-bottom:1px solid var(--line)}
ul.seances li:last-child{border-bottom:0}
ul.seances button{display:flex;gap:9px;align-items:baseline;width:100%;text-align:left;
  border:0;background:transparent;font:inherit;color:var(--body);padding:9px 14px;
  cursor:pointer;border-left:3px solid transparent}
ul.seances button:hover{background:var(--sunken)}
ul.seances button[aria-current="true"]{background:var(--acier-bg);color:var(--ink);
  font-weight:700;border-left-color:var(--acier)}
.code{font-family:var(--mono);font-size:11.5px;font-weight:700;color:var(--muted);
  min-width:20px}
ul.seances button[aria-current="true"] .code{color:var(--acier)}
.tt{flex:1;font-size:14px;line-height:1.35}
.pastille{width:7px;height:7px;border-radius:50%;background:var(--fait);flex:none;
  align-self:center}
.pastille.non{background:transparent;border:1px solid var(--line-fort)}

.vue{background:var(--card);border:1px solid var(--line);border-radius:4px;overflow:hidden}
.onglets{display:flex;gap:2px;padding:10px 12px 0;background:var(--sunken);
  border-bottom:1px solid var(--line);flex-wrap:wrap;align-items:flex-end}
.onglets button{border:1px solid var(--line);border-bottom:0;background:var(--sunken);
  color:var(--muted);font:inherit;font-weight:700;font-size:14px;padding:9px 16px;
  border-radius:4px 4px 0 0;cursor:pointer;position:relative;top:1px}
.onglets button[aria-selected="true"]{background:var(--card);color:var(--ink);
  border-color:var(--line)}
.onglets .droite{margin-left:auto;padding:0 2px 9px;font-size:13px}
.onglets .droite a{color:var(--acier);font-weight:700;text-decoration:none}
.onglets .droite a:hover{text-decoration:underline}
.barre{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;
  padding:10px 15px;border-bottom:1px solid var(--line);font-size:13.5px;color:var(--muted)}
.barre b{color:var(--ink);font-size:15px;font-weight:700}
.badge{font-size:11px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;
  padding:3px 9px;border-radius:2px;background:var(--fait-bg);color:var(--fait)}
.badge.non{background:var(--sunken);color:var(--muted);border:1px solid var(--line)}
iframe{display:block;width:100%;height:78vh;border:0;background:#fff}
.pied{margin-top:30px;padding-top:18px;border-top:1px solid var(--line);
  font-size:13px;color:var(--muted)}
</style>
</head>
<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Bibliothèque de francisation · niveau 6 · essai</p>
<h1>La théorie descend-elle dans la fiche&nbsp;?</h1>
<p class="chapeau">Les <strong>160 fiches du niveau 6</strong>, en deux versions&nbsp;: celle
d'aujourd'hui, et une où la mini-leçon — le « En apprendre plus » qui ne vit qu'à l'écran —
est imprimée <strong>dans la fiche de sa séance</strong>. Changez d'onglet&nbsp;: la séance
ne bouge pas, seule la version change.</p>
<p class="note">111 fiches sur 160 portent une mini-leçon&nbsp;; les 49 autres sont
identiques dans les deux onglets — ce sont les séances de production et d'application, qui
n'en ont pas. Le point vert dans la liste dit lesquelles changent. Le rattachement d'une
mini-leçon à une séance est lu dans le deck de la séance, pas deviné.
<strong>La série d'origine n'a pas été touchée</strong>&nbsp;: l'essai vit dans
<code>assets/documents/plus/</code>.</p>

<div class="plan">
  <nav class="rail">
    <h2>Les dix modules</h2>
    <select class="mod" id="mod"></select>
    <ul class="seances" id="seances"></ul>
  </nav>
  <main class="vue">
    <div class="onglets" role="tablist">
      <button role="tab" id="ong-avant" aria-selected="true">Fiche élève</button>
      <button role="tab" id="ong-apres" aria-selected="false">Fiche élève avec « En apprendre plus »</button>
      <span class="droite"><a id="ouvrir" href="#" target="_blank" rel="noopener">Ouvrir seule&nbsp;↗</a></span>
    </div>
    <div class="barre"><b id="tt">—</b><span id="etat"></span></div>
    <iframe id="vue" title="La fiche"></iframe>
  </main>
</div>

<div class="pied">
  <p>Produit par <code>python3 build/fiches_plus.py</code>. Le rendu papier des mini-leçons
  est celui du manuel de l'élève, réemployé tel quel — une seule mise en page pour une
  seule chose.</p>
</div>
</div>

<script>
var DONNEES = /*DONNEES*/;
var mod = 0, sea = 0, apres = false;
/* On ouvre sur la première séance qui porte une mini-leçon : atterrir sur une
   séance où les deux onglets sont identiques ferait croire que la page ne
   marche pas. */
function premiereAvecPlus(m) {
  for (var i = 0; i < m.seances.length; i++) if (m.seances[i].plus) return i;
  return 0;
}
var $ = function (id) { return document.getElementById(id); };

function chemin() {
  var s = DONNEES[mod].seances[sea];
  return '../documents/' + (apres ? 'plus/' : '') + s.f;
}

function rendre() {
  var m = DONNEES[mod], s = m.seances[sea];
  $('vue').src = chemin();
  $('ouvrir').href = chemin();
  $('tt').textContent = s.titre;
  /* Dire quand les deux onglets montrent la même chose. Sans ce mot, une
     séance sans mini-leçon passerait pour un onglet cassé. */
  $('etat').innerHTML = s.plus
    ? '<span class="badge">porte une mini-leçon</span>'
    : '<span class="badge non">aucune mini-leçon — les deux onglets sont identiques</span>';
  $('ong-avant').setAttribute('aria-selected', String(!apres));
  $('ong-apres').setAttribute('aria-selected', String(apres));
  Array.prototype.forEach.call($('seances').children, function (li, i) {
    li.firstChild.setAttribute('aria-current', String(i === sea));
  });
}

function rendreSeances() {
  $('seances').innerHTML = DONNEES[mod].seances.map(function (s, i) {
    return '<li><button type="button" data-i="' + i + '">'
      + '<span class="code">' + s.code + '</span>'
      + '<span class="tt">' + s.titre.replace(/^[A-E]\\d+\\s*·\\s*/, '') + '</span>'
      + '<span class="pastille' + (s.plus ? '' : ' non') + '" title="'
      + (s.plus ? 'porte une mini-leçon' : 'aucune mini-leçon') + '"></span>'
      + '</button></li>';
  }).join('');
}

$('mod').innerHTML = DONNEES.map(function (m, i) {
  return '<option value="' + i + '">' + m.titre + '</option>';
}).join('');
$('mod').addEventListener('change', function () {
  mod = Number(this.value); sea = premiereAvecPlus(DONNEES[mod]);
  rendreSeances(); rendre();
});
$('seances').addEventListener('click', function (e) {
  var b = e.target.closest('button[data-i]');
  /* On garde l'onglet en changeant de séance : c'est tout l'intérêt de la
     page — comparer la même chose, pas retrouver son onglet à chaque clic. */
  if (b) { sea = Number(b.dataset.i); rendre(); }
});
$('ong-avant').addEventListener('click', function () { apres = false; rendre(); });
$('ong-apres').addEventListener('click', function () { apres = true; rendre(); });
sea = premiereAvecPlus(DONNEES[0]);
rendreSeances(); rendre();
</script>
</body>
</html>
"""


# ── La page de comparaison ──────────────────────────────────────────────────
#
# Deux séries de 160 fiches ne se comparent pas dans un explorateur de
# fichiers. La page les met côte à côte : un onglet par série, la même séance
# des deux côtés, et le passage de l'un à l'autre **sans changer de séance** —
# c'est le seul geste qui compte quand on montre ça à un enseignant.

PAGE = os.path.join(RACINE, 'assets', 'presentations', 'fiches-plus-niveau-6.html')


def titre_de(chemin):
    """Le titre lisible d'une fiche, lu dans sa balise `<title>`."""
    with open(chemin, encoding='utf-8') as f:
        tete = f.read(2000)
    m = re.search(r'<title>(.*?)</title>', tete, re.S)
    if not m:
        return os.path.basename(chemin)
    t = re.sub(r'\s*—\s*Fiche élève\s*$', '', m.group(1).strip())
    return t


def ecrire_page(index):
    """L'index est [(slug, titre du module, [(code, titre, fichier, aPlus)])]."""
    import json as _json
    donnees = _json.dumps([
        {'slug': s, 'titre': t,
         'seances': [{'code': c.upper(), 'titre': ti, 'f': f, 'plus': p}
                     for c, ti, f, p in ss]}
        for s, t, ss in index], ensure_ascii=False)
    with open(PAGE, 'w', encoding='utf-8') as f:
        f.write(GABARIT_PAGE.replace('/*DONNEES*/', donnees))
    print('✓ %s' % os.path.relpath(PAGE, RACINE))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('niveau', nargs='?', default='6')
    ap.add_argument('--releve', action='store_true',
                    help="dire ce qui serait fait, sans rien écrire")
    args = ap.parse_args()

    manuel = _charger_manuel()
    slugs = modules_du_niveau(args.niveau)
    if not slugs:
        print('Aucun module au niveau %s.' % args.niveau)
        return 1
    if not args.releve:
        os.makedirs(SORTIE, exist_ok=True)

    total = enrichies = orphelines = sommaires = 0
    index = []
    for slug in slugs:
        plus = manuel.mini_lecons(slug)
        posees = set()
        n_mod = n_fiches = 0
        seances = []
        for source in sorted(glob.glob(os.path.join(DOCUMENTS, '%s-*.html' % slug))):
            nom = os.path.basename(source)
            reste = nom[len(slug) + 1:]
            if reste.startswith('fiches-eleves'):
                # Le sommaire : recopié tel quel. Ses liens sont des noms de
                # voisins, donc ils pointent d'eux-mêmes vers les fiches d'essai.
                if not args.releve:
                    with open(source, encoding='utf-8') as f:
                        contenu = f.read()
                    with open(os.path.join(SORTIE, nom), 'w', encoding='utf-8') as f:
                        f.write(contenu)
                sommaires += 1
                continue
            code = reste.split('-')[0]
            total += 1
            n_fiches += 1
            cles = cles_de_la_fiche(slug, code, plus)
            posees |= set(cles)
            with open(source, encoding='utf-8') as f:
                contenu = f.read()
            section = section_plus(manuel, plus, cles)
            if section:
                enrichies += 1
                n_mod += 1
            seances.append((code, titre_de(source), nom, bool(section)))
            if not args.releve:
                with open(os.path.join(SORTIE, nom), 'w', encoding='utf-8') as f:
                    f.write(enrichir(contenu, section) if section else contenu)
        import modules as _reg
        index.append((slug, _reg.MODULES.get(slug, {}).get('titre', slug),
                      sorted(seances)))
        manquantes = sorted(set(plus) - posees)
        orphelines += len(manquantes)
        print('  %-26s %2d/%2d fiches enrichies · %2d mini-leçons%s'
              % (slug, n_mod, n_fiches, len(plus),
                 (' · orpheline%s : %s' % ('s' if len(manquantes) > 1 else '',
                                           ', '.join(manquantes))) if manquantes else ''))

    quoi = 'seraient écrites' if args.releve else 'écrites dans assets/documents/plus/'
    print('\n%d fiches %s — %d portent un « En apprendre plus », %d n’en ont pas.'
          % (total, quoi, enrichies, total - enrichies))
    print('%d sommaires suivis. %d mini-leçons qu’aucune fiche ne nomme.'
          % (sommaires, orphelines))
    if not args.releve:
        ecrire_page(index)
    print('\nLa série d’origine dans assets/documents/ n’a pas été touchée.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
