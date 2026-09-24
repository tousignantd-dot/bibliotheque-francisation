#!/usr/bin/env python3
"""La fiche de poche de la Maison Francœur — une par langue, plus le français seul.

    python3 build/francoeur_fiche.py              # les 12 pages + les 12 PDF
    python3 build/francoeur_fiche.py es --sans-pdf

Une feuille lettre, recto seul, qui reste dans la poche du tablier. Les règles
de la fiche de Chaussures Rivard, reprises telles quelles :
  · aucune couleur — elle sort de la photocopieuse du magasin ;
  · la hiérarchie passe par la graisse et les filets ;
  · les phrases restent EN FRANÇAIS ; la langue d'appui, en petit, dessous.

Le contenu vient de trois sources, rien n'est recopié : `fiche.py` (les six
phrases), `lexique.py` (pièges, couleurs, tailles), `traductions.json` (la
langue d'appui). Une ligne « quand » pas encore traduite s'imprime en français
seul — le pied de page le dit.

Sortie : assets/presentations/francoeur-fiche/fiche-<langue>.html (+ .pdf)
"""
import html, json, pathlib, re, subprocess, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-francoeur"
sys.path.insert(0, str(CONTENU))
from lexique import LEXIQUE  # noqa: E402
from fiche import PHRASES, DEFI  # noqa: E402

DEST = RACINE / "assets" / "presentations" / "francoeur-fiche"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
POLICE = "../../design-system/fonts/nunito-latin.woff2"   # relatif : vaut aussi en file://
LETTRE = (612, 792)
E = html.escape

CSS = """
@page { size: letter; margin: 9mm 11mm 8mm; }
*{box-sizing:border-box}
@font-face{font-family:'Nunito';src:url('@@POLICE@@') format('woff2');font-weight:400 800}
html,body{margin:0;background:#FFF;color:#000}
body{font-family:'Nunito',-apple-system,'Segoe UI','Geeza Pro','PingFang SC','Kefa',sans-serif;font-size:9.6pt;line-height:1.3}
.f{max-width:190mm;margin:0 auto}
.tete{display:flex;align-items:flex-end;justify-content:space-between;gap:12px;border-bottom:2.2pt solid #000;padding-bottom:5px}
.tete h1{font-size:15.5pt;font-weight:800;margin:0;line-height:1.05}
.tete .ou{font-size:8pt;font-weight:700;text-transform:uppercase;letter-spacing:.11em;text-align:right}
h2{font-size:8pt;font-weight:800;text-transform:uppercase;letter-spacing:.11em;margin:8px 0 3px}
ol.p{list-style:none;margin:0;padding:0}
ol.p li{border-bottom:.6pt solid #B8B8B8;padding:3px 0 3px 22px;position:relative;break-inside:avoid}
ol.p li:first-child{border-top:.6pt solid #B8B8B8}
ol.p .n{position:absolute;left:0;top:5px;font-size:11.5pt;font-weight:800}
ol.p .fr{font-size:11.2pt;font-weight:800;line-height:1.2}
ol.p .q{font-size:8.4pt;margin-top:0}
.ap{font-size:8.2pt;line-height:1.25;color:#3A3A3A;margin-top:1px;padding-left:7px;border-left:1.4pt solid #C9C9C9}
.ap[dir=rtl]{border-left:0;border-right:1.4pt solid #C9C9C9;padding:0 7px 0 0;text-align:right}
.deux{display:grid;grid-template-columns:1.35fr 1fr;gap:14px}
.cols{columns:3;column-gap:14px;font-size:8.8pt}
.lc{break-inside:avoid;border-bottom:.5pt solid #C9C9C9;padding:1.5px 0}
.lc .a,.lc .t{color:#3A3A3A;font-size:8.3pt}
table{border-collapse:collapse;width:100%}
td{border-bottom:.5pt solid #C9C9C9;padding:1.4px 4px 1.4px 0;vertical-align:top;font-size:8.6pt}
td.m{font-weight:800}
td.a{color:#3A3A3A}
td.t{color:#3A3A3A;font-size:8.6pt}
td.t[dir=rtl]{text-align:right}
.defi{border:1.4pt solid #000;padding:6px 9px;margin-top:8px;break-inside:avoid}
.defi p{margin:0;font-weight:700;font-size:10.4pt}
.cases{display:flex;gap:14px;margin-top:6px;font-size:8pt;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.case{width:12px;height:12px;border:1.1pt solid #000;display:inline-block;vertical-align:-2px;margin-right:4px}
.pied{margin-top:8px;border-top:.6pt solid #B8B8B8;padding-top:5px;font-size:7.8pt;color:#3A3A3A;display:flex;justify-content:space-between;gap:10px}
@media screen{body{background:#EDEDEA;padding:20px 0}.f{background:#FFF;padding:14mm;box-shadow:0 1px 3px rgba(0,0,0,.2)}}
""".replace("@@POLICE@@", POLICE)


