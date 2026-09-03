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
    if (!f.verdict && !f.note) return;
    lignes.push('- ' + e.dataset.cle + ' — ' + (f.verdict || 'sans verdict')
      + (f.note ? ' : ' + f.note : ''));
  });
  const t = lignes.length ? lignes.join('\\n') : 'Aucun verdict posé.';
  navigator.clipboard.writeText(t).then(() => { copier.textContent = 'Copié';
    setTimeout(() => { copier.textContent = 'Copier les verdicts'; }, 1600); });
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
            vues = papier.images(c["id"], plan["id"], captures)
            vue = ('<img src="%s" alt="">' % html.escape(
                       vues[0].replace("../../", "../../"))
                   if vues else '<div class="absent">aucune capture pour cette étape</div>')
            cadre = plan.get("surligne") or "la fenêtre entière"
            corps.append(
                '<div class="etape" data-cle="%s %d">'
                '<div><div class="num">Étape %d</div>'
                '<p class="tit">%s</p>%s'
                '<div class="cadre-info">Ce qui est cadré : <code>%s</code></div>'
                '<div class="verdicts">'
                '<button data-v="bonne">Bonne</button>'
                '<button data-v="cadrer">À recadrer</button>'
                '<button data-v="reprendre">À reprendre</button></div>'
                '<textarea placeholder="Ce qu\'il faudrait voir à la place…"></textarea>'
                '</div><div class="vue">%s</div></div>'
                % (html.escape(c["titre"]), n, n, html.escape(titre),
                   '<p class="txt">%s</p>' % html.escape(suite) if suite else "",
                   html.escape(str(cadre)), vue))

    SORTIE.write_text(PAGE.replace("{{CORPS}}", "".join(corps)), encoding="utf-8")
    etapes = sum(1 for c in manifeste["capsules"]
                 for p in c["plans"] if p["id"] != "fin")
    manquantes = sum(1 for c in manifeste["capsules"] for p in c["plans"]
                     if p["id"] != "fin" and not papier.images(c["id"], p["id"], captures))
    print("%d étapes → %s" % (etapes, SORTIE.relative_to(RACINE)))
    if manquantes:
        print("  ⚠ %d étape(s) sans capture — node build/tutoriels/guide_captures.js 5321"
              % manquantes)


if __name__ == "__main__":
    main()
