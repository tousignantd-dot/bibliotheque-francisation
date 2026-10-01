#!/usr/bin/env python3
"""Trois pistes de système de design pour BoucleDidactique — une à choisir.

    python3 build/boucledidactique_pistes_page.py
    # écrit assets/presentations/identite/boucledidactique-pistes.html

LE 1er OCTOBRE 2026, Daniel a tranché le nom de la maison : BoucleDidactique,
en un mot, avec les deux majuscules. Trame est abandonné, son système de
design avec lui. Il en faut un neuf pour le site de la maison (conception
pédagogique pour la formation en entreprise : trousses de métier, diagnostic
didactique, pièces d'apprentissage).

Trois directions complètes, chacune avec sa palette (contrastes WCAG calculés
dans la page, pas écrits), sa paire de polices, une esquisse de logo et le même
écran type. L'esquisse n'est PAS le logo : le logo final se dessine ensuite sur
un canevas, comme celui de Trame. Les polices sont chargées de Google pour
l'aperçu seulement ; le système retenu les logera en local (voir la fiche
ressources-design).

La page est GÉNÉRÉE. Le choix vit dans le localStorage ; « Exporter » rend le
JSON qui pilote l'écriture du système.
"""
import html
import json
import pathlib

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "identite" / "boucledidactique-pistes.html"

