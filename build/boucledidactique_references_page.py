#!/usr/bin/env python3
"""Le mur de références de BoucleDidactique — réagir d'un clic, avant toute piste.

    python3 build/boucledidactique_references_page.py
    # écrit assets/presentations/identite/boucledidactique-references.html

POURQUOI. Deux tours de pistes adaptées ont été refusés le 1er octobre 2026 :
la v1 « trop français » (papier chaud, serif), la v2 (Wise, une firme-conseil,
Lyssna) suivie de « cherche encore ». Adapter avant de savoir ce qui plaît fait
deviner deux fois. Ici, douze systèmes RÉELS, montrés tels quels par leur
vignette, très différents entre eux ; Daniel réagit (j'aime · bof · non + un
mot), et les pistes se bâtissent ensuite sur ce qui ressort.

Sélection : parcourue dans styles.refero.design (140 systèmes relevés au
navigateur ce jour-là). Exclus d'office : le crème et le serif éditorial (ce
qui se lit « français »), les trois références de la v2, les sites de produit
grand public sans rapport (Apple, voitures, alimentation).

Les vignettes sont celles de Refero, liées et non copiées. La page est
GÉNÉRÉE ; les réactions vivent dans le localStorage, « Exporter » rend le JSON.
"""
import html
import json
import pathlib

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "identite" / "boucledidactique-references.html"
R = "https://styles.refero.design/style/"
I = "https://images.refero.design/styles/refero.design/image/"

# nom, page Refero, vignette, couleurs, polices d'origine, l'ambiance, ce qui pourrait servir
REFS = [
    ("Ramp", R + "b38702a0-75ab-474c-9106-00b624535825", I + "4fcf10e3-d62d-4e41-8a9e-9f591b57e8a9.jpg",
     ["#E4F222", "#0C0A08"], "Lausanne", "Bureau de finance éditorial, surligneur jaune sur encre.",
     "Le surligneur : on souligne ce qui compte dans une formation, comme dans un rapport."),
    ("Brex", R + "b58d92f6-68a8-4358-8fc9-6ea58e6d483b", I + "403e867e-a873-4b01-8175-33edf6bfde0b.jpg",
     ["#FF5900", "#000710"], "Inter, Flecha", "Béton blanc, une seule braise orange.",
     "Une seule couleur vive, le reste en noir et blanc : très lisible, très affirmé."),
    ("Calendly", R + "9946887b-ffa9-4276-af81-ae6352795afb", I + "8790afdf-d95b-4840-9adf-4e739f67d63e.jpg",
     ["#0B3558", "#006BFF"], "Gilroy", "Encre marine sur marbre froid.",
     "Le logiciel d'entreprise aimable : sérieux pour la direction, rassurant pour l'employé."),
    ("Quizlet", R + "528eb1d4-8508-4dc6-87b4-c7b92d648dac", I + "f116898c-8782-436c-90b9-261f0f9d1657.jpg",
     ["#4255FF", "#282E3E"], "Hurme Geometric Sans", "Classe codée par couleur, sur blanc.",
     "Le seul de la liste qui vient de l'apprentissage : un code couleur pour les types d'activité."),
    ("Busuu", R + "72b85d0a-1ff8-4dd3-b33a-f55aad6df5c9", I + "d9c417c5-ba35-4d0f-812b-369956982ed6.jpg",
     ["#3B1E90", "#116EEE"], "Nista", "Passeport ludique des langues du monde.",
     "Apprendre une langue, pour un public international : indigo profond et bleu vif."),
    ("teenage engineering", R + "aecf9dda-5cba-4dc7-9e73-59b65d895cdf", I + "ced22f54-921e-4cf3-bce5-fc54269fbed9.jpg",
     ["#F6F8F7", "#000000", "#F0A800"], "te-20, te-40", "Catalogue industriel sous éclairage de studio.",
     "L'objet bien fait, la notice d'usage : la formation comme un outil de précision."),
    ("Figure 03", R + "2997507c-ba60-4653-b217-3eca4858dec8", I + "26c00315-490e-482d-8690-494c538802af.jpg",
     ["#FFFFFF", "#0C0C0C"], "Neue Machina, Neue Haas Grotesk", "Catalogue de laboratoire de robotique, blanc.",
     "Le geste technique montré en grand, sur fond blanc : nos croquis et nos pièces jouées."),
    ("Linear", R + "90ce5883-bb24-4466-93f7-801cd617b0d1", I + "17d8b2ae-d82e-461d-a94b-bc5054836305.jpg",
     ["#08090A", "#0F1011"], "Inter, Berkeley Mono", "Instrument de précision, minuit.",
     "Le thème sombre, net, sans ornement. Rare pour de la formation, donc remarqué."),
    ("Column", R + "a76ec6ba-20b3-495c-9d89-1e58281e79e7", I + "0e867410-c907-4888-82a5-d74ddb3d3084.jpg",
     ["#111A4A", "#011821"], "Suisse Int'l, Suisse Mono", "Grand livre marine sous l'aube froide.",
     "La banque d'infrastructure : rigueur suisse, marine profond, chiffres en chasse fixe."),
    ("Firecrawl", R + "78fec83e-4b27-44ab-9f64-31e9dee53e46", I + "b0e090f5-4e98-4135-a54a-0fb93fb5359c.jpg",
     ["#FF4D00", "#FCDDCC"], "Suisse, Geist Mono", "Plan technique, orange braise.",
     "Le plan d'ingénieur : la conception pédagogique montrée comme une construction."),
    ("Orderful", R + "d95a35c2-d3f7-49e7-9ba7-282d52d3211d", I + "697fbb6a-b586-4dfc-b189-7570806efae4.jpg",
     ["#E42B0C", "#000000"], "Telegraf, Modern Gothic", "Poste de commande industriel, vermillon.",
     "Le monde des entrepôts et des opérations : parle aux employeurs de première ligne."),
    ("Agence Foudre", R + "c1534c74-f7b8-44de-a913-586d0f78fb08", I + "bfbb150c-5eab-46ae-9318-9ee9789a255a.jpg",
     ["#DB3C8A", "#00522D"], "Beni, Clash Grotesk", "Page de magazine, magenta et vert forêt.",
     "L'agence qui ose : deux couleurs franches qui ne se ressemblent pas. Le plus audacieux du mur."),
]


