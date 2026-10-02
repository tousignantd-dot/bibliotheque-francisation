#!/usr/bin/env python3
"""La galerie publique des produits autonomes — une vitrine, une carte par application.

    python3 build/galerie_produits.py     # → modules-autonomes/galerie/index.html

Demande de Daniel, 2 oct. 2026 : « une galerie publique avec tous les produits
autonomes ». Produite, jamais écrite à la main. Ajouter un produit = une entrée
dans PRODUITS ci-dessous (et une image).

Les images : les captures des dépliants quand le produit en a ; sinon une
capture rangée dans modules-autonomes/galerie/ (Montréal, Chez Jocelyne).
Le prix n'est PAS écrit ici : la page le lit à l'ouverture sur
/api/pelerins/offre, qui fait foi (pelerins.offre(), réglable sans déployer).
Sans réponse, la carte dit seulement « Conversations jouées : payantes ».

Le vocabulaire de l'apprenant : « assistance », jamais « IA ».
"""
import html, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
import qr  # noqa: E402  (le générateur maison, bibliothèque standard)

DOMAINE = "https://portail.edufrancis.ca"
SORTIE = RACINE / "modules-autonomes" / "galerie" / "index.html"
INDEXER = False   # passe à True au lancement, avec les applications (liste de mise en service)

# (id, famille, nom, langue, accroche, ce qu'on y fait, image, adresse, dépliant, état)
# état : "vente" (application gratuite, conversations jouées payantes), "gratuit", "preparation".
PRODUITS = [
    ("compostelle", "voyage", "En route vers Compostelle", "Espagnol",
     "L'espagnol du pèlerin francophone, étape par étape sur le Camino francés.",
     ["Dix étapes du chemin, des mots aux phrases utiles", "Une credencial qu'on tamponne en avançant",
      "Parler librement avec les gens du chemin"],
     "../compostelle/depliant/accueil.jpg", "../compostelle/", "../compostelle/presentation.html", "vente"),
    ("toronto", "voyage", "Une semaine à Toronto", "Anglais",
     "L'anglais du touriste francophone, pour une semaine à Toronto.",
     ["Dix lieux de la ville, du café au marché", "Une semaine jouée : commander, demander, s'expliquer",
      "Ma trousse : urgences, pourboires, phrases à montrer, même hors ligne"],
     "../toronto/depliant/accueil.jpg", "../toronto/", "../toronto/presentation.html", "vente"),
    ("montreal", "voyage", "Montréal en poche", "Français · English · Español",
     "Un guide de Montréal dans le téléphone : les lieux, les quartiers, ce qu'on y mange.",
     ["28 lieux en croquis, avec l'audioguide", "Quatre circuits à pied et la carte",
      "Un passeport à tampons, un par lieu visité"],
     "montreal.jpg", "../montreal/", "", "gratuit"),
    ("francoeur", "travail", "Maison Francœur", "Français",
     "Pour qui travaille, ou veut travailler, dans un magasin de vêtements.",
     ["Les mots du magasin, rayon par rayon, en croquis", "Une aide dans onze langues, masquée par défaut",
      "Le magasin joué : des clients à servir"],
     "../francoeur-planches/depliant/magasin.jpg", "../francoeur-planches/", "../francoeur-planches/presentation.html", "vente"),
    ("hotel", "travail", "Hôtel Rive-Claire", "Français · English · Español",
     "Pour qui travaille, ou veut travailler, à la réception d'un hôtel.",
     ["Le comptoir en trois langues, à égalité", "Les faux amis d'une langue à l'autre",
      "Le comptoir joué : des clients au comptoir et au téléphone"],
     "../hotel-reception/depliant/comptoir.jpg", "../hotel-reception/", "../hotel-reception/presentation.html", "vente"),
    ("restaurant", "travail", "Chez Jocelyne", "Français",
     "Les mots du restaurant, de la cuisine à la salle, avec une aide en espagnol et en anglais.",
     ["Le poste et douze planches, mot par mot", "Huit exercices, du mot à la consigne du chef"],
     "restaurant.jpg", "../restaurant-planches/", "", "preparation"),
]

# La couleur de chaque carte : celle de l'application elle-même (filet, plaque de l'écran, bouton).
# Le mauve reste à la marque seule. Texte blanc sur chaque teinte : contraste ≥ 4,5:1.
COULEURS = {
    "compostelle": ("#2C5594", "#E3EBF7"),
    "toronto": ("#C8102E", "#FBE7EA"),
    "montreal": ("#B8325A", "#FFE3EA"),
    "francoeur": ("#2B4A78", "#E6ECF4"),
    "hotel": ("#0F5E63", "#DDEDEC"),
    "restaurant": ("#8A2E1C", "#F6E7E1"),
}

FAMILLES = [
    ("voyage", "Pour voyager", "Une langue pour partir : on prépare le voyage chez soi, on le garde dans le téléphone sur place."),
    ("travail", "Pour le travail", "La langue d'un poste, sur les objets et les gestes de ce poste, jusqu'à la situation jouée."),
]

