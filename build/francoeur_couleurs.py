#!/usr/bin/env python3
"""Les couleurs des cours en entreprise — la page de propositions.

    python3 build/francoeur_couleurs.py   # → assets/presentations/francoeur-couleurs.html

Produite, jamais éditée. Daniel, 24 septembre 2026 : le système de design de
francis est gardé, mais ces cours-là sont « différents » — le mauve s'en va,
le fond change. Chaque palette est montrée sur un VRAI écran de la trousse
(téléphone), et ses contrastes sont CALCULÉS ici : une palette qui ne passe pas
4,5:1 sur le texte ne se construit pas.

Ce qui ne bouge pas, quelle que soit la palette : le nom « francis » et son
point sur le « i » (la marque), le vert et le rouge de la rétroaction (juste /
pas juste), qui portent toujours un mot et un signe en plus de la couleur.
"""
import html, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "francoeur-couleurs.html"
E = html.escape

# (clé, nom, idée, jetons)
# jetons : fond (la page), surface (les cartes), encre (texte fort), discret
# (texte d'appui), action (bouton principal), sur_action (son texte), marque
# (le point du « i », le filet de la barre, l'enseigne), halo (fond d'un bloc
# mis en avant : le piège, l'avant-d'entrer), ligne (bordures), ok, non.
PALETTES = [
    ("boutique", "Boutique",
     "L'ivoire d'un sac de papier, l'encre noire d'une étiquette, un bordeaux pour l'enseigne. "
     "Le bouton principal est noir : c'est le code des boutiques de vêtements.",
     dict(fond="#F6F1E9", surface="#FFFDF8", encre="#1E1B18", discret="#5E574F",
          action="#1E1B18", sur_action="#FFFFFF", marque="#7A2433", titre="#7A2433", halo="#F3E4D6",
          ligne="#E3D8C8", ok="#2E6B3F", non="#B3261E")),
    ("denim", "Denim",
     "Le bleu d'un jean et l'orange de sa surpiqûre. Un fond gris-bleu, frais, qui ne ressemble à "
     "aucun écran de francis.",
     dict(fond="#EDF1F5", surface="#FFFFFF", encre="#17212E", discret="#4F5B6A",
          action="#2B4A78", sur_action="#FFFFFF", marque="#C8692A", titre="#2B4A78", halo="#FBE9DC",
          ligne="#D5DDE6", ok="#1F7A4D", non="#B42318")),
    ("sauge", "Sauge et terracotta",
     "Une vitrine d'automne : fond lin, titres sauge, action terracotta. Chaud sans être criard.",
     dict(fond="#F1F0E8", surface="#FFFFFF", encre="#1F2620", discret="#50584F",
          action="#A6482A", sur_action="#FFFFFF", marque="#4E6B52", titre="#4E6B52", halo="#F6E3D8",
          ligne="#DCDACB", ok="#2F6B3A", non="#9F1D35")),
    ("vitrine", "Vitrine",
     "Noir, blanc, et une seule couleur vive — la moutarde d'une étiquette de solde. "
     "Le plus « magasin » des quatre ; la moutarde ne porte jamais de texte blanc.",
     dict(fond="#F4F4F2", surface="#FFFFFF", encre="#111111", discret="#55565A",
          action="#111111", sur_action="#FFFFFF", marque="#B07D05", titre="#111111", halo="#FCEFC7",
          ligne="#DADAD6", ok="#17744A", non="#B42318")),
]
ROLES = [("fond", "Le fond de la page"), ("surface", "Les cartes"), ("encre", "Le texte"),
         ("discret", "Le texte d'appui"), ("action", "Le bouton principal"),
         ("marque", "L'enseigne, le point du « i », le filet"), ("halo", "Un bloc mis en avant"),
         ("ok", "Juste"), ("non", "Pas juste")]


