#!/usr/bin/env python3
"""La page de tri de l'audit impeccable du portail élève — un jugement par constat.

    python3 build/audit_impeccable_page.py   # écrit assets/presentations/decider/audit-impeccable-eleve.html

Le 30 septembre 2026, eleve.html a été audité avec la grille « audit » de la
compétence impeccable (cinq dimensions notées sur 4, constats P0 à P3), SANS son
lanceur — décision de Daniel : aucun binaire téléchargé. La page a été rendue et
mesurée à 320, 390, 640 et 1280 px. Les constats qui contredisaient le système de
design ont été écartés à la source et sont montrés à part, avec leur raison.

La source est data/audit/impeccable-eleve.json ; la page est GÉNÉRÉE. Les
décisions vivent dans le localStorage du poste ; « Exporter » rend le JSON qui
pilote les corrections.
"""
import html
import json
import pathlib

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "data" / "audit" / "impeccable-eleve.json"
SORTIE = RACINE / "assets" / "presentations" / "decider" / "audit-impeccable-eleve.html"

DIMS = [("accessibilite", "Accessibilité"), ("performance", "Performance"), ("responsive", "Téléphone et écrans"),
        ("theming", "Jetons et couleurs"), ("integrite", "Fidélité au système")]
GRAV = {"P0": "Bloquant", "P1": "Majeur", "P2": "Mineur", "P3": "Finition"}
CAT = dict(DIMS)


def e(t):
    return html.escape(str(t or ""))


def carte(c):
    return f"""<article class="c" id="{e(c['id'])}" data-id="{e(c['id'])}" data-g="{e(c['gravite'])}" data-cat="{e(c['categorie'])}">
  <div class="tete"><span class="g g-{e(c['gravite'])}">{e(c['gravite'])} · {GRAV.get(c['gravite'], '')}</span><span class="cat">{e(CAT.get(c['categorie'], c['categorie']))}</span><span class="num">{e(c['id'])}</span></div>
  <h2>{e(c['titre'])}</h2>
  <div class="bloc"><b>Pour l'élève</b><p>{e(c.get('impact'))}</p></div>
  <div class="bloc geste"><b>Correction proposée</b><p>{e(c.get('correction'))}</p></div>
  <details><summary>Preuve et emplacement</summary><p>{e(c.get('preuve'))}</p><p class="ou">{e(c.get('ou'))}</p></details>
  <div class="dec" role="group" aria-label="Décision sur {e(c['id'])}">
    <button type="button" data-v="corriger">Corriger</button>
    <button type="button" data-v="tard">Plus tard</button>
    <button type="button" data-v="non">Non</button>
    <input type="text" class="note" placeholder="Une note (facultatif)" aria-label="Note sur {e(c['id'])}">
  </div>
</article>"""


def main():
    d = json.loads(SOURCE.read_text(encoding="utf-8"))
    ordre = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    cons = sorted(d["constats"], key=lambda c: (ordre.get(c["gravite"], 9), c["id"]))
    total = sum(d["scores"].values())
    scores = "".join('<div><b>%d<small>/4</small></b><span>%s</span></div>' % (d["scores"].get(k, 0), lib) for k, lib in DIMS)
    comptes = {g: sum(1 for c in cons if c["gravite"] == g) for g in GRAV}
    filtres = "".join('<button type="button" data-f="%s" aria-pressed="false">%s (%d)</button>' % (g, g, n)
                      for g, n in comptes.items() if n)
    ecartes = "".join("<li><b>%s</b> — %s</li>" % (e(x["titre"]), e(x["raison"])) for x in d.get("ecartes", []))
    positifs = "".join("<li>%s</li>" % e(p) for p in d.get("positifs", []))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(GABARIT % {
        "total": total, "scores": scores, "n": len(cons), "filtres": filtres,
        "methode": e(d.get("methode")), "verdict": e(d.get("verdict_integrite")),
        "cartes": "\n".join(carte(c) for c in cons), "ecartes": ecartes, "necartes": len(d.get("ecartes", [])),
        "positifs": positifs, "date": e(d.get("date", "30 septembre 2026")),
        "data": json.dumps([{k: c[k] for k in ("id", "gravite", "categorie", "titre")} for c in cons], ensure_ascii=False),
    }, encoding="utf-8")
    print("Écrit : %s (%d constats)" % (SORTIE.relative_to(RACINE), len(cons)))


