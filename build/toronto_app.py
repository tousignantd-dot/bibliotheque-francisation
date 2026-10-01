#!/usr/bin/env python3
"""L'application « Une semaine à Toronto » — l'anglais du touriste francophone, sur téléphone.

    python3 build/toronto_app.py     # → modules-autonomes/toronto/index.html

Produite, jamais écrite à la main. Elle lit build/contenu/toronto/ (`preparation.py`,
`lexique.py`, `personnages.py`) et la liste des sons de build/toronto_commun.py,
la même que celle du générateur de voix (build/toronto_audio.py).

ÉTAPE 1 (1er oct. 2026) : l'accueil, « Avant de partir » (huit séances de
quinze minutes, trois temps chacune) et le test « Prêt à partir ? ». Le moteur
est celui de Compostelle (build/compostelle_app.py) — son, micro, avis de la
Loi 25, comparaison des réponses, place tournante de la bonne réponse — réécrit
pour l'anglais. Les étapes suivantes (les mots, la semaine jouée, la poche)
viendront s'y ajouter.

FAUX DÉBUTANT (décision du plan) : rien n'est verrouillé ; le test se passe
d'abord si l'on veut, et « Solide » partout dit qu'on peut sauter les séances.

RIEN NE PART : l'état vit dans le localStorage du téléphone. La reconnaissance
vocale est celle du navigateur, annoncée avant le premier usage.
"""
import json, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import toronto_commun as C  # noqa: E402

SORTIE = RACINE / "modules-autonomes" / "toronto" / "index.html"
MEDIA = RACINE / "assets" / "interactive" / "toronto"
MEDIA_V = "3"  # 3 : test 0-5 refait (fin coupée) ; 2 : cinq extraits refaits après le tour 3 (même nom, autre son) ; 1 : première production


def donnees():
    PR, LX, PS = C.charger("preparation"), C.charger("lexique"), C.charger("personnages")
    LX.verifier()
    PR.verifier({e[0] for e in LX.LEXIQUE}, PS.VOIX)
    tous = C.extraits()
    noms = [x["fichier"] for x in tous]
    assert len(noms) == len(set(noms)), "deux extraits au même nom"
    sons = sorted(f for f in noms if (C.SONS / f).exists())
    mots = {}
    for i, pl, en, fr, dessin, note in LX.LEXIQUE:
        img = "croquis" if dessin == "croquis" and (MEDIA / "croquis" / f"{i}.jpg").exists() else ""
        mots[i] = {"p": pl, "en": en, "fr": fr, "img": img, "note": note}
    perso = {k: {"nom": v[0], "qui": v[4]} for k, v in PS.VOIX.items()}
    for i, pl, en, fr, dessin, note in LX.LEXIQUE:
        if dessin.startswith("picto:"):
            mots[i]["img"] = dessin
    # La série des pièges : (id, phrase, bonne, fausse lecture, second choix, explication).
    pieges = [{"id": i, "en": t[0], "bonne": t[1], "fausse": t[2], "seconde": t[3], "expl": t[4]} for i, t in LX.PIEGES.items()]
    return {"v": MEDIA_V, "mots": mots, "perso": perso, "sons": sons, "planches": LX.PLANCHES, "pieges": pieges,
            "prep": {"seances": PR.SEANCES, "test": PR.TEST, "objectifs": PR.OBJECTIFS, "seuil": PR.SEUIL,
                     "conseils": PR.CONSEILS, "fin": PR.FIN, "lieu": PR.LIEU, "solide": PR.SEUIL_SOLIDE},
            # Les réponses témoins des clés, rejouées dans le moteur de la page (audit tour 5) : `window.__toronto`.
            "controle": {"refus": PR.REFUS, "accepte": PR.ACCEPTE}}, len(sons), len(noms)


