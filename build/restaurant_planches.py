#!/usr/bin/env python3
"""Les planches de Chez Jocelyne — l'écran de l'employé de restaurant (étape 1).

    python3 build/restaurant_planches.py   # → modules-autonomes/restaurant-planches/index.html

Produite, jamais écrite à la main. Même parcours que la Maison Francœur
(francoeur_planches.py), réduit à l'étape 1 — les exercices viendront à
l'étape 2, sur ce même écran. Elle lit, et rien d'autre :
  build/contenu/entreprise-restaurant/lexique.py        les mots, les 12 planches
  build/contenu/entreprise-restaurant/decor.py          les zones du poste
  build/contenu/entreprise-restaurant/traductions.json  espagnol et anglais, figés
  build/contenu/entreprise-restaurant/identite.py       le nom, le secteur
  assets/interactive/restaurant/{croquis,sons}/         ce qui existe sur le disque

LE PARCOURS : la langue (Français seulement, Español, English ; gardée sous
`francisation-langue`, la clé des modules) → les planches, et d'abord le POSTE
(le décor : on touche la ligne, le passe, la plonge) → une planche numérotée →
un mot : le croquis, le mot d'ici, l'autre, Écouter, « Voir dans ma langue »
MASQUÉ par défaut, le piège.

LES TROIS COUCHES : le mot reste en français en tête ; la consigne de l'écran
en français, l'appui DESSOUS ; la traduction du mot masquée par défaut.

ÉTATS PAR ADRESSE (démo, captures) : ?langue=es&planche=ustensiles&mot=poele,
?planche=poste. `window.__resto` expose les données aux contrôles.
"""
import html, json, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-restaurant"
sys.path.insert(0, str(CONTENU))
from lexique import LEXIQUE, PLANCHES, verifier  # noqa: E402
from decor import ZONES  # noqa: E402
import identite as IDE  # noqa: E402

CROQUIS = RACINE / "assets" / "interactive" / "restaurant" / "croquis"
SONS = RACINE / "assets" / "interactive" / "restaurant" / "sons"
SORTIE = RACINE / "modules-autonomes" / "restaurant-planches" / "index.html"
URL = "/assets/interactive/restaurant"

# Incrémenter après toute image ou tout son refait : même nom, même adresse,
# le navigateur servirait l'ancien sans rien dire.
MEDIA_V = "1"


def donnees():
    trad_f = CONTENU / "traductions.json"
    trad = json.loads(trad_f.read_text(encoding="utf-8")) if trad_f.exists() else {}
    lex = {e[0] for e in LEXIQUE}
    assert all(z[0] in lex for z in ZONES), "zone du décor absente du lexique"
    zones = {z[0]: z[1:] for z in ZONES}
    mots = []
    for ident, planche, mot, autre, dessin, note in LEXIQUE:
        m = {"id": ident, "p": planche, "mot": mot, "autre": autre, "note": note,
             "piege": note.startswith("PIÈGE")}
        if dessin == "croquis" and (CROQUIS / f"{ident}.jpg").exists():
            m["img"] = f"{URL}/croquis/{ident}.jpg?v={MEDIA_V}"
        if ident in zones:
            m["zone"] = zones[ident]
        if (SONS / f"{ident}.mp3").exists():
            m["son"] = f"{URL}/sons/{ident}.mp3?v={MEDIA_V}"
        if (SONS / "autre" / f"{ident}.mp3").exists():
            m["autre_son"] = f"{URL}/sons/autre/{ident}.mp3?v={MEDIA_V}"
        mots.append(m)
    langues = [{"c": c, "loc": trad[c]["loc"], "relu": trad[c]["relu"],
                "ui": trad[c].get("interface", {}),
                # Le modèle a préfixé les pièges tantôt « Atención: », tantôt
                # « Attention: » ou « Careful: » : l'écran dit déjà « Attention ».
                "mots": {k: [t["mot"], re.sub(r"^(Atención|Attention|Careful|Cuidado)\s*:\s*", "", t["note"])]
                         for k, t in trad[c]["mots"].items()}}
               for c in IDE.LANGUES_APPUI if c in trad]
    return {"planches": [{"k": k, "t": t, "poste": p} for k, t, p in PLANCHES],
            "mots": mots, "langues": langues,
            "poste": f"{URL}/croquis/poste.jpg?v={MEDIA_V}",
            "zones": [z[0] for z in ZONES]}


