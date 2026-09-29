#!/usr/bin/env python3
"""Mettre en valeur le titre des dépliants — cinq façons, sans le surlignage.

    python3 build/depliant_titres.py   # → assets/presentations/depliant-titres.html

Daniel, 29 sept. 2026 : le surlignage jaune sous « là où vous en aurez besoin »
(et sous « dans la langue du client ») ne lui plaît pas ; il veut d'autres
propositions. Chaque façon est montrée sur les TROIS dépliants, dans leurs
couleurs et leur police, à la taille réelle du titre ; le choix s'exporte.
"""
import html, json, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "assets" / "presentations" / "hotellerie-prix.html"
SORTIE = RACINE / "assets" / "presentations" / "depliant-titres.html"
E = html.escape

DEPLIANTS = [
    ("Compostelle", "L'espagnol du Camino,", "là où vous en aurez besoin", "Pour les pèlerins francophones",
     {"fond": "#FDFBF6", "encre": "#13233B", "accent": "#1F4E9C", "chaud": "#9B2C2C", "halo": "#F2C230"}),
    ("Maison Francœur", "Le français du magasin,", "client par client", "Pour qui travaille dans un magasin de vêtements",
     {"fond": "#FAFBFD", "encre": "#16243A", "accent": "#2B4A78", "chaud": "#C8692A", "halo": "#FBE9DC"}),
    ("Hôtel Rive-Claire", "L'accueil à la réception,", "dans la langue du client", "Pour qui travaille à la réception d'un hôtel",
     {"fond": "#FDFBF7", "encre": "#0B3437", "accent": "#0F5E63", "chaud": "#C4613A", "halo": "#F6E3D9"}),
]

# (clé, nom, ce que ça donne, recommandé, CSS du titre — {…} = couleurs du dépliant)
FACONS = [
    ("actuel", "Aujourd'hui : le surlignage", "Pour comparer : le trait jaune à mi-hauteur, sous la seconde moitié.", False,
     "h1 .s{background:linear-gradient(transparent 60%,{halo} 60%)}"),
    ("deux-lignes", "Deux lignes, deux voix", "La seconde moitié passe à la ligne, plus légère et dans la couleur du dépliant. "
     "Le titre se lit comme une promesse en deux temps, sans aucun ornement.", True,
     "h1 .s{display:block;font-weight:500;color:{accent}}"),
    ("couleur", "La couleur seule", "La seconde moitié garde la même graisse, en couleur chaude. Le plus sobre : un seul changement.", False,
     "h1 .s{color:{chaud}}"),
    ("italique", "Une italique d'accent", "La seconde moitié en italique à empattements, comme une voix plus personnelle. "
     "Élégant, plus « éditorial » ; demande une seconde police (Newsreader, déjà employée au classeur).", False,
     "h1 .s{font-family:Newsreader,Georgia,serif;font-style:italic;font-weight:500;color:{accent};letter-spacing:0}"),
    ("filet", "Un filet au-dessus", "Le titre reste d'une seule couleur ; un court trait de couleur chaude, posé au-dessus, "
     "annonce qu'il est important. La seconde moitié passe en couleur du dépliant.", False,
     "h1{position:relative;padding-top:18px} h1::before{content:'';position:absolute;left:0;top:0;width:64px;height:6px;border-radius:3px;background:{chaud}} "
     "h1 .s{color:{accent}}"),
]


def main():
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    import re
    tete = re.sub(r"<title>.*?</title>", "<title>Le titre des dépliants — cinq façons</title>", tete)
    css = []
    blocs = []
    for k, nom, quoi, reco, regle in FACONS:
        vignettes = []
        for i, (dep, a, b, sur, c) in enumerate(DEPLIANTS):
            cls = f"v-{k}-{i}"
            r = regle
            for cle, val in c.items():
                r = r.replace("{" + cle + "}", val)
            css.append(" ".join(f".{cls} {sel.strip()}{{{corps}}}" for sel, corps in re.findall(r"([^{}]+)\{([^{}]*)\}", r)))
            css.append(f".{cls}{{background:{c['fond']};color:{c['encre']}}} .{cls} h1{{color:{c['encre']}}} .{cls} .sur{{color:{c['chaud']}}}")
            vignettes.append(f'<div class="vig {cls}"><p class="nomdep">{E(dep)}</p><p class="sur">{E(sur)}</p>'
                             f'<h1>{E(a)} <span class="s">{E(b)}.</span></h1></div>')
        blocs.append(f'<div class="facon"><div class="entete"><h2>{E(nom)}{" <span class=tag>recommandé</span>" if reco else ""}</h2>'
                     f'<p>{E(quoi)}</p><button type="button" class="opt" data-v="{k}" aria-pressed="false">Choisir celle-ci</button></div>'
                     f'<div class="vigs">{"".join(vignettes)}</div></div>')
    corps = f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@500;700;900&family=Newsreader:ital,wght@1,500&display=swap');
