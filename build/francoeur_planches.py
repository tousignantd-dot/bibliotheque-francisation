#!/usr/bin/env python3
"""Les planches de la Maison Francœur — l'écran de l'employé (étape 1).

    python3 build/francoeur_planches.py   # → modules-autonomes/francoeur-planches/index.html

Produite, jamais écrite à la main. Elle lit trois sources, et rien d'autre :
  build/contenu/entreprise-francoeur/lexique.py        les mots
  build/contenu/entreprise-francoeur/traductions.json  les onze langues, figées
  assets/interactive/francoeur/{croquis,sons}/         ce qui existe sur le disque

LE PARCOURS : choisir sa langue (une fois, gardée sous `francisation-langue`,
la clé que partagent déjà les modules) → les onze rayons → une planche
numérotée → un article : le croquis, le mot d'ici, l'autre mot, le bouton
d'écoute, et « Voir dans ma langue ».

LES TROIS COUCHES, qui ne se confondent pas :
  - le mot à apprendre ne se traduit jamais à sa place : il reste en tête ;
  - la consigne de l'écran s'écrit en français, sa langue d'appui DESSOUS ;
  - la traduction du mot est MASQUÉE par défaut — visible d'emblée, le
    français ne serait plus traité.

LA PLANCHE EST COMPOSÉE, pas engendrée : chaque croquis est un fichier à lui,
posé dans une grille numérotée. C'est ce qui permet à un exercice de désigner
« le numéro 7 », et de corriger un seul dessin sans refaire les onze autres.
"""
import html, json, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-francoeur"
sys.path.insert(0, str(CONTENU))
sys.path.insert(0, str(RACINE / "build"))
from lexique import LEXIQUE, PLANCHES, verifier  # noqa: E402
from francoeur_etape0 import TEINTES, MOTIFS  # noqa: E402
from demandes import DEMANDES, COULEURS_DISTRACTRICES, TAILLES  # noqa: E402
import random  # noqa: E402

CROQUIS = RACINE / "assets" / "interactive" / "francoeur" / "croquis"
SONS = RACINE / "assets" / "interactive" / "francoeur" / "sons"
SORTIE = RACINE / "modules-autonomes" / "francoeur-planches" / "index.html"

# Incrémenter après toute image ou tout son refait : même nom, même adresse,
# le navigateur servirait l'ancien sans rien dire.
MEDIA_V = "1"


def donnees():
    trad = json.loads((CONTENU / "traductions.json").read_text(encoding="utf-8"))
    mots = []
    for ident, planche, mot, autre, dessin, note in LEXIQUE:
        m = {"id": ident, "p": planche, "mot": mot, "autre": autre, "note": note,
             "piege": note.startswith("PIÈGE")}
        if dessin == "croquis" and (CROQUIS / f"{ident}.jpg").exists():
            m["img"] = f"/assets/interactive/francoeur/croquis/{ident}.jpg?v={MEDIA_V}"
        elif dessin == "pastille":
            m["pastille"] = MOTIFS.get(ident) or f"background:{TEINTES[ident]}"
        if (SONS / f"{ident}.mp3").exists():
            m["son"] = f"/assets/interactive/francoeur/sons/{ident}.mp3?v={MEDIA_V}"
        mots.append(m)
    langues = [{"c": c, "loc": v["loc"], "rtl": v["rtl"], "relu": v["relu"],
                "ui": v.get("interface", {}),
                "mots": {k: [t["mot"], t["note"]] for k, t in v["mots"].items()}}
               for c, v in trad.items()]
    return {"planches": [{"k": k, "t": t} for k, t in PLANCHES], "mots": mots,
            "langues": langues, "demandes": demandes(mots)}


ETIQUETTE = {"tp": "TP", "p": "P", "m": "M", "g": "G", "tg": "TG"}


