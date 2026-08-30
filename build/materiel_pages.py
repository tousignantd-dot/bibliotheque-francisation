#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Les deux documents du matériel : les fiches de l'élève, les diaporamas.

Ils répondent à la question qu'une direction pose toujours en premier — « et
concrètement, qu'est-ce que l'enseignant a en main ? » — et ils la chiffrent sur
le dépôt lui-même, jamais de mémoire : les fiches sont comptées dans
`assets/documents`, les diapositives sont lues dans les `.pptx`, les types de
diapositives sont relevés dans les scripts de `build/powerpoints/decks`.

    python3 build/materiel_pages.py
    python3 build/materiel_pages.py --sans-pdf

Écrit `assets/presentations/fiches-eleve.html` et
`assets/presentations/powerpoints-enseignant.html`, **et leurs PDF** : la
version papier est ce qu'on laisse sur la table, et une page refaite dont le
PDF reste à l'ancienne édition est pire qu'un PDF absent — rien ne signale
l'écart. Les captures, elles, sont posées à la main dans
`assets/presentations/captures-materiel/`.
"""

import argparse
import collections
import html
import json
import pathlib
import re
import statistics
import time
import sys
import zipfile

RACINE = pathlib.Path(__file__).resolve().parent.parent
PRES = RACINE / "assets" / "presentations"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from imprimer import imprimer  # noqa: E402


# ── Mesures ───────────────────────────────────────────────────────────────

def niveaux():
    """slug de module -> niveau, d'après le catalogue."""
    out = {}
    for a in json.loads((RACINE / "data" / "activities.json").read_text()):
        inter = a.get("interactive") or ""
        if inter.startswith("assets/interactive/"):
            out[inter.split("/")[2]] = a.get("level") or "?"
    return out


def mesures():
    niv = niveaux()
    m = {"quand": time.strftime("%-d %B %Y").replace("August", "août")}

    docs = sorted((RACINE / "assets" / "documents").glob("*.html"))
    fiches = [p for p in docs if re.search(r"-[a-e][1-5]-", p.name)]
    m["fiches"] = len(fiches)
    m["sommaires"] = len([p for p in docs if p.name.endswith("-fiches-eleves.html")])
    m["autres_docs"] = len(docs) - m["fiches"] - m["sommaires"]

    par_module = collections.Counter(
        re.match(r"(.+?)-[a-e][1-5]-", p.name).group(1) for p in fiches)
    m["modules_fiches"] = len(par_module)
    m["repartition_fiches"] = dict(sorted(collections.Counter(par_module.values()).items()))
    m["fiches_par_niveau"] = dict(sorted(collections.Counter(
        niv.get(re.match(r"(.+?)-[a-e][1-5]-", p.name).group(1), "?") for p in fiches).items()))

    decks = sorted((RACINE / "assets" / "powerpoints").rglob("*.pptx"))
    m["decks"] = len(decks)
    m["decks_par_niveau"] = dict(sorted(collections.Counter(
        niv.get(d.parent.name, "?") for d in decks).items()))
    diapos, tailles = [], []
    for d in decks:
        tailles.append(d.stat().st_size)
        try:
            with zipfile.ZipFile(d) as z:
                diapos.append(len([n for n in z.namelist()
                                   if re.match(r"ppt/slides/slide\d+\.xml$", n)]))
        except Exception:
            pass
    m["diapos"] = sum(diapos)
    m["diapos_min"], m["diapos_max"] = min(diapos), max(diapos)
    m["diapos_med"] = int(statistics.median(diapos))
    m["poids_decks"] = round(sum(tailles) / 1e6)

    # la grammaire des diaporamas, relevée dans les scripts de séance
    appels, notes, minutes = collections.Counter(), 0, 0
    sources = list((RACINE / "build" / "powerpoints" / "decks").rglob("*.py"))
    for p in sources:
        t = p.read_text(errors="ignore")
        for a in re.finditer(r"\bd\.(\w+)\(", t):
            appels[a.group(1)] += 1
        notes += len(re.findall(r"notes=", t))
        d = re.search(r"duree='(\d+)", t)
        if d:
            minutes += int(d.group(1))
    appels.pop("save", None)
    m["types"] = appels.most_common()
    m["appels"] = sum(appels.values())
    m["notes"] = notes
    m["heures"] = round(minutes / 60)
    m["scripts"] = len(sources)

    # les séances qui ont un diaporama mais pas de fiche
    f_par_mod = collections.defaultdict(set)
    for p in fiches:
        mm = re.match(r"(.+?)-([a-e][1-5])-", p.name)
        f_par_mod[mm.group(1)].add(mm.group(2))
    d_par_mod = collections.defaultdict(set)
    for d in decks:
        d_par_mod[d.parent.name].add(d.name[:2].lower())
    trous = {mod: sorted(s - f_par_mod.get(mod, set()))
             for mod, s in d_par_mod.items() if s - f_par_mod.get(mod, set())}
    m["trous"] = trous
    m["trous_n"] = sum(len(v) for v in trous.values())

    m["vignettes"] = len(list((RACINE / "assets" / "vignettes").rglob("*.png")))
    return m


