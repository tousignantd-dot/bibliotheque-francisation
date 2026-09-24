#!/usr/bin/env python3
"""La page des constats de la boucle didactique — Maison Francœur.

    python3 build/francoeur_audit_page.py            # tour 1
    python3 build/francoeur_audit_page.py --tour 2   # après révision

Produite, jamais éditée : elle lit les relevés des auditeurs dans
build/contenu/entreprise-francoeur/boucle/audit<tour>-*.json (un par regard :
le contenu, la page servie) et le cadrage. Chaque constat porte un code de la
grille (A1…G2) et une gravité ; la page trie par gravité, groupe par famille,
et laisse trancher : à corriger · garder tel quel · à discuter. « Exporter »
rend le JSON à recoller dans la séance suivante — c'est lui qui pilote la
révision, pas la mémoire de la conversation.

Sortie : assets/presentations/francoeur-audit-<tour>.html
"""
import html, json, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
BOUCLE = RACINE / "build" / "contenu" / "entreprise-francoeur" / "boucle"
E = html.escape

FAMILLES = {"A": "Alignement", "B": "Entrée en matière", "C": "Charge cognitive",
            "D": "Pratique", "E": "Rétroaction", "F": "Transfert", "G": "Accès"}
CRITERES = {"A1": "Objectif observable", "A2": "Écart de performance réel", "A3": "Alignement constructif",
            "B1": "Tâche d'abord", "B2": "Activation des acquis", "B3": "Pertinence et ton",
            "C1": "Segmentation", "C2": "Cohérence", "C3": "Contiguïté et signalisation",
            "C4": "Exemple travaillé", "C5": "Langage clair", "D1": "Récupération",
            "D2": "Fidélité à la situation", "D3": "Variété et entrelacement",
            "D4": "Distracteurs plausibles", "E1": "Rétroaction explicative",
            "E2": "Conséquence visible", "F1": "Évaluation alignée", "F2": "Soutien au travail",
            "F3": "Espacement prévu", "G1": "Accessibilité", "G2": "Durée et contrôle"}
RANG = {"bloquant": 0, "majeur": 1, "mineur": 2}


def lire(tour):
    constats = []
    for f in sorted(BOUCLE.glob(f"audit{tour}-*.json")):
        for c in json.loads(f.read_text(encoding="utf-8")):
            c.setdefault("source", f.stem.split("-", 1)[1])
            constats.append(c)
    for n, c in enumerate(sorted(constats, key=lambda c: (RANG.get(c["gravite"], 3), c["code"])), 1):
        c["id"] = f"t{tour}-{n:02d}"
    return sorted(constats, key=lambda c: (RANG.get(c["gravite"], 3), c["code"]))


