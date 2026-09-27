#!/usr/bin/env python3
"""La fiche de poche de la réception de l'Hôtel Rive-Claire — une par direction.

    python3 build/hotel_fiche.py              # les 6 pages + les 6 PDF
    python3 build/hotel_fiche.py es-fr --sans-pdf

Une feuille lettre, recto seul, qui reste sous le comptoir. Les règles de la
fiche de Francœur (build/francoeur_fiche.py), reprises telles quelles :
  · aucune couleur — elle sort de la photocopieuse ;
  · la hiérarchie passe par la graisse et les filets ;
  · les phrases sont dans la langue APPRISE ; la langue de l'employé, en petit, dessous.

Ce qui change : trois langues, donc six directions (fiche-<parle>-<apprend>) ; et
l'alphabet de la langue apprise, parce qu'on épelle au téléphone (O2).

Contrôle : chaque PDF doit faire UNE page lettre (612 × 792 pt), sinon code 1.
Sortie : assets/presentations/hotellerie-fiche/fiche-<parle>-<apprend>.html (+ .pdf)
"""
import html, importlib.util, pathlib, re, subprocess, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-hotel"
DEST = RACINE / "assets" / "presentations" / "hotellerie-fiche"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
POLICE = "../../design-system/fonts/nunito-latin.woff2"   # relatif : vaut aussi en file://
LETTRE = (612, 792)
LANGUES = ("fr", "en", "es")
E = html.escape


def _charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


EX = _charger("hf_exercices", CONTENU / "exercices.py")
CL = _charger("hf_clients", CONTENU / "clients.py")
FI = _charger("hf_fiche", CONTENU / "fiche.py")
HP = _charger("hf_planches", RACINE / "build" / "hotel_planches.py")
PAIRE_ORDRE = {"en·fr": "fr·en", "es·fr": "fr·es", "en·es": "es·en"}

CSS = """
@page { size: letter; margin: 9mm 11mm 8mm; }
*{box-sizing:border-box}
@font-face{font-family:'Nunito';src:url('@@POLICE@@') format('woff2');font-weight:400 800}
html,body{margin:0;background:#FFF;color:#000}
body{font-family:'Nunito',-apple-system,'Segoe UI',sans-serif;font-size:9.6pt;line-height:1.3}
.f{max-width:190mm;margin:0 auto}
.tete{display:flex;align-items:flex-end;justify-content:space-between;gap:12px;border-bottom:2.2pt solid #000;padding-bottom:5px}
.tete h1{font-size:15pt;font-weight:800;margin:0;line-height:1.05}
.tete .ou{font-size:8pt;font-weight:700;text-transform:uppercase;letter-spacing:.11em;text-align:right}
h2{font-size:8pt;font-weight:800;text-transform:uppercase;letter-spacing:.11em;margin:8px 0 3px}
ol.p{list-style:none;margin:0;padding:0}
ol.p li{border-bottom:.6pt solid #B8B8B8;padding:3px 0 3px 22px;position:relative;break-inside:avoid}
ol.p li:first-child{border-top:.6pt solid #B8B8B8}
ol.p .n{position:absolute;left:0;top:5px;font-size:11.5pt;font-weight:800}
ol.p .dit{font-size:11pt;font-weight:800;line-height:1.2}
ol.p .q{font-size:8.2pt;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:#3A3A3A}
.ap{font-size:8.2pt;line-height:1.25;color:#3A3A3A;margin-top:1px;padding-left:7px;border-left:1.4pt solid #C9C9C9}
.regle{border:1.4pt solid #000;padding:5px 9px;margin-top:7px;break-inside:avoid;font-size:8.8pt}
.regle b{display:block;font-size:9.6pt}
.deux{display:grid;grid-template-columns:1.25fr 1fr;gap:14px}
table{border-collapse:collapse;width:100%}
td{border-bottom:.5pt solid #C9C9C9;padding:1.4px 4px 1.4px 0;vertical-align:top;font-size:8.4pt}
td.m{font-weight:800}
td.a{color:#3A3A3A}
td.n{color:#3A3A3A;font-size:7.8pt}
.abc{display:grid;grid-template-columns:repeat(4,1fr);gap:0 8px;font-size:8.4pt}
.abc span{border-bottom:.5pt solid #C9C9C9;padding:1px 0}
.abc b{display:inline-block;width:14px}
.sig{font-size:8.2pt;margin-top:4px;color:#3A3A3A}
.defi{border:1.4pt solid #000;padding:6px 9px;margin-top:8px;break-inside:avoid}
.defi p{margin:0;font-weight:700;font-size:10pt}
.cases{display:flex;gap:14px;margin-top:6px;font-size:8pt;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.case{width:12px;height:12px;border:1.1pt solid #000;display:inline-block;vertical-align:-2px;margin-right:4px}
.pied{margin-top:8px;border-top:.6pt solid #B8B8B8;padding-top:5px;font-size:7.8pt;color:#3A3A3A;display:flex;justify-content:space-between;gap:10px}
@media screen{body{background:#EDEDEA;padding:20px 0}.f{background:#FFF;padding:14mm;box-shadow:0 1px 3px rgba(0,0,0,.2)}}
""".replace("@@POLICE@@", POLICE)


