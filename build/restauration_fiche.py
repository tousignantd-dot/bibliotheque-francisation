#!/usr/bin/env python3
"""La fiche de poche de Chez Jocelyne — une par langue d'appui.

    python3 build/restauration_fiche.py              # fr, es, en + les 3 PDF
    python3 build/restauration_fiche.py es --sans-pdf

Une feuille lettre, recto seul, qui reste dans le tablier. Les règles de la fiche
de Francœur et de l'hôtel, reprises telles quelles :
  · aucune couleur — elle sort de la photocopieuse ;
  · la hiérarchie passe par la graisse et les filets ;
  · les phrases sont en FRANÇAIS ; la langue de l'employé, en petit, dessous.

Ce qui change : deux postes côte à côte (la cuisine, la salle), la règle d'allergie
au centre — c'est la seule erreur éliminatoire —, ce qu'on crie en cuisine, et les
mots d'ici qui piègent. Tout est LU ailleurs, rien n'est recopié : les gestes et
leurs phrases dans situations.py, la règle dans exercices.py, les pièges et les cris
dans le lexique, l'appui dans traductions.json (INTERFACE « gp_* », « fiche_* »).

Contrôle : chaque PDF doit faire UNE page lettre (612 × 792 pt), sinon code 1.
Sortie : assets/presentations/restauration/fiche/fiche-<langue>.html (+ .pdf)
"""
import html, importlib.util, json, pathlib, re, subprocess, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-restaurant"
DEST = RACINE / "assets" / "presentations" / "restauration" / "fiche"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
POLICE = "../../../design-system/fonts/nunito-latin.woff2"   # relatif : vaut aussi en file://
LETTRE = (612, 792)
E = html.escape


def _charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


LX = _charger("rf_lexique", CONTENU / "lexique.py")
EX = _charger("rf_exercices", CONTENU / "exercices.py")
SI = _charger("rf_situations", CONTENU / "situations.py")
ID = _charger("rf_identite", CONTENU / "identite.py")
sys.path.insert(0, str(RACINE / "build"))
from restaurant_traductions import INTERFACE  # noqa: E402
TRAD = json.loads((CONTENU / "traductions.json").read_text(encoding="utf-8"))
CRIS = ["chaud-derriere", "derriere", "ca-glisse"]

CSS = """
@page { size: letter; margin: 9mm 11mm 8mm; }
*{box-sizing:border-box}
@font-face{font-family:'Nunito';src:url('@@POLICE@@') format('woff2');font-weight:400 800}
html,body{margin:0;background:#FFF;color:#000}
body{font-family:'Nunito',-apple-system,'Segoe UI',sans-serif;font-size:9.4pt;line-height:1.28}
.f{max-width:190mm;margin:0 auto}
.tete{display:flex;align-items:flex-end;justify-content:space-between;gap:12px;border-bottom:2.2pt solid #000;padding-bottom:5px}
.tete h1{font-size:15pt;font-weight:800;margin:0;line-height:1.05}
.tete .ou{font-size:8pt;font-weight:700;text-transform:uppercase;letter-spacing:.11em;text-align:right}
h2{font-size:8pt;font-weight:800;text-transform:uppercase;letter-spacing:.11em;margin:8px 0 3px}
.deux{display:grid;grid-template-columns:1fr 1fr;gap:14px}
ol.p{list-style:none;margin:0;padding:0}
ol.p li{border-bottom:.6pt solid #B8B8B8;padding:3px 0;break-inside:avoid}
ol.p li:first-child{border-top:.6pt solid #B8B8B8}
ol.p .q{font-size:7.8pt;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:#3A3A3A}
ol.p .dit{font-size:10.4pt;font-weight:800;line-height:1.2}
.ap[dir=rtl]{border-left:0;border-right:1.4pt solid #C9C9C9;padding-left:0;padding-right:7px;text-align:right}
.ap{font-size:8pt;line-height:1.22;color:#3A3A3A;margin-top:1px;padding-left:7px;border-left:1.4pt solid #C9C9C9}
.regle{border:1.6pt solid #000;padding:6px 10px;margin-top:9px;break-inside:avoid}
.regle ol{margin:3px 0 0;padding-left:18px}
.regle li{font-weight:800;font-size:10pt;margin:2px 0}
.regle .grave{font-weight:800;margin-top:4px;font-size:9pt}
table{border-collapse:collapse;width:100%}
td{border-bottom:.5pt solid #C9C9C9;padding:1.2px 4px 1.2px 0;vertical-align:top;font-size:7.9pt}
td.m{font-weight:800}
td.a{color:#3A3A3A}
.cris{display:flex;flex-wrap:wrap;gap:4px 16px}
.cris span{font-weight:800;font-size:10pt}
.cris small{display:block;font-weight:600;font-size:8pt;color:#3A3A3A}
.defi{border:1.4pt solid #000;padding:6px 9px;margin-top:9px;break-inside:avoid}
.defi p{margin:0;font-weight:700;font-size:9.6pt}
.cases{display:flex;gap:14px;margin-top:6px;font-size:8pt;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.case{width:12px;height:12px;border:1.1pt solid #000;display:inline-block;vertical-align:-2px;margin-right:4px}
.pied{margin-top:8px;border-top:.6pt solid #B8B8B8;padding-top:5px;font-size:7.6pt;color:#3A3A3A;display:flex;justify-content:space-between;gap:10px}
@media screen{body{background:#EDEDEA;padding:20px 0}.f{background:#FFF;padding:14mm;box-shadow:0 1px 3px rgba(0,0,0,.2)}}
""".replace("@@POLICE@@", POLICE)