.facon{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:16px 0}}
.facon h2{{margin:0 0 4px;font-size:21px}} .facon p{{margin:0 0 10px;font-size:15px;color:var(--muted)}}
.tag{{font-size:12px;font-weight:700;color:var(--fait);background:var(--fait-bg);border-radius:99px;padding:2px 8px;margin-left:6px;vertical-align:3px}}
.vigs{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}
.vig{{border-radius:12px;padding:18px;border:1px solid rgba(0,0,0,.08);font-family:Nunito,system-ui,sans-serif}}
.vig .nomdep{{font-size:12px;font-weight:700;color:#8a8a84;margin:0 0 8px;letter-spacing:.06em;text-transform:uppercase}}
.vig .sur{{font-size:11px;letter-spacing:.14em;text-transform:uppercase;font-weight:900;margin:0 0 6px}}
.vig h1{{font-family:Nunito,system-ui,sans-serif;font-size:30px;line-height:1.06;font-weight:900;margin:0;letter-spacing:-.01em}}
.opt[aria-pressed="true"]{{background:var(--fait-bg);border-color:var(--fait);font-weight:700}}
@media (max-width:900px){{ .vigs{{grid-template-columns:1fr}} }}
{chr(10).join(css)}
</style>
<body><div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Dépliants &middot; Compostelle, Maison Francœur, Hôtel Rive-Claire</p>
<h1 style="font-family:inherit">Le titre des dépliants : cinq façons</h1>
<p class="chapeau">Le surlignage jaune sous la seconde moitié du titre ne vous plaît pas. Voici quatre autres façons de la mettre en
valeur, chacune montrée sur les trois dépliants, dans leurs couleurs. Choisissez-en une ; elle s'appliquera aux trois.</p>
{"".join(blocs)}
<section>
  <p><b>Un mot</b> (facultatif) :</p><textarea id="note" rows="2" style="width:100%"></textarea>
  <p style="margin-top:1rem"><button type="button" class="btn-export" id="exporter">Exporter mon choix</button> <span id="etat" class="etat"></span></p>
</section>
<div class="pied"><p>Page produite par <code>build/depliant_titres.py</code> — ne pas l'éditer.</p></div>
</div>
<script>
(function(){{
  var CLE='depliant-titres', s={{choix:null,note:''}};
  try{{ var l=JSON.parse(localStorage.getItem(CLE)||'null'); if(l) s=l; }}catch(e){{}}
  function sv(){{ try{{ localStorage.setItem(CLE,JSON.stringify(s)); }}catch(e){{}} }}
  function peindre(){{ document.querySelectorAll('.opt').forEach(function(b){{ b.setAttribute('aria-pressed', b.dataset.v===s.choix?'true':'false'); }}); }}
  document.querySelectorAll('.opt').forEach(function(b){{ b.onclick=function(){{ s.choix = s.choix===b.dataset.v ? null : b.dataset.v; sv(); peindre(); }}; }});
  var n=document.getElementById('note'); n.value=s.note||''; n.oninput=function(){{ s.note=n.value; sv(); }};
  document.getElementById('exporter').onclick=function(){{
    var t=JSON.stringify({{page:'depliant-titres', date:new Date().toISOString().slice(0,10), choix:s.choix, note:s.note||''}},null,2);
    var fin=function(){{ document.getElementById('etat').textContent='Copié — recolle-le-moi.'; }};
    if(navigator.clipboard) navigator.clipboard.writeText(t).then(fin,function(){{prompt('Copiez :',t);}}); else prompt('Copiez :',t);
  }};
  peindre();
}})();
</script>
</body></html>
"""
    style, reste = corps.split("<body>", 1)
    SORTIE.write_text(tete.replace("</head>", style + "</head>") + "<body>" + reste, encoding="utf-8")
    print(SORTIE.relative_to(RACINE), f"— {len(FACONS)} façons × {len(DEPLIANTS)} dépliants")


if __name__ == "__main__":
    main()
