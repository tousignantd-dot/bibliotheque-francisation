#!/usr/bin/env python3
"""La fiche de poche du bloc A — « Un instant, s'il vous plaît ».

    python3 build/fiche_chaussure.py              # la page + le PDF
    python3 build/fiche_chaussure.py --sans-pdf   # la page seule

C'est l'objet qui sort de la salle : une feuille lettre qui reste dans la poche
du tablier. Elle est aussi la première chose qu'une gérante regarde — d'où le
soin.

Trois règles, héritées des fiches élèves du dépôt et de la fiche de Belrive :
  · **aucune couleur** — elle sort de la photocopieuse du magasin ;
  · la hiérarchie passe par la graisse et les filets, jamais par la teinte ;
  · les cinq phrases restent **en français**. L'espagnol et l'anglais sont un
    appui, en plus petit, dessous — jamais à leur place. Un vendeur qui ne
    lirait que sa langue n'aurait plus rien à dire au client.

LE CHEMIN DE LA POLICE EST RELATIF, et ce n'est pas un détail : le PDF
s'imprime en `file://`, et un chemin absolu ferait tomber sur une police de
repli **sans rien signaler**. Le contrôle du format relit le `/MediaBox` plutôt
que de faire confiance à la ligne de commande — Chrome imprime ce que dit
`@page`, pas ce qu'on lui demande.

Sortie : assets/presentations/fiche-chaussure-blocA.html (+ .pdf)
"""
import argparse
import pathlib
import re
import subprocess

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / 'assets' / 'presentations' / 'fiche-chaussure-blocA.html'
PDF = SORTIE.with_suffix('.pdf')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
POLICE = '../design-system/fonts/nunito-latin.woff2'  # relatif : vaut aussi pour le PDF
LETTRE = (612, 792)   # points, format lettre

# (numéro, la phrase française, quand s'en servir, espagnol, anglais)
PHRASES = [
    ('1', "Un instant, s'il vous plaît.",
     "Quand ça va trop vite. Quatre mots, polis, et le client s'arrête.",
     "Cuando va demasiado rápido. Cuatro palabras, y el cliente se detiene.",
     "When it is going too fast. Four polite words, and the customer stops."),
    ('2', "Vous cherchez quel modèle&nbsp;?",
     "Une chose à la fois. Le client sait quoi répondre.",
     "Una cosa a la vez. El cliente sabe qué contestar.",
     "One thing at a time. The customer knows what to answer."),
    ('3', "Quelle pointure, s'il vous plaît&nbsp;?",
     "On y répond par un nombre. La question la plus facile du magasin.",
     "Se contesta con un número. La pregunta más fácil de la tienda.",
     "It is answered with a number. The easiest question in the shop."),
    ('4', "Je vais voir en réserve. <span class=\"gris\">Je reviens tout de suite.</span>",
     "« Je reviens » est la moitié du geste : un client qui le sait attend.",
     "« Je reviens » es la mitad del gesto: el cliente que lo sabe, espera.",
     "« Je reviens » is half the move: a customer who knows it waits."),
    ('5', "Un instant. Je vais chercher ma collègue.",
     "Le plus difficile, et le seul qui garde le client dans le magasin.",
     "Lo más difícil, y lo único que mantiene al cliente en la tienda.",
     "The hardest one, and the only one that keeps the customer in the shop."),
]

CSS = """
@page { size: letter; margin: 14mm 14mm 12mm; }
*{box-sizing:border-box}
@font-face{font-family:'Nunito';src:url('%(police)s') format('woff2');
  font-weight:400 800;font-display:swap}
html,body{margin:0;padding:0;background:#FFF;color:#000}
body{font-family:'Nunito',-apple-system,'Segoe UI',sans-serif;font-size:11.4pt;line-height:1.42}
.f{max-width:186mm;margin:0 auto;padding:10mm 0 0}

.tete{display:flex;align-items:flex-end;justify-content:space-between;gap:14px;
  border-bottom:2.4pt solid #000;padding-bottom:7px}
.tete h1{font-size:19pt;font-weight:800;letter-spacing:-.01em;margin:0;line-height:1.08}
.tete .ou{font-size:8.6pt;font-weight:700;text-transform:uppercase;letter-spacing:.11em;
  text-align:right;white-space:nowrap}
.chapeau{font-size:10.4pt;margin:9px 0 0;max-width:150mm}
.chapeau b{font-weight:800}

ol.p{list-style:none;margin:13px 0 0;padding:0}
ol.p li{border-bottom:.6pt solid #B8B8B8;padding:9px 0 9px 30px;position:relative;
  break-inside:avoid}
ol.p li:first-child{border-top:.6pt solid #B8B8B8}
ol.p .n{position:absolute;left:0;top:9px;font-size:13pt;font-weight:800;
  width:22px;text-align:left}
ol.p .fr{font-size:13.2pt;font-weight:800;line-height:1.24}
ol.p .fr .gris{font-weight:600;color:#555}
ol.p .q{font-size:9.9pt;margin-top:2px}
ol.p .ap{font-size:8.9pt;color:#4A4A4A;margin-top:4px;padding-left:9px;
  border-left:1.6pt solid #C9C9C9;line-height:1.4}
ol.p .ap i{font-style:normal;font-weight:800;letter-spacing:.06em;font-size:7.6pt;
  text-transform:uppercase;color:#000;margin-right:5px}

.defi{border:1.6pt solid #000;padding:11px 13px;margin-top:14px;break-inside:avoid}
.defi h2{font-size:9pt;font-weight:800;text-transform:uppercase;letter-spacing:.11em;
  margin:0 0 5px}
.defi p{margin:0;font-size:11.8pt;font-weight:700}
.defi .ap{font-size:8.9pt;color:#4A4A4A;margin-top:5px;font-weight:400}
.cases{display:flex;gap:16px;margin-top:9px;align-items:center;flex-wrap:wrap}
.cases span{font-size:8.6pt;font-weight:700;text-transform:uppercase;letter-spacing:.07em}
.case{width:15px;height:15px;border:1.2pt solid #000;display:inline-block;
  vertical-align:-2px;margin-right:5px}

.pied{margin-top:12px;border-top:.6pt solid #B8B8B8;padding-top:7px;
  font-size:8.4pt;color:#4A4A4A;display:flex;justify-content:space-between;gap:12px}
.pied b{color:#000}
@media screen{ body{background:#EDEDEA;padding:22px 0}
  .f{background:#FFF;padding:16mm 16mm 12mm;box-shadow:0 1px 3px rgba(0,0,0,.2)} }
""" % {'police': POLICE}


