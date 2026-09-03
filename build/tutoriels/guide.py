#!/usr/bin/env python3
"""Le guide de validation — et le procédurier papier, dans le même fichier.

    node build/tutoriels/guide_captures.js 5321   # les copies d'écran
    python3 build/tutoriels/guide.py              # les sept capsules
    python3 build/tutoriels/guide.py 01-tour-du-portail   # une seule, + son PDF

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
import sys

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parent.parent
PRESENTATIONS = RACINE / "assets" / "presentations"
sys.path.insert(0, str(RACINE / "build"))
sys.path.insert(0, str(ICI))
import versions  # noqa: E402

QUAND = {"debut": "au début", "milieu": "en cours",
         "fin": "à la fin"}


def legende(cle):
    """« geste 3 » se lit tel quel ; le reste passe par la table."""
    if cle.startswith("geste"):
        return "après le geste " + cle[5:]
    return QUAND.get(cle, cle)


def secondes(v):
    m, s = divmod(int(round(v)), 60)
    return f"{m} min {s:02d}" if m else f"{int(round(v))} s"


def page(seule=None):
    """La page du guide. `seule` la réduit à une capsule — c'est la forme qui
    part à l'impression : un procédurier de sept capsules ne se relit pas, et
    on n'en tourne qu'une à la fois."""
    manifeste = json.loads((ICI / "manifeste.json").read_text(encoding="utf-8"))
    captures = json.loads((ICI / "guide" / "captures.json").read_text(encoding="utf-8"))
    total = 0
    corps = []
    titre = None
    for n, capsule in enumerate(manifeste["capsules"], 1):
        if seule and capsule["id"] != seule:
            continue
        titre = "%d · %s" % (n, capsule["titre"])
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
                % (im["fichier"], im["fichier"], legende(im["quand"]))
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
        v = versions.etat(capsule["id"])
        corps.append(
            '<section class="capsule">'
            '<h2><span class="num">%d</span>%s</h2>'
            '<p class="resume">%d plans · environ %s · <b>storyboard %s</b>%s</p>'
            '<table><thead><tr><th>Plan</th><th>Ce que la voix dit</th>'
            '<th>Ce qu\'on voit</th><th>Durée</th></tr></thead>'
            '<tbody>%s</tbody></table></section>'
            % (n, html.escape(capsule["titre"]), len(capsule["plans"]),
               secondes(duree), v["version"],
               " · " + v["quand"] if v.get("quand") else "",
               "".join(lignes)))
    # `str.replace` et non l'opérateur `%` : la feuille de style est pleine de
    # pourcentages, et le formatage les prendrait pour des marqueurs.
    if seule and not corps:
        raise SystemExit("capsule inconnue : %s" % seule)
    nombre = 1 if seule else len(manifeste["capsules"])
    tete = (TETE.replace("{{total}}", secondes(total))
                .replace("{{capsules}}", str(nombre))
                .replace("{{titre}}", html.escape(titre) if seule
                         else "les sept capsules")
                .replace("{{sujet}}", "Capsule %s" % html.escape(titre) if seule
                         else "%d capsules" % nombre)
                .replace("{{corps}}", "une" if seule else ""))
    return tete + "".join(corps) + PIED


TETE = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Guide des tutoriels — {{titre}}</title>
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
/* Sur un guide d'une seule capsule, le titre du bloc redit celui de la
   page : deux fois le meme titre a trois centimetres d'ecart. */
body.une .capsule h2{display:none}
body.une .capsule .resume{margin-top:0}
.duree{width:80px;text-align:right;font-family:var(--mono);font-size:13px;color:var(--ink)}
.avert{background:#FBF2E2;border:1px solid #E8D3A0;border-left:4px solid #C07A08;
  border-radius:10px;padding:16px 18px;margin:0 0 28px;color:#5A4409}
.avert b{color:#3E2F06}
@media print{
  body{background:#fff;font-size:10.5pt}
  .wrap{max-width:none;padding:0}
  .capsule{border:0;padding:0;margin:0 0 18pt;break-inside:auto}
  .capsule + .capsule{break-before:page}
  figure{margin-bottom:8pt}
}
</style>
</head>
<body class="{{corps}}">
<div class="wrap">
<h1>Guide des tutoriels — {{titre}}</h1>
<p class="chapeau">{{sujet}}, environ {{total}}. Une ligne par plan :
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



# ═══════════════════════════════════════════════════════════════════
#  LE TUTORIEL PAPIER
#
#  Même source, autre lecteur. Le guide est une pièce de validation :
#  il porte les durées, le texte « dit à la voix », les gestes, et
#  l'avertissement sur la synthèse. Rien de tout cela ne regarde une
#  enseignante à qui l'on remet un tutoriel au lieu d'une vidéo.
#
#  Ce qu'on garde : les étapes numérotées, ce qu'elle doit savoir, et
#  les copies d'écran. Ce qu'on retire : les secondes, la voix, les
#  sélecteurs. Le plan « fin » devient une note de bas de page plutôt
#  qu'une étape — on ne numérote pas un au revoir.
#
#  Le logotype est composé par le système de design, jamais redessiné
#  à la main : « francıs » en U+0131 et le point posé par le CSS.
# ═══════════════════════════════════════════════════════════════════

PAPIER = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{titre}} — tutoriel</title>
<link rel="stylesheet" href="../design-system/tokens/fonts.css">
<link rel="stylesheet" href="../design-system/marque-francis.css">
<style>
:root{--ground:#fff;--ink:#17181A;--body:#33363A;--muted:#6E7175;
  --line:#E4E4E0;--accent:#0A8F5B;--accent-pale:#E6F5EE}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--body);
  font-family:'Nunito','Helvetica Neue',Arial,sans-serif;font-size:15.5px;line-height:1.55}
.feuille{max-width:820px;margin:0 auto;padding:40px 34px 70px}
.entete{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;
  border-bottom:2px solid var(--accent);padding-bottom:14px;margin-bottom:26px}
.sur{font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;
  color:var(--accent);font-weight:900;margin:0 0 4px}
h1{font-size:30px;color:var(--ink);margin:0;letter-spacing:-.02em;line-height:1.15}
.etape{display:grid;grid-template-columns:38px 1fr;gap:16px;margin:0 0 26px;
  break-inside:avoid}
.rang{display:grid;place-items:center;width:32px;height:32px;border-radius:999px;
  background:var(--accent-pale);color:var(--accent);font-weight:900;font-size:15px}
.etape p{margin:4px 0 12px;color:var(--ink)}
.etape figure{margin:0 0 12px}
.etape img{width:100%;border:1px solid var(--line);border-radius:8px;display:block}
.fin{background:var(--accent-pale);border-radius:11px;padding:16px 20px;
  color:#08573A;margin:30px 0 0;break-inside:avoid}
.fin p{margin:0}
footer{margin-top:34px;padding-top:12px;border-top:1px solid var(--line);
  font-size:11.5px;color:var(--muted);display:flex;justify-content:space-between;gap:16px}
@page{size:letter;margin:14mm 13mm}
@media print{ .feuille{max-width:none;padding:0} body{font-size:10.5pt} }
</style>
</head>
<body>
<div class="feuille">
<div class="entete">
  <div>
    <p class="sur">Espace enseignant · tutoriel {{rang}}</p>
    <h1>{{titre}}</h1>
  </div>
  <span class="fr-lockup fr-lockup--etroit">
    <span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span>
    <span class="fr-trait" aria-hidden="true"></span>
    <span class="fr-desc">Aide à l'apprentissage du français</span>
  </span>
</div>
{{corps}}
<footer><span>{{version}} · {{quand}}</span><span>francis · espace enseignant</span></footer>
</div>
</body>
</html>
"""


