#!/usr/bin/env python3
"""La page de l'étape 0 de la trousse de restauration — le cadrage à valider.

    python3 build/restauration_etape0.py   # → assets/presentations/restauration/restauration-etape0.html

Produite, jamais éditée. Elle lit `build/contenu/entreprise-restaurant/lexique.py`,
les croquis de `assets/interactive/restaurant/croquis/` et les extraits de
`assets/presentations/restauration/voix/` (s'ils existent).

Ce qui demande le jugement de Daniel : les objectifs, le nom, le registre du
dessin, le décor (laissé sans réponse au plan), les voix, le lexique mot par mot,
ce qui manque. « Exporter » rend un JSON à recoller dans la séance suivante.
"""
import html, importlib.util, json, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
_s = importlib.util.spec_from_file_location("resto_lexique", RACINE / "build/contenu/entreprise-restaurant/lexique.py")
LX = importlib.util.module_from_spec(_s); _s.loader.exec_module(LX)

CROQUIS = RACINE / "assets" / "interactive" / "restaurant" / "croquis"
VOIX = RACINE / "assets" / "presentations" / "restauration" / "voix"
SORTIE = RACINE / "assets" / "presentations" / "restauration" / "restauration-etape0.html"
TETE_DE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
E = html.escape

# ── Le nom : cherché le 30 sept. 2026, nom exact entre guillemets ──────────
NOMS = [
    ("jocelyne", "Chez Jocelyne", True,
     "Aucun restaurant de ce nom trouvé (deux recherches, 30 sept.). Une « Jocelyne » cuisine au Restaurant Chez Pascal, à Embrun (France) : le prénom, pas l'enseigne.",
     "Trois syllabes nettes, un prénom très d'ici pour une propriétaire de restaurant familial ; se dit bien en commande (« Chez Jocelyne, bonjour ! »)."),
    ("alderic", "Chez Aldéric", False,
     "Aucun restaurant de ce nom. Le plus proche : « Chez Alcide », un chalet-restaurant en Savoie — un autre prénom.",
     "Un vieux prénom québécois, rare, chaleureux ; un peu plus dur à dire pour un débutant (le « d » et le « r » rapprochés)."),
    ("beaulac", "Restaurant Beaulac", False,
     "Aucun restaurant de ce nom trouvé (première ronde). Beaulac est un nom de lieu et de famille d'ici.",
     "Facile à dire, sonne vrai ; plus neutre, moins chaleureux qu'un « Chez »."),
]
ECARTES = [
    ("Chez Ovila", "refusé par vous le 30 sept."),
    ("Chez Martin", "votre premier choix ; aucun au Québec, mais pris en France (Rambouillet), en Belgique (Liège) et en Suisse — écarté à votre demande."),
    ("Chez Réjean", "un restaurant de Saint-Pamphile — écarté."),
    ("Chez Denise", "Saint-Sauveur et Shannon, et une série de Radio-Canada dont c'est le décor — écarté."),
    ("Chez Normand", "le Casse-croûte Normand sert de la poutine à Verdun depuis 1964 — écarté."),
    ("Chez Lucien", "Ottawa (ByWard) et Lyon — écarté."),
    ("Chez Rita", "une taqueria rue Saint-Jean à Québec, un italien à Verdun, deux à Paris — écarté."),
    ("Chez Huguette · Chez Fernande · Chez Albertine · Chez Gédéon", "tous pris en France ou en Belgique — écartés."),
    ("Chez Gisèle · Chez Yvon · Chez Ghislain · Chez Rolande", "trop proches d'enseignes existantes (Gisèle Buvette à Québec, Chez Yvonne, Chez Ghislaine, Restaurant Rolande) — écartés."),
    ("Chez Rosaire · La Bonne Fourchette · Chez Clovis · Chez Mado · Chez Aurèle", "première ronde : Shawinigan, Donnacona, France, Corse — écartés."),
]

