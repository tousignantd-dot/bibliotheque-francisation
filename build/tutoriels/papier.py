#!/usr/bin/env python3
"""Le tutoriel papier : les sept capsules en un seul document, avec sa table.

    python3 build/tutoriels/papier.py            # → HTML + PDF
    python3 build/tutoriels/papier.py --sans-pdf # l'HTML seul, pour relire vite

Demandé le 3 septembre 2026. Une première tentative, la veille, produisait un
PDF **par capsule** : « ce n'est pas le bon ton, pour un document tutoriel on
va tout mettre ensemble avec une table des matières ». D'où celui-ci — un seul
document, sept chapitres numérotés, une étape par plan, les mêmes copies
d'écran que le film.

**Le texte vient du manifeste**, comme la voix et les sous-titres : c'est la
règle de la chaîne, et c'est ce qui garantit que le papier ne raconte pas autre
chose que la vidéo. On ne le récrit pas ici. Les **copies d'écran** viennent de
`guide/captures.json` — rognées sur l'élément dont parle le plan, sans quoi une
fenêtre de 1600 pixels réduite à la largeur d'une page ne se lit plus.

    node build/tutoriels/guide_captures.js 5321   # les refaire toutes

Deux partis pris de mise en page, tous deux payés ailleurs dans le dépôt :

· **Le format se règle dans la feuille** (`@page { size: letter }`), jamais en
  ligne de commande — c'est ce que Chrome imprime, et `build/imprimer.py` relit
  le résultat. Voir la note de `programme/outils/fiche_pdf.py`.
· **La table des matières ne porte pas de numéros de page** : Chrome
  n'implémente pas `target-counter`, et un numéro faux serait pire que pas de
  numéro. Les chapitres sont numérotés, et chacun commence sur une page neuve.

Et deux règles du dépôt, qui décident de l'allure :

· **Le logotype ne se recopie jamais à la main.** La page **lie**
  `assets/design-system/marque-francis.css` et pose le balisage de la remise ;
  un disque placé à l'œil retombe sur le « n » dès que la police manque.
· **Un imprimé du dépôt est en noir et blanc**, hiérarchie par la graisse et
  les filets — c'est la feuille commune `fiche-imprimee.css`, dont ce document
  reprend les conventions (Nunito, 11,5 pt, largeur lettre, filets plus
  sombres qu'à l'écran, parce qu'une photocopieuse efface tout ce qui est plus
  clair que 15 % de noir). La seule couleur de la page est le point du « i ».
"""
import html
import json
import pathlib
import re
import sys
from datetime import date

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parent.parent
sys.path.insert(0, str(RACINE / "build"))

SORTIE = RACINE / "assets/presentations/tutoriel-espace-enseignant.html"
PDF = SORTIE.with_suffix(".pdf")
DS = RACINE / "assets/design-system"

MOIS = ("janvier février mars avril mai juin juillet août septembre octobre "
        "novembre décembre").split()

# Ce que chaque chapitre apprend, en une ligne — le manifeste porte le texte
# dit, pas la promesse. Écrit ici parce que c'est du texte de document, absent
# de la vidéo : une table des matières qui ne dit que des titres n'aide pas à
# choisir où aller.
PROMESSES = {
    "01-tour-du-portail": "Les grandes pièces de l'écran, et à quoi sert chacune.",
    "05-groupes": "Ouvrir un groupe, lui donner son nom et son niveau.",
    "02-planifier": "Donner des dates à des activités — le geste central du portail.",
    "03-sections": "Ouvrir un module section par section plutôt que d'un bloc.",
    "04-eleves": "Inscrire les élèves, générer et imprimer leurs codes.",
    "06-materiel": "Retrouver les présentations et les fiches, et déposer les vôtres.",
    "07-composer": "Composer la commande d'une activité neuve, aux termes du programme.",
}