def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contraste(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def controles(j):
    """Les paires qui doivent passer 4,5:1 (texte) ou 3:1 (repère graphique)."""
    return [
        ("texte sur le fond", contraste(j["encre"], j["fond"]), 4.5),
        ("texte d'appui sur le fond", contraste(j["discret"], j["fond"]), 4.5),
        ("texte d'appui sur un bloc mis en avant", contraste(j["discret"], j["halo"]), 4.5),
        ("bouton principal", contraste(j["sur_action"], j["action"]), 4.5),
        ("rétroaction « pas juste » sur carte", contraste(j["non"], j["surface"]), 4.5),
        ("rétroaction « juste » sur carte", contraste(j["ok"], j["surface"]), 4.5),
        ("point du « i » sur blanc", contraste(j["marque"], "#FFFFFF"), 3.0),
        ("enseigne et descripteur sur le fond", contraste(j["titre"], j["fond"]), 4.5),
    ]


def maquette(k, j):
    img = "/assets/interactive/francoeur/croquis/{}.jpg"
    carte = lambda a, pastille, mot, t, faux=False: (
        f'<div class="m-opt{" m-faux" if faux else ""}"><img src="{img.format(a)}" alt="">'
        f'<span class="m-attr"><i style="background:{pastille}"></i><b>{t}</b></span>'
        f'<span class="m-cmot">{mot} · {t}</span></div>')
    return f"""<div class="tel" style="{';'.join(f'--p-{a}:{b}' for a, b in j.items())};--marque-600:{j['marque']}">
  <div class="fr-barre"><div class="fr-barre__in">
    <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">Aide à l'apprentissage du français</span></span>
  </div></div>
  <div class="m-page">
    <p class="m-enseigne">Maison Francœur</p>
    <p class="m-h1">Ce que le client veut</p>
    <p class="m-appui">Lo que quiere el cliente</p>
    <div class="m-boutons"><span class="m-btn m-pri">▶ Réécouter</span><span class="m-btn">Plus lentement</span></div>
    <div class="m-choix">
      {carte("pantalon", "#8A8D91", "gris", "L", True)}
      {carte("jogging", "#111111", "noir", "L")}
    </div>
    <p class="m-non">✕ Pas tout à fait. Essayez encore.</p>
    <p class="m-appui">Pas la bonne taille</p>
    <div class="m-halo"><b>Attention</b> — « une veste », au Québec, n'a pas de manches.</div>
    <p class="m-ok">✓ Bien joué !</p>
  </div>
</div>"""


def page():
    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Maison Francœur — les couleurs</title>", tete)
    tete = tete.replace("</head>", '<link rel="stylesheet" href="/assets/design-system/marque-francis.css">\n</head>', 1)
    tete = tete.replace("</style>", CSS + "</style>", 1)
    blocs = []
    for k, nom, idee, j in PALETTES:
        c = controles(j)
        rates = [x for x in c if x[1] < x[2]]
        assert not rates, f"{nom} : " + ", ".join(f"{a} {v:.2f}:1 < {s}" for a, v, s in rates)
        nuancier = "".join(f'<li><i style="background:{j[r]}"></i><span><b>{E(lib)}</b><code>{j[r]}</code></span></li>'
                           for r, lib in ROLES)
        mesures = "".join(f"<li>{E(a)} <b>{v:.1f}:1</b></li>" for a, v, _s in c)
        blocs.append(f"""
<section class="pal" id="{k}">
  <div class="pal-texte">
    <h2>{E(nom)}</h2>
    <p>{E(idee)}</p>
    <ul class="nuancier">{nuancier}</ul>
    <details><summary>Les contrastes, mesurés</summary><ul class="mesures">{mesures}</ul></details>
    <fieldset class="choix-pal" data-k="{k}"><legend>Votre avis</legend>
      <label><input type="radio" name="v-{k}" value="garder"> Celle-ci</label>
      <label><input type="radio" name="v-{k}" value="retravailler"> À retravailler</label>
      <label><input type="radio" name="v-{k}" value="non"> Non</label>
      <textarea rows="2" placeholder="Ce que je changerais…" data-n="{k}"></textarea>
    </fieldset>
  </div>
  {maquette(k, j)}
</section>""")
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Maison Francœur &middot; les couleurs</p>
<h1>D'autres couleurs pour les cours en entreprise</h1>
<p class="chapeau">Ces cours ne sont pas ceux du portail : ils se donnent à des employés, au plancher d'un
commerce. Quatre palettes pour les distinguer. <strong>Le mauve s'en va</strong> : le point du « i », le
filet de la barre et l'enseigne prennent la couleur de la palette. Ce qui reste de francis : le nom, son
point, la police Nunito, et le vert et le rouge de la rétroaction — toujours accompagnés d'un signe et d'un mot.
Chaque maquette est un vrai écran de la trousse, au format téléphone, et chaque contraste est mesuré.</p>
{''.join(blocs)}
<section class="decision">
  <h2>Ce que vous voulez</h2>
  <textarea id="general" rows="3" placeholder="Une autre idée, un mélange de deux palettes, une couleur à éviter…"></textarea>
  <p><button type="button" class="btn-export" id="exporter">Exporter mes choix</button> <span id="copie" aria-live="polite"></span></p>
  <pre id="sortie" hidden></pre>
</section>
<div class="pied"><p>Page produite par <code>build/francoeur_couleurs.py</code> — ne pas l'éditer.</p></div>
</div>
<script>
const CLE = 'francoeur-couleurs';
const lire = () => {{ try {{ return JSON.parse(localStorage.getItem(CLE) || '{{}}'); }} catch (e) {{ return {{}}; }} }};
const garder = o => {{ try {{ localStorage.setItem(CLE, JSON.stringify(o)); }} catch (e) {{}} }};
const etat = lire();
document.querySelectorAll('.choix-pal').forEach(f => {{
  const k = f.dataset.k, e = etat[k] || {{}};
  f.querySelectorAll('input').forEach(i => {{ i.checked = e.avis === i.value; i.onchange = () => {{ const s = lire(); s[k] = Object.assign(s[k] || {{}}, {{avis: i.value}}); garder(s); }}; }});
  const t = f.querySelector('textarea'); t.value = e.note || '';
  t.oninput = () => {{ const s = lire(); s[k] = Object.assign(s[k] || {{}}, {{note: t.value}}); garder(s); }};
}});
const g = document.getElementById('general'); g.value = etat._general || '';
g.oninput = () => {{ const s = lire(); s._general = g.value; garder(s); }};
document.getElementById('exporter').onclick = async () => {{
  const txt = JSON.stringify({{page: 'francoeur-couleurs', choix: lire()}}, null, 1);
  const pre = document.getElementById('sortie'); pre.textContent = txt; pre.hidden = false;
  try {{ await navigator.clipboard.writeText(txt); document.getElementById('copie').textContent = 'Copié : recollez-le dans la conversation.'; }}
  catch (e) {{ document.getElementById('copie').textContent = 'Copiez le texte ci-dessous.'; }}
}};
</script>
</body></html>"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {len(PALETTES)} palettes, contrastes vérifiés")


