#!/usr/bin/env python3
"""La page de décision sur les 25 astuces de design — un jugement par astuce retenue.

    python3 build/astuces_design_page.py   # écrit assets/presentations/identite/astuces-design.html

Le 30 septembre 2026, Daniel a apporté un guide de 25 astuces pour mieux
designer avec Claude (« 25 tricks to level up Claude Design », RoboNuggets).
Chaque astuce a été lue contre ce qui existe déjà ici — le système francis,
Trame, les compétences de ~/.claude/skills, la mémoire — et reçoit un avis :
déjà en place, à adopter (et sous quelle forme : compétence, fiche de mémoire,
simple ressource), à essayer, ou à écarter, avec la raison.

La page est GÉNÉRÉE : l'avis vit dans ASTUCES ci-dessous, pas dans le HTML.
Les décisions de Daniel vivent dans le localStorage du poste ; « Exporter »
rend un JSON à recoller dans une session, et c'est ce fichier qui pilote la
suite (quelles compétences écrire, quelles fiches poser).
"""
import html
import json
import pathlib

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "identite" / "astuces-design.html"

# avis : place (déjà en place) · adopter · essayer
# Les cinq astuces écartées (8, 13, 14, 15, 18) ont été retirées à la demande de
# Daniel le 30 sept. 2026 ; les numéros d'origine sont gardés.
# forme : competence · memoire · ressource · rien
# prio : 1 (d'abord) à 3 (plus tard) ; 0 = sans objet
ASTUCES = [
    dict(n=1, titre="Un système de design, fait de zéro ou tiré d'un exemple",
         quoi="Décrire la marque, ou montrer une capture, un site, un diaporama, et laisser Claude en tirer couleurs, polices et composants.",
         avis="place", forme="rien", prio=0,
         pourquoi="C'est déjà la fondation : francis (assets/design-system/), Trame et Braise existent, et Braise a justement été relevé sur une capture. La méthode du relevé est écrite (relever un design externe).",
         geste="Rien à faire."),
    dict(n=2, titre="Une galerie de 2 000 systèmes prêts à lire (Refero Styles)",
         quoi="styles.refero.design publie des systèmes réels, rédigés pour qu'un modèle les lise : on copie, on ajuste, on colle.",
         avis="adopter", forme="memoire", prio=2,
         pourquoi="Utile là où il faut inventer une marque vite : les enseignes fictives des formations en entreprise (Maison Francœur, Rive-Claire, Chaussures Rivard) et les pièces du portfolio. Inutile pour francis, qui est fixé.",
         geste="Une ligne dans la compétence trousse-de-metier, à l'étape de l'identité de l'enseigne : partir d'un système Refero plutôt que d'une page blanche."),
    dict(n=3, titre="Laisser Claude choisir les trois plus proches",
         quoi="Donner la galerie et une phrase sur l'entreprise ; recevoir trois liens et une raison chacun.",
         avis="adopter", forme="memoire", prio=2,
         pourquoi="Va avec l'astuce 2. La galerie se charge en JavaScript : le navigateur intégré la lit, un simple téléchargement non. Même geste pour les pièces du portfolio.",
         geste="Même ligne que l'astuce 2, avec la précision : passer par le navigateur, pas par un téléchargement."),
    dict(n=4, titre="Un système de design rangé dans une compétence",
         quoi="Dans Claude Code, un système est une compétence : /duolingo, et tout ce qu'on demande sort dans ce style.",
         avis="adopter", forme="competence", prio=1,
         pourquoi="Le système francis a un SKILL.md, mais il dort dans le dépôt : il ne se déclenche que si une compétence de module le cite. Une page du portfolio ou de la maison peut le rater. En faire /francis et /trame le rend appelable partout, et règle le choix du système en un mot.",
         geste="Écrire deux compétences minces, /francis et /trame, qui pointent vers les jetons et les règles existants (sans les recopier), plus les pièges déjà payés : jetons recopiés et non importés en file://, sélection en plaque encre, violet réservé à la marque."),
    dict(n=5, titre="Des polices choisies, pas celles par défaut (Fontshare, Fontesk)",
         quoi="La police trahit le design fait à la va-vite. Fontshare est libre pour l'usage commercial ; Fontesk, licence par police ; Fontjoy pour les paires.",
         avis="adopter", forme="memoire", prio=3,
         pourquoi="Nunito et Manrope/Source Serif sont fixés ; la question ne se pose que pour une enseigne fictive ou une pièce du portfolio. Deux leçons déjà payées s'y ajoutent : la police se loge en .woff2 local (Nunito en local), et la licence se vérifie avant.",
         geste="Une fiche de mémoire courte : Fontshare d'abord, licence vérifiée, fichier local, jamais la pile système."),
    dict(n=6, titre="Écrire comme les cinq meilleurs du créneau",
         quoi="Faire relever ce que les cinq meilleurs font dans leurs titres, boutons et premier écran, puis en tirer des règles de rédaction.",
         avis="essayer", forme="memoire", prio=2,
         pourquoi="Pas pour les modules — leur langue suit le programme. Mais pour ce qui vend : la page publique d'edufrancis, le démarchage des employeurs, les courriels aux directions. On n'a jamais regardé ce que font les meilleurs éditeurs de formation linguistique.",
         geste="Une seule passe sur la page publique, avec le résultat versé à la compétence de ton (astuce 12) plutôt qu'à une fiche à part."),
    dict(n=7, titre="Mélanger deux systèmes",
         quoi="La typographie de l'un, la couleur et le mouvement de l'autre : un mélange qui n'est la copie de personne.",
         avis="place", forme="rien", prio=0,
         pourquoi="Le banc d'essai des habillages fait déjà ce travail (francis ↔ Trame sur le classeur, un bloc de jetons par système). La technique sert surtout aux enseignes fictives, et l'astuce 2 la couvre.",
         geste="Rien à faire."),
    dict(n=9, titre="Partir d'un projet déjà fini",
         quoi="Pointer vers un projet terminé et en reprendre système, médias et décisions.",
         avis="place", forme="rien", prio=0,
         pourquoi="C'est le rôle de la mémoire, des gabarits et de page-engendree. Le guide confirme la règle qu'on applique : pointer le dossier, pas une conversation passée.",
         geste="Rien à faire."),
    dict(n=10, titre="Une bibliothèque de références visuelles",
         quoi="Une extension Chrome qui garde en un clic une capture, l'adresse et une note, et une page-mur pour les retrouver.",
         avis="essayer", forme="ressource", prio=3,
         pourquoi="Le goût se nourrit, et on relève souvent des designs externes. Mais c'est un outil de plus à entretenir, et le « système d'exploitation du design » (astuce 25) le recouvre en partie.",
         geste="Plus tard, et seulement si les relevés de sites se multiplient. À construire alors comme une page du classeur plutôt qu'une extension."),
    dict(n=11, titre="impeccable : l'audit qui enlève l'air « fait par IA »",
         quoi="Une compétence libre (1 compétence, 24 commandes) qui audite hiérarchie, espacement, typographie, accessibilité et états vides, puis corrige.",
         avis="essayer", forme="competence", prio=1,
         pourquoi="C'est le pendant visuel de boucle-didactique : la boucle audite la pédagogie, rien n'audite l'œil. Beaucoup de nos corrections (boutons à 12 px, barre alignée, cadre qui bouge) auraient pu sortir d'un audit. Risque : ses goûts par défaut peuvent contredire francis ; il faut lui dire que le système l'emporte.",
         geste="L'installer, le passer sur UNE page (le portail élève), lire ses constats sur une page de tri comme les autres audits, et ne garder que ceux qui ne contredisent pas le système."),
    dict(n=12, titre="Une compétence de ton de voix",
         quoi="Mots bannis, façon d'écrire, exemples réels, plus des règles reconnues (anglais technique simplifié, guides de Google et d'Apple). Elle apprend à chaque correction.",
         avis="adopter", forme="competence", prio=1,
         pourquoi="Nos règles de rédaction sont éparpillées dans vingt fiches de mémoire : vouvoiement, aucun émoji, québécois (courriel, 15 h), « mode avec assistance » et jamais « IA », pseudo et jamais nom, phrases courtes. Le principe « une idée par phrase, des mots simples » est exactement celui du langage clair, qui compte double pour des apprenants en francisation.",
         geste="Écrire /ton-francis : les règles rassemblées, deux registres (ce que lit l'élève, ce que lit la direction ou l'employeur), cinq vrais textes de Daniel comme modèles, et la consigne de s'enrichir à chaque correction."),
    dict(n=16, titre="Ne pas laisser Claude dessiner les icônes",
         quoi="Prendre UN jeu d'icônes dans UN style (Iconify, Flaticon) et interdire d'en dessiner.",
         avis="adopter", forme="memoire", prio=2,
         pourquoi="Les icônes de la barre d'outils viennent d'une remise de design, mais chaque pièce du portfolio en invente de nouvelles, au trait inégal. Un jeu libre (Tabler ou Lucide, licence MIT, par Iconify) donnerait une seule famille partout.",
         geste="Choisir le jeu, le loger dans assets/design-system/, et une fiche de mémoire : « jamais dessiner une icône ; si elle manque, la prendre dans le même jeu »."),
    dict(n=17, titre="Demander du SVG",
         quoi="Icônes, schémas, illustrations au trait : en SVG, pour les redimensionner, les recolorer et les animer.",
         avis="place", forme="rien", prio=0,
         pourquoi="Déjà la pratique pour les schémas et les images au trait. Les croquis restent en image, avec raison : ce sont des dessins, pas des pictogrammes.",
         geste="Rien à faire."),
    dict(n=19, titre="Le répertoire Creators Toolbox",
         quoi="Plus de 150 ressources de design réunies (composants, effets 3D, icônes, logos, maquettes).",
         avis="adopter", forme="ressource", prio=3,
         pourquoi="Un signet, pas un chantier. Utile au moment de chercher une ressource précise ; tout n'y est pas gratuit.",
         geste="Une ligne dans une fiche de références (avec Refero et Fontshare)."),
    dict(n=20, titre="Les règles d'interface d'Apple (HIG) en compétence",
         quoi="Cibles tactiles, échelle typographique, marges, contraste : les chiffres d'Apple dans une compétence /hig.",
         avis="adopter", forme="competence", prio=2,
         pourquoi="Nos seuils (17 px, 44 px, 4,5:1) sont les bons, mais le téléphone nous a coûté cher : le cadre à 100vh sous Safari, le boîtier SimDEA séparé sur mobile, le site installable. Les chiffres d'Apple pour l'iPhone combleraient ce qui manque. Plutôt qu'une compétence de plus, les verser dans /francis (astuce 4).",
         geste="Une section « Téléphone » dans /francis : zones sûres, dvh plutôt que vh, cibles, échelle — avec les leçons déjà payées."),
    dict(n=21, titre="GSAP pour le mouvement de qualité vitrine",
         quoi="La bibliothèque d'animation des grandes agences, entièrement gratuite depuis 2025, défilement et révélations compris.",
         avis="essayer", forme="memoire", prio=2,
         pourquoi="Pas pour les modules. Mais les diaporamas HTML animés, le film des planches, la formation DEA et la vitrine du portfolio se jouent au temps près, et on règle aujourd'hui chaque minutage à la main en CSS. GSAP donne une ligne de temps qu'on peut caler sur une narration.",
         geste="Un essai sur UN diaporama animé, avec respect de prefers-reduced-motion ; si l'essai tient, une ligne dans piece-apprentissage."),
    dict(n=22, titre="/design dans Claude Code",
         quoi="Une toile de planches modifiables, comme Figma, mais qui connaît l'espace de travail, les règles et la mémoire.",
         avis="essayer", forme="rien", prio=2,
         pourquoi="Encore en aperçu. Le moment de l'essayer : le prochain écran neuf du portail, là où on compare aujourd'hui des variantes 2a, 4a… par pages séparées.",
         geste="Rien à écrire ; l'essayer au prochain écran, avec /francis chargé."),
    dict(n=23, titre="/tweak : des curseurs sur la page, puis on fige",
         quoi="Un panneau de curseurs (taille, espacement, couleurs, arrondis, sections masquées) posé sur n'importe quelle page ; « Figer » réécrit les valeurs.",
         avis="adopter", forme="competence", prio=1,
         pourquoi="C'est le geste qu'on fait le plus, à coups d'aller-retour : « un peu plus d'air », « le bouton plus bas », remesurer. Des curseurs font ce réglage en une minute. Piège à tenir absolument : nos pages sont engendrées, donc « Figer » ne doit JAMAIS écrire dans le HTML (une refonte a déjà été perdue ainsi). Il exporte les valeurs, et on les reporte dans le gabarit ou la feuille source.",
         geste="Écrire /tweak : un script injecté qui lit les jetons CSS de la page (--espace, --rayon, tailles), des curseurs dessus, et un bouton qui rend un bloc de jetons à coller dans la source — reporté par Claude selon page-engendree."),
    dict(n=24, titre="Du texte dit aux animations calées",
         quoi="Transcription mot à mot (Whisper), repérage des moments qui méritent une animation, animations HTML calées sur le temps, rendues en MP4 (HyperFrames).",
         avis="essayer", forme="memoire", prio=3,
         pourquoi="On a une longueur d'avance : nos narrations sortent d'Azure, qui donne déjà le temps de chaque mot — pas besoin de Whisper. Et les captures passent déjà par Chrome sans fenêtre. Ce qui manque est le rendu direct HTML → MP4, pour les capsules et le film.",
         geste="Au prochain tournage de capsule : essayer HyperFrames avec les minutages Azure, et consigner le résultat dans le protocole des capsules."),
    dict(n=25, titre="Son propre « système d'exploitation du design »",
         quoi="Une page où chaque design fini apparaît et où chaque image générée est indexée par ce qu'elle montre, pour la retrouver et la réutiliser.",
         avis="essayer", forme="ressource", prio=3,
         pourquoi="On en a déjà les morceaux : le classeur, le tableau de bord, la page d'audit des 1 502 images, les registres de prompts. Ce qui manque, c'est la recherche par contenu. Coût réel : un passage d'un modèle de vision sur chaque image.",
         geste="Plus tard. Commencer par un seul dossier (les croquis du portfolio) et une recherche par les prompts déjà écrits, qui ne coûte rien."),
]

