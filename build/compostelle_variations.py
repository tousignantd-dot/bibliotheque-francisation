#!/usr/bin/env python3
"""Trois variations du système de design pour « En route vers Compostelle ».

    python3 build/compostelle_variations.py   # → assets/presentations/compostelle-variations.html

Demande de Daniel, 26 sept. 2026 : « une variation au niveau du système de
design, sans changer la police de caractère — quelque chose qui ferait plus
pèlerin, plus Compostelle ; au moins trois ». Nunito reste partout ; ce qui
varie : la palette, les surfaces, les rayons, le tampon et la progression.

Chaque variation est un jeu de jetons (THEMES) appliqué aux MÊMES maquettes,
bâties en HTML avec les vraies images et les vraies répliques de la trousse :
on compare des palettes, pas des mises en page. La barre francis ne varie pas
(le mauve est à la marque seule). La page se termine par un choix à exporter.
"""
import html, json, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import compostelle_commun as C  # noqa: E402

SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "compostelle-variations.html"
MEDIA = "../interactive/compostelle/"
E = html.escape

# (clé, nom, accroche, jetons, nuancier [(nom, couleur)], raison, prudence)
THEMES = [
    ("actuel", "Aujourd'hui : le thème francis", "La référence : le système de la plateforme, le jaune de la flèche réservé à la progression.",
     dict(bg="#F7F7F5", card="#FFFFFF", ink="#17181A", body="#2B2D31", muted="#6B6E73", line="#E4E4E0",
          act="#0A8F5B", actink="#FFFFFF", prog="#F2C230", titre="#6B6E73", audio="#C8102E",
          ok="#0A8F5B", okbg="#E6F4EC", rad="12px", cellbg="#FBF6E4", cellline="#C9B98A",
          tampon="#0A8F5B", tamponbg="#FFFFFF", fond="none", bande="transparent"),
     [("Fond", "#F7F7F5"), ("Action", "#0A8F5B"), ("Flèche", "#F2C230"), ("Audio", "#C8102E")],
     "", ""),
    ("carnet", "A · La credencial", "Le carnet du pèlerin : papier crème, encre sépia, tampons à l'encre rouge. L'application devient l'objet qu'on fait tamponner.",
     dict(bg="#EFE5CF", card="#FBF6EA", ink="#3B2E14", body="#4A3B22", muted="#85704A", line="#DCCBA5",
          act="#9B2C2C", actink="#FFFFFF", prog="#C9A227", titre="#9B2C2C", audio="#1D4E89",
          ok="#3F6B2E", okbg="#E9EFD9", rad="6px", cellbg="#FBF6EA", cellline="#B79F6E",
          tampon="#9B2C2C", tamponbg="transparent",
          fond="repeating-linear-gradient(0deg,rgba(120,90,40,.035) 0 1px,transparent 1px 26px)", bande="transparent"),
     [("Papier", "#EFE5CF"), ("Encre sépia", "#3B2E14"), ("Rouge Santiago", "#9B2C2C"), ("Or", "#C9A227"), ("Bleu encre", "#1D4E89")],
     "C'est la métaphore que l'application porte déjà : la credencial et ses tampons. La pousser jusqu'à la surface rend "
     "chaque tampon gagné plus précieux, et le rouge est celui de la croix de Santiago, brodée sur les capes.",
     "Le papier crème baisse un peu le contraste : garder l'encre très foncée pour le texte courant. Un rouge qui sert "
     "à l'action ne peut plus signaler une erreur : les erreurs passent au brun-orangé."),
    ("borne", "B · La flèche et la borne", "La signalétique du chemin : le jaune de la flèche devient l'action, le bleu de la borne galicienne encadre.",
     dict(bg="#E8ECEE", card="#FFFFFF", ink="#13233B", body="#22324A", muted="#5B6979", line="#D2D9DF",
          act="#F2C230", actink="#13233B", prog="#1F4E9C", titre="#1F4E9C", audio="#1F4E9C",
          ok="#1F4E9C", okbg="#E3EBF7", rad="14px", cellbg="#FFFFFF", cellline="#AFBFD3",
          tampon="#F2C230", tamponbg="#1F4E9C", fond="none", bande="transparent"),
     [("Granite", "#E8ECEE"), ("Flèche", "#F2C230"), ("Bleu borne", "#1F4E9C"), ("Nuit", "#13233B")],
     "Sur le Camino, on suit une flèche jaune et une borne bleue à coquille jaune — le pèlerin les voit mille fois. "
     "Le bouton « Reprendre la route » devient littéralement la flèche ; chaque tampon, une petite borne.",
     "Le jaune ne porte pas de texte blanc : texte bleu nuit sur jaune (contraste 10:1). Le jaune quitte la barre de "
     "progression, qui passe au bleu. C'est la plus lisible au soleil, et la plus « signalétique » — moins chaleureuse."),
    ("meseta", "C · La Meseta, terre et ciel", "Les couleurs du paysage : ocre des blés, terre cuite des toits, bleu du grand ciel de Castille, olive des haies.",
     dict(bg="#F6EFE2", card="#FFFDF8", ink="#2E2A24", body="#3D372E", muted="#7C7163", line="#E6DAC4",
          act="#B04A20", actink="#FFFFFF", prog="#E3B04B", titre="#2F6FA3", audio="#2F6FA3",
          ok="#5F7A2E", okbg="#EDF1E0", rad="18px", cellbg="#FFFDF8", cellline="#D9C29A",
          tampon="#B04A20", tamponbg="#FFFDF8", fond="none",
          bande="linear-gradient(180deg,#CFE3F0 0 86%,#EBCB86 86% 100%)"),
     [("Blé", "#E3B04B"), ("Terre cuite", "#B04A20"), ("Ciel", "#2F6FA3"), ("Olive", "#5F7A2E"), ("Sable", "#F6EFE2")],
     "Les vignettes de l'application sont déjà dans ces tons : la palette sort des images au lieu de les encadrer de "
     "gris. Un horizon ciel-blé ouvre l'accueil, comme la Meseta ouvre la deuxième moitié du chemin.",
     "La plus chaleureuse, et la plus proche des dessins ; mais c'est aussi celle qui s'éloigne le plus du reste de la "
     "plateforme. La terre cuite est foncée à dessein : plus claire, le texte blanc ne passerait plus."),
]