def phrases(texte):
    """Le texte d'un plan coupé en (première phrase, reste).

    La première phrase devient le titre de l'étape : elle dit toujours ce qu'on
    fait, puisqu'elle a été écrite pour être entendue en tête de plan.
    """
    m = re.match(r"(.+?[.!?])(\s+)(.*)", texte, re.S)
    if not m or len(m.group(1)) > 120:
        return texte, ""
    return m.group(1), m.group(3)


def images(capsule, plan, captures, fiche_plan=None):
    """La copie d'écran d'une étape, chemin relatif à la page produite.

    Trois sources, dans l'ordre :

    1. **Une image déposée à la main** — `guide/deposees/<capsule>_<plan>.*`,
       arrivée par la case de dépôt du storyboard. Quand l'utilisateur a
       montré ce qu'il voulait voir, c'est ça qu'on imprime, et rien d'autre.
    2. **L'image après le geste demandé** — `papier.apres_geste` du plan, pour
       montrer le bouton *avant* qu'on le clique quand le texte dit de le
       cliquer : une fois cliqué, il a disparu avec son écran.
    3. **L'image de la fin du plan** — l'écran une fois le geste fait, donc ce
       que le lecteur doit reconnaître.

    Une entrée de `captures.json` est un objet — `{quand, geste, fichier}` —
    et son `fichier` porte déjà le préfixe `guide/`.
    """
    deposee = next(iter(sorted((ICI / "guide" / "deposees").glob(
        "%s_%s.*" % (capsule, plan)))), None)
    if deposee:
        return ["../../build/tutoriels/%s" % deposee.relative_to(ICI).as_posix()]
    voulu = (fiche_plan or {}).get("papier", {}).get("apres_geste")
    for fiche in captures.get(capsule, []):
        if fiche["plan"] != plan:
            continue
        vues = fiche.get("images", [])
        if not vues:
            return []
        if voulu is not None:
            # la dernière image prise au plus tard au geste demandé — les
            # images identiques ayant été retirées, le geste exact peut manquer
            candidates = [i for i in vues if i.get("geste", 0) <= voulu]
            choisie = candidates[-1] if candidates else vues[0]
        else:
            choisie = next((i for i in vues if i.get("quand") == "fin"), vues[-1])
        return ["../../build/tutoriels/%s" % choisie["fichier"]]
    return []


def duree(secondes):
    m, s = divmod(int(round(secondes)), 60)
    return "%d min %02d" % (m, s) if m else "%d s" % s


