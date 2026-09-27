#!/usr/bin/env python3
"""Les prix de la page acheteur de l'hôtel, à confirmer par Daniel.

    python3 build/hotel_prix.py   # → assets/presentations/hotellerie-prix.html

Produite, jamais éditée. Les montants affichés sont LUS dans
`build/contenu/entreprise-hotel/prix.py` (le seul endroit où ils vivent) ; les
chiffres de la trousse, dans son contenu. La page ne décide rien : elle rend un
export, et c'est l'export qui se recopie dans prix.py.

Pourquoi une page : les trois formules de l'hôtel ont été recopiées de la
Maison Francœur (24 sept. 2026) sans être chiffrées pour ce secteur. Or
l'hôtel diffère sur deux points qui touchent le prix : trois langues à égalité
(six directions, trois jeux de voix et de clients) et un pilote à DEUX groupes.
"""
import html, importlib.util, json, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-hotel"
SORTIE = RACINE / "assets" / "presentations" / "hotellerie-prix.html"
E = html.escape

# Ordre de grandeur MESURÉ sur les jeux de rôle des modules (mémoire
# cout-jeu-de-role-mesure) ; le comptoir de l'hôtel n'a pas été mesuré à part.
COUT_SESSION_JEU = 0.078   # $ US par session


def nb(t):
    """Un montant ne se coupe pas en fin de ligne : « 12 000 $ », jamais « 12 / 000 $ »."""
    return re.sub(r"(\d) (?=\d{3}\b)", "\\1\u00a0", t).replace(" $", "\u00a0$")


def _charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


CSS = """
table.cmp{display:table;width:100%;min-width:0;table-layout:fixed}
table.cmp th:last-child,table.cmp td:last-child{width:34%}
.cmp td{overflow-wrap:anywhere}
.cmp td.num{text-align:right}
.autre{display:none;margin-top:10px;gap:8px;flex-wrap:wrap;align-items:center}
.autre.ouvert{display:flex}
.autre input{font:inherit;font-size:15px;padding:7px 10px;border:1px solid var(--line-fort);border-radius:8px;
  background:var(--card);color:var(--ink);width:9.5em}
.actuel{font-size:14px;color:var(--muted);margin:0 0 10px}
.actuel b{color:var(--ink)}
textarea{font:inherit;font-size:15px;width:100%;padding:10px;border:1px solid var(--line-fort);border-radius:10px;
  background:var(--card);color:var(--ink);box-sizing:border-box}
"""


