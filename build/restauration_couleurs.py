#!/usr/bin/env python3
"""Les couleurs de Chez Jocelyne — la page de propositions.

    python3 build/restauration_couleurs.py   # → assets/presentations/restauration/restauration-couleurs.html

Produite, jamais éditée. Copie de build/francoeur_couleurs.py (troisième
trousse : la palette de chaque trousse se choisit sur la même page). La palette
« brique » a été posée à l'étape 1 comme PROVISOIRE (30 sept. 2026) ; Daniel
demande ce soir-là de la trancher, avec un audit de design en parallèle.

Chaque palette est montrée sur un VRAI écran de la trousse (la consigne du chef,
la règle d'allergie), au format téléphone, et ses contrastes sont CALCULÉS : une
palette qui ne passe pas ne se construit pas. Une mesure de plus qu'à Francœur :
l'ÉCART entre le bouton principal et le rouge « pas juste » — au restaurant, une
action rouge brique se confond avec l'erreur.

Ce qui ne bouge pas : le nom « francis » et son point (la marque), le vert et le
rouge de la rétroaction, toujours accompagnés d'un signe et d'un mot.
"""
import html, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "restauration" / "restauration-couleurs.html"
E = html.escape

# (clé, nom, idée, jetons)
# jetons : fond (la page), surface (les cartes), encre (texte fort), discret
# (texte d'appui), action (bouton principal), sur_action (son texte), marque
# (le point du « i », le filet de la barre, l'enseigne), halo (fond d'un bloc
# mis en avant : le piège, l'avant-d'entrer), ligne (bordures), ok, non.
# ── Tour 1 (30 sept. 2026) : cinq palettes. Daniel : « brique » à retravailler (« je changerais le
# fond de la page »), les quatre autres non. Gardé pour mémoire.
PALETTES_TOUR_1 = [
    ("brique", "Brique (l'actuelle)",
     "Celle posée à l'étape 1 : fond crème, action et enseigne brique, orange pour les pièges. Chaude, mais le "
     "bouton principal est proche du rouge de l'erreur.",
     dict(fond="#F5F0EA", surface="#FFFFFF", encre="#241A14", discret="#5E5046",
          action="#8A2E1C", sur_action="#FFFFFF", marque="#C8692A", titre="#8A2E1C", halo="#FBE9DC",
          ligne="#E4DAD0", ok="#1F7A4D", non="#B42318")),
    ("comptoir", "Comptoir",
     "Le casse-croûte d'ici : banquettes sarcelle, nappe crème, une pointe de tomate pour l'enseigne. "
     "L'action n'est ni rouge ni verte : elle ne se confond avec aucune rétroaction.",
     dict(fond="#F3F1EA", surface="#FFFFFF", encre="#16242A", discret="#4E5B60",
          action="#0E6E6B", sur_action="#FFFFFF", marque="#C4502A", titre="#0E6E6B", halo="#FBE5DA",
          ligne="#DAD8CC", ok="#1F7A4D", non="#B42318")),
    ("erable", "Érable",
     "Le déjeuner du dimanche : crème, brun de sirop pour l'action, ambre pour l'enseigne. Le plus « Chez "
     "Jocelyne » des cinq ; l'ambre ne porte jamais de texte blanc.",
     dict(fond="#F6F0E4", surface="#FFFDF8", encre="#2A1E14", discret="#5F5244",
          action="#5B3A1E", sur_action="#FFFFFF", marque="#B87A12", titre="#5B3A1E", halo="#F8EAD0",
          ligne="#E5DAC6", ok="#2E6B3F", non="#B3261E")),
    ("inox", "Inox",
     "La cuisine professionnelle : acier clair, anthracite pour l'action, orange de flamme pour l'enseigne. "
     "Sobre, lisible dans un éclairage dur.",
     dict(fond="#EEF0F1", surface="#FFFFFF", encre="#151B21", discret="#4D5660",
          action="#1F2A33", sur_action="#FFFFFF", marque="#D0691C", titre="#1F2A33", halo="#FBE7D6",
          ligne="#D6DADE", ok="#1F7A4D", non="#B42318")),
    ("marche", "Marché",
     "Une épicerie fine : fond lin, prune pour l'action, moutarde pour l'enseigne. Plus élégant, un peu moins "
     "« cuisine ».",
     dict(fond="#F2EFE8", surface="#FFFFFF", encre="#221A22", discret="#5A4F58",
          action="#5A2E4F", sur_action="#FFFFFF", marque="#B07D05", titre="#5A2E4F", halo="#FBEFC9",
          ligne="#DDD7CB", ok="#1F7A4D", non="#B42318")),
]

# ── Tour 2 : la BRIQUE, sur quatre fonds. Deux corrections communes, tirées de la mesure et de
# l'audit de design : le rouge de l'erreur passe au cramoisi #D12F4B (la brique et l'ancien rouge
# étaient trop proches : 6° de teinte, 7 points de clarté) ; les bordures sont plus marquées (les
# cartes blanches se détachaient mal du fond, 1,13:1).
_BRIQUE = dict(surface="#FFFFFF", encre="#241A14", discret="#5E5046", action="#8A2E1C", sur_action="#FFFFFF",
               marque="#C8692A", titre="#8A2E1C", halo="#FBE9DC", ok="#1F7A4D", non="#D12F4B")
