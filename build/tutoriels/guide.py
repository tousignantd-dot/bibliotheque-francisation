#!/usr/bin/env python3
"""Le guide de validation — et le procédurier papier, dans le même fichier.

    node build/tutoriels/guide_captures.js 5321   # les copies d'écran
    python3 build/tutoriels/guide.py              # la page

Décidé le 2 septembre 2026, après quatre séries de corrections trouvées au
visionnement — un bouton renommé, quatre états décrits dont un seul à l'écran,
douze dossiers ouverts à toute vitesse, « le nom de l'élève » là où le portail
exige un pseudo. Chacune a coûté un tournage complet pour deux lignes de
texte. **On ne tourne plus rien qui n'ait été relu ici.**

Une ligne par plan, trois colonnes : ce que la voix dira, ce qu'on verra,
combien de temps. Les copies d'écran sont de vraies captures du portail,
prises en rejouant les gestes du manifeste par la même fonction que le
tournage — un guide qui montrerait autre chose que le film ne servirait à
rien.

La page est aussi le **procédurier papier** : le texte lu est le texte écrit,
les vignettes sont les illustrations, et `@media print` la met en pages. Il
n'y a pas deux documents à tenir d'accord.

Les durées sont **estimées** : 2,71 mots à la seconde, relevés sur les 54
narrations déjà produites. Synthétiser pour les connaître exactement
engagerait l'argent qu'on veut justement ne pas engager avant validation — et
la synthèse HD n'étant pas déterministe, la durée exacte d'aujourd'hui ne
serait de toute façon pas celle de demain.
"""
import html
import json
import pathlib

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parent.parent
SORTIE = RACINE / "assets" / "presentations" / "guide-tutoriels-enseignant.html"

QUAND = {"debut": "au début", "milieu": "en cours", "fin": "à la fin"}


def secondes(v):
    m, s = divmod(int(round(v)), 60)
    return f"{m} min {s:02d}" if m else f"{int(round(v))} s"


def page():
    manifeste = json.loads((ICI / "manifeste.json").read_text(encoding="utf-8"))
    captures = json.loads((ICI / "guide" / "captures.json").read_text(encoding="utf-8"))
    total = 0
    corps = []
    for n, capsule in enumerate(manifeste["capsules"], 1):
        releve = {p["plan"]: p for p in captures.get(capsule["id"], [])}
        duree = sum(p["secondes"] for p in releve.values())
        total += duree
        lignes = []
        for plan in capsule["plans"]:
            r = releve.get(plan["id"], {"secondes": 0, "images": []})
            vignettes = "".join(
                '<figure><a href="../../build/tutoriels/%s" target="_blank" rel="noopener">'
                '<img src="../../build/tutoriels/%s" alt="" loading="lazy"></a>'
                '<figcaption>%s</figcaption></figure>'
                % (im["fichier"], im["fichier"], QUAND.get(im["quand"], im["quand"]))
                for im in r["images"]) or '<p class="rien">aucune capture</p>'
            dit = plan.get("texte_voix")
            note = ('<p class="note">Dit à la voix : « %s »</p>' % html.escape(dit)
                    if dit and dit != plan["texte"] else "")
            lignes.append(
                '<tr><th scope="row">%s</th>'
                '<td class="texte"><p>%s</p>%s</td>'
                '<td class="ecrans">%s</td>'
                '<td class="duree">%s</td></tr>'
                % (html.escape(plan["id"]), html.escape(plan["texte"]), note,
                   vignettes, secondes(r["secondes"])))
        corps.append(
            '<section class="capsule">'
            '<h2><span class="num">%d</span>%s</h2>'
            '<p class="resume">%d plans · environ %s</p>'
            '<table><thead><tr><th>Plan</th><th>Ce que la voix dit</th>'
            '<th>Ce qu\'on voit</th><th>Durée</th></tr></thead>'
            '<tbody>%s</tbody></table></section>'
            % (n, html.escape(capsule["titre"]), len(capsule["plans"]),
               secondes(duree), "".join(lignes)))
    # `str.replace` et non l'opérateur `%` : la feuille de style est pleine de
    # pourcentages, et le formatage les prendrait pour des marqueurs.
    tete = (TETE.replace("{{total}}", secondes(total))
                .replace("{{capsules}}", str(len(manifeste["capsules"]))))
    return tete + "".join(corps) + PIED


TETE = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Guide des tutoriels — espace enseignant</title>
<link rel="stylesheet" href="../design-system/tokens/fonts.css">
<style>
:root{
  --ground:#F7F7F5; --card:#FFFFFF; --ink:#17181A; --body:#3A3D40;
  --muted:#6E7175; --line:#E4E4E0; --accent:#0A8F5B;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--body);
  font-family:'Nunito','Helvetica Neue',Arial,sans-serif;font-size:15px;line-height:1.5}