# Chaque piste : jetons, polices, esquisse de logo (SVG), et ce qu'elle affirme.
# v2 (1er oct. 2026) : la v1 (cycle, carnet, mesure) faisait « trop français »
# — papier chaud, serif, l'univers de francis. Daniel : « il faut trouver autre
# chose… il faudrait fouiller ». Les trois pistes partent de systèmes réels
# relevés dans styles.refero.design, ADAPTÉS (polices libres à la place des
# leurs, qui sont payantes ; palette retouchée pour les contrastes). La v1 est
# gardée telle quelle : assets/presentations/identite/boucledidactique-pistes-v1.html
REFERO = "https://styles.refero.design"
PISTES = [
    dict(cle="voltage", nom="Le voltage", devise="Vert forêt et lime : une maison sûre d'elle, qui parle à tout le monde.",
         ref=("Wise", REFERO + "/style/367c0c6e-73a7-441c-a8ff-91d139ac60dc",
              "Une banque internationale qui s'adresse à des gens de partout, dans leur langue : exactement notre public d'employés allophones et d'employeurs pressés."),
         prend="Le duo encre forêt + lime en aplat, les titres très gras et serrés, beaucoup de blanc, des boutons en pilule.",
         affirme="Une maison moderne et internationale, sans un gramme de terroir. Le lime ne sert qu'aux surfaces de marque, jamais au texte : on écrit en forêt dessus.",
         titre="Inter Tight", texte="Inter", mono="JetBrains Mono",
         pourquoi_polices="Wise compose en Wise Sans (propriétaire) et Inter. Inter Tight, la version serrée d'Inter, donne la même voix de titre très grasse ; Inter tient le texte. Couverture complète du latin, du cyrillique et du vietnamien.",
         jetons={"fond": "#FFFFFF", "surface": "#F2F5EF", "encre": "#0E0F0C", "encre-2": "#454745",
                  "accent": "#163300", "accent-doux": "#9FE870", "trait": "#DFE4DA",
                  "juste": "#1F5B0E", "faux": "#A8200D"},
         rayon="999px", ombre="none", bouton_texte="#9FE870", hero="#9FE870",
         logo='<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="2" y="2" width="44" height="44" rx="14" fill="var(--accent-doux)"/><circle cx="24" cy="24" r="11" fill="none" stroke="var(--accent)" stroke-width="5.5" stroke-linecap="round" stroke-dasharray="54 15" transform="rotate(-50 24 24)"/><circle cx="31.5" cy="15" r="3.6" fill="var(--accent)"/></svg>',
         risque="Le lime en grand peut fatiguer : il reste au logo, à un bandeau par page et aux pastilles, jamais derrière un paragraphe."),
    dict(cle="dossier", nom="Le dossier", devise="Pierre, encre et indigo : la firme-conseil qui livre des preuves.",
         ref=("Outsource Consultants", REFERO + "/style/16be276a-d8ce-484e-8f7a-cbbb09f717f7",
              "Une firme-conseil qui se présente comme un dossier d'architecte : sobre, précis, chiffré. C'est la posture du diagnostic didactique vendu à une direction."),
         prend="Le fond pierre froide, l'indigo « trait de stylo » pour l'action, la grotesque suisse pour tout, la chasse fixe pour les données et les étiquettes.",
         affirme="Une maison de méthode : chaque page se lit comme un rapport qu'on peut poser sur la table d'un comité de direction. Le logo est la boucle entre crochets — la méthode encadre.",
         titre="Hanken Grotesk", texte="Hanken Grotesk", mono="JetBrains Mono",
         pourquoi_polices="La référence compose en PP Neue Montreal et GT America Mono, toutes deux payantes. Hanken Grotesk en est la cousine libre la plus proche ; JetBrains Mono remplace la chasse fixe pour les chiffres et les étiquettes.",
         jetons={"fond": "#E8E6E0", "surface": "#F6F5F1", "encre": "#0A0A0A", "encre-2": "#4A4948",
                  "accent": "#1925AA", "accent-doux": "#DCDFF5", "trait": "#CFCBC4",
                  "juste": "#1E6B45", "faux": "#A3201A"},
         rayon="2px", ombre="none", bouton_texte="#FFFFFF",
         logo='<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M11 8H5v32h6M37 8h6v32h-6" fill="none" stroke="var(--encre)" stroke-width="3.5"/><circle cx="24" cy="24" r="9" fill="none" stroke="var(--accent)" stroke-width="4.5" stroke-dasharray="44 13" transform="rotate(-50 24 24)"/></svg>',
         risque="Bien tenu, c'est d'une élégance rare ; relâché, c'est austère. Il faut de vraies images des formations en cours pour que le dossier ait des visages."),
    dict(cle="terrain", nom="Le terrain", devise="Sarcelle profonde et menthe : la recherche appliquée, au poste de travail.",
         ref=("Lyssna", REFERO + "/style/65f775f1-6dcc-4c49-80d2-b5a017b76f59",
              "Un outil de recherche auprès des utilisateurs : on observe des gens faire une tâche et on mesure. C'est mot pour mot ce que fait le diagnostic didactique."),
         prend="La sarcelle profonde pour l'action, la menthe en aplat pour les blocs de marque, une touche de rose pour signaler, des formes arrondies sans mièvrerie.",
         affirme="Une maison de terrain : on va voir les employés travailler, on mesure, on corrige. Plus vivante que « Le dossier », plus posée que « Le voltage ».",
         titre="Sora", texte="Instrument Sans", mono="JetBrains Mono",
         pourquoi_polices="La référence compose en Grenette et Mint (payantes). Sora porte des titres géométriques et ouverts, Instrument Sans un texte net et un peu étroit qui laisse de la place aux traductions plus longues.",
         jetons={"fond": "#FFFFFF", "surface": "#F1FAF7", "encre": "#061D29", "encre-2": "#425D6D",
                  "accent": "#006E75", "accent-doux": "#B9FFE8", "trait": "#D5E6E1",
                  "juste": "#11603F", "faux": "#A51D4A"},
         rayon="12px", ombre="0 1px 2px rgba(6,29,41,.06), 0 6px 20px rgba(6,29,41,.06)", bouton_texte="#FFFFFF",
         logo='<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="21" fill="var(--accent-doux)"/><path d="M15 28c0-8 6-13 12-12s8 7 5 11-10 4-11-1 4-9 9-7" fill="none" stroke="var(--accent)" stroke-width="4" stroke-linecap="round"/></svg>',
         risque="La menthe et le rose peuvent tirer vers le ludique : ils restent des aplats de marque, le texte est toujours en encre ou en sarcelle."),
]

POLICES = sorted({p["titre"] for p in PISTES} | {p["texte"] for p in PISTES} | {p["mono"] for p in PISTES})