# « je veux de l'animation » (Daniel, 1er oct. 2026). Une vignette ne montre pas
# le mouvement : chaque carte mène AUSSI au site réel, où l'animation se voit.
MOUVEMENT = [
    ("GSAP", R + "00537a20-e99e-4ef2-b119-c6f532c44cc9", I + "a0928c1f-8a5c-4b01-bba0-8cf9d38ab0f5.jpg",
     ["#0E100F", "#FFFCE1"], "Mori", "La bibliothèque d'animation elle-même : tableau noir animé.",
     "L'outil qu'on prendrait : textes qui se révèlent au défilement, sections épinglées, minutage sur une narration.",
     "https://gsap.com/showcase/"),
    ("Lusion", R + "1b44386e-31a8-40b0-a577-27c088b51264", I + "2ae3d3b0-32e1-45b7-8bff-edf2d8a91844.jpg",
     ["#F0F1FA", "#FFFFFF"], "Aeonik", "Galerie de sculptures 3D sur verre dépoli.",
     "Le mouvement en 3D, sur fond clair : spectaculaire sans être sombre.", "https://lusion.co/"),
    ("Active Theory", R + "3416bd14-96bb-4c23-bd01-b2ea178ba5ce", I + "cc863ac2-3415-4e05-b30a-e2e8442c82b3.jpg",
     ["#000000", "#FFFFFF"], "NB Architekt, Times", "Vide cosmique, une seule lumière.",
     "L'immersion totale : on entre dans le site comme dans une pièce. Le plus spectaculaire, le plus coûteux.",
     "https://activetheory.net/"),
    ("monopo saigon", R + "3e52dd36-6ab1-48c6-bc40-47ef6d33abc2", I + "9f8b76b0-28b6-4677-b358-4ccdd5539e59.jpg",
     ["#000000", "#FFFFFF"], "Roobert, Raleway", "Iridescence liquide derrière une typographie nette.",
     "Une matière qui bouge derrière un texte immobile : le mouvement sans gêner la lecture.", "https://monopo.vn/"),
    ("14islands", R + "139c4bee-396d-494c-baf0-fe211bf4928d", I + "7eaab214-4218-430d-a091-6ac6554c1415.jpg",
     ["#070707", "#FFFFFF"], "Benton Sans, Aften Screen", "Galerie éditoriale monochrome, en mouvement.",
     "Le noir et blanc qui s'anime au défilement : sobre au repos, vivant quand on avance.", "https://14islands.com/"),
    ("Superhuman", R + "418b374a-be64-44f0-b17e-1d45308c7e62", I + "7589726e-fdbe-4a7c-8a61-66e62f6c8d8b.jpg",
     ["#421D24", "#714CB6"], "Super Sans VF", "Tableau de bord éditorial à l'heure dorée.",
     "Le logiciel d'entreprise qui soigne ses transitions : chaque geste répond, rien ne gesticule.",
     "https://superhuman.com/"),
]