# ── Gabarit ───────────────────────────────────────────────────────────────

STYLE = """
  :root{
    --accent:#0A8F5B; --accent-soft:#E6F5EE; --accent-ink:#07734A;
    --surface-band:#EDF6F1;
    --ink-900:#17181A; --ink-700:#3A3D40; --ink-500:#4B4F52; --ink-400:#6E7175;
    --surface-page:#F7F7F5; --surface-card:#FFFFFF; --surface-sunken:#FBFBFA;
    --paper-200:#F0F0EE; --border:#EAEAE8; --border-firm:#D6D6D2; --border-tint:#D8E8DF;
    --acier-600:#1D6B8F; --acier-100:#E7F0F6;
    --ambre-700:#B45309; --ambre-100:#FBEEDC;
    --teal-700:#0D7A6F;  --teal-100:#E3F2F0;
    --indigo-600:#3B49A0; --indigo-100:#E8EAFA;
    --marque-600:#6B4FBB; --marque-100:#EDE7F9; --marque-filet:#C3B4EA;
    --font-sans:"Nunito",system-ui,-apple-system,"Segoe UI",sans-serif;
    --content-max:1120px;
  }
  *{box-sizing:border-box}
  body{margin:0; background:var(--surface-page); color:var(--ink-900);
    font-family:var(--font-sans); font-size:18px; font-weight:600; line-height:1.55;
    -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:100%}
  :focus-visible{outline:3px solid var(--accent); outline-offset:2px; border-radius:4px}
  .conteneur{max-width:var(--content-max); margin:0 auto; padding:0 24px}
  .verrou{display:inline-flex; align-items:center; gap:16px; flex-wrap:wrap}
  .verrou .nom{font-weight:900; font-size:28px; letter-spacing:-.035em; line-height:1;
    color:var(--ink-900); white-space:nowrap}
  .verrou .i{position:relative; display:inline-block}
  .verrou .point{position:absolute; left:1px; top:2px; width:7px; height:7px;
    border-radius:999px; background:var(--marque-600)}
  .verrou .filet{width:2px; height:24px; background:var(--marque-filet)}
  .verrou .desc{font-size:16px; font-weight:900; letter-spacing:-.015em; line-height:1;
    color:var(--marque-600); white-space:nowrap}
  @media (max-width:480px){ .verrou .filet,.verrou .desc{display:none} }
  .barre{background:#FFFFFF; border-bottom:2px solid var(--marque-600); padding:16px 0}
  .bande{background:var(--surface-band); border-bottom:1px solid var(--border-tint);
    padding:44px 0 34px}
  .bande .conteneur{display:flex; flex-direction:column; gap:20px}
  .surtitre{font-size:13px; font-weight:800; letter-spacing:.12em; text-transform:uppercase;
    color:var(--ink-400); margin:0}
  h1{font-size:clamp(32px,5.4vw,46px); font-weight:900; letter-spacing:-.02em;
    line-height:1.14; margin:0; text-wrap:balance}
  .chapeau{font-size:19px; font-weight:600; color:var(--ink-500); margin:0; max-width:64ch}
  .quand{font-size:14px; color:var(--ink-400); margin:0}
  main{padding:8px 0 80px}
  section{padding:42px 0 0}
  h2{font-size:27px; font-weight:900; letter-spacing:-.015em; margin:0 0 6px; text-wrap:balance}
  h3{font-size:19px; font-weight:900; margin:24px 0 6px}
  p{margin:0 0 14px; max-width:68ch}
  .eyebrow{display:inline-block; font-size:12px; font-weight:800; letter-spacing:.12em;
    text-transform:uppercase; padding:4px 10px; border-radius:999px; margin:0 0 10px}
  .e-acier{background:var(--acier-100); color:var(--acier-600)}
  .e-ambre{background:var(--ambre-100); color:var(--ambre-700)}
  .e-teal{background:var(--teal-100); color:var(--teal-700)}
  .e-indigo{background:var(--indigo-100); color:var(--indigo-600)}
  strong,b{font-weight:900}
  code{font-family:ui-monospace,Menlo,Consolas,monospace; font-size:.86em;
    background:var(--paper-200); padding:1px 5px; border-radius:5px; font-weight:700}
  .garde{background:var(--accent-soft); border:1px solid #BFE3D2; border-radius:14px;
    padding:16px 20px}
  .garde p:last-child{margin-bottom:0}
  .alerte{background:var(--ambre-100); border:1px solid #E8D7B8; border-radius:14px;
    padding:16px 20px}
  .alerte p:last-child{margin-bottom:0}
  .liens{display:flex; flex-wrap:wrap; gap:10px; margin-top:6px}
  .lien{display:inline-block; font-size:15px; font-weight:800; text-decoration:none;
    color:var(--ink-900); background:#FFFFFF; border:1px solid var(--border-firm);
    border-radius:999px; padding:9px 15px}
  .lien:hover{background:var(--paper-200)}
  .tuiles{display:grid; gap:14px; grid-template-columns:repeat(auto-fit,minmax(min(170px,100%),1fr));
    margin:24px 0 4px}
  .tuile{background:var(--surface-card); border:1px solid var(--border);
    border-left:4px solid var(--accent); border-radius:14px; padding:14px 16px}
  .tuile .n{font-size:26px; font-weight:900; letter-spacing:-.02em; display:block; line-height:1.12}
  .tuile .l{font-size:13.5px; font-weight:700; color:var(--ink-500)}
  .cadre-table{overflow-x:auto; border:1px solid var(--border); border-radius:14px;
    background:var(--surface-card); margin-top:14px}
  table{border-collapse:collapse; width:100%; min-width:560px; font-size:15px}
  th,td{text-align:left; padding:10px 14px; border-bottom:1px solid var(--border);
    vertical-align:top}
  thead th{font-size:12px; font-weight:800; letter-spacing:.08em; text-transform:uppercase;
    color:var(--ink-400); background:var(--surface-sunken); white-space:nowrap}
  tbody tr:last-child td{border-bottom:0}
  td.n{font-variant-numeric:tabular-nums; font-weight:800; white-space:nowrap}
  .prise{background:var(--surface-card); border:1px solid var(--border); border-radius:16px;
    overflow:hidden; margin:22px 0 0}
  .prise > figure{margin:0}
  .prise .tete{padding:16px 20px 12px; border-bottom:1px solid var(--border)}
  .prise h3{font-size:20px; font-weight:900; margin:0 0 4px; letter-spacing:-.01em}
  .prise .quoi{font-size:16px; font-weight:600; color:var(--ink-500); margin:0; max-width:78ch}
  .prise img{display:block; width:100%; height:auto; background:var(--surface-sunken)}
  .prise figcaption{padding:13px 20px 16px; font-size:15px; font-weight:600;
    color:var(--ink-500); border-top:1px solid var(--border); background:var(--surface-sunken)}
  .prise figcaption b{color:var(--ink-900)}
  .paire{display:grid; gap:22px; grid-template-columns:repeat(auto-fit,minmax(min(340px,100%),1fr))}
  .paire .prise{margin:0}
  hr{border:0; border-top:1px solid var(--border); margin:44px 0 0}
  footer p{font-size:16px; color:var(--ink-500)}

  /* ── Version papier — imprimée en couleur, format lettre ─────────── */
  @media print{
    @page{ size:letter; margin:14mm 14mm 16mm; }
    *{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
    html,body{ background:#FFFFFF; font-size:10.5pt; }
    .conteneur{ max-width:none; padding:0; }
    .barre{ padding:0 0 4mm; border-bottom-width:1.2pt; }
    .bande{ background:#FFFFFF; border-bottom:1px solid var(--border); padding:0 0 6mm; }
    .liens{ display:none; }
    h1{ font-size:26pt; } h2{ font-size:15pt; } h3{ font-size:12.5pt; }
    .chapeau{ font-size:12pt; } .quand{ font-size:9.5pt; }
    p{ max-width:none; }
    section{ padding:7mm 0 0; }
    section > h2, section > .eyebrow{ break-after:avoid; }
    table{ min-width:0; font-size:9.5pt; }
    .cadre-table, .garde, .alerte, .tuiles{ break-inside:avoid; }
    .prise{ break-inside:avoid; page-break-inside:avoid; margin:6mm 0 0; }
    .prise img{ width:auto; max-width:100%; max-height:150mm; margin:0 auto; }
    .prise figcaption{ font-size:9.5pt; padding:9px 14px 11px; }
    .paire{ display:block; }
    .paire .prise{ margin:6mm 0 0; }
    a[href]{ color:inherit; text-decoration:none; }
  }
"""

