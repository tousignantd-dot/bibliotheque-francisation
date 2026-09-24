#!/usr/bin/env python3
"""La page de l'étape 0 de la trousse de réception — le cadrage à valider.

Produite, jamais écrite à la main. Elle lit `build/contenu/entreprise-hotel/
lexique.py`, les croquis de `assets/interactive/hotel/croquis/` et les
extraits de `assets/presentations/hotel-voix/`.

    python3 build/hotellerie_etape0.py   # → assets/presentations/hotellerie-etape0.html

Tout ce qui demande le jugement de Daniel y est : le nom, les deux directions
du pilote, le registre du dessin, le comptoir, les voix anglaises, le lexique
mot par mot. « Exporter » rend un JSON à recoller dans la séance suivante.
"""
import html, importlib.util, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
_p = RACINE / "build" / "contenu" / "entreprise-hotel" / "lexique.py"
_s = importlib.util.spec_from_file_location("hotel_lexique", _p)
LX = importlib.util.module_from_spec(_s); _s.loader.exec_module(LX)

CROQUIS = RACINE / "assets" / "interactive" / "hotel" / "croquis"
VOIX = RACINE / "assets" / "presentations" / "hotel-voix"
SORTIE = RACINE / "assets" / "presentations" / "hotellerie-etape0.html"
TETE_DE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
E = html.escape
DRAPEAU = {"fr": "FR", "en": "EN", "es": "ES"}

# ── Le nom : vérifié par recherche le 24 sept. 2026 (exact, guillemets) ──
NOMS = [
    ("rive-claire", "Hôtel Rive-Claire", True,
     "Aucun hôtel de ce nom trouvé. Le plus proche : le « Domaine de Claire Rive », une résidence de tourisme à Prayssac (France) — ordre inversé, autre pays.",
     "Se dit sans peine dans les trois langues ; évoque un bord d'eau sans nommer de ville."),
    ("cap-aurore", "Hôtel Cap-Aurore", False,
     "Aucun hôtel de ce nom. « Hôtel Aurore » existe à Paris (gare de Lyon) et à Lomé : le mot seul est pris, l'ensemble ne l'est pas.",
     "« Cap » passe en anglais et en espagnol ; « Aurore » se reconnaît (aurora)."),
    ("brise-lune", "Hôtel Brise-Lune", False,
     "Aucun hôtel de ce nom. Des « La Brise » et « Brise Marine » existent (France, Brésil, Algérie).",
     "Joli en français, mais « Brise » et « Lune » sont durs pour un anglophone : c'est le moins trilingue des trois."),
]
ECARTES = [
    ("Hôtel Le Mirador", "existe au Québec (Saint-Alphonse-de-Granby) — écarté."),
    ("Hôtel Marelle", "le Marelle Hotel Boutique existe à Playa del Carmen, au Mexique — la variété d'espagnol choisie. Écarté."),
    ("Hôtel Belle-Anse", "Résidence Belle Anse en Martinique, et une ville d'Haïti — écarté."),
]

DIRECTIONS = [
    ("fr-en", "Je parle français · j'apprends l'anglais", True,
     "La réceptionniste d'ici devant la clientèle touristique : le cas le plus fréquent à Québec et à Montréal."),
    ("es-fr", "Je parle espagnol · j'apprends le français", True,
     "L'employé hispanophone embauché à la réception : c'est le mandat de francisation, et il éprouve le français comme langue apprise."),
    ("fr-es", "Je parle français · j'apprends l'espagnol", False,
     "Utile, mais moins de demande ; il réutilise tout ce que les deux premières auront corrigé."),
    ("en-fr", "Je parle anglais · j'apprends le français", False,
     "Proche de es-fr ; à piloter en second."),
]

VOIX_LISTE = [  # (langue, nom, genre, choix imposé ?)
    ("fr-CA", "Sylvie", "F", True), ("fr-CA", "Thierry", "M", True),
    ("es-MX", "Dalia", "F", True), ("es-MX", "Jorge", "M", True),
    ("en-US", "Ava", "F", False), ("en-US", "Emma", "F", False),
    ("en-US", "Andrew", "M", False), ("en-US", "Brian", "M", False),
]