def page(P, A, mots):
    U = lambda k: FI.UI[k][P]
    langue_a = FI.UI["langues"][A][P]
    phrases = "".join(
        f'<li><span class="n">{n}</span><div class="q">{E(g["nom"][P])}</div>'
        f'<div class="dit" lang="{A}">{E(g["phrase"][A])}</div><div class="ap" lang="{P}">{E(g["phrase"][P])}</div></li>'
        for n, g in enumerate(CL.GESTES, 1))
    paire = PAIRE_ORDRE.get("·".join(sorted((P, A))), "·".join(sorted((P, A))))
    nettoie = lambda t: re.sub(r"^(PIÈGE|TRAP|TRAMPA)\s*(\([^)]*\))?\s*:\s*", "", t or "")
    pieges = [m for m in mots if m["paire"] == paire]
    lignes = "".join(f'<tr><td class="m" lang="{A}">{E(m[A])}</td><td class="a">{E(m[P])}</td></tr>'
                     f'<tr><td colspan="2" class="n">{E(nettoie(m["notes"].get(P, "")))}</td></tr>' for m in pieges)
    noms = FI.NOMS_LETTRES_EN if A == "en" else EX.LETTRES[A]
    abc = "".join(f'<span><b>{l}</b> {E(noms[l])}</span>' for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    sig = EX.SIGNES[A]
    signes = " · ".join(E(sig[k].replace("{l}", "L")) for k in ("accent_aigu", "trait", "espace", "double")
                        if k in sig)
    ancres = " · ".join(f"{l} = « {E(v)} »" for l, v in EX.ANCRES.get(A, {}).items())
    note = U("note").format(l=langue_a)
    if "en" in (P, A) or "es" in (P, A):
        note += " " + U("non_relu")
    return f"""<!doctype html>
<html lang="{P}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fiche de poche — Hôtel Rive-Claire ({P} → {A})</title><style>{CSS}</style></head>
<body><div class="f">
<div class="tete"><h1>{E(U("titre"))}</h1><div class="ou">Hôtel Rive-Claire<br>{E(U("apprend").format(l=langue_a))}</div></div>
<h2>{E(U("six"))}</h2>
<ol class="p">{phrases}</ol>
<div class="regle"><b>{E(U("regle"))} — {E(U("eliminatoire"))}</b>{E(EX.REGLE_RELAIS[P])}</div>
<div class="deux">
  <div><h2>{E(U("pieges"))}</h2><table>{lignes}</table></div>
  <div><h2>{E(U("alphabet"))}</h2><div class="abc" lang="{A}">{abc}</div>
    <p class="sig" lang="{A}"><b>{E(U("signes"))} :</b> {signes}{(" · " + ancres) if ancres else ""}</p></div>
</div>
<div class="defi"><p>{E(U("defi"))}</p>
  <div class="cases"><span><i class="case"></i>{E(U("fait"))}</span><span><i class="case"></i>{E(U("vu"))}</span><span>{E(U("date"))} : ____________</span></div></div>
<div class="pied"><span><b>{E(U("pied"))}</b></span><span>{E(note)}</span></div>
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
    voulues = [a for a in args if not a.startswith("--")]
    directions = [(p, a) for p in LANGUES for a in LANGUES if p != a and (not voulues or f"{p}-{a}" in voulues)]
    mots = HP.donnees()["mots"]
    DEST.mkdir(parents=True, exist_ok=True)
    ecarts = 0
    for p, a in directions:
        f = DEST / f"fiche-{p}-{a}.html"
        f.write_text(page(p, a, mots), encoding="utf-8")
        ligne = f"  {p} → {a}"
        if "--sans-pdf" not in args:
            taille, pages = imprimer(f)
            ok = taille == LETTRE and pages == 1
            ecarts += not ok
            ligne += f" · PDF {taille} {pages} p. {'✓' if ok else '✗'}"
        print(ligne)
    sys.exit(1 if ecarts else 0)


if __name__ == "__main__":
    main()