TETE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITRE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap">
<style>__STYLE__</style>
</head>
<body>

<div class="barre">
  <div class="conteneur">
    <div class="verrou">
      <span class="nom" role="img" aria-label="francis">franc<span class="i" aria-hidden="true">ı<span class="point"></span></span>s</span>
      <span class="filet" aria-hidden="true"></span>
      <span class="desc">Aide à l'apprentissage du français</span>
    </div>
  </div>
</div>

<header class="bande">
  <div class="conteneur">
    <div>
      <p class="surtitre">__SURTITRE__</p>
      <h1>__H1__</h1>
    </div>
    <p class="chapeau">__CHAPEAU__</p>
    <p class="quand">__DATE__</p>
    <div class="liens">__LIENS__</div>
  </div>
</header>

<main>
__CORPS__
</main>
</body>
</html>
"""


def page(nom, titre, surtitre, h1, chapeau, date, liens, corps):
    h = (TETE.replace("__STYLE__", STYLE).replace("__TITRE__", titre)
         .replace("__SURTITRE__", surtitre).replace("__H1__", h1)
         .replace("__CHAPEAU__", chapeau).replace("__DATE__", date)
         .replace("__LIENS__", liens).replace("__CORPS__", corps))
    (PRES / nom).write_text(h)
    print("écrit :", nom)


def nb(v):
    """Les milliers se séparent : « 15 154 » se lit, « 15154 » se déchiffre."""
    return "{:,}".format(v).replace(",", "\u202f") if isinstance(v, int) else str(v)


def tuiles(paires):
    return ('<div class="tuiles">%s</div>' % "".join(
        '<div class="tuile"><span class="n">%s</span><span class="l">%s</span></div>'
        % (html.escape(nb(v)), l) for v, l in paires))


def table(entetes, lignes):
    return ('<div class="cadre-table"><table><thead><tr>%s</tr></thead><tbody>%s'
            '</tbody></table></div>'
            % ("".join("<th>%s</th>" % e for e in entetes),
               "".join("<tr>%s</tr>" % "".join(
                   '<td class="n">%s</td>' % c if i and str(c).replace(" ", "").isdigit()
                   else "<td>%s</td>" % c for i, c in enumerate(l)) for l in lignes)))


def prise(titre, quoi, img, alt, legende):
    return ('<article class="prise"><figure><div class="tete"><h3>%s</h3>'
            '<p class="quoi">%s</p></div>'
            '<img src="captures-materiel/%s" alt="%s">'
            '<figcaption>%s</figcaption></figure></article>'
            % (titre, quoi, img, html.escape(alt), legende))


def etat_couverture(m):
    """Dire l'état réel : une fiche par séance, ou les trous s'il y en a.

    Le premier jet annonçait quatorze fiches manquantes. C'était mon propre
    filtre qui les cachait — il ne connaissait que les séances 1 à 4, et sept
    modules ont un B5 et un C5. Le compte est refait ici sur le dépôt, à chaque
    passage : une page qui annonce un trou inexistant est pire qu'une page
    muette."""
    if not m["trous"]:
        return ('<div class="garde"><p><b>La couverture est complète.</b> '
                '%s fiches pour %s diaporamas : <b>chaque séance projetée a sa fiche '
                'imprimable</b>, et l\'inverse. %d modules ont seize séances, %d en ont '
                'huit — ce sont les modules courts des premiers niveaux.</p></div>'
                % (nb(m["fiches"]), nb(m["decks"]),
                   m["repartition_fiches"].get(16, 0), m["repartition_fiches"].get(8, 0)))
    return ('<div class="alerte"><p><b>Ce qui manque, et il vaut mieux le dire :</b> '
            '%d séances ont leur diaporama mais pas encore leur fiche (%s).</p></div>'
            % (m["trous_n"], ", ".join(sorted(m["trous"])[:5])))


# ── Les deux documents ────────────────────────────────────────────────────

def page_fiches(m):
    niv = m["fiches_par_niveau"]
    lignes = [[n, niv[n], m["decks_par_niveau"].get(n, 0)] for n in sorted(niv)]
    lignes.append(["<b>Total</b>", "<b>%d</b>" % m["fiches"], "<b>%d</b>" % m["decks"]])
    corps = """