def main():
    PX = _charger("hx_prix", CONTENU / "prix.py")
    LX = _charger("hx_lexique", CONTENU / "lexique.py")
    CL = _charger("hx_clients", CONTENU / "clients.py")
    FP = _charger("hx_prix_fc", RACINE / "build" / "contenu" / "entreprise-francoeur" / "prix.py")
    sons = RACINE / "assets" / "interactive" / "hotel" / "sons"
    n_voix = len([f for f in sons.rglob("*.mp3") if "lettres" not in f.parts])
    n_clients = len(CL.CLIENTS)
    memes = all(a[1] == b[1] for a, b in zip(PX.FORMULES, FP.FORMULES))
    F = {i: f for i, f in enumerate(PX.FORMULES)}

    # Une licence : 30 employés, chaque client joué deux fois dans l'année.
    sessions = 30 * n_clients * 2
    cout_an = sessions * COUT_SESSION_JEU

    decisions = [
        {"k": "pilote", "q": f"{F[0][0]} — {F[0][1]}",
         "actuel": F[0][1],
         "o": [["releve", "Relever à 4 000 à 8 000 $", True],
               ["garder", f"Garder {F[0][1]}", False],
               ["autre", "Un autre montant", False]],
         "w": "À l'hôtel, le pilote se fait avec <b>deux groupes</b> (fr → en et es → fr), qui ne se comparent pas : "
              "deux fois les séances et deux lectures du direct. Chez Francœur, il n'y en avait qu'un. Le plancher "
              "compte : ce premier prix devient celui des suivants."},
        {"k": "trousse", "q": f"{F[1][0]} — {F[1][1]}",
         "actuel": F[1][1],
         "o": [["par-langue", "12 000 à 25 000 $ pour une langue apprise, plus 4 000 $ par langue de plus", True],
               ["garder", f"Garder {F[1][1]}, toutes langues comprises", False],
               ["autre", "Un autre montant", False]],
         "w": f"Une langue de plus, c'est le lexique traduit et relu par un locuteur, un jeu de voix complet "
              f"(la trousse de l'hôtel en compte {n_voix} pour trois langues) et {n_clients} clients réécrits. "
              "Un prix unique ferait payer le client à une langue comme celui à trois — ou l'inverse."},
        {"k": "licence", "q": f"{F[2][0]} — {F[2][1]} {F[2][2]}",
         "actuel": f"{F[2][1]} {F[2][2]}",
         "o": [["garder", f"Garder {F[2][1]} par année", True],
               ["autre", "Un autre montant", False]],
         "w": f"Ce que la licence coûte à faire tourner est petit : 30 employés qui jouent chacun des {n_clients} "
              f"clients deux fois, c'est {sessions} sessions, soit environ {cout_an:.0f} $ US d'appels par année "
              f"(à {COUT_SESSION_JEU * 100:.1f} ¢ la session, mesuré sur les jeux de rôle des modules ; le comptoir "
              "de l'hôtel n'a pas été mesuré à part). Le prix paie l'hébergement, les corrections et le droit d'usage, "
              "pas les appels."},
        {"k": "affichage", "q": "Les prix sur la page acheteur",
         "actuel": "fourchettes affichées",
         "o": [["fourchettes", "Afficher les fourchettes, comme aujourd'hui", True],
               ["sur-demande", "« Sur demande » seulement, les chiffres en rencontre", False]],
         "w": "Une fourchette écrite trie les acheteurs avant la rencontre et évite une heure avec quelqu'un qui "
              "cherchait 500 $. Mais la page est privée : c'est vous qui l'envoyez, à qui vous voulez."},
    ]
    for d in decisions:
        d["q"], d["actuel"], d["w"] = nb(d["q"]), nb(d["actuel"]), nb(d["w"])
        d["o"] = [[k, nb(l), r] for k, l, r in d["o"]]
    notes = "".join(f"<li>{E(n)}</li>" for n in PX.NOTES)
    formules = "".join(
        f"<tr><td><b>{E(t)}</b><br><span style=\"color:var(--muted)\">{E(pq)}</span></td>"
        f"<td class=\"num\">{E(nb(m))}<br><span style=\"color:var(--muted)\">{E(u)}</span></td></tr>"
        for t, m, u, pq, _ in PX.FORMULES)

    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Hôtel Rive-Claire — les prix</title>", tete)
    RIVE = _charger("hx_rive", RACINE / "build" / "hotel_rive.py")
    tete = tete.replace("</style>", CSS + RIVE.CSS + "</style>", 1)

    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#hotellerie"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Hôtel Rive-Claire &middot; page acheteur</p>
<h1>Les prix à confirmer</h1>
<p class="chapeau">Les trois formules de la page acheteur ont été {"<strong>recopiées telles quelles</strong> de la Maison Francœur" if memes else "reprises de la Maison Francœur, puis retouchées"}.
L'hôtel n'a jamais été chiffré à part. Quatre décisions, chacune avec une recommandation ; l'export se recolle
dans la séance, et les montants changent à un seul endroit, <code>prix.py</code>.</p>

<section>
  <h2>Ce qui est affiché aujourd'hui</h2>
  <table class="cmp"><thead><tr><th>Formule</th><th>Montant</th></tr></thead><tbody>{formules}</tbody></table>
  <p style="margin-top:12px"><b>Les notes sous les prix :</b></p>
  <ul class="simple">{notes}</ul>
  <div class="reserve"><p><strong>D'où viennent ces fourchettes :</strong> elles ont été <b>construites</b> le
  19 septembre 2026 pour le commerce de détail, jamais relevées : aucun tarif de formation sur mesure n'est publié,
  ni au privé ni dans le réseau public. Trois règles les accompagnent et valent ici aussi : jamais à l'heure ; le
  premier prix devient le plancher des suivants ; le matériel reste le nôtre.</p></div>
</section>