OBJECTIFS = [
    ("O1", "cuisine", "Exécuter une consigne du chef",
     "entendue une fois, au débit réel et dans le bruit de la cuisine, en la redisant (« Oui, chef : deux burgers, un sans fromage »)",
     "7 consignes sur 8 justes"),
    ("O2", "les deux", "Traiter une allergie",
     "annoncée par la salle ou demandée par un client : la faire répéter, la transmettre, vérifier — jamais affirmer qu'un allergène est absent",
     "toutes — une seule erreur fait échouer (éliminatoire, dit d'avance)"),
    ("O3", "les deux", "Reconnaître les objets, les aliments et les gestes du poste",
     "entendus seuls ou dans une phrase, sur le décor ou les planches",
     "18 mots sur 20"),
    ("O4", "salle", "Prendre une commande modifiée",
     "« sans », « avec », « à part », « bien cuit » — et la redire au client avant de l'envoyer",
     "5 commandes sur 6 exactes, modifications comprises"),
]
ALIGNEMENT = [
    ("O1", "La consigne du chef (avec le bruit, réglable)", "Partie B · la consigne entendue", "Le premier quart · Le rush"),
    ("O2", "L'allergie (avec un contre-exemple par série)", "Partie C · qui décide, je vérifie", "Une allergie arrive de la salle · « Y a-t-il des noix ? »"),
    ("O3", "J'entends et je trouve · Le mot et son image · Je me souviens · Les pièges", "Partie A · les mots", "Toutes"),
    ("O4", "La commande modifiée", "Partie B · la commande entendue (porte salle)", "Une commande avec des changements"),
]

TEMOINS = [("etiquette", "L'étiquette d'un bac", "Un objet qui porte d'ordinaire un texte et une date : ici, trois barres grises, aucune lettre."),
           ("thermometre", "Le thermomètre", "Un cadran à chiffres : ici, les graduations seules et l'aiguille."),
           ("poutine", "La poutine", "Une matière difficile (la sauce, le fromage en grains) : elle se reconnaît.")]


def img(e):
    ident, _, mot, _, dessin, _ = e
    if dessin == "croquis" and (CROQUIS / f"{ident}.jpg").exists():
        return f'<img class="img" src="/assets/interactive/restaurant/croquis/{ident}.jpg" alt="{E(mot)}" loading="lazy">'
    if dessin == "croquis":
        return '<div class="img attente">croquis<br>à venir</div>'
    if dessin == "decor":
        return '<div class="img attente">sur le<br>décor</div>'
    return '<div class="img rien">sans image</div>'


def carte(e):
    ident, _, mot, autre, dessin, note = e
    piege = note.startswith("PIÈGE")
    return (f'<article class="mot{" piege" if piege else ""}" data-id="{ident}">{img(e)}'
            f'<p class="ici">{E(mot)}</p>'
            + (f'<p class="autre">{E(autre)}</p>' if autre else '<p class="autre vide">—</p>')
            + (f'<p class="note">{E(note)}</p>' if note else "")
            + '<div class="choix"><button type="button" data-v="garder" aria-pressed="false">Garder</button>'
              '<button type="button" data-v="retirer" aria-pressed="false">Retirer</button>'
              '<button type="button" data-v="douteux" aria-pressed="false">À revoir</button></div></article>')


def option(groupe, val, titre, texte, reco):
    return (f'<button type="button" class="opt" data-g="{groupe}" data-v="{val}" aria-pressed="false">'
            f'<b>{E(titre)}</b>{" <span class=tag>recommandé</span>" if reco else ""}'
            f'<span class="det">{texte}</span></button>')


