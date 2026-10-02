#!/usr/bin/env python3
"""La fiche d'une page de chaque application, à imprimer ou à joindre à un courriel.

    python3 build/fiches_une_page.py            # les 4 fiches HTML + leur PDF (serveur local sur 5497)
    python3 build/fiches_une_page.py --sans-pdf

Demande de Daniel, 2 oct. 2026 : « je veux une version qui tient sur une page,
avec en couleur seulement l'image de l'écran du portable ; mets ensuite un lien
sur le dépliant ». Elle remplace le PDF du dépliant entier (5-6 pages, en
couleur), jugé à refaire.

Sortie, pour chaque application : modules-autonomes/<app>/fiche.html (la
source, noindex) et modules-autonomes/<app>/fiche.pdf (le lien du dépliant).
Tout est en noir et gris — le point de la marque compris, comme à toute
impression — sauf la capture du téléphone. Les chiffres viennent des
dépliants ; le prix est lu dans la caisse (pelerins.offre()) AU MOMENT de la
production : refaire les fiches après un changement de prix ou la fin de la
promotion (31 déc. 2026). Le format lettre et la page UNIQUE se relisent dans
le PDF : le script refuse une deuxième page.
"""
import html, pathlib, re, subprocess, sys, time

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
import pelerins  # noqa: E402
from qr_bloc import url  # noqa: E402
import qr  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

FICHES = [
    {"dossier": "compostelle", "nom": "En route vers Compostelle", "vente": True,
     "sur": "Voyage · espagnol · chemin de Saint-Jacques",
     "accroche": "L'espagnol du Camino francés, appris la veille du jour où vous en aurez besoin, dans votre téléphone.",
     "chiffres": [("8", "entraînements de 15 minutes, à la maison, avant de partir"),
                  ("10", "étapes choisies, de Roncesvalles à Santiago"),
                  ("0 $", "pour tout le chemin, sans inscription ni courriel")],
     "temps": [("Avant de partir", "Préparer son sac : les sons, les nombres et les prix, l'heure, les questions, comprendre la réponse."),
               ("Sur le chemin", "Une situation par étape : l'albergue complet, le bar du matin, la pharmacie, le marché."),
               ("Le soir", "Parler librement avec les gens du chemin : ils vous répondent vraiment, en espagnol, puis un bilan en français.")],
     "paye": "Parler librement", "capture": "depliant/accueil.jpg"},
    {"dossier": "toronto", "nom": "Une semaine à Toronto", "vente": True,
     "sur": "Voyage · anglais",
     "accroche": "L'anglais qu'il faut à un francophone pour une semaine à Toronto : quinze minutes à la fois, à préparer chez vous, puis dans la trousse une fois sur place.",
     "chiffres": [("8", "séances de 15 minutes avant de partir"),
                  ("10", "lieux de Toronto où jouer la situation"),
                  ("196", "mots du voyage, dits par de vraies voix de Toronto")],
     "temps": [("Avant de partir", "Faire sa valise : huit séances, chacune en trois temps — j'écoute, je reconnais, je le dis."),
               ("La semaine jouée", "Dix lieux, de l'arrivée au départ : la personne du lieu vous répond en anglais, le bilan est en français."),
               ("Sur place", "Ma trousse, même sans réseau : les phrases de chaque lieu, les urgences, les phrases à montrer, le pourboire.")],
     "paye": "La semaine jouée", "capture": "depliant/accueil.jpg"},
    {"dossier": "francoeur-planches", "nom": "Maison Francœur", "vente": True,
     "sur": "Formation en milieu de travail · vente au détail · vêtements",
     "accroche": "Le français du magasin de vêtements, client par client : les mots et les phrases du plancher, en images et à l'oreille, puis de vrais clients à servir.",
     "chiffres": [("149", "mots du magasin, dessinés, en 11 rayons"),
                  ("11", "langues d'appui, de l'arabe au tigrigna ; ou le français seul"),
                  ("8", "clients qui vous parlent vraiment")],
     "temps": [("Mon niveau", "Un court test pour savoir par où commencer."),
               ("Les mots et les exercices", "Les rayons, vêtement par vêtement ; ce que le client veut, ce que la gérante demande."),
               ("Le magasin joué", "Les clients entrent ; vous les servez à voix haute, puis un bilan geste par geste.")],
     "paye": "Le magasin joué", "capture": "depliant/magasin.jpg"},
    {"dossier": "hotel-reception", "nom": "Hôtel Rive-Claire", "vente": True,
     "sur": "Formation en milieu de travail · hôtellerie · réception",
     "accroche": "L'accueil à la réception, dans la langue du client : français, anglais et espagnol, à égalité. Vous choisissez la langue que vous parlez et celle que vous apprenez.",
     "chiffres": [("153", "mots de la réception, en 8 thèmes et un comptoir à toucher"),
                  ("3", "langues à égalité : six façons d'apprendre"),
                  ("8", "clients qui vous parlent vraiment, au comptoir et au téléphone")],
     "temps": [("Le comptoir", "Votre poste, tel que vous le voyez de votre place ; vous touchez, vous entendez."),
               ("Les mots et les pièges", "Les faux amis d'une langue à l'autre, les nombres, les noms épelés."),
               ("Le comptoir joué", "Une arrivée sans réservation, une demande hors règle : vous répondez, puis un bilan.")],
     "paye": "Le comptoir joué", "capture": "depliant/comptoir.jpg"},
]