GABARIT = r"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Audit du portail élève</title>
<style>
@font-face{font-family:"Nunito";src:url("../../design-system/fonts/nunito-latin.woff2") format("woff2");font-weight:200 1000;font-display:swap}
:root{--paper:#F7F7F5;--card:#fff;--ink:#17181A;--ink-2:#4A4D52;--line:#E4E3DE;--accent:#0A8F5B;--accent-bg:#E7F4EE;
      --rouge:#B3261E;--rouge-bg:#FFF6F5;--ambre:#9A5B00;--ambre-bg:#FBF1E0;--gris:#6B6E73;--gris-bg:#EFEFEC}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%%}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.55 "Nunito",system-ui,-apple-system,"Segoe UI",sans-serif}
.cadre{max-width:920px;margin:0 auto;padding:32px 16px 96px}
.sur{font-weight:800;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--gris)}
h1{font-size:34px;line-height:1.15;margin:6px 0 12px;font-weight:900}
.chapeau{font-size:18px;color:var(--ink-2);max-width:64ch;margin:0 0 20px}
.scores{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin:0 0 16px}
.scores div{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
.scores b{display:block;font-size:28px;font-weight:900;line-height:1}
.scores small{font-size:14px;color:var(--gris);font-weight:800}
.scores span{font-size:14px;color:var(--ink-2)}
.scores .tot{background:var(--ink);color:#fff;border-color:var(--ink)}.scores .tot span,.scores .tot small{color:#ddd}
.encart{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:12px;padding:14px 18px;margin:0 0 16px}
.encart p{margin:4px 0}
.barre{position:sticky;top:0;z-index:5;background:var(--paper);padding:12px 0;border-bottom:1px solid var(--line);margin-bottom:16px;display:flex;flex-wrap:wrap;gap:12px;align-items:center}
button{font:inherit;font-size:15px;font-weight:700;min-height:44px;padding:0 16px;border:1px solid var(--line);border-radius:999px;background:var(--card);color:var(--ink);cursor:pointer}
button[aria-pressed=true]{background:var(--ink);color:#fff;border-color:var(--ink)}
.fin{margin-left:auto;display:flex;gap:12px;align-items:center}
.cpt{font-size:14px;color:var(--ink-2);font-variant-numeric:tabular-nums}
button:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.c{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin:0 0 14px}
.c[hidden]{display:none}.c.fait{border-color:var(--ink)}
.tete{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.g,.cat{font-size:13px;font-weight:800;padding:3px 10px;border-radius:999px}
.g-P0,.g-P1{color:var(--rouge);background:var(--rouge-bg)}.g-P2{color:var(--ambre);background:var(--ambre-bg)}.g-P3{color:var(--gris);background:var(--gris-bg)}
.cat{color:var(--ink-2);border:1px solid var(--line)}
.num{margin-left:auto;font:700 13px ui-monospace,Menlo,monospace;color:var(--gris)}
.c h2{font-size:20px;line-height:1.3;margin:10px 0 6px;font-weight:800}
.bloc{border-left:3px solid var(--line);padding:2px 0 2px 14px;margin:10px 0}
.bloc b{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--gris)}
.bloc p{margin:2px 0 0}.geste{border-left-color:var(--accent)}
details{font-size:15px;color:var(--ink-2);margin-top:6px}
summary{cursor:pointer;font-weight:700;color:var(--ink);min-height:36px;display:flex;align-items:center}
.ou{font-family:ui-monospace,Menlo,monospace;font-size:13px;word-break:break-word}
.dec{display:flex;flex-wrap:wrap;gap:12px;margin-top:14px;padding-top:14px;border-top:1px solid var(--line)}
.dec .note{flex:1 1 220px;min-height:44px;font:inherit;font-size:16px;padding:0 14px;border:1px solid var(--line);border-radius:10px;background:var(--paper);color:var(--ink)}
.annexe{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin-top:24px}
.annexe h2{font-size:18px;margin:0 0 8px}.annexe li{margin:6px 0}
@media (max-width:640px){h1{font-size:28px}.scores{grid-template-columns:repeat(3,1fr)}.fin{margin-left:0;width:100%%}.c{padding:16px}}
@media print{.barre,.dec{display:none}.c{break-inside:avoid}}
</style></head>
<body><div class="cadre">
<div class="sur">francis · Décider · à trancher</div>
<h1>Audit du portail élève</h1>
<p class="chapeau">eleve.html passé à la grille « audit » d'impeccable, sans son programme, le %(date)s. %(n)d constats, chacun vérifié dans le code. Ceux qui contredisaient le système de design sont écartés plus bas. Une décision par constat ; « Exporter » rend la liste des corrections à faire.</p>
<div class="scores">%(scores)s<div class="tot"><b>%(total)d<small>/20</small></b><span>Acceptable</span></div></div>
<div class="encart"><p><b>Ce qui a été mesuré.</b> %(methode)s</p></div>
<div class="encart"><p><b>Fidélité au système.</b> %(verdict)s</p></div>
<div class="barre" role="toolbar" aria-label="Filtrer">
  <button type="button" data-f="tout" aria-pressed="true">Tous</button>%(filtres)s
  <span class="fin"><span class="cpt" id="cpt"></span><button type="button" id="exp">Exporter</button></span>
</div>
<main id="liste">
%(cartes)s
</main>
<section class="annexe"><h2>Ce qui marche, à garder</h2><ul>%(positifs)s</ul></section>
<section class="annexe"><h2>Écartés parce qu'ils contredisent le système (%(necartes)d)</h2><ul>%(ecartes)s</ul></section>
<p style="font-size:14px;color:var(--gris);margin-top:32px">Source : data/audit/impeccable-eleve.json. Page engendrée par build/audit_impeccable_page.py.</p>
</div>
<script>
(function(){
  var DATA=%(data)s, CLE="audit-impeccable-eleve-v1", etat={};
  try{etat=JSON.parse(localStorage.getItem(CLE)||"{}")}catch(e){etat={}}
  function garder(){try{localStorage.setItem(CLE,JSON.stringify(etat))}catch(e){}}
  var cartes=[].slice.call(document.querySelectorAll(".c"));
  function compter(){document.getElementById("cpt").textContent=cartes.filter(function(c){return (etat[c.dataset.id]||{}).v}).length+" / "+cartes.length+" tranchés"}
  cartes.forEach(function(c){
    var id=c.dataset.id, bs=[].slice.call(c.querySelectorAll(".dec button")), note=c.querySelector(".note");
    function peindre(){var v=(etat[id]||{}).v; bs.forEach(function(b){b.setAttribute("aria-pressed",String(b.dataset.v===v))}); c.classList.toggle("fait",!!v)}
    note.value=(etat[id]||{}).note||"";
    bs.forEach(function(b){b.addEventListener("click",function(){var x=etat[id]||{}; x.v=(x.v===b.dataset.v)?"":b.dataset.v; etat[id]=x; garder(); peindre(); compter();})});
    note.addEventListener("input",function(){var x=etat[id]||{}; x.note=note.value; etat[id]=x; garder();});
    peindre();
  });
  [].slice.call(document.querySelectorAll(".barre [data-f]")).forEach(function(b,_,tous){
    b.addEventListener("click",function(){tous.forEach(function(x){x.setAttribute("aria-pressed",String(x===b))});
      cartes.forEach(function(c){c.hidden=!(b.dataset.f==="tout"||c.dataset.g===b.dataset.f)})});
  });
  document.getElementById("exp").addEventListener("click",function(){
    var out={page:"audit-impeccable-eleve",date:new Date().toISOString().slice(0,10),decisions:DATA.map(function(c){var x=etat[c.id]||{};return {id:c.id,gravite:c.gravite,titre:c.titre,decision:x.v||"",note:x.note||""}})};
    var txt=JSON.stringify(out,null,2), a=document.createElement("a");
    a.href=URL.createObjectURL(new Blob([txt],{type:"application/json"})); a.download="audit-impeccable-eleve-decisions.json"; a.click();
    if(navigator.clipboard){navigator.clipboard.writeText(txt).catch(function(){})}
  });
  compter();
})();
</script>
</body></html>
"""

if __name__ == "__main__":
    main()
