"""Le code QR d'une application, prêt à poser dans un dépliant ou une galerie.

    from qr_bloc import bloc
    bloc("/modules-autonomes/toronto/", "Une semaine à Toronto")

Demande de Daniel, 2 oct. 2026 : « ajoute le code barre au document de
présentation ». Le carré vient de qr.py (bibliothèque standard, aucun service
tiers) et pointe vers l'adresse publique complète : un dépliant imprimé n'a pas
d'adresse relative. Il reste visible à l'impression — c'est là qu'il sert le
plus — et se masque sous 640 px, où l'on est déjà sur le téléphone.
"""
import html, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import qr  # noqa: E402

DOMAINE = "https://portail.edufrancis.ca"


def url(chemin):
    return DOMAINE + "/" + chemin.strip("/") + "/"


def bloc(chemin, nom, cote=112):
    adresse = url(chemin)
    carre = qr.svg(adresse, cote=cote).replace("Code QR de la séance", "Code QR : " + nom)
    lisible = html.escape(adresse.replace("https://", ""))
    return f"""<div class="qrb">{carre}<p><b>Sur votre téléphone</b><br>Visez ce code avec l'appareil photo, ou tapez
  <span class="qrb-url">{lisible}</span></p></div>
<p class="qrb-pdf"><a href="/{chemin.strip('/')}/fiche.pdf" target="_blank" rel="noopener">La fiche d'une page, à imprimer (PDF)</a></p>
<style>.qrb{{display:flex;align-items:center;gap:14px;margin-top:16px;max-width:430px}}
.qrb svg{{flex:none;border-radius:6px;border:1px solid #E2E1DC}}
.qrb p{{margin:0;font-size:14px;line-height:1.4}}
.qrb-url{{font-family:ui-monospace,Menlo,monospace;font-size:12.5px;word-break:break-all}}
@media (max-width:640px){{.qrb{{display:none}}}}
.qrb-pdf{{margin:10px 0 0;font-size:14px}}
@media print{{.qrb-pdf{{display:none}}}}
@media print{{.qrb{{display:flex!important;break-inside:avoid}}}}</style>"""