def e(s):
    return html.escape(s, quote=True)


def dollars(c):
    return f"{c // 100},{c % 100:02d} $"


def offre_txt():
    o = pelerins.offre()
    t = f"{dollars(o['prix'])} pour {o['conversations']} conversations pendant {round(o['jours'] / 30.4)} mois"
    if o["promo"] and o["prixRegulier"] > o["prix"]:
        j, m = int(o["promoFin"][8:10]), int(o["promoFin"][5:7])
        mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"][m - 1]
        t += f" — prix de lancement, au lieu de {dollars(o['prixRegulier'])}, jusqu'au {'1er' if j == 1 else j} {mois} {o['promoFin'][:4]}"
    return t + f". Une conversation : jusqu'à {o['toursMax']} échanges, puis le bilan."


def page(f):
    adresse = url("/modules-autonomes/" + f["dossier"] + "/")
    carre = qr.svg(adresse, cote=150).replace("Code QR de la séance", "Code QR : " + f["nom"])
    chiffres = "".join(f'<div class="ch"><b>{e(n)}</b><span>{e(t)}</span></div>' for n, t in f["chiffres"])
    temps = "".join(f'<li><b>{e(a)}.</b> {e(b)}</li>' for a, b in f["temps"])
    return f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex"><title>{e(f['nom'])} — fiche</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@800;900&family=IBM+Plex+Sans:wght@400;600;700&display=swap">