def carte(i, r, pref="r"):
    nom, lien, img, couleurs, polices, ambiance, sert = r[:7]
    vivant = r[7] if len(r) > 7 else ""
    e = html.escape
    pastilles = "".join('<span class="pt" style="background:%s" title="%s"></span>' % (c, c) for c in couleurs)
    voir = (f'<a class="vivant" href="{e(vivant)}" target="_blank" rel="noopener">Voir l\'animation en vrai</a>' if vivant else "")
    return f"""<article class="c" data-id="{pref}{i:02d}" data-nom="{e(nom)}">
  <a class="vig" href="{e(lien)}" target="_blank" rel="noopener"><img src="{e(img)}" alt="Aperçu du site de {e(nom)}" loading="lazy"></a>
  <div class="corps">
    <h2>{e(nom)}</h2>
    <p class="amb">{e(ambiance)}</p>
    <p class="sert"><b>Pour nous :</b> {e(sert)}</p>
    <p class="meta"><span class="pts">{pastilles}</span><span>{e(polices)}</span></p>
    {voir}
    <div class="dec" role="group" aria-label="Réaction à {e(nom)}">
      <button type="button" data-v="aime">J'aime</button>
      <button type="button" data-v="bof">Bof</button>
      <button type="button" data-v="non">Non</button>
    </div>
    <input type="text" class="note" placeholder="Ce qui accroche ou ce qui rebute" aria-label="Note sur {e(nom)}">
  </div>
</article>"""


def main():
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(GABARIT % {
        "n": len(REFS),
        "cartes": "\n".join(carte(i, r) for i, r in enumerate(REFS, 1)),
        "mvt": "\n".join(carte(i, r, "m") for i, r in enumerate(MOUVEMENT, 1)),
        "n2": len(MOUVEMENT),
        "data": json.dumps([{"id": "r%02d" % i, "nom": r[0], "lien": r[1]} for i, r in enumerate(REFS, 1)]
                           + [{"id": "m%02d" % i, "nom": r[0], "lien": r[7]} for i, r in enumerate(MOUVEMENT, 1)], ensure_ascii=False),
    }, encoding="utf-8")
    print("Écrit : %s (%d références)" % (SORTIE.relative_to(RACINE), len(REFS)))