COQUILLE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3c-5 0-9 4-9 9 0 1 .4 2 1 3l8 6 8-6c.6-1 1-2 1-3 '
            '0-5-4-9-9-9z" fill="currentColor" opacity=".9"/><path d="M12 5v14M8 6.5 11 19M16 6.5 13 19M5.2 9.5 10.5 19M18.8 '
            '9.5 13.5 19" stroke="rgba(0,0,0,.28)" stroke-width="1" fill="none"/></svg>')


def telephone_accueil(k):
    lieux = ["Ronces.", "Pampl.", "Puente", "Logroño", "Burgos", "Carrión", "León", "Cebreiro", "Sarria", "Santiago"]
    cases = "".join(
        f'<div class="case{" faite" if i < 3 else ""}{" ici" if i == 3 else ""}"><span class="num">{i + 1}</span>'
        + (f'<span class="sceau">{COQUILLE}</span>' if i < 3 else "") + f'<small>{lieux[i]}</small></div>' for i in range(10))
    frise = "".join(f'<i class="{"pass" if i < 4 else ""}"></i>' for i in range(10))
    return f"""<div class="tel th-{k}"><div class="barre"><span class="fr-nom">francis</span><span class="tr">En route vers Compostelle</span></div>
<div class="ecran"><div class="horizon"></div>
 <p class="sur">Ma credencial · 3 tampons sur 10</p>
 <h4>Jour 4 · Logroño</h4><p class="sous">La Rioja, km 163</p>
 <div class="btn act">Reprendre la route <span class="fl">➜</span></div>
 <div class="frise">{frise}</div>
 <div class="cred">{cases}</div>
 <div class="deux"><div class="tuile"><b>La poche</b><span>Hors ligne</span></div><div class="tuile"><b>Suis-je prêt ?</b><span>Un quart d'heure</span></div></div>
</div></div>"""


