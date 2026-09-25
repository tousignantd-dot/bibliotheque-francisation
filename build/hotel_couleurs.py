#!/usr/bin/env python3
"""Les couleurs de la réception de l'Hôtel Rive-Claire — la page de propositions.

    python3 build/hotel_couleurs.py   # → assets/presentations/hotellerie-couleurs.html

Produite, jamais éditée. Daniel, 25 septembre 2026 : après le thème francis tel
quel (décision du 24 sept.), il demande d'autres propositions, comme pour la
Maison Francœur (qui a pris Denim). Même page, même contrôle : les contrastes
sont CALCULÉS par `francoeur_couleurs.controles()`, et une palette qui ne passe
pas 4,5:1 sur le texte ne se construit pas.

Ce qui ne bouge pas : le nom « francis » et son point sur le « i », la police
Nunito, le vert et le rouge de la rétroaction (toujours avec un signe et un mot).
"""
import html, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import francoeur_couleurs as FC  # noqa: E402

SORTIE = RACINE / "assets" / "presentations" / "hotellerie-couleurs.html"
E = html.escape

PALETTES = [
    ("hall", "Le hall",
     "Le marine d'un uniforme de réception et le laiton des poignées de porte. Sobre, hôtelier, "
     "un fond ivoire comme le papier à en-tête.",
     dict(fond="#F4F1EA", surface="#FFFFFF", encre="#16202B", discret="#525B66",
          action="#1F3A5F", sur_action="#FFFFFF", marque="#9A7426", titre="#1F3A5F", halo="#F4E9D2",
          ligne="#E2DCCF", ok="#1F7A4D", non="#B42318")),
    ("rive", "Rive-Claire",
     "Le nom de l'hôtel : l'eau et le sable. Sarcelle profonde pour l'action, corail doux pour la "
     "marque, fond sable. Vacances, sans faire carte postale.",
     dict(fond="#F3EFE6", surface="#FFFFFF", encre="#132A2C", discret="#4D5E5F",
          action="#0F5E63", sur_action="#FFFFFF", marque="#C4613A", titre="#0F5E63", halo="#F8E3D8",
          ligne="#DFD8C9", ok="#1F7A4D", non="#B42318")),
    ("chalet", "Chalet",
     "Une auberge des Laurentides : vert sapin, cuivre, fond de lin. Chaud et d'ici.",
     dict(fond="#EFF0EA", surface="#FFFFFF", encre="#1B241E", discret="#4E574F",
          action="#2F5D46", sur_action="#FFFFFF", marque="#A9582A", titre="#2F5D46", halo="#F5E4D6",
          ligne="#D9DBCF", ok="#1F6E3F", non="#A61B2B")),
    ("concierge", "Clés d'or",
     "Le comptoir du concierge : charbon et or, fond perle. Le plus « grand hôtel » des quatre ; "
     "l'or ne porte jamais de texte blanc.",
     dict(fond="#F5F4F1", surface="#FFFFFF", encre="#161618", discret="#55565B",
          action="#1C1C1E", sur_action="#FFFFFF", marque="#A57B1E", titre="#1C1C1E", halo="#F7EDCF",
          ligne="#DEDCD6", ok="#17744A", non="#B42318")),
    ("denim", "Denim (celle de la Maison Francœur)",
     "Pour comparer : la palette choisie pour le magasin de vêtements. La prendre ici ferait des deux "
     "trousses une même famille « en entreprise ».",
     dict(fond="#EDF1F5", surface="#FFFFFF", encre="#17212E", discret="#4F5B6A",
          action="#2B4A78", sur_action="#FFFFFF", marque="#C8692A", titre="#2B4A78", halo="#FBE9DC",
          ligne="#D5DDE6", ok="#1F7A4D", non="#B42318")),
    ("francis", "francis, tel quel (l'actuel)",
     "Ce que l'écran porte aujourd'hui : le vert du système de design pour l'action, le mauve réservé "
     "au point du « i ». C'est la décision du 24 septembre — à garder si rien d'autre ne convainc.",
     dict(fond="#F7F6F3", surface="#FFFFFF", encre="#17181A", discret="#55575C",
          action="#087A4E", sur_action="#FFFFFF", marque="#6B4FBB", titre="#087A4E", halo="#FBEEDC",
          ligne="#E4E2DC", ok="#087A4E", non="#B42318")),
]