GABARIT = r"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Références BoucleDidactique</title>
<style>
@font-face{font-family:"Nunito";src:url("../../design-system/fonts/nunito-latin.woff2") format("woff2");font-weight:200 1000;font-display:swap}
:root{--page:#F7F7F5;--carte:#fff;--ink:#17181A;--ink-2:#4A4D52;--line:#E4E3DE;--vert:#0A8F5B}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%%}
body{margin:0;background:var(--page);color:var(--ink);font:17px/1.55 "Nunito",system-ui,-apple-system,sans-serif}
.cadre{max-width:1200px;margin:0 auto;padding:32px 16px 96px}
.sur{font-weight:800;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:#6B6E73}
h1{font-size:34px;line-height:1.15;margin:6px 0 12px;font-weight:900}
.chapeau{font-size:18px;color:var(--ink-2);max-width:70ch;margin:0 0 16px}
.barre{position:sticky;top:0;z-index:5;background:var(--page);padding:12px 0;border-bottom:1px solid var(--line);display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:20px}
.barre input{flex:1 1 320px;min-height:44px;font:inherit;font-size:16px;padding:0 14px;border:1px solid var(--line);border-radius:10px;background:var(--carte);color:var(--ink)}
.cpt{font-size:15px;color:var(--ink-2)}
button{font:inherit;font-size:15px;font-weight:700;min-height:44px;padding:0 16px;border:1px solid var(--line);border-radius:999px;background:var(--carte);color:var(--ink);cursor:pointer}
button[aria-pressed=true]{background:var(--ink);color:#fff;border-color:var(--ink)}
button:focus-visible,input:focus-visible,a:focus-visible{outline:3px solid var(--vert);outline-offset:2px}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px}
.c{background:var(--carte);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column}
.c.aime{border:2px solid var(--ink)}.c.non{opacity:.55}
.vig{display:block;aspect-ratio:16/10;background:#EEE;overflow:hidden}
.vig img{width:100%%;height:100%%;object-fit:cover;object-position:top;display:block}
.corps{padding:14px 16px 16px;display:flex;flex-direction:column;gap:6px;flex:1}
.c h2{font-size:20px;margin:0;font-weight:900}
.amb{margin:0;color:var(--ink-2);font-size:16px}
.sert{margin:0;font-size:16px}
.meta{margin:4px 0 0;display:flex;gap:10px;align-items:center;flex-wrap:wrap;font-size:13px;color:#6B6E73}
.pts{display:inline-flex;gap:4px}.pt{width:20px;height:20px;border-radius:6px;border:1px solid rgba(0,0,0,.15)}
.dec{display:flex;gap:12px;flex-wrap:wrap;margin-top:auto;padding-top:10px}
.note{min-height:44px;font:inherit;font-size:16px;padding:0 12px;border:1px solid var(--line);border-radius:10px;background:var(--page);color:var(--ink)}
.source{font-size:14px;color:#6B6E73;margin-top:32px}
.sec{font-size:24px;font-weight:900;margin:28px 0 8px}.sec span{font-size:14px;color:#6B6E73;margin-left:6px}
.sec-chap{color:var(--ink-2);margin:0 0 14px;max-width:70ch}
.vivant{align-self:flex-start;font-weight:800;color:var(--ink);min-height:44px;display:inline-flex;align-items:center}
@media (max-width:640px){h1{font-size:28px}.grille{grid-template-columns:1fr}}
</style></head>
<body><div class="cadre">
<div class="sur">La maison · Identité · à trancher</div>
<h1>BoucleDidactique : le mur de références</h1>
<p class="chapeau">Avant de refaire des pistes, %(n)d sites réels pour l'ambiance et %(n2)d pour le mouvement, très différents les uns des autres, montrés tels quels. Une réaction par vignette — j'aime, bof, non — et un mot si quelque chose accroche ou rebute. Les pistes suivantes se bâtiront sur ce qui ressort. Cliquer une vignette ouvre le système d'origine.</p>
<div class="barre"><input type="text" id="global" placeholder="Une idée qui n'est sur aucune vignette (un site, une marque, une ambiance…)" aria-label="Note générale"><span class="cpt" id="cpt"></span><button type="button" id="exp">Exporter</button></div>
<main>
<h2 class="sec">Les ambiances <span>%(n)d</span></h2>
<div class="grille">
%(cartes)s
</div>
<h2 class="sec">Le mouvement <span>%(n2)d</span></h2>
<p class="sec-chap">Vous voulez de l'animation : ces six sites sont connus pour la leur. La vignette ne montre rien du mouvement — « Voir l'animation en vrai » ouvre le site. Dites jusqu'où aller : une révélation discrète au défilement, ou une entrée spectaculaire.</p>
<div class="grille">
%(mvt)s
</div>
</main>
<p class="source">Vignettes et systèmes : styles.refero.design (liés, non copiés). Exclus d'office : le crème et le serif éditorial, les références de la v2. Page engendrée par build/boucledidactique_references_page.py.</p>
</div>
<script>
(function(){
  var DATA=%(data)s, CLE="boucledidactique-references-v1", etat={};
  try{etat=JSON.parse(localStorage.getItem(CLE)||"{}")}catch(e){etat={}}
  function garder(){try{localStorage.setItem(CLE,JSON.stringify(etat))}catch(e){}}
  var cartes=[].slice.call(document.querySelectorAll(".c")), glob=document.getElementById("global");
  glob.value=etat._global||""; glob.addEventListener("input",function(){etat._global=glob.value;garder();});
  function compter(){var n=cartes.filter(function(c){return (etat[c.dataset.id]||{}).v}).length;
    var a=cartes.filter(function(c){return (etat[c.dataset.id]||{}).v==="aime"}).length;
    document.getElementById("cpt").textContent=n+" / "+cartes.length+" vues · "+a+" j'aime";}
  cartes.forEach(function(c){
    var id=c.dataset.id, bs=[].slice.call(c.querySelectorAll(".dec button")), note=c.querySelector(".note");
    function peindre(){var v=(etat[id]||{}).v; bs.forEach(function(b){b.setAttribute("aria-pressed",String(b.dataset.v===v))});
      c.classList.toggle("aime",v==="aime"); c.classList.toggle("non",v==="non");}
    note.value=(etat[id]||{}).note||"";
    bs.forEach(function(b){b.addEventListener("click",function(){var x=etat[id]||{}; x.v=(x.v===b.dataset.v)?"":b.dataset.v; etat[id]=x; garder(); peindre(); compter();})});
    note.addEventListener("input",function(){var x=etat[id]||{}; x.note=note.value; etat[id]=x; garder();});
    peindre();
  });
  document.getElementById("exp").addEventListener("click",function(){
    var out={page:"boucledidactique-references",date:new Date().toISOString().slice(0,10),general:etat._global||"",
      reactions:DATA.map(function(r){var x=etat[r.id]||{};return {nom:r.nom,lien:r.lien,reaction:x.v||"",note:x.note||""}})};
    var txt=JSON.stringify(out,null,2), a=document.createElement("a");
    a.href=URL.createObjectURL(new Blob([txt],{type:"application/json"})); a.download="boucledidactique-references.json"; a.click();
    if(navigator.clipboard){navigator.clipboard.writeText(txt).catch(function(){})}
  });
  compter();
})();
</script>
</body></html>
"""

if __name__ == "__main__":
    main()