CSS = """
.doc.large{max-width:1180px}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(168px,1fr));gap:12px}
.mot{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px;display:flex;flex-direction:column;gap:4px}
.mot.piege{border-color:#C8692A;box-shadow:inset 0 0 0 1px #C8692A}
.mot .img{width:100%;aspect-ratio:1;object-fit:contain;background:#fff;border-radius:8px}
.mot .attente,.mot .rien{display:grid;place-items:center;text-align:center;font-size:12px;color:var(--muted);background:var(--sunken)}
.mot .ici{margin:4px 0 0;font-weight:800;color:var(--ink);font-size:15px}
.mot .autre{margin:0;font-size:13px;color:var(--muted)} .mot .autre.vide{opacity:.5}
.mot .note{margin:2px 0 0;font-size:12.5px;line-height:1.35;color:var(--body)}
.mot.piege .note{color:#8a4312}
.choix{display:flex;gap:4px;margin-top:auto;padding-top:6px}
.choix button{flex:1;font:inherit;font-size:12px;font-weight:700;padding:6px 2px;border-radius:8px;border:1px solid var(--line-fort);background:var(--sunken);color:var(--body);cursor:pointer}
.choix button[aria-pressed=true][data-v=garder]{background:#DCF2E6;border-color:#0A8F5B;color:#0b3d27}
.choix button[aria-pressed=true][data-v=retirer]{background:#FBE4E0;border-color:#B42318;color:#5c130c}
.choix button[aria-pressed=true][data-v=douteux]{background:#FBEEDC;border-color:#B45309;color:#5a2c05}
.planche h2 .compte,.planche h2 .poste{font-size:13px;font-weight:700;color:var(--muted);margin-left:8px}
.opts2{display:grid;gap:10px}
.opt{display:block;text-align:left;font:inherit;background:var(--card);border:1px solid var(--line-fort);border-radius:12px;padding:12px 14px;cursor:pointer;color:var(--body)}
.opt[aria-pressed=true]{border-color:#0A8F5B;box-shadow:inset 0 0 0 2px #0A8F5B}
.opt .det{display:block;font-size:14px;color:var(--muted);margin-top:4px}
.opt .tag{font-size:12px;color:#B45309;font-weight:700}
.temoins{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px}
.temoins figure{margin:0;background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px}
.temoins img{width:100%;aspect-ratio:1;object-fit:contain}
.temoins figcaption{font-size:14px;color:var(--body)} .temoins figcaption b{display:block;color:var(--ink)}
.decor img{width:100%;border:1px solid var(--line);border-radius:12px;background:#fff}
audio{width:100%;max-width:360px}
textarea{width:100%;font:inherit;font-size:15px;padding:10px;border-radius:10px;border:1px solid var(--line-fort);background:var(--card);color:var(--ink);box-sizing:border-box}
table.cmp{display:block;max-width:100%;min-width:0;overflow-x:auto}
@media (max-width:640px){.grille{grid-template-columns:repeat(2,1fr)}table.cmp{font-size:14px}table.cmp td{min-width:8em}}
"""