CSS = """
.pal{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:28px;align-items:start;padding:26px 0;border-top:1px solid var(--line,#E4E2DC)}
.pal h2{margin:0 0 6px}
.nuancier{list-style:none;padding:0;margin:12px 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:8px}
.nuancier li{display:flex;gap:10px;align-items:center;font-size:14px}
.nuancier i{flex:none;width:34px;height:34px;border-radius:8px;border:1px solid rgba(0,0,0,.12)}
.nuancier b{display:block;font-weight:700}
.nuancier code{font-size:12px;color:#5E5E5E}
.mesures{font-size:14px;margin:6px 0 0;padding-left:18px}
.choix-pal{border:1px solid var(--line,#E4E2DC);border-radius:12px;padding:10px 14px;margin-top:12px;display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.choix-pal legend{font-weight:800;padding:0 6px}
.choix-pal label{display:flex;gap:6px;align-items:center;min-height:44px;cursor:pointer}
.choix-pal textarea,.decision textarea{width:100%;font:inherit;border-radius:10px;border:1px solid #CFCBC2;padding:8px}
.decision{padding:26px 0;border-top:1px solid var(--line,#E4E2DC)}
.decision pre{white-space:pre-wrap;background:#F4F3EF;padding:10px;border-radius:8px;font-size:13px}
.btn-export{font:inherit;font-weight:700;cursor:pointer;background:#1E1B18;color:#fff;border:0;border-radius:10px;padding:10px 16px;min-height:44px}
/* La maquette : un écran de téléphone, peint par les jetons de SA palette. */
.tel{width:340px;max-width:100%;border-radius:26px;border:8px solid #1A1A1A;overflow:hidden;background:var(--p-fond);color:var(--p-encre);box-shadow:0 10px 30px rgba(0,0,0,.12)}
.tel .fr-barre{background:#FFFFFF;border-bottom:2px solid var(--p-marque)}
.tel .fr-barre__in{padding:10px 14px}
.tel .fr-lockup{font-size:22px}
.tel .fr-desc{color:var(--p-titre)}
/* Sous 480 px, le vrai écran ne garde que le nom : la maquette fait pareil. */
.tel .fr-desc,.tel .fr-trait{display:none}
.m-page{padding:14px 14px 18px}
.m-enseigne{margin:0;font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--p-titre)}
.m-h1{margin:2px 0 0;font-size:22px;font-weight:900;color:var(--p-encre)}
.m-appui{margin:2px 0 0;font-size:13px;color:var(--p-discret)}
.m-boutons{display:flex;gap:12px;margin:12px 0}
.m-btn{display:inline-flex;align-items:center;min-height:44px;padding:0 14px;border-radius:12px;border:1px solid var(--p-ligne);background:var(--p-surface);font-weight:800;font-size:14px;color:var(--p-encre)}
.m-pri{background:var(--p-action);border-color:var(--p-action);color:var(--p-sur_action)}
.m-choix{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.m-opt{background:var(--p-surface);border:2px solid var(--p-ligne);border-radius:14px;padding:8px;text-align:center}
.m-opt img{width:100%;aspect-ratio:1/1;object-fit:contain;filter:grayscale(1);background:#fff;border-radius:8px}
.m-faux{border-color:var(--p-non)}
.m-attr{display:flex;gap:6px;justify-content:center;align-items:center;margin-top:4px}
.m-attr i{width:22px;height:22px;border-radius:50%;border:1px solid rgba(0,0,0,.15)}
.m-attr b{border:1.5px solid var(--p-encre);border-radius:5px;padding:0 5px;font-size:12px}
.m-cmot{display:block;font-size:13px;font-weight:700;margin-top:2px}
.m-non{margin:12px 0 0;font-weight:800;color:var(--p-non)}
.m-ok{margin:10px 0 0;font-weight:800;color:var(--p-ok)}
.m-halo{margin-top:12px;background:var(--p-halo);border-left:4px solid var(--p-marque);border-radius:10px;padding:10px 12px;font-size:14px;color:var(--p-encre)}
@media (max-width:760px){.pal{grid-template-columns:1fr}.tel{margin:0 auto}}
"""

if __name__ == "__main__":
    page()