.wrap{max-width:1100px;margin:0 auto;padding:44px 24px 90px}
h1{font-size:34px;line-height:1.15;color:var(--ink);margin:0 0 8px;letter-spacing:-.02em}
.chapeau{font-size:17px;max-width:68ch;margin:0 0 6px}
.date{font-size:12.5px;color:var(--muted);font-weight:800;letter-spacing:.07em;
  text-transform:uppercase;margin:0 0 34px}
.capsule{background:var(--card);border:1px solid var(--line);border-radius:14px;
  padding:22px 24px;margin:0 0 22px}
h2{font-size:21px;color:var(--ink);margin:0 0 2px;display:flex;align-items:center;gap:12px}
.num{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:999px;
  background:var(--accent);color:#fff;font-size:15px;flex:0 0 auto}
.resume{margin:0 0 16px;color:var(--muted);font-size:13.5px;font-weight:700}
table{width:100%;border-collapse:collapse}
thead th{text-align:left;font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;
  color:var(--muted);border-bottom:2px solid var(--line);padding:0 10px 8px}
tbody tr{border-bottom:1px solid var(--line);break-inside:avoid}
tbody th{width:44px;text-align:left;vertical-align:top;padding:14px 10px;
  font-family:var(--mono);font-size:13px;color:var(--muted);font-weight:700}
td{vertical-align:top;padding:14px 10px}
.texte{width:38%}
.texte p{margin:0;color:var(--ink);font-size:15px}
.note{margin:8px 0 0!important;font-size:12.5px;color:var(--muted)!important;font-style:italic}
.ecrans{width:44%}
/* Une vignette par ligne, a la largeur de la colonne. Cote a cote, les
   captures rognees sur une bande large — l'en-tete, la barre d'action — se
   reduisaient a un trait ou l'on ne lisait aucun mot, et un guide papier dont
   on ne lit pas les copies d'ecran ne vaut pas mieux que pas de guide. */
figure{margin:0 0 12px}
figure a{display:block}
figure img{width:100%;border:1px solid var(--line);border-radius:6px;display:block}
figcaption{font-size:11px;color:var(--muted);margin-top:3px;letter-spacing:.04em;
  text-transform:uppercase;font-weight:800}
.rien{color:var(--muted);font-style:italic;margin:0}
.duree{width:80px;text-align:right;font-family:var(--mono);font-size:13px;color:var(--ink)}
.avert{background:#FBF2E2;border:1px solid #E8D3A0;border-left:4px solid #C07A08;
  border-radius:10px;padding:16px 18px;margin:0 0 28px;color:#5A4409}
.avert b{color:#3E2F06}
@media print{
  body{background:#fff;font-size:10.5pt}
  .wrap{max-width:none;padding:0}
  .capsule{border:0;padding:0;margin:0 0 18pt;break-inside:auto}
  .capsule + .capsule{break-before:page}
  .avert{break-after:page}
  figure{margin-bottom:8pt}
}
</style>
</head>
<body>
<div class="wrap">
<h1>Guide des tutoriels — espace enseignant</h1>
<p class="chapeau">{{capsules}} capsules, environ {{total}}. Une ligne par plan :
le texte exact que dira la voix, les copies d'écran de ce qu'on verra pendant
qu'elle le dit, et la durée. À relire et à corriger <b>avant</b> qu'on
synthétise et qu'on enregistre.</p>
<p class="date">Guide du 2 septembre 2026</p>
<div class="avert">
  <p style="margin:0 0 8px"><b>Les durées sont estimées.</b> 2,71 mots à la
  seconde, relevés sur les 54 narrations déjà produites, plus 0,7 s de
  respiration. Synthétiser pour les connaître exactement engagerait la dépense
  qu'on veut éviter avant validation — et la synthèse HD n'est pas
  déterministe : deux tirages du même texte ne durent pas pareil.</p>
  <p style="margin:0"><b>Les copies d'écran sont réelles.</b> Elles viennent du
  portail de démonstration, en rejouant les gestes du manifeste par la même
  fonction que le tournage. Quand un plan surligne un élément, l'image est
  rognée dessus ; quand l'écran bouge pendant le plan, il y a plusieurs
  images ; quand il ne bouge pas, une seule.</p>
</div>
"""

PIED = """
</div>
</body>
</html>
"""


if __name__ == "__main__":
    SORTIE.write_text(page(), encoding="utf-8")
    print("écrit :", SORTIE.relative_to(RACINE))