<section>
  <h2>Les quatre décisions</h2>
  <div id="decisions"></div>
  <p style="margin-top:14px"><b>Un mot</b> (facultatif) — un chiffre entendu chez un acheteur, une réserve :</p>
  <textarea id="note" rows="3"></textarea>
  <p style="margin-top:1.4rem"><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button>
  <span id="etat" class="etat"></span></p>
</section>

<div class="pied"><p>Page produite par <code>build/hotel_prix.py</code> — ne pas l'éditer.
Les montants vivent dans <code>build/contenu/entreprise-hotel/prix.py</code> ; la page acheteur les lit là.</p></div>
</div>
<script>
(function(){{
  var D={json.dumps(decisions, ensure_ascii=False)};
  var CLE='hotellerie-prix', s={{choix:{{}},montant:{{}},note:''}};
  try{{ var l=JSON.parse(localStorage.getItem(CLE)||'null'); if(l&&l.choix) s=l; }}catch(e){{}}
  function sv(){{ try{{ localStorage.setItem(CLE,JSON.stringify(s)); }}catch(e){{}} }}
  var zone=document.getElementById('decisions');
  D.forEach(function(d,i){{
    var div=document.createElement('div'); div.className='dec2';
    var h='<p class="dq"><span class="dn">'+(i+1)+'</span>'+d.q+'</p><p class="actuel">Aujourd\\'hui : <b>'+d.actuel+'</b></p><div class="opts">';
    d.o.forEach(function(o){{
      h+='<button type="button" class="opt" data-k="'+d.k+'" data-v="'+o[0]+'" aria-pressed="false">'
        +o[1]+(o[2]?' <span class="tag">recommandé</span>':'')+'</button>';
    }});
    h+='</div>';
    if(d.o.some(function(o){{return o[0]==='autre';}}))
      h+='<div class="autre" data-k="'+d.k+'"><label>Montant : <input type="text" data-k="'+d.k+'" placeholder="ex. 5 000 à 9 000 $"></label></div>';
    div.innerHTML=h+'<p class="dw">'+d.w+'</p>';
    zone.appendChild(div);
  }});
  var note=document.getElementById('note'); note.value=s.note||'';
  note.addEventListener('input',function(){{ s.note=note.value; sv(); }});
  zone.querySelectorAll('input').forEach(function(i){{
    i.value=s.montant[i.dataset.k]||'';
    i.addEventListener('input',function(){{ s.montant[i.dataset.k]=i.value; sv(); }});
  }});
  function peindre(){{
    zone.querySelectorAll('.opt').forEach(function(b){{
      b.setAttribute('aria-pressed', s.choix[b.dataset.k]===b.dataset.v ? 'true':'false');
    }});
    zone.querySelectorAll('.autre').forEach(function(a){{ a.classList.toggle('ouvert', s.choix[a.dataset.k]==='autre'); }});
    var n=Object.keys(s.choix).length;
    document.getElementById('etat').textContent=n+' décision'+(n>1?'s':'')+' sur '+D.length;
  }}
  zone.addEventListener('click',function(e){{
    var b=e.target.closest('.opt'); if(!b) return;
    if(s.choix[b.dataset.k]===b.dataset.v) delete s.choix[b.dataset.k]; else s.choix[b.dataset.k]=b.dataset.v;
    sv(); peindre();
  }});
  document.getElementById('exporter').addEventListener('click',function(){{
    var out={{page:'hotellerie-prix', date:new Date().toISOString().slice(0,10), decisions:{{}}, note:s.note||''}};
    D.forEach(function(d){{
      var v=s.choix[d.k], o=d.o.filter(function(x){{return x[0]===v;}})[0];
      out.decisions[d.k]= !o ? null : (v==='autre' ? {{choix:'autre', montant:s.montant[d.k]||''}} : o[1]);
    }});
    var t=JSON.stringify(out,null,2);
    var fin=function(){{ document.getElementById('etat').textContent='Copié — recolle-le-moi.'; }};
    if(navigator.clipboard) navigator.clipboard.writeText(t).then(fin,function(){{prompt('Copiez :',t);}});
    else prompt('Copiez :',t);
  }});
  peindre();
}})();
</script>
</body></html>"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {n_voix} voix, {n_clients} clients, licence ~{cout_an:.0f} $/an d'appels"
          f"{', formules identiques à Francœur' if memes else ''}")


if __name__ == "__main__":
    main()