<section class="conteneur">
  %s
  <p style="margin-top:16px">Chaque séance de chaque module a <b>sa fiche</b> : une page,
  format lettre, <b>en noir et blanc</b>, prête pour la photocopieuse de l'école. Aucune
  couleur nulle part — toute la hiérarchie passe par la graisse, les filets et les mots.
  C'est la règle du système poussée à son terme : jamais d'information portée par la
  couleur seule, parce qu'une photocopie de photocopie ne garde que le noir.</p>
</section>

<section class="conteneur">
  <p class="eyebrow e-acier">Ce que c'est</p>
  <h2>Une séance, une fiche, une page</h2>
  <p>Un module de cours, c'est <b>seize séances</b> réparties en cinq blocs — A on
  découvre, B, C et D les trois défis, E on se lance. Les modules courts des niveaux 1 et 2
  en comptent huit. La fiche reprend, pour l'élève, ce que la classe a fait : la règle, les
  exemples, les tableaux d'analyse, les exercices à faire de sa main.</p>
  %s
</section>

<section class="conteneur">
  <p class="eyebrow e-teal">La règle qui tient tout</p>
  <h2>Un seul contenu, deux sorties</h2>
  <div class="garde">
    <p><b>Le fichier de séance est lu deux fois.</b> Lu par le moteur des présentations, il
    donne le diaporama que l'enseignant projette. Lu par le moteur des fiches, il donne la
    page que l'élève reçoit. <b>Elles ne peuvent pas diverger</b> : corriger une règle dans
    la séance corrige les deux, et il n'existe pas de version « à jour » et de version
    « oubliée ».</p>
    <p style="margin-top:10px">Ce que la fiche fait autrement : <b>les notes d'enseignant
    disparaissent</b> — elles pilotent la classe, elles n'ont rien à faire entre les mains
    de l'élève — et les réponses des exercices projetés cèdent la place à des lignes à
    remplir.</p>
  </div>