def page(L):
    ui = TRAD.get(L, {}).get("interface", {}) if L != "fr" else {}
    mots = TRAD.get(L, {}).get("mots", {}) if L != "fr" else {}
    fr = lambda k: INTERFACE[k]
    rtl = TRAD.get(L, {}).get("rtl", False)
    d = ' dir="rtl"' if rtl else ""
    ap = lambda k: (f'<div class="ap" lang="{L}"{d}>{E(ui[k])}</div>' if ui.get(k) else "")
    ap_txt = lambda k: E(ui.get(k, "")) if ui.get(k) else ""

    def gestes(porte):
        ids = [g["id"] for g in SI.GESTES if g["porte"] in (porte, "deux") and g["id"] != "allergie"]
        return "".join(f'<li><div class="q">{E(fr("g_" + i))}</div><div class="dit" lang="fr">{E(fr("gp_" + i))}</div>{ap("gp_" + i)}</li>'
                       for i in ids)
    regle = "".join(f'<li>{E(fr(f"regle_{n}"))}{ap(f"regle_{n}")}</li>' for n in (1, 2, 3))
    lex = {e[0]: e for e in LX.LEXIQUE}
    cris = "".join(f'<span lang="fr">{E(lex[i][2])}<small lang="{L}"{d}>{E(mots[i]["mot"]) if i in mots else ""}</small></span>' for i in CRIS)
    pieges = [e for e in LX.LEXIQUE if e[5].startswith("PIÈGE")]
    # Deux colonnes : en une seule, la version avec appui débordait sur une 2e page.
    ligne = lambda e: (f'<tr><td class="m" lang="fr">{E(e[2])}</td><td class="a">{E(e[3])}</td>'
                       f'<td class="a" lang="{L}"{d}>{E(mots[e[0]]["mot"]) if e[0] in mots else ""}</td></tr>')
    moitie = (len(pieges) + 1) // 2
    lignes = (f'<div class="deux"><table>{"".join(ligne(e) for e in pieges[:moitie])}</table>'
              f'<table>{"".join(ligne(e) for e in pieges[moitie:])}</table></div>')
    note = (fr("fiche_note") + " " + fr("fiche_non_relu")) if L != "fr" else fr("fiche_hygiene")
    loc = TRAD.get(L, {}).get("loc", "Français seulement") if L != "fr" else "Français seulement"
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fiche de poche — {E(ID.NOM)} ({E(loc)})</title><style>{CSS}</style></head>
<body><div class="f">
<div class="tete"><h1>{E(fr("fiche_titre"))}{(' <small style="font-size:9pt;font-weight:600">· ' + ap_txt("fiche_titre") + '</small>') if ui.get("fiche_titre") else ''}</h1><div class="ou">{E(ID.NOM)}<br>{E(loc)}</div></div>
<div class="deux">
  <div><h2>{E(fr("fiche_cuisine"))}</h2><ol class="p">{gestes("cuisine")}</ol></div>
  <div><h2>{E(fr("fiche_salle"))}</h2><ol class="p">{gestes("salle")}</ol></div>
</div>
<div class="regle"><h2 style="margin-top:0">{E(fr("fiche_regle"))}</h2><ol>{regle}</ol>
  <div class="grave">{E(EX.CRITERE_GRAVE)}</div>{ap("critere_grave")}</div>
<h2>{E(fr("fiche_cris"))}</h2><div class="cris">{cris}</div>
<h2>{E(fr("fiche_pieges"))}</h2>{lignes}
<div class="defi"><p>{E(fr("fiche_defi"))}</p>{ap("fiche_defi")}
  <div class="cases"><span><i class="case"></i>{E(fr("fiche_fait"))}</span><span><i class="case"></i>{E(fr("fiche_vu"))}</span><span>{E(fr("fiche_date"))} : ____________</span></div></div>
<div class="pied"><span><b>francis — formation en milieu de travail</b></span><span>{E(note)}</span></div>
</div></body></html>"""


def imprimer(html_path):
    pdf = html_path.with_suffix(".pdf")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", html_path.as_uri()], capture_output=True, timeout=120)
    brut = pdf.read_bytes()[:400000] if pdf.exists() else b""
    m = re.search(rb"/MediaBox\s*\[\s*0\s+0\s+([\d.]+)\s+([\d.]+)", brut)
    pages = len(re.findall(rb"/Type\s*/Page[^s]", brut))
    return ((round(float(m.group(1))), round(float(m.group(2)))) if m else None), pages


def main():
    args = sys.argv[1:]
    # Seulement les langues TRADUITES : sinon une fiche « ukrainien » sortait en français seul.
    voulues = [a for a in args if not a.startswith("--")] or ["fr"] + [l for l in ID.LANGUES_APPUI if l in TRAD]
    DEST.mkdir(parents=True, exist_ok=True)
    ecarts = 0
    for L in voulues:
        f = DEST / f"fiche-{L}.html"
        f.write_text(page(L), encoding="utf-8")
        ligne = f"  {L}"
        if "--sans-pdf" not in args:
            taille, pages = imprimer(f)
            ok = taille == LETTRE and pages == 1
            ecarts += not ok
            ligne += f" · PDF {taille} {pages} p. {'✓' if ok else '✗'}"
        print(ligne)
    sys.exit(1 if ecarts else 0)


if __name__ == "__main__":
    main()