ETATS = {
    "vente": "Application gratuite · conversations jouées payantes",
    "gratuit": "Gratuit",
    "preparation": "En préparation",
}


def e(s):
    return html.escape(s, quote=True)


def carte(p):
    pid, _, nom, langue, accroche, points, image, adresse, depliant, etat = p
    url = DOMAINE + "/modules-autonomes/" + adresse.strip("./") + "/"
    code = qr.svg(url, cote=96).replace("Code QR de la séance", "Code QR : " + nom)
    lis = "".join(f"<li>{e(x)}</li>" for x in points)
    prix = f'<p class="prix" data-prix="{pid}">{e(ETATS[etat])}</p>'
    liens = f'<a class="btn" href="{e(adresse)}">Ouvrir l\'application</a>'
    if depliant:
        liens += f'<a class="btn sec" href="{e(depliant)}">Voir la présentation</a>'
    c, pale = COULEURS[pid]
    return f"""<article class="carte" id="{pid}" style="--c:{c};--c-pale:{pale}">
  <a class="ecran" href="{e(adresse)}" tabindex="-1" aria-hidden="true"><img src="{e(image)}" alt="" loading="lazy" width="520" height="1125"></a>
  <div class="corps">
    <p class="langue">{e(langue)}</p>
    <h3>{e(nom)}</h3>
    <p class="accroche">{e(accroche)}</p>
    <ul>{lis}</ul>
    <p class="etat etat-{etat}">{e(ETATS[etat]) if etat != "vente" else ""}</p>
    {prix if etat == "vente" else ""}
    <div class="bas">
      <div class="liens">{liens}</div>
      <figure class="qr">{code}<figcaption>Scannez pour l'ouvrir sur votre téléphone</figcaption></figure>
    </div>
  </div>
</article>"""