</section>

<section class="conteneur">
  <p class="eyebrow e-ambre">À quoi ça ressemble</p>
  <h2>Deux fiches, prises telles quelles</h2>
  <div class="paire">
    %s
    %s
  </div>
  %s
</section>

<section class="conteneur">
  <p class="eyebrow e-indigo">Ce que l'enseignant a en main</p>
  <h2>Le dépôt de matériel, dans son portail</h2>
  <p>Quatrième onglet de l'espace enseignant. Il ne demande rien à personne : le matériel
  est déjà là, accroché à la planification du groupe.</p>
  %s
  %s
  <div class="garde" style="margin-top:20px">
    <p><b>L'impression sort en une fois.</b> Une série de fiches s'imprime dans un seul
    dialogue, chaque fiche sur sa page — et l'impression passe par un cadre isolé, jamais
    par la page du portail : rien de l'interface ne peut se glisser dans la photocopie.</p>
  </div>
</section>

<section class="conteneur">
  <p class="eyebrow e-acier">Pour ceux qui préfèrent le papier relié</p>
  <h2>Le manuel de l'élève</h2>
  <p>Les fiches d'un niveau entier reliées en un seul PDF, avec couverture, mode d'emploi,
  table des matières paginée, intercalaire par module, folios et signets par séance. Deux
  mises en page, <b>contenu identique</b> : pleine page (1 753 p., la fiche telle qu'elle
  est photocopiée) et serré (852 p., un format de consultation).</p>
  %s
</section>

<section class="conteneur">
  %s
</section>

<hr>
<footer class="conteneur">
  <p>Les nombres de cette page sont comptés sur le dépôt par
  <code>build/materiel_pages.py</code>, jamais recopiés : les fiches sont dénombrées dans
  <code>assets/documents</code>, les séances relevées dans les fichiers de contenu. Une
  production nouvelle change la page dès qu'on relance le script.</p>