def img(ident, dessin, mot):
    if dessin == "croquis" and (CROQUIS / f"{ident}.jpg").exists():
        return f'<img class="img" src="/assets/interactive/hotel/croquis/{ident}.jpg" alt="{E(mot)}" loading="lazy">'
    if dessin == "croquis":
        return '<div class="img attente">croquis<br>à venir</div>'
    if dessin == "comptoir":
        return '<div class="img attente comptoir-tag">dans le<br>comptoir</div>'
    return '<div class="img rien">sans image</div>'


def carte(e):
    ident, _, fr, en, es, dessin, note = e
    piege = note.startswith("PIÈGE (")
    paire = note[len("PIÈGE ("):note.index(")")] if piege else ""
    langues = "".join(f'<p class="l"><span class="dr">{DRAPEAU[k]}</span>{E(v)}</p>'
                      for k, v in (("fr", fr), ("en", en), ("es", es)))
    return (f'<article class="mot{" piege" if piege else ""}" data-id="{ident}" data-paire="{paire}">'
            f'{img(ident, dessin, fr)}{langues}'
            + (f'<p class="note">{E(note)}</p>' if note else "")
            + '<div class="choix">'
              '<button type="button" data-v="garder" aria-pressed="false">Garder</button>'
              '<button type="button" data-v="retirer" aria-pressed="false">Retirer</button>'
              '<button type="button" data-v="douteux" aria-pressed="false">À revoir</button>'
              '</div></article>')


def option(groupe, val, titre, texte, reco):
    return (f'<button type="button" class="opt" data-g="{groupe}" data-v="{val}" aria-pressed="false">'
            f'<b>{E(titre)}</b>{" <span class=reco>recommandé</span>" if reco else ""}'
            f'<span>{E(texte)}</span></button>')