def page():
    sections = []
    for fid, titre, intro in FAMILLES:
        cartes = "\n".join(carte(p) for p in PRODUITS if p[1] == fid)
        sections.append(f'<section class="famille"><h2>{e(titre)}</h2><p class="intro">{e(intro)}</p><div class="grille">{cartes}</div></section>')
    robots = "" if INDEXER else '<meta name="robots" content="noindex">\n'
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{robots}<title>Nos applications</title>
<meta name="description" content="Les applications autonomes de francis : des langues pour voyager et pour travailler, dans le téléphone.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<style>
:root{{--sol:#FAFAF8;--carte:#FFFFFF;--encre:#17181A;--texte:#3A3D40;--gris:#6E7175;--filet:#E2E1DC;
  --mauve:#6B4FBB;--action:#17181A;--action-txt:#FFFFFF;--vert:#0D7A6F;--vert-pale:#DCF2EF;--ambre:#B45309;--ambre-pale:#FBEEDC;--ecran:#EFEEEA}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--sol:#151618;--carte:#1E2023;--encre:#F2F1EE;--texte:#C9CACC;--gris:#9A9DA1;--filet:#33363A;
  --action:#F2F1EE;--action-txt:#17181A;--vert:#5CC6B8;--vert-pale:#173733;--ambre:#F0A55A;--ambre-pale:#3A2A17;--ecran:#2A2C30}}}}
:root[data-theme="dark"]{{--sol:#151618;--carte:#1E2023;--encre:#F2F1EE;--texte:#C9CACC;--gris:#9A9DA1;--filet:#33363A;
  --action:#F2F1EE;--action-txt:#17181A;--vert:#5CC6B8;--vert-pale:#173733;--ambre:#F0A55A;--ambre-pale:#3A2A17;--ecran:#2A2C30}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]) .ecran{{background:color-mix(in srgb,var(--c) 30%,#1E2023)}}
  :root:not([data-theme="light"]) .langue{{color:color-mix(in srgb,var(--c) 45%,#FFFFFF)}}}}
:root[data-theme="dark"] .ecran{{background:color-mix(in srgb,var(--c) 30%,#1E2023)}}
:root[data-theme="dark"] .langue{{color:color-mix(in srgb,var(--c) 45%,#FFFFFF)}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--sol);color:var(--texte);font:15px/1.55 'IBM Plex Sans','Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased}}
h1,h2,h3{{margin:0;font-family:'Nunito',sans-serif;color:var(--encre);text-wrap:balance}}
p,ul{{margin:0}}
.barre{{background:var(--carte);border-bottom:2px solid var(--mauve)}}
.barre-in{{max-width:1120px;margin:0 auto;padding:14px 40px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}}
.nom{{font-family:'Nunito',sans-serif;font-weight:900;font-size:28px;letter-spacing:-.035em;line-height:1;color:var(--encre);text-decoration:none;white-space:nowrap}}
.fr-i{{position:relative;display:inline-block}}
.fr-point{{position:absolute;left:1px;top:2px;width:7px;height:7px;border-radius:999px;background:var(--mauve)}}
.trait{{width:1px;height:24px;background:var(--filet)}}
.desc{{font-size:14px;color:var(--gris)}}
.page{{max-width:1120px;margin:0 auto;padding:0 40px 90px}}
.tete{{padding:56px 0 8px}}
.tete h1{{font-size:44px;font-weight:900;letter-spacing:-.025em;line-height:1.05}}
.tete p{{font-size:18px;max-width:60ch;margin-top:14px}}
.famille{{padding-top:52px}}
.famille h2{{font-size:26px;font-weight:900;border-top:2px solid var(--encre);padding-top:12px}}
.intro{{margin-top:8px;max-width:70ch;color:var(--gris)}}
.grille{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:22px;margin-top:22px}}
.carte{{background:var(--carte);border:1px solid var(--filet);border-top:5px solid var(--c);border-radius:18px;overflow:hidden;display:flex;flex-direction:column}}
.ecran{{display:block;background:var(--c-pale);padding:22px 22px 0;height:300px;overflow:hidden}}
.ecran img{{display:block;width:190px;height:auto;margin:0 auto;border-radius:22px 22px 0 0;border:6px solid #17181A;border-bottom:0;box-shadow:0 8px 24px rgba(0,0,0,.12)}}
.corps{{padding:18px 22px 22px;display:flex;flex-direction:column;gap:10px;flex:1}}
.langue{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--c)}}
.carte h3{{font-size:22px;font-weight:900;letter-spacing:-.015em;line-height:1.15}}
.accroche{{font-size:15px;color:var(--encre)}}
.carte ul{{padding-left:18px;font-size:14px}}
.carte li+li{{margin-top:3px}}
.etat:empty{{display:none}}
.etat,.prix{{font-size:13px;font-weight:600;border-radius:8px;padding:6px 10px;align-self:flex-start}}
.etat-gratuit,.prix{{background:var(--vert-pale);color:var(--vert)}}
.etat-preparation{{background:var(--ambre-pale);color:var(--ambre)}}
.bas{{margin-top:auto;padding-top:6px;display:flex;align-items:flex-end;justify-content:space-between;gap:14px}}
.liens{{display:flex;flex-direction:column;align-items:flex-start;gap:10px}}
.qr{{margin:0;display:flex;flex-direction:column;align-items:center;gap:4px;flex:none}}
.qr svg{{display:block;width:96px;height:96px;border-radius:6px}}
.qr figcaption{{font-size:11px;line-height:1.3;color:var(--gris);text-align:center;max-width:110px}}
.btn{{display:inline-block;padding:10px 16px;border-radius:10px;background:var(--c,var(--action));color:#FFFFFF;font-weight:600;font-size:14px;text-decoration:none}}
.btn.sec{{background:transparent;color:var(--encre);border:1px solid var(--filet)}}
.btn:focus-visible{{outline:3px solid var(--mauve);outline-offset:2px}}
.pied{{margin-top:64px;padding-top:18px;border-top:1px solid var(--filet);font-size:13px;color:var(--gris);display:flex;gap:18px;flex-wrap:wrap}}
.pied a{{color:var(--gris)}}
@media (max-width:640px){{
  .barre-in{{padding:12px 16px}} .trait,.desc{{display:none}}
  .page{{padding:0 16px 64px}} .tete{{padding-top:32px}} .tete h1{{font-size:32px}} .tete p{{font-size:16px}}
  .grille{{grid-template-columns:1fr}} .qr{{display:none}} .ecran{{height:250px}} .ecran img{{width:160px}}
}}
</style>
</head>
<body>
<header class="barre"><div class="barre-in">
  <a class="nom" href="/" aria-label="francis">franc<span class="fr-i">ı<span class="fr-point"></span></span>s</a>
  <span class="trait"></span><span class="desc">Aide à l'apprentissage des langues</span>
</div></header>
<main class="page">
  <div class="tete">
    <h1>Nos applications</h1>
    <p>Des langues pour voyager et pour travailler, dans le téléphone. Sans compte, sans installation : on ouvre et on commence.</p>
  </div>
  {"".join(sections)}
  <footer class="pied">
    <span>Les conversations jouées se font avec un personnage, à l'aide de l'assistance ; le reste de chaque application est gratuit.</span>
    <a href="mailto:support@edufrancis.ca">support@edufrancis.ca</a>
  </footer>
</main>
<script>
(function () {{
  var vente = document.querySelectorAll('[data-prix]');
  if (!vente.length || !window.fetch) return;
  var $ = function (c) {{ return (c / 100).toFixed(2).replace('.', ',') + '\\u00a0$'; }};
  fetch('/api/pelerins/offre').then(function (r) {{ return r.ok ? r.json() : null; }}).then(function (o) {{
    if (!o || !o.prix) return;
    var t = 'Application gratuite · ' + o.conversations + ' conversations jouées : ' + $(o.prix);
    if (o.promo && o.prixRegulier > o.prix) t += ' (au lieu de ' + $(o.prixRegulier) + ')';
    vente.forEach(function (n) {{ n.textContent = t; }});
  }}).catch(function () {{}});
}})();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    for p in PRODUITS:
        img = (SORTIE.parent / p[6]).resolve()
        assert img.exists(), f"image manquante : {img}"
        assert (SORTIE.parent / p[7] / "index.html").resolve().exists(), p[7]
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page(), encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {len(PRODUITS)} produits")