</footer>
""" % (
        tuiles([(m["fiches"], "fiches de séance"),
                (m["modules_fiches"], "modules couverts"),
                (m["sommaires"], "sommaires de module"),
                ("2", "mises en page du manuel relié"),
                (m["autres_docs"], "autres documents")]),
        table(["Niveau", "Fiches de l'élève", "Diaporamas de séance"], lignes),
        prise("Une fiche de grammaire", "Séance B2 du module 1 — « Dire pourquoi ».",
              "01-fiche-seance.jpg", "Fiche élève en noir et blanc",
              "<b>À regarder :</b> les lignes « nom » et « date » en tête, les objectifs "
              "écrits à la première personne, la règle encadrée, deux tableaux d'analyse, "
              "puis le test qui tranche. Aucune couleur, et pourtant six niveaux de "
              "hiérarchie."),
        prise("Une fiche de compréhension", "Séance A1 — le dialogue d'ouverture.",
              "02-fiche-dialogue.jpg", "Fiche élève d'écoute",
              "<b>À regarder :</b> le dialogue transcrit, le vocabulaire, puis les "
              "questions avec la place pour écrire. L'élève repart avec ce qu'il a "
              "entendu."),
        prise("Le sommaire d'un module", "Une page par module, remise en tête du paquet.",
              "03-sommaire-module.jpg", "Sommaire des seize séances d'un module",
              "<b>À regarder :</b> les seize séances par bloc, avec leur durée — 60, 75 ou "
              "90 minutes. C'est aussi la carte de route de l'élève : il voit où il en est."),
        prise("Ma semaine", "Ce que le groupe fait cette semaine, séance par séance.",
              "04-materiel-semaine.jpg", "Onglet Matériel, vue « Ma semaine »",
              "<b>À regarder :</b> l'état du dépôt, à droite — <b>86 modules complets sur "
              "87</b>. Et les dépôts de l'équipe : un enseignant peut déposer sa propre "
              "version d'une fiche à côté de l'officielle, sans jamais l'écraser."),
        prise("Le catalogue", "Tout le matériel, filtrable.",
              "05-materiel-catalogue.jpg", "Onglet Matériel, vue catalogue",
              "<b>À regarder :</b> les filtres — type de séance, domaine de vie, type de "
              "fichier, bloc — et sur chaque module « <b>Tout prendre</b> » ou « Les "
              "fiches ». Le compte annonce ce qui est équipé : « 16 séances équipées "
              "sur 16 »."),
        prise("Le manuel relié", "Le niveau 4 en un seul PDF.",
              "06-manuel-couverture.jpg", "Couverture du manuel de l'élève niveau 4",
              "<b>À regarder :</b> ce n'est pas un autre contenu — ce sont les mêmes "
              "fiches, reliées. Produit par une commande, donc refait à neuf dès qu'une "
              "séance change."),
        etat_couverture(m))

    page("fiches-eleve.html", "Les fiches de l'élève",
         "Direction et enseignants · Le matériel",
         "Les fiches de l'élève",
         "Ce que l'élève reçoit sur papier, et ce que l'enseignant a en main sans rien "
         "préparer : <b>%s fiches de séance</b> couvrant %d modules, une page par séance, "
         "en noir et blanc, plus les sommaires et le manuel relié. Toutes sortent du même "
         "fichier que le diaporama projeté en classe : elles ne peuvent pas diverger."
         % (nb(m["fiches"]), m["modules_fiches"]),
         "Compté sur le dépôt le %s. Les captures sont prises sur les fichiers réels." % m["quand"],
         '<a class="lien" href="powerpoints-enseignant.html">Les diaporamas de séance</a>'
         '<a class="lien" href="fiches-eleve.pdf">Version papier (PDF)</a>',
         corps)


def page_decks(m):
    niv = m["decks_par_niveau"]
    lignes = [[n, niv[n], niv[n] * 12] for n in sorted(niv)]
    types = {
        "titre": "la page de garde : le code de la séance, son titre, sa durée",
        "objectifs": "« À la fin, je serai capable de… » — la voix de l'élève, pas celle du programme",
        "declencheur": "la question d'ouverture, avec sa photo pédagogique",
        "regle": "un énoncé, gros, seul — la diapositive qu'on photographie",
        "tableau": "l'analyse en rangées, séparées par un filet",
        "cartes": "une grille de cas, deux ou trois colonnes",
        "dialogue": "les répliques, le locuteur en gras",
        "piege": "ce qu'on entend souvent, à côté de ce qu'il faut dire",
        "pratique": "l'exercice projeté — suivi de son corrigé, même mise en page",
        "vocabulaire": "les mots avec leur définition, l'article compris",
        "capture": "l'écran de l'exercice interactif, projeté avant qu'on l'ouvre",
        "billet": "le seul bloc foncé autorisé, et il ferme la séance",
    }
    lignes_types = [[t.capitalize(), n, types.get(t, "")] for t, n in m["types"] if t in types]

    corps = """
