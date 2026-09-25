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
MEDIA_V = "2"   # 2 : exercices (étape 2), 25 sept. 2026


def _charger(nom):
    s = importlib.util.spec_from_file_location(f"hotel_{nom}", CONTENU / f"{nom}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


def donnees():
    LX, IF, CP, EX = (_charger("lexique"), _charger("interface"), _charger("comptoir"),
                      _charger("exercices"))
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
    for i, faux in EX.PIEGES_FAUX.items():
        m = next(x for x in mots if x["id"] == i)
        assert m["paire"], f"{i} : fausse lecture sur un mot sans piège"
        assert set(faux) <= set(m["paire"].split("·")), f"{i} : fausse lecture hors de la paire"
    for r in EX.REPONSES:
        assert r[3][0][1] is None and all(fb for _, fb in r[3][1:]), f"{r[0]} : la bonne d'abord, une rétroaction par mauvaise"
    ex = {"faux": EX.PIEGES_FAUX, "noms": EX.NOMS, "nombres": EX.NOMBRES, "lits": EX.LITS,
          "demandes": EX.DEMANDES, "nuits": EX.NUITS, "reponses": EX.REPONSES}
    return {"hotel": IF.HOTEL, "ui": {**IF.UI, **EX.UI}, "ex": ex, "langues": IF.NOM_LANGUE, "desc": IF.DESCRIPTEUR,
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

/* Les exercices */
.exos{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
.exo-c{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:14px;padding:14px;display:flex;flex-direction:column;gap:4px}
.exo-c:hover{border-color:var(--accent)}
.exo-c b{font-size:17px;color:var(--text-strong)}
.exo-c span{font-size:14px;color:var(--text-muted)}
.progres{font-size:14px;font-weight:800;color:var(--text-muted)}
.consigne{font-size:17px;margin:0 0 14px;color:var(--text-body)}
.contexte{display:inline-block;background:var(--surface-sunken);border-radius:8px;padding:6px 10px;font-weight:800;margin:0 0 10px}
.alerte{background:var(--warn-bg);color:var(--warn-ink);border:1px solid var(--warn-line);border-radius:10px;padding:10px 12px;font-weight:700;margin:0 0 12px}
.cible{font-size:26px;font-weight:900;color:var(--text-strong);margin:0 0 12px}
.cible-img{width:min(260px,70%);aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:12px;border:1px solid var(--line-200);display:block;margin:0 0 12px}
.ecoute{display:flex;flex-wrap:wrap;gap:12px;margin:0 0 16px}
.choix{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;max-width:640px}
.choix.large{grid-template-columns:1fr}
.choix button{font:inherit;cursor:pointer;text-align:start;border:2px solid var(--line-300);background:var(--surface-card);
  border-radius:12px;padding:12px;min-height:56px;font-size:18px;font-weight:800;color:var(--text-strong);display:flex;flex-direction:column;gap:6px}
.choix.large button{font-size:17px;font-weight:700}
.choix button img{width:100%;aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:8px}
.choix button small{font-size:15px;font-weight:800;color:var(--text-body)}
.choix button.ok{border-color:var(--ok-line);background:var(--ok-bg)}
.choix button.ko{border-color:var(--warn-line);background:var(--warn-bg);opacity:.8}
.choix button:disabled{cursor:default}
.retour-fb{margin:14px 0 0;min-height:28px;font-size:17px;font-weight:700;max-width:640px}
.retour-fb.ok{color:var(--ok-ink)}
.retour-fb.ko{color:var(--warn-ink)}
.saisie{display:flex;flex-wrap:wrap;gap:12px;align-items:center;max-width:640px}
.saisie input{font:inherit;font-size:22px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;padding:10px 12px;
  border:2px solid var(--line-300);border-radius:10px;flex:1 1 220px;min-width:0;background:var(--surface-card);color:var(--text-strong)}
.suite{margin-top:18px}
.bilan{font-size:22px;font-weight:900;color:var(--text-strong)}
@media (max-width:480px){.choix{gap:10px}.choix button{font-size:16px;padding:10px}.cible{font-size:22px}}
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
    <h2>${E(T('exercices'))}</h2>
    <div class="exos">${FAMILLES.map(f => `<button type="button" class="exo-c" data-aller="x-${f}"><b>${E(T('x_'+f))}</b><span>${E(T('x_'+f+'_c'))}</span></button>`).join('')}</div>
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


// ── Les exercices ────────────────────────────────────────────────────────
const FAMILLES = ['entends','image','souviens','pieges','epeler','nombres','client','reponds'];
const melange = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
// La bonne réponse TOURNE d'un item à l'autre (leçon de la boucle : « toujours
// la deuxième » réussissait l'épreuve). Graine tirée au début de la série.
// Les places sont ÉQUILIBRÉES (chacune revient autant de fois) puis MÉLANGÉES :
// une rotation régulière (0, 1, 2, 3, 0…) se devine aussi bien qu'une place fixe.
let PLACES = [];
function places(n, N){ PLACES = melange(Array.from({length: N}, (_, k) => k % n)); }
function placer(bonne, autres, i){
  const out = melange(autres);
  out.splice(PLACES[i] % (autres.length + 1), 0, bonne); return out;
}
const imgUrl = id => `/assets/interactive/hotel/croquis/${id}.jpg?v=${D.v}`;
function jouer(chemin, lent){
  if (son) son.pause();
  son = new Audio(`/assets/interactive/hotel/sons/${chemin}?v=${D.v}`);
  if (lent) son.playbackRate = 0.8;
  son.play().catch(()=>{});
}
let X = null;

function serie(fam){
  const A = L.apprend, P = L.parle;
  const avecImg = D.mots.filter(m => m.img);
  const voisins = (m, n, filtre) => {
    let v = D.mots.filter(x => x.id !== m.id && x.p === m.p && filtre(x));
    if (v.length < n) v = v.concat(D.mots.filter(x => x.id !== m.id && x.p !== m.p && filtre(x)));
    return melange(v).slice(0, n);
  };
  let items = [];
  if (fam === 'entends' || fam === 'image') places(4, 8);
  if (fam === 'nombres') places(4, D.ex.nombres.length);
  if (fam === 'client') places(4, D.ex.demandes.length);
  if (fam === 'reponds') places(3, D.ex.reponses.length);
  if (fam === 'entends' || fam === 'image')
    items = melange(avecImg).slice(0, 8).map((m, i) => ({m, choix: placer(m, voisins(m, 3, x => x.img), i)}));
  if (fam === 'souviens') items = melange(D.mots).slice(0, 10).map(m => ({m}));
  if (fam === 'pieges') {
    const pr = PAIRE_ORDRE[paire()];
    const lot = melange(D.mots.filter(m => m.paire === pr && D.ex.faux[m.id] && D.ex.faux[m.id][P]));
    places(3, lot.length);
    items = lot.map((m, i) => ({m, choix: placer({t: m[P], ok: true}, [{t: D.ex.faux[m.id][P]}, {t: voisins(m, 1, x => !x.paire)[0][P]}], i)}));
  }
  if (fam === 'epeler') items = melange(D.ex.noms).map(nom => ({nom}));
  if (fam === 'nombres') items = melange(D.ex.nombres).map(([id, , ch], i) => ({id, choix: placer(ch[0], ch.slice(1), i), bonne: ch[0]}));
  if (fam === 'client') items = melange(D.ex.demandes).map(([id, lit, n], i) => {
    const autreLit = melange(D.ex.lits.filter(l => l !== lit)), autreN = melange([1,2,3,4,5].filter(k => k !== n));
    return {id, lit, n, choix: placer({lit, n}, [{lit, n: autreN[0]}, {lit: autreLit[0], n}, {lit: autreLit[1], n: autreN[1]}], i)};
  });
  if (fam === 'reponds') items = melange(D.ex.reponses).map((r, i) => ({r, choix: placer({k: 0}, [{k: 1}, {k: 2}], i)}));
  X = {fam, items, n0: items.length, i: 0, premier: 0, essais: 0, resolu: false, sus: 0, file: []};
}

function nuits(n){ const [un, pl] = D.ex.nuits[L.parle]; return `${n} ${n > 1 ? pl : un}`; }
function jouerItem(lent){
  const it = X.items[X.i], A = L.apprend;
  if (!it) return;
  if (X.fam === 'entends' || X.fam === 'souviens' || X.fam === 'pieges') jouer(`${A}/${it.m.id}.mp3`, lent);
  if (X.fam === 'epeler') jouer(`x/epeler/${A}/${it.nom.toLowerCase()}.mp3`, lent);
  if (X.fam === 'nombres') jouer(`x/nombres/${A}/${it.id}.mp3`, lent);
  if (X.fam === 'client') jouer(`x/client/${A}/${it.id}.mp3`, lent);
  if (X.fam === 'reponds') jouer(`x/reponds/${A}/${it.r[0]}.mp3`, lent);
}

function ecranExercice(fam){
  if (!X || X.fam !== fam) serie(fam);
  const A = L.apprend, P = L.parle, N = X.items.length;
  const tete = `<div class="barre-haut"><button type="button" class="btn" data-aller="accueil">${ICO.retour}${E(T('retour'))}</button>
    <span class="progres">${Math.min(X.i + 1, N)} / ${N}</span></div>
    <p class="enseigne">${E(D.hotel)}</p><h1>${E(T('x_' + fam))}</h1>`;
  if (!N) return tete + `<p class="consigne">${E(T('aucun_piege'))}</p>`;
  if (X.i >= N) return tete + `<p class="bilan">${E(T('fini'))}</p>
    <p class="consigne">${fam === 'souviens' ? `${X.premier} / ${X.n0} ${E(T('je_savais').toLowerCase())}` : `${X.premier} ${E(T('sur'))} ${X.n0} ${E(T('premier_coup'))}`}</p>
    <div class="ecoute"><button type="button" class="btn btn--pri" data-refaire="${fam}">${E(T('recommencer'))}</button>
    <button type="button" class="btn" data-aller="accueil">${E(T('autres_ex'))}</button></div>`;
  const it = X.items[X.i];
  const boutonsSon = `<div class="ecoute"><button type="button" class="btn btn--son" data-rejouer="0">${ICO.son}${E(T('reecouter'))}</button>
    ${['epeler','client','nombres','reponds'].includes(fam) ? `<button type="button" class="btn" data-rejouer="1">${E(T('lent'))}</button>` : ''}</div>`;
  let corps = `<p class="consigne">${E(T('x_' + fam + '_c'))}</p>`;
  if (fam === 'entends') corps += boutonsSon + `<div class="choix">${it.choix.map(m =>
      `<button type="button" data-rep="${m.id}"><img src="${imgUrl(m.id)}" alt=""></button>`).join('')}</div>`;
  if (fam === 'image') corps += `<img class="cible-img" src="${imgUrl(it.m.id)}" alt=""><div class="choix large">${it.choix.map(m =>
      `<button type="button" data-rep="${m.id}" lang="${A}">${E(m[A])}</button>`).join('')}</div>`;
  if (fam === 'souviens') corps += `<p class="cible" lang="${A}">${E(it.m[A])}</p>` + boutonsSon
      + `<p class="trad" id="sens" hidden style="font-size:20px;font-weight:800">${E(it.m[P])}</p>
      <div class="ecoute"><button type="button" class="btn" id="voirSens">${ICO.oeil}${E(T('voir_sens'))}</button></div>
      <div class="ecoute" id="auto" hidden><button type="button" class="btn btn--pri" data-auto="1">${E(T('je_savais'))}</button>
      <button type="button" class="btn" data-auto="0">${E(T('pas_encore'))}</button></div>`;
  if (fam === 'pieges') corps += `<p class="cible" lang="${A}">${E(it.m[A])}</p>` + boutonsSon + `<div class="choix large">${it.choix.map((c, k) =>
      `<button type="button" data-rep="${k}">${E(c.t)}</button>`).join('')}</div>`;
  if (fam === 'epeler') corps += boutonsSon + `<form class="saisie" id="formNom"><input id="nom" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-label="${E(T('votre_reponse'))}">
      <button type="submit" class="btn btn--pri">${E(T('verifier'))}</button></form>`;
  if (fam === 'nombres') corps += boutonsSon + `<div class="choix">${it.choix.map(c =>
      `<button type="button" data-rep="${E(c)}" style="font-size:24px">${E(c)}</button>`).join('')}</div>`;
  if (fam === 'client') corps += boutonsSon + `<div class="choix">${it.choix.map((c, k) =>
      `<button type="button" data-rep="${k}"><img src="${imgUrl(c.lit)}" alt=""><small>${E(PAR_ID[c.lit][P])} · ${E(nuits(c.n))}</small></button>`).join('')}</div>`;
  if (fam === 'reponds') {
    const [, ctx, client, reps, hors] = it.r;
    corps += (ctx ? `<p class="contexte">${E(ctx[P])}</p>` : '') + (hors ? `<p class="alerte">${E(T('hors_regle'))}</p>` : '')
      + `<p class="cible" lang="${A}" style="font-size:20px">« ${E(client[A])} »</p>` + boutonsSon
      + `<div class="choix large">${it.choix.map(c => `<button type="button" data-rep="${c.k}" lang="${A}">${E(reps[c.k][0][A])}</button>`).join('')}</div>`;
  }
  return tete + corps + `<p class="retour-fb" id="fb" aria-live="polite"></p>
    <div class="suite" id="suite" hidden><button type="button" class="btn btn--pri" data-suivant="1">${E(T('suivant'))}</button></div>`;
}

function repondre(b){
  const it = X.items[X.i], A = L.apprend, P = L.parle, fb = document.getElementById('fb');
  if (X.resolu || b.disabled) return;
  let ok = false, msg = '';
  if (X.fam === 'entends' || X.fam === 'image') {
    ok = b.dataset.rep === it.m.id;
    if (!ok) { const m = PAR_ID[b.dataset.rep]; msg = `${T('non_cest')} « ${X.fam === 'entends' ? m[A] : m[P]} ».`;
      if (X.fam === 'entends') jouer(`${A}/${m.id}.mp3`); }
  }
  if (X.fam === 'pieges') {
    const c = it.choix[+b.dataset.rep]; ok = !!c.ok;
    const note = (it.m.notes[P] || '').replace(/^(PIÈGE|TRAP|TRAMPA)\s*(\([^)]*\))?\s*:\s*/, '');
    msg = ok ? note : `${T('encore')} ${note}`;
  }
  if (X.fam === 'nombres') { ok = b.dataset.rep === it.bonne; if (!ok) { msg = T('encore'); } }
  if (X.fam === 'client') {
    const c = it.choix[+b.dataset.rep]; ok = c.lit === it.lit && c.n === it.n;
    if (!ok) msg = c.lit === it.lit ? T('lit_ok') : c.n === it.n ? T('nuits_ok') : T('rien_ok');
  }
  if (X.fam === 'reponds') { const k = +b.dataset.rep; ok = k === 0; msg = ok ? '' : it.r[3][k][1][P]; }
  noter(ok, msg, b);
}

function noter(ok, msg, b){
  const fb = document.getElementById('fb');
  if (ok) {
    if (X.essais === 0) X.premier++;
    X.resolu = true;
    if (b) b.classList.add('ok');
    document.querySelectorAll('.choix button').forEach(x => x.disabled = true);
    fb.className = 'retour-fb ok'; fb.textContent = `${T('juste')} ${msg}`.trim();
    document.getElementById('suite').hidden = false;
    document.querySelector('[data-suivant]').focus();
  } else {
    X.essais++;
    if (b) { b.classList.add('ko'); b.disabled = true; }
    fb.className = 'retour-fb ko'; fb.textContent = msg;
  }
}

function verifierNom(){
  const it = X.items[X.i], v = document.getElementById('nom').value.toUpperCase().replace(/[^A-Z]/g, '');
  if (!v || X.resolu) return;
  if (v === it.nom) return noter(true, it.nom, null);
  const justes = [...it.nom].filter((c, k) => v[k] === c).length;
  if (X.essais >= 1) {
    noter(false, `${T('la_bonne')} ${it.nom.split('').join(' ')}`, null);
    X.resolu = true; document.getElementById('suite').hidden = false;
  } else noter(false, `${T('encore')} ${justes} / ${it.nom.length} ${T('lettre_juste')}.`, null);
}

function suivant(){ X.i++; X.essais = 0; X.resolu = false; rendre(); setTimeout(() => jouerItem(false), 150); }

function rendre(){
  marque();
  const h = location.hash.slice(1);
  const pret = L.parle && L.apprend && L.parle !== L.apprend;
  let html;
  if (!pret || h === 'langue') html = ecranLangue();
  else if (h === 'comptoir') html = ecranComptoir();
  else if (h.startsWith('p-') && D.planches.some(p => 'p-'+p[0] === h)) html = ecranPlanche(h.slice(2));
  else if (h.startsWith('x-') && FAMILLES.includes(h.slice(2))) html = ecranExercice(h.slice(2));
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
  if (b.dataset.rep !== undefined && X) { repondre(b); return; }
  if (b.dataset.rejouer !== undefined) { jouerItem(b.dataset.rejouer === '1'); return; }
  if (b.dataset.suivant) { suivant(); return; }
  if (b.dataset.refaire) { serie(b.dataset.refaire); rendre(); setTimeout(() => jouerItem(false), 150); return; }
  if (b.id === 'voirSens') { document.getElementById('sens').hidden = false; document.getElementById('auto').hidden = false; b.hidden = true; return; }
  if (b.dataset.auto !== undefined) {
    // « Je me souviens » n'est pas jugé : « pas encore » remet la carte une fois en fin de série.
    const it = X.items[X.i];
    if (b.dataset.auto === '1') X.premier++; else if (!it.revu) X.items.push(Object.assign({}, it, {revu: true}));
    suivant(); return; }
  if (b.dataset.voir) {
    const tr = document.getElementById('tr-' + b.dataset.voir), ouvert = tr.hidden;
    tr.hidden = !ouvert; b.setAttribute('aria-expanded', ouvert);
    b.lastChild.textContent = ouvert ? T('cacher') : T('voir'); return; }
  if (b.dataset.objet) {
    objet = b.dataset.objet; rendre(); ecouter(objet);
    document.querySelector('.panneau').scrollIntoView({block:'nearest'}); return; }
});
document.addEventListener('submit', e => { if (e.target.id === 'formNom') { e.preventDefault(); verifierNom(); } });
window.addEventListener('hashchange', () => {
  objet = null;
  const h = location.hash.slice(1);
  if (h.startsWith('x-')) { serie(h.slice(2)); rendre(); setTimeout(() => jouerItem(false), 150); }
  else { X = null; rendre(); }
});
// Pour les contrôles joués par programme (build/controles) : l'état de la série.
window.HR = {familles: FAMILLES, etat: () => X};
rendre();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