def telephone_scene(k, tour0, choix):
    btns = "".join(
        f'<div class="choix{" bon" if i == 0 else ""}">{E(es)}</div>' for i, (es, fr, retro) in enumerate(choix))
    return f"""<div class="tel th-{k}"><div class="barre"><span class="fr-nom">francis</span><span class="tr">En route vers Compostelle</span></div>
<div class="ecran">
 <img class="vig" src="{MEDIA}etapes/pamplona.jpg" alt="">
 <p class="sur">Jour 2 · La scène</p>
 <div class="qui"><img src="{MEDIA}portraits/ainhoa.jpg" alt=""><div><b>Ainhoa</b><span>serveuse, Pamplona</span></div></div>
 <div class="bulle"><span class="play">▶</span><div>{E(tour0["es"])}</div></div>
 {btns}
 <div class="retro">✓ C'est ce qu'elle attendait : commandez directement.</div>
</div></div>"""


CSS = """<style>
.th-actuel{%s}.th-carnet{%s}.th-borne{%s}.th-meseta{%s}
.variation{margin-top:46px}
.variation>header h2{margin:0 0 4px}
.variation>header p{margin:0 0 14px;font-size:16px}
.telephones{display:flex;gap:22px;flex-wrap:wrap;align-items:flex-start}
.nuancier{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 16px;padding:0;list-style:none}
.nuancier li{display:flex;align-items:center;gap:7px;font-size:13.5px;background:var(--card);border:1px solid var(--line);border-radius:99px;padding:4px 11px 4px 4px}
.nuancier i{width:20px;height:20px;border-radius:50%%;border:1px solid rgba(0,0,0,.15);display:block}
.pourquoi{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:16px}
.pourquoi div{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;font-size:14.5px;line-height:1.45}
.pourquoi b{display:block;color:var(--ink);margin-bottom:3px}
/* le téléphone : ses couleurs sont celles de la variation, jamais celles de la page */
.tel{width:300px;max-width:100%%;border-radius:30px;border:9px solid #1B1C1E;background:var(--p-bg);background-image:var(--p-fond);
 overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,.18);font-size:13px;color:var(--p-body);flex:none}
.tel .barre{display:flex;justify-content:space-between;align-items:baseline;background:#fff;border-bottom:2px solid #6B4FBB;padding:9px 12px}
.tel .fr-nom{font-weight:900;letter-spacing:-.035em;color:#17181A;font-size:16px}
.tel .tr{font-weight:900;color:var(--p-act-txt);font-size:11.5px}
.tel .ecran{padding:12px 13px 16px;position:relative}
.tel .horizon{position:absolute;inset:0 0 auto 0;height:104px;background:var(--p-bande);z-index:0}
.tel .ecran>*{position:relative;z-index:1}
.tel .ecran>.horizon{position:absolute;z-index:0}
.tel *{font-style:normal}
.tel .sur{margin:2px 0 2px;font-size:10px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:var(--p-titre)}
.tel h4{margin:0;font-size:21px;line-height:1.15;color:var(--p-ink);font-weight:900}
.tel .sous{margin:2px 0 10px;color:var(--p-muted)}
.tel .btn{border-radius:var(--p-rad);padding:11px;text-align:center;font-weight:900;font-size:14px}
.tel .btn.act{background:var(--p-act);color:var(--p-actink)}
.tel .fl{margin-left:4px}
.tel .frise{display:flex;justify-content:space-between;align-items:center;margin:13px 4px 11px;position:relative}
.tel .frise::before{content:"";position:absolute;left:0;right:0;top:50%%;border-top:2px dotted var(--p-prog)}
.tel .frise i{width:10px;height:10px;border-radius:50%%;background:var(--p-card);border:2px solid var(--p-prog);position:relative}
.tel .frise i.pass{background:var(--p-prog)}
.tel .cred{display:grid;grid-template-columns:repeat(5,1fr);gap:5px;background:var(--p-card);border:1px solid var(--p-line);border-radius:var(--p-rad);padding:8px}
.tel .case{aspect-ratio:1/1.12;border:1.5px dashed var(--p-cellline);border-radius:calc(var(--p-rad) * .6);background:var(--p-cellbg);
 display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative}
.tel .case .num{font-weight:900;font-size:15px;color:var(--p-muted)}
.tel .case small{font-size:7.5px;color:var(--p-muted);position:absolute;bottom:2px}
.tel .case.ici{border:2px solid var(--p-act);border-style:solid}
.tel .case.faite .num{display:none}
.tel .sceau{width:25px;height:25px;margin-bottom:7px;border-radius:50%%;display:grid;place-items:center;color:var(--p-tampon);background:var(--p-tamponbg);
 border:2px solid var(--p-tampon);transform:rotate(-12deg)}
.tel .sceau svg{width:16px;height:16px}
.th-carnet .sceau{box-shadow:0 0 0 2px var(--p-card),0 0 0 3.2px var(--p-tampon);opacity:.88}
.th-borne .case.faite{background:#1F4E9C;border:none}
.th-borne .case.faite small{color:#DDE6F4}
.th-borne .sceau{border:none;transform:none}
.th-meseta .sceau{border-width:2.5px}
.tel .deux{display:grid;grid-template-columns:1fr 1fr;gap:7px;margin-top:9px}
.tel .tuile{background:var(--p-card);border:1px solid var(--p-line);border-radius:var(--p-rad);padding:8px 9px}
.tel .tuile b{display:block;color:var(--p-ink);font-size:12.5px}
.tel .tuile span{color:var(--p-muted);font-size:11px}
.th-meseta .sous{margin-bottom:22px}
.th-borne .tuile{border-left:4px solid #1F4E9C}
.tel .vig{width:100%%;height:92px;object-fit:cover;border-radius:var(--p-rad);display:block;margin-bottom:9px}
.tel .qui{display:flex;gap:9px;align-items:center;margin:6px 0 8px}
.tel .qui img{width:40px;height:40px;border-radius:50%%;object-fit:cover;border:2px solid var(--p-card);background:#fff}
.tel .qui b{display:block;color:var(--p-ink)}
.tel .qui span{color:var(--p-muted);font-size:11.5px}
.tel .bulle{display:flex;gap:9px;align-items:center;background:var(--p-card);border:1px solid var(--p-line);border-radius:var(--p-rad);padding:9px 10px;color:var(--p-ink);font-weight:800;font-size:14px;margin-bottom:9px}
.tel .play{flex:none;width:30px;height:30px;border-radius:50%%;background:var(--p-audio);color:#fff;display:grid;place-items:center;font-size:11px}
.tel .choix{background:var(--p-card);border:1.5px solid var(--p-line);border-radius:var(--p-rad);padding:9px 10px;margin-top:6px;color:var(--p-ink);font-weight:700}
.tel .choix.bon{border-color:var(--p-ok);background:var(--p-okbg)}
.tel .retro{margin-top:8px;color:var(--p-ok);font-weight:800;font-size:12.5px}
.choisir{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}
.choisir label{display:flex;gap:8px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;cursor:pointer;font-weight:700}
.choisir input{accent-color:#0A8F5B;width:18px;height:18px}
textarea.note{width:100%%;min-height:90px;font:inherit;border:1px solid var(--line-fort);border-radius:10px;padding:10px;background:var(--card);color:var(--body)}
.exporter{margin-top:10px;font:inherit;font-weight:800;background:#0A8F5B;color:#fff;border:0;border-radius:10px;padding:11px 18px;cursor:pointer}
pre.json{white-space:pre-wrap;background:var(--sunken);border-radius:10px;padding:12px;font-size:13px}
@media (max-width:760px){.pourquoi{grid-template-columns:1fr}.telephones{justify-content:center}}
</style>
</head>"""