def page(tour, constats):
    compte = {g: sum(c["gravite"] == g for c in constats) for g in RANG}
    par_code = {}
    for c in constats:
        par_code[c["code"]] = par_code.get(c["code"], 0) + 1
    plus = sorted(par_code.items(), key=lambda x: -x[1])[:5]
    t = (RACINE / "assets" / "presentations" / "francoeur-etape0.html").read_text(encoding="utf-8")
    t = t[:t.index("<body")]
    t = re.sub(r"<title>.*?</title>", f"<title>Maison Francœur — audit, tour {tour}</title>", t)
    t = t.replace("</style>", CSS + "</style>", 1)
    cadrage = (BOUCLE / "cadrage.md").read_text(encoding="utf-8")
    objectifs = re.findall(r"- \*\*(O\d) — (.*?)\*\* (.*?)(?=\n- \*\*O|\n\n)", cadrage, re.S)

    def carte(c):
        g = c["gravite"]
        return (f'<article class="constat {g}" data-id="{c["id"]}" data-g="{g}" data-f="{c["code"][0]}">'
                f'<div class="tete-c"><span class="code">{E(c["code"])}</span>'
                f'<span class="nomc">{E(CRITERES.get(c["code"], ""))}</span>'
                f'<span class="grav">{E(g)}</span><span class="src">{E(c.get("source", ""))}</span></div>'
                f'<p class="lieu">{E(c["lieu"])}</p><p class="cst">{E(c["constat"])}</p>'
                f'<p class="cor"><b>Correctif :</b> {E(c["correctif"])}</p>'
                '<div class="choix"><button type="button" data-v="corriger" aria-pressed="false">À corriger</button>'
                '<button type="button" data-v="garder" aria-pressed="false">Garder tel quel</button>'
                '<button type="button" data-v="discuter" aria-pressed="false">À discuter</button></div></article>')

    cartes = "".join(carte(c) for c in constats)
    filtres = ('<button type="button" data-fg="tout" aria-pressed="true">Tout</button>'
               + "".join(f'<button type="button" data-fg="{g}" aria-pressed="false">{g.capitalize()}s · {compte[g]}</button>' for g in RANG)
               + "".join(f'<button type="button" data-ff="{k}" aria-pressed="false">{k} · {v}</button>' for k, v in FAMILLES.items()
                         if any(c["code"][0] == k for c in constats)))
    net = lambda d: re.sub(r"\*\*", "", d).strip()
    obj = "".join(f"<li><b>{E(o)} — {E(n)}.</b> {E(net(d))}</li>" for o, n, d in objectifs)
    corps = f"""<body><div class="doc large">
<a class="retour" href="/presentations.html#francoeur"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Maison Francœur &middot; boucle didactique &middot; tour {tour}</p>
<h1>L'audit de la trousse</h1>
<p class="chapeau">La trousse passée à la grille de la boucle didactique — 22 critères, sept familles — par deux
regards qui n'avaient pas les intentions de l'auteur : l'un a lu le <b>contenu</b>, l'autre a <b>servi et joué
la page</b> à 375 et à 1280 px. <strong>{compte['bloquant']} bloquant{'s' if compte['bloquant'] > 1 else ''},
{compte['majeur']} majeur{'s' if compte['majeur'] > 1 else ''}, {compte['mineur']} mineur{'s' if compte['mineur'] > 1 else ''}.</strong>
Sortie de boucle : zéro bloquant, zéro majeur. Tranchez chaque constat, puis exportez : l'export pilote la révision.</p>

<div class="chiffres">
  <div class="ch"><span class="n">{compte['bloquant']}</span><span class="q">bloquants — l'objectif ne peut pas être atteint, ou on enseigne le mauvais geste</span></div>
  <div class="ch"><span class="n">{compte['majeur']}</span><span class="q">majeurs — atteint par une minorité, ou ne tiendra pas une semaine</span></div>
  <div class="ch"><span class="n">{compte['mineur']}</span><span class="q">mineurs — friction, consignés</span></div>
  <div class="ch"><span class="n">{E(plus[0][0]) if plus else '—'}</span><span class="q">le critère le plus touché{(' — ' + ', '.join(f'{k} ({v})' for k, v in plus)) if plus else ''}</span></div>
</div>

<section class="premier"><h2>Les objectifs contre lesquels on juge</h2>
<p>La trousse n'avait pas d'objectifs observables écrits : ils ont été posés pour l'audit, dans
<code>build/contenu/entreprise-francoeur/boucle/cadrage.md</code>.</p><ul class="obj">{obj}</ul></section>

<nav class="filtres" aria-label="Filtrer les constats">{filtres}</nav>
<section class="liste-c">{cartes}</section>

<p style="margin-top:1.4rem"><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button>
<span id="etat" class="etat"></span></p>
<div class="pied"><p>Ce que la boucle ne vérifie pas : l'exactitude du contenu (un locuteur et un commerçant doivent
valider), l'essai auprès de vrais employés (le pilote), l'effet au travail (des semaines après). Page produite par
<code>build/francoeur_audit_page.py</code> — ne pas l'éditer.</p></div>
</div>
<script>
(function(){{
  var CLE='francoeur-audit-{tour}', v={{}}, fg='tout', ff=null;
  try{{ v=JSON.parse(localStorage.getItem(CLE)||'{{}}'); }}catch(e){{}}
  function peindre(){{
    document.querySelectorAll('.constat').forEach(function(c){{
      c.querySelectorAll('.choix button').forEach(function(b){{ b.setAttribute('aria-pressed', v[c.dataset.id]===b.dataset.v?'true':'false'); }});
      c.hidden = !((fg==='tout'||c.dataset.g===fg) && (!ff||c.dataset.f===ff));
    }});
    var n=Object.keys(v).length, t=document.querySelectorAll('.constat').length;
    document.getElementById('etat').textContent=n+' constats tranchés sur '+t;
  }}
  document.addEventListener('click',function(e){{
    var b=e.target.closest('.choix button');
    if(b){{ var id=b.closest('.constat').dataset.id; if(v[id]===b.dataset.v) delete v[id]; else v[id]=b.dataset.v;
      try{{ localStorage.setItem(CLE,JSON.stringify(v)); }}catch(x){{}} peindre(); return; }}
    var f=e.target.closest('.filtres button'); if(!f) return;
    if(f.dataset.fg){{ fg=f.dataset.fg; ff=null; }} else {{ ff = ff===f.dataset.ff ? null : f.dataset.ff; }}
    document.querySelectorAll('.filtres button').forEach(function(x){{
      x.setAttribute('aria-pressed', String((x.dataset.fg&&x.dataset.fg===fg&&!ff) || (x.dataset.ff&&x.dataset.ff===ff))); }});
    peindre();
  }});
  document.getElementById('exporter').onclick=function(){{
    var out={{audit:'francoeur', tour:{tour}, decisions:v}};
    var t=JSON.stringify(out,null,2);
    if(navigator.clipboard) navigator.clipboard.writeText(t).then(function(){{ document.getElementById('etat').textContent='Copié — à recoller dans la séance suivante.'; }},function(){{prompt('Copiez :',t);}}); else prompt('Copiez :',t);
  }};
  peindre();
}})();
</script></body></html>"""
    sortie = RACINE / "assets" / "presentations" / f"francoeur-audit-{tour}.html"
    sortie.write_text(t + corps, encoding="utf-8")
    return sortie, compte


