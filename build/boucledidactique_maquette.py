#!/usr/bin/env python3
"""La maquette du site BoucleDidactique — une page d'accueil qui bouge.

    python3 build/boucledidactique_maquette.py
    # écrit assets/presentations/identite/boucledidactique-maquette.html

D'OÙ ELLE VIENT. Le 1er octobre 2026, après deux tours de pistes refusés,
Daniel a réagi au mur de références : il aime Ramp, Brex, Quizlet, Figure 03
et surtout Agence Foudre ; pour le mouvement, GSAP et Lusion. Non au sombre, au
plan technique, au monochrome. Et le site aura une section démo : les
applications déjà faites.

Ce qui en est tiré :
  · la palette d'Agence Foudre (magenta + vert forêt), le jaune surligneur de
    Ramp en touche, sur fond BLANC (aucun crème : c'est ce qui faisait
    « français ») ;
  · Clash Grotesk — la police même d'Agence Foudre, libre chez Fontshare
    (licence ITF) — avec General Sans pour le texte ;
  · le titre cinétique à la GSAP (SplitText, lettres qui montent) et des
    anneaux en 3D à la Lusion (three.js) : l'anneau, c'est la boucle ;
  · la section démo lue dans build/applications.py — la même liste que l'onglet
    « Applications » du classeur, donc jamais en retard sur lui.

v2 (même jour) : « couleur trop vive ». La structure et le mouvement restent ;
quatre palettes adoucies (prune et sauge, ardoise et brique, pétrole et lilas,
graphite et bleu) se changent en direct par un sélecteur, anneaux 3D compris ;
la vive reste au bout pour comparer. Jetons neutres : --c1 (couleur de marque),
--c2 (action), --c3 (accent pâle). Contrastes calculés pour chacune : texte
courant ≥ 4,5:1, grandes formes ≥ 3:1.

v1 — contrastes (calculés) : le magenta #DB3C8A fait 4,18:1 sur blanc — il ne porte
que des formes et du texte de grande taille ; le texte courant magenta prend
#B8216C (6,05:1). Le vert forêt porte les boutons (blanc 9,35:1, jaune 7,58:1).

Mouvement : tout passe par GSAP + ScrollTrigger, et `prefers-reduced-motion`
coupe tout — la page reste complète et lisible sans une seule animation. Les
icônes viennent de Tabler (build/icone.py), jamais dessinées.

Polices et bibliothèques sont servies par le dépôt
(assets/presentations/boucledidactique/fonts et vendor) : la page ne demande
rien au réseau.
"""
import html
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parent
sys.path.insert(0, str(ICI))
import applications  # noqa: E402
import icone  # noqa: E402

SORTIE = RACINE / "assets" / "presentations" / "identite" / "boucledidactique-maquette.html"
# Le système servi : polices et bibliothèques en local (rien ne vient du réseau).
SYSTEME = RACINE / "assets" / "presentations" / "boucledidactique"
VERS_SYSTEME = "../boucledidactique/"
VERS_RACINE = "../../../"

# Icône Tabler par application (clé = chemin). Une application neuve sans icône
# prend « sparkles » : elle paraît quand même.
ICONES = {
    "modules-autonomes/compostelle/": "walk",
    "modules-autonomes/montreal/": "building-skyscraper",
    "modules-autonomes/hotel-reception/": "bell-ringing",
    "modules-autonomes/francoeur-planches/": "shirt",
    "modules-autonomes/belrive-bloc3/": "building-factory",
    "modules-autonomes/chaussure-blocA/": "shoe",
    "assets/presentations/formation-dea-v5.html": "heartbeat",
    "assets/presentations/simdea-vous-anime-v5.html": "user",
    "assets/presentations/simulateur-dea.html": "device-heart-monitor",
    "assets/presentations/atelier-prototypes/banc-de-panne/tournee.html": "coffee",
    "assets/presentations/courriel-de-trop/le-courriel-de-trop.html": "mail-off",
    "assets/presentations/a-la-main-dabord/a-la-main-dabord.html": "tool",
    "assets/presentations/le-dernier-millimetre/le-dernier-millimetre.html": "car",
    "assets/presentations/boucle-animee.html": "refresh-dot",
    "assets/presentations/atelier-prototypes/index.html": "flask",
    "assets/presentations/cv/daniel-tousignant-cv.html": "id-badge",
}
# Le site parle aux employeurs : ses rayons, pas ceux du classeur.
RAYONS = {"Formations en entreprise": "Formations en entreprise",
          "Portfolio": "Pièces d'apprentissage",
          "Voyage": "Applications grand public"}