def jetons(t):
    return (f"--p-bg:{t['bg']};--p-card:{t['card']};--p-ink:{t['ink']};--p-body:{t['body']};--p-muted:{t['muted']};"
            f"--p-line:{t['line']};--p-act:{t['act']};--p-actink:{t['actink']};--p-prog:{t['prog']};--p-titre:{t['titre']};"
            f"--p-audio:{t['audio']};--p-ok:{t['ok']};--p-okbg:{t['okbg']};--p-rad:{t['rad']};--p-cellbg:{t['cellbg']};"
            f"--p-cellline:{t['cellline']};--p-tampon:{t['tampon']};--p-tamponbg:{t['tamponbg']};--p-fond:{t['fond']};"
            f"--p-bande:{t['bande']};--p-act-txt:{t['act'] if t['act'] != '#F2C230' else t['prog']}")


def main():
    ET = C.charger("etapes")
    pamp = next(e for e in ET.ETAPES if e["id"] == "pamplona")
    tour0, choix = pamp["scene"]["tours"][0], pamp["scene"]["tours"][1]["choix"]
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Compostelle — trois habits</title>", tete)
    tete = tete.replace("</head>", CSS % tuple(jetons(t[3]) for t in THEMES))

    blocs = []
    for k, nom, accroche, t, nuancier, raison, prudence in THEMES:
        nu = "".join(f'<li><i style="background:{c}"></i>{E(n)} <code style="font-size:12px;color:var(--muted)">{c}</code></li>'
                     for n, c in nuancier)
        pq = (f'<div class="pourquoi"><div><b>Pourquoi elle fait « chemin »</b>{E(raison)}</div>'
              f'<div><b>À surveiller</b>{E(prudence)}</div></div>') if raison else ""
        blocs.append(f"""<section class="variation" id="{k}"><header><h2>{E(nom)}</h2><p>{E(accroche)}</p></header>
<ul class="nuancier">{nu}</ul>
<div class="telephones">{telephone_accueil(k)}{telephone_scene(k, tour0, choix)}</div>{pq}</section>""")

    options = [("actuel", "Garder le thème francis")] + [(t[0], t[1]) for t in THEMES[1:]]
    radios = "".join(f'<label><input type="radio" name="choix" value="{k}">{E(n)}</label>' for k, n in options)

    corps = f"""<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Voyage &middot; grand public &middot; chemin de Saint-Jacques</p>
<h1>Compostelle &mdash; trois habits pour le chemin</h1>
<p class="chapeau">Trois variations du système de design, <strong>même police</strong> (Nunito), mêmes écrans : l'accueil
avec la credencial, et la scène de Pamplona. Ce qui change : la palette, le papier, les rayons, le tampon et la progression.
Les maquettes sont faites avec les vraies images et les vraies répliques de l'application.</p>
<div class="pourquoi"><div><b>Ce qui ne bouge pas</b>La barre francis et son filet mauve (le mauve n'appartient qu'à la marque) ;
Nunito ; la mise en page, les sept temps, les dessins ; un état dit toujours par un signe <i>et</i> un mot, jamais par la couleur seule.</div>
<div><b>Ce qui s'écarte de la règle</b>Sur la plateforme, l'action est toujours le vert <code>#0A8F5B</code>. La trousse de Compostelle
s'adresse au grand public, hors de la classe : elle peut porter un habit de secteur, comme Maison Francœur porte le sien (Denim).
Chaque variation remplace donc ce vert.</div></div>
{"".join(blocs)}
<section class="variation" id="choix"><header><h2>Votre choix</h2><p>Choisissez, ajoutez ce que vous voulez garder d'une
autre, puis exportez : collez le texte dans la conversation.</p></header>
<div class="choisir">{radios}</div>
<textarea class="note" id="note" placeholder="Par exemple : B, mais avec les tampons rouges de A."></textarea>
<button class="exporter" id="exp" type="button">Exporter mon choix</button>
<pre class="json" id="sortie" hidden></pre>
</section>
</div>
<script>
const CLE = 'compostelle-variations:choix';
function lire(){{ try {{ return JSON.parse(localStorage.getItem(CLE) || '{{}}'); }} catch (e) {{ return {{}}; }} }}
function ecrire(v){{ try {{ localStorage.setItem(CLE, JSON.stringify(v)); }} catch (e) {{}} }}
const etat = lire();
if (etat.choix) {{ const r = document.querySelector(`input[value="${{etat.choix}}"]`); if (r) r.checked = true; }}
if (etat.note) document.getElementById('note').value = etat.note;
document.querySelectorAll('input[name=choix]').forEach(r => r.addEventListener('change', () => {{ etat.choix = r.value; ecrire(etat); }}));
document.getElementById('note').addEventListener('input', e => {{ etat.note = e.target.value; ecrire(etat); }});
document.getElementById('exp').addEventListener('click', async () => {{
  const txt = JSON.stringify({{page: 'compostelle-variations', date: new Date().toLocaleDateString('fr-CA'),
    choix: etat.choix || null, note: etat.note || ''}}, null, 2);
  const s = document.getElementById('sortie'); s.textContent = txt; s.hidden = false;
  try {{ await navigator.clipboard.writeText(txt); document.getElementById('exp').textContent = 'Copié — collez-le dans la conversation'; }}
  catch (e) {{ document.getElementById('exp').textContent = 'Sélectionnez le texte ci-dessous et copiez-le'; }}
}});
</script>
</body>
</html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {len(THEMES) - 1} variations")


if __name__ == "__main__":
    main()
