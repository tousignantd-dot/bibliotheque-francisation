#!/usr/bin/env python3
"""Les reprises de voix de la Maison Francœur — plusieurs candidats, l'oreille choisit.

    python3 build/francoeur_reprises.py                # candidats + page d'écoute
    python3 build/francoeur_reprises.py --page         # la page seule

POURQUOI DES CANDIDATS : la voix HD n'est pas déterministe — refaire un tirage
est un pari. Pour chaque mot signalé « à refaire » sur la page d'écoute, on
produit quatre versions et Daniel choisit à l'oreille :
  1. une nouvelle prise HD, texte inchangé ;
  2-3. des prises HD avec une GRAPHIE DE PRONONCIATION qui ne peut se lire
       qu'en français (« le dénime », « le polyestère ») — l'écran, lui, garde
       l'orthographe ; seule la voix change ;
  4. la voix NEURALE de Sylvie, qui respecte toujours le xml:lang français.

Le choix revient sous forme de JSON exporté ; il se pose dans
`PRONONCIATION` de build/audio_francoeur.py, qui le rejoue à chaque
régénération.

Sortie : assets/interactive/francoeur/sons/_candidats/<id>-<n>.mp3 et
assets/presentations/francoeur-reprises.html
"""
import html, pathlib, re, sys
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
sys.path.insert(0, str(RACINE / "build" / "contenu" / "entreprise-francoeur"))
import azure_voix  # noqa: E402
from lexique import LEXIQUE  # noqa: E402

DEST = RACINE / "assets" / "interactive" / "francoeur" / "sons" / "_candidats"
PAGE = RACINE / "assets" / "presentations" / "francoeur-reprises.html"

# Signalés « à refaire » par Daniel sur la page d'écoute, le 24 septembre 2026.
# (id, [(étiquette, texte envoyé à la voix, rôle)])
REPRISES = [
    ("lin", [("HD, nouvelle prise", "le lin", "hd_feminin"),
             ("HD, « du lin »", "du lin", "hd_feminin"),
             ("HD, graphie « le lain »", "le lain", "hd_feminin"),
             ("Neurale, Sylvie", "le lin", "enseignante")]),
    ("polyester", [("HD, nouvelle prise", "le polyester", "hd_feminin"),
                   ("HD, graphie « le polyestère »", "le polyestère", "hd_feminin"),
                   ("HD, graphie « le poliestère »", "le poliestère", "hd_feminin"),
                   ("Neurale, Sylvie", "le polyester", "enseignante")]),
    ("denim", [("HD, nouvelle prise", "le denim", "hd_feminin"),
               ("HD, graphie « le dénim »", "le dénim", "hd_feminin"),
               ("HD, graphie « le dénime »", "le dénime", "hd_feminin"),
               ("Neurale, Sylvie", "le denim", "enseignante")]),
    ("rose", [("HD, nouvelle prise", "rose", "hd_feminin"),
              ("HD, « Rose. »", "Rose.", "hd_feminin"),
              ("HD, graphie « rôse »", "rôse", "hd_feminin"),
              ("Neurale, Sylvie", "rose", "enseignante")]),
]


def produire():
    DEST.mkdir(parents=True, exist_ok=True)
    cle, region = azure_voix.cle_region()
    taches = [(i, n, t, r) for i, cands in REPRISES for n, (_e, t, r) in enumerate(cands, 1)]

    def un(x):
        i, n, t, r = x
        d = azure_voix.parle(t, r, DEST / f"{i}-{n}.mp3", cle=cle, region=region,
                             reference=azure_voix.TAUX_SONS)
        print(f"  {i:10} {n}  {d:4.2f} s  {r:12} {t}", flush=True)

    with ThreadPoolExecutor(4) as pool:
        list(pool.map(un, taches))


def page():
    E = html.escape
    mots = {e[0]: e[2] for e in LEXIQUE}
    tete = (RACINE / "assets" / "presentations" / "francoeur-etape0.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Maison Francœur — reprises de voix</title>", tete)
    tete = tete.replace("</style>", """
.mot-r{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;margin:12px 0}
.mot-r h2{margin:0 0 8px}
.cand{display:flex;flex-wrap:wrap;align-items:center;gap:10px;padding:8px 0;border-top:1px solid var(--line)}
.cand label{display:flex;gap:8px;align-items:center;font-weight:700;min-width:260px;cursor:pointer}
.cand audio{width:240px;max-width:100%}
</style>""", 1)
    blocs = "".join(
        f'<div class="mot-r" data-id="{i}"><h2>{E(mots[i])}</h2>'
        + "".join(f'<div class="cand"><label><input type="radio" name="{i}" value="{n}"> {E(e)}</label>'
                  f'<audio controls preload="none" src="/assets/interactive/francoeur/sons/_candidats/{i}-{n}.mp3?v=1"></audio></div>'
                  for n, (e, _t, _r) in enumerate(c, 1))
        + '<div class="cand"><label><input type="radio" name="' + i + '" value="0"> Aucune ne va — à retravailler</label></div></div>'
        for i, c in REPRISES)
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Maison Francœur &middot; voix</p>
<h1>Reprises de voix</h1>
<p class="chapeau">Les quatre mots signalés « à refaire ». Pour chacun, quatre versions : une nouvelle prise HD,
deux prises HD avec une graphie qui ne peut se lire qu'en français (l'écran garde l'orthographe normale), et la
voix neurale de Sylvie. <strong>Choisissez celle qui sonne juste</strong>, puis exportez.</p>
{blocs}
<p style="margin-top:1.4rem"><button type="button" class="btn-export" id="exporter">Exporter mes choix</button>
<span id="etat" class="etat"></span></p>
<div class="pied"><p>Produite par <code>build/francoeur_reprises.py</code> — ne pas l'éditer.</p></div>
</div>
<script>
(function(){{
  var CLE='francoeur-reprises', v={{}};
  try{{ v=JSON.parse(localStorage.getItem(CLE)||'{{}}'); }}catch(e){{}}
  Object.keys(v).forEach(function(k){{ var r=document.querySelector('input[name="'+k+'"][value="'+v[k]+'"]'); if(r) r.checked=true; }});
  document.addEventListener('change',function(e){{ if(e.target.type!=='radio') return; v[e.target.name]=e.target.value;
    try{{ localStorage.setItem(CLE,JSON.stringify(v)); }}catch(x){{}} document.getElementById('etat').textContent=Object.keys(v).length+' choix sur {len(REPRISES)}'; }});
  document.getElementById('exporter').onclick=function(){{
    var t=JSON.stringify({{reprises:'francoeur',choix:v}},null,2);
    if(navigator.clipboard) navigator.clipboard.writeText(t).then(function(){{ document.getElementById('etat').textContent='Copié — à recoller dans la conversation.'; }}); else prompt('Copiez :',t); }};
}})();
</script></body></html>"""
    PAGE.write_text(tete + corps, encoding="utf-8")


if __name__ == "__main__":
    if "--page" not in sys.argv:
        produire()
    page()
    print(PAGE.relative_to(RACINE))
