#!/usr/bin/env python3
"""La fiche de poche du bloc 3 — « Je n'ai pas compris ».

    python3 build/fiche_belrive.py              # la page + le PDF
    python3 build/fiche_belrive.py --sans-pdf   # la page seule

C'est l'objet qui sort de la salle : une feuille lettre, pliée en deux, qui
reste dans la poche du sarrau. Elle est aussi la première chose qu'un
contremaître regarde — d'où le soin.

Trois règles, héritées des fiches élèves du dépôt :
  · **aucune couleur** — elle sort d'une photocopieuse de plancher ;
  · la hiérarchie passe par la graisse et les filets, jamais par la teinte ;
  · les cinq phrases restent **en français**. L'espagnol et l'anglais sont
    un appui, en plus petit, dessous — jamais à leur place. Un travailleur qui
    ne lirait que sa langue n'aurait plus rien à dire au superviseur.

Sortie : assets/presentations/fiche-belrive-bloc3.html (+ .pdf)
"""
import argparse
import pathlib
import subprocess

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / 'assets' / 'presentations' / 'fiche-belrive-bloc3.html'
PDF = SORTIE.with_suffix('.pdf')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
POLICE = '../design-system/fonts/nunito-latin.woff2'  # relatif : vaut aussi pour le PDF, imprimé en file://

# (numéro, la phrase française, quand s'en servir, espagnol, anglais)
PHRASES = [
    ('1', "Attendez, s'il vous plaît.",
     "Quand ça va trop vite. Trois mots, et tout le monde s'arrête.",
     "Cuando va demasiado rápido.", "When it is going too fast."),
    ('2', "Vous parlez trop vite pour moi. Répétez lentement&nbsp;?",
     "Ce n'est pas un reproche : « pour moi » change tout.",
     "No es un reproche: « pour moi » lo cambia todo.",
     "It is not a complaint: « pour moi » changes everything."),
    ('3', "Montrez-moi, s'il vous plaît.",
     "Quand c'est un objet, un endroit, un geste. Le plus rapide.",
     "Cuando es un objeto, un lugar, un gesto.",
     "When it is an object, a place, a movement."),
    ('4', "Je fais… <span class=\"gris\">(redites la consigne dans vos mots)</span>",
     "La seule preuve que vous avez compris. Redire, toujours.",
     "La única prueba de que entendió. Repita siempre.",
     "The only proof that you understood. Always say it back."),
    ('5', "Je n'aurai pas le temps. Je peux le faire après&nbsp;?",
     "Le plus difficile, et le plus utile : dites-le tôt.",
     "Lo más difícil y lo más útil: dígalo temprano.",
     "The hardest and the most useful: say it early."),
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
<title>Fiche de poche — Je n'ai pas compris</title>
<style>%s</style>
</head>
<body>
<div class="f">

  <div class="tete">
    <h1>Je n'ai pas compris</h1>
    <div class="ou">Aliments Belrive<br>Bloc 3 sur 8</div>
  </div>

  <p class="chapeau">Cinq phrases à garder dans la poche du sarrau. Aucune n'est difficile&nbsp;:
  vous les connaissiez déjà presque toutes. <b>Ce bloc ne vous a pas appris des mots — il vous a
  donné la permission de les dire.</b></p>

  <ol class="p">
%s
  </ol>

  <div class="defi">
    <h2>Le défi de la semaine</h2>
    <p>Demandez <b>une fois</b> à quelqu'un de répéter plus lentement. Une seule fois.</p>
    <div class="ap">ES&nbsp;· Pídale <b>una vez</b> a alguien que repita más despacio.
      &nbsp;&nbsp;EN&nbsp;· Ask someone <b>once</b> to repeat more slowly.</div>
    <div class="cases">
      <span><i class="case"></i>Je l'ai fait</span>
      <span><i class="case"></i>Vu par le chef d'équipe</span>
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


def imprimer():
    if not pathlib.Path(CHROME).exists():
        print('  Chrome introuvable — PDF non produit')
        return
    cmd = [CHROME, '--headless', '--disable-gpu', '--no-pdf-header-footer',
           '--print-to-pdf=%s' % PDF, SORTIE.as_uri()]
    subprocess.run(cmd, capture_output=True, timeout=90)
    if PDF.exists():
        print('  %-38s %d ko' % (PDF.name, PDF.stat().st_size // 1024))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sans-pdf', action='store_true')
    a = ap.parse_args()
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page(), encoding='utf-8')
    print('  %-38s %d phrases' % (SORTIE.name, len(PHRASES)))
    if not a.sans_pdf:
        imprimer()


if __name__ == '__main__':
    main()