def piste_html(p):
    e = html.escape
    j = p["jetons"]
    style = ";".join("--%s:%s" % (k, v) for k, v in j.items())
    style += ";--rayon:%s;--ombre:%s;--f-titre:'%s';--f-texte:'%s';--f-mono:'%s';--btn-texte:%s" % (
        p["rayon"], p["ombre"], p["titre"], p["texte"], p["mono"], p["bouton_texte"])
    style += ";--hero:%s" % p.get("hero", "transparent")
    nuancier = "".join(
        '<div class="sw"><span class="pastille" style="background:%s"></span><b>%s</b><code>%s</code></div>' % (v, k, v)
        for k, v in j.items())
    return f"""<section class="piste" id="{p['cle']}" data-cle="{p['cle']}" style="{style}">
  <header class="p-tete">
    <div class="marque">{p['logo']}<span class="mot">Boucle<b>Didactique</b></span></div>
    <div><h2>{e(p['nom'])}</h2><p class="devise">{e(p['devise'])}</p></div>
  </header>

  <div class="ecran" aria-label="Écran type, piste {e(p['nom'])}">
    <div class="e-barre"><span class="marque petite">{p['logo']}<span class="mot">Boucle<b>Didactique</b></span></span><span class="e-nav"><span>Formations</span><span>Diagnostic</span><span>Nous joindre</span></span></div>
    <div class="e-hero">
      <p class="e-sur">Formation en entreprise</p>
      <h3>Des formations qui changent les gestes, et la preuve qu'elles le font.</h3>
      <p class="e-chap">Nous concevons la formation, nous la faisons jouer à vos employés, puis nous mesurons ce qui a changé au poste de travail.</p>
      <span class="e-btn">Demander un diagnostic</span> <span class="e-btn e-btn--2">Voir une trousse</span>
    </div>
    <div class="e-cartes">
      <div class="e-carte"><p class="e-sur">Diagnostic didactique</p><h4>Votre matériel, jugé par les réponses de vos employés</h4><p>Douze questions, quarante personnes : ce qui est compris, ce qui ne l'est pas, et pourquoi.</p>
        <p class="e-verdicts"><span class="v v-juste">✓ Juste · 86 %</span><span class="v v-faux">✕ À revoir · 3 questions</span></p></div>
      <div class="e-carte"><p class="e-sur">Trousse de métier</p><h4>Réception d'hôtel, vente au détail, cuisine</h4><p>Lexique en planches, exercices, test de positionnement et jeu de rôle avec un client.</p><p class="e-donnee">v4 · 23 critères · 0 constat majeur</p></div>
    </div>
  </div>

  <div class="ref"><b>Cherchée chez {e(p['ref'][0])}</b> — {e(p['ref'][2])} <a href="{e(p['ref'][1])}" target="_blank" rel="noopener">Voir le système d'origine</a><br><b>Ce qu'on lui prend :</b> {e(p['prend'])}</div>

  <div class="p-corps">
    <div><h4>Ce que la piste affirme</h4><p>{e(p['affirme'])}</p></div>
    <div><h4>Polices · {e(p['titre'])} + {e(p['texte'])}</h4><p>{e(p['pourquoi_polices'])}</p>
      <p class="specimen"><span class="t">Aa Bb · Diagnostic</span><span class="x">Le texte courant se lit sans effort, même long — à 17 px, comme sur le site.</span></p></div>
    <div><h4>Le risque à tenir</h4><p>{e(p['risque'])}</p></div>
  </div>

  <h4 class="n-tit">Palette — contrastes calculés dans la page</h4>
  <div class="nuancier">{nuancier}</div>
  <table class="contrastes"><thead><tr><th>Texte</th><th>sur</th><th>Rapport</th><th>Seuil 4,5:1</th></tr></thead><tbody></tbody></table>

  <div class="dec" role="group" aria-label="Décision sur la piste {e(p['nom'])}">
    <button type="button" data-v="choisie">Je choisis cette piste</button>
    <button type="button" data-v="non">Non</button>
    <input type="text" class="note" placeholder="Ce que je garderais d'ici (couleur, police, logo…)" aria-label="Note sur la piste {e(p['nom'])}">
  </div>
</section>"""