FEUILLE = """
@page { size: letter; margin: 16mm 15mm 18mm; }
@font-face{font-family:'Nunito';src:url('../design-system/fonts/nunito-latin.woff2') format('woff2');
           font-weight:400 900;font-display:swap}
/* Les conventions de `fiche-imprimee.css` : aucune couleur, la hiérarchie par
   la graisse et les filets, des gris plus sombres qu'à l'écran. */
:root{
  --paper:#FFFFFF; --tint:#F0F0EE; --line:#C9C9C6; --rule:#17181A;
  --ink:#17181A; --body:#2B2E30; --soft:#4B4F52; --muted:#5E6165;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Nunito','Trebuchet MS',sans-serif;font-size:11.5pt;line-height:1.5;
     color:var(--body);background:var(--paper);
     -webkit-print-color-adjust:exact;print-color-adjust:exact}
h1,h2,h3{color:var(--ink);line-height:1.2;letter-spacing:-0.01em}
.eyebrow{font-size:9.5pt;font-weight:800;text-transform:uppercase;letter-spacing:.12em;
         color:var(--muted)}

/* À l'écran, la page se donne la largeur du papier : on relit ce qui sera
   imprimé, pas une colonne étirée à la fenêtre. */
@media screen{
  html{background:#BBBBBB}
  body{width:215.9mm;margin:0 auto;padding:16mm 15mm 18mm;background:var(--paper)}
}

/* — Couverture — */
.couverture{height:230mm;display:flex;flex-direction:column;justify-content:center;
            break-after:page}
.couverture .fr-lockup{margin-bottom:30pt}
.couverture h1{font-size:32pt;font-weight:900;letter-spacing:-0.02em;line-height:1.06;
               margin:6pt 0 12pt;max-width:15cm}
.couverture .chapeau{font-size:13pt;font-weight:600;color:var(--soft);max-width:12.5cm;
                     margin-bottom:26pt}
.couverture .date{font-size:9.5pt;color:var(--muted);border-top:1.5px solid var(--rule);
                  padding-top:9pt;max-width:12.5cm}

/* — Table des matières — */
.table{break-after:page}
.table h2{font-size:22pt;font-weight:900;margin-bottom:5pt}
.table .note{color:var(--soft);font-size:10.5pt;font-weight:600;margin-bottom:16pt;
             max-width:13cm}
.table ol{list-style:none;counter-reset:ch}
.table li{counter-increment:ch;position:relative;padding:10pt 0 10pt 11mm;
          border-top:1px solid var(--line);break-inside:avoid}
.table li:first-child{border-top:1.5px solid var(--rule)}
.table li::before{content:counter(ch);position:absolute;left:0;top:11pt;
                  width:7mm;height:7mm;border-radius:50%;border:1.5px solid var(--rule);
                  color:var(--ink);font-size:10pt;font-weight:800;
                  display:flex;align-items:center;justify-content:center}
.table .t{font-weight:900;font-size:12.5pt;color:var(--ink)}
.table .p{color:var(--soft);font-size:10.5pt;font-weight:600}
.table .d{position:absolute;right:0;top:11pt;color:var(--muted);font-size:9.5pt;
          font-weight:800;font-variant-numeric:tabular-nums}

/* — Chapitres — */
.chap{break-before:page}
.chap > header{border-bottom:2.5px solid var(--rule);padding-bottom:8pt;margin-bottom:16pt}
.chap h2{font-size:22pt;font-weight:900;margin-top:3pt}
.chap .promesse{font-size:12pt;font-weight:600;color:var(--soft);margin-top:4pt}

.etape{position:relative;padding-left:11mm;margin-bottom:15pt;
       break-inside:avoid;page-break-inside:avoid}
.etape::before{content:attr(data-n);position:absolute;left:0;top:1pt;
               width:7mm;height:7mm;border-radius:50%;border:1.5px solid var(--rule);
               color:var(--ink);font-size:10pt;font-weight:800;
               display:flex;align-items:center;justify-content:center}
.etape h3{font-size:12.5pt;font-weight:900;margin-bottom:4pt}
.etape p{margin-bottom:8pt}
.etape figure{margin-top:7pt}
.etape img{display:block;max-width:100%;max-height:76mm;width:auto;
           border:1px solid var(--line);border-radius:6px}

.retenir{border:2.5px solid var(--rule);border-radius:12px;padding:11pt 14pt;
         margin-top:16pt;break-inside:avoid}
.retenir .lbl{font-size:9.5pt;font-weight:800;text-transform:uppercase;
              letter-spacing:.12em;color:var(--ink);margin-bottom:4pt}
.retenir p{font-size:12pt;font-weight:600;color:var(--ink)}

footer{margin-top:20pt;padding-top:8pt;border-top:1px solid var(--line);
       color:var(--muted);font-size:9pt}
"""


# Le balisage de la remise, mot pour mot. Le disque du « i » ne se dessine pas
# à la main : il vient de `marque-francis.css`, que la page lie. Un point posé
# à l'œil tombe sur le « n » dès que Nunito manque — c'est arrivé.
LOCKUP = ("""<span class="fr-lockup fr-lockup--grand fr-lockup--sombre">
  <span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" \
aria-hidden="true">ı<span class="fr-point"></span></span>s</span>
  <span class="fr-trait" aria-hidden="true"></span>
  <span class="fr-desc">Aide à l'apprentissage du français</span>
</span>""")


