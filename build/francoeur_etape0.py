#!/usr/bin/env python3
"""La page de l'étape 0 de la Maison Francœur — le lexique à valider.

Produite, jamais écrite à la main : elle lit `build/contenu/entreprise-francoeur/
lexique.py` et les croquis présents sur le disque. Relancer après toute
modification du lexique ou tout nouveau croquis.

    python3 build/francoeur_etape0.py   # → assets/presentations/francoeur-etape0.html

Les décisions (garder / retirer / douteux par mot, verdict sur le registre,
mots à ajouter) vivent dans le localStorage du poste ; « Exporter » rend un
JSON à recoller dans la séance suivante — c'est lui qui pilote la suite.
"""
import html, json, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build" / "contenu" / "entreprise-francoeur"))
from lexique import LEXIQUE, PLANCHES, par_planche, verifier  # noqa: E402

CROQUIS = RACINE / "assets" / "interactive" / "francoeur" / "croquis"
SORTIE = RACINE / "assets" / "presentations" / "francoeur-etape0.html"
TETE_DE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"

# Les pastilles : composées en HTML, jamais engendrées. Une teinte écrite ne
# se trompe pas ; une teinte dessinée par un modèle, si.
TEINTES = {
    "noir": "#1b1b1b", "blanc": "#ffffff", "gris": "#9a9ea3", "marine": "#1f2f56",
    "bleu": "#2f6fc0", "rouge": "#c62f2f", "vert": "#2f8a4c", "jaune": "#f1c93b",
    "rose": "#ee9cbc", "mauve": "#8a5cb8", "brun": "#7a4e2d", "beige": "#dcc9a6",
    "kaki": "#7d7a45", "bourgogne": "#7a1f33",
}
MOTIFS = {
    "uni": "background:#1f2f56",
    "raye": "background:repeating-linear-gradient(0deg,#1f2f56 0 9px,#f4f1e8 9px 18px)",
    "carreaute": ("background-color:#f4f1e8;background-image:"
                  "linear-gradient(90deg,rgba(198,47,47,.55) 50%,transparent 50%),"
                  "linear-gradient(rgba(198,47,47,.55) 50%,transparent 50%);"
                  "background-size:22px 22px"),
    "pois": ("background-color:#1f2f56;background-image:radial-gradient(#f4f1e8 22%,"
             "transparent 24%);background-size:16px 16px"),
}

E = html.escape


def image_de(e):
    ident, _, mot, _, dessin, _ = e
    if dessin == "pastille":
        style = MOTIFS.get(ident) or f"background:{TEINTES.get(ident, '#ccc')}"
        return f'<div class="img pastille" style="{style}" aria-hidden="true"></div>'
    if dessin == "croquis":
        if (CROQUIS / f"{ident}.jpg").exists():
            return (f'<img class="img" src="/assets/interactive/francoeur/croquis/{ident}.jpg"'
                    f' alt="{E(mot)}" loading="lazy">')
        return '<div class="img attente">croquis<br>à venir</div>'
    return '<div class="img rien">sans image</div>'


def carte(e):
    ident, _, mot, autre, dessin, note = e
    piege = note.startswith("PIÈGE")
    return (
        f'<article class="mot{" piege" if piege else ""}" data-id="{ident}">'
        f'{image_de(e)}'
        f'<p class="ici">{E(mot)}</p>'
        + (f'<p class="autre">{E(autre)}</p>' if autre else '<p class="autre vide">—</p>')
        + (f'<p class="note">{E(note)}</p>' if note else "")
        + '<div class="choix">'
          '<button type="button" data-v="garder" aria-pressed="false">Garder</button>'
          '<button type="button" data-v="retirer" aria-pressed="false">Retirer</button>'
          '<button type="button" data-v="douteux" aria-pressed="false">À revoir</button>'
          '</div></article>')