def main():
    familles = "&".join("family=" + f.replace(" ", "+") + ":wght@400;600;700;800" for f in POLICES)
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(GABARIT % {
        "polices": html.escape("https://fonts.googleapis.com/css2?" + familles + "&display=swap"),
        "pistes": "\n".join(piste_html(p) for p in PISTES),
        "btn": json.dumps({p["cle"]: p["bouton_texte"] for p in PISTES}),
        "data": json.dumps([{"cle": p["cle"], "nom": p["nom"], "jetons": p["jetons"], "titre": p["titre"],
                             "texte": p["texte"]} for p in PISTES], ensure_ascii=False),
    }, encoding="utf-8")
    print("Écrit : %s (%d pistes)" % (SORTIE.relative_to(RACINE), len(PISTES)))


GABARIT = r"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pistes BoucleDidactique</title>
<link rel="stylesheet" href="%(polices)s">
<style>
@font-face{font-family:"Nunito";src:url("../../design-system/fonts/nunito-latin.woff2") format("woff2");font-weight:200 1000;font-display:swap}
:root{--page:#F7F7F5;--carte:#fff;--ink:#17181A;--ink-2:#4A4D52;--line:#E4E3DE;--vert:#0A8F5B}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%%}
body{margin:0;background:var(--page);color:var(--ink);font:17px/1.55 "Nunito",system-ui,-apple-system,sans-serif}
.cadre{max-width:1080px;margin:0 auto;padding:32px 16px 96px}
.sur{font-weight:800;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:#6B6E73}
h1{font-size:34px;line-height:1.15;margin:6px 0 12px;font-weight:900}
.chapeau{font-size:18px;color:var(--ink-2);max-width:68ch;margin:0 0 16px}
.sommaire{display:flex;flex-wrap:wrap;gap:12px;margin:0 0 8px}
.sommaire a{font-weight:800;color:var(--ink);text-decoration:none;border:1px solid var(--line);background:var(--carte);border-radius:999px;padding:0 16px;min-height:44px;display:inline-flex;align-items:center}
.barre{position:sticky;top:0;z-index:5;background:var(--page);padding:12px 0;border-bottom:1px solid var(--line);display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:24px}
.barre .cpt{font-size:15px;color:var(--ink-2)}
button{font:inherit;font-size:15px;font-weight:700;min-height:44px;padding:0 16px;border:1px solid var(--line);border-radius:999px;background:var(--carte);color:var(--ink);cursor:pointer}
button[aria-pressed=true]{background:var(--ink);color:#fff;border-color:var(--ink)}
button:focus-visible,input:focus-visible,a:focus-visible{outline:3px solid var(--vert);outline-offset:2px}

/* Une piste : ses jetons sont posés sur la section ; tout ce qui est dedans les lit. */
.piste{background:var(--carte);border:1px solid var(--line);border-radius:18px;padding:24px;margin:0 0 32px}
.p-tete{display:flex;flex-wrap:wrap;gap:16px 32px;align-items:center;margin-bottom:20px}
.p-tete h2{margin:0;font-size:26px;font-weight:900}
.devise{margin:2px 0 0;color:var(--ink-2)}
.marque{display:inline-flex;align-items:center;gap:10px;color:var(--encre)}
.marque svg{width:48px;height:48px;flex:none}
.mot{font-family:var(--f-titre);font-size:28px;font-weight:600;letter-spacing:-.02em;color:var(--encre)}
.mot b{font-weight:800}
.marque.petite svg{width:28px;height:28px}.marque.petite .mot{font-size:18px}

.ecran{background:var(--fond);border:1px solid var(--trait);border-radius:14px;overflow:hidden;font-family:var(--f-texte);color:var(--encre)}
.e-barre{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;padding:14px 20px;background:var(--surface);border-bottom:1px solid var(--trait)}
.e-nav{display:flex;gap:20px;font-size:15px;color:var(--encre-2);font-weight:600}
.e-hero{padding:32px 24px 28px;background:var(--hero);margin-bottom:24px}
.e-hero>*{max-width:720px}
.e-sur{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:0 0 8px}
.e-hero h3{font-family:var(--f-titre);font-size:34px;line-height:1.12;letter-spacing:-.015em;margin:0 0 12px;font-weight:700}
.e-chap{font-size:18px;color:var(--encre-2);margin:0 0 20px;max-width:60ch}
.e-btn{display:inline-flex;align-items:center;min-height:44px;padding:0 20px;border-radius:var(--rayon);background:var(--accent);color:var(--btn-texte);font-weight:700;font-size:16px;margin:0 8px 8px 0}
.e-btn--2{background:transparent;color:var(--encre);border:1.5px solid var(--encre)}
.e-cartes{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;padding:0 24px 28px}
.e-carte{background:var(--surface);border:1px solid var(--trait);border-radius:var(--rayon);box-shadow:var(--ombre);padding:18px 20px}
.e-carte h4{font-family:var(--f-titre);font-size:20px;line-height:1.25;margin:0 0 8px;font-weight:700}
.e-carte p{margin:0 0 10px;font-size:16px;color:var(--encre-2)}
.e-verdicts{display:flex;flex-wrap:wrap;gap:8px}
.v{font-size:14px;font-weight:700;padding:4px 10px;border-radius:999px;background:var(--accent-doux)}
.v-juste{color:var(--juste)}.v-faux{color:var(--faux)}
.e-donnee{font-family:var(--f-mono),ui-monospace,monospace;font-size:14px!important;color:var(--encre)!important}

.p-corps{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin:24px 0 8px}
.p-corps h4,.n-tit{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:#6B6E73;margin:0 0 6px;font-weight:800}
.p-corps p{margin:0 0 8px}
.specimen{border-left:3px solid var(--accent);padding-left:12px}
.ref{background:var(--page);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin-top:20px;font-size:16px}
.ref a{color:var(--ink);font-weight:700}
.specimen .t{display:block;font-family:var(--f-titre);font-size:28px;font-weight:700;color:var(--encre)}
.specimen .x{display:block;font-family:var(--f-texte);font-size:17px;color:var(--encre-2)}
.n-tit{margin-top:20px}
.nuancier{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.sw{display:flex;align-items:center;gap:8px;font-size:14px}
.pastille{width:28px;height:28px;border-radius:8px;border:1px solid rgba(0,0,0,.12);flex:none}
.sw b{font-weight:700}.sw code{font-size:12px;color:var(--ink-2);margin-left:auto}
.contrastes{width:100%%;border-collapse:collapse;margin-top:12px;font-size:15px}
.contrastes th,.contrastes td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line)}
.contrastes th{font-size:13px;color:#6B6E73;text-transform:uppercase;letter-spacing:.06em}
.ok{color:#07734A;font-weight:800}.ko{color:#B3261E;font-weight:800}
.dec{display:flex;flex-wrap:wrap;gap:12px;margin-top:20px;padding-top:16px;border-top:1px solid var(--line)}
.dec .note{flex:1 1 260px;min-height:44px;font:inherit;font-size:16px;padding:0 14px;border:1px solid var(--line);border-radius:10px;background:var(--page);color:var(--ink)}
.piste.choisie{border:2px solid var(--ink)}
.source{font-size:14px;color:#6B6E73}
@media (max-width:640px){h1{font-size:28px}.piste{padding:16px}.e-hero h3{font-size:27px}.e-nav{display:none}}
@media print{.barre,.dec{display:none}.piste{break-inside:avoid}}
</style></head>
<body><div class="cadre">
<div class="sur">La maison · Identité · à trancher</div>
<h1>BoucleDidactique : trois pistes, cherchées ailleurs</h1>
<p class="chapeau">Le nom est décidé : <b>BoucleDidactique</b>. Les trois premières pistes faisaient trop « francisation » — papier chaud, serif, l'univers de francis. Celles-ci partent de systèmes réels, cherchés dans une galerie de 220 sites, chez des maisons qui vendent de la méthode à des entreprises et parlent à des gens de partout. Chacune est adaptée, pas recopiée. Le logo reste une esquisse.</p>
<nav class="sommaire" aria-label="Les pistes"><a href="#voltage">Le voltage</a><a href="#dossier">Le dossier</a><a href="#terrain">Le terrain</a><a href="boucledidactique-pistes-v1.html">Les pistes écartées (v1)</a></nav>
<div class="barre"><span class="cpt" id="cpt"></span><button type="button" id="exp">Exporter</button></div>
%(pistes)s
<p class="source">Polices chargées de Google pour l'aperçu ; le système retenu les logera en local. Page engendrée par build/boucledidactique_pistes_page.py.</p>
</div>
<script>
(function(){
  var DATA=%(data)s, BTN=%(btn)s, CLE="boucledidactique-pistes-v2", etat={};
  try{etat=JSON.parse(localStorage.getItem(CLE)||"{}")}catch(e){etat={}}
  function garder(){try{localStorage.setItem(CLE,JSON.stringify(etat))}catch(e){}}
  function lum(h){h=h.replace("#","");var c=[0,2,4].map(function(i){var v=parseInt(h.substr(i,2),16)/255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*c[0]+.7152*c[1]+.0722*c[2]}
  function rap(a,b){var x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)}
  // Les paires qui comptent : le texte tel que l'écran type le pose.
  var PAIRES=[["encre","fond"],["encre-2","fond"],["encre","surface"],["encre-2","surface"],["accent","fond"],["btn","accent"],["juste","accent-doux"],["faux","accent-doux"],["juste","surface"],["faux","surface"]];
  DATA.forEach(function(p){
    var tb=document.querySelector('#'+p.cle+' .contrastes tbody'), j=p.jetons;
    PAIRES.forEach(function(pr){
      var a=pr[0]==="btn"?BTN[p.cle]:(pr[0][0]==="#"?pr[0]:j[pr[0]]), b=j[pr[1]], r=rap(a,b);
      var tr=document.createElement("tr");
      tr.innerHTML="<td>"+(pr[0]==="btn"?"texte du bouton":pr[0])+"</td><td>"+pr[1]+"</td><td>"+r.toFixed(2)+":1</td><td class='"+(r>=4.5?"ok'>✓ passe":"ko'>✕ échoue")+"</td>";
      tb.appendChild(tr);
    });
  });
  var sections=[].slice.call(document.querySelectorAll(".piste"));
  function peindre(){
    var n=0;
    sections.forEach(function(s){var d=etat[s.dataset.cle]||{};
      s.querySelectorAll(".dec button").forEach(function(b){b.setAttribute("aria-pressed",String(b.dataset.v===d.v))});
      s.classList.toggle("choisie",d.v==="choisie"); if(d.v)n++;});
    var ch=sections.filter(function(s){return (etat[s.dataset.cle]||{}).v==="choisie"}).map(function(s){return s.querySelector("h2").textContent});
    document.getElementById("cpt").textContent=ch.length?("Choisie : "+ch.join(", ")):(n+" / 3 tranchées");
  }
  sections.forEach(function(s){
    var k=s.dataset.cle, note=s.querySelector(".note"); note.value=(etat[k]||{}).note||"";
    s.querySelectorAll(".dec button").forEach(function(b){b.addEventListener("click",function(){
      var v=b.dataset.v, d=etat[k]||{};
      // Une seule piste choisie : en choisir une rend les autres à « non tranchée ».
      if(v==="choisie"&&d.v!=="choisie"){Object.keys(etat).forEach(function(o){if(etat[o].v==="choisie")etat[o].v=""})}
      d.v=(d.v===v)?"":v; etat[k]=d; garder(); peindre();});});
    note.addEventListener("input",function(){var d=etat[k]||{}; d.note=note.value; etat[k]=d; garder();});
  });
  document.getElementById("exp").addEventListener("click",function(){
    var out={page:"boucledidactique-pistes",date:new Date().toISOString().slice(0,10),pistes:DATA.map(function(p){var d=etat[p.cle]||{};return {cle:p.cle,nom:p.nom,decision:d.v||"",note:d.note||""}})};
    var txt=JSON.stringify(out,null,2), a=document.createElement("a");
    a.href=URL.createObjectURL(new Blob([txt],{type:"application/json"})); a.download="boucledidactique-pistes-decisions.json"; a.click();
    if(navigator.clipboard){navigator.clipboard.writeText(txt).catch(function(){})}
  });
  peindre();
})();
</script>
</body></html>
"""

if __name__ == "__main__":
    main()