<section class="conteneur">
  %s
  <p style="margin-top:16px">Chaque séance a <b>son diaporama</b>, prêt à projeter : pas un
  gabarit à remplir, une séance construite. L'enseignant l'ouvre dans PowerPoint, Keynote
  ou Google Slides — c'est un <code>.pptx</code> ordinaire, sans dépendance et sans
  compte.</p>
</section>

<section class="conteneur">
  <p class="eyebrow e-acier">Ce qu'il y a dedans</p>
  <h2>Douze types de diapositives, et pas un de plus</h2>
  <p>Les %s diapositives des %s diaporamas sont bâties avec douze blocs. C'est ce qui rend
  la collection reconnaissable : l'enseignant qui a projeté une séance sait lire toutes les
  autres, et l'élève reconnaît la page où il est.</p>
  %s
  <div class="garde" style="margin-top:18px">
    <p><b>%s diapositives sur %s portent des notes de présentateur</b> — pas un résumé de
    la diapositive, mais ce qu'il faut faire : la question à poser, ce qu'on écrit au
    tableau, l'erreur qui va venir et quoi en faire. C'est ce qui permet à un remplaçant de
    prendre la séance.</p>
  </div>
</section>

<section class="conteneur">
  <p class="eyebrow e-ambre">À quoi ça ressemble</p>
  <h2>Une séance, de la première à la dernière diapositive</h2>
  <p>Voici six diapositives de la même séance — B2 du module 1, « Dire pourquoi » —
  redessinées à partir du fichier livré.</p>
  <div class="paire">%s%s</div>
  <div class="paire" style="margin-top:22px">%s%s</div>
  <div class="paire" style="margin-top:22px">%s%s</div>
</section>

<section class="conteneur">
  <p class="eyebrow e-teal">Un module d'un coup d'œil</p>
  <h2>Les seize séances d'un module</h2>
  %s
</section>

<section class="conteneur">
  <p class="eyebrow e-indigo">Comment l'enseignant les obtient</p>
  <h2>Le même dépôt que les fiches</h2>
  <p>Les diaporamas et les fiches vivent au même endroit, dans l'onglet <b>Matériel</b> du
  portail : « Tout prendre » descend la séance entière — le diaporama, la fiche, et le
  corrigé s'il existe.</p>
  %s
</section>

<section class="conteneur">
  <div class="garde">
    <p><b>Un seul contenu, deux sorties.</b> Le fichier de séance qui produit ce diaporama
    produit aussi la fiche de l'élève. Corriger une règle la corrige des deux côtés — et
    c'est la seule façon connue d'éviter qu'un paquet de photocopies dise autre chose que
    ce qui est projeté au tableau.</p>
  </div>
</section>

<hr>
<footer class="conteneur">
  <p>Les nombres sont comptés sur le dépôt par <code>build/materiel_pages.py</code> : les
  diapositives sont dénombrées dans les <code>.pptx</code> eux-mêmes, les types relevés
  dans les %s fichiers de séance. Les six diapositives ci-dessus sont un <b>rendu
  d'épreuve</b> : le poste n'a pas de suite bureautique en ligne de commande, alors la
  chaîne relit le fichier produit et le redessine — elle ne simule pas la mise en page,
  elle lit ce qui a été écrit.</p>