CSS = """
.doc.large{max-width:1100px}
.obj li{margin:6px 0}
.filtres{position:sticky;top:0;z-index:2;background:var(--ground);display:flex;flex-wrap:wrap;gap:6px;padding:10px 0;border-bottom:1px solid var(--line);margin:18px 0 8px}
.filtres button,.choix button{font:inherit;font-size:14px;cursor:pointer;background:var(--sunken);color:var(--body);border:1px solid var(--line-fort);border-radius:9px;padding:6px 10px}
.filtres button[aria-pressed=true]{background:var(--ink);color:var(--card);border-color:var(--ink)}
.constat{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--line-fort);border-radius:12px;padding:12px 14px;margin:10px 0}
.constat.bloquant{border-left-color:var(--loi)}
.constat.majeur{border-left-color:var(--decid)}
.constat.mineur{border-left-color:var(--acier)}
.tete-c{display:flex;flex-wrap:wrap;gap:8px;align-items:baseline}
.code{font-weight:900;font-size:16px;color:var(--ink)}
.nomc{font-weight:700;color:var(--ink)}
.grav{font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:.08em}
.constat.bloquant .grav{color:var(--loi)} .constat.majeur .grav{color:var(--decid)} .constat.mineur .grav{color:var(--acier)}
.src{font-size:12px;color:var(--muted);margin-left:auto}
.lieu{margin:4px 0 0;font-size:14px;color:var(--muted)}
.cst{margin:6px 0 0}
.cor{margin:6px 0 0;font-size:15px}
.choix{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.choix button[aria-pressed=true][data-v=corriger]{background:var(--loi-bg);border-color:var(--loi);color:var(--ink);font-weight:700}
.choix button[aria-pressed=true][data-v=garder]{background:var(--fait-bg);border-color:var(--fait);color:var(--ink);font-weight:700}
.choix button[aria-pressed=true][data-v=discuter]{background:var(--decid-bg);border-color:var(--decid);color:var(--ink);font-weight:700}
"""

if __name__ == "__main__":
    tour = int(sys.argv[sys.argv.index("--tour") + 1]) if "--tour" in sys.argv else 1
    c = lire(tour)
    s, compte = page(tour, c)
    print(f"{s.relative_to(RACINE)} — {len(c)} constats {compte}")
