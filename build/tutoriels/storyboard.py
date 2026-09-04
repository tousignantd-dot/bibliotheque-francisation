#!/usr/bin/env python3
"""Le storyboard du guide papier : chaque texte à côté de sa capture, à approuver.

    python3 build/tutoriels/storyboard.py          # → assets/presentations/storyboard-tutoriels.html

Demandé le 3 septembre 2026, après un premier guide papier dont les copies
d'écran ne montraient pas ce que le texte annonçait : « est-ce qu'on va revenir
au storyboard ? Puis tu me mets cette fois-là le texte avec la capture d'écran
à côté pour que je l'approuve ou pas ». C'est la même leçon que pour la vidéo,
appliquée au papier : **on valide avant de fabriquer**.

Ce que la page montre, une ligne par étape :

· le **texte** exact du document, tel qu'il sera imprimé ;
· la **capture** telle qu'elle sera imprimée, à sa vraie proportion ;
· **ce qui est cadré** — le sélecteur du plan, écrit en clair — parce que c'est
  lui la cause quand l'image ne montre pas la bonne chose, et qu'on ne peut pas
  le deviner en regardant l'image ;
· un **verdict** à cocher : bonne, à recadrer, à reprendre — et une note.

Les verdicts vivent dans `guide/verdicts.json` (volume de travail, non
versionné) et se posent par un clic ; la page les recharge au retour. Elle ne
se sert **pas** du serveur du portail : on doit pouvoir la relire dans le
train.

Ce que la page ne fait pas : corriger. Un cadrage se corrige dans
`manifeste.json` (le champ `surligne` du plan), puis on refait les captures —
`node build/tutoriels/guide_captures.js 5321`. Deux gestes, et c'est voulu :
une page qui écrirait dans le manifeste ferait une seconde source.
"""
import html
import json
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parent.parent
SORTIE = RACINE / "assets/presentations/storyboard-tutoriels.html"
VERDICTS = ICI / "guide" / "verdicts.json"

sys.path.insert(0, str(ICI))
import papier                                     # noqa: E402  (PROMESSES, phrases)


# Le micro du rail « Mes outils » : grille 24, trait 2,2, bouts ronds.
MICRO = ('<svg viewBox="0 0 24 24" aria-hidden="true">'
         '<rect x="9" y="3" width="6" height="11" rx="3"></rect>'
         '<path d="M5 11a7 7 0 0 0 14 0"></path><path d="M12 18v3"></path></svg>')

PAGE = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Storyboard du guide papier</title>
<link rel="stylesheet" href="../design-system/marque-francis.css">
<style>
:root{--ink:#17181A;--soft:#4B4F52;--muted:#6E7275;--paper:#FAFAF8;--card:#FFFFFF;
      --rule:#E4E4E0;--sunken:#F4F4F1;--ok:#0A8F5B;--cadre:#B45309;--reprendre:#A83A22}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
     font:15px/1.55 'Nunito','Helvetica Neue',Arial,sans-serif}
.page{max-width:1180px;margin:0 auto;padding:28px 22px 90px}
h1{font-size:27px;font-weight:900;letter-spacing:-.02em;margin:18px 0 4px}
.sous{color:var(--soft);margin:0 0 22px;max-width:760px}
h2{font-size:20px;font-weight:900;margin:38px 0 4px;padding-top:20px;border-top:2px solid var(--ink)}
h2 .n{color:var(--muted);font-size:13px;display:block;font-weight:800;letter-spacing:.08em;
      text-transform:uppercase}
.etape{display:grid;grid-template-columns:minmax(300px,1fr) minmax(340px,1.15fr);
       gap:0 22px;background:var(--card);border:1px solid var(--rule);border-radius:10px;
       padding:16px 18px;margin:0 0 14px}
.etape.v-bonne{border-left:4px solid var(--ok)}
.etape.v-cadrer{border-left:4px solid var(--cadre)}
.etape.v-reprendre{border-left:4px solid var(--reprendre)}
.num{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
     color:var(--muted);margin-bottom:4px}