def main():
    LX.verifier()
    g = LX.par_planche()
    L = LX.LEXIQUE
    n_c = sum(e[5] == "croquis" for e in L)
    n_k = sum(e[5] == "comptoir" for e in L)
    pieges = LX.pieges()

    tete = TETE_DE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Réception d'hôtel — étape 0</title>", tete)
    tete = tete.replace("</style>", CSS + "</style>", 1)

    noms = "".join(
        f'<div class="nom">{option("nom", k, t, "", r)}'
        f'<p><b>Vérification :</b> {E(v)}</p><p><b>À l\'oreille :</b> {E(o)}</p></div>'
        for k, t, r, v, o in NOMS)
    ecartes = "".join(f"<li><b>{E(n)}</b> : {E(p)}</li>" for n, p in ECARTES)
    dirs = "".join(option("pilote", k, t, x, r) for k, t, r, x in DIRECTIONS)

    def lecteur(nom):
        return "".join(f'<audio controls preload="none" src="/assets/presentations/hotel-voix/{nom.lower()}-{i}.mp3"></audio>'
                       for i in (1, 2) if (VOIX / f"{nom.lower()}-{i}.mp3").exists())
    voix = ""
    for lang, titre in (("fr-CA", "Français du Québec"), ("es-MX", "Espagnol du Mexique"), ("en-US", "Anglais nord-américain")):
        cartes = "".join(
            (f'<div class="vx impose"><p class="vn">{n} <span>{"femme" if s == "F" else "homme"}</span></p>{lecteur(n)}'
             f'<div class="verdict mini" data-k="voix-{n.lower()}"><button type="button" data-v="ok" aria-pressed="false">Juste</button>'
             f'<button type="button" data-v="revoir" aria-pressed="false">Un défaut</button></div></div>')
            if imp else
            (f'<div class="vx"><p class="vn">{n} <span>{"femme" if s == "F" else "homme"}</span></p>{lecteur(n)}'
             f'<button type="button" class="opt petit" data-g="voix-en" data-multi="2" data-v="{n.lower()}" aria-pressed="false">Je la garde</button></div>')
            for l, n, s, imp in VOIX_LISTE if l == lang)
        aide = ("Le catalogue HD n'offre que ces deux voix : rien à choisir, seulement à écouter. "
                "Dites s'il y a un défaut (surtout dans le nom épelé)." if lang != "en-US" else
                "Quatre candidates, deux à garder (une femme et un homme de préférence).")
        voix += f'<div class="bloc-voix"><h3>{titre}</h3><p class="aide">{aide}</p><div class="vgrille">{cartes}</div></div>'

    sections = []
    for k, titre in LX.PLANCHES:
        cartes = "".join(carte(e) for e in g[k])
        sections.append(f'<section class="planche" id="p-{k}"><h2>{E(titre)} '
                        f'<span class="compte">{len(g[k])}</span></h2><div class="grille">{cartes}</div></section>')

    corps = f"""<body>
<div class="doc large">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Réception d'hôtel &middot; étape 0 du plan &middot; cadrage</p>
<h1>Le cadrage, à valider</h1>
<p class="chapeau">Vos huit décisions du 24 septembre sont appliquées. Voici ce qu'elles ont
donné&nbsp;: <strong>le public et les objectifs</strong>, <strong>trois noms vérifiés</strong>,
<strong>le dessin</strong> (trois témoins et le comptoir), <strong>les voix</strong> à écouter,
et <strong>{len(L)} mots en trois langues</strong>. Tout se marque dans la page&nbsp;; « Exporter »,
tout en bas, me renvoie vos choix.</p>

<div class="chiffres">
  <div class="ch"><span class="n">{len(L)}</span><span class="q">mots, chacun en français, anglais et espagnol</span></div>
  <div class="ch"><span class="n">{len(pieges)}</span><span class="q">pièges : {len(LX.pieges('fr·en'))} fr·en, {len(LX.pieges('fr·es'))} fr·es, {len(LX.pieges('es·en'))} es·en</span></div>
  <div class="ch"><span class="n">{n_c}</span><span class="q">croquis à produire, ≈&nbsp;{(n_c - 3) * 0.067:.0f}&nbsp;$ pour le reste</span></div>
  <div class="ch"><span class="n">{n_k}</span><span class="q">objets désignés sur le comptoir, sans image de plus</span></div>
</div>

<section>
  <h2>1 · Le public, l'écart, les objectifs</h2>
  <p><b>Qui.</b> Les employés de la réception d'un hôtel, au Québec. Ils se forment sur un téléphone
  ou la tablette du comptoir, dix à quinze minutes pendant les heures creuses. Certains parlent
  français et doivent servir en anglais ou en espagnol&nbsp;; d'autres parlent espagnol ou anglais et
  doivent servir en français.</p>
  <p><b>Ce qui rate aujourd'hui, au comptoir.</b></p>
  <ul class="simple">
    <li>Le <b>nom épelé</b> et le <b>numéro</b> mal entendus, surtout au téléphone&nbsp;: la réservation introuvable, la mauvaise chambre.</li>
    <li>Les <b>heures et les dates</b>&nbsp;: « 3 p.m. » contre « 15 h », « 04/05 » qui n'est pas le même jour aux États-Unis.</li>
    <li>Les <b>faux amis</b> qui trompent le client&nbsp;: le <i>déjeuner</i> québécois servi le matin, la <i>caution</i>, la <i>factura</i> mexicaine.</li>
    <li>Refuser ou expliquer <b>poliment</b> (hôtel complet, un frais)&nbsp;: on passe au geste, ou à l'anglais par défaut.</li>
    <li><b>Promettre ce qui revient au gérant</b> (un remboursement, une exception).</li>
  </ul>
  <table class="cmp"><thead><tr><th>Objectif (verbe · condition · critère)</th><th>Où il se pratique</th><th>Où il s'évalue</th></tr></thead><tbody>
    <tr><td><b>O1.</b> Entendre une demande dite au débit d'un client (type de chambre, nuits, dates) et la saisir juste. <i>7 sur 8 en série.</i></td><td>« Je l'entends, je le trouve », « Ce que le client veut »</td><td>Test, partie A</td></tr>
    <tr><td><b>O2.</b> Faire épeler et noter un nom, un numéro de chambre, un prix, une heure, <i>au téléphone compris</i>. <i>5 de suite sans erreur.</i></td><td>« Épeler un nom », « Les nombres et les heures »</td><td>Test, partie B (à l'oreille seule)</td></tr>
    <tr><td><b>O3.</b> Accueillir, confirmer, refuser poliment et expliquer un frais avec les formules de la langue apprise. <i>6 situations sur 8 au comptoir.</i></td><td>« Ce que je réponds », dialogues modèles</td><td>Jeu de rôle, bilan par situation</td></tr>
    <tr><td><b>O4.</b> Garder pour le gérant ce qui lui revient. <i>Aucune promesse hors règle — éliminatoire, et dit avant.</i></td><td>Série « Hors règle », situation 8</td><td>Jeu de rôle et test, partie C</td></tr>
  </tbody></table>
  <p class="aide">Ces objectifs reprennent la leçon de la Maison Francœur&nbsp;: chacun a son exercice
  <b>et</b> sa question de test, et l'erreur qui coûte cher (la promesse) fait échouer.</p>
</section>

<section>
  <h2>2 · Le nom de l'hôtel</h2>
  <p>Trois noms, cherchés un à un sur le Web (nom exact, en guillemets). Aucun ne désigne un hôtel
  existant. Ce n'est <b>pas</b> une recherche de marque de commerce&nbsp;: elle reste à faire avant
  toute vente.</p>
  <div class="noms">{noms}</div>
  <p><b>Écartés en chemin</b>&nbsp;:</p><ul class="simple">{ecartes}</ul>
</section>

<section>
  <h2>3 · Les deux directions du pilote</h2>
  <p>Vous avez choisi les trois langues dès le départ, avec un pilote sur deux directions.
  Choisissez-en deux&nbsp;:</p>
  <div class="opts">{dirs}</div>
</section>

<section class="premier">
  <h2>4 · Le dessin</h2>
  <p>Même trait que la Maison Francœur&nbsp;: contour noir égal, aplat doux, l'objet seul sur fond
  blanc. Trois témoins choisis pour leurs risques&nbsp;: <b>une carte qui ne doit porter aucun
  chiffre</b>, <b>un meuble en perspective</b>, <b>un objet métallique</b>. Les trois sont sortis
  justes du premier appel.</p>
  <div class="temoins">
    <figure><img src="/assets/interactive/hotel/croquis/carte-cle.jpg" alt="une carte-clé"><figcaption>une carte-clé</figcaption></figure>
    <figure><img src="/assets/interactive/hotel/croquis/lit-queen.jpg" alt="un lit queen"><figcaption>un lit queen</figcaption></figure>
    <figure><img src="/assets/interactive/hotel/croquis/sonnette.jpg" alt="la sonnette"><figcaption>la sonnette</figcaption></figure>
  </div>
  <div class="verdict" data-k="registre">
    <button type="button" data-v="ok" aria-pressed="false">Ce registre me va &mdash; on produit les {n_c}</button>
    <button type="button" data-v="revoir" aria-pressed="false">À ajuster avant de produire</button>
  </div>
  <h3>Le comptoir</h3>
  <p>La pièce maîtresse, vue de <b>derrière</b>&nbsp;: la place de l'employé. Tous les objets du
  lexique y sont&nbsp;: écran, clavier, imprimante, terminal, encodeur et cartes vierges, téléphone,
  tiroir-caisse, sonnette, chemise, plan de la ville, présentoir, trois horloges <b>sans chiffres</b>,
  la porte du gérant. L'espace au centre, de l'autre côté, est <b>vide</b>&nbsp;: c'est là que le
  client apparaîtra au jeu de rôle.</p>
  <figure class="comptoir"><img src="/assets/interactive/hotel/croquis/comptoir.jpg" alt="Le comptoir de réception vu de derrière"></figure>
  <p class="aide">Un défaut vu au zoom&nbsp;: une petite clé métallique, non demandée, à côté de
  l'encodeur. Elle peut rester (un hôtel en a) ou partir à la retouche.</p>
  <div class="verdict" data-k="comptoir">
    <button type="button" data-v="ok" aria-pressed="false">Le comptoir me va</button>
    <button type="button" data-v="revoir" aria-pressed="false">À retoucher</button>
  </div>
</section>

<section>
  <h2>5 · Les voix</h2>
  <p>Deux phrases par voix&nbsp;: l'accueil (un numéro de chambre, des heures) et <b>un nom épelé</b>,
  le point faible connu d'Azure. Écoutez surtout la seconde.</p>
  {voix}
</section>

<section>
  <h2>6 · Le lexique, en trois langues</h2>
  <p>Le mot du comptoir dans chaque variété choisie. Les <b>pièges</b> sont en ambre, avec la paire
  de langues qu'ils trompent&nbsp;: la série des pièges d'une direction ne montrera que les siens.</p>
  <p><button type="button" class="opt petit" id="filtrePieges" aria-pressed="false">Ne voir que les {len(pieges)} pièges</button></p>
  <nav class="sommaire">{"".join(f'<a href="#p-{k}">{E(t)}</a>' for k, t in LX.PLANCHES)}</nav>
  {"".join(sections)}
</section>

<section>
  <h2>Ce qui manque</h2>
  <p>Un mot par ligne, dans la langue que vous voulez&nbsp;: je trouve les deux autres.</p>
  <textarea id="ajouts" rows="6" placeholder="le coffret de sûreté&#10;la carte de fidélité"></textarea>
  <p><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button>
  <span id="etat" class="etat"></span></p>
</section>

<div class="pied">
  <p>Étape 0 · {len(L)} mots · page produite par <code>build/hotellerie_etape0.py</code> depuis
  <code>build/contenu/entreprise-hotel/lexique.py</code> &mdash; ne pas l'éditer.</p>
</div>
</div>
<script>{JS}</script>
</body>
</html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {len(L)} mots, {len(pieges)} pièges")


CSS = """
/* ── étape 0 de la réception ── */
.doc.large{max-width:1180px}
.chiffres{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.temoins{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin:16px 0}
.temoins figure,.comptoir{margin:0;background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px}
.temoins img,.comptoir img{width:100%;display:block}
.temoins figcaption{text-align:center;font-weight:700;color:#17181A;margin-top:6px}
.comptoir{margin:14px 0}
.verdict,.choix{display:flex;flex-wrap:wrap;gap:12px;margin:12px 0}
.verdict button,.choix button{font:inherit;cursor:pointer;background:var(--sunken);color:var(--body);
  border:1px solid var(--line-fort);border-radius:10px;padding:8px 12px;min-height:40px}
.choix{gap:12px}
.choix button{font-size:13px;padding:5px 8px;border-radius:8px}
button[aria-pressed="true"][data-v="ok"],button[aria-pressed="true"][data-v="garder"]{background:var(--fait-bg);border-color:var(--fait);color:var(--ink);font-weight:700}
button[aria-pressed="true"][data-v="retirer"]{background:var(--loi-bg);border-color:var(--loi);color:var(--ink);font-weight:700}
button[aria-pressed="true"][data-v="douteux"],button[aria-pressed="true"][data-v="revoir"]{background:var(--decid-bg);border-color:var(--decid);color:var(--ink);font-weight:700}
.opts,.noms{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;margin:12px 0}
.opt{font:inherit;text-align:left;cursor:pointer;background:var(--card);color:var(--body);border:1px solid var(--line-fort);
  border-radius:12px;padding:12px 14px;display:flex;flex-direction:column;gap:4px;width:100%}
.opt b{color:var(--ink)}
.opt span{font-size:14px;color:var(--muted)}
.opt .reco{display:inline;font-size:12px;font-weight:700;color:var(--acier);margin-left:6px}
.opt[aria-pressed="true"]{border-color:var(--acier);box-shadow:inset 0 0 0 2px var(--acier);background:var(--acier-bg)}
.opt.petit{display:inline-flex;width:auto;padding:8px 12px;min-height:40px}
.nom{display:flex;flex-direction:column;gap:6px}
.nom p{margin:0;font-size:14px;line-height:1.45}
.aide{color:var(--muted);font-size:15px}
.bloc-voix{margin:18px 0}
.vgrille{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px}
.vx{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:8px}
.vx audio{width:100%;height:36px}
.vn{margin:0;font-weight:800;color:var(--ink)}
.vn span{font-weight:600;color:var(--muted);font-size:14px;margin-left:6px}
.verdict.mini{margin:0}
.sommaire{position:sticky;top:0;z-index:2;background:var(--ground);display:flex;flex-wrap:wrap;gap:6px 14px;
  padding:10px 0;border-bottom:1px solid var(--line);margin:16px 0 8px;font-size:15px}
.sommaire a{color:var(--acier);text-decoration:none;font-weight:700}
.planche h2 .compte{font-size:15px;color:var(--muted);font-weight:600;margin-left:6px}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:12px}
.mot{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px;display:flex;flex-direction:column;gap:3px}
.mot.piege{border-color:var(--decid);box-shadow:inset 0 3px 0 var(--decid)}
.mot[data-etat="retirer"]{opacity:.45}
body.pieges-seuls .mot:not(.piege),body.pieges-seuls .planche:not(:has(.piege)){display:none}
.mot .img{width:100%;aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:8px}
.mot .attente,.mot .rien{display:grid;place-items:center;text-align:center;font-size:13px;color:var(--muted);
  background:var(--sunken);border:1px dashed var(--line-fort);aspect-ratio:3/2}
.mot .l{margin:0;font-size:15px;line-height:1.3;color:var(--ink)}
.mot .l:first-of-type{font-weight:800;font-size:16px;margin-top:4px}
.mot .dr{display:inline-block;min-width:24px;font-size:11px;font-weight:800;color:var(--muted);letter-spacing:.04em}
.mot .note{margin:4px 0 2px;font-size:13px;line-height:1.4;color:var(--body)}
.mot.piege .note{color:var(--decid);font-weight:700}
.mot .choix{margin-top:auto;padding-top:6px}
@media (max-width:640px){
  .grille{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
  .sommaire{flex-wrap:nowrap;overflow-x:auto;white-space:nowrap}
  .mot .l{font-size:14px}
  .cmp{font-size:14px}
}
textarea{width:100%;font:inherit;font-size:15px;padding:10px;border-radius:10px;border:1px solid var(--line-fort);
  background:var(--card);color:var(--ink)}
"""

JS = r"""
(function(){
  var CLE='hotellerie-etape0', s={mots:{},verdicts:{},choix:{},ajouts:''};
  try{ var l=JSON.parse(localStorage.getItem(CLE)||'null'); if(l) s=Object.assign(s,l); }catch(e){}
  function sauver(){ try{ localStorage.setItem(CLE,JSON.stringify(s)); }catch(e){} }
  function peindre(){
    document.querySelectorAll('.mot').forEach(function(m){
      var v=s.mots[m.dataset.id]; m.dataset.etat=v||'';
      m.querySelectorAll('.choix button').forEach(function(b){ b.setAttribute('aria-pressed', v===b.dataset.v?'true':'false'); });
    });
    document.querySelectorAll('.verdict').forEach(function(d){
      d.querySelectorAll('button').forEach(function(b){ b.setAttribute('aria-pressed', s.verdicts[d.dataset.k]===b.dataset.v?'true':'false'); });
    });
    document.querySelectorAll('.opt[data-g]').forEach(function(b){
      var c=s.choix[b.dataset.g]||[]; b.setAttribute('aria-pressed', c.indexOf(b.dataset.v)>=0?'true':'false');
    });
    var n=Object.keys(s.mots).length, t=document.querySelectorAll('.mot').length;
    document.getElementById('etat').textContent=n+' mots marqués sur '+t;
  }
  // Combien de choix par groupe : un nom, deux directions, deux voix anglaises.
  var MAX={nom:1,pilote:2,'voix-en':2};
  document.addEventListener('click',function(e){
    var b=e.target.closest('.choix button'), m=b&&b.closest('.mot');
    if(m){ var id=m.dataset.id; if(s.mots[id]===b.dataset.v) delete s.mots[id]; else s.mots[id]=b.dataset.v; sauver(); peindre(); return; }
    var r=e.target.closest('.verdict button');
    if(r){ var k=r.closest('.verdict').dataset.k; s.verdicts[k]= s.verdicts[k]===r.dataset.v ? null : r.dataset.v; sauver(); peindre(); return; }
    var o=e.target.closest('.opt[data-g]');
    if(o){ var g=o.dataset.g, c=(s.choix[g]||[]).slice(), i=c.indexOf(o.dataset.v);
      if(i>=0) c.splice(i,1); else { c.push(o.dataset.v); while(c.length>(MAX[g]||1)) c.shift(); }
      s.choix[g]=c; sauver(); peindre(); return; }
    if(e.target.id==='filtrePieges'){ var on=document.body.classList.toggle('pieges-seuls');
      e.target.setAttribute('aria-pressed',on?'true':'false'); }
  });
  var ta=document.getElementById('ajouts'); ta.value=s.ajouts||'';
  ta.addEventListener('input',function(){ s.ajouts=ta.value; sauver(); });
  document.getElementById('exporter').addEventListener('click',function(){
    var out={etape:'hotellerie-etape0',date:new Date().toISOString().slice(0,10),
      nom:(s.choix.nom||[])[0]||null, pilote:s.choix.pilote||[], voixAnglaises:s.choix['voix-en']||[],
      verdicts:s.verdicts, retirer:[], douteux:[],
      garder:Object.keys(s.mots).filter(function(k){return s.mots[k]==='garder';}).length,
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