def main():
    manifeste = json.loads((ICI / "manifeste.json").read_text(encoding="utf-8"))
    fichier = ICI / "guide" / "captures.json"
    captures = json.loads(fichier.read_text(encoding="utf-8")) if fichier.exists() else {}
    capsules = manifeste["capsules"]
    sans = [c["id"] for c in capsules
            if not any(images(c["id"], p["id"], captures, p) for p in c["plans"])]

    quand = date.today()
    aujourdhui = "%d %s %d" % (quand.day, MOIS[quand.month - 1], quand.year)

    # La table
    lignes = []
    for i, c in enumerate(capsules, 1):
        secondes = sum(f["secondes"] for f in captures.get(c["id"], [])) or 0
        lignes.append(
            '<li><div><div class="t">%s</div><div class="p">%s</div></div>'
            '%s</li>' % (html.escape(c["titre"]),
                         html.escape(PROMESSES.get(c["id"], "")),
                         '<div class="d">%s</div>' % duree(secondes) if secondes else ""))

    # Les chapitres
    chapitres = []
    for i, c in enumerate(capsules, 1):
        etapes = []
        n = 0
        for plan in c["plans"]:
            if plan["id"] == "fin":
                continue
            n += 1
            titre, suite = phrases(plan["texte"])
            vues = "".join('<img src="%s" alt="">' % html.escape(u)
                           for u in images(c["id"], plan["id"], captures, plan))
            etapes.append(
                '<div class="etape" data-n="%d">'
                '<h3>%s</h3>%s%s</div>'
                % (n, html.escape(titre),
                   "<p>%s</p>" % html.escape(suite) if suite else "",
                   "<figure>%s</figure>" % vues if vues else ""))
        fin = next((p for p in c["plans"] if p["id"] == "fin"), None)
        retenir = ""
        if fin:
            texte = re.sub(r"\s*Voilà pour (cette capsule|celle-ci)\.\s*À la prochaine\.\s*$",
                           "", fin["texte"]).strip()
            retenir = ('<div class="retenir"><div class="lbl">À retenir</div>'
                       '<p>%s</p></div>' % html.escape(texte))
        chapitres.append(
            '<section class="chap"><header><div class="num">Chapitre %d</div>'
            '<h2>%s</h2><p class="promesse">%s</p></header>%s%s</section>'
            % (i, html.escape(c["titre"]), html.escape(PROMESSES.get(c["id"], "")),
               "".join(etapes), retenir))

    page = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>L'espace enseignant — le guide</title>
<link rel="stylesheet" href="../design-system/marque-francis.css">
<style>%s</style></head><body>
<section class="couverture">%s
  <div class="eyebrow">Francisation · Guide de l'enseignant</div>
  <h1>L'espace enseignant, pas à pas</h1>
  <p class="chapeau">Les sept capsules vidéo du portail, réunies en un seul document :
  le même parcours, les mêmes écrans, à lire et à annoter.</p>
  <p class="date">Version du %s · %d chapitres · Ce guide accompagne les capsules vidéo,
  accessibles par le bouton « Tutoriels » de la barre de groupe.</p>
</section>
<section class="table">
  <h2>Table des matières</h2>
  <p class="note">Chaque chapitre commence sur une page neuve et se lit indépendamment.
  L'ordre est celui des gestes d'une rentrée : ouvrir un groupe, poser des dates,
  inscrire les élèves, puis le matériel et les outils.</p>
  <ol>%s</ol>
</section>
%s
<footer>Document produit le %s par <code>build/tutoriels/papier.py</code>,
depuis le manifeste des capsules — il dit exactement ce que disent les vidéos.</footer>
</body></html>
""" % (FEUILLE, LOCKUP, aujourdhui, len(capsules), "".join(lignes),
       "".join(chapitres), aujourdhui)

    SORTIE.write_text(page, encoding="utf-8")
    print("→ %s" % SORTIE.relative_to(RACINE))
    if sans:
        print("  ⚠ aucune copie d'écran pour : %s" % ", ".join(sans))
        print("    node build/tutoriels/guide_captures.js 5321")
    if "--sans-pdf" not in sys.argv:
        from imprimer import imprimer
        pages = imprimer(SORTIE, PDF)
        print("→ %s%s" % (PDF.relative_to(RACINE),
                          " — %d pages" % pages if pages else ""))


if __name__ == "__main__":
    main()