def main():
    verifier()
    d = donnees()
    page = (GABARIT.replace("%%NOM%%", html.escape(IDE.NOM))
            .replace("%%SURTITRE%%", html.escape(IDE.SURTITRE))
            .replace("%%SECTEUR%%", html.escape(IDE.SECTEUR))
            .replace("%%SECTEUR_COURT%%", html.escape(IDE.SECTEUR_COURT))
            .replace("%%DONNEES%%", json.dumps(d, ensure_ascii=False).replace("</", "<\\/")))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page, encoding="utf-8")
    n_img = sum("img" in m for m in d["mots"])
    n_son = sum("son" in m for m in d["mots"])
    print(f"{len(d['mots'])} mots · {n_img} croquis · {n_son} voix · "
          f"{len(d['langues'])} langues d'appui → {SORTIE.relative_to(RACINE)}")


GABARIT = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>%%NOM%% — les mots du restaurant</title>
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<style>
/* Page produite par build/restaurant_planches.py — ne pas l'éditer. */
:root{
  /* Palette PROVISOIRE « brique » (30 sept. 2026, à faire trancher comme
     Francœur l'a fait sur sa page de couleurs) : pas le mauve de francis.
     Brique pour l'action et l'enseigne, orange pour les pièges, fond crème.
     Brique sur blanc ≈ 9:1 ; texte discret ≥ 4,5:1 sur le fond. */
  --surface-page:#F5F0EA;--surface-card:#FFFFFF;--text-strong:#241A14;--text-body:#241A14;
  --line-200:#E4DAD0;--line-300:#CDBFB2;--accent:#8A2E1C;--text-muted:#5E5046;
  --warn-bg:#FBE9DC;--warn-line:#C8692A;--warn-ink:#8A3F0F;
  --rj-teinte:#8A2E1C;--rj-fond:#F3E3DC}
.fr-barre .fr-desc{color:var(--rj-teinte)}
body{margin:0;background:var(--surface-page);color:var(--text-body);font-family:Nunito,system-ui,sans-serif}
.rj{max-width:1080px;margin:0 auto;padding:18px 16px 60px}
.fr-barre .fr-barre__in{max-width:1080px;padding-left:16px;padding-right:16px}
.rj-tete{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.rj-enseigne{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--rj-teinte);margin:0}
.rj h1{font-size:28px;line-height:1.15;margin:4px 0 0;color:var(--text-strong)}
.appui{display:block;font-size:15px;font-weight:600;color:var(--text-muted);margin-top:3px}
.appui:empty{display:none}
.btn-rj{font:inherit;font-weight:700;font-size:15px;cursor:pointer;border-radius:10px;padding:9px 14px;min-height:44px;
  border:1px solid var(--line-300);background:var(--surface-card);color:var(--text-strong);display:inline-flex;gap:8px;align-items:center}
.btn-rj:hover{border-color:var(--rj-teinte)}
.btn-rj--pri{background:var(--accent);border-color:var(--accent);color:#fff}
.btn-rj--pri .appui{color:#fff;opacity:.9}
.btn-rj svg{width:20px;height:20px;flex:none}
.btn-rj .appui{font-size:12px;margin:0}
.btn-rj--pile{flex-direction:column;align-items:flex-start;gap:0}

/* La langue */
.sans-trad{font:inherit;cursor:pointer;text-align:start;margin-top:18px;width:100%;max-width:520px;padding:16px 18px;border-radius:12px;
  border:2px solid var(--rj-teinte);background:var(--rj-fond);font-size:22px;font-weight:900;color:var(--text-strong)}
.sans-trad small{display:block;font-size:15px;font-weight:700;color:var(--rj-teinte)}
.langues{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;margin-top:12px;max-width:520px}
.langues button{font:inherit;cursor:pointer;text-align:start;padding:14px 16px;border-radius:12px;
  border:1px solid var(--line-300);background:var(--surface-card);font-size:20px;font-weight:800;color:var(--text-strong)}
.langues button:hover,.langues button:focus-visible{border-color:var(--rj-teinte);background:var(--rj-fond)}

/* Les planches */
.planches{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px;margin-top:16px}
.pl{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:6px;color:var(--text-body)}
.pl:hover{border-color:var(--rj-teinte)}
.pl .vign{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;background:#fff;border-radius:10px;padding:6px}
.pl .vign img{width:100%;aspect-ratio:1/1;object-fit:contain;display:block}
.pl .vign i{display:grid;place-items:center;aspect-ratio:1/1;border-radius:6px;background:var(--rj-fond);color:var(--rj-teinte)}
.pl .vign i svg{width:40%;height:40%}
.pl .large{width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:10px;display:block}
.pl.poste{grid-column:1/-1;flex-direction:row;align-items:center;gap:16px;border-color:var(--rj-teinte);box-shadow:inset 4px 0 0 var(--rj-teinte)}
.pl.poste .large{width:min(360px,45%)}
.pl b{font-size:17px;color:var(--text-strong)}
.pl .n{font-size:13px;color:var(--text-muted);font-weight:600}
.etiq{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;color:var(--rj-teinte);background:var(--rj-fond);border-radius:6px;padding:2px 7px;align-self:flex-start}

/* Une planche */
.planche{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin-top:14px}
.art{font:inherit;cursor:pointer;position:relative;border:1px solid var(--line-200);background:#fff;border-radius:12px;
  padding:8px 8px 10px;display:flex;flex-direction:column;gap:4px;text-align:center;color:#17181A}
.art:hover,.art:focus-visible{border-color:var(--rj-teinte);box-shadow:0 0 0 3px var(--rj-fond)}
.art .num{position:absolute;top:6px;inset-inline-start:8px;font-size:13px;font-weight:800;color:var(--text-muted)}
.art img{width:100%;aspect-ratio:1/1;object-fit:contain;border-radius:8px}
.art .sans{display:grid;place-items:center;aspect-ratio:3/2;margin:18px 0 10px;background:var(--rj-fond);border-radius:8px;color:var(--rj-teinte)}
.art .sans svg{width:34px;height:34px}
.art .mot{font-weight:800;font-size:16px;line-height:1.2}
.art.piege{box-shadow:inset 0 3px 0 var(--warn-line)}
.art .dec{margin:18px 0 10px}

/* Le décor et ses zones */
.decor{position:relative;margin-top:14px;background:#fff;border-radius:14px;overflow:hidden;border:1px solid var(--line-200)}
.decor img{width:100%;display:block}
.zone{position:absolute;font:inherit;cursor:pointer;border:3px solid transparent;border-radius:10px;background:transparent;padding:0}
.zone:hover,.zone:focus-visible{border-color:var(--rj-teinte);background:rgba(138,46,28,.08)}
.zone .pastille{position:absolute;top:-2px;inset-inline-start:-2px;min-width:26px;height:26px;border-radius:13px;background:var(--rj-teinte);color:#fff;font-weight:900;font-size:14px;display:grid;place-items:center;padding:0 6px}
.zliste{list-style:none;padding:0;margin:14px 0 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px}
.zliste button{font:inherit;cursor:pointer;width:100%;text-align:start;display:flex;gap:10px;align-items:center;border:1px solid var(--line-200);background:var(--surface-card);border-radius:10px;padding:8px 12px;min-height:44px;font-weight:800;color:var(--text-strong)}
.zliste .pastille{flex:none;min-width:26px;height:26px;border-radius:13px;background:var(--rj-teinte);color:#fff;font-size:14px;display:grid;place-items:center}
.mini{position:relative;border-radius:8px;overflow:hidden}
.mini img{width:100%;display:block;aspect-ratio:auto}
.mini i{position:absolute;border:3px solid var(--rj-teinte);border-radius:6px;box-shadow:0 0 0 999px rgba(255,255,255,.45)}

/* La fiche d'un mot */
.fiche{position:fixed;inset:0;background:rgba(23,24,26,.55);display:grid;place-items:center;padding:16px;z-index:10}
.fiche[hidden]{display:none}
.carte{background:var(--surface-card);border-radius:16px;max-width:520px;width:100%;max-height:100%;overflow:auto;padding:16px;box-sizing:border-box}
.carte .grand{background:#fff;border-radius:12px;display:grid;place-items:center;border:1px solid var(--line-200)}
.carte .grand > img{width:100%;max-width:360px;aspect-ratio:1/1;object-fit:contain}
.carte .grand .mini{width:100%}
.carte .grand .sans{padding:26px;color:var(--rj-teinte)}
.carte .grand .sans svg{width:48px;height:48px}
.carte h2{font-size:30px;margin:12px 0 0;color:var(--text-strong)}
.carte .autre{margin:4px 0 0;color:var(--text-muted);font-weight:600;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.carte .autre b{color:var(--text-body)}
.carte .gestes{display:flex;flex-wrap:wrap;gap:12px;margin:14px 0 6px}
.carte .trad{margin-top:8px;padding:12px 14px;border-radius:12px;background:var(--rj-fond);font-size:22px;font-weight:800;color:var(--text-strong)}
.carte .trad[hidden]{display:none}
.carte .trad small{display:block;font-size:15px;font-weight:600;color:var(--text-body);margin-top:6px}
.carte .trad .relu{display:block;font-size:12px;font-weight:600;color:var(--text-muted);margin-top:8px}
.carte .piege{margin-top:10px;padding:10px 12px;border-radius:10px;background:var(--warn-bg);border:1px solid var(--warn-line);color:var(--warn-ink);font-size:15px;font-weight:700}
.carte .note{margin-top:10px;font-size:15px;color:var(--text-body)}
.carte .nav{display:flex;justify-content:space-between;gap:12px;margin-top:14px}
.ferme{float:inline-end}
.petit{padding:6px 10px;min-height:36px;font-size:14px}

.secteur{display:flex;flex-direction:column;align-items:flex-end;text-align:right;line-height:1.15}
.secteur small{font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted)}
.secteur b{font-size:19px;font-weight:900;color:var(--rj-teinte)}
.secteur .court{display:none}
@media (max-width:640px){
  .rj h1{font-size:23px}
  .planche,.planches{grid-template-columns:repeat(2,minmax(0,1fr))}
  .pl.poste{flex-direction:column;align-items:stretch}
  .pl.poste .large{width:100%}
  .zone .pastille{min-width:22px;height:22px;font-size:12px}
}
@media (max-width:480px){.secteur small{display:none}.secteur b{font-size:16px}.secteur .long{display:none}.secteur .court{display:inline}}
</style>
</head>
<body>
<div class="fr-barre"><div class="fr-barre__in">
  <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">Aide à l'apprentissage du français</span></span>
  <span class="secteur"><small>%%SURTITRE%%</small><b><span class="long">%%SECTEUR%%</span><span class="court">%%SECTEUR_COURT%%</span></b></span>
</div></div>
<main class="rj" id="app"></main>
<div class="fiche" id="fiche" hidden><div class="carte" role="dialog" aria-modal="true" aria-labelledby="ficheMot" id="carte"></div></div>
<script>
(function(){
const D = %%DONNEES%%;
const NOM = %%NOM_JS%%;
const CLE = 'francisation-langue';
const ICO = {
  son:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4z"/><path d="M16.5 8.5a5 5 0 0 1 0 7"/><path d="M19 6a8.5 8.5 0 0 1 0 12"/></svg>',
  oeil:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
  x:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
  g:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>',
  d:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg>'
};
const FR = {choisir:'Choisissez votre langue',choisir_sous:'Les mots restent en français. Votre langue vous aide à comprendre.',
  francais_seul:'Français seulement',francais_seul_sous:'Sans traduction',planches:'Les planches du restaurant',
  planches_sous:'Touchez une planche, puis un mot pour l’entendre.',cuisine:'Cuisine',salle:'Salle',deux:'Cuisine et salle',
  toucher:'Touchez un mot pour l’entendre.',ecouter:'Écouter',voir:'Voir dans ma langue',cacher:'Cacher',retour:'Toutes les planches',
  langue:'Changer de langue',non_relu:'Traduction pas encore vérifiée par une personne.',piege:'Attention',aussi:'On entend aussi',
  suivant:'Suivant',precedent:'Précédent',mots:'mots',decor:'Dans la cuisine',decor_sous:'Touchez un endroit du poste pour entendre son nom.',fermer:'Fermer'};
D.planches.forEach(p => FR['p_' + p.k] = p.t);
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const app = $('#app'), fiche = $('#fiche'), carte = $('#carte');
const parId = Object.fromEntries(D.mots.map(m => [m.id, m]));
let langue = null, liste = [], rang = 0, retourFocus = null, courante = null;
const audio = new Audio();

function lireLangue(){ try { return localStorage.getItem(CLE); } catch(e){ return null; } }
function poserLangue(c){ try { localStorage.setItem(CLE, c); } catch(e){} }
function L(){ return D.langues.find(l => l.c === langue) || null; }
// Une consigne : le français, puis l'appui DESSOUS (jamais à sa place).
function t(k){ const l = L(); const a = l && l.ui[k]; return esc(FR[k]) + (a ? '<span class="appui" lang="' + l.c + '">' + esc(a) + '</span>' : ''); }
function tb(k){ const l = L(); const a = l && l.ui[k]; return '<span>' + esc(FR[k]) + '</span>' + (a ? '<span class="appui" lang="' + l.c + '">' + esc(a) + '</span>' : ''); }
function jouer(src){ if (!src) return; try { audio.pause(); audio.src = src; audio.currentTime = 0; audio.play().catch(()=>{}); } catch(e){} }

function adresse(o){
  const u = new URL(location.href);
  ['planche','mot'].forEach(k => u.searchParams.delete(k));
  Object.entries(o || {}).forEach(([k,v]) => v && u.searchParams.set(k, v));
  history.replaceState(null, '', u);
}
function tete(titreK, sousK, retour){
  return '<div class="rj-tete"><div><p class="rj-enseigne">' + esc(NOM) + '</p><h1>' + t(titreK) + '</h1>'
    + (sousK ? '<p style="margin:6px 0 0">' + t(sousK) + '</p>' : '') + '</div><div style="display:flex;gap:8px;flex-wrap:wrap">'
    + (retour ? '<button class="btn-rj btn-rj--pile" data-act="accueil">' + tb('retour') + '</button>' : '')
    + '<button class="btn-rj btn-rj--pile" data-act="langue">' + tb('langue') + '</button></div></div>';
}

function ecranLangue(){
  adresse({});
  app.innerHTML = '<div class="rj-tete"><div><p class="rj-enseigne">' + esc(NOM) + '</p><h1>' + esc(FR.choisir) + '</h1>'
    + '<p style="margin:6px 0 0">' + esc(FR.choisir_sous) + '</p></div></div>'
    + '<button class="sans-trad" data-lang="fr">' + esc(FR.francais_seul) + '<small>' + esc(FR.francais_seul_sous) + '</small></button>'
    + '<div class="langues">' + D.langues.map(l => '<button data-lang="' + l.c + '" lang="' + l.c + '">' + esc(l.loc) + '</button>').join('') + '</div>';
  app.querySelector('button').focus();
}

function vignettes(p){
  const ms = D.mots.filter(m => m.p === p.k);
  const avec = ms.filter(m => m.img).slice(0, 6);
  let v = avec.map(m => '<img src="' + m.img + '" alt="" loading="lazy">').join('');
  // Une planche sans croquis (les repas, le quart) : des mots à entendre.
  for (let i = avec.length; i < 3; i++) v += '<i>' + ICO.son + '</i>';
  return '<span class="vign">' + v + '</span>';
}
function accueil(){
  adresse({});
  const posteN = D.zones.length;
  app.innerHTML = tete('planches', 'planches_sous', false)
    + '<div class="planches">'
    + '<button class="pl poste" data-planche="poste"><img class="large" src="' + D.poste + '" alt=""><span><span class="etiq">' + esc(FR.cuisine) + '</span><br><b>' + t('decor') + '</b><br><span class="n">' + posteN + ' ' + esc(FR.mots) + '</span></span></button>'
    + D.planches.map(p => {
        const n = D.mots.filter(m => m.p === p.k).length;
        return '<button class="pl" data-planche="' + p.k + '"><span class="etiq">' + esc(FR[p.poste]) + '</span>' + vignettes(p)
          + '<b>' + t('p_' + p.k) + '</b><span class="n">' + n + ' ' + esc(FR.mots) + '</span></button>';
      }).join('') + '</div>';
}

function illustration(m, grand){
  if (m.img) return '<img src="' + m.img + '" alt="">';
  if (m.zone) {
    const [x,y,w,h] = m.zone;
    return '<span class="mini' + (grand ? '' : ' dec') + '"><img src="' + D.poste + '" alt=""><i style="left:' + x + '%;top:' + y + '%;width:' + w + '%;height:' + h + '%"></i></span>';
  }
  return '<span class="sans">' + ICO.son + '</span>';
}
function planche(k){
  courante = k;
  adresse({planche: k});
  if (k === 'poste') return decor();
  const p = D.planches.find(x => x.k === k);
  if (!p) return accueil();
  liste = D.mots.filter(m => m.p === k);
  app.innerHTML = tete('p_' + k, 'toucher', true)
    + '<div class="planche">' + liste.map((m, i) =>
      '<button class="art' + (m.piege ? ' piege' : '') + '" data-i="' + i + '"><span class="num">' + (i + 1) + '</span>'
      + illustration(m, false) + '<span class="mot">' + esc(m.mot) + '</span></button>').join('') + '</div>';
}
function decor(){
  liste = D.zones.map(id => parId[id]);
  app.innerHTML = tete('decor', 'decor_sous', true)
    + '<div class="decor"><img src="' + D.poste + '" alt="">' + liste.map((m, i) => {
      const [x,y,w,h] = m.zone;
      return '<button class="zone" data-i="' + i + '" aria-label="' + (i + 1) + ' — ' + esc(m.mot) + '" style="left:' + x + '%;top:' + y + '%;width:' + w + '%;height:' + h + '%"><span class="pastille">' + (i + 1) + '</span></button>';
    }).join('') + '</div>'
    // Sur téléphone, les zones se serrent : la liste numérotée les double.
    + '<ol class="zliste">' + liste.map((m, i) => '<li><button data-i="' + i + '"><span class="pastille">' + (i + 1) + '</span>' + esc(m.mot) + '</button></li>').join('') + '</ol>';
}

function ouvrir(i){
  rang = i;
  const m = liste[i];
  adresse({planche: courante, mot: m.id});
  const l = L(), tr = l && l.mots[m.id];
  const note = m.note ? m.note.replace(/^PIÈGE\s*:\s*/, '') : '';
  carte.innerHTML = '<button class="btn-rj ferme petit" data-act="fermer" aria-label="' + esc(FR.fermer) + '">' + ICO.x + '</button>'
    + '<div class="grand">' + illustration(m, true) + '</div>'
    + '<h2 id="ficheMot">' + esc(m.mot) + '</h2>'
    + (m.autre ? '<p class="autre">' + esc(FR.aussi) + ' : <b>' + esc(m.autre) + '</b>'
        + (m.autre_son ? ' <button class="btn-rj petit" data-act="autre" aria-label="' + esc(FR.ecouter) + ' : ' + esc(m.autre) + '">' + ICO.son + '</button>' : '') + '</p>' : '')
    + '<div class="gestes">' + (m.son ? '<button class="btn-rj btn-rj--pri btn-rj--pile" data-act="ecouter">' + tb('ecouter') + '</button>' : '')
    + (tr ? '<button class="btn-rj btn-rj--pile" data-act="voir" aria-expanded="false">' + tb('voir') + '</button>' : '') + '</div>'
    + (tr ? '<div class="trad" id="trad" hidden lang="' + l.c + '">' + esc(tr[0]) + (tr[1] ? '<small>' + esc(tr[1]) + '</small>' : '')
        + (l.relu ? '' : '<span class="relu">' + t('non_relu') + '</span>') + '</div>' : '')
    + (note ? (m.piege ? '<div class="piege">' + esc(FR.piege) + ' : ' + esc(note) + '</div>' : '<p class="note">' + esc(note) + '</p>') : '')
    + '<div class="nav"><button class="btn-rj petit" data-act="prec" ' + (i ? '' : 'disabled') + '>' + ICO.g + esc(FR.precedent) + '</button>'
    + '<button class="btn-rj petit" data-act="suiv" ' + (i < liste.length - 1 ? '' : 'disabled') + '>' + esc(FR.suivant) + ICO.d + '</button></div>';
  if (fiche.hidden) retourFocus = document.activeElement;
  fiche.hidden = false;
  carte.querySelector('[data-act=ecouter]') ? carte.querySelector('[data-act=ecouter]').focus() : carte.querySelector('[data-act=fermer]').focus();
  jouer(m.son);
}
function fermer(){
  fiche.hidden = true; audio.pause();
  adresse({planche: courante});
  if (retourFocus && document.contains(retourFocus)) retourFocus.focus();
}

app.addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  if (b.dataset.lang) { langue = b.dataset.lang === 'fr' ? null : b.dataset.lang; poserLangue(b.dataset.lang); return accueil(); }
  if (b.dataset.act === 'langue') return ecranLangue();
  if (b.dataset.act === 'accueil') return accueil();
  if (b.dataset.planche) { planche(b.dataset.planche); window.scrollTo(0, 0); return; }
  if (b.dataset.i != null) return ouvrir(+b.dataset.i);
});
carte.addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  const m = liste[rang];
  if (b.dataset.act === 'fermer') return fermer();
  if (b.dataset.act === 'ecouter') return jouer(m.son);
  if (b.dataset.act === 'autre') return jouer(m.autre_son);
  if (b.dataset.act === 'prec' && rang > 0) return ouvrir(rang - 1);
  if (b.dataset.act === 'suiv' && rang < liste.length - 1) return ouvrir(rang + 1);
  if (b.dataset.act === 'voir') {
    const tr = $('#trad'), vu = tr.hidden; tr.hidden = !vu;
    b.setAttribute('aria-expanded', vu); b.innerHTML = tb(vu ? 'cacher' : 'voir');
  }
});
fiche.addEventListener('click', e => { if (e.target === fiche) fermer(); });
document.addEventListener('keydown', e => {
  if (fiche.hidden) return;
  if (e.key === 'Escape') fermer();
  if (e.key === 'ArrowRight' && rang < liste.length - 1) ouvrir(rang + 1);
  if (e.key === 'ArrowLeft' && rang > 0) ouvrir(rang - 1);
  if (e.key === 'Tab') {  // le focus reste dans la fiche
    const f = [...carte.querySelectorAll('button:not([disabled])')];
    if (!f.length) return;
    if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
    else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
  }
});

// Démarrage : la langue de l'adresse, sinon celle déjà choisie, sinon le choix.
const q = new URLSearchParams(location.search);
const choisie = q.get('langue') || lireLangue();
window.__resto = {D, etat: () => ({langue, planche: q.get('planche'), liste: liste.map(m => m.id), rang, ouverte: !fiche.hidden})};
if (!choisie || (choisie !== 'fr' && !D.langues.some(l => l.c === choisie))) { ecranLangue(); return; }
langue = choisie === 'fr' ? null : choisie;
if (q.get('planche')) {
  planche(q.get('planche'));
  const i = liste.findIndex(m => m.id === q.get('mot'));
  if (i >= 0) ouvrir(i);
} else accueil();
})();
</script>
</body>
</html>
"""
GABARIT = GABARIT.replace("%%NOM_JS%%", json.dumps(IDE.NOM, ensure_ascii=False))

if __name__ == "__main__":
    main()