<style>
/* Une page lettre, en noir et gris ; seule la capture du téléphone est en couleur. */
@page{{size:letter;margin:13mm 14mm}}
:root{{--encre:#111;--texte:#333;--gris:#666;--filet:#BBB}}
*{{box-sizing:border-box}}
html{{background:#fff}}
body{{margin:0 auto;max-width:7.6in;color:var(--texte);font:11pt/1.45 'IBM Plex Sans',Arial,sans-serif;background:#fff}}
h1,h2,b{{color:var(--encre)}}
h1,h2{{font-family:'Nunito',Arial,sans-serif;margin:0}}
.barre{{display:flex;align-items:baseline;gap:12px;border-bottom:1.5pt solid var(--encre);padding-bottom:7pt}}
.nom{{font-family:'Nunito',sans-serif;font-weight:900;font-size:20pt;letter-spacing:-.035em;color:var(--encre)}}
.fr-i{{position:relative;display:inline-block}}
.fr-point{{position:absolute;left:1px;top:1px;width:5px;height:5px;border-radius:999px;background:var(--encre)}}
.desc{{font-size:9.5pt;color:var(--gris)}}
.corps{{display:grid;grid-template-columns:1fr 2.35in;gap:22pt;margin-top:16pt;align-items:start}}
.sur{{font-size:8.5pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gris)}}
h1{{font-size:27pt;font-weight:900;letter-spacing:-.02em;line-height:1.05;margin-top:4pt}}
.accroche{{font-size:12.5pt;margin:9pt 0 0;color:var(--encre)}}
.chiffres{{display:grid;grid-template-columns:repeat(3,1fr);gap:8pt;margin-top:14pt}}
.ch{{border-top:1pt solid var(--encre);padding-top:5pt}}
.ch b{{display:block;font-family:'Nunito',sans-serif;font-size:20pt;font-weight:900;line-height:1}}
.ch span{{display:block;font-size:8.5pt;line-height:1.3;margin-top:3pt;color:var(--gris)}}
h2{{font-size:13pt;font-weight:900;margin-top:15pt;border-bottom:.75pt solid var(--filet);padding-bottom:3pt}}
ul{{margin:7pt 0 0;padding-left:15pt}} li{{margin-top:4pt}}
.prix{{margin-top:7pt;font-size:10.5pt}}
.cadre{{border:1.25pt solid var(--encre);border-radius:8pt;padding:10pt 12pt;margin-top:8pt}}
.tel{{border:7px solid #111;border-radius:26px;overflow:hidden;background:#111}}
.tel img{{display:block;width:100%;height:auto}}
.legende{{font-size:8.5pt;color:var(--gris);text-align:center;margin-top:5pt}}
.depart{{margin-top:12pt;border:1.25pt solid var(--encre);border-radius:8pt;padding:9pt 10pt;text-align:center;font-size:9.5pt;line-height:1.35}}
.depart svg{{display:block;width:1.3in;height:1.3in;margin:0 auto 6pt}}
.depart p{{margin:0}}
.url{{display:block;margin-top:3pt;font-family:ui-monospace,Menlo,monospace;font-size:8pt;word-break:break-all}}
.pied{{margin-top:16pt;font-size:8pt;color:var(--gris);border-top:.75pt solid var(--filet);padding-top:5pt}}
@media screen{{body{{padding:24px 16px}}}}
@media (max-width:640px){{.corps{{grid-template-columns:1fr}} .chiffres{{grid-template-columns:1fr}}}}
</style></head>
<body>
<div class="barre"><span class="nom" role="img" aria-label="francis">franc<span class="fr-i">ı<span class="fr-point"></span></span>s</span>
  <span class="desc">Aide à l'apprentissage des langues</span></div>
<div class="corps">
  <div>
    <p class="sur">{e(f['sur'])}</p>
    <h1>{e(f['nom'])}</h1>
    <p class="accroche">{e(f['accroche'])}</p>
    <div class="chiffres">{chiffres}</div>
    <h2>Comment ça marche</h2>
    <ul>{temps}</ul>
    <h2>Ce que ça coûte</h2>
    <div class="cadre"><b>Gratuit :</b> tout, sauf « {e(f['paye'])} ». Dans le navigateur du téléphone, sans compte ni mot de passe.
      <p class="prix"><b>« {e(f['paye'])} » :</b> {e(offre_txt())} Paiement par carte chez Stripe ; le code s'affiche tout de suite.</p></div>
  </div>
  <div><div class="tel"><img src="{e(f['capture'])}" alt="L'écran d'accueil de l'application"></div>
    <p class="legende">L'application, sur un téléphone</p>
    <div class="depart">{carre}<p><b>Pour commencer :</b> visez ce code avec l'appareil photo du téléphone, ou tapez
      <span class="url">{e(adresse.replace('https://', ''))}</span></p></div></div>
</div>
<p class="pied">Vendu par Boucledidactique · support@edufrancis.ca · Conditions de vente : portail.edufrancis.ca/conditions-de-vente.html</p>
</body></html>
"""


def imprimer(dossier, port):
    sortie = RACINE / "modules-autonomes" / dossier / "fiche.pdf"
    profil = pathlib.Path("/tmp") / f"fiche-pdf-{time.time_ns()}"
    debut = sortie.stat().st_mtime if sortie.exists() else 0
    proc = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--mute-audio",
                             f"--user-data-dir={profil}", "--virtual-time-budget=6000", f"--print-to-pdf={sortie}",
                             f"http://localhost:{port}/modules-autonomes/{dossier}/fiche.html"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(90):   # Chrome écrit le PDF puis tarde parfois à rendre la main : on attend le fichier
        time.sleep(1)
        if sortie.exists() and sortie.stat().st_mtime > debut and sortie.stat().st_size > 10000:
            time.sleep(2)
            break
    proc.kill()
    b = sortie.read_bytes()
    boites = set(re.findall(rb"/MediaBox\s*\[\s*0 0 ([\d.]+) ([\d.]+)", b))
    pages = len(re.findall(rb"/Type\s*/Page[^s]", b))
    assert boites == {(b"612", b"792")}, f"{dossier} : format inattendu {boites}"
    assert pages == 1, f"{dossier} : {pages} pages — la fiche doit tenir sur une seule"
    return len(b) // 1024


if __name__ == "__main__":
    port = next((a.split("=")[1] for a in sys.argv if a.startswith("--port=")), "5497")
    for f in FICHES:
        d = RACINE / "modules-autonomes" / f["dossier"]
        assert (d / f["capture"]).exists(), f["capture"]
        (d / "fiche.html").write_text(page(f), encoding="utf-8")
        ligne = f"modules-autonomes/{f['dossier']}/fiche.html"
        if "--sans-pdf" not in sys.argv:
            ligne += f" + fiche.pdf ({imprimer(f['dossier'], port)} Ko, 1 page lettre)"
        print(ligne)