TEINTES = ["mag", "foret", "jaune"]


def demos():
    traces, _ = icone.charger()
    blocs = []
    # Le site parle aux employeurs : leurs formations d'abord, le grand public en dernier.
    ordre = list(RAYONS)
    rangees = sorted(applications.APPLICATIONS, key=lambda e: ordre.index(e[0]) if e[0] in ordre else 99)
    for k, (etagere, apps) in enumerate(rangees):
        cartes = []
        for nom, chemin, quoi, *_ in apps:
            ic = ICONES.get(chemin, "sparkles")
            if ic not in traces:
                ic = "sparkles"
            cartes.append(
                '<a class="demo t-%s" href="%s" target="_blank" rel="noopener">'
                '<span class="demo-ic">%s</span><span class="demo-nom">%s</span>'
                '<span class="demo-quoi">%s</span><span class="demo-go">Essayer →</span></a>'
                % (TEINTES[len(cartes) % 3], html.escape(VERS_RACINE + chemin),
                   icone.svg(ic, traces, 2, 28), html.escape(nom), html.escape(quoi)))
        blocs.append('<div class="rayon"><h3 class="rayon-tit">%s <span>%d</span></h3><div class="demos">%s</div></div>'
                     % (html.escape(RAYONS.get(etagere, etagere)), len(cartes), "".join(cartes)))
    return "\n".join(blocs), sum(len(a) for _, a in applications.APPLICATIONS)


def main():
    blocs, n = demos()
    # Les @font-face du système, recopiés avec le chemin qui convient à cette page.
    polices = (SYSTEME / "polices.css").read_text(encoding="utf-8").replace('url("fonts/', 'url("' + VERS_SYSTEME + 'fonts/')
    page = GABARIT.replace("@@DEMOS@@", blocs).replace("@@N@@", str(n)).replace("@@POLICES@@", polices)
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page, encoding="utf-8")
    print("Écrit : %s (%d démos)" % (SORTIE.relative_to(RACINE), n))