LIB_AVIS = {"place": "Déjà en place", "adopter": "À adopter", "essayer": "À essayer"}
LIB_FORME = {"competence": "Compétence", "memoire": "Fiche de mémoire", "ressource": "Ressource", "rien": "Rien à écrire"}
LIB_PRIO = {1: "D'abord", 2: "Ensuite", 3: "Plus tard", 0: ""}


def carte(a):
    e = html.escape
    prio = ('<span class="prio p%d">%s</span>' % (a["prio"], LIB_PRIO[a["prio"]])) if a["prio"] else ""
    return f"""<article class="c" id="a{a['n']}" data-n="{a['n']}" data-avis="{a['avis']}" data-forme="{a['forme']}" data-prio="{a['prio']}">
  <div class="tete"><span class="num">{a['n']:02d}</span><h2>{e(a['titre'])}</h2></div>
  <div class="etis"><span class="eti av-{a['avis']}">{LIB_AVIS[a['avis']]}</span><span class="eti forme">{LIB_FORME[a['forme']]}</span>{prio}</div>
  <p class="quoi">{e(a['quoi'])}</p>
  <div class="bloc"><b>Pour nos projets</b><p>{e(a['pourquoi'])}</p></div>
  <div class="bloc geste"><b>Le geste</b><p>{e(a['geste'])}</p></div>
  <div class="dec" role="group" aria-label="Votre décision sur l'astuce {a['n']}">
    <button type="button" data-v="oui">Je prends</button>
    <button type="button" data-v="tard">Plus tard</button>
    <button type="button" data-v="non">Non</button>
    <input type="text" class="note" placeholder="Une note (facultatif)" aria-label="Note sur l'astuce {a['n']}">
  </div>
</article>"""