def demandes(mots):
    """Les quatre variantes de chaque demande, DÉDUITES et non écrites : chaque
    distracteur ne diffère de la bonne réponse que par UN attribut. Tirage semé
    sur l'id, pour que deux constructions rendent la même page."""
    par_id = {m["id"]: m for m in mots}
    planche = {e[0]: e[1] for e in LEXIQUE}
    sortie = []
    for ident, _voix, phrase, art, coul, taille in DEMANDES:
        assert art in par_id and "img" in par_id[art], f"{ident} : {art} sans croquis"
        assert coul in TEINTES, f"{ident} : couleur {coul} inconnue"
        r = random.Random(ident)
        autres_c = [c for c in COULEURS_DISTRACTRICES if c != coul]
        voisins = [e[0] for e in LEXIQUE if e[1] == planche[art] and e[0] != art
                   and "img" in par_id[e[0]]]
        v = [(art, coul, taille)]
        v.append((art, r.choice(autres_c), taille))                 # la couleur change
        if taille:
            i = TAILLES.index(taille)
            proches = [TAILLES[j] for j in (i - 1, i + 1) if 0 <= j < len(TAILLES)]
            v.append((art, coul, r.choice(proches)))                # la taille change
        else:
            v.append((art, r.choice([c for c in autres_c if c != v[1][1]]), None))
        v.append((r.choice(voisins), coul, taille))                 # l'article change
        sortie.append({"id": ident, "phrase": phrase,
                       "son": f"/assets/interactive/francoeur/sons/demandes/{ident}.mp3?v={MEDIA_V}",
                       "v": [{"a": a, "img": par_id[a]["img"], "mot": par_id[a]["mot"],
                              "c": c, "cmot": par_id[c]["mot"], "hex": TEINTES[c],
                              "t": ETIQUETTE.get(t) if t else None} for a, c, t in v]})
    return sortie


def main():
    verifier()
    d = donnees()
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    page = GABARIT.replace("%%DONNEES%%", json.dumps(d, ensure_ascii=False, separators=(",", ":")))
    SORTIE.write_text(page, encoding="utf-8")
    n_img = sum("img" in m for m in d["mots"])
    n_son = sum("son" in m for m in d["mots"])
    print(f"{SORTIE.relative_to(RACINE)} — {len(d['mots'])} mots, {n_img} croquis, "
          f"{n_son} sons, {len(d['langues'])} langues, {len(page)//1024} Ko")


GABARIT = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Maison Francœur — les vêtements</title>
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<style>
/* Page produite par build/francoeur_planches.py — ne pas l'éditer. */
:root{--mf-teinte:var(--acier-600);--mf-fond:var(--acier-100)}
body{margin:0;background:var(--surface-page);color:var(--text-body);font-family:Nunito,system-ui,sans-serif}
.mf{max-width:1080px;margin:0 auto;padding:18px 16px 60px}
.mf-tete{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.mf-enseigne{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--mf-teinte);margin:0}
.mf h1{font-size:28px;line-height:1.15;margin:4px 0 0;color:var(--text-strong)}
.appui{display:block;font-size:15px;font-weight:600;color:var(--text-muted);margin-top:3px}
.appui:empty{display:none}
[dir=rtl].appui,.appui[dir=rtl]{text-align:right}
.mf-btn{font:inherit;font-weight:700;font-size:15px;cursor:pointer;border-radius:10px;padding:9px 14px;
  border:1px solid var(--line-300);background:var(--surface-card);color:var(--text-strong);display:inline-flex;gap:8px;align-items:center}