PALETTES = [
    ("pierre", "Brique sur pierre",
     "Un gris chaud, neutre, comme un comptoir de béton poli. Le crème disparaît ; la brique ressort mieux.",
     dict(_BRIQUE, fond="#EEEDEA", ligne="#D4D0C8")),
    ("sable", "Brique sur sable",
     "Un beige plus soutenu que l'actuel : plus chaud, et les cartes blanches s'en détachent le mieux.",
     dict(_BRIQUE, fond="#EFE8DD", ligne="#D8CCBB")),
    ("papier", "Brique sur papier",
     "Presque blanc, un peu froid : l'écran le plus clair et le plus net ; les cartes tiennent par leur bordure.",
     dict(_BRIQUE, fond="#F7F7F5", ligne="#D9D6D0")),
    ("sauge", "Brique sur sauge",
     "Un gris légèrement vert, comme un mur de cuisine : la brique et l'orange y sont complémentaires.",
     dict(_BRIQUE, fond="#ECEFEA", ligne="#CFD5CC")),
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


def ecart_teinte(a, b):
    """(écart de teinte en degrés, écart de clarté en points) entre deux couleurs. Une action se lit
    comme l'erreur quand les deux sont petits (même teinte ET même clarté) : un brun foncé, bien que
    voisin en teinte, ne se confond pas avec un rouge vif."""
    import colorsys
    la = colorsys.rgb_to_hls(*[int(a[i:i + 2], 16) / 255 for i in (1, 3, 5)])
    lb = colorsys.rgb_to_hls(*[int(b[i:i + 2], 16) / 255 for i in (1, 3, 5)])
    d = abs(la[0] - lb[0]) * 360 % 360
    return min(d, 360 - d), abs(la[1] - lb[1]) * 100


def maquette(k, j):
    img = "/assets/interactive/restaurant/croquis/{}.jpg"
    carte = lambda a, faux=False: (f'<div class="m-opt{" m-faux" if faux else ""}"><img src="{img.format(a)}" alt=""></div>')
    return f"""<div class="tel" style="{';'.join(f'--p-{a}:{b}' for a, b in j.items())};--marque-600:{j['marque']}">
  <div class="fr-barre"><div class="fr-barre__in">
    <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">Aide à l'apprentissage du français</span></span>
  </div></div>
  <div class="m-page">
    <p class="m-enseigne">Chez Jocelyne</p>
    <p class="m-h1">La consigne du chef</p>
    <p class="m-appui">La instrucción del chef</p>
    <div class="m-boutons"><span class="m-btn m-pri">Réécouter</span><span class="m-btn">Plus lentement</span></div>
    <p class="m-q">Où vont les assiettes sales ?</p>
    <div class="m-choix">{carte("evier", True)}{carte("lave-vaisselle")}</div>
    <p class="m-non">✕ Pas tout à fait. Essayez encore.</p>
    <p class="m-ok">✓ Bien joué !</p>
    <div class="m-halo"><b>L'allergie — la règle</b><br>1. Si ce n'est pas clair, je fais répéter : « Allergique à quoi ? »</div>
  </div>
</div>"""


def page():
    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Chez Jocelyne — les couleurs</title>", tete)
    tete = tete.replace("</head>", '<link rel="stylesheet" href="/assets/design-system/marque-francis.css">\n</head>', 1)
    tete = tete.replace("</style>", CSS + "</style>", 1)
    blocs = []
    for k, nom, idee, j in PALETTES:
        c = controles(j)
        rates = [x for x in c if x[1] < x[2]]
        assert not rates, f"{nom} : " + ", ".join(f"{a} {v:.2f}:1 < {s}" for a, v, s in rates)
        nuancier = "".join(f'<li><i style="background:{j[r]}"></i><span><b>{E(lib)}</b><code>{j[r]}</code></span></li>'
                           for r, lib in ROLES)
        et, ec = ecart_teinte(j["action"], j["non"])
        proche = et < 25 and ec < 15
        mesures = "".join(f"<li>{E(a)} <b>{v:.1f}:1</b></li>" for a, v, _s in c) + (
            f"<li>bouton principal et « pas juste » : teinte <b>{et:.0f}°</b>, clarté <b>{ec:.0f} points</b>"
            f"{' — trop proches : l’action se lit comme l’erreur' if proche else ''}</li>")
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
<a class="retour" href="/presentations.html#restauration"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Chez Jocelyne &middot; les couleurs</p>
<h1>La brique, deuxième tour : le fond</h1>
<p class="chapeau"><b>Au premier tour, vous avez gardé la brique, avec un autre fond.</b> La voici sur quatre fonds.
Deux corrections communes : le rouge de l'erreur devient un <b>cramoisi</b> (l'ancien se confondait avec la brique
du bouton), et les bordures sont un peu plus marquées pour que les cartes se détachent. </p>
{''.join(blocs)}
<section class="decision">
  <h2>Ce que vous voulez</h2>
  <textarea id="general" rows="3" placeholder="Une autre idée, un mélange de deux palettes, une couleur à éviter…"></textarea>
  <p><button type="button" class="btn-export" id="exporter">Exporter mes choix</button> <span id="copie" aria-live="polite"></span></p>
  <pre id="sortie" hidden></pre>
</section>
<div class="pied"><p>Page produite par <code>build/restauration_couleurs.py</code> — ne pas l'éditer.</p></div>
</div>
<script>
const CLE = 'restauration-couleurs-tour2';
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
  const txt = JSON.stringify({{page: 'restauration-couleurs', tour: 2, choix: lire()}}, null, 1);
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
.m-opt img{width:100%;aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:8px}
.m-q{margin:4px 0 10px;font-weight:800;text-align:center;color:var(--p-encre)}
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