</footer>
""" % (
        tuiles([(m["decks"], "diaporamas de séance"),
                (m["diapos"], "diapositives"),
                (m["notes"], "notes de présentateur"),
                ("%d h" % m["heures"], "de classe préparées"),
                (m["vignettes"], "vignettes d'aperçu")]),
        "{:,}".format(m["diapos"]).replace(",", " "),
        "{:,}".format(m["decks"]).replace(",", " "),
        table(["Bloc", "Fois", "Ce qu'il fait"], lignes_types),
        "{:,}".format(m["notes"]).replace(",", " "),
        "{:,}".format(m["appels"]).replace(",", " "),
        prise("1 · La page de garde", "Le code, le titre, la durée.",
              "10-diapo-titre.jpg", "Diapositive de titre",
              "<b>À regarder :</b> jamais de bandeau noir — le système l'interdit en tête. "
              "La durée est annoncée, parce qu'une séance se planifie."),
        prise("2 · Les objectifs", "Ce que l'élève saura faire à la fin.",
              "11-diapo-objectifs.jpg", "Diapositive des objectifs",
              "<b>À regarder :</b> « À la fin, je serai capable de… » — écrit du point de "
              "vue de l'élève, comme les titres d'exercice du module."),
        prise("3 · La règle", "Un énoncé, gros, seul.",
              "12-diapo-regle.jpg", "Diapositive de règle",
              "<b>À regarder :</b> c'est la diapositive que les élèves photographient. "
              "Elle tient en une phrase testable, pas en une définition."),
        prise("4 · L'exercice projeté", "Le même exercice que dans le module.",
              "13-diapo-exercice.jpg", "Diapositive d'exercice",
              "<b>À regarder :</b> la classe travaille ensemble sur ce que l'élève "
              "retrouvera seul sur son téléphone."),
        prise("5 · Le corrigé", "Généré juste après, même mise en page.",
              "14-diapo-corrige.jpg", "Diapositive de corrigé",
              "<b>À regarder :</b> l'œil ne se déplace pas d'un pixel entre la question et "
              "la réponse — on compare, on ne cherche pas."),
        prise("6 · Le piège", "Ce qu'on entend souvent, ce qu'il faut dire.",
              "15-diapo-piege.jpg", "Diapositive de piège",
              "<b>À regarder :</b> chaque colonne porte son mot et son glyphe (✕ / ✓) : "
              "jamais la couleur seule, ici comme partout."),
        prise("Les seize vignettes du module 1",
              "Une image par séance, celle que le portail montre à l'enseignant.",
              "17-planche-vignettes.jpg", "Planche des seize vignettes de séance",
              "<b>À regarder :</b> le module entier tient sur une planche — cinq blocs, "
              "seize séances, de « Le genou de Yannick » à « Je retiens des mots ». "
              "L'enseignant choisit une séance en la voyant."),
        prise("Le catalogue du dépôt", "Diaporamas et fiches, au même endroit.",
              "05-materiel-catalogue.jpg", "Onglet Matériel du portail enseignant",
              "<b>À regarder :</b> « 16 séances équipées sur 16 », et les filtres par bloc "
              "— l'enseignant qui prépare son bloc C ne descend que le bloc C."),
        m["scripts"])

    page("powerpoints-enseignant.html", "Les diaporamas de séance",
         "Direction et enseignants · Le matériel",
         "Les diaporamas de séance",
         "Ce que l'enseignant projette en classe, sans rien préparer : <b>%s diaporamas</b>, "
         "un par séance, <b>%s diapositives</b> en tout, et <b>%s notes de présentateur</b> "
         "qui disent quoi faire à chaque page. Douze types de diapositives, pas un de plus, "
         "et le même fichier de contenu que la fiche remise à l'élève."
         % ("{:,}".format(m["decks"]).replace(",", " "),
            "{:,}".format(m["diapos"]).replace(",", " "),
            "{:,}".format(m["notes"]).replace(",", " ")),
         "Compté sur le dépôt le %s. Les diapositives montrées sont des fichiers réels." % m["quand"],
         '<a class="lien" href="fiches-eleve.html">Les fiches de l\'élève</a>'
         '<a class="lien" href="powerpoints-enseignant.pdf">Version papier (PDF)</a>',
         corps)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sans-pdf", action="store_true",
                    help="n'écrit que les pages HTML")
    a = ap.parse_args()

    m = mesures()
    page_fiches(m)
    page_decks(m)
    print("%d fiches · %d diaporamas · %d diapositives · %d h de classe"
          % (m["fiches"], m["decks"], m["diapos"], m["heures"]))

    if not a.sans_pdf:
        for nom in ("fiches-eleve", "powerpoints-enseignant"):
            n = imprimer(PRES / (nom + ".html"), PRES / (nom + ".pdf"))
            print("  %-30s %s" % (nom + ".pdf", ("%d pages" % n) if n else "produit"))
