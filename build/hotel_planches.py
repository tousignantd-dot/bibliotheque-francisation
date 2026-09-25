#!/usr/bin/env python3
"""L'écran de l'employé de la réception — étape 1 : les mots et le comptoir.

    python3 build/hotel_planches.py   # → modules-autonomes/hotel-reception/index.html

Produit, jamais écrit à la main. Il lit, dans build/contenu/entreprise-hotel/ :
`lexique.py` (les mots, en trois langues), `interface.py` (les textes de
l'écran, trois fois), `comptoir.py` (les zones à toucher du grand dessin).

LES DEUX LANGUES. L'employé choisit celle qu'il PARLE et celle qu'il APPREND.
L'écran est dans la première ; les mots, leur voix et ce qu'il devra dire sont
dans la seconde. Sa langue à lui reste CACHÉE sous chaque mot tant qu'il ne la
demande pas (règle langue-appui-trois-couches).

LES PIÈGES d'une direction ne sont que ceux de SA paire de langues : un
francophone qui apprend l'anglais ne voit pas « embarazada ».

LE THÈME est celui de francis, tel quel (décision du 24 sept.) : aucune
couleur redéfinie, seulement les jetons du système de design. La marque garde
son nom ; son descripteur suit la langue apprise.

Paramètres d'adresse, pour les captures : ?parle=fr&apprend=en#comptoir
"""
import html, importlib.util, json, pathlib

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-hotel"
CROQUIS = RACINE / "assets" / "interactive" / "hotel" / "croquis"
SORTIE = RACINE / "modules-autonomes" / "hotel-reception" / "index.html"
MEDIA_V = "1"


def _charger(nom):
    s = importlib.util.spec_from_file_location(f"hotel_{nom}", CONTENU / f"{nom}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


def donnees():
    LX, IF, CP = _charger("lexique"), _charger("interface"), _charger("comptoir")
    LX.verifier()
    mots = []
    for i, pl, fr, en, es, dessin, note in LX.LEXIQUE:
        paire = note[len("PIÈGE ("):note.index(")")] if note.startswith("PIÈGE (") else ""
        notes = {"fr": note} if note else {}
        notes.update(IF.PIEGES.get(i, {}))
        if paire:
            for l in paire.split("·"):
                assert l in notes, f"{i} : piège {paire} sans note en {l}"
        mots.append({"id": i, "p": pl, "fr": fr, "en": en, "es": es,
                     "img": dessin == "croquis" and (CROQUIS / f"{i}.jpg").exists(),
                     "k": dessin == "comptoir", "paire": paire, "notes": notes})
    ids = {m["id"] for m in mots}
    for z in CP.ZONES:
        assert z[0] in ids, f"zone {z[0]} absente du lexique"
    return {"hotel": IF.HOTEL, "ui": IF.UI, "langues": IF.NOM_LANGUE, "desc": IF.DESCRIPTEUR,
            "planches": [[k, IF.PLANCHES[k]] for k, _ in LX.PLANCHES],
            "mots": mots, "zones": CP.ZONES, "v": MEDIA_V}


def main():
    d = donnees()
    page = GABARIT.replace("%%DONNEES%%", json.dumps(d, ensure_ascii=False).replace("</", "<\\/"))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {len(d['mots'])} mots, {len(d['zones'])} zones au comptoir")


GABARIT = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hôtel Rive-Claire — la réception</title>
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<style>
/* Page produite par build/hotel_planches.py — ne pas l'éditer.
   Thème francis tel quel : seulement les jetons du système de design. */
body{margin:0;background:var(--surface-page);color:var(--text-body);font-family:Nunito,system-ui,sans-serif}
.hr{max-width:1080px;margin:0 auto;padding:18px 16px 60px}
.fr-barre .fr-barre__in{max-width:1080px;padding-left:16px;padding-right:16px}
.secteur{display:flex;flex-direction:column;align-items:flex-end;text-align:right;line-height:1.15}
.secteur small{font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted)}
.secteur b{font-size:19px;font-weight:900;color:var(--text-accent)}
.secteur .court{display:none}
@media (max-width:480px){.secteur small{display:none}.secteur b{font-size:16px}.secteur .long{display:none}.secteur .court{display:inline}}
.enseigne{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-accent);margin:0}
.hr h1{font-size:28px;line-height:1.15;margin:4px 0 8px;color:var(--text-strong)}
.hr h2{font-size:20px;margin:26px 0 10px;color:var(--text-strong)}
.chapeau{font-size:17px;line-height:1.5;max-width:720px;margin:0 0 6px}
.btn{font:inherit;font-weight:700;font-size:15px;cursor:pointer;border-radius:10px;padding:9px 14px;min-height:44px;
  border:1px solid var(--line-300);background:var(--surface-card);color:var(--text-strong);display:inline-flex;gap:8px;align-items:center}