def page():
    lignes = []
    for n, fr, quand, es, en in PHRASES:
        lignes.append(
            '    <li><span class="n">%s</span>\n'
            '      <div class="fr">%s</div>\n'
            '      <div class="q">%s</div>\n'
            '      <div class="ap"><i>ES</i>%s</div>\n'
            '      <div class="ap"><i>EN</i>%s</div>\n'
            '    </li>' % (n, fr, quand, es, en))
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fiche de poche — Un instant, s'il vous plaît</title>
<style>%s</style>
</head>
<body>
<div class="f">

  <div class="tete">
    <h1>Un instant, s'il vous plaît</h1>
    <div class="ou">Chaussures Rivard<br>Bloc A sur 4</div>
  </div>

  <p class="chapeau">Cinq phrases à garder dans la poche du tablier. Aucune n'est
  difficile&nbsp;: vous les connaissiez déjà presque toutes. <b>Ce bloc ne vous a pas appris des
  mots — il vous a donné la permission de les dire.</b></p>

  <ol class="p">
%s
  </ol>

  <div class="defi">
    <h2>Le défi de la semaine</h2>
    <p>Dites <b>une fois</b> «&nbsp;un instant, s'il vous plaît&nbsp;» à un client qui parle
    trop vite. Une seule fois.</p>
    <div class="ap">ES&nbsp;· Diga <b>una vez</b> « un instant, s'il vous plaît » a un cliente
      que habla demasiado rápido.
      &nbsp;&nbsp;EN&nbsp;· Say « un instant, s'il vous plaît » <b>once</b>, to a customer who
      is talking too fast.</div>
    <div class="cases">
      <span><i class="case"></i>Je l'ai fait</span>
      <span><i class="case"></i>Vu par la gérante</span>
      <span>Date&nbsp;: ______________</span>
    </div>
  </div>

  <div class="pied">
    <span><b>francis</b> — formation en milieu de travail</span>
    <span>Les cinq phrases restent en français&nbsp;: c'est ce qu'il faut dire sur le plancher.</span>
  </div>

</div>
</body>
</html>
""" % (CSS, '\n'.join(lignes))


def controler_format():
    """Chrome imprime ce que dit @page, pas ce qu'on lui demande. On relit."""
    if not PDF.exists():
        return
    brut = PDF.read_bytes()[:400000]
    m = re.search(rb'/MediaBox\s*\[\s*0\s+0\s+([\d.]+)\s+([\d.]+)', brut)
    if not m:
        print('  ⚠ format illisible — /MediaBox introuvable')
        return
    l, h = round(float(m.group(1))), round(float(m.group(2)))
    pages = len(re.findall(rb'/Type\s*/Page[^s]', brut))
    if (l, h) != LETTRE:
        print('  ✗ FORMAT %d × %d pt — attendu %d × %d (lettre)' % (l, h, *LETTRE))
    else:
        print('  ✓ format lettre %d × %d pt · %d page(s)' % (l, h, pages))
    if pages > 1:
        print('  ⚠ %d pages : la fiche doit tenir sur UNE feuille' % pages)


def imprimer():
    if not pathlib.Path(CHROME).exists():
        print('  Chrome introuvable — PDF non produit')
        return
    cmd = [CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
           '--print-to-pdf=%s' % PDF, SORTIE.as_uri()]
    subprocess.run(cmd, capture_output=True, timeout=90)
    if PDF.exists():
        print('  %-38s %d ko' % (PDF.name, PDF.stat().st_size // 1024))
        controler_format()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sans-pdf', action='store_true')
    a = ap.parse_args()
    police = (SORTIE.parent / POLICE).resolve()
    if not police.exists():
        print('  ⚠ police introuvable : %s' % police)
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page(), encoding='utf-8')
    print('  %-38s %d phrases' % (SORTIE.name, len(PHRASES)))
    if not a.sans_pdf:
        imprimer()


if __name__ == '__main__':
    main()