def papier(seule):
    """Le tutoriel d'une capsule, écrit pour être remis sur papier."""
    manifeste = json.loads((ICI / "manifeste.json").read_text(encoding="utf-8"))
    captures = json.loads((ICI / "guide" / "captures.json").read_text(encoding="utf-8"))
    for rang, capsule in enumerate(manifeste["capsules"], 1):
        if capsule["id"] != seule:
            continue
        releve = {p["plan"]: p for p in captures.get(capsule["id"], [])}
        etapes, cloture, n = [], "", 0
        for plan in capsule["plans"]:
            images = releve.get(plan["id"], {}).get("images", [])
            # Une seule image par étape sur papier : la dernière, celle qui
            # montre l'écran une fois le geste fait. La suite début-milieu-fin
            # sert à valider un film, pas à guider quelqu'un qui lit.
            vignette = ('<figure><img src="../../build/tutoriels/%s" alt=""></figure>'
                        % images[-1]["fichier"]) if images else ""
            if plan["id"] == "fin":
                cloture = ('<div class="fin"><p>%s</p></div>'
                           % html.escape(plan["texte"]))
                continue
            n += 1
            etapes.append('<div class="etape"><div class="rang">%d</div><div>'
                          '<p>%s</p>%s</div></div>'
                          % (n, html.escape(plan["texte"]), vignette))
        v = versions.etat(capsule["id"])
        return (PAPIER.replace("{{titre}}", html.escape(capsule["titre"]))
                      .replace("{{rang}}", str(rang))
                      .replace("{{corps}}", "".join(etapes) + cloture)
                      .replace("{{version}}", v["version"])
                      .replace("{{quand}}", v.get("quand", "")))
    raise SystemExit("capsule inconnue : %s" % seule)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    seule = args[0] if args else None
    # `--papier` rend le tutoriel qu'on remet à l'enseignante : les étapes et
    # les écrans, sans les secondes ni la voix. Sans lui, c'est le guide de
    # validation qui sort.
    tutoriel = "--papier" in sys.argv
    if tutoriel and not seule:
        raise SystemExit("--papier demande une capsule")
    nom = ("tutoriel-%s" % seule if tutoriel
           else "guide-tutoriels-%s" % (seule or "enseignant"))
    fichier = PRESENTATIONS / (nom + ".html")
    fichier.write_text(papier(seule) if tutoriel else page(seule), encoding="utf-8")
    print("écrit :", fichier.relative_to(RACINE))
    # Le PDF se dépose à côté de la page, comme partout dans le dépôt : c'est
    # ce qu'on imprime et ce qu'on relit hors de l'écran.
    from imprimer import imprimer
    pdf = fichier.with_suffix(".pdf")
    pages = imprimer(fichier, pdf)
    print("imprimé :", pdf.relative_to(RACINE),
          "(%s pages)" % pages if pages else "")