.tit{font-weight:900;font-size:16px;margin:0 0 6px}
.txt{color:#2D2F33;margin:0 0 10px}
.cadre-info{font-size:13px;color:var(--soft);background:var(--sunken);border-radius:6px;
            padding:7px 10px;margin-bottom:10px}
.cadre-info code{font:12px ui-monospace,Menlo,monospace}
.vue{align-self:start}
.vue img{width:100%;border:1px solid var(--rule);border-radius:6px;display:block;background:#fff}
.vue .absent{border:1px dashed var(--reprendre);border-radius:6px;padding:22px;text-align:center;
             color:var(--reprendre);font-weight:700}
.verdicts{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
.verdicts button{font:inherit;font-size:13px;font-weight:700;padding:5px 11px;cursor:pointer;
                 border:1px solid var(--rule);background:#fff;border-radius:999px;color:var(--soft)}
.verdicts button[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:#fff}
textarea{width:100%;margin-top:8px;font:inherit;font-size:13.5px;padding:8px 10px;
         border:1px solid var(--rule);border-radius:6px;resize:vertical;min-height:38px;
         background:#fff;color:var(--ink)}
.note{position:relative;margin-top:8px}
.note textarea{margin-top:0;padding-right:46px}
.micro{position:absolute;right:8px;bottom:9px;width:30px;height:30px;padding:0;cursor:pointer;
       border:1px solid var(--rule);border-radius:50%;background:#fff;
       display:flex;align-items:center;justify-content:center}
.micro svg{width:15px;height:15px;fill:none;stroke:var(--soft);stroke-width:2;stroke-linecap:round}
.micro[aria-pressed="true"]{background:var(--reprendre);border-color:var(--reprendre)}
.micro[aria-pressed="true"] svg{stroke:#fff}
.depot{margin-top:10px;padding:12px;text-align:center;cursor:pointer;background:var(--sunken);
       border:1px dashed var(--rule);border-radius:8px;color:var(--muted);font-size:13px}
.depot:hover,.depot.sur{border-color:var(--ink);color:var(--ink)}
.depot img{display:block;width:100%;margin-bottom:8px;border:1px solid var(--rule);border-radius:6px}
.depot .nom{display:block;font-weight:800;color:var(--ok);font-size:12.5px}
.depot input{display:none}
.barre{position:sticky;bottom:0;background:rgba(250,250,248,.96);border-top:1px solid var(--rule);
       padding:12px 22px;margin:0 -22px -90px;display:flex;gap:16px;align-items:center;
       backdrop-filter:blur(6px)}
.barre b{font-size:15px}.barre span{color:var(--soft);font-size:13.5px}
.barre .copier{margin-left:auto;font:inherit;font-weight:800;padding:8px 16px;cursor:pointer;
               border:0;border-radius:8px;background:var(--ink);color:#fff}
@media (max-width:900px){.etape{grid-template-columns:1fr}.vue{margin-top:12px}}
</style></head><body><div class="page">
<span class="fr-lockup fr-lockup--grand fr-lockup--sombre">
  <span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span>
  <span class="fr-trait" aria-hidden="true"></span>
  <span class="fr-desc">Aide à l'apprentissage du français</span>
</span>
<h1>Storyboard du guide papier</h1>
<p class="sous">Chaque étape du document, avec le texte à gauche et la copie d'écran telle
qu'elle sera imprimée à droite. <b>Ce qui est cadré</b> dit quel élément de la page l'image
suit : c'est lui qu'on change quand l'image ne montre pas ce que le texte annonce.
Cochez un verdict par étape ; ils sont gardés dans ce navigateur, et le bouton du bas
les recopie pour me les envoyer.</p>
{{CORPS}}
<div class="barre"><b id="compte"></b><span id="detail"></span>
<button class="copier" id="copier">Copier les verdicts</button></div>
</div>
<script>
const CLE = 'storyboard-tutoriels';
const etat = JSON.parse(localStorage.getItem(CLE) || '{}');
function peindre(){
  let bonnes = 0, cadrer = 0, reprendre = 0, vus = 0;
  document.querySelectorAll('.etape').forEach((e) => {
    const v = (etat[e.dataset.cle] || {}).verdict || '';
    e.className = 'etape' + (v ? ' v-' + v : '');
    e.querySelectorAll('.verdicts button').forEach((b) => {
      b.setAttribute('aria-pressed', String(b.dataset.v === v));
    });
    if (v) vus += 1;
    if (v === 'bonne') bonnes += 1;
    if (v === 'cadrer') cadrer += 1;
    if (v === 'reprendre') reprendre += 1;
  });
  const total = document.querySelectorAll('.etape').length;
  compte.textContent = vus + ' étape' + (vus > 1 ? 's' : '') + ' sur ' + total + ' jugée'
    + (vus > 1 ? 's' : '');
  detail.textContent = bonnes + ' bonne' + (bonnes > 1 ? 's' : '') + ' · ' + cadrer
    + ' à recadrer · ' + reprendre + ' à reprendre';
}
document.addEventListener('click', (ev) => {
  const b = ev.target.closest('.verdicts button');
  if (!b) return;
  const cle = b.closest('.etape').dataset.cle;
  const f = etat[cle] || (etat[cle] = {});
  f.verdict = f.verdict === b.dataset.v ? '' : b.dataset.v;
  localStorage.setItem(CLE, JSON.stringify(etat));
  peindre();
});
document.addEventListener('input', (ev) => {
  if (!ev.target.matches('textarea')) return;
  const cle = ev.target.closest('.etape').dataset.cle;
  (etat[cle] || (etat[cle] = {})).note = ev.target.value;
  localStorage.setItem(CLE, JSON.stringify(etat));
});
document.querySelectorAll('.etape').forEach((e) => {
  const f = etat[e.dataset.cle];
  if (f && f.note) e.querySelector('textarea').value = f.note;
});
copier.addEventListener('click', () => {
  const lignes = [];
  document.querySelectorAll('.etape').forEach((e) => {
    const f = etat[e.dataset.cle] || {};
    if (!f.verdict && !f.note && !f.capture) return;
    lignes.push('- ' + e.dataset.cle + ' — ' + (f.verdict || 'sans verdict')
      + (f.note ? ' : ' + f.note : '')
      + (f.capture ? ' [capture déposée : ' + f.capture + ']' : ''));
  });
  const t = lignes.length ? lignes.join('\\n') : 'Aucun verdict posé.';
  navigator.clipboard.writeText(t).then(() => { copier.textContent = 'Copié';
    setTimeout(() => { copier.textContent = 'Copier les verdicts'; }, 1600); });
});

/* ── La dictée ─────────────────────────────────────────────────────────────
   Le champ « Ce qu'il faudrait voir à la place » se dicte : décrire un cadrage
   à la voix va plus vite qu'à deux doigts, et c'est là qu'on écrit le plus. */
const Reco = window.SpeechRecognition || window.webkitSpeechRecognition;
let reco = null, dictee = null;
function poserNote(ta){
  const cle = ta.closest('.etape').dataset.cle;
  (etat[cle] || (etat[cle] = {})).note = ta.value;
  localStorage.setItem(CLE, JSON.stringify(etat));
}
document.addEventListener('click', (ev) => {
  const b = ev.target.closest('.micro');
  if (!b) return;
  const ta = b.parentNode.querySelector('textarea');
  if (!Reco){ b.title = "La dictée demande Chrome ou Safari"; ta.focus(); return; }
  if (reco){ const meme = dictee === ta; reco.onend = null; reco.stop(); arreter(); if (meme) return; }
  dictee = ta;
  reco = new Reco();
  reco.lang = 'fr-CA'; reco.continuous = true; reco.interimResults = false;
  reco.onresult = (e) => {
    for (let i = e.resultIndex; i < e.results.length; i++){
      if (!e.results[i].isFinal) continue;
      const dit = e.results[i][0].transcript.trim();
      if (!dit) continue;
      ta.value = (ta.value ? ta.value.replace(/\s*$/, ' ') : '') + dit;
    }
    poserNote(ta);
  };
  reco.onerror = arreter;
  reco.onend = arreter;
  b.setAttribute('aria-pressed', 'true');
  ta.focus();
  reco.start();
});
function arreter(){
  document.querySelectorAll('.micro[aria-pressed="true"]')
    .forEach((b) => b.setAttribute('aria-pressed', 'false'));
  reco = null; dictee = null;
}

/* ── La bonne capture, déposée à la main ───────────────────────────────────
   Quand le cadrage ne se décrit pas, on montre. L'image déposée est **tout de
   suite téléchargée** sous le nom de son étape (`06-materiel_c.png`) : c'est
   par ce fichier-là qu'elle me parvient. La vignette, elle, reste dans le
   navigateur (IndexedDB, jamais localStorage — 48 images crèveraient le quota)
   pour qu'on voie au retour ce qu'on a déjà donné. */
let bd = null;
const ouvrirBd = () => new Promise((ok, non) => {
  if (bd) return ok(bd);
  const d = indexedDB.open('storyboard-captures', 1);
  d.onupgradeneeded = () => d.result.createObjectStore('vues');
  d.onsuccess = () => ok(bd = d.result);
  d.onerror = non;
});
const enBd = (mode, faire) => ouvrirBd().then((b) => new Promise((ok, non) => {
  const t = b.transaction('vues', mode), r = faire(t.objectStore('vues'));
  r.onsuccess = () => ok(r.result); r.onerror = non;
})).catch(() => null);

function montrer(zone, url, nom){
  zone.innerHTML = '<img src="' + url + '" alt=""><span class="nom">' + nom
    + '</span>Déposer une autre image';
}
function recevoir(zone, fichier){
  if (!fichier || !/^image\//.test(fichier.type)) return;
  const etape = zone.closest('.etape');
  const nom = etape.dataset.capsule + '_' + etape.dataset.plan
    + (fichier.name.match(/\.[a-z0-9]+$/i) || ['.png'])[0];
  const lire = new FileReader();
  lire.onload = () => {
    const url = lire.result;
    montrer(zone, url, nom);
    enBd('readwrite', (s) => s.put({url: url, nom: nom}, etape.dataset.cle));
    const cle = etape.dataset.cle;
    (etat[cle] || (etat[cle] = {})).capture = nom;
    localStorage.setItem(CLE, JSON.stringify(etat));
    const a = document.createElement('a');
    a.href = url; a.download = nom;
    document.body.appendChild(a); a.click(); a.remove();
  };
  lire.readAsDataURL(fichier);
}
document.querySelectorAll('.depot').forEach((zone) => {
  const champ = zone.querySelector('input');
  zone.addEventListener('click', () => champ.click());
  champ.addEventListener('change', () => recevoir(zone, champ.files[0]));
  zone.addEventListener('dragover', (e) => { e.preventDefault(); zone.classList.add('sur'); });
  zone.addEventListener('dragleave', () => zone.classList.remove('sur'));
  zone.addEventListener('drop', (e) => {
    e.preventDefault(); zone.classList.remove('sur');
    recevoir(zone, e.dataTransfer.files[0]);
  });
  zone.closest('.etape').addEventListener('paste', (e) => {
    const it = [...(e.clipboardData || {}).items || []].find((x) => /^image\//.test(x.type));
    if (it) recevoir(zone, it.getAsFile());
  });
  enBd('readonly', (s) => s.get(zone.closest('.etape').dataset.cle))
    .then((v) => { if (v) montrer(zone, v.url, v.nom); });
});

peindre();
</script></body></html>
"""


def main():
    manifeste = json.loads((ICI / "manifeste.json").read_text(encoding="utf-8"))
    fichier = ICI / "guide" / "captures.json"
    captures = json.loads(fichier.read_text(encoding="utf-8")) if fichier.exists() else {}

    corps = []
    for i, c in enumerate(manifeste["capsules"], 1):
        corps.append('<h2><span class="n">Chapitre %d</span>%s</h2>'
                     % (i, html.escape(c["titre"])))
        n = 0
        for plan in c["plans"]:
            if plan["id"] == "fin":
                continue
            n += 1
            titre, suite = papier.phrases(plan["texte"])
            vues = papier.images(c["id"], plan["id"], captures, plan)
            vue = ('<img src="%s" alt="">' % html.escape(
                       vues[0].replace("../../", "../../"))
                   if vues else '<div class="absent">aucune capture pour cette étape</div>')
            pap = plan.get("papier", {})
            cadre = pap.get("cadre") or plan.get("surligne") or "la fenêtre entière"
            if vues and "/deposees/" in vues[0]:
                cadre = "votre capture déposée (%s)" % pathlib.Path(vues[0]).name
            elif pap.get("apres_geste") is not None:
                cadre = "%s — après le geste %d" % (cadre, pap["apres_geste"])
            corps.append(
                '<div class="etape" data-cle="%s %d" data-capsule="%s" data-plan="%s">'
                '<div><div class="num">Étape %d</div>'
                '<p class="tit">%s</p>%s'
                '<div class="cadre-info">Ce qui est cadré : <code>%s</code></div>'
                '<div class="verdicts">'
                '<button data-v="bonne">Bonne</button>'
                '<button data-v="cadrer">À recadrer</button>'
                '<button data-v="reprendre">À reprendre</button></div>'
                '<div class="note">'
                '<textarea placeholder="Ce qu\'il faudrait voir à la place…"></textarea>'
                '<button class="micro" type="button" aria-pressed="false" '
                'aria-label="Dicter la note" title="Dicter la note">%s</button></div>'
                '</div><div class="vue">%s'
                '<div class="depot">Déposer ici la bonne capture'
                '<input type="file" accept="image/*"></div>'
                '</div></div>'
                % (html.escape(c["titre"]), n, c["id"], plan["id"], n, html.escape(titre),
                   '<p class="txt">%s</p>' % html.escape(suite) if suite else "",
                   html.escape(str(cadre)), MICRO, vue))

    SORTIE.write_text(PAGE.replace("{{CORPS}}", "".join(corps)), encoding="utf-8")
    etapes = sum(1 for c in manifeste["capsules"]
                 for p in c["plans"] if p["id"] != "fin")
    manquantes = sum(1 for c in manifeste["capsules"] for p in c["plans"]
                     if p["id"] != "fin" and not papier.images(c["id"], p["id"], captures, p))
    print("%d étapes → %s" % (etapes, SORTIE.relative_to(RACINE)))
    if manquantes:
        print("  ⚠ %d étape(s) sans capture — node build/tutoriels/guide_captures.js 5321"
              % manquantes)


if __name__ == "__main__":
    main()