.btn:hover{border-color:var(--accent)}
.btn--pri{background:var(--accent);border-color:var(--accent);color:#fff}
.btn svg{width:20px;height:20px;flex:none}
.btn--son{background:var(--audio);border-color:var(--audio);color:#fff}
.barre-haut{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;margin-bottom:10px}
.avis{font-size:13px;color:var(--text-muted);margin:24px 0 0}

/* Le choix des deux langues */
.choix-l{margin:18px 0 6px;font-size:13px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--text-muted)}
.langues{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;max-width:620px}
.langues button{font:inherit;cursor:pointer;text-align:start;padding:14px 16px;border-radius:12px;min-height:64px;
  border:1px solid var(--line-300);background:var(--surface-card);font-size:20px;font-weight:800;color:var(--text-strong)}
.langues button small{display:block;font-size:13px;font-weight:600;color:var(--text-muted)}
.langues button[aria-pressed=true]{border-color:var(--accent);box-shadow:inset 0 0 0 2px var(--accent);background:var(--accent-soft)}
.langues button:disabled{opacity:.35;cursor:not-allowed}
@media (max-width:480px){.langues button{font-size:17px;padding:12px}}

/* L'accueil */
.carte-comptoir{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:16px;align-items:center;cursor:pointer;
  background:var(--surface-card);border:1px solid var(--line-200);border-radius:16px;padding:12px;margin-top:16px;text-align:start;font:inherit;width:100%}
.carte-comptoir:hover{border-color:var(--accent)}
.carte-comptoir img{width:100%;border-radius:10px;display:block}
.carte-comptoir b{font-size:22px;color:var(--text-strong);display:block}
.carte-comptoir span{color:var(--text-muted)}
@media (max-width:640px){.carte-comptoir{grid-template-columns:1fr}}
.planches{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}
.planche-c{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:6px}
.planche-c:hover{border-color:var(--accent)}
.planche-c .vign{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;background:#fff;border-radius:10px;padding:6px;min-height:40px}
.planche-c .vign img{width:100%;aspect-ratio:1/1;object-fit:contain;display:block}
.planche-c b{font-size:17px;color:var(--text-strong)}
.planche-c .n{font-size:13px;color:var(--text-muted);font-weight:600}

/* Une planche */
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px}
.mot{background:var(--surface-card);border:1px solid var(--line-200);border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:8px}
.mot.piege{border-color:var(--warn-line);box-shadow:inset 0 3px 0 var(--warn-line)}
.mot .img{width:100%;aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:10px;display:block}
.mot .appris{font-size:20px;font-weight:900;color:var(--text-strong);line-height:1.25;margin:0}
.mot .actions{display:flex;flex-wrap:wrap;gap:12px}
.mot .trad{margin:0;font-size:16px;color:var(--text-muted);font-weight:700}
.mot .note{margin:0;font-size:14px;line-height:1.45;color:var(--text-body)}
.mot.piege .note{background:var(--warn-bg);color:var(--warn-ink);border-radius:8px;padding:8px 10px;font-weight:700}
@media (max-width:480px){.grille{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.mot .appris{font-size:17px}
  .mot .actions .btn{padding:8px 10px;font-size:14px}}

/* Le comptoir */
.scene{position:relative;background:#fff;border-radius:14px;overflow:hidden;border:1px solid var(--line-200)}
.scene img{width:100%;display:block}
.zone{position:absolute;transform:translate(-50%,-50%);width:44px;height:44px;border-radius:50%;cursor:pointer;
  border:3px solid var(--accent);background:rgba(255,255,255,.55);font:inherit;font-weight:900;font-size:15px;color:var(--text-strong);padding:0}
.zone[aria-pressed=true]{background:var(--accent);color:#fff}
@media (max-width:640px){.zone{width:30px;height:30px;font-size:12px;border-width:2px}}
.panneau{margin-top:12px;background:var(--surface-card);border:1px solid var(--line-200);border-radius:14px;padding:14px;min-height:76px}
.panneau .appris{font-size:24px;font-weight:900;color:var(--text-strong);margin:0 0 10px}
.panneau .actions{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.panneau .trad{margin:10px 0 0;font-size:17px;color:var(--text-muted);font-weight:700}
.objets{display:flex;flex-wrap:wrap;gap:12px;margin-top:10px;padding:0;list-style:none}
.objets button{font:inherit;cursor:pointer;border:1px solid var(--line-300);background:var(--surface-card);border-radius:999px;padding:8px 12px;min-height:40px;color:var(--text-strong)}
.objets button b{margin-right:6px;color:var(--text-accent)}
.objets button[aria-pressed=true]{border-color:var(--accent);background:var(--accent-soft)}
</style>
</head>
<body>
<div class="fr-barre"><div class="fr-barre__in">
  <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc" id="desc"></span></span>
  <span class="secteur"><small id="surtitre"></small><b><span class="long" id="secteur"></span><span class="court" id="secteurCourt"></span></b></span>
</div></div>
<main class="hr" id="app"></main>
<script>
const D = %%DONNEES%%;
const E = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const ICO = {
  son:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H3v6h3l5 4V5z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M18.5 5.5a9 9 0 0 1 0 13"/></svg>',
  oeil:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
  retour:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>'};
const PAR_ID = Object.fromEntries(D.mots.map(m => [m.id, m]));
const CLE = 'hotel-reception-langues';
let L = {parle:null, apprend:null};
try { L = Object.assign(L, JSON.parse(localStorage.getItem(CLE) || '{}')); } catch (e) {}
const q = new URLSearchParams(location.search);
if (q.get('parle')) L.parle = q.get('parle');
if (q.get('apprend')) L.apprend = q.get('apprend');
function sauver(){ try { localStorage.setItem(CLE, JSON.stringify(L)); } catch (e) {} }
const T = k => D.ui[k][L.parle || 'fr'];
const paire = () => [L.parle, L.apprend].sort().join('·');
const PAIRE_ORDRE = {'en·fr':'fr·en','es·fr':'fr·es','en·es':'es·en'};

let son = null;
function ecouter(id){
  if (son) son.pause();
  son = new Audio(`/assets/interactive/hotel/sons/${L.apprend}/${id}.mp3?v=${D.v}`);
  son.play().catch(()=>{});
}
function piegeDe(m){ return m.paire && m.paire === PAIRE_ORDRE[paire()]; }
function noteDe(m){
  // Un piège d'une autre paire ne se montre pas ; une note ordinaire n'existe
  // pour l'instant qu'en français (étape 1).
  if (m.paire) return piegeDe(m) ? (m.notes[L.parle] || '') : '';
  return m.notes[L.parle] || '';
}

function marque(){
  const p = L.parle || 'fr';
  document.documentElement.lang = p;
  document.getElementById('desc').textContent = L.apprend ? D.desc[p][L.apprend] : D.desc.fr.fr;
  document.getElementById('surtitre').textContent = D.ui.surtitre[p];
  document.getElementById('secteur').textContent = D.ui.secteur[p];
  document.getElementById('secteurCourt').textContent = D.ui.secteur_court[p];
}

function ecranLangue(){
  const bouton = (g, l) => {
    const pris = g === 'apprend' && l === L.parle;
    return `<button type="button" data-g="${g}" data-l="${l}" aria-pressed="${L[g]===l}" ${pris?'disabled':''}>`
      + `${E(D.langues[l][l])}<small>${E(D.langues[L.parle||'fr'][l])}</small></button>`;
  };
  const pret = L.parle && L.apprend && L.parle !== L.apprend;
  return `<p class="enseigne">${E(D.hotel)}</p>
    <h1>Bienvenue · Welcome · Bienvenido</h1>
    <p class="choix-l">${E(D.ui.je_parle.fr)} · ${E(D.ui.je_parle.en)} · ${E(D.ui.je_parle.es)}</p>
    <div class="langues">${['fr','en','es'].map(l => bouton('parle', l)).join('')}</div>
    <p class="choix-l">${E(D.ui.j_apprends.fr)} · ${E(D.ui.j_apprends.en)} · ${E(D.ui.j_apprends.es)}</p>
    <div class="langues">${['fr','en','es'].map(l => bouton('apprend', l)).join('')}</div>
    <p style="margin-top:20px"><button type="button" class="btn btn--pri" id="go" ${pret?'':'disabled'}>${E(T('commencer'))}</button></p>`;
}

function ecranAccueil(){
  const vign = k => D.mots.filter(m => m.p === k && m.img).slice(0,3)
    .map(m => `<img src="/assets/interactive/hotel/croquis/${m.id}.jpg?v=${D.v}" alt="" loading="lazy">`).join('');
  const cartes = D.planches.filter(([k]) => k !== 'comptoir').map(([k, t]) =>
    `<button type="button" class="planche-c" data-aller="p-${k}"><span class="vign">${vign(k)}</span>`
    + `<b>${E(t[L.parle])}</b><span class="n">${D.mots.filter(m=>m.p===k).length} ${E(T('mots'))}</span></button>`).join('');
  return `<div class="barre-haut"><p class="enseigne">${E(D.hotel)}</p>
      <button type="button" class="btn" data-aller="langue">${E(T('changer'))}</button></div>
    <h1>${E(T('bienvenue_tit'))}</h1>
    <p class="chapeau">${E(T('intro'))}</p>
    <button type="button" class="carte-comptoir" data-aller="comptoir">
      <img src="/assets/interactive/hotel/croquis/comptoir.jpg?v=${D.v}" alt="">
      <span><b>${E(T('comptoir_tit'))}</b><span>${E(T('comptoir_sous'))}</span></span></button>
    <h2>${E(T('les_planches'))}</h2>
    <div class="planches">${cartes}</div>
    <p class="avis">${E(T('non_relu'))}</p>`;
}

function carteMot(m){
  const note = noteDe(m), pg = piegeDe(m);
  const img = m.img ? `<img class="img" src="/assets/interactive/hotel/croquis/${m.id}.jpg?v=${D.v}" alt="" loading="lazy">` : '';
  return `<article class="mot${pg?' piege':''}" data-id="${m.id}">${img}
    <p class="appris" lang="${L.apprend}">${E(m[L.apprend])}</p>
    <div class="actions"><button type="button" class="btn btn--son" data-son="${m.id}">${ICO.son}${E(T('ecouter'))}</button>
      <button type="button" class="btn" data-voir="${m.id}" aria-expanded="false">${ICO.oeil}${E(T('voir'))}</button></div>
    <p class="trad" id="tr-${m.id}" hidden>${E(m[L.parle])}</p>
    ${note ? `<p class="note">${pg ? `<b>${E(T('piege'))}</b> · ` : ''}${E(note.replace(/^(PIÈGE|TRAP|TRAMPA)\s*(\([^)]*\))?\s*:\s*/, ''))}</p>` : ''}
  </article>`;
}

function ecranPlanche(k){
  const t = D.planches.find(p => p[0] === k)[1];
  return `<div class="barre-haut"><button type="button" class="btn" data-aller="accueil">${ICO.retour}${E(T('retour'))}</button></div>
    <p class="enseigne">${E(D.hotel)}</p><h1>${E(t[L.parle])}</h1>
    <div class="grille">${D.mots.filter(m => m.p === k).map(carteMot).join('')}</div>`;
}

let objet = null;
function ecranComptoir(){
  const zones = D.zones.map(([id, x, y], i) =>
    `<button type="button" class="zone" style="left:${x}%;top:${y}%" data-objet="${id}" aria-pressed="${objet===id}"
      aria-label="${i+1}">${i+1}</button>`).join('');
  const liste = D.zones.map(([id], i) =>
    `<li><button type="button" data-objet="${id}" aria-pressed="${objet===id}"><b>${i+1}</b><span lang="${L.apprend}">${E(PAR_ID[id][L.apprend])}</span></button></li>`).join('');
  const m = objet && PAR_ID[objet];
  const panneau = m ? `<p class="appris" lang="${L.apprend}">${E(m[L.apprend])}</p>
      <div class="actions"><button type="button" class="btn btn--son" data-son="${m.id}">${ICO.son}${E(T('ecouter'))}</button>
      <button type="button" class="btn" data-voir="${m.id}" aria-expanded="false">${ICO.oeil}${E(T('voir'))}</button></div>
      <p class="trad" id="tr-${m.id}" hidden>${E(m[L.parle])}</p>` : `<p>${E(T('touchez'))}</p>`;
  return `<div class="barre-haut"><button type="button" class="btn" data-aller="accueil">${ICO.retour}${E(T('retour'))}</button></div>
    <p class="enseigne">${E(D.hotel)}</p><h1>${E(T('comptoir_tit'))}</h1>
    <p class="chapeau">${E(T('comptoir_sous'))}</p>
    <div class="scene"><img src="/assets/interactive/hotel/croquis/comptoir.jpg?v=${D.v}" alt="">${zones}</div>
    <div class="panneau" aria-live="polite">${panneau}</div>
    <h2>${E(T('liste_objets'))}</h2><ul class="objets">${liste}</ul>`;
}

function rendre(){
  marque();
  const h = location.hash.slice(1);
  const pret = L.parle && L.apprend && L.parle !== L.apprend;
  let html;
  if (!pret || h === 'langue') html = ecranLangue();
  else if (h === 'comptoir') html = ecranComptoir();
  else if (h.startsWith('p-') && D.planches.some(p => 'p-'+p[0] === h)) html = ecranPlanche(h.slice(2));
  else html = ecranAccueil();
  document.getElementById('app').innerHTML = html;
}

document.addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  // On reste sur le choix des langues jusqu'à « Commencer » : sans l'ancre,
  // le second choix faisait sauter à l'accueil.
  if (b.dataset.g) { L[b.dataset.g] = b.dataset.l; if (L.apprend === L.parle) L.apprend = null; sauver();
    if (location.hash !== '#langue') history.replaceState(null, '', '#langue'); rendre(); return; }
  if (b.id === 'go') { location.hash = 'accueil'; return; }
  if (b.dataset.aller) { location.hash = b.dataset.aller; window.scrollTo(0, 0); return; }
  if (b.dataset.son) { ecouter(b.dataset.son); return; }
  if (b.dataset.voir) {
    const tr = document.getElementById('tr-' + b.dataset.voir), ouvert = tr.hidden;
    tr.hidden = !ouvert; b.setAttribute('aria-expanded', ouvert);
    b.lastChild.textContent = ouvert ? T('cacher') : T('voir'); return; }
  if (b.dataset.objet) {
    objet = b.dataset.objet; rendre(); ecouter(objet);
    document.querySelector('.panneau').scrollIntoView({block:'nearest'}); return; }
});
window.addEventListener('hashchange', () => { objet = null; rendre(); });
rendre();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