def maquette(k, j):
    img = "/assets/interactive/hotel/croquis/{}.jpg"
    carte = lambda a, t, faux=False: (
        f'<div class="m-opt{" m-faux" if faux else ""}"><img src="{img.format(a)}" alt="">'
        f'<span class="m-cmot">{t}</span></div>')
    return f"""<div class="tel" style="{';'.join(f'--p-{a}:{b}' for a, b in j.items())};--marque-600:{j['marque']}">
  <div class="fr-barre"><div class="fr-barre__in">
    <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">Aide à l'apprentissage de l'anglais</span></span>
  </div></div>
  <div class="m-page">
    <p class="m-enseigne">Hôtel Rive-Claire</p>
    <p class="m-h1">Ce que le client veut</p>
    <p class="m-appui">Choisissez le lit ET le nombre de nuits.</p>
    <div class="m-boutons"><span class="m-btn m-pri">▶ Réécouter</span><span class="m-btn">Plus lentement</span></div>
    <div class="m-choix">
      {carte("lit-king", "un lit king · 2 nuits", True)}
      {carte("lit-queen", "un lit queen · 3 nuits")}
    </div>
    <p class="m-non">✕ Les nuits sont justes, pas le lit.</p>
    <div class="m-halo"><b>La règle du comptoir</b> — un remboursement, un service gratuit : c'est le gérant qui décide.</div>
    <p class="m-ok">✓ Juste!</p>
  </div>
</div>"""


def page():
    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Hôtel Rive-Claire — les couleurs</title>", tete)
    tete = tete.replace("</head>", '<link rel="stylesheet" href="/assets/design-system/marque-francis.css">\n</head>', 1)
    tete = tete.replace("</style>", FC.CSS + CSS + "</style>", 1)
    blocs = []
    for k, nom, idee, j in PALETTES:
        c = FC.controles(j)
        rates = [x for x in c if x[1] < x[2]]
        assert not rates, f"{nom} : " + ", ".join(f"{a} {v:.2f}:1 < {s}" for a, v, s in rates)
        nuancier = "".join(f'<li><i style="background:{j[r]}"></i><span><b>{E(lib)}</b><code>{j[r]}</code></span></li>'
                           for r, lib in FC.ROLES)
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
<a class="retour" href="/presentations.html#hotellerie"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Hôtel Rive-Claire &middot; les couleurs</p>
<h1>Des couleurs pour la réception</h1>
<p class="chapeau">L'écran de la réception porte aujourd'hui le thème francis tel quel. Voici d'autres
propositions, pensées pour un hôtel : <strong>quatre neuves</strong>, Denim (celle de la Maison Francœur) pour
comparer, et l'actuelle en dernier. Dans les palettes neuves, le mauve s'en va : le point du « i », le filet
et l'enseigne prennent la couleur de la palette, comme pour Francœur. Ce qui reste : le nom, son point, Nunito,
le vert et le rouge de la rétroaction. Chaque maquette est un vrai écran de la trousse, au format téléphone,
et chaque contraste est mesuré.</p>
{''.join(blocs)}
<section class="decision">
  <h2>Ce que vous voulez</h2>
  <textarea id="general" rows="3" placeholder="Une autre idée, un mélange de deux palettes, une couleur à éviter…"></textarea>
  <p><button type="button" class="btn-export" id="exporter">Exporter mes choix</button> <span id="copie" aria-live="polite"></span></p>
  <pre id="sortie" hidden></pre>
</section>
<div class="pied"><p>Page produite par <code>build/hotel_couleurs.py</code> — ne pas l'éditer.</p></div>
</div>
<script>
const CLE = 'hotellerie-couleurs';
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
  const txt = JSON.stringify({{page: 'hotellerie-couleurs', choix: lire()}}, null, 1);
  const pre = document.getElementById('sortie'); pre.textContent = txt; pre.hidden = false;
  try {{ await navigator.clipboard.writeText(txt); document.getElementById('copie').textContent = 'Copié : recollez-le dans la conversation.'; }}
  catch (e) {{ document.getElementById('copie').textContent = 'Copiez le texte ci-dessous.'; }}
}};
</script>
</body></html>"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {len(PALETTES)} palettes, contrastes vérifiés")


# Les croquis de lits sont en couleur et la maquette les montre tels quels.
CSS = """
.tel .m-opt img{filter:none}
.tel .m-cmot{font-size:12px}
"""

if __name__ == "__main__":
    page()
