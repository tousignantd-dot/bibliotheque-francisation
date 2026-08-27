#!/usr/bin/env python3
"""La page d'écoute d'un banc d'essai de voix, avec les cases pour écarter.

Les deux bancs — `essai_gemini_tts.py` et `essai_azure.py` — se jugent de la
même façon : on écoute, et on coche ce qui ne va pas. La page était née dans
le banc Gemini ; la recopier dans celui d'Azure aurait garanti que les deux
divergent à la première retouche. Elle vit donc ici, et chaque banc lui passe
son titre, son chapeau et l'ordre de ses blocs.

Chaque extrait est un dict : `bloc`, `fichier`, `affiche`, `texte`, `duree`.
"""
import html
import json

CLE_STOCKAGE = "banc-voix-ecartes"

STYLE = """<style>
body{font:16px/1.55 system-ui,-apple-system,sans-serif;max-width:56rem;
  margin:0 auto;padding:1.5rem 1rem 5rem}
h1{margin:.2rem 0 .4rem}
h2{margin:2.5rem 0 .6rem;border-bottom:1px solid #ddd;padding-bottom:.3rem;
  font-size:1.15rem;letter-spacing:.02em;text-transform:uppercase;color:#555}
table{border-collapse:collapse;width:100%}
td{padding:.4rem .8rem .4rem 0;vertical-align:middle;border-bottom:1px solid #f0f0f0}
td.k{width:1.6rem;padding-right:.2rem}
td.a{width:16rem}
td.t{color:#333}
td.d{color:#999;font-variant-numeric:tabular-nums;white-space:nowrap;
  text-align:right;font-size:.9rem}
audio{height:2rem;width:15rem}
input[type=checkbox]{width:1.15rem;height:1.15rem;accent-color:#b3261e;cursor:pointer}
tr.out td.t,tr.out td.d{color:#bbb;text-decoration:line-through}
#bilan{position:sticky;top:0;background:#fff;border-bottom:2px solid #222;
  padding:.7rem 0 .8rem;margin-bottom:.5rem;z-index:5}
#bilan b{font-size:1.05rem}
#liste{width:100%;min-height:3.4rem;font:13px/1.5 ui-monospace,monospace;
  margin-top:.5rem;padding:.5rem;border:1px solid #ccc;border-radius:4px;
  background:#fafafa;color:#333;display:none}
#liste.on{display:block}
button{font:inherit;padding:.25rem .7rem;margin-left:.5rem;cursor:pointer}
p.i{color:#666;margin:.3rem 0 1rem}
</style>"""


def page(res, titre, chapeau, ordre, cle=CLE_STOCKAGE):
    """La page complète, prête à écrire sur le disque.

    `cle` sépare les cases d'un banc de celles de l'autre dans le
    `localStorage` : les deux pages sont servies depuis `file://`, donc depuis
    la même origine, et une clé commune ferait que cocher une voix Azure
    raierait une ligne chez Gemini.
    """
    blocs = {}
    for r in res:
        blocs.setdefault(r["bloc"], []).append(r)
    out = ["<meta charset='utf-8'><title>%s</title>" % html.escape(titre), STYLE,
           "<h1>%s</h1>" % html.escape(titre),
           "<p class='i'>%s Cocher la case d'un extrait pour l'<b>écarter</b> : "
           "ce qui est coché ne convient pas. "
           "Les choix sont gardés dans le navigateur.</p>" % chapeau,
           "<div id='bilan'><b><span id='n'>0</span> extrait(s) écarté(s)</b>"
           "<button onclick='basculer()'>Voir la liste</button>"
           "<button onclick='tout()'>Tout décocher</button>"
           "<textarea id='liste' readonly></textarea></div>"]
    for nom in ordre:
        if nom not in blocs:
            continue
        out.append("<h2>%s</h2><table>" % nom)
        for r in blocs[nom]:
            cs = len(r["texte"]) / r["duree"] if r["duree"] else 0
            out.append(
                "<tr><td class='k'>"
                "<input type=checkbox data-f='%s' onchange='maj()'></td>"
                "<td class='a'><audio controls preload=none src='%s'></audio></td>"
                "<td class='t'>%s</td>"
                "<td class='d'>%.1f s &middot; %.1f c/s</td></tr>"
                % (r["fichier"], r["fichier"],
                   html.escape(r["affiche"]), r["duree"], cs))
        out.append("</table>")
    out.append("""<script>
const CLE=%s;
const cases=[...document.querySelectorAll('input[type=checkbox]')];
function ecartes(){return cases.filter(c=>c.checked).map(c=>c.dataset.f)}
function maj(){
  const e=ecartes();
  try{localStorage.setItem(CLE,JSON.stringify(e))}catch(err){}
  document.getElementById('n').textContent=e.length;
  // `String.fromCharCode(10)` plutot qu'un retour echappe : ce JS vit dans une
  // chaine Python, l'echappement s'y perd une fois de trop et la page rendue
  // se retrouvait avec une vraie coupure de ligne au milieu du script.
  document.getElementById('liste').value=e.join(String.fromCharCode(10));
  cases.forEach(c=>c.closest('tr').classList.toggle('out',c.checked));
}
function basculer(){document.getElementById('liste').classList.toggle('on')}
function tout(){cases.forEach(c=>c.checked=false);maj()}
try{
  const gardes=new Set(JSON.parse(localStorage.getItem(CLE)||'[]'));
  cases.forEach(c=>c.checked=gardes.has(c.dataset.f));
}catch(e){}
maj();
</script>""" % json.dumps(cle))
    return "\n".join(out)