GABARIT = r"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>BoucleDidactique — maquette</title>
<link rel="icon" type="image/svg+xml" href="../boucledidactique/logo/favicon.svg">
<style id="polices">@@POLICES@@</style>
<style>
:root{
  --blanc:#FFFFFF; --gris:#F2F2EF; --encre:#111311; --encre-2:#5C605C; --trait:#E2E2DD;
  /* Palette retenue le 1er oct. 2026 : graphite et bleu. Les autres restent
     au sélecteur pour mémoire, posées par [data-palette] sur <html>. */
  --c1:#6E93BF; --c1-texte:#3E6593; --c1-doux:#E5EDF6;
  --c2:#26292E; --c2-doux:#E6E8EB; --c3:#D4E2F0; --fin-texte:#111311;
  --f-titre:"Clash Grotesk","Arial Black",system-ui,sans-serif;
  --f-texte:"General Sans",system-ui,-apple-system,sans-serif;
}
:root[data-palette="ardoise"]{--c1:#C97B66;--c1-texte:#A3523E;--c1-doux:#F6E7E2;--c2:#2F4558;--c2-doux:#E3E9EF;--c3:#F2D7CF;--fin-texte:#111311}
:root[data-palette="petrole"]{--c1:#8C7BC2;--c1-texte:#5E4B9A;--c1-doux:#ECE8F6;--c2:#1E4E5C;--c2-doux:#DDEBEC;--c3:#CFE6E4;--fin-texte:#111311}
:root[data-palette="prune"]{--c1:#8A4F6E;--c1-texte:#7A3E5D;--c1-doux:#F1E6EC;--c2:#3F5E4E;--c2-doux:#E3ECE6;--c3:#DCE8D2;--fin-texte:#FFFFFF}
:root[data-palette="vive"]{--c1:#DB3C8A;--c1-texte:#B8216C;--c1-doux:#FBE3EF;--c2:#00522D;--c2-doux:#DCEFE4;--c3:#E4F222;--fin-texte:#111311}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
/* Le sélecteur de palette (maquette seulement) */
.palettes{display:flex;gap:6px;align-items:center;flex-wrap:wrap;justify-content:center}
.palettes b{font-size:13px;padding:0 4px;color:#cfd2cf;font-weight:600}
.palettes button{font:inherit;font-size:14px;font-weight:600;min-height:40px;padding:0 12px 0 8px;border-radius:999px;border:1px solid var(--trait);background:#fff;color:var(--encre);cursor:pointer;display:inline-flex;align-items:center;gap:6px}
.palettes button[aria-pressed=true]{background:var(--c3);color:var(--encre);border-color:var(--c3)}
.palettes i{width:18px;height:18px;border-radius:50%;display:inline-block;flex:none}
body{margin:0;background:var(--blanc);color:var(--encre);font:17px/1.55 var(--f-texte);overflow-x:hidden}
a{color:inherit}
:focus-visible{outline:3px solid var(--c2);outline-offset:3px}
.bande-maquette{background:var(--encre);color:#fff;font-size:14px;text-align:center;padding:8px 16px;display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;justify-content:center}
.bande-maquette a{color:var(--c3);font-weight:600}

/* En-tête */
.tete{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--trait)}
.tete-in{max-width:1240px;margin:0 auto;padding:12px 24px;display:flex;align-items:center;gap:24px}
.marque{display:inline-flex;align-items:center;gap:10px;text-decoration:none}
.marque svg{width:34px;height:34px}
.mot{font-family:var(--f-titre);font-size:24px;font-weight:600;letter-spacing:-.02em}
.mot b{font-weight:700;color:var(--c1-texte)}
.nav{display:flex;gap:28px;margin-left:auto;font-weight:500}
.nav a{text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:0 24px;white-space:nowrap;border-radius:999px;font-weight:600;text-decoration:none;font-size:16px;border:2px solid transparent;transition:transform .2s}
.btn:hover{transform:translateY(-2px)}
.btn-foret{background:var(--c2);color:var(--c3)}
.btn-ligne{border-color:var(--encre);color:var(--encre)}

/* Accueil : le titre cinétique et les anneaux 3D */
.hero{position:relative;min-height:calc(100vh - 110px);min-height:calc(100dvh - 110px);display:flex;align-items:center;overflow:hidden}
#scene{position:absolute;inset:0;width:100%;height:100%;z-index:0}
.hero-in{position:relative;z-index:1;max-width:1240px;margin:0 auto;padding:48px 24px;width:100%;pointer-events:none}
@media (max-width:860px){.hero{align-items:flex-end}.hero-in{padding-top:38vh;padding-bottom:40px}}
.hero-in *{pointer-events:auto}
.sur{font-weight:600;font-size:14px;letter-spacing:.12em;text-transform:uppercase;color:var(--c2);margin:0 0 16px}
.hero h1{font-family:var(--f-titre);font-weight:700;font-size:clamp(48px,8.6vw,136px);line-height:.95;letter-spacing:-.02em;word-spacing:.06em;margin:0 0 28px;max-width:11ch}
.hero h1 .m{color:var(--c1)}
.surligne{position:relative;display:inline-block;z-index:0}
.surligne::before{content:"";position:absolute;left:-.04em;right:-.04em;bottom:.08em;height:.32em;background:var(--c3);z-index:-1;transform-origin:left;transform:scaleX(var(--sx,1))}
.hero p.chap{font-size:clamp(18px,1.6vw,22px);max-width:34ch;color:var(--encre-2);margin:0 0 28px;background:rgba(255,255,255,.75);border-radius:8px}
.rangee{display:flex;gap:12px;flex-wrap:wrap}

/* Le bandeau qui défile */
.defile{background:var(--c2);color:var(--c3);overflow:hidden;white-space:nowrap;padding:18px 0;font-family:var(--f-titre);font-weight:600;font-size:clamp(26px,4vw,48px);letter-spacing:-.01em}
.defile-pista{display:inline-flex;gap:48px;padding-right:48px}
.defile-pista span::after{content:"↻";margin-left:48px;color:var(--c1-doux)}

/* La boucle, épinglée au défilement */
.section{max-width:1240px;margin:0 auto;padding:120px 24px}
.h2{font-family:var(--f-titre);font-weight:700;font-size:clamp(40px,6vw,84px);line-height:.95;letter-spacing:-.03em;margin:0 0 20px}
.chap2{font-size:20px;color:var(--encre-2);max-width:52ch;margin:0 0 48px}
.boucle{display:grid;grid-template-columns:minmax(260px,420px) 1fr;gap:64px;align-items:center}
.cercle{position:relative;aspect-ratio:1}
.cercle svg{width:100%;height:100%;overflow:visible}
.cercle .fond{fill:none;stroke:var(--gris);stroke-width:22}
.cercle .trace{fill:none;stroke:var(--c1);stroke-width:22;stroke-linecap:round}
.cercle .num{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;flex-direction:column;font-family:var(--f-titre)}
.cercle .num b{font-size:clamp(64px,8vw,110px);line-height:1;font-weight:700}
.cercle .num span{font-size:18px;color:var(--encre-2);font-family:var(--f-texte)}
.etapes{list-style:none;margin:0;padding:0;display:grid;gap:14px}
.etape{border:2px solid var(--trait);border-radius:20px;padding:22px 26px;transition:background .3s,border-color .3s,transform .3s}
.etape h3{font-family:var(--f-titre);font-size:30px;font-weight:600;margin:0 0 4px;letter-spacing:-.01em}
.etape p{margin:0;color:var(--encre-2)}
.etape.on{background:var(--c1-doux);border-color:var(--c1);transform:translateX(8px)}
.etape.on h3{color:var(--c1-texte)}

/* Démos */
.demos-zone{background:var(--gris)}
.rayon{margin-top:48px}
.rayon-tit{font-family:var(--f-titre);font-size:28px;font-weight:600;margin:0 0 16px}
.rayon-tit span{font-family:var(--f-texte);font-size:16px;color:var(--encre-2);font-weight:500;margin-left:6px}
.demos{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:16px}
.demo{position:relative;display:flex;flex-direction:column;gap:10px;min-height:230px;padding:24px;border-radius:24px;text-decoration:none;background:var(--blanc);border:2px solid transparent;transition:transform .25s,border-color .25s;will-change:transform}
.demo:hover{border-color:var(--encre)}
.demo-ic{width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center}
.t-mag .demo-ic{background:var(--c1);color:#fff}
.t-foret .demo-ic{background:var(--c2);color:var(--c3)}
.t-jaune .demo-ic{background:var(--c3);color:var(--encre)}
.demo-nom{font-family:var(--f-titre);font-size:24px;font-weight:600;line-height:1.1;letter-spacing:-.01em}
.demo-quoi{color:var(--encre-2);font-size:16px}
.demo-go{margin-top:auto;font-weight:600;color:var(--c2)}

/* Le diagnostic en chiffres */
.chiffres{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px}
.chiffre{border-top:4px solid var(--encre);padding-top:18px}
.chiffre b{display:block;font-family:var(--f-titre);font-size:clamp(64px,8vw,104px);line-height:1;font-weight:700;letter-spacing:-.03em}
.chiffre:nth-child(2) b{color:var(--c1-texte)}
.chiffre span{color:var(--encre-2);font-size:18px}

.fin{background:var(--c1);color:var(--fin-texte);text-align:center;padding:120px 24px}
.fin .h2{max-width:14ch;margin:0 auto 32px}
.pied{max-width:1240px;margin:0 auto;padding:28px 24px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;color:var(--encre-2);font-size:15px}

@media (max-width:480px){.tete .btn{padding:0 16px;font-size:15px}.mot{font-size:20px}}
@media (max-width:860px){.nav{display:none}.boucle{grid-template-columns:1fr}.section{padding:80px 20px}.tete-in{padding:10px 20px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style></head>
<body>
<div class="bande-maquette"><span>Maquette de direction — pas encore le site. <a href="boucledidactique-references.html">Le mur de références</a></span>
<div class="palettes" role="group" aria-label="Palette de la maquette">
  <b>Palette</b>
  <button type="button" data-p="prune"><i style="background:linear-gradient(90deg,#8A4F6E 50%,#3F5E4E 50%)"></i>Prune et sauge</button>
  <button type="button" data-p="ardoise"><i style="background:linear-gradient(90deg,#C97B66 50%,#2F4558 50%)"></i>Ardoise et brique</button>
  <button type="button" data-p="petrole"><i style="background:linear-gradient(90deg,#8C7BC2 50%,#1E4E5C 50%)"></i>Pétrole et lilas</button>
  <button type="button" data-p="graphite"><i style="background:linear-gradient(90deg,#6E93BF 50%,#26292E 50%)"></i>Graphite et bleu (retenue)</button>
  <button type="button" data-p="vive"><i style="background:linear-gradient(90deg,#DB3C8A 50%,#00522D 50%)"></i>La vive (refusée)</button>
</div>
</div>

<header class="tete"><div class="tete-in">
  <a class="marque" href="#" aria-label="BoucleDidactique, accueil">
    <!-- Le quart de tour, retenu le 1er oct. 2026 (systemes-design/boucledidactique/logo/). -->
    <svg viewBox="0 0 48 48" aria-hidden="true"><g fill="none" stroke-width="7"><path d="M39.91 25.67A16 16 0 0 1 25.67 39.91" stroke="var(--c2)"/><path d="M22.33 39.91A16 16 0 0 1 8.09 25.67" stroke="var(--c2)"/><path d="M8.09 22.33A16 16 0 0 1 22.33 8.09" stroke="var(--c2)"/><path class="quart-logo" d="M25.67 8.09A16 16 0 0 1 39.91 22.33" stroke="var(--c1)"/></g></svg>
    <span class="mot">Boucle<b>Didactique</b></span>
  </a>
  <nav class="nav" aria-label="Sections"><a href="#boucle">La méthode</a><a href="#demos">Démos</a><a href="#diagnostic">Diagnostic</a></nav>
  <a class="btn btn-foret" href="#contact">Nous écrire</a>
</div></header>

<main>
<section class="hero" aria-labelledby="titre">
  <canvas id="scene" aria-hidden="true"></canvas>
  <div class="hero-in">
    <p class="sur">Formation en entreprise</p>
    <h1 id="titre">Des formations qui <span class="m">se jouent</span>, <span class="surligne">pour vrai</span>.</h1>
    <p class="chap">Vos employés font le geste eux-mêmes, dans une pièce jouée. Puis nous mesurons ce qui a changé au poste de travail.</p>
    <div class="rangee"><a class="btn btn-foret" href="#demos">Essayer une démo</a><a class="btn btn-ligne" href="#boucle">Voir la méthode</a></div>
  </div>
</section>

<div class="defile" aria-hidden="true"><div class="defile-pista"><span>Cadrer</span><span>Écrire</span><span>Faire jouer</span><span>Mesurer</span><span>Réviser</span><span>Cadrer</span><span>Écrire</span><span>Faire jouer</span><span>Mesurer</span><span>Réviser</span></div></div>

<section class="section" id="boucle" aria-labelledby="t-boucle">
  <h2 class="h2" id="t-boucle">Une boucle, pas une ligne droite.</h2>
  <p class="chap2">Une formation n'est jamais finie au premier jet. Nous la mettons à l'épreuve, nous corrigeons, et nous recommençons jusqu'à ce que les gestes changent.</p>
  <div class="boucle">
    <div class="cercle">
      <svg viewBox="0 0 200 200"><circle class="fond" cx="100" cy="100" r="80"/><circle class="trace" cx="100" cy="100" r="80" pathLength="100" stroke-dasharray="100" stroke-dashoffset="0" transform="rotate(-90 100 100)"/></svg>
      <div class="num"><b id="tour">4</b><span>temps</span></div>
    </div>
    <ol class="etapes">
      <li class="etape on"><h3>1 · Cadrer</h3><p>Ce que l'employé saura faire, observé au poste, avec un critère qui se vérifie.</p></li>
      <li class="etape on"><h3>2 · Écrire et dessiner</h3><p>Une version zéro : des croquis qui avancent sous une voix, et une partie jouée.</p></li>
      <li class="etape on"><h3>3 · Faire jouer et mesurer</h3><p>Vos employés la jouent. Leurs réponses disent ce qui est compris, et ce qui ne l'est pas.</p></li>
      <li class="etape on"><h3>4 · Réviser</h3><p>Chaque constat est corrigé, puis réaudité — jusqu'à zéro constat majeur.</p></li>
    </ol>
  </div>
</section>

<section class="demos-zone" id="demos" aria-labelledby="t-demos"><div class="section">
  <h2 class="h2" id="t-demos">Essayez-les.</h2>
  <p class="chap2">@@N@@ applications et pièces déjà faites. Elles s'ouvrent dans le navigateur, sur ordinateur comme sur téléphone.</p>
  @@DEMOS@@
</div></section>

<section class="section" id="diagnostic" aria-labelledby="t-diag">
  <h2 class="h2" id="t-diag">La preuve, en chiffres.</h2>
  <p class="chap2">Le diagnostic didactique juge votre matériel par les réponses de vos employés — pas par l'impression qu'il donne.</p>
  <div class="chiffres">
    <div class="chiffre"><b data-compte="23">23</b><span>critères d'audit, de l'alignement au transfert au poste</span></div>
    <div class="chiffre"><b data-compte="86" data-suffixe=" %">86 %</b><span>de réponses justes au premier essai, sur une trousse révisée</span></div>
    <div class="chiffre"><b data-compte="0">0</b><span>constat majeur à la livraison : la boucle ne s'arrête qu'à ce moment-là</span></div>
  </div>
</section>

<section class="fin" id="contact" aria-labelledby="t-fin">
  <h2 class="h2" id="t-fin">Vingt minutes pour voir si c'est pour vous.</h2>
  <a class="btn btn-foret" href="#">Nous écrire</a>
</section>
</main>
<footer class="pied"><span>BoucleDidactique · conception pédagogique pour la formation en entreprise</span><span>Montréal</span></footer>

<script src="../boucledidactique/vendor/gsap.min.js"></script>
<script src="../boucledidactique/vendor/ScrollTrigger.min.js"></script>
<script src="../boucledidactique/vendor/SplitText.min.js"></script>
<script src="../boucledidactique/vendor/three.min.js"></script>
<script>
(function(){
  var calme = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  window.__maquette = {calme: calme, gsap: !!window.gsap, three: !!window.THREE, anneaux: 0};

  /* ── Les anneaux en 3D (à la Lusion) : la boucle, littéralement ── */
  (function scene(){
    var c = document.getElementById("scene");
    if (!window.THREE || !c) return;
    var r = new THREE.WebGLRenderer({canvas: c, antialias: true, alpha: true});
    r.setPixelRatio(Math.min(devicePixelRatio, 2));
    var s = new THREE.Scene(), cam = new THREE.PerspectiveCamera(35, 1, .1, 100);
    cam.position.set(0, 0, 14);
    s.add(new THREE.AmbientLight(0xffffff, .55));
    var d = new THREE.DirectionalLight(0xffffff, 1.1); d.position.set(4, 6, 8); s.add(d);
    var d2 = new THREE.DirectionalLight(0xffffff, .35); d2.position.set(-6, -3, 4); s.add(d2);
    // Les teintes viennent des jetons CSS : changer de palette repeint les anneaux.
    var ROLES = ["--c1", "--c2", "--c3", "--c1", "--encre", "--c3", "--c2"];
    function lire(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim() || "#888888";}
    var teintes = ROLES.map(function(v){return new THREE.Color(lire(v)).getHex();});
    var groupe = new THREE.Group(); s.add(groupe);
    var anneaux = teintes.map(function(t, i){
      var g = i % 3 === 0 ? new THREE.TorusGeometry(1.15, .42, 40, 90) : new THREE.TorusGeometry(.8, .3, 32, 80);
      var m = new THREE.MeshStandardMaterial({color: t, roughness: .35, metalness: .05});
      var o = new THREE.Mesh(g, m);
      // Tous à droite du titre (x positif) : le texte garde la moitié gauche libre.
      o.userData = {base: new THREE.Vector3(1.9 + (i * 1.37) % 4.3, ((i * 1.7) % 5.2) - 2.6, -((i * 2.1) % 4)),
                    vit: .2 + (i % 4) * .08, phase: i * 1.3};
      o.position.copy(o.userData.base);
      o.rotation.set(i, i * .7, 0);
      groupe.add(o); return o;
    });
    window.__maquette.anneaux = anneaux.length;
    window.__repeindre = function(){
      anneaux.forEach(function(o, i){o.material.color.set(lire(ROLES[i]));});
      if (calme) r.render(s, cam);
    };
    function taille(){var w = c.clientWidth, h = c.clientHeight; r.setSize(w, h, false); cam.aspect = w / h; cam.updateProjectionMatrix();
      // Téléphone : les anneaux montent au-dessus du titre, plus petits.
      var etroit = w < 860;
      groupe.position.set(etroit ? -2.05 : 0, etroit ? 3.0 : 0, 0); groupe.scale.setScalar(etroit ? .5 : 1);}
    taille(); addEventListener("resize", taille);
    var px = 0, py = 0, defil = 0;
    addEventListener("pointermove", function(e){px = e.clientX / innerWidth - .5; py = e.clientY / innerHeight - .5;});
    addEventListener("scroll", function(){defil = Math.min(scrollY / innerHeight, 1.5);}, {passive: true});
    var t0 = performance.now();
    function tour(t){
      var k = (t - t0) / 1000;
      anneaux.forEach(function(o){var u = o.userData;
        o.rotation.x += .004 * u.vit * 10; o.rotation.y += .003 * u.vit * 10;
        o.position.y = u.base.y + Math.sin(k * u.vit + u.phase) * .35 + defil * (1 + u.vit * 3);});
      groupe.rotation.y += ((px * .5) - groupe.rotation.y) * .05;
      groupe.rotation.x += ((py * .3) - groupe.rotation.x) * .05;
      r.render(s, cam);
      if (!calme) requestAnimationFrame(tour);
    }
    requestAnimationFrame(tour);   // en mouvement réduit : une seule image, immobile
  })();

  /* Le sélecteur de palette : se souvient du choix sur ce poste. */
  (function(){
    var CLE = "boucledidactique-palette-v2", el = document.documentElement, choix = "graphite";
    try { choix = localStorage.getItem(CLE) || "graphite"; } catch (e) {}
    var bs = [].slice.call(document.querySelectorAll(".palettes button"));
    function poser(p){
      if (p === "graphite") el.removeAttribute("data-palette"); else el.setAttribute("data-palette", p);
      bs.forEach(function(b){b.setAttribute("aria-pressed", String(b.dataset.p === p));});
      try { localStorage.setItem(CLE, p); } catch (e) {}
      if (window.__repeindre) window.__repeindre();
      window.__maquette.palette = p;
    }
    bs.forEach(function(b){b.addEventListener("click", function(){poser(b.dataset.p);});});
    poser(choix);
  })();

  if (!window.gsap || calme) return;   // sans GSAP ou en mouvement réduit : la page reste entière, immobile
  gsap.registerPlugin(ScrollTrigger, SplitText);

  /* ── Le titre cinétique (à la GSAP) ── */
  var titre = new SplitText("#titre", {type: "words,chars", charsClass: "ch"});
  gsap.set("#titre", {perspective: 600});
  var tl = gsap.timeline({defaults: {ease: "back.out(1.6)"}});
  gsap.fromTo(".quart-logo", {rotation: 0}, {rotation: 360, svgOrigin: "24 24", duration: 2.4, ease: "steps(4)", delay: .2});
  tl.from(titre.chars, {yPercent: 120, rotateX: -80, opacity: 0, duration: .8, stagger: .025})
    .fromTo(".surligne", {"--sx": 0}, {"--sx": 1, duration: .6, ease: "power3.inOut"}, "-=.3")
    .from(".hero .sur, .hero .chap, .hero .rangee", {y: 24, opacity: 0, duration: .6, stagger: .1, ease: "power2.out"}, "-=.5");

  /* ── Le bandeau qui défile sans fin ── */
  var piste = document.querySelector(".defile-pista");
  gsap.to(piste, {xPercent: -50, duration: 22, ease: "none", repeat: -1});

  /* ── La boucle : le cercle se trace au défilement, les étapes s'allument ── */
  var etapes = gsap.utils.toArray(".etape");
  etapes.forEach(function(e){e.classList.remove("on")});
  gsap.set(".cercle .trace", {attr: {"stroke-dashoffset": 100}});
  ScrollTrigger.create({
    trigger: ".boucle", start: "top 70%", end: "bottom 40%", scrub: .6,
    onUpdate: function(st){
      var p = st.progress;
      document.querySelector(".cercle .trace").setAttribute("stroke-dashoffset", String(100 - p * 100));
      var n = Math.min(4, Math.floor(p * 4.0001) + (p > 0 ? 1 : 0));
      etapes.forEach(function(e, i){e.classList.toggle("on", i < n)});
      document.getElementById("tour").textContent = String(Math.max(1, n));
    }
  });

  /* ── Les titres de section montent ; les démos arrivent en cascade ── */
  gsap.utils.toArray(".h2").forEach(function(h){
    var sp = new SplitText(h, {type: "words"});
    gsap.from(sp.words, {yPercent: 100, opacity: 0, duration: .7, stagger: .06, ease: "power3.out",
      scrollTrigger: {trigger: h, start: "top 85%"}});
  });
  gsap.utils.toArray(".demos").forEach(function(g){
    gsap.from(g.children, {y: 40, opacity: 0, rotate: 2, duration: .6, stagger: .07, ease: "power2.out",
      scrollTrigger: {trigger: g, start: "top 85%"}});
  });
  /* Les cartes se penchent vers le pointeur. */
  document.querySelectorAll(".demo").forEach(function(d){
    d.addEventListener("pointermove", function(e){var b = d.getBoundingClientRect();
      gsap.to(d, {rotateY: ((e.clientX - b.left) / b.width - .5) * 8, rotateX: -((e.clientY - b.top) / b.height - .5) * 8,
        transformPerspective: 700, duration: .3});});
    d.addEventListener("pointerleave", function(){gsap.to(d, {rotateX: 0, rotateY: 0, duration: .5, ease: "elastic.out(1,.5)"});});
  });

  /* ── Les chiffres comptent ── */
  document.querySelectorAll("[data-compte]").forEach(function(b){
    var fin = +b.dataset.compte, suf = b.dataset.suffixe || "", o = {v: 0};
    if (!fin) return;
    gsap.to(o, {v: fin, duration: 1.6, ease: "power2.out", scrollTrigger: {trigger: b, start: "top 85%"},
      onUpdate: function(){b.textContent = Math.round(o.v) + suf;}});
  });
  window.__maquette.anime = true;
})();
</script>
</body></html>
"""

if __name__ == "__main__":
    main()