def main():
    n = {k: sum(1 for a in ASTUCES if a["avis"] == k) for k in LIB_AVIS}
    comp = [a for a in ASTUCES if a["forme"] == "competence"]
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(GABARIT % {
        "cartes": "\n".join(carte(a) for a in ASTUCES),
        "place": n["place"], "adopter": n["adopter"], "essayer": n["essayer"], "total": len(ASTUCES),
        "ncomp": len(comp),
        "data": json.dumps([{k: a[k] for k in ("n", "titre", "avis", "forme", "prio")} for a in ASTUCES], ensure_ascii=False),
    }, encoding="utf-8")
    print("Écrit : %s (%d astuces)" % (SORTIE.relative_to(RACINE), len(ASTUCES)))


GABARIT = r"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Astuces de design</title>
<style>
@font-face{font-family:"Nunito";src:url("../../design-system/fonts/nunito-latin.woff2") format("woff2");font-weight:200 1000;font-display:swap}
:root{--paper:#F7F7F5;--card:#fff;--ink:#17181A;--ink-2:#4A4D52;--line:#E4E3DE;--accent:#0A8F5B;--accent-bg:#E7F4EE;
      --ambre:#9A5B00;--ambre-bg:#FBF1E0;--acier:#35597A;--acier-bg:#E9EFF5;--gris:#6B6E73;--gris-bg:#EFEFEC;--rouge:#B3261E}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%%}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.55 "Nunito",system-ui,-apple-system,"Segoe UI",sans-serif}
.cadre{max-width:920px;margin:0 auto;padding:32px 16px 96px}
.sur{font-weight:800;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--gris)}
h1{font-size:34px;line-height:1.15;margin:6px 0 12px;font-weight:900;letter-spacing:-.01em}
.chapeau{font-size:18px;color:var(--ink-2);max-width:62ch;margin:0 0 24px}
.bilan{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:0 0 20px}
.bilan div{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.bilan b{display:block;font-size:30px;font-weight:900;line-height:1}
.bilan span{font-size:14px;color:var(--ink-2)}
.priorite{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:12px;padding:16px 20px;margin:0 0 24px}
.priorite h2{font-size:18px;margin:0 0 8px}
.priorite ol{margin:0;padding-left:22px}
.priorite li{margin:4px 0}
.priorite a{color:var(--ink);font-weight:800}
.barre{position:sticky;top:0;z-index:5;background:var(--paper);padding:12px 0;border-bottom:1px solid var(--line);margin-bottom:16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.barre button,.dec button{font:inherit;font-size:15px;font-weight:700;min-height:44px;padding:0 16px;border:1px solid var(--line);border-radius:999px;background:var(--card);color:var(--ink);cursor:pointer}
.barre button[aria-pressed=true],.dec button[aria-pressed=true]{background:var(--ink);color:#fff;border-color:var(--ink)}
.barre .fin{margin-left:auto;display:flex;gap:8px;align-items:center}
.cpt{font-size:14px;color:var(--ink-2);font-variant-numeric:tabular-nums}
button:focus-visible,input:focus-visible,a:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.c{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px 22px;margin:0 0 14px}
.c[hidden]{display:none}
.tete{display:flex;gap:14px;align-items:baseline}
.num{font-weight:900;font-size:15px;color:var(--gris);font-variant-numeric:tabular-nums}
.c h2{font-size:21px;line-height:1.25;margin:0;font-weight:800}
.etis{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 8px}
.eti,.prio{font-size:13px;font-weight:800;padding:3px 10px;border-radius:999px;border:1px solid var(--line);color:var(--ink-2);background:var(--paper)}
.av-adopter{color:var(--accent);background:var(--accent-bg);border-color:transparent}
.av-essayer{color:var(--ambre);background:var(--ambre-bg);border-color:transparent}
.av-place{color:var(--acier);background:var(--acier-bg);border-color:transparent}
.prio.p1{color:#fff;background:var(--ink);border-color:var(--ink)}
.quoi{color:var(--ink-2);margin:6px 0 12px}
.bloc{border-left:3px solid var(--line);padding:2px 0 2px 14px;margin:10px 0}
.bloc b{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--gris)}
.bloc p{margin:2px 0 0}
.geste{border-left-color:var(--accent)}
.dec{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px;padding-top:14px;border-top:1px solid var(--line)}
.dec .note{flex:1 1 220px;min-height:44px;font:inherit;font-size:16px;padding:0 14px;border:1px solid var(--line);border-radius:10px;background:var(--paper);color:var(--ink)}
.c.fait{border-color:var(--ink)}
.source{font-size:14px;color:var(--gris);margin-top:32px}
@media (max-width:640px){h1{font-size:28px}.bilan{grid-template-columns:repeat(2,1fr)}.barre .fin{margin-left:0;width:100%%}.c{padding:16px}}
@media print{.barre,.dec{display:none}.c{break-inside:avoid}}
</style></head>
<body><div class="cadre">
<div class="sur">La maison · Identité · à trancher</div>
<h1>Les %(total)d astuces de design retenues</h1>
<p class="chapeau">Le guide « 25 tricks to level up Claude Design » passé au crible de ce qui existe déjà : francis, Trame, les compétences, la mémoire. Seules les astuces retenues restent ici, sous leur numéro d'origine. Pour chaque astuce, un avis, la forme qu'elle prendrait, et le geste. Vos décisions restent sur ce poste ; « Exporter » les rend à une prochaine session.</p>

<div class="bilan">
  <div><b>%(adopter)d</b><span>à adopter</span></div>
  <div><b>%(essayer)d</b><span>à essayer d'abord</span></div>
  <div><b>%(place)d</b><span>déjà en place</span></div>
</div>

<div class="priorite">
  <h2>Ce que je ferais d'abord</h2>
  <ol>
    <li><a href="#a12">Une compétence de ton</a> — rassembler vingt règles éparses en une seule, qui apprend de vos corrections.</li>
    <li><a href="#a23">/tweak</a> — régler l'espacement au curseur au lieu de dix allers-retours, sans jamais écrire dans le HTML engendré.</li>
    <li><a href="#a4">/francis et /trame</a> — le système appelable d'un mot, partout, avec les leçons du téléphone (<a href="#a20">astuce 20</a>).</li>
    <li><a href="#a11">impeccable</a> — un essai sur le portail élève : l'audit visuel qui manque à côté de la boucle didactique.</li>
  </ol>
</div>

<div class="barre" role="toolbar" aria-label="Filtrer">
  <button type="button" data-f="tout" aria-pressed="true">Toutes</button>
  <button type="button" data-f="adopter" aria-pressed="false">À adopter</button>
  <button type="button" data-f="essayer" aria-pressed="false">À essayer</button>
  <button type="button" data-f="place" aria-pressed="false">Déjà en place</button>
  <button type="button" data-f="competence" aria-pressed="false">Compétences (%(ncomp)d)</button>
  <span class="fin"><span class="cpt" id="cpt"></span><button type="button" id="exp">Exporter</button></span>
</div>

<main id="liste">
%(cartes)s
</main>

<p class="source">Source : « 25 tricks to level up Claude Design », RoboNuggets, liens vérifiés par l'auteur du 21 au 25 septembre 2026. Résumés et avis rédigés ici ; le guide n'est pas reproduit. Page engendrée par build/astuces_design_page.py.</p>
</div>
<script>
(function(){
  var DATA=%(data)s, CLE="astuces-design-v1", etat={};
  try{etat=JSON.parse(localStorage.getItem(CLE)||"{}")}catch(e){etat={}}
  function garder(){try{localStorage.setItem(CLE,JSON.stringify(etat))}catch(e){}}
  var cartes=[].slice.call(document.querySelectorAll(".c"));
  function compter(){
    var n=cartes.filter(function(c){var d=etat[c.dataset.n];return d&&d.v}).length;
    document.getElementById("cpt").textContent=n+" / "+cartes.length+" tranchées";
  }
  cartes.forEach(function(c){
    var n=c.dataset.n, d=etat[n]||{}, bs=[].slice.call(c.querySelectorAll(".dec button")), note=c.querySelector(".note");
    function peindre(){bs.forEach(function(b){b.setAttribute("aria-pressed",String(b.dataset.v===(etat[n]||{}).v))});
      c.classList.toggle("fait",!!(etat[n]||{}).v)}
    note.value=d.note||"";
    bs.forEach(function(b){b.addEventListener("click",function(){
      var e=etat[n]||{}; e.v=(e.v===b.dataset.v)?"":b.dataset.v; etat[n]=e; garder(); peindre(); compter();})});
    note.addEventListener("input",function(){var e=etat[n]||{}; e.note=note.value; etat[n]=e; garder();});
    peindre();
  });
  [].slice.call(document.querySelectorAll(".barre [data-f]")).forEach(function(b,_,tous){
    b.addEventListener("click",function(){
      tous.forEach(function(x){x.setAttribute("aria-pressed",String(x===b))});
      var f=b.dataset.f;
      cartes.forEach(function(c){c.hidden=!(f==="tout"||c.dataset.avis===f||c.dataset.forme===f)});
    });
  });
  document.getElementById("exp").addEventListener("click",function(){
    var out={page:"astuces-design",date:new Date().toISOString().slice(0,10),decisions:DATA.map(function(a){
      var d=etat[a.n]||{}; return {n:a.n,titre:a.titre,avis:a.avis,forme:a.forme,decision:d.v||"",note:d.note||""}})};
    var txt=JSON.stringify(out,null,2), blob=new Blob([txt],{type:"application/json"}), a=document.createElement("a");
    a.href=URL.createObjectURL(blob); a.download="astuces-design-decisions.json"; a.click();
    if(navigator.clipboard){navigator.clipboard.writeText(txt).catch(function(){})}
  });
  compter();
})();
</script>
</body></html>
"""

if __name__ == "__main__":
    main()