.mf-btn:hover{border-color:var(--mf-teinte)}
.mf-btn--pri{background:var(--accent);border-color:var(--accent);color:#fff}
.mf-btn svg{width:20px;height:20px;flex:none}
.mf-btn .appui{font-size:12px;margin:0}
.mf-btn--pri .appui{color:#fff;opacity:.9}
.mf-btn--pile{flex-direction:column;align-items:flex-start;gap:0}

/* Choix de la langue */
.langues{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px;margin-top:18px}
.langues button{font:inherit;cursor:pointer;text-align:start;padding:14px 16px;border-radius:12px;
  border:1px solid var(--line-300);background:var(--surface-card);font-size:20px;font-weight:800;color:var(--text-strong)}
.langues button:hover,.langues button:focus-visible{border-color:var(--mf-teinte);background:var(--mf-fond)}
.langues button small{display:block;font-size:13px;font-weight:600;color:var(--text-muted)}

/* Les rayons */
.rayons{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin-top:16px}
.rayon{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:6px}
.rayon:hover{border-color:var(--mf-teinte)}
.rayon .vign{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;background:#fff;border-radius:10px;padding:6px}
.rayon .vign img,.rayon .vign i{width:100%;aspect-ratio:1/1;object-fit:contain;display:block;border-radius:6px}
.rayon b{font-size:17px;color:var(--text-strong)}
.rayon .n{font-size:13px;color:var(--text-muted);font-weight:600}

/* Une planche */
.planche{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin-top:14px}
.art{font:inherit;cursor:pointer;position:relative;border:1px solid var(--line-200);background:#fff;border-radius:12px;
  padding:8px 8px 10px;display:flex;flex-direction:column;gap:4px;text-align:center;color:#17181A}
.art:hover,.art:focus-visible{border-color:var(--mf-teinte);box-shadow:0 0 0 3px var(--mf-fond)}
.art .num{position:absolute;top:6px;inset-inline-start:8px;font-size:13px;font-weight:800;color:var(--ink-500)}
.art img,.art .past,.art .sans{width:100%;aspect-ratio:1/1;object-fit:contain;border-radius:8px}
.art .past{aspect-ratio:3/2;margin:18px 0 10px;border:1px solid var(--line-200)}
.art .sans{display:grid;place-items:center;aspect-ratio:3/2;margin:18px 0 10px;background:var(--surface-sunken);
  font-size:26px;font-weight:900;color:var(--ink-400)}
.art .mot{font-weight:800;font-size:16px;line-height:1.2}
.art.piege{box-shadow:inset 0 3px 0 var(--warn-line)}

/* La fiche d'un article */
.fiche{position:fixed;inset:0;background:rgba(23,24,26,.55);display:grid;place-items:center;padding:16px;z-index:10}
.fiche[hidden]{display:none}
.carte{background:var(--surface-card);border-radius:16px;max-width:520px;width:100%;max-height:100%;overflow:auto;padding:16px}
.carte .grand{background:#fff;border-radius:12px;display:grid;place-items:center}
.carte .grand img{width:100%;max-width:360px;aspect-ratio:1/1;object-fit:contain}
.carte .grand .past{width:100%;aspect-ratio:3/2;border-radius:12px}
.carte .grand .sans{padding:28px;font-size:34px;font-weight:900;color:var(--ink-400)}
.carte h2{font-size:30px;margin:12px 0 0;color:var(--text-strong)}
.carte .autre{margin:2px 0 0;color:var(--text-muted);font-weight:600}
.carte .autre b{color:var(--text-body)}
.carte .gestes{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 6px}
.carte .trad{margin-top:8px;padding:12px 14px;border-radius:12px;background:var(--mf-fond);font-size:22px;font-weight:800;color:var(--text-strong)}
.carte .trad[hidden]{display:none}
.carte .trad small{display:block;font-size:15px;font-weight:600;color:var(--text-body);margin-top:6px}
.carte .trad .relu{display:block;font-size:12px;font-weight:600;color:var(--text-muted);margin-top:8px}
.carte .piege{margin-top:10px;padding:10px 12px;border-radius:10px;background:var(--warn-bg);border:1px solid var(--warn-line);
  color:var(--warn-ink);font-size:15px;font-weight:700}
.carte .nav{display:flex;justify-content:space-between;gap:8px;margin-top:14px}
.ferme{float:inline-end}
/* Accueil et exercices */
.accueil{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin-top:18px}
.porte{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:16px;padding:18px;display:flex;flex-direction:column;gap:6px}
.porte:hover{border-color:var(--mf-teinte)}
.porte b{font-size:22px;color:var(--text-strong)}
.exos{display:grid;gap:10px;margin-top:14px}
.exo-porte{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:14px;padding:14px 16px;display:flex;gap:14px;align-items:center}
.exo-porte:hover{border-color:var(--mf-teinte)}
.exo-porte .rang{flex:none;width:34px;height:34px;border-radius:50%;display:grid;place-items:center;background:var(--mf-fond);color:var(--mf-teinte);font-weight:900}
.exo-porte b{font-size:18px;color:var(--text-strong)}
.exo-porte.pont{border-color:var(--mf-teinte);box-shadow:inset 4px 0 0 var(--mf-teinte)}
.filtre{margin-top:14px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.filtre select{font:inherit;font-size:16px;padding:8px 10px;border-radius:10px;border:1px solid var(--line-300);background:var(--surface-card);color:var(--text-strong)}
.jeu{margin-top:12px}
.jeu .barre{height:6px;border-radius:3px;background:var(--line-200);overflow:hidden;margin-bottom:12px}
.jeu .barre i{display:block;height:100%;background:var(--accent)}
.jeu .consigne{font-weight:700;margin:0 0 10px}
.jeu .sujet{background:#fff;border-radius:14px;border:1px solid var(--line-200);display:grid;place-items:center;padding:8px;max-width:320px;margin:0 auto 12px}
.jeu .sujet img{width:100%;max-width:260px;aspect-ratio:1/1;object-fit:contain}
.jeu .sujet .past{width:100%;aspect-ratio:3/2;border-radius:10px}
.jeu .ecoute{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:6px 0 14px}
.choix{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}
.choix.mots{grid-template-columns:1fr}
.opt{font:inherit;cursor:pointer;border:2px solid var(--line-200);background:#fff;border-radius:12px;padding:8px;color:#17181A;
  display:flex;flex-direction:column;align-items:center;gap:6px;position:relative}
.opt:hover{border-color:var(--mf-teinte)}
.opt img{width:100%;aspect-ratio:1/1;object-fit:contain}
.opt .past{width:100%;aspect-ratio:3/2;border-radius:8px;border:1px solid var(--line-200)}
.choix.mots .opt{flex-direction:row;justify-content:center;font-size:20px;font-weight:800;padding:14px}
.opt.gris img{filter:grayscale(1) contrast(.9) opacity(.75)}
.opt .attrs{display:flex;gap:8px;align-items:center;justify-content:center}
.opt .chip{width:34px;height:34px;border-radius:50%;border:2px solid #17181A33}
.opt .tag{font-weight:900;font-size:16px;border:2px solid #17181A;border-radius:6px;padding:2px 7px;background:#fff}
.opt.faux{border-color:var(--no-line);background:var(--no-bg);animation:non .3s}
.opt.juste{border-color:var(--ok-line);background:var(--ok-bg)}
.opt[disabled]{cursor:default}
@keyframes non{25%{transform:translateX(-5px)}75%{transform:translateX(5px)}}
@media (prefers-reduced-motion:reduce){.opt.faux{animation:none}}
.retro{margin:12px 0 0;font-weight:800;min-height:1.4em}
.retro.ok{color:var(--ok-ink)} .retro.non{color:var(--no-ink)}
.suite{display:flex;justify-content:flex-end;margin-top:12px}
.revele{text-align:center;margin:10px 0}
.revele .gros{font-size:30px;font-weight:900;color:var(--text-strong)}
.bilan{text-align:center;padding:20px 0}
.bilan .score{font-size:44px;font-weight:900;color:var(--text-strong)}

@media (max-width:640px){
  .mf h1{font-size:23px}
  .choix{grid-template-columns:repeat(2,minmax(0,1fr))}
  .planche{grid-template-columns:repeat(2,minmax(0,1fr))}
  .rayons{grid-template-columns:repeat(2,minmax(0,1fr))}
  .langues{grid-template-columns:repeat(2,minmax(0,1fr))}
  .langues button{font-size:17px;padding:12px}
}
@media (prefers-reduced-motion:no-preference){.art,.rayon{transition:border-color .15s,box-shadow .15s}}
</style>
</head>
<body>
<div class="fr-barre"><div class="fr-barre__in">
  <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">Aide à l'apprentissage du français</span></span>
</div></div>
<main class="mf" id="app"></main>
<div class="fiche" id="fiche" hidden><div class="carte" role="dialog" aria-modal="true" aria-labelledby="ficheMot" id="carte"></div></div>
<script>
const D = %%DONNEES%%;
const CLE = 'francisation-langue';
const ICO = {
  son:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4z"/><path d="M16.5 8.5a5 5 0 0 1 0 7"/><path d="M19 6a8.5 8.5 0 0 1 0 12"/></svg>',
  oeil:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
  retour:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>',
  suiv:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg>',
  globe:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/></svg>',
  ferme:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'
};
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
let langue = null;
try { langue = localStorage.getItem(CLE); } catch(e) {}
const L = () => D.langues.find(l => l.c === langue) || null;
// Une consigne : le français, et la langue d'appui dessous.
function dit(cle, fr) {
  const l = L(), t = l && l.ui[cle];
  return esc(fr) + (t ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '" lang="' + l.c + '">' + esc(t) + '</span>' : '');
}
const FR = {choisir:"Choisissez votre langue", choisir_sous:"Les mots restent en français. Votre langue vous aide à comprendre.",
  francais_seul:"Français seulement", rayons:"Les rayons du magasin", toucher:"Touchez un vêtement pour l'entendre.",
  ecouter:"Écouter", voir:"Voir dans ma langue", cacher:"Cacher", retour:"Retour aux rayons", langue:"Changer de langue",
  non_relu:"Traduction pas encore vérifiée par une personne.", piege:"Attention", aussi:"On entend aussi",
  suivant:"Suivant", precedent:"Précédent", mots:"mots",
  accueil:"Accueil", apprendre:"Apprendre les mots", apprendre_sous:"Les onze rayons, mot par mot.",
  exercer:"Je m'exerce", exercer_sous:"Cinq exercices, du mot au client.", exercices:"Les exercices",
  tous_rayons:"Tous les rayons",
  ex_ecoute:"Je l'entends, je le trouve", ex_ecoute_c:"Écoutez, puis touchez le bon vêtement.",
  ex_image:"Le mot et son image", ex_image_c:"Touchez le bon mot.",
  ex_rappel:"Je me souviens", ex_rappel_c:"Dites le mot à voix haute, puis vérifiez.",
  ex_rayon:"Range le rayon", ex_rayon_c:"Dans quel rayon va cet article ?",
  ex_client:"Ce que le client veut", ex_client_c:"Écoutez le client. Touchez ce qu'il demande.",
  reecouter:"Réécouter", lentement:"Plus lentement", voir_mot:"Voir le mot",
  savais:"Je le savais", a_revoir:"À revoir", bravo:"Bien joué !",
  essaie:"Pas tout à fait. Essayez encore.", reponse:"Voici la bonne réponse.",
  fin:"Série terminée", premier_coup:"du premier coup", recommencer:"Une autre série"};
const T = k => dit(k, FR[k]);
const app = document.getElementById('app');
let audio = null;
function joue(src) { if (!src) return; if (audio) audio.pause(); audio = new Audio(src); audio.play().catch(()=>{}); }

function image(m, grand) {
  if (m.img) return '<img src="' + m.img + '" alt="' + esc(m.mot) + '"' + (grand ? '' : ' loading="lazy"') + '>';
  if (m.pastille) return '<span class="past" style="' + m.pastille + '" aria-hidden="true"></span>';
  return '<span class="sans" aria-hidden="true">' + esc(m.mot.replace(/^(un |une |des |le |la |les |l')/, '').slice(0, 2).toUpperCase()) + '</span>';
}

function ecranLangue() {
  app.innerHTML = '<p class="mf-enseigne">Maison Francœur</p>'
    + '<h1>Choisissez votre langue</h1><p style="margin:6px 0 0">Les mots restent en français. Votre langue vous aide à comprendre.</p>'
    + '<div class="langues">' + D.langues.map(l => '<button type="button" data-l="' + l.c + '" lang="' + l.c + '" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">'
        + esc(l.loc) + (l.ui.choisir ? '<small>' + esc(l.ui.choisir) + '</small>' : '') + '</button>').join('')
    + '<button type="button" data-l="fr">Français<small>Français seulement</small></button></div>';
  app.querySelectorAll('[data-l]').forEach(b => b.onclick = () => {
    langue = b.dataset.l; try { localStorage.setItem(CLE, langue); } catch(e) {}
    ecranAccueil();
  });
}

function ecranAccueil() {
  app.innerHTML = tete('Bienvenue', '', false)
    + '<div class="accueil">'
    + '<button type="button" class="porte" id="aRayons"><b>' + T('apprendre') + '</b><span>' + T('apprendre_sous') + '</span></button>'
    + '<button type="button" class="porte" id="aExos"><b>' + T('exercer') + '</b><span>' + T('exercer_sous') + '</span></button></div>';
  document.getElementById('aRayons').onclick = ecranRayons;
  document.getElementById('aExos').onclick = ecranExercices;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}


function tete(titre, sous, retour, cleRetour) {
  return '<div class="mf-tete"><div><p class="mf-enseigne">Maison Francœur</p><h1>' + titre + '</h1>'
    + (sous ? '<p style="margin:6px 0 0">' + sous + '</p>' : '') + '</div><div style="display:flex;gap:8px;flex-wrap:wrap">'
    + (retour ? '<button type="button" class="mf-btn mf-btn--pile" id="retour">' + T(cleRetour || 'retour') + '</button>' : '')
    + '<button type="button" class="mf-btn mf-btn--pile" id="chLangue">' + T('langue') + '</button></div></div>';
}

function ecranRayons() {
  const l = L();
  app.innerHTML = tete(T('rayons'), T('toucher'), true, 'accueil')
    + '<div class="rayons">' + D.planches.map(p => {
        const ms = D.mots.filter(m => m.p === p.k), v = ms.filter(m => m.img || m.pastille).slice(0, 3);
        const tr = l && l.ui['planche_' + p.k];
        return '<button type="button" class="rayon" data-p="' + p.k + '"><span class="vign">'
          + v.map(m => m.img ? '<img src="' + m.img + '" alt="" loading="lazy">' : '<i style="' + m.pastille + '"></i>').join('')
          + '</span><b>' + esc(p.t) + (tr ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(tr) + '</span>' : '') + '</b>'
          + '<span class="n">' + ms.length + ' ' + FR.mots + '</span></button>';
      }).join('') + '</div>';
  app.querySelectorAll('[data-p]').forEach(b => b.onclick = () => ecranPlanche(b.dataset.p));
  document.getElementById('retour').onclick = ecranAccueil;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}

let courante = [];
function ecranPlanche(k) {
  const p = D.planches.find(x => x.k === k), l = L(), tr = l && l.ui['planche_' + k];
  courante = D.mots.filter(m => m.p === k);
  app.innerHTML = tete(esc(p.t) + (tr ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(tr) + '</span>' : ''), T('toucher'), true)
    + '<div class="planche">' + courante.map((m, i) =>
        '<button type="button" class="art' + (m.piege ? ' piege' : '') + '" data-i="' + i + '"><span class="num">' + (i + 1) + '</span>'
        + image(m) + '<span class="mot">' + esc(m.mot) + '</span></button>').join('') + '</div>';
  app.querySelectorAll('[data-i]').forEach(b => b.onclick = () => ouvrir(+b.dataset.i));
  document.getElementById('retour').onclick = ecranRayons;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}

const fiche = document.getElementById('fiche'), carte = document.getElementById('carte');
let ouvert = -1, avant = null;
function ouvrir(i) {
  if (ouvert < 0) avant = document.activeElement;
  ouvert = i; const m = courante[i], l = L(), t = l && l.mots[m.id];
  carte.innerHTML = '<button type="button" class="mf-btn ferme" id="ferme" aria-label="Fermer">' + ICO.ferme + '</button>'
    + '<div class="grand">' + image(m, true) + '</div>'
    + '<h2 id="ficheMot">' + esc(m.mot) + '</h2>'
    + (m.autre ? '<p class="autre">' + esc(FR.aussi) + ' : <b>' + esc(m.autre) + '</b></p>' : '')
    + '<div class="gestes">'
    + (m.son ? '<button type="button" class="mf-btn mf-btn--pri" id="ecoute">' + ICO.son + '<span>' + T('ecouter') + '</span></button>' : '')
    + (t ? '<button type="button" class="mf-btn" id="voir" aria-expanded="false">' + ICO.oeil + '<span>' + T('voir') + '</span></button>' : '')
    + '</div>'
    + (t ? '<div class="trad" id="trad" hidden lang="' + l.c + '" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(t[0])
        + (t[1] ? '<small>' + esc(t[1]) + '</small>' : '')
        + (l.relu ? '' : '<span class="relu" dir="ltr" lang="fr">' + esc(FR.non_relu) + (l.ui.non_relu ? ' · <span dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(l.ui.non_relu) + '</span>' : '') + '</span>')
        + '</div>' : '')
    + (m.piege && !(t && t[1]) ? '<p class="piege">' + esc(m.note.replace(/^PIÈGE\s*:\s*/, '')) + '</p>' : '')
    + '<div class="nav"><button type="button" class="mf-btn" id="prec"' + (i ? '' : ' disabled') + '>' + ICO.retour + FR.precedent + '</button>'
    + '<button type="button" class="mf-btn" id="suiv"' + (i < courante.length - 1 ? '' : ' disabled') + '>' + FR.suivant + ICO.suiv + '</button></div>';
  fiche.hidden = false;
  document.getElementById('ferme').onclick = fermer;
  const e = document.getElementById('ecoute'); if (e) e.onclick = () => joue(m.son);
  const v = document.getElementById('voir');
  if (v) v.onclick = () => { const tr = document.getElementById('trad'); tr.hidden = !tr.hidden; v.setAttribute('aria-expanded', String(!tr.hidden)); };
  document.getElementById('prec').onclick = () => ouvrir(i - 1);
  document.getElementById('suiv').onclick = () => ouvrir(i + 1);
  (e || document.getElementById('ferme')).focus();
  joue(m.son);
}
function fermer() { fiche.hidden = true; ouvert = -1; if (audio) audio.pause(); if (avant) avant.focus(); }
fiche.addEventListener('click', ev => { if (ev.target === fiche) fermer(); });
document.addEventListener('keydown', ev => {
  if (fiche.hidden) return;
  if (ev.key === 'Escape') fermer();
  if (ev.key === 'ArrowRight' && ouvert < courante.length - 1) ouvrir(ouvert + 1);
  if (ev.key === 'ArrowLeft' && ouvert > 0) ouvrir(ouvert - 1);
});


/* ── Les exercices ─────────────────────────────────────────────────────
   Cinq, du mot isolé à la phrase du client. Une série = 8 questions.
   Deux essais, puis la bonne réponse se montre (règle du dépôt : jamais la
   réponse au premier envoi). Les mots ratés vont dans « à revoir » et
   repassent devant à la série suivante. Tout reste sur l'appareil. */
const EXOS = [
  {k:'ecoute', n:1}, {k:'image', n:2}, {k:'rappel', n:3}, {k:'rayon', n:4}, {k:'client', n:5, pont:true}];
const RAYONS = ['hauts','bas','robes','exterieur','dessous','chaussures','accessoires'];
const SERIE = 8;
const CLE_REVOIR = 'francoeur-revoir';
let revoir = new Set();
try { revoir = new Set(JSON.parse(localStorage.getItem(CLE_REVOIR) || '[]')); } catch(e) {}
const garderRevoir = () => { try { localStorage.setItem(CLE_REVOIR, JSON.stringify([...revoir])); } catch(e) {} };
let filtre = '';
const melange = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const visuel = m => m.img || m.pastille;
function tirage(pool) {
  // Les mots « à revoir » d'abord, puis le reste au hasard.
  const a = melange(pool.filter(m => revoir.has(m.id))), b = melange(pool.filter(m => !revoir.has(m.id)));
  return a.concat(b).slice(0, SERIE);
}

function ecranExercices() {
  app.innerHTML = tete(T('exercices'), '', true, 'accueil')
    + '<div class="filtre"><select id="filtre" aria-label="' + esc(FR.tous_rayons) + '"><option value="">' + esc(FR.tous_rayons) + '</option>'
    + D.planches.filter(p => RAYONS.includes(p.k) || p.k === 'couleurs').map(p => '<option value="' + p.k + '"' + (filtre === p.k ? ' selected' : '') + '>' + esc(p.t) + '</option>').join('')
    + '</select></div><div class="exos">'
    + EXOS.map(x => '<button type="button" class="exo-porte' + (x.pont ? ' pont' : '') + '" data-x="' + x.k + '"><span class="rang">' + x.n + '</span><span><b>'
      + T('ex_' + x.k) + '</b><span style="display:block;margin-top:4px">' + T('ex_' + x.k + '_c') + '</span></span></button>').join('') + '</div>';
  document.getElementById('filtre').onchange = e => { filtre = e.target.value; };
  app.querySelectorAll('[data-x]').forEach(b => b.onclick = () => lancer(b.dataset.x));
  document.getElementById('retour').onclick = ecranAccueil;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}

let J = null;   // la série en cours
function lancer(k) {
  const dansFiltre = m => !filtre || m.p === filtre;
  let items;
  if (k === 'client') items = melange(D.demandes).slice(0, SERIE);
  else if (k === 'rayon') items = tirage(D.mots.filter(m => m.img && RAYONS.includes(m.p) && dansFiltre(m)));
  else items = tirage(D.mots.filter(m => visuel(m) && m.son && dansFiltre(m)));
  J = {k, items, i: 0, essais: 0, premier: 0, fini: false};
  question();
}

function cadreJeu(corps) {
  app.innerHTML = tete(T('ex_' + J.k), T('ex_' + J.k + '_c'), true, 'exercices')
    + '<div class="jeu"><div class="barre"><i style="width:' + Math.round(100 * J.i / J.items.length) + '%"></i></div>' + corps
    + '<p class="retro" id="retro" aria-live="polite"></p><div class="suite" id="suite"></div></div>';
  document.getElementById('retour').onclick = () => { if (audio) audio.pause(); ecranExercices(); };
  document.getElementById('chLangue').onclick = ecranLangue;
}
const boutonsEcoute = () => '<div class="ecoute"><button type="button" class="mf-btn mf-btn--pri" id="reec">' + ICO.son + '<span>' + T('reecouter') + '</span></button>'
  + '<button type="button" class="mf-btn" id="lent"><span>' + T('lentement') + '</span></button></div>';
function brancherEcoute(src) {
  document.getElementById('reec').onclick = () => joue(src);
  document.getElementById('lent').onclick = () => { joue(src); if (audio) { audio.preservesPitch = true; audio.playbackRate = 0.75; } };
}

function question() {
  if (J.i >= J.items.length) return bilan();
  J.essais = 0;
  const it = J.items[J.i];
  if (J.k === 'ecoute') {
    const autres = melange(D.mots.filter(m => m.p === it.p && m.id !== it.id && visuel(m))).slice(0, 5);
    J.bonne = it.id; J.options = melange([it].concat(autres));
    cadreJeu(boutonsEcoute() + '<div class="choix">' + J.options.map(m => '<button type="button" class="opt" data-o="' + m.id + '">' + image(m) + '</button>').join('') + '</div>');
    brancherEcoute(it.son); joue(it.son);
  } else if (J.k === 'image') {
    const autres = melange(D.mots.filter(m => m.p === it.p && m.id !== it.id)).slice(0, 2);
    J.bonne = it.id; J.options = melange([it].concat(autres));
    cadreJeu('<div class="sujet">' + image(it, true) + '</div><div class="choix mots">'
      + J.options.map(m => '<button type="button" class="opt" data-o="' + m.id + '">' + esc(m.mot) + '</button>').join('') + '</div>');
  } else if (J.k === 'rayon') {
    const autres = melange(RAYONS.filter(r => r !== it.p)).slice(0, 3);
    J.bonne = it.p; J.options = melange([it.p].concat(autres));
    const l = L();
    cadreJeu('<div class="sujet">' + image(it, true) + '</div><p style="text-align:center;font-weight:800;font-size:20px;margin:0 0 10px">' + esc(it.mot) + '</p><div class="choix mots">'
      + J.options.map(k => { const tr = l && l.ui['planche_' + k];
          return '<button type="button" class="opt" data-o="' + k + '"><span>' + esc(D.planches.find(p => p.k === k).t)
            + (tr ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(tr) + '</span>' : '') + '</span></button>'; }).join('') + '</div>');
    joue(it.son);
  } else if (J.k === 'rappel') {
    cadreJeu('<div class="sujet">' + image(it, true) + '</div><div class="revele" id="revele"><button type="button" class="mf-btn mf-btn--pri" id="voirMot">' + ICO.oeil + '<span>' + T('voir_mot') + '</span></button></div>');
    document.getElementById('voirMot').onclick = () => {
      joue(it.son);
      document.getElementById('revele').innerHTML = '<p class="gros">' + esc(it.mot) + '</p>'
        + '<div class="ecoute"><button type="button" class="mf-btn mf-btn--pri" id="savais"><span>' + T('savais') + '</span></button>'
        + '<button type="button" class="mf-btn" id="arevoir"><span>' + T('a_revoir') + '</span></button></div>';
      document.getElementById('savais').onclick = () => { J.premier++; revoir.delete(it.id); garderRevoir(); J.i++; question(); };
      document.getElementById('arevoir').onclick = () => { revoir.add(it.id); garderRevoir(); J.i++; question(); };
    };
    return;
  } else if (J.k === 'client') {
    J.bonne = 0; J.options = melange(it.v.map((v, n) => Object.assign({n}, v)));
    cadreJeu(boutonsEcoute() + '<div class="choix">' + J.options.map(v =>
      '<button type="button" class="opt gris" data-o="' + v.n + '"><img src="' + v.img + '" alt="' + esc(v.mot) + '" loading="lazy">'
      + '<span class="attrs"><span class="chip" style="background:' + v.hex + '" role="img" aria-label="' + esc(v.cmot) + '"></span>'
      + (v.t ? '<span class="tag">' + v.t + '</span>' : '') + '</span></button>').join('') + '</div>');
    brancherEcoute(it.son); joue(it.son);
  }
  app.querySelectorAll('[data-o]').forEach(b => b.onclick = () => repondre(b));
}

function repondre(b) {
  const it = J.items[J.i], retro = document.getElementById('retro');
  const juste = String(b.dataset.o) === String(J.bonne);
  const idMot = J.k === 'client' ? null : it.id;
  if (juste) {
    b.classList.add('juste');
    if (J.essais === 0) { J.premier++; if (idMot) { revoir.delete(idMot); garderRevoir(); } }
    retro.className = 'retro ok'; retro.innerHTML = T('bravo');
    if (J.k !== 'ecoute' && J.k !== 'client') joue(it.son);
    finQuestion();
  } else {
    J.essais++; b.classList.add('faux'); b.disabled = true;
    if (idMot) { revoir.add(idMot); garderRevoir(); }
    if (J.essais >= 2) {
      const bon = app.querySelector('[data-o="' + J.bonne + '"]'); if (bon) bon.classList.add('juste');
      retro.className = 'retro non'; retro.innerHTML = T('reponse');
      if (J.k === 'client') retro.innerHTML += '<span class="appui" style="font-style:italic" lang="fr">« ' + esc(it.phrase) + ' »</span>';
      else joue(it.son);
      finQuestion();
    } else { retro.className = 'retro non'; retro.innerHTML = T('essaie'); }
  }
}
function finQuestion() {
  app.querySelectorAll('[data-o]').forEach(x => x.disabled = true);
  const s = document.getElementById('suite');
  s.innerHTML = '<button type="button" class="mf-btn mf-btn--pri" id="apres"><span>' + T('suivant') + '</span>' + ICO.suiv + '</button>';
  const a = document.getElementById('apres'); a.onclick = () => { J.i++; question(); }; a.focus();
}
function bilan() {
  J.fini = true;
  app.innerHTML = tete(T('ex_' + J.k), '', true, 'exercices')
    + '<div class="bilan"><p style="font-weight:800;margin:0">' + T('fin') + '</p><p class="score">' + J.premier + ' / ' + J.items.length + '</p>'
    + '<p style="margin:0 0 16px">' + T('premier_coup') + '</p>'
    + '<button type="button" class="mf-btn mf-btn--pri" id="encore"><span>' + T('recommencer') + '</span></button></div>';
  document.getElementById('encore').onclick = () => lancer(J.k);
  document.getElementById('retour').onclick = ecranExercices;
  document.getElementById('chLangue').onclick = ecranLangue;
}
window.__francoeur = { etat: () => J, D };

if (langue) ecranAccueil(); else ecranLangue();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