def main():
    D, n, total = donnees()
    page = GABARIT.replace("%%DONNEES%%", json.dumps(D, ensure_ascii=False, separators=(",", ":")))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)}  {len(page)//1024} Ko — sons {n}/{total}")


GABARIT = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Une semaine à Toronto</title>
<meta name="description" content="L'anglais du touriste francophone, pour une semaine à Toronto.">
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<meta name="theme-color" content="#FFFFFF">
<meta name="robots" content="noindex">
<style>
/* Page produite par build/toronto_app.py — ne pas l'éditer. */
/* La carte postale : un brun d'encre (#7A3B1D), réservé à la progression ; l'action
   reste le vert de francis. Le rouge du tramway marque la ville sur l'en-tête. */
:root{--carte:#7A3B1D;--carte-bg:#FBF3EC;--ville:#C8102E}
*{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--surface-page,#F7F7F5);color:var(--text-body,#2B2D31);
  font-family:Nunito,system-ui,sans-serif;font-size:17px;line-height:1.5}
.fr-barre .fr-barre__in{max-width:760px;padding-left:16px;padding-right:16px}
.secteur{display:flex;flex-direction:column;align-items:flex-end;text-align:right;line-height:1.15}
.secteur small{font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted)}
.secteur b{font-size:17px;font-weight:900;color:var(--ville)}
@media (max-width:480px){.secteur small{display:none}.secteur b{font-size:15px}}
main{max-width:760px;margin:0 auto;padding:14px 16px 90px}
h1{font-size:28px;line-height:1.15;margin:6px 0 6px;color:var(--text-strong)}
h2{font-size:21px;line-height:1.2;margin:22px 0 10px;color:var(--text-strong)}
p{margin:0 0 10px}
.muted{color:var(--text-muted)}
.surtitre{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);margin:0}
button{font:inherit}
.btn{font-weight:800;font-size:16px;cursor:pointer;border-radius:12px;padding:10px 16px;min-height:48px;
  border:1px solid var(--line-300,#D6D6D2);background:var(--surface-card,#fff);color:var(--text-strong);
  display:inline-flex;gap:8px;align-items:center;justify-content:center;text-decoration:none}
.btn--pri{background:var(--accent);border-color:var(--accent);color:#fff}
.btn--large{width:100%;white-space:normal;line-height:1.25}
.btn--son{background:var(--audio);border-color:var(--audio);color:#fff;min-width:48px;padding:10px 12px}
.btn--petit{min-height:44px;padding:6px 12px;font-size:14.5px}
.btn svg{width:20px;height:20px;flex:none}
.btn[disabled]{opacity:.45;cursor:not-allowed}
.rangee{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.carte{background:var(--surface-card,#fff);border:1px solid var(--line-200,#E8E8E4);border-radius:16px;padding:16px}
.retour{display:inline-flex;align-items:center;gap:6px;font-weight:800;font-size:15px;color:var(--text-muted);
  background:none;border:0;padding:8px 0;cursor:pointer;min-height:44px}
.retour svg{width:18px;height:18px}
#app a{color:var(--text-accent)}
.acc{background:#fff;border:1px solid var(--line-200);border-radius:18px;padding:16px;margin:14px 0}
.acc--carte{background:var(--carte-bg);border-color:#E7D3C3}
.acc h2{margin:2px 0 6px}
.valise{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;margin:10px 0}
.valise span{aspect-ratio:3/2;border:1.5px dashed #D7BFAE;border-radius:6px;display:grid;place-items:center;font-weight:900;color:#B79A86;background:#fff}
.valise span.fait{border:1.5px solid var(--carte);background:var(--carte);color:#fff}
.ariane{list-style:none;padding:0;margin:12px 0 14px;display:flex}
.ariane li{flex:1;position:relative;text-align:center;min-width:0}
.ariane li+li::before{content:"";position:absolute;top:17px;right:calc(50% + 19px);left:calc(-50% + 19px);height:3px;border-radius:2px;background:var(--line-200)}
.ariane li.relie::before{background:var(--ok-line,#2E7D4F)}
.ariane button{background:none;border:0;padding:0;font:inherit;color:inherit;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:5px;width:100%}
.ariane button:disabled{cursor:not-allowed}
.ariane .rond{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;font-weight:900;font-size:16px;background:#fff;border:2px solid var(--carte);color:var(--carte);position:relative;z-index:1}
.ariane .lib{font-size:13px;font-weight:800;line-height:1.2}
.ariane li.fait .rond{background:var(--ok-line,#2E7D4F);border-color:var(--ok-line,#2E7D4F);color:#fff}
.ariane li.ici .rond{background:var(--carte);color:#fff;box-shadow:0 0 0 4px rgba(122,59,29,.2)}
.ariane li.ferme .rond{border-color:var(--line-300);color:var(--text-muted);background:#F3F0E8}
.ariane li.ferme .lib{color:var(--text-muted);font-weight:700}
.fil-legende{font-size:14.5px;color:var(--text-muted);margin:-4px 0 12px;text-align:center}
.meca{background:#fff;border:1px solid var(--line-200);border-left:4px solid var(--carte);border-radius:12px;padding:10px 14px;margin:10px 0 14px}
.meca ul{margin:6px 0 0;padding-left:18px}.meca li{margin:5px 0;font-size:15.5px;line-height:1.5}
.objectif{background:var(--carte-bg);border:1px solid #E7D3C3;border-radius:12px;padding:10px 12px;margin:10px 0;font-size:15.5px;color:#4A2412}
.etapes-j{list-style:none;padding:0;margin:14px 0 0;display:flex;flex-direction:column;gap:8px}
.etapes-j button{width:100%;display:flex;align-items:center;gap:12px;text-align:left;background:#fff;border:1px solid var(--line-200);
  border-radius:14px;padding:12px 14px;cursor:pointer;min-height:60px}
.etapes-j .num{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;
  background:var(--surface-sunken,#FBFBFA);border:1px solid var(--line-200);flex:none;font-size:14px}
.etapes-j .fait .num{background:var(--ok-bg);border-color:var(--ok-line);color:var(--ok-ink)}
.etapes-j b{display:block;color:var(--text-strong)}
.etapes-j span.d{font-size:13.5px;color:var(--text-muted);display:block;line-height:1.3}
.etat{margin-left:auto;font-size:12.5px;font-weight:800;color:var(--ok-ink);white-space:nowrap}
.ph{display:flex;gap:10px;align-items:center;padding:10px 14px;border-top:1px solid var(--line-200)}
.ph:first-child{border-top:0}
.ph .t{flex:1;min-width:0}
.ph .t b{display:block;color:var(--text-strong);font-size:16.5px;line-height:1.25}
.ph .t span{font-size:14px;color:var(--text-muted)}
.liste-ecoute{padding:4px 0}
.grille{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
@media (min-width:600px){.grille{grid-template-columns:repeat(3,minmax(0,1fr))}}
.mot{background:#fff;border:1px solid var(--line-200);border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:4px;cursor:pointer;text-align:left;min-width:0;font:inherit}
.mot img{width:100%;aspect-ratio:1;object-fit:contain}
.mot .en{font-weight:900;font-size:16.5px;color:var(--text-strong);line-height:1.2;overflow-wrap:anywhere}
.mot .fr{font-size:14px;color:var(--text-muted);line-height:1.25}
.mot .piege{font-size:11.5px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;color:var(--warn-ink);background:var(--warn-bg);
  border:1px solid var(--warn-line);border-radius:99px;padding:1px 8px;align-self:flex-start}
.consigne{font-size:15.5px;color:var(--text-muted);margin:0 0 10px}
.progres{height:8px;background:#EEE9DA;border-radius:99px;overflow:hidden;margin:6px 0 14px}
.progres i{display:block;height:100%;background:var(--carte);border-radius:99px;transition:width .3s}
.choix{display:flex;flex-direction:column;gap:8px;margin:10px 0}
.choix button{text-align:left;background:#fff;border:1.5px solid var(--line-300,#D6D6D2);border-radius:12px;padding:12px 14px;
  cursor:pointer;min-height:52px;font-size:16.5px;color:var(--text-strong);line-height:1.3}
.choix button.juste::before{content:"✓ ";font-weight:900}
.choix button.juste{border-color:var(--ok-line);background:var(--ok-bg);color:var(--ok-ink)}
.choix button.faux::before{content:"✕ ";font-weight:900}
.choix button.faux{border-color:var(--no-line);background:var(--no-bg);color:var(--no-ink);cursor:default}
.retro{border-radius:10px;padding:10px 12px;margin:8px 0;font-size:15.5px}
.retro.ok{background:var(--ok-bg);border:1px solid var(--ok-line);color:var(--ok-ink)}
.retro.no{background:var(--no-bg);border:1px solid var(--no-line);color:var(--no-ink)}
.retro.info{background:var(--carte-bg);border:1px solid #E7D3C3;color:#4A2412}
.gros-son{display:flex;justify-content:center;margin:10px 0 4px}
.gros-son .btn--son{width:84px;height:84px;border-radius:50%}
.gros-son .btn--son svg{width:36px;height:36px}
.phrase-en{font-size:21px;font-weight:900;color:var(--text-strong);line-height:1.3;margin:6px 0}
.micro{display:flex;flex-direction:column;align-items:center;gap:8px;margin:12px 0}
.micro .btn-micro{width:84px;height:84px;border-radius:50%;background:var(--surface-inverse,#17181A);color:#fff;border:0;cursor:pointer;display:flex;align-items:center;justify-content:center}
.micro .btn-micro svg{width:34px;height:34px}
.micro .btn-micro.ecoute{background:var(--audio);animation:pouls 1.2s infinite}
@keyframes pouls{0%{box-shadow:0 0 0 0 rgba(220,38,38,.45)}70%{box-shadow:0 0 0 16px rgba(220,38,38,0)}100%{box-shadow:0 0 0 0 rgba(220,38,38,0)}}
.entendu{font-size:15.5px;min-height:24px;text-align:center;color:var(--text-body)}
.scene-tete{display:flex;gap:12px;align-items:center;margin:4px 0 10px}
.rappel{font-size:12.5px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;color:#7A5A45;background:var(--carte-bg);border:1px solid #E7D3C3;border-radius:99px;padding:2px 10px;display:inline-block;margin-bottom:6px}
.regle{border:1px dashed var(--warn-line);background:var(--warn-bg);color:var(--warn-ink);border-radius:12px;padding:10px 12px;font-size:15px;margin:8px 0}
.aide-bascule{display:flex;align-items:center;gap:8px;min-height:44px;font-size:15px;font-weight:800;color:var(--text-body);margin:6px 0;cursor:pointer}
.aide-bascule input{width:22px;height:22px}
.avis-fond{position:fixed;inset:0;background:rgba(19,35,59,.55);display:grid;place-items:center;padding:16px;z-index:50}
.avis-micro{background:#fff;border-radius:16px;padding:18px;max-width:440px;width:100%;box-shadow:0 16px 40px rgba(0,0,0,.3)}
.avis-micro h3{margin:0 0 8px}.avis-micro p{margin:0 0 10px;font-size:15.5px}
.sans-son{background:var(--warn-bg);border:1px solid var(--warn-line);color:var(--warn-ink);border-radius:12px;padding:10px 12px;font-size:14.5px;margin:0 0 12px}
.pied{max-width:720px;margin:24px auto 0;padding:14px 16px 28px;text-align:center;font-size:13.5px;color:var(--text-muted)}
.pied a{color:var(--text-muted)}
.avis-local{font-size:13px;color:var(--text-muted)}
/* Étape 2 : les planches */
.pl-liste{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.pl-liste button{display:flex;flex-direction:column;gap:2px;text-align:left;background:#fff;border:1px solid var(--line-200);border-left:4px solid var(--carte);
  border-radius:14px;padding:12px;cursor:pointer;min-height:72px;font:inherit;color:var(--text-body)}
.pl-liste b{font-size:16px;color:var(--text-strong)}.pl-liste span{font-size:13px;color:var(--text-muted)}
.mot .vis{aspect-ratio:1;border-radius:10px;background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden}
.mot .vis img{width:100%;height:100%;object-fit:contain}
.mot .vis svg{width:62%;height:62%}
.mot .vis.vide{background:var(--carte-bg);color:#D7BFAE}.mot .vis.vide svg{width:36%;height:36%}
.mot .note{font-size:12.5px;line-height:1.35;color:var(--text-muted)}
.mot.piege-m{border-color:var(--warn-line)}
.bascule-sens{margin:0 0 12px}
</style>
</head>
<body>
<div class="fr-barre"><div class="fr-barre__in">
  <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">Aide à l'apprentissage de l'anglais</span></span>
  <span class="secteur"><small>Voyage · anglais</small><b>Une semaine à Toronto</b></span>
</div></div>
<main id="app"></main>
<footer class="pied"><a href="#reglages">Réglages</a> · <a href="/confidentialite.html">Confidentialité</a></footer>
<audio id="lecteur" preload="none"></audio>
<script>
const D = %%DONNEES%%;
const SONS = new Set(D.sons);
const BASE = '/assets/interactive/toronto/';
const E = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const $ = s => document.querySelector(s);
const ICO = {
  son:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H3v6h3l5 4V5z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M18.5 5.5a9 9 0 0 1 0 13"/></svg>',
  retour:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>',
  micro:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0"/><path d="M12 18v3"/></svg>',
  stop:'<svg viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="6" width="12" height="12" rx="2"/></svg>',
  test:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>'
};
const LIEUX = {union: 'à Union Station, le premier jour', cafe: 'au café, le premier matin', hotel: 'à la réception de l’hôtel', kensington: 'dans Kensington, quand vous chercherez votre chemin'};

/* ---------- l'état, dans ce téléphone seulement ---------- */
const CLE = 'toronto:v1';
let S = {lent:false, aide:false, prep:{}};
try { Object.assign(S, JSON.parse(localStorage.getItem(CLE) || '{}')); } catch(e) {}
function sauver(){ try { localStorage.setItem(CLE, JSON.stringify(S)); } catch(e) {} }
const aujourdhui = () => new Date().toLocaleDateString('fr-CA', {day:'numeric', month:'short', year:'numeric'});

/* ---------- le son ---------- */
const lecteur = $('#lecteur');
function jouer(fichier, naturel){
  return new Promise(res => {
    if (!fichier || !SONS.has(fichier)) { res(false); return; }
    arreterMicro(); lecteur.pause();
    lecteur.src = BASE + 'sons/' + fichier + '?v=' + D.v;
    // Le ralenti étire dans le navigateur, sans changer la hauteur : les fichiers
    // restent au débit naturel (mémoire bouton-vitesse-voix).
    lecteur.playbackRate = (S.lent && !naturel) ? 0.8 : 1; lecteur.preservesPitch = true;
    lecteur.onended = () => res(true); lecteur.onerror = () => res(false);
    const p = lecteur.play(); if (p && p.catch) p.catch(() => res(false));
  });
}
const SANS_SON = !D.sons.length;

/* ---------- le micro (reconnaissance du navigateur, en en-CA) ---------- */
const Reco = window.SpeechRecognition || window.webkitSpeechRecognition;
let recoActive = null, micRefuse = false, micErreur = '';
function arreterMicro(){ if (recoActive) { const r = recoActive; try { r.stop(); } catch(e) {} if (r.terminer) setTimeout(r.terminer, 1500); } }
const rienEntendu = sinon => {
  const repli = 'Dites la phrase à voix haute, puis touchez « C’est dit ! ».';
  if (micRefuse) return 'Micro fermé, comme vous l’avez choisi. ' + repli;
  if (micErreur === 'not-allowed' || micErreur === 'service-not-allowed')
    return 'Le navigateur bloque le micro. Touchez l’icône à gauche de l’adresse du site, choisissez « Autoriser » pour le micro, puis réessayez. Sinon : ' + repli.charAt(0).toLowerCase() + repli.slice(1);
  if (micErreur === 'audio-capture') return 'Aucun micro trouvé sur cet appareil. ' + repli;
  if (micErreur === 'network') return 'La reconnaissance de la voix demande une connexion Internet. ' + repli;
  return sinon;
};
function fournisseurVoix(){
  const u = navigator.userAgent;
  if (/Edg\//.test(u)) return 'Microsoft (Edge)';
  if (/Chrome|CriOS|Android/.test(u)) return 'Google (Chrome)';
  if (/Safari|iPhone|iPad|Macintosh/.test(u)) return 'Apple (Safari)';
  return 'l’éditeur de votre navigateur';
}
/* Loi 25 : avant le premier usage, dire où va la voix — chez le fournisseur du
   navigateur, pas chez nous. Accepté une fois, gardé dans le téléphone. */
function ecouterMicro(surTexte, surFin){
  if (S.avisMicro) return ouvrirMicro(surTexte, surFin);
  const fond = document.createElement('div'); fond.className = 'avis-fond';
  fond.innerHTML = `<div class="avis-micro" role="dialog" aria-modal="true" aria-labelledby="avisT">
    <h3 id="avisT">Avant d'ouvrir le micro</h3>
    <p>Pour comprendre ce que vous dites, l'application utilise la reconnaissance vocale de <b>votre navigateur</b>.
    Votre voix est donc envoyée à <b>${fournisseurVoix()}</b>, aux États-Unis, qui la transcrit et renvoie le texte.</p>
    <p>Nous ne recevons pas votre voix et ne l'enregistrons pas. Le texte reste dans votre téléphone.</p>
    <p class="muted" style="font-size:14px">Vous préférez ne pas l'utiliser ? Tout se fait aussi sans micro : dites la phrase à voix haute, puis touchez « C’est dit ! » — elle n’est alors pas vérifiée.</p>
    <div class="rangee"><button class="btn btn--pri" id="avisOui">J'ai compris, ouvrir le micro</button><button class="btn" id="avisNon">Pas maintenant</button></div></div>`;
  document.body.appendChild(fond);
  fond.querySelector('#avisOui').onclick = () => { S.avisMicro = aujourdhui(); sauver(); fond.remove(); ouvrirMicro(surTexte, surFin); };
  fond.querySelector('#avisNon').onclick = () => { fond.remove(); micRefuse = true; surFin(''); micRefuse = false; };
  fond.querySelector('#avisOui').focus();
}
function ouvrirMicro(surTexte, surFin){
  // Reconnaissance continue qui accumule ; fin sur « Arrêter » ou 4 s de silence
  // (9 s avant le premier mot). Une seule fin, quoi qu'il arrive (leçon de Compostelle).
  const r = new Reco(); r.lang = 'en-CA'; r.continuous = true; r.interimResults = true;
  let final = '', minuterie = null, fini = false;
  const terminer = () => { if (fini) return; fini = true; clearTimeout(minuterie); if (recoActive === r) recoActive = null; surFin(final.trim()); };
  r.terminer = terminer;
  const relancer = d => { clearTimeout(minuterie); minuterie = setTimeout(() => { try { r.stop(); } catch(e) {} setTimeout(terminer, 1500); }, d); };
  r.onresult = ev => { let prov = '';
    for (let i = ev.resultIndex; i < ev.results.length; i++) {
      if (ev.results[i].isFinal) final += ev.results[i][0].transcript + ' '; else prov += ev.results[i][0].transcript; }
    surTexte((final + prov).trim()); relancer(4000); };
  micErreur = '';
  r.onerror = e => { if (e && e.error && e.error !== 'aborted' && e.error !== 'no-speech') micErreur = e.error; setTimeout(terminer, 300); };
  r.onend = terminer;
  recoActive = r; lecteur.pause();
  try { r.start(); relancer(9000); } catch(e) { terminer(); }
}
/* La reconnaissance anglaise écrit les nombres en chiffres (« 2 coffees », « $13.50 »,
   « 10:30 ») : on les remet en lettres avant de comparer, comme preparation.py le fait. */
const UN = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(' ');
const DIZ = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'};
function nombreEn(n){ n = +n; if (n < 20) return UN[n]; if (n < 100) return DIZ[Math.floor(n / 10)] + (n % 10 ? ' ' + UN[n % 10] : ''); return String(n); }
const enLettres = t => String(t)
  .replace(/(\d{1,2}):(\d{2})/g, (_, h, m) => nombreEn(h) + (+m ? ' ' + nombreEn(m) : ''))
  .replace(/\$\s*(\d+)\.(\d{2})/g, (_, a, b) => nombreEn(a) + ' ' + nombreEn(b))
  .replace(/\d+/g, n => ' ' + nombreEn(n) + ' ');
const plat = t => enLettres(String(t).replace(/['’]/g, ' ')).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim();
// Une clé qui commence par « ~ » est une expression régulière sur le texte aplati.
const trouve = (t, cle) => cle.startsWith('~') ? new RegExp(cle.slice(1)).test(plat(t)) : cle.split('|').some(a => new RegExp('(^| )' + plat(a).replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(s|es)?( |$)').test(plat(t)));
/* ---------- ordre des choix : jamais la bonne toujours au même rang ---------- */
// Audit tour 2 : une rotation garde l'ordre cyclique (la bonne précède toujours le leurre). Mélange à graine stable.
function ordre(n, g){ const o = [...Array(n).keys()]; g = g + 1; for (let i = n - 1; i > 0; i--) { g = (g * 16807) % 2147483647; const j = g % (i + 1); [o[i], o[j]] = [o[j], o[i]]; } return o; }

/* ---------- navigation ---------- */
const app = $('#app');
function aller(h){ location.hash = h; }
function retour(h, t){ return `<button class="retour" onclick="aller('${h}')">${ICO.retour} ${E(t)}</button>`; }
function rendre(){
  window.scrollTo(0, 0); arreterMicro(); lecteur.pause();
  const p = (location.hash.slice(1) || 'accueil').split('/');
  if (p[0] === 'prep') return p[1] === 'test' ? vuePrepTest() : p[1] ? vueSeance(p[1], p[2]) : vuePrep();
  if (p[0] === 'reglages') return vueReglages();
  if (p[0] === 'mots') return p[1] ? vuePlanche(p[1]) : vueMots();
  if (p[0] === 'pieges') return vuePieges();
  return vueAccueil();
}
window.addEventListener('hashchange', rendre);

/* ---------- l'accueil ---------- */
function vueAccueil(){
  const n = prepFaites(), tot = D.prep.seances.length, pro = prepProchaine(), t = S.prep.test || {};
  app.innerHTML = `<p class="surtitre">Voyage · anglais</p><h1>Une semaine à Toronto</h1>
    <p>Arriver, prendre le métro, s'installer à l'hôtel, commander, visiter, manger au restaurant, bavarder avec les gens de la ville :
    l'anglais qu'il vous faut pour une semaine à Toronto, à préparer chez vous, quinze minutes à la fois.</p>
    ${SANS_SON ? '<div class="sans-son">Version de travail : les voix ne sont pas encore enregistrées. Les écrans se parcourent, mais rien ne se fait entendre.</div>' : ''}
    <section class="acc acc--carte">
      <p class="surtitre">1 · Avant de partir</p><h2>Faire ma valise</h2>
      <p>Huit séances de quinze minutes : les sons de l'anglais, les politesses, les prix, l'heure, les demandes, les questions,
      se présenter, et surtout <b>comprendre la réponse</b>.</p>
      <div class="valise" aria-label="${n} séances faites sur ${tot}">${D.prep.seances.map((x, i) => `<span class="${prepEtat(x.id).fin ? 'fait' : ''}">${prepEtat(x.id).fin ? '✓' : i + 1}</span>`).join('')}</div>
      ${pro ? `<button class="btn btn--pri btn--large" onclick="aller('prep/${pro.id}')">${n ? 'Continuer' : 'Commencer'} : séance ${n + 1}, ${E(pro.titre.toLowerCase())}</button>`
            : `<div class="retro ok">✓ Les huit séances sont faites.</div>`}
      <button class="btn btn--large" style="margin-top:8px" onclick="aller('prep')">Les huit séances</button>
    </section>
    <section class="acc">
      <p class="surtitre">Vous avez déjà de l'anglais ?</p><h2>Prêt à partir ?</h2>
      <p>${D.prep.test[0].length} questions, un quart d'heure, avec le son et le micro. Le test vous situe ; « Solide » partout, et vous pouvez
      sauter les séances.${t.dernier ? ' Dernier passage : ' + E(t.dernier) + '.' : ''}</p>
      <button class="btn btn--large" onclick="aller('prep/test')">${ICO.test} Faire le test</button>
    </section>
    <section class="acc">
      <p class="surtitre">Les mots</p><h2>Douze planches</h2>
      <p>Près de deux cents mots du voyage, avec leur voix : se déplacer, l'hôtel, le café, le restaurant, payer, visiter… et les
      faux amis qui trompent un francophone.</p>
      <div class="rangee"><button class="btn btn--pri" style="flex:1" onclick="aller('mots')">Les planches</button>
      <button class="btn" style="flex:1" onclick="aller('pieges')">Les faux amis</button></div>
    </section>
    <section class="acc">
      <p class="surtitre">2 · La semaine</p><h2>Dix lieux, dix cartes postales</h2>
      <p class="muted">Union Station, l'hôtel, le café, la tour CN, le marché St. Lawrence, Kensington, le restaurant, la pharmacie,
      les îles, le départ. En préparation.</p>
    </section>`;
}

/* ---------- avant de partir : huit séances et « Prêt à partir ? » ---------- */
const PREP_TEMPS = [['ecoute', 'J’écoute', 'Les phrases et les mots, avec leur voix'],
                    ['quiz', 'Je reconnais', 'J’entends, je choisis'],
                    ['dire', 'Je le dis', 'Au micro, puis le modèle']];
function prepEtat(id){ if (!S.prep) S.prep = {}; return S.prep[id] || (S.prep[id] = {faits:{}, fin:null}); }
const seanceParId = id => D.prep.seances.find(x => x.id === id);
const prepFaites = () => D.prep.seances.filter(x => prepEtat(x.id).fin).length;
const prepProchaine = () => D.prep.seances.find(x => !prepEtat(x.id).fin) || null;
const numSeance = x => D.prep.seances.indexOf(x) + 1;
function vuePrep(){
  const n = prepFaites(), pro = prepProchaine();
  const liste = D.prep.seances.map((x, i) => { const e = prepEtat(x.id);
    return `<li class="${e.fin ? 'fait' : ''}"><button onclick="aller('prep/${x.id}')"><span class="num">${e.fin ? '✓' : i + 1}</span>
      <span><b>${E(x.titre)}</b><span class="d">${E(D.prep.objectifs[x.obj])} · ${x.minutes} min</span></span>${e.fin ? '<span class="etat">✓ faite</span>' : ''}</button></li>`; }).join('');
  app.innerHTML = `${retour('accueil', 'Accueil')}<p class="surtitre">1 · Avant de partir · ${n} sur ${D.prep.seances.length}</p>
  <h1>Faire ma valise</h1>
  <p>Huit séances de quinze minutes, dans l'ordre, dans les semaines qui précèdent le départ. Chacune a trois temps : on écoute, on
  reconnaît, puis on le dit au micro. Rien n'est fermé : si vous avez déjà de l'anglais, passez le test et sautez ce que vous savez.</p>
  ${pro ? `<button class="btn btn--pri btn--large" style="margin:6px 0 4px" onclick="aller('prep/${pro.id}')">${n ? 'Continuer' : 'Commencer'} : ${E(pro.titre)}</button>` : ''}
  <ul class="etapes-j">${liste}</ul>
  <button class="btn btn--large" style="margin-top:14px" onclick="aller('prep/test')">${ICO.test} Le test « Prêt à partir ? »</button>`;
}
const CADENAS = '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>';
function tempsOuvert(x, j){ const e = prepEtat(x.id); return !!e.fin || PREP_TEMPS.slice(0, j).every(([t]) => e.faits[t]); }
function filSeance(x, actif){
  const e = prepEtat(x.id);
  return `<ol class="ariane" aria-label="Les temps de la séance">${PREP_TEMPS.map(([t, nom], j) => {
    const fait = !!e.faits[t], ouvert = tempsOuvert(x, j), ici = t === actif, avant = j > 0 && e.faits[PREP_TEMPS[j - 1][0]];
    const cls = [fait ? 'fait' : '', ici ? 'ici' : '', ouvert ? '' : 'ferme', avant ? 'relie' : ''].filter(Boolean).join(' ');
    return `<li class="${cls}"><button ${ouvert && !ici ? `onclick="aller('prep/${x.id}/${t}')"` : ''} ${ouvert ? '' : 'disabled'}
      ${ouvert ? '' : `title="D'abord : ${E(PREP_TEMPS[j - 1][1])}"`} ${ici ? 'aria-current="step"' : ''}><span class="rond">${fait ? '✓' : ouvert ? j + 1 : CADENAS}</span><span class="lib">${nom}</span></button></li>`; }).join('')}</ol>`;
}
function teteSeance(x, k){
  const i = PREP_TEMPS.findIndex(t => t[0] === k);
  return `${retour('prep/' + x.id, 'Séance ' + numSeance(x) + ' · ' + x.titre)}${filSeance(x, k)}<h1>${PREP_TEMPS[i][1]}</h1>`;
}
function finTemps(x, k){
  const e = prepEtat(x.id); e.faits[k] = true;
  if (PREP_TEMPS.every(([t]) => e.faits[t]) && !e.fin) e.fin = aujourdhui();
  sauver();
  const suivant = PREP_TEMPS.find(([t]) => !e.faits[t]);
  if (suivant) return `<button class="btn btn--pri btn--large" onclick="aller('prep/${x.id}/${suivant[0]}')">Suivant : ${suivant[1]}</button>`;
  const pro = prepProchaine();
  return `<div class="retro ok">✓ Séance terminée : ${prepFaites()} sur ${D.prep.seances.length} dans la valise.</div>
    ${pro ? `<button class="btn btn--pri btn--large" onclick="aller('prep/${pro.id}')">Séance suivante : ${E(pro.titre)}</button>` :
      `<button class="btn btn--pri btn--large" onclick="aller('prep/test')">Les huit sont faites : le test « Prêt à partir ? »</button>`}
    <button class="btn btn--large" style="margin-top:8px" onclick="aller('prep')">Ma valise</button>`;
}
function vueSeance(id, k){
  const x = seanceParId(id); if (!x) return vuePrep();
  const jk = PREP_TEMPS.findIndex(([t]) => t === k);
  if (jk > 0 && !tempsOuvert(x, jk)) { const f = PREP_TEMPS.find(([t]) => !prepEtat(x.id).faits[t]); history.replaceState(null, '', '#prep/' + x.id + '/' + f[0]); k = f[0]; }
  if (k === 'ecoute') return seanceEcoute(x);
  if (k === 'quiz') return seanceQuiz(x);
  if (k === 'dire') return seanceDire(x);
  const e = prepEtat(x.id), suivant = PREP_TEMPS.find(([t]) => !e.faits[t]) || PREP_TEMPS[0];
  app.innerHTML = `${retour('prep', 'Ma valise')}<p class="surtitre">Séance ${numSeance(x)} sur ${D.prep.seances.length} · ${x.minutes} minutes</p>
    <h1>${E(x.titre)}</h1><p>${E(x.intro)}</p>
    ${filSeance(x, e.fin ? null : suivant[0])}
    <p class="fil-legende">${e.fin ? '✓ Séance faite. Refaites le temps de votre choix.' : 'Dans l’ordre : on écoute, on reconnaît, et on finit par parler.'}</p>
    <button class="btn btn--pri btn--large" onclick="aller('prep/${x.id}/${suivant[0]}')">${e.fin ? 'Refaire' : Object.keys(e.faits).length ? 'Continuer' : 'Commencer'} : ${suivant[1]}</button>
    <div class="objectif" style="margin-top:16px">${E(D.prep.fin[x.obj])}</div>
    <div class="meca"><p class="surtitre">L'aide-mémoire</p><ul>${x.meca.map(t => `<li>${t}</li>`).join('')}</ul></div>`;
}
function carteMot(id){
  const m = D.mots[id]; if (!m) return '';
  return `<button class="mot" onclick="jouer('mots/${id}.mp3')" aria-label="Écouter : ${E(m.en)}">
    ${m.img ? `<img src="${BASE}croquis/${id}.jpg?v=${D.v}" alt="" loading="lazy">` : ''}
    <span class="en" lang="en">${E(m.en)}</span><span class="fr">${E(m.fr)}</span>${m.note.startsWith('PIÈGE') ? '<span class="piege">Piège</span>' : ''}</button>`;
}
function seanceEcoute(x){
  // Le temps n'est fait qu'une fois chaque phrase écoutée (audit de Compostelle, G2).
  const entendues = new Set();
  const lignes = x.ecoute.map(([en, fr], k) => `<div class="ph"><button class="btn btn--son" aria-label="Écouter" data-k="${k}" data-f="prep/${x.id}/e${k}.mp3">${ICO.son}</button>
    <div class="t"><b lang="en">${E(en)}</b><span class="sens" ${S.aide ? '' : 'hidden'}>${E(fr)}</span></div></div>`).join('');
  app.innerHTML = `${teteSeance(x, 'ecoute')}
    <p class="consigne">Touchez le haut-parleur : vous entendez la phrase, et son sens apparaît. Répétez-la à voix haute, deux fois.</p>
    <div class="carte liste-ecoute">${lignes}</div>
    <h2>Les mots</h2><p class="consigne">Touchez un mot pour l'entendre.</p>
    <div class="grille">${x.mots.map(carteMot).join('')}</div>
    <div id="finEcoute" style="margin-top:16px"><button class="btn btn--pri btn--large" id="jaiEcoute" disabled>J'ai tout écouté (0 sur ${x.ecoute.length})</button></div>`;
  app.querySelectorAll('.liste-ecoute .btn--son').forEach(b => b.onclick = () => {
    jouer(b.dataset.f); b.closest('.ph').querySelector('.sens').hidden = false; entendues.add(b.dataset.k);
    const bt = $('#jaiEcoute'); if (!bt) return;
    bt.textContent = entendues.size >= x.ecoute.length ? 'J’ai tout écouté' : `J'ai tout écouté (${entendues.size} sur ${x.ecoute.length})`;
    bt.disabled = entendues.size < x.ecoute.length; });
  $('#jaiEcoute').onclick = () => { $('#finEcoute').innerHTML = finTemps(x, 'ecoute'); };
}
/* Une question à choix, jouée jusqu'à la bonne réponse : chaque mauvais choix
   dit pourquoi, et la place de la bonne tourne. */
function questionPrep(it, fichier, graine, surFin, rappel, une){
  const p = it.qui ? D.perso[it.qui] : null, estEn = it.type === 'dire' || (it.type === 'rep' && !!it.q) || (it.type === 'mot' && !it.q);
  const o = ordre(it.choix.length, graine);
  let fini = false, erreurs = 0;
  const titre = it.q || (it.type === 'rep' ? 'Que veut dire la phrase ?' : it.type === 'mot' ? 'Quel mot entendez-vous ?' : 'Que dites-vous ?');
  const haut = it.type === 'dire' ? `<div class="carte"><p style="font-size:18px;font-weight:800;margin:0">${E(it.fr)}</p></div>`
    : `${p ? `<div class="scene-tete"><div><b>${E(p.nom)}</b><div class="muted" style="font-size:14px">${E(p.qui)}</div></div></div>` : ''}
       <div class="gros-son"><button class="btn btn--son" aria-label="Écouter" id="rejouer">${ICO.son}</button></div>`;
  const html = `${rappel ? `<span class="rappel">${E(rappel)}</span>` : ''}${une ? '<span class="rappel">Une seule écoute, comme au comptoir : touchez le haut-parleur quand vous êtes prêt</span>' : ''}
    <h2 style="margin-top:6px">${titre}</h2>${haut}
    <div class="choix">${o.map(i => `<button data-i="${i}" ${estEn ? 'lang="en"' : ''}>${E(it.choix[i][0])}</button>`).join('')}</div><div id="r" aria-live="polite"></div>`;
  function brancher(){
    if ($('#rejouer')) {
      const jouerUne = () => { if (une) $('#rejouer').disabled = true; jouer(fichier, une).then(ok => { if (!ok && une) $('#rejouer').disabled = false; }); };
      $('#rejouer').onclick = jouerUne; if (!une) setTimeout(jouerUne, 250); }
    app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      if (fini || b.disabled) return; const i = +b.dataset.i;
      if (i === 0) { fini = true; b.classList.add('juste');
        $('#r').innerHTML = `<div class="retro ok">✓ ${it.type === 'rep' ? '« ' + E(it.en) + ' »' : it.type === 'dire' ? 'C’est bien ce qu’il faut dire.' : 'Bien entendu.'}</div>`;
        if (it.type === 'dire') jouer(fichier);
        surFin(erreurs);
      } else { erreurs++; b.classList.add('faux'); b.disabled = true;
        $('#r').innerHTML = `<div class="retro no">${E(it.choix[i][1])} Essayez encore.</div>`; }
    });
  }
  return [html, brancher];
}
function seanceQuiz(x){
  // Deux questions des séances précédentes ouvrent le quiz (rappel espacé, audit de Compostelle D1).
  const idx = D.prep.seances.indexOf(x);
  const vues = D.prep.seances.slice(0, idx).flatMap((y, j) => y.quiz.map((it, k) => ({it, sid:y.id, k, rappel:'Rappel · séance ' + (j + 1)})));
  const tires = []; while (vues.length && tires.length < 2) tires.push(vues.splice(Math.floor(Math.random() * vues.length), 1)[0]);
  // Aux séances 3, 4 et 8, les deux dernières questions ne s'écoutent qu'une fois, comme au comptoir.
  const unefois = ['p3', 'p4', 'p8'].includes(x.id);
  const items = [...tires, ...x.quiz.map((it, k) => ({it, sid:x.id, k, une: unefois && it.type !== 'dire' && k >= x.quiz.length - 2}))];
  let n = 0, erreurs = 0;
  function tour(){
    if (n >= items.length) {
      app.innerHTML = `${teteSeance(x, 'quiz')}<div class="retro ok">✓ ${items.length} questions${erreurs ? ', ' + erreurs + ' essai' + (erreurs > 1 ? 's' : '') + ' de trop — c’est ainsi qu’on apprend' : ', toutes du premier coup'}.</div>
        <div style="margin-top:12px">${finTemps(x, 'quiz')}</div>`; return; }
    const {it, sid, k, rappel, une} = items[n];
    const fichier = `prep/${sid}/q${k}` + (it.type === 'dire' ? '-c0' : '') + '.mp3';
    // Tour 4 : au hasard à chaque affichage — un rappel refait de mémoire de bouton ne prouve rien.
    const [html, brancher] = questionPrep(it, fichier, Math.floor(Math.random() * 9973), e => {
      erreurs += e; const b = document.createElement('button'); b.className = 'btn btn--pri btn--large'; b.textContent = 'Suivant';
      b.onclick = () => { n++; tour(); }; $('#r').appendChild(b); }, rappel, une);
    app.innerHTML = `${teteSeance(x, 'quiz')}<div class="progres"><i style="width:${100 * n / items.length}%"></i></div>${html}`;
    brancher();
  }
  tour();
}
// Les mots du modèle qui correspondent à une clé manquante, écrits comme dans le modèle.
function motDuModele(en, cle){
  const mots = en.replace(/[?!.,]/g, ' ').split(/\s+/).filter(Boolean);
  for (const n of [1, 2, 3, 4])
    for (let i = 0; i + n <= mots.length; i++) { const bout = mots.slice(i, i + n).join(' '); if (trouve(bout, cle)) return bout; }
  return cle.startsWith('~') ? en : cle.split('|')[0];
}
function seanceDire(x){
  let n = 0, comprises = 0, dites = 0;
  function tour(){
    if (n >= x.dire.length) {
      const assez = dites >= Math.ceil(x.dire.length / 2);
      app.innerHTML = `${teteSeance(x, 'dire')}<div class="retro ${assez ? 'ok' : 'info'}">${assez ? '✓' : '→'} ${dites} phrase${dites > 1 ? 's' : ''} dite${dites > 1 ? 's' : ''} sur ${x.dire.length}${Reco ? `, dont ${comprises} comprise${comprises > 1 ? 's' : ''} au micro du premier ou du deuxième coup` : ''}. ${assez ? 'Le plus dur est fait : oser.' : 'Dites-en au moins la moitié à voix haute pour terminer la séance.'}</div>
        <div style="margin-top:12px">${assez ? finTemps(x, 'dire') : `<button class="btn btn--pri btn--large" onclick="rendre()">Recommencer</button>`}</div>`; return; }
    const [fr, en, cles] = x.dire[n], fichier = `prep/${x.id}/d${n}.mp3`;
    let tente = false, essais = 0, modeleVu = false;
    app.innerHTML = `${teteSeance(x, 'dire')}<div class="progres"><i style="width:${100 * n / x.dire.length}%"></i></div>
      <div class="carte"><p class="surtitre">À vous</p><p style="font-size:19px;font-weight:800;color:var(--text-strong);margin:4px 0 0">${E(fr)}</p></div>
      ${Reco ? `<div class="micro"><button class="btn-micro" id="mic" aria-label="Parler">${ICO.micro}</button>
        <div class="muted" id="micEtat" style="font-size:14px">Touchez le micro, dites-le en anglais.</div><div class="entendu" id="entendu"></div></div>` : ''}
      <button class="btn btn--large" id="dit" style="margin:6px 0">C'est dit !</button><div id="r" aria-live="polite"></div>
      <div class="rangee" style="margin-top:10px"><button class="btn" id="modele" disabled>${ICO.son} Le modèle</button>
       <button class="btn btn--pri" id="suite" style="flex:1" disabled>Suivant</button></div>
      <p class="avis-local" style="margin-top:8px">Le modèle s'ouvre après votre essai : on cherche d'abord, on compare ensuite.</p>
      <button class="btn btn--petit" id="passer" style="margin-top:4px">Passer cette phrase</button>`;
    const zone = $('#r');
    const poserR = h => { zone.querySelectorAll(':scope > :not(.modele-carte)').forEach(y => y.remove()); zone.insertAdjacentHTML('afterbegin', h); };
    const montrer = () => { if (!document.body.contains(zone)) return;
      if (!modeleVu) { modeleVu = true; $('#modele').innerHTML = `${ICO.son} Réécouter`; $('#dit').disabled = true;
        zone.insertAdjacentHTML('beforeend', `<div class="retro info modele-carte"><span class="surtitre">Le modèle</span><div class="phrase-en" lang="en">${E(en)}</div></div>`); }
      $('#modele').disabled = false; jouer(fichier); };
    const essaye = () => { if (!tente) { tente = true; dites++; } $('#modele').disabled = false; $('#suite').disabled = false; };
    $('#modele').onclick = montrer;
    $('#suite').onclick = () => { n++; tour(); };
    $('#passer').onclick = () => { n++; tour(); };
    $('#dit').onclick = () => { essaye(); montrer(); };
    if (Reco) $('#mic').onclick = () => {
      const mic = $('#mic'); if (recoActive) { arreterMicro(); return; }
      mic.classList.add('ecoute'); mic.innerHTML = ICO.stop; $('#micEtat').textContent = 'Je vous écoute… touchez pour arrêter.';
      ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
        mic.classList.remove('ecoute'); mic.innerHTML = ICO.micro; $('#micEtat').textContent = 'Touchez le micro pour réessayer.';
        if (!final) { poserR(`<div class="retro info">${rienEntendu('Je n’ai rien entendu. Vérifiez que le micro est permis, ou dites-le et touchez « C’est dit ! ».')}</div>`); return; }
        essais++;
        const manque = cles.filter(c => !trouve(final, c));
        if (!manque.length) { if (essais <= 2 && !modeleVu) comprises++;
          poserR(`<div class="retro ok">✓ Well done! On vous a compris.</div>`); essaye(); setTimeout(montrer, 600); return; }
        const presque = manque.length <= cles.length / 2;
        poserR(`<div class="retro no">${presque ? `Presque. Il manque : <b lang="en">${manque.map(c => E(motDuModele(en, c))).join(', ')}</b>. ` : 'Je n’ai pas reconnu la phrase. '}${essais < 2 && !modeleVu ? 'Réessayez, sans regarder le modèle.' : 'Comparez avec le modèle.'}</div>`);
        essaye();
        if (essais >= 2) montrer(); else $('#modele').disabled = false;
      });
    };
  }
  tour();
}
function vuePrepTest(){
  const T = S.prep.test || (S.prep.test = {});
  const f = T.prochaine != null ? T.prochaine : Math.floor(Math.random() * 2);
  const items = D.prep.test[f]; let k = 0; const res = {}, nonVerif = {}, manquees = {};
  function intro(){
    app.innerHTML = `${retour('accueil', 'Accueil')}<p class="surtitre">Le test de la maison</p><h1>Prêt à partir ?</h1>
      <p>${items.length} questions, un quart d'heure, avec le son et le micro. Pour chacun des cinq objectifs, quelques questions — des phrases
      nouvelles : les mêmes outils que dans les séances, d'autres mots.</p>
      <div class="regle"><b>Comme à Toronto.</b> Les phrases qu'on vous dit ne s'écoutent <b>qu'une fois</b>, au débit normal. Au micro, <b>deux essais</b>.
      ${E(D.prep.seuil.replace(" Au micro, deux essais au plus ; les phrases entendues ne s'écoutent qu'une fois.", ''))} C'est un repère, pas une note : il ne vous empêche de rien.</div>
      ${Reco ? '' : '<div class="sans-son">Ce navigateur ne reconnaît pas la voix : ouvrez la page dans Chrome ou Safari pour mesurer l’oral. Sans cela, les questions au micro ne compteront pas.</div>'}
      <button class="btn btn--pri btn--large" id="go">Commencer</button>`;
    // Tour 3 : la forme suivante est fixée dès le départ — un test abandonné ne retombe pas sur la même.
    // Tour 5 : une forme vue, même abandonnée, est « revue » au passage suivant.
    $('#go').onclick = () => { T.prochaine = 1 - f; T.vues = T.vues || {}; T.revu = !!T.vues[f]; T.vues[f] = true; sauver(); tour(); };
  }
  function tour(){
    if (k >= items.length) return bilan();
    const it = items[k]; let compte = false;
    const noter = ok => { if (compte) return; compte = true; const r = res[it.obj] || (res[it.obj] = [0, 0]); r[1]++; if (ok) r[0]++;
      else (manquees[it.obj] || (manquees[it.obj] = [])).push(it.en || it.modele || it.choix[0][0]); };
    const suite = () => { const b = document.createElement('button'); b.className = 'btn btn--pri btn--large'; b.textContent = 'Suivant'; b.onclick = () => { k++; tour(); }; $('#r').appendChild(b); };
    const tete2 = `${retour('accueil', 'Accueil')}<p class="surtitre">Question ${k + 1} sur ${items.length}</p><div class="progres"><i style="width:${100 * k / items.length}%"></i></div>`;
    if (it.type === 'oral') {
      // Audit tour 1 (M3) : la présentation se compte par parties (2 sur 3 = en route), pas tout ou rien.
      let prises = 0, bons = 0;
      app.innerHTML = `${tete2}<h1>Dites-le</h1><div class="carte"><p style="font-size:18px;font-weight:800;margin:0">${E(it.fr)}</p></div>
        ${Reco ? `<div class="micro"><button class="btn-micro" id="mic" aria-label="Parler">${ICO.micro}</button><div class="muted" id="micEtat" style="font-size:14px">Deux essais.</div><div class="entendu" id="entendu"></div></div>` : ''}
        <div id="r" aria-live="polite"></div><button class="btn btn--large" id="sansmic" style="margin-top:8px">${Reco ? 'Sans micro : c’est dit !' : 'C’est dit !'}</button>`;
      const fin = (ok, verifie) => {
        if (verifie && it.parties) { compte = true; const r = res[it.obj] || (res[it.obj] = [0, 0]); r[0] += ok ? it.cles.length : bons; r[1] += it.cles.length;
          if (!ok) (manquees[it.obj] || (manquees[it.obj] = [])).push(it.modele); }
        else if (verifie) noter(ok); else { compte = true; nonVerif[it.obj] = (nonVerif[it.obj] || 0) + 1; }
        if ($('#sansmic')) $('#sansmic').remove(); if ($('#mic')) $('#mic').disabled = true;
        $('#r').insertAdjacentHTML('beforeend', `<div class="retro ${!verifie ? 'info' : ok ? 'ok' : 'no'}">${!verifie ? 'Non vérifié : sans le micro, cet objectif ne pourra pas être « Solide ».' : ok ? '✓ On vous a compris.' : 'Deux essais sans qu’on vous comprenne tout à fait.'}</div>
          <div class="retro info"><span class="surtitre">Le modèle</span><div class="phrase-en" lang="en">${E(it.modele)}</div></div>`);
        jouer(`prep/test/${f}-${k}-m.mp3`); suite(); };
      $('#sansmic').onclick = () => fin(false, false);
      if (Reco) $('#mic').onclick = () => { const mic = $('#mic'); if (recoActive) { arreterMicro(); return; }
        mic.classList.add('ecoute'); mic.innerHTML = ICO.stop;
        ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
          mic.classList.remove('ecoute'); mic.innerHTML = ICO.micro;
          if (!final) { $('#r').innerHTML = `<div class="retro info">${rienEntendu($('#sansmic') ? 'Je n’ai rien entendu. Vérifiez que le micro est permis et réessayez — ou touchez « Sans micro : c’est dit ! ».' : 'Je n’ai rien entendu. Vérifiez que le micro est permis et réessayez.')}</div>`; return; }
          const manque = it.cles.map((c, i) => [c, i]).filter(([c]) => !trouve(final, c));
          prises++; bons = Math.max(bons, it.cles.length - manque.length);
          // Une fois le micro entendu, « sans micro » n'est plus une issue (Compostelle, tour 2, F1).
          if ($('#sansmic')) $('#sansmic').remove();
          if (!manque.length) { $('#r').innerHTML = ''; return fin(true, true); }
          const quoi = it.parties ? 'Il manque : ' + manque.map(([, i]) => E(it.parties[i])).join(', ') + '.' : `J'ai entendu « ${E(final)} ».`;
          if (prises >= 2) { $('#r').innerHTML = `<div class="retro no">${quoi}</div>`; return fin(false, true); }
          $('#r').innerHTML = `<div class="retro no">${quoi} Réessayez (dernier essai).</div>`;
        }); };
      return;
    }
    // Au test, le premier choix compte. P2 et P5 : une seule écoute, au débit naturel.
    const fichier = `prep/test/${f}-${k}` + (it.type === 'dire' ? '-c0' : '') + '.mp3';
    const unefois = it.obj === 'P2' || it.obj === 'P5';
    // Tour 4 : un tirage indépendant à chaque affichage. Une graine fixe mettait la bonne au même bouton
    // (tour 3) ; une permutation posée dans les données se déduisait des places déjà montrées (tour 4).
    const o = ordre(it.choix.length, Math.floor(Math.random() * 9973)).filter(i => i !== 0);
    o.splice(Math.floor(Math.random() * it.choix.length), 0, 0);
    const estEn = it.type !== 'rep', p = it.qui ? D.perso[it.qui] : null;
    const titre = it.type === 'rep' ? 'Que veut dire la phrase ?' : it.type === 'mot' ? 'Quel mot entendez-vous ?' : 'Que dites-vous ?';
    app.innerHTML = `${tete2}<h1>${titre}</h1>
      ${it.type === 'dire' ? `<div class="carte"><p style="font-size:18px;font-weight:800;margin:0">${E(it.fr)}</p></div>` :
        `${p ? `<div class="scene-tete"><div><b>${E(p.nom)}</b><div class="muted" style="font-size:14px">${unefois ? 'Une seule écoute, comme au comptoir : touchez le haut-parleur quand vous êtes prêt.' : 'Vous pouvez réécouter.'}</div></div></div>` : ''}
         <div class="gros-son"><button class="btn btn--son" aria-label="Écouter" id="ecoute1">${ICO.son}</button></div>`}
      <div class="choix">${o.map(i => `<button data-i="${i}" ${estEn ? 'lang="en"' : ''}>${E(it.choix[i][0])}</button>`).join('')}</div><div id="r" aria-live="polite"></div>`;
    if (it.type !== 'dire') {
      let joue = false;
      // Une seule écoute : elle part au toucher, jamais toute seule (Compostelle, 27 sept. 2026).
      const une = () => { if (unefois && joue) return; if (unefois) { joue = true; $('#ecoute1').disabled = true; }
        jouer(fichier, unefois).then(ok => { if (!ok && unefois) { joue = false; $('#ecoute1').disabled = false; } }); };
      $('#ecoute1').onclick = une; if (!unefois) setTimeout(une, 250);
    }
    app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      if (compte) return; const i = +b.dataset.i; noter(i === 0);
      b.classList.add(i === 0 ? 'juste' : 'faux'); if (i !== 0) app.querySelector('.choix button[data-i="0"]').classList.add('juste');
      $('#r').innerHTML = `<div class="retro ${i === 0 ? 'ok' : 'no'}">${i === 0 ? '✓' + (it.en ? ' « ' + E(it.en) + ' »' : '') : E(it.choix[i][1]) + (it.en ? ' « ' + E(it.en) + ' »' : '')}</div>`;
      if ($('#ecoute1')) { $('#ecoute1').disabled = false; $('#ecoute1').onclick = () => jouer(fichier); }
      if (it.type === 'dire') jouer(fichier); suite();
    });
  }
  function bilan(){
    // Tour 4 : deux formes seulement ; dès le 3e passage, on a déjà vu les réponses de la forme.
    const revu = !!T.revu;
    let solides = 0;
    const lignes = Object.keys(D.prep.objectifs).map(o => {
      const [ok, tot] = res[o] || [0, 0], nv = nonVerif[o] || 0, lieu = LIEUX[D.prep.lieu[o]];
      if (!tot) return `<div class="carte" style="margin:8px 0"><b>${E(D.prep.objectifs[o])}</b><div class="retro info" style="margin:6px 0">Non vérifié au micro : refaites ces questions avec le micro.</div><p class="muted" style="margin:0;font-size:15px">${E(D.prep.conseils[o])}</p></div>`;
      // Audit tour 2 : une question passée sans micro empêche « Solide » (sinon on saute l'item difficile).
      const r = ok / tot, solideIci = r >= D.prep.solide && !nv; if (solideIci) solides++;
      const etat = solideIci ? ['ok', '✓ Solide'] : r >= .5 ? ['info', '→ En route'] : ['no', '— À reprendre'];
      return `<div class="carte" style="margin:8px 0"><b>${E(D.prep.objectifs[o])}</b><div class="retro ${etat[0]}" style="margin:6px 0">${etat[1]} — ${ok} sur ${tot}${nv ? ` (et ${nv} non vérifiée${nv > 1 ? 's' : ''} au micro)` : ''}</div>
        ${!solideIci ? `<p class="muted" style="margin:0;font-size:15px">${E(D.prep.conseils[o])}</p>` : ''}
        ${(manquees[o] || []).length ? `<p class="muted" style="margin:4px 0 0;font-size:14px">À revoir : ${manquees[o].map(t => '<i lang="en">' + E(t) + '</i>').join(' · ')}</p>` : ''}
        ${lieu ? `<p class="muted" style="margin:4px 0 0;font-size:14px">Vous en aurez besoin ${E(lieu)}.</p>` : ''}</div>`;
    }).join('');
    T.prochaine = 1 - f; T.passages = (T.passages || 0) + 1; T.dernier = aujourdhui(); sauver();
    const tous = solides === Object.keys(D.prep.objectifs).length;
    app.innerHTML = `${retour('accueil', 'Accueil')}<h1>Où vous en êtes</h1>
      <p>Un repère sur un échantillon, pas une note. La prochaine fois — la veille du départ, par exemple — ce sera l'autre forme.</p>
      ${tous ? (revu ? '<div class="retro info">Vous connaissiez déjà ces questions : ce résultat dit surtout que vous vous en souvenez. Pour vous situer pour vrai, faites une séance que vous n’avez pas faite.</div>' : '<div class="retro ok">✓ Solide partout : vous pouvez sauter les séances, ou n’y revenir que pour vous rafraîchir la mémoire.</div>') : ''}${lignes}
      <button class="btn btn--pri btn--large" onclick="aller('prep')">${tous ? 'Ma valise' : 'Aux séances'}</button>`;
  }
  intro();
}

/* ---------- étape 2 : les planches et les faux amis ---------- */
const PICTO = {
  gauche:'<svg viewBox="0 0 64 64"><path d="M50 32H16M28 18 14 32l14 14" fill="none" stroke="#7A3B1D" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  droite:'<svg viewBox="0 0 64 64"><path d="M14 32h34M36 18l14 14-14 14" fill="none" stroke="#7A3B1D" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  droit:'<svg viewBox="0 0 64 64"><path d="M32 52V14M18 26l14-14 14 14" fill="none" stroke="#7A3B1D" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  blocs:'<svg viewBox="0 0 64 64"><rect x="6" y="6" width="22" height="22" rx="2" fill="#E9DCD2"/><rect x="36" y="6" width="22" height="22" rx="2" fill="#E9DCD2"/><rect x="6" y="36" width="22" height="22" rx="2" fill="#E9DCD2"/><rect x="36" y="36" width="22" height="22" rx="2" fill="#E9DCD2"/><path d="M32 60V32H58" fill="none" stroke="#7A3B1D" stroke-width="4" stroke-linecap="round" stroke-dasharray="1 7"/><circle cx="32" cy="60" r="4" fill="#7A3B1D"/></svg>',
  carrefour:'<svg viewBox="0 0 64 64"><rect x="26" y="2" width="12" height="60" fill="#D8D3CC"/><rect x="2" y="26" width="60" height="12" fill="#D8D3CC"/><circle cx="32" cy="32" r="6" fill="#C8102E"/></svg>',
  huard:'<svg viewBox="0 0 64 64"><polygon points="32,6 54,17 54,47 32,58 10,47 10,17" fill="#D4A62A" stroke="#7A5A10" stroke-width="2"/><path d="M20 38c6-8 16-8 24-2" fill="none" stroke="#7A5A10" stroke-width="3" stroke-linecap="round"/><circle cx="40" cy="30" r="2.5" fill="#7A5A10"/></svg>',
  deux:'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="27" fill="#C9CDD2" stroke="#5F656C" stroke-width="2"/><circle cx="32" cy="32" r="17" fill="#D4A62A" stroke="#7A5A10" stroke-width="2"/></svg>',
  '25':'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="22" fill="#C9CDD2" stroke="#5F656C" stroke-width="2"/><path d="M22 40c4-10 14-14 20-10" fill="none" stroke="#5F656C" stroke-width="3" stroke-linecap="round"/></svg>',
  thermo:'<svg viewBox="0 0 64 64"><rect x="26" y="6" width="12" height="40" rx="6" fill="#fff" stroke="#333" stroke-width="2.5"/><rect x="29" y="20" width="6" height="28" fill="#C8102E"/><circle cx="32" cy="50" r="9" fill="#C8102E" stroke="#333" stroke-width="2.5"/></svg>'
};
function boussole(dir){ const ang = {nord:0, est:90, sud:180, ouest:270}[dir];
  return `<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="27" fill="#fff" stroke="#333" stroke-width="2.5"/><g transform="rotate(${ang} 32 32)"><polygon points="32,9 39,34 32,29 25,34" fill="#C8102E"/></g><circle cx="32" cy="32" r="3" fill="#333"/></svg>`; }
function horloge(h, m){
  const a = (h % 12) * 30 + m / 2, b = m * 6, rad = x => (x - 90) * Math.PI / 180;
  const pt = (ang, L) => [32 + L * Math.cos(rad(ang)), 32 + L * Math.sin(rad(ang))];
  let t = ''; for (let i = 0; i < 12; i++) { const [x1, y1] = pt(i * 30, 24), [x2, y2] = pt(i * 30, 27); t += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#333" stroke-width="2"/>`; }
  const [ax, ay] = pt(a, 15), [bx, by] = pt(b, 23);
  return `<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="29" fill="#fff" stroke="#333" stroke-width="3"/>${t}<line x1="32" y1="32" x2="${ax}" y2="${ay}" stroke="#111" stroke-width="4" stroke-linecap="round"/><line x1="32" y1="32" x2="${bx}" y2="${by}" stroke="#111" stroke-width="2.5" stroke-linecap="round"/><circle cx="32" cy="32" r="2.5" fill="#111"/></svg>`;
}
function picto(nom){
  if (PICTO[nom]) return PICTO[nom];
  if (['nord', 'sud', 'est', 'ouest'].includes(nom)) return boussole(nom);
  const m = /^h(\d{2})(\d{2})?$/.exec(nom); if (m) return horloge(+m[1], m[2] ? +m[2] : 0);
  return '';
}
function visuel(m, id){
  if (m.img === 'croquis') return `<span class="vis"><img src="${BASE}croquis/${id}.jpg?v=${D.v}" alt="" loading="lazy"></span>`;
  if (m.img && m.img.startsWith('picto:')) return `<span class="vis">${picto(m.img.slice(6))}</span>`;
  return `<span class="vis vide" aria-hidden="true">${ICO.son}</span>`;
}
function vueMots(){
  const n = p => D.planches.length && Object.values(D.mots).filter(m => m.p === p).length;
  app.innerHTML = `${retour('accueil', 'Accueil')}<p class="surtitre">Les mots</p><h1>Douze planches</h1>
    <p>Touchez un mot : vous l'entendez, et son sens en français apparaît. Répétez-le à voix haute. Les <b>faux amis</b> sont marqués : ils ont
    leur série à part.</p>
    <div class="pl-liste">${D.planches.map(([k, fr, en]) => `<button onclick="aller('mots/${k}')"><b>${E(fr)}</b><span lang="en">${E(en)} · ${n(k)} mots</span></button>`).join('')}</div>
    <button class="btn btn--large" style="margin-top:14px" onclick="aller('pieges')">Les faux amis : la série</button>`;
}
function vuePlanche(k){
  const pl = D.planches.find(x => x[0] === k); if (!pl) return vueMots();
  const i = D.planches.indexOf(pl), suiv = D.planches[i + 1];
  const ids = Object.keys(D.mots).filter(id => D.mots[id].p === k);
  app.innerHTML = `${retour('mots', 'Les planches')}<p class="surtitre">Planche ${i + 1} sur ${D.planches.length}</p><h1>${E(pl[1])}</h1>
    <label class="aide-bascule bascule-sens"><input type="checkbox" id="sens" ${S.aide ? 'checked' : ''}> Montrer le sens en français</label>
    <div class="grille">${ids.map(id => { const m = D.mots[id], pg = m.note.startsWith('PIÈGE');
      return `<button class="mot${pg ? ' piege-m' : ''}" data-id="${id}" aria-label="Écouter : ${E(m.en)}">${visuel(m, id)}
        <span class="en" lang="en">${E(m.en)}</span><span class="fr" ${S.aide ? '' : 'hidden'}>${E(m.fr)}</span>
        ${pg ? '<span class="piege">Faux ami</span>' : ''}${m.note && !pg ? `<span class="note" ${S.aide ? '' : 'hidden'}>${E(m.note)}</span>` : ''}</button>`; }).join('')}</div>
    ${suiv ? `<button class="btn btn--pri btn--large" style="margin-top:14px" onclick="aller('mots/${suiv[0]}')">Planche suivante : ${E(suiv[1])}</button>` : ''}`;
  app.querySelectorAll('.mot').forEach(b => b.onclick = () => { jouer('mots/' + b.dataset.id + '.mp3'); b.querySelectorAll('.fr,.note').forEach(x => x.hidden = false); });
  $('#sens').onchange = e => { S.aide = e.target.checked; sauver(); app.querySelectorAll('.mot .fr,.mot .note').forEach(x => x.hidden = !S.aide); };
}
/* La série des faux amis : chaque piège dans sa phrase de voyage (règle de l'hôtel : jamais montré seul).
   La place de la bonne lecture est tirée au hasard (leçon de la boucle de l'étape 1). */
function vuePieges(){
  const items = [...D.pieges].sort(() => Math.random() - .5).slice(0, 10);
  let n = 0, premiers = 0;
  function tour(){
    if (n >= items.length) {
      app.innerHTML = `${retour('mots', 'Les planches')}<h1>Les faux amis</h1><div class="retro ok">✓ ${items.length} pièges, dont ${premiers} déjoués du premier coup.</div>
        <p class="muted">La série tire dix pièges sur ${D.pieges.length} : refaites-la, ce ne seront pas les mêmes.</p>
        <button class="btn btn--pri btn--large" onclick="rendre()">Une autre série</button>
        <button class="btn btn--large" style="margin-top:8px" onclick="aller('mots')">Les planches</button>`; return; }
    const it = items[n], ch = [[it.bonne, null], [it.fausse, it.expl], [it.seconde, it.expl]];
    const o = ordre(3, Math.floor(Math.random() * 9973)); let erreurs = 0, fini = false;
    app.innerHTML = `${retour('mots', 'Les planches')}<p class="surtitre">Faux ami ${n + 1} sur ${items.length}</p>
      <div class="progres"><i style="width:${100 * n / items.length}%"></i></div><h2>Que veut dire la phrase ?</h2>
      <div class="gros-son"><button class="btn btn--son" aria-label="Écouter" id="rejouer">${ICO.son}</button></div>
      <p class="phrase-en" lang="en" style="text-align:center">${E(it.en)}</p>
      <div class="choix">${o.map(i => `<button data-i="${i}">${E(ch[i][0])}</button>`).join('')}</div><div id="r" aria-live="polite"></div>`;
    const f = 'pieges/' + it.id + '.mp3'; $('#rejouer').onclick = () => jouer(f); setTimeout(() => jouer(f), 250);
    app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      if (fini || b.disabled) return; const i = +b.dataset.i;
      if (i === 0) { fini = true; if (!erreurs) premiers++; b.classList.add('juste');
        $('#r').innerHTML = `<div class="retro ok">✓ ${E(it.expl)}</div>`;
        const s2 = document.createElement('button'); s2.className = 'btn btn--pri btn--large'; s2.textContent = 'Suivant'; s2.onclick = () => { n++; tour(); }; $('#r').appendChild(s2);
      } else { erreurs++; b.classList.add('faux'); b.disabled = true; $('#r').innerHTML = `<div class="retro no">${i === 1 ? 'C’est le piège. ' : ''}${E(ch[i][1])} Essayez encore.</div>`; }
    });
  }
  tour();
}

/* ---------- réglages ---------- */
function vueReglages(){
  app.innerHTML = `${retour('accueil', 'Accueil')}<h1>Réglages</h1>
    <label class="aide-bascule"><input type="checkbox" id="lent" ${S.lent ? 'checked' : ''}> Les voix plus lentes (sauf au test)</label>
    <label class="aide-bascule"><input type="checkbox" id="aide" ${S.aide ? 'checked' : ''}> Montrer le sens en français dès l'arrivée</label>
    <p class="muted" style="font-size:14.5px">Votre progression reste dans ce téléphone : rien n'est envoyé.</p>
    <button class="btn" id="raz">Tout recommencer</button>`;
  $('#lent').onchange = e => { S.lent = e.target.checked; sauver(); };
  $('#aide').onchange = e => { S.aide = e.target.checked; sauver(); };
  $('#raz').onclick = () => { if (confirm('Effacer votre progression dans ce téléphone ?')) { S = {lent:false, aide:false, prep:{}}; sauver(); aller('accueil'); } };
}

// Le contrôle par programme (leçon de Compostelle : jouer chaque temps trouve ce qu'aucune relecture ne voit).
window.__toronto = {D, S: () => S, trouve, plat, extraits: () => D.sons,
  controle: () => [...D.controle.refus.filter(([c, t]) => trouve(t, c)).map(([, t]) => 'accepte à tort : ' + t),
                   ...D.controle.accepte.filter(([c, t]) => !trouve(t, c)).map(([, t]) => 'refuse à tort : ' + t)]};
rendre();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