def main():
    verifier()
    groupes = par_planche()
    n_c = sum(1 for e in LEXIQUE if e[4] == "croquis")
    n_p = sum(1 for e in LEXIQUE if e[4] == "pastille")
    n_faits = sum(1 for e in LEXIQUE if e[4] == "croquis" and (CROQUIS / f"{e[0]}.jpg").exists())
    n_pieges = sum(1 for e in LEXIQUE if e[5].startswith("PIÈGE"))

    tete = TETE_DE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Maison Francœur — étape 0</title>", tete)
    tete = tete.replace("</style>", CSS + "</style>", 1)

    temoins = "".join(
        f'<figure><img src="/assets/interactive/francoeur/croquis/{i}.jpg" alt="{E(m)}">'
        f'<figcaption>{E(m)}</figcaption></figure>'
        for i, m in (("chandail", "un chandail rayé marine"), ("parka", "un parka"),
                     ("espadrilles", "des espadrilles"))
        if (CROQUIS / f"{i}.jpg").exists())

    sections = []
    for k, titre in PLANCHES:
        cartes = "".join(carte(e) for e in groupes[k])
        sections.append(f'<section class="planche" id="p-{k}"><h2>{E(titre)} '
                        f'<span class="compte">{len(groupes[k])}</span></h2>'
                        f'<div class="grille">{cartes}</div></section>')

    corps = f"""<body>
<div class="doc large">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Maison Francœur &middot; étape 0 du plan</p>
<h1>Le lexique du magasin, à valider</h1>
<p class="chapeau"><strong>{len(LEXIQUE)} mots</strong> rangés en {len(PLANCHES)} planches, comme un
magasin est rangé. Le mot en gras est celui que le client dira au Québec&nbsp;; l'autre, en
dessous, est celui qu'on entendra aussi. <strong>{n_pieges} pièges</strong> sont signalés en ambre
&mdash; des mots qui veulent dire autre chose en France, ou deux choses ici. Marquez ce qui
reste, ce qui part et ce qui est à revoir&nbsp;; ajoutez ce qui manque en bas.</p>

<div class="chiffres">
  <div class="ch"><span class="n">{len(LEXIQUE)}</span><span class="q">mots au lexique</span></div>
  <div class="ch"><span class="n">{n_c}</span><span class="q">croquis à produire &mdash; {n_faits} faits, ≈&nbsp;{(n_c - n_faits) * 0.067:.0f}&nbsp;$ pour le reste</span></div>
  <div class="ch"><span class="n">{n_p}</span><span class="q">pastilles composées en HTML, sans coût</span></div>
  <div class="ch"><span class="n">{len(LEXIQUE) - n_c - n_p}</span><span class="q">mots sans image (tailles, matières, service)</span></div>
</div>

<section class="premier">
  <h2>Le registre, sur trois témoins</h2>
  <p>Trait noir, aplat de couleur discret, le vêtement seul à plat &mdash; le dessin des
  catalogues de mode. Trois essais choisis pour leurs risques&nbsp;: <b>un motif et une
  couleur</b> (le rayé marine), <b>des détails nommés</b> (capuchon, fermeture éclair,
  poches), <b>une paire</b> (les chaussures). Les trois sont sortis justes du premier appel,
  sans texte ni mannequin.</p>
  <div class="temoins">{temoins}</div>
  <div class="verdict" data-k="registre">
    <button type="button" data-v="ok" aria-pressed="false">Ce registre me va &mdash; on produit les {n_c}</button>
    <button type="button" data-v="revoir" aria-pressed="false">À ajuster avant de produire</button>
  </div>
  <p class="aide">Une remarque sur le dessin&nbsp;? Écrivez-la dans la case du bas, elle part avec l'export.</p>
</section>

<section>
  <h2>Les couleurs et les motifs sont des pastilles</h2>
  <p>Une couleur dessinée par un modèle d'image dérive d'un tirage à l'autre&nbsp;; une couleur
  écrite en HTML, jamais. Les quatorze couleurs et quatre des six motifs sont donc composés
  dans la page. Seuls <em>fleuri</em> et <em>imprimé</em> demandent un croquis.</p>
</section>

<nav class="sommaire">{"".join(f'<a href="#p-{k}">{E(t)}</a>' for k, t in PLANCHES)}</nav>

{"".join(sections)}

<section>
  <h2>Ce qui manque</h2>
  <p>Un mot par ligne. S'il a un équivalent, après une barre&nbsp;: <code>un chandail à col en V / un pull col V</code>.</p>
  <textarea id="ajouts" rows="6" placeholder="un pantalon capri&#10;des bretelles / des bretelles"></textarea>
  <p><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button>
  <span id="etat" class="etat"></span></p>
</section>

<div class="pied">
  <p>Étape 0 · {len(LEXIQUE)} mots · page produite par <code>build/francoeur_etape0.py</code> depuis
  <code>build/contenu/entreprise-francoeur/lexique.py</code> &mdash; ne pas l'éditer.</p>
</div>
</div>
<script>{JS}</script>
</body>
</html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {len(LEXIQUE)} mots, {n_faits}/{n_c} croquis")


CSS = """
/* ── étape 0 : planches du lexique ── */
.doc.large{max-width:1180px}
.chiffres{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.temoins{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:16px 0}
.temoins figure{margin:0;background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px}
.temoins img{width:100%;display:block}
.temoins figcaption{text-align:center;font-weight:700;color:#17181A;margin-top:6px}
.verdict,.choix{display:flex;flex-wrap:wrap;gap:8px}
.verdict button,.choix button{font:inherit;cursor:pointer;background:var(--sunken);color:var(--body);
  border:1px solid var(--line-fort);border-radius:10px;padding:8px 12px}
.choix button{font-size:13px;padding:5px 8px;border-radius:8px}
button[aria-pressed="true"][data-v="ok"],button[aria-pressed="true"][data-v="garder"]{background:var(--fait-bg);border-color:var(--fait);color:var(--ink);font-weight:700}
button[aria-pressed="true"][data-v="retirer"]{background:var(--loi-bg);border-color:var(--loi);color:var(--ink);font-weight:700}
button[aria-pressed="true"][data-v="douteux"],button[aria-pressed="true"][data-v="revoir"]{background:var(--decid-bg);border-color:var(--decid);color:var(--ink);font-weight:700}
.aide{color:var(--muted);font-size:15px}
.sommaire{position:sticky;top:0;z-index:2;background:var(--ground);display:flex;flex-wrap:wrap;gap:6px 14px;
  padding:10px 0;border-bottom:1px solid var(--line);margin:24px 0 8px;font-size:15px}
.sommaire a{color:var(--acier);text-decoration:none;font-weight:700}
.planche h2 .compte{font-size:15px;color:var(--muted);font-weight:600;margin-left:6px}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:12px}
.mot{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px;display:flex;flex-direction:column;gap:4px}
.mot.piege{border-color:var(--decid);box-shadow:inset 0 3px 0 var(--decid)}
.mot[data-etat="retirer"]{opacity:.45}
.mot .img{width:100%;aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:8px}
.mot .pastille{aspect-ratio:3/2;border:1px solid var(--line-fort)}
.mot .attente,.mot .rien{display:grid;place-items:center;text-align:center;font-size:13px;color:var(--muted);
  background:var(--sunken);border:1px dashed var(--line-fort);aspect-ratio:3/2}
.mot .ici{margin:4px 0 0;font-weight:800;color:var(--ink);font-size:17px;line-height:1.25}
.mot .autre{margin:0;color:var(--muted);font-size:14px}
.mot .autre.vide{opacity:.4}
.mot .note{margin:2px 0;font-size:13px;line-height:1.4;color:var(--body)}
.mot.piege .note{color:var(--decid);font-weight:700}
.mot .choix{margin-top:auto;padding-top:6px}
@media (max-width:640px){
  .grille{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
  .sommaire{flex-wrap:nowrap;overflow-x:auto;white-space:nowrap}
  .mot .ici{font-size:15px}
}
textarea{width:100%;font:inherit;font-size:15px;padding:10px;border-radius:10px;border:1px solid var(--line-fort);
  background:var(--card);color:var(--ink)}
"""

JS = r"""
(function(){
  var CLE='francoeur-etape0', s={mots:{},registre:null,ajouts:''};
  try{ var l=JSON.parse(localStorage.getItem(CLE)||'null'); if(l) s=l; }catch(e){}
  function sauver(){ try{ localStorage.setItem(CLE,JSON.stringify(s)); }catch(e){} }
  function peindre(){
    document.querySelectorAll('.mot').forEach(function(m){
      var v=s.mots[m.dataset.id]; m.dataset.etat=v||'';
      m.querySelectorAll('button').forEach(function(b){ b.setAttribute('aria-pressed', v===b.dataset.v?'true':'false'); });
    });
    document.querySelectorAll('.verdict button').forEach(function(b){
      b.setAttribute('aria-pressed', s.registre===b.dataset.v?'true':'false'); });
    var n=Object.keys(s.mots).length, t=document.querySelectorAll('.mot').length;
    document.getElementById('etat').textContent=n+' mots marqués sur '+t;
  }
  document.addEventListener('click',function(e){
    var b=e.target.closest('.choix button'), m=b&&b.closest('.mot');
    if(m){ var id=m.dataset.id; if(s.mots[id]===b.dataset.v) delete s.mots[id]; else s.mots[id]=b.dataset.v; sauver(); peindre(); return; }
    var r=e.target.closest('.verdict button');
    if(r){ s.registre = s.registre===r.dataset.v ? null : r.dataset.v; sauver(); peindre(); }
  });
  var ta=document.getElementById('ajouts'); ta.value=s.ajouts||'';
  ta.addEventListener('input',function(){ s.ajouts=ta.value; sauver(); });
  document.getElementById('exporter').addEventListener('click',function(){
    var out={etape:'francoeur-etape0',date:new Date().toISOString().slice(0,10),
      registre:s.registre, retirer:[], douteux:[], garder:Object.keys(s.mots).filter(function(k){return s.mots[k]==='garder';}).length,
      ajouts:(s.ajouts||'').split('\n').map(function(x){return x.trim();}).filter(Boolean)};
    Object.keys(s.mots).forEach(function(k){ if(s.mots[k]==='retirer') out.retirer.push(k); if(s.mots[k]==='douteux') out.douteux.push(k); });
    var t=JSON.stringify(out,null,2);
    var fin=function(){ document.getElementById('etat').textContent='Copié — à recoller dans la séance suivante.'; };
    if(navigator.clipboard) navigator.clipboard.writeText(t).then(fin,function(){prompt('Copiez :',t);}); else prompt('Copiez :',t);
  });
  peindre();
})();
"""

if __name__ == "__main__":
    main()