def page(code, trad):
    L = trad.get(code) if code != "fr" else None
    d = f' dir="rtl" lang="{code}"' if L and L["rtl"] else (f' lang="{code}"' if L else "")
    manque = []

    def appui(texte_cle, defaut=None):
        if not L:
            return ""
        t = L.get("fiche", {}).get(texte_cle)
        if not t:
            manque.append(texte_cle)
            return ""
        return f'<div class="ap"{d}>{E(t)}</div>'

    phrases = "".join(
        f'<li><span class="n">{n}</span><div class="fr">{E(fr)}</div><div class="q">{E(q)}</div>'
        f'{appui("quand_" + i)}</li>' for n, (i, fr, q) in enumerate(PHRASES, 1))

    def rangee(e):
        t = L["mots"][e[0]]["mot"] if L else ""
        return (f'<tr><td class="m">{E(e[2])}</td><td class="a">{E(e[3])}</td>'
                + (f'<td class="t"{d}>{E(t)}</td>' if L else "") + "</tr>")
    pieges = "".join(rangee(e) for e in LEXIQUE if e[5].startswith("PIÈGE"))
    # Les couleurs en deux colonnes : en une seule, la fiche passait sur deux feuilles.
    def ligne_c(e):
        t = L["mots"][e[0]]["mot"] if L else ""
        return (f'<div class="lc"><b>{E(e[2])}</b>' + (f' <span class="a">({E(e[3])})</span>' if e[3] else "")
                + (f' <span class="t"{d}>{E(t)}</span>' if L else "") + "</div>")
    couleurs = "".join(ligne_c(e) for e in LEXIQUE if e[1] == "couleurs" and e[4] == "pastille")
    tailles = "".join(rangee(e) for e in LEXIQUE if e[0] in ("tp", "p", "m", "g", "tg", "pointure"))

    titre_langue = f'{E(L["loc"])} · appui' if L else "Français seulement"
    note = ("Les phrases se disent en français. La langue d'appui aide à comprendre quand s'en servir."
            if L else "Les phrases se disent en français.")
    if L and not L.get("relu"):
        note += " Traduction pas encore relue par une personne."
    if manque:
        note += " Certaines lignes attendent leur traduction."
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fiche de poche — Maison Francœur ({E(code)})</title><style>{CSS}</style></head>
<body><div class="f">
<div class="tete"><h1>Au plancher : les phrases du vendeur</h1><div class="ou">Maison Francœur<br>{titre_langue}</div></div>
<h2>Six phrases, dans l'ordre d'une vente</h2>
<ol class="p">{phrases}</ol>
<div class="deux">
  <div><h2>Les mots qui piègent</h2><table>{pieges}</table></div>
  <div><h2>Les tailles</h2><table>{tailles}</table>
       </div>
</div>
<h2>Les couleurs et les motifs</h2><div class="cols">{couleurs}</div>
<div class="defi"><p>{E(DEFI[0])}</p>{appui("defi")}
  <div class="cases"><span><i class="case"></i>Je l'ai fait</span><span><i class="case"></i>Vu par la gérante</span><span>Date : ____________</span></div></div>
<div class="pied"><span><b>francis</b> — formation au poste</span><span>{E(note)}</span></div>
</div></body></html>""", manque


def imprimer(html_path):
    pdf = html_path.with_suffix(".pdf")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", html_path.as_uri()], capture_output=True, timeout=120)
    brut = pdf.read_bytes()[:400000] if pdf.exists() else b""
    m = re.search(rb"/MediaBox\s*\[\s*0\s+0\s+([\d.]+)\s+([\d.]+)", brut)
    pages = len(re.findall(rb"/Type\s*/Page[^s]", brut))
    taille = (round(float(m.group(1))), round(float(m.group(2)))) if m else None
    return taille, pages


def main():
    trad = json.loads((CONTENU / "traductions.json").read_text(encoding="utf-8"))
    args = sys.argv[1:]
    codes = [a for a in args if not a.startswith("--")] or (["fr"] + list(trad))
    DEST.mkdir(parents=True, exist_ok=True)
    ecarts = 0
    for c in codes:
        texte, manque = page(c, trad)
        f = DEST / f"fiche-{c}.html"
        f.write_text(texte, encoding="utf-8")
        ligne = f"  {c:3} {len(manque)} ligne(s) sans traduction" if manque else f"  {c:3} complète"
        if "--sans-pdf" not in args:
            taille, pages = imprimer(f)
            ok = taille == LETTRE and pages == 1
            ecarts += not ok
            ligne += f" · PDF {taille} {pages} p. {'✓' if ok else '✗'}"
        print(ligne)
    sys.exit(1 if ecarts else 0)


if __name__ == "__main__":
    main()