def main():
    LX.verifier()
    g = LX.par_planche()
    n = len(LX.LEXIQUE)
    n_c = sum(1 for e in LX.LEXIQUE if e[4] == "croquis")
    n_p = sum(1 for e in LX.LEXIQUE if e[5].startswith("PIÈGE"))
    voix = sorted(VOIX.glob("*.mp3")) if VOIX.exists() else []

    tete = TETE_DE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>La restauration — étape 0</title>", tete)
    tete = tete.replace("</style>", CSS + "</style>", 1)

    obj = "".join(f"<tr><td><b>{o}</b></td><td>{E(p)}</td><td><b>{E(v)}</b> — {E(c)}</td><td>{E(cr)}</td></tr>"
                  for o, p, v, c, cr in OBJECTIFS)
    ali = "".join(f"<tr><td><b>{o}</b></td><td>{E(x)}</td><td>{E(t)}</td><td>{E(s)}</td></tr>" for o, x, t, s in ALIGNEMENT)
    noms = "".join(option("nom", k, n_, f"<b>Recherche :</b> {E(r)}<br><b>À l'oreille :</b> {E(a)}", reco)
                   for k, n_, reco, r, a in NOMS)
    ecartes = "".join(f"<li><b>{E(n_)}</b> : {E(r)}</li>" for n_, r in ECARTES)
    temoins = "".join(f'<figure><img src="/assets/interactive/restaurant/croquis/{i}.jpg" alt="{E(t)}">'
                      f'<figcaption><b>{E(t)}</b>{E(d)}</figcaption></figure>'
                      for i, t, d in TEMOINS if (CROQUIS / f"{i}.jpg").exists())
    if voix:
        v_html = "".join(f'<p><b>{E(f.stem)}</b><br><audio controls preload="none" '
                         f'src="/assets/presentations/restauration/voix/{f.name}"></audio></p>' for f in voix)
    else:
        v_html = ('<div class="reserve"><p><strong>Pas d\'extrait pour l\'instant :</strong> le 30 septembre, Azure refuse '
                  'la clé de synthèse (401, y compris sur la liste des voix). Les deux voix du Québec sont celles du '
                  'français de l\'hôtel, Sylvie et Thierry : vous les connaissez déjà. Deux phrases par voix seront '
                  'ajoutées ici dès que la clé passe — une consigne du chef, une annonce de la salle.</p></div>')
    sections = "".join(
        f'<section class="planche" id="p-{k}"><h2>{E(t)}<span class="poste">{E(p)}</span>'
        f'<span class="compte">{len(g[k])}</span></h2><div class="grille">{"".join(carte(e) for e in g[k])}</div></section>'
        for k, t, p in LX.PLANCHES)

    corps = f"""<body>
<div class="doc large">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">La restauration &middot; étape 0</p>
<h1>Le cadrage, à valider</h1>
<p class="chapeau">Le plan est tranché : deux portes, <b>la cuisine d'abord</b>, un restaurant familial québécois, la
formule Francœur, les allergies éliminatoires, le bruit de la cuisine. Voici ce qu'il faut arrêter avant de
dessiner : les objectifs, le nom, le dessin et le décor, les voix, puis <b>{n} mots</b> un par un.
La visite en cuisine, décidée avant l'étape 1, viendra corriger ce lexique.</p>

<div class="chiffres">
  <div class="ch"><span class="n">{n}</span><span class="q">mots en {len(LX.PLANCHES)} planches</span></div>
  <div class="ch"><span class="n">{n_c}</span><span class="q">croquis à produire, ≈&nbsp;{n_c * 0.067:.0f}&nbsp;$</span></div>
  <div class="ch"><span class="n">{n_p}</span><span class="q">pièges d'ici (déjeuner, dîner, souper…)</span></div>
  <div class="ch"><span class="n">4</span><span class="q">objectifs, dont un éliminatoire</span></div>
</div>

<section class="premier">
  <h2>1 · Le public, l'écart, les objectifs</h2>
  <p><b>Le public</b> : des gens qui commencent en restaurant sans parler encore français — à la plonge, à la
  préparation, comme commis ; en salle ensuite. Niveaux 1 à 3, sur leur téléphone, par morceaux de dix minutes.</p>
  <p><b>L'écart</b> : ils connaissent parfois le mot, ils ne comprennent pas la consigne dite vite, de dos, dans le
  bruit ; et devant une allergie, ils répondent pour ne pas déranger.</p>
  <table class="cmp"><thead><tr><th></th><th>Porte</th><th>Objectif — condition</th><th>Critère</th></tr></thead><tbody>{obj}</tbody></table>
  <p style="margin-top:14px"><b>L'alignement</b> — chaque objectif a son exercice, sa question de test et sa situation :</p>
  <table class="cmp"><thead><tr><th></th><th>Exercice</th><th>Test</th><th>Situation jouée</th></tr></thead><tbody>{ali}</tbody></table>
  <div class="reserve"><p><strong>L'éliminatoire est dit avant</strong>, en une phrase affichée au début des exercices, du
  test et des situations : « Une allergie se vérifie toujours. Répondre “il n'y en a pas” sans vérifier fait
  échouer. » Chaque série d'allergies garde un contre-exemple, où la question ne porte pas sur un allergène.</p></div>
  <div class="opts2" style="margin-top:12px">
    {option("objectifs", "oui", "Ces objectifs me vont", "On aligne les exercices et le test dessus.", True)}
    {option("objectifs", "ajuster", "À ajuster", "Dites quoi dans « Ce qui manque », en bas.", False)}
  </div>
</section>

<section>
  <h2>2 · Le nom du restaurant</h2>
  <div class="these"><p class="cle">Deuxième ronde, 30 septembre : « Chez Ovila » et « Chez Martin » écartés à votre
  demande. Les prénoms d'ici derrière un « Chez » sont presque tous pris ; trois candidats restent libres.</p></div>
  <p>Trois candidats, cherchés un à un sur le Web, nom exact entre guillemets. Ce n'est pas une recherche de marque
  de commerce : on vérifie seulement qu'aucun restaurant connu ne le porte.</p>
  <div class="opts2">{noms}</div>
  <p style="margin-top:10px"><b>Écartés :</b></p><ul class="simple">{ecartes}</ul>
</section>

<section>
  <h2>3 · Le dessin et le décor</h2>
  <p>Le registre de Francœur et de l'hôtel : trait noir égal, aplat doux, fond blanc. Trois témoins choisis pour
  leurs risques :</p>
  <div class="temoins">{temoins}</div>
  <div class="opts2" style="margin-top:12px">
    {option("registre", "garder", "Le registre tient", "On dessine les autres croquis de la même façon.", True)}
    {option("registre", "retoucher", "À retoucher", "Dites quoi en bas.", False)}
  </div>
  <p style="margin-top:18px"><b>Le décor</b> — laissé sans réponse au plan. Voici le poste de travail dessiné, vu de la
  place du commis : la planche et le couteau, les bacs, la plaque, la friteuse, le passe et ses billets (vierges), la
  plonge à gauche. L'ouverture du passe reste <b>vide</b> : le chef y paraîtra, puis le serveur.</p>
  <figure class="decor"><img src="/assets/interactive/restaurant/croquis/poste.jpg" alt="Le poste de travail dessiné"></figure>
  <div class="opts2" style="margin-top:12px">
    {option("decor", "dessin", "Ce décor dessiné, fixe", "Les objets s'y touchent ; il sert ensuite de fond aux situations en cuisine.", True)}
    {option("decor", "photo", "Une photo de cuisine", "Plus réaliste, mais elle porterait étiquettes et marques illisibles, et changerait d'un tirage à l'autre.", False)}
  </div>
</section>

<section>
  <h2>4 · Les voix</h2>
  {v_html}
</section>

<section>
  <h2>5 · Le lexique, mot par mot</h2>
  <p>Le mot en gras est celui qu'on dira en cuisine ou en salle au Québec ; dessous, l'autre qu'on entendra. Les
  pièges sont encadrés. La porte de chaque planche (cuisine, salle, les deux) décide où elle paraît.
  <button type="button" class="btn-export" id="toutGarder" style="margin-left:8px">Tout garder ce qui n'est pas marqué</button></p>
  {sections}
</section>

<section>
  <h2>Ce qui manque</h2>
  <p>Des mots, des consignes que vous entendez en cuisine, un objectif à reprendre :</p>
  <textarea id="manque" rows="5"></textarea>
  <p style="margin-top:1.2rem"><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button>
  <span id="etat" class="etat"></span></p>
</section>

<div class="pied"><p>Produite par <code>build/restauration_etape0.py</code> — ne pas l'éditer. Lexique :
<code>build/contenu/entreprise-restaurant/lexique.py</code>.</p></div>
</div>
<script>
(function(){{
  var CLE='restauration-etape0', s={{mots:{{}},choix:{{}},manque:''}};
  try{{var l=JSON.parse(localStorage.getItem(CLE)||'null');if(l&&l.mots)s=l;}}catch(e){{}}
  function sv(){{try{{localStorage.setItem(CLE,JSON.stringify(s));}}catch(e){{}}}}
  var N={n};
  function peindre(){{
    document.querySelectorAll('.mot').forEach(function(m){{var v=s.mots[m.dataset.id];
      m.querySelectorAll('.choix button').forEach(function(b){{b.setAttribute('aria-pressed',b.dataset.v===v);}});}});
    document.querySelectorAll('.opt').forEach(function(b){{b.setAttribute('aria-pressed',s.choix[b.dataset.g]===b.dataset.v);}});
    document.getElementById('etat').textContent=Object.keys(s.mots).length+' mots marqués sur '+N+' · '+Object.keys(s.choix).length+' choix sur 4';
  }}
  document.addEventListener('click',function(e){{
    var b=e.target.closest('.choix button');
    if(b){{var id=b.closest('.mot').dataset.id; if(s.mots[id]===b.dataset.v)delete s.mots[id]; else s.mots[id]=b.dataset.v; sv(); peindre(); return;}}
    var o=e.target.closest('.opt');
    if(o){{if(s.choix[o.dataset.g]===o.dataset.v)delete s.choix[o.dataset.g]; else s.choix[o.dataset.g]=o.dataset.v; sv(); peindre();}}
  }});
  document.getElementById('toutGarder').onclick=function(){{document.querySelectorAll('.mot').forEach(function(m){{if(!s.mots[m.dataset.id])s.mots[m.dataset.id]='garder';}});sv();peindre();}};
  var t=document.getElementById('manque'); t.value=s.manque||''; t.oninput=function(){{s.manque=t.value;sv();}};
  document.getElementById('exporter').onclick=function(){{
    var r=[],d=[]; Object.keys(s.mots).forEach(function(k){{if(s.mots[k]==='retirer')r.push(k); if(s.mots[k]==='douteux')d.push(k);}});
    var out={{page:'restauration-etape0',date:new Date().toISOString().slice(0,10),choix:s.choix,
      gardes:Object.keys(s.mots).filter(function(k){{return s.mots[k]==='garder';}}).length,sur:N,retirer:r,a_revoir:d,manque:s.manque||''}};
    var txt=JSON.stringify(out,null,2),fin=function(){{document.getElementById('etat').textContent='Copié — recolle-le-moi.';}};
    if(navigator.clipboard)navigator.clipboard.writeText(txt).then(fin,function(){{prompt('Copiez :',txt);}});else prompt('Copiez :',txt);
  }};
  peindre();
}})();
</script>
</body></html>"""
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {n} mots, {n_c} croquis, {len(voix)} extraits de voix")


if __name__ == "__main__":
    main()
