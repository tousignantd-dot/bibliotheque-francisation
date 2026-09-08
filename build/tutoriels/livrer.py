#!/usr/bin/env python3
"""Livre les capsules dans le dépôt et écrit la page de visionnement.

La page est **produite depuis le manifeste**, jamais écrite à la main : la
transcription sous chaque vidéo est le texte même qu'a dit la voix. Recopier
ces paragraphes les ferait diverger à la première retouche du scénario.
"""
import json
import shutil
import subprocess
from html import escape
from pathlib import Path

ICI = Path(__file__).parent
DEPOT = ICI.parent.parent
VIDEOS = DEPOT / "assets" / "tutoriels"
PAGE = DEPOT / "assets" / "outils" / "tutoriels-enseignant.html"


def duree(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nw=1:nk=1", str(f)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def mmss(s):
    return f"{int(s) // 60} min {int(s) % 60:02d} s" if s >= 60 else f"{int(s)} s"


manifeste = json.loads((ICI / "manifeste.json").read_text())
VIDEOS.mkdir(parents=True, exist_ok=True)

# Le nombre de capsules s'écrit en toutes lettres dans le chapô, et il se
# compte : « Six capsules » est resté au-dessus de dix pendant une livraison.
MOTS = ("zéro une deux trois quatre cinq six sept huit neuf dix onze douze "
        "treize quatorze quinze seize").split()


def combien(n):
    return MOTS[n].capitalize() if n < len(MOTS) else str(n)


cartes, sommaire = [], []
# Les chapitres nés sur le papier n'ont pas encore de film : la page de
# visionnement ne les annonce donc pas. Les y mettre promettrait une vidéo qui
# n'existe pas — et `livrer.py` mourait sur leur `.mp4` introuvable.
filmees = [c for c in manifeste["capsules"] if not c.get("papier_seulement")]

for i, capsule in enumerate(filmees, 1):
    source = ICI / "capsules" / f"{capsule['id']}.mp4"
    shutil.copy2(source, VIDEOS / source.name)

    # Les sous-titres accompagnent le film : public en apprentissage du
    # français, lire pendant qu'on écoute change tout. Fichier à part plutôt
    # qu'incrusté — on peut les couper, et les corriger sans réencoder.
    sous_titres = ICI / "capsules" / f"{capsule['id']}.vtt"
    if sous_titres.exists():
        shutil.copy2(sous_titres, VIDEOS / sous_titres.name)

    # Vignette d'affiche : prise après le carton de titre, sinon les six
    # cartes de la page montreraient six cartons presque identiques.
    affiche = VIDEOS / f"{capsule['id']}.jpg"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "4.5",
                    "-i", str(source), "-frames:v", "1", "-vf", "scale=640:-2",
                    "-q:v", "4", str(affiche)], check=True)

    d = mmss(duree(source))
    titre = escape(capsule["titre"])
    sommaire.append(f'<li><a href="#c{i}"><span>{i}</span>{titre}<em>{d}</em></a></li>')

    transcription = "".join(
        f"<p>{escape(p['texte'])}</p>" for p in capsule["plans"])
    # La vignette remplace le lecteur pleine largeur. Onze lecteurs empilés
    # font une page qu'on ne parcourt plus : on ne voit que des rectangles
    # noirs, tous de la même taille, et il faut défiler pour lire un titre.
    # Le bouton devient le lecteur au clic — la piste de sous-titres est donc
    # gardée, ce qu'un simple lien vers le fichier aurait perdu.
    cartes.append(f"""
    <section class="tu-capsule" id="c{i}">
      <div class="tu-rangee">
        <button class="tu-vignette" type="button"
                data-video="../tutoriels/{capsule['id']}.mp4"
                data-vtt="../tutoriels/{capsule['id']}.vtt"
                aria-label="Lire la capsule {i} : {titre}">
          <img src="../tutoriels/{capsule['id']}.jpg" alt="" loading="lazy" />
          <span class="tu-play" aria-hidden="true"></span>
          <span class="tu-duree">{d}</span>
        </button>
        <div class="tu-infos">
          <div class="tu-num">Capsule {i} sur {len(filmees)}</div>
          <h2>{titre}</h2>
          <details class="tu-texte">
            <summary>Lire la transcription</summary>
            {transcription}
          </details>
          <p class="tu-fichier"><a href="../tutoriels/{capsule['id']}.mp4">
            Ouvrir la vidéo dans un onglet</a></p>
        </div>
      </div>
    </section>""")

# ── Le tutoriel papier ────────────────────────────────────────────────────
#
# Il passe AVANT les films, et c'est un choix : quand on découvre le portail,
# on veut un document qu'on feuillette, qu'on annote et qu'on garde à côté du
# clavier. Une vidéo se regarde une fois ; celui-ci se pose ouvert à la page
# qu'on est en train de faire.
#
# Il vit dans `assets/outils/`, comme cette page — et non dans
# `assets/presentations/`, qui est derrière le verrou du classeur : le lien y
# demandait un identifiant que l'enseignante n'a pas.
PAPIER = DEPOT / "assets" / "outils" / "tutoriel-espace-enseignant.pdf"
papier = ""
if PAPIER.exists():
    mo = PAPIER.stat().st_size / (1024 * 1024)
    papier = f"""
      <section class="tu-capsule tu-papier" id="papier">
        <div class="tu-num">Le document · à imprimer ou à garder ouvert</div>
        <h2>Le tutoriel de l'espace enseignant</h2>
        <p class="tu-chapeau">Tout ce que disent les capsules, en un seul document :
           un chapitre par sujet, une étape par geste, et les copies d'écran du
           portail. C'est par là qu'on commence.</p>
        <div class="tu-boutons">
          <a class="btn btn--primary" href="tutoriel-espace-enseignant.pdf"
             target="_blank" rel="noopener">Ouvrir le PDF ({mo:.0f} Mo)</a>
          <a class="btn btn--ghost" href="tutoriel-espace-enseignant.html"
             target="_blank" rel="noopener">Le lire dans le navigateur</a>
        </div>
      </section>"""
else:
    print("[!] tutoriel-espace-enseignant.pdf absent — bloc papier omis")


# ── Le film de présentation ───────────────────────────────────────────────
# Ce n'est pas une capsule : les capsules apprennent à se servir du portail,
# celui-ci présente le produit. Il a donc son bloc, au-dessus du sommaire, et
# il ne compte pas dans « N capsules » — sans quoi la page annoncerait une
# leçon de plus qu'elle n'en donne.
#
# Il n'est pas filmé par la chaîne (`enregistrer.js`) et ne vit donc pas dans
# `capsules/` : il est livré directement dans `assets/tutoriels/`. `livrer.py`
# ne le copie pas, il vérifie qu'il est là — un bloc qui promet une vidéo
# absente est pire que pas de bloc.
presentation = ""
pres = manifeste.get("presentation")
if pres:
    film = VIDEOS / f"{pres['id']}.mp4"
    if not film.exists():
        print(f"[!] {film.name} est déclaré au manifeste mais absent — bloc omis")
    else:
        affiche_p = VIDEOS / f"{pres['id']}.jpg"
        if not affiche_p.exists():
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "20",
                            "-i", str(film), "-frames:v", "1",
                            "-vf", "scale=640:-2", "-q:v", "4", str(affiche_p)],
                           check=True)
        # La page existe parce que ce public lit en apprenant : taire l'absence
        # de sous-titres serait le seul endroit du dépôt où on la cacherait.
        note = ("<p class=\"tu-sansst\">Ce film n'a pas de sous-titres, "
                "contrairement aux capsules.</p>" if pres.get("sans_sous_titres") else "")
        presentation = f"""
      <section class="tu-capsule tu-presentation" id="film">
        <div class="tu-rangee">
          <button class="tu-vignette" type="button"
                  data-video="../tutoriels/{pres['id']}.mp4"
                  aria-label="Lire le film de présentation">
            <img src="../tutoriels/{pres['id']}.jpg" alt="" loading="lazy" />
            <span class="tu-play" aria-hidden="true"></span>
            <span class="tu-duree">{mmss(duree(film))}</span>
          </button>
          <div class="tu-infos">
            <div class="tu-num">Film de présentation</div>
            <h2>{escape(pres['titre'])}</h2>
            <p class="tu-chapeau">{escape(pres.get('chapeau', ''))}</p>
            {note}
            <p class="tu-fichier"><a href="../tutoriels/{pres['id']}.mp4">
              Ouvrir la vidéo dans un onglet</a></p>
          </div>
        </div>
      </section>"""

combien = combien(len(filmees))
PAGE.write_text(f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Tutoriels — Espace enseignant</title>
<!-- Le système de design versionné, pas ds-bundle/ (ignoré par git). -->
<link rel="stylesheet" href="../design-system/styles.css" />
<style>
  /* Page de visionnement des capsules. Aucune couleur en dur : uniquement
     des jetons du système. Les seules pièces écrites ici sont le sommaire
     numéroté et le cadre de lecture, qui n'existent pas dans le système. */
  .tu-pile {{ padding: var(--sp-8) 0 var(--sp-12); display: grid; gap: var(--sp-12); }}
  .tu-sommaire {{ margin: 0; padding: 0; list-style: none; display: grid; gap: var(--sp-2); }}
  .tu-sommaire a {{
    display: flex; align-items: center; gap: var(--sp-4); min-height: var(--tap-comfort);
    padding: var(--sp-3) var(--sp-4); text-decoration: none;
    background: var(--surface-card); border: 1px solid var(--border); border-radius: var(--r-sm);
    font-size: var(--fs-body-sm); font-weight: var(--fw-bold); color: var(--text-strong);
  }}
  .tu-sommaire a:hover {{ background: var(--accent-soft); }}
  .tu-sommaire span {{
    flex: none; display: inline-flex; align-items: center; justify-content: center;
    width: 30px; height: 30px; border-radius: var(--r-md);
    background: var(--accent-soft); color: var(--accent-ink); font-weight: var(--fw-black);
  }}
  .tu-sommaire em {{ margin-left: auto; font-style: normal; font-size: var(--fs-ui-sm); color: var(--text-muted); }}
  .tu-capsule {{ display: grid; gap: var(--sp-4); scroll-margin-top: var(--sp-6); }}
  .tu-num {{
    font-size: var(--fs-label); font-weight: var(--fw-bold);
    letter-spacing: var(--ls-label); text-transform: uppercase; color: var(--text-accent);
  }}
  .tu-capsule h2 {{ font-size: var(--fs-h3); }}
  .tu-capsule video {{
    width: 100%; aspect-ratio: 16 / 9; display: block;
    background: var(--ink-900); border-radius: var(--r-lg); box-shadow: var(--sh-raise);
  }}
  /* ── La vignette ──────────────────────────────────────────────────────
     Onze lecteurs pleine largeur faisaient une page qu'on ne parcourait
     plus : rien que des rectangles noirs de la même taille, un titre par
     écran. La vignette rend la liste lisible d'un coup d'œil, et le clic
     rend le lecteur — avec ses sous-titres, qu'un lien vers le fichier
     aurait perdus. */
  .tu-rangee {{ display: grid; grid-template-columns: 300px 1fr;
    gap: var(--sp-5); align-items: start; }}
  .tu-vignette {{
    position: relative; padding: 0; border: 0; background: var(--ink-900);
    border-radius: var(--r-lg); overflow: hidden; cursor: pointer; display: block;
    width: 100%; aspect-ratio: 16 / 9; box-shadow: var(--sh-card);
  }}
  .tu-vignette img {{ width: 100%; height: 100%; object-fit: cover; display: block;
    transition: transform .18s ease, opacity .18s ease; }}
  .tu-vignette:hover img, .tu-vignette:focus-visible img {{
    transform: scale(1.03); opacity: .88; }}
  .tu-vignette:focus-visible {{ outline: 3px solid var(--text-accent);
    outline-offset: 3px; }}
  /* Le triangle est dessiné en CSS : aucune image, aucun émoji. */
  .tu-play {{
    position: absolute; inset: 0; margin: auto; width: 54px; height: 54px;
    border-radius: 50%; background: rgba(255,255,255,.92);
    box-shadow: 0 2px 10px rgba(0,0,0,.28);
  }}
  .tu-play::after {{
    content: ""; position: absolute; inset: 0; margin: auto;
    width: 0; height: 0; margin-left: 22px;
    border-left: 17px solid var(--ink-900);
    border-top: 10px solid transparent; border-bottom: 10px solid transparent;
  }}
  .tu-duree {{
    position: absolute; right: 8px; bottom: 8px;
    background: rgba(23,24,26,.82); color: #fff; border-radius: var(--r-sm);
    padding: 2px 7px; font-size: var(--fs-ui-sm); font-weight: var(--fw-bold);
    font-variant-numeric: tabular-nums;
  }}
  .tu-infos {{ display: grid; gap: var(--sp-3); }}
  .tu-fichier {{ margin: 0; font-size: var(--fs-ui-sm); }}
  .tu-fichier a {{ color: var(--text-muted); font-weight: var(--fw-medium); }}
  /* Une fois lancée, la capsule reprend toute la largeur : à 300 px, on ne
     lit pas ce qui se passe dans le portail, et c'est tout ce que la capsule
     montre. La vignette sert à choisir, le lecteur à regarder. */
  .tu-capsule.joue .tu-rangee {{ grid-template-columns: 1fr; }}
  @media (max-width: 720px) {{
    .tu-rangee {{ grid-template-columns: 1fr; }}
  }}
  .tu-texte summary {{
    cursor: pointer; min-height: var(--tap-min); display: flex; align-items: center;
    font-size: var(--fs-ui); font-weight: var(--fw-bold); color: var(--text-accent);
  }}
  .tu-texte p {{
    margin-top: var(--sp-3); font-size: var(--fs-body-sm);
    font-weight: var(--fw-medium); color: var(--ink-500); max-width: 72ch;
  }}
  .tu-autre {{
    background: var(--surface-band); border-radius: var(--r-lg); padding: var(--sp-6);
    font-size: var(--fs-body-sm); font-weight: var(--fw-medium); color: var(--ink-500);
  }}
  .tu-autre b {{ color: var(--text-strong); }}
  /* Retour vers l'espace enseignant : la pilule fantôme du système, juste
     décollée du surtitre. */
  .tu-presentation {{ padding: var(--sp-5); border-radius: var(--r-lg);
    background: var(--acier-100); }}
  /* Le document papier, en tête : c'est par lui qu'on commence quand on
     découvre le portail, et une vidéo ne se feuillette pas. Encadré plutôt
     que teinté — il n'est pas de la même nature que les films. */
  .tu-papier {{ padding: var(--sp-5); border-radius: var(--r-lg);
    border: 2px solid var(--line-300); background: var(--surface-card); }}
  .tu-papier .tu-boutons {{ display: flex; flex-wrap: wrap; gap: var(--sp-3);
    margin-top: var(--sp-4); }}
  .tu-chapeau {{ margin: 0; color: var(--ink-500); font-size: var(--fs-body-sm); }}
  .tu-sansst {{ margin: 0; color: var(--ink-500); font-size: var(--fs-ui-sm); }}
  .tu-retour {{ margin: 0 0 var(--sp-4); }}
</style>
</head>
<body>
<div class="page">
  <header class="band">
    <div class="container">
      <a class="btn btn--ghost btn--sm tu-retour" href="../../enseignant.html"><span aria-hidden="true">←</span> Retour à l’espace enseignant</a>
      <div class="band__eyebrow">Espace enseignant · Francisation Niveau 4</div>
      <h1 style="margin:var(--sp-3) 0 0;font-size:var(--fs-h2);font-weight:var(--fw-black)">Tutoriels</h1>
      <p class="band__lead">Le tutoriel en document, d'abord — c'est le plus complet, et
         il s'imprime. Puis {combien.lower()} capsules courtes, filmées dans le portail, avec
         narration et sous-titres : regardez celle dont vous avez besoin, elles ne se
         suivent pas obligatoirement.</p>
    </div>
  </header>
  <div class="container">
    <div class="tu-pile">
      {papier}
      {presentation}
      <ul class="tu-sommaire">{''.join(sommaire)}</ul>
      {''.join(cartes)}
      <div class="tu-autre">
        <b>Vous préférez lire ?</b> Le même contenu existe en diapositives, à parcourir
        au clavier ou à imprimer : <a href="guide-espace-enseignant.html">Guide de l'espace enseignant</a>.
      </div>
    </div>
  </div>
</div>
<script>
/* Retour à l'espace enseignant. Le portail ouvre cette page dans un onglet à
   part, avec ?de=enseignant : revenir veut alors dire fermer cet onglet, celui
   d'origine étant resté ouvert avec la planification en cours. Si le
   navigateur refuse la fermeture (page ouverte à la main, signet), on retombe
   sur la navigation normale du lien. */
(() => {{
  const lien = document.querySelector(".tu-retour");
  if (!lien) return;
  if (new URLSearchParams(location.search).get("de") !== "enseignant") return;
  // Le guide est l'autre forme du même contenu : on lui reporte le paramètre
  // pour que son propre bouton retour ferme l'onglet lui aussi.
  const guide = document.querySelector('a[href="guide-espace-enseignant.html"]');
  if (guide) guide.href = "guide-espace-enseignant.html?de=enseignant";
  lien.innerHTML = '<span aria-hidden="true">\u2190</span> Fermer et revenir \u00e0 l\u2019espace enseignant';
  lien.addEventListener("click", (e) => {{
    e.preventDefault();
    const cible = lien.href;
    window.close();
    // window.close() est silencieux quand il est refusé : on vérifie après coup.
    setTimeout(() => {{ if (!window.closed) location.href = cible; }}, 200);
  }});
}})();

/* La vignette devient le lecteur, à sa place. On construit le <video> au
   clic plutôt que de le poser masqué : onze lecteurs dans le document, même
   invisibles, c'est onze fois la plomberie du navigateur pour une page qu'on
   ouvre le plus souvent pour lire une transcription. Un seul joue à la fois —
   deux narrations en même temps ne s'écoutent pas. */
(() => {{
  let enCours = null;
  document.addEventListener("click", (e) => {{
    const b = e.target.closest(".tu-vignette");
    if (!b) return;
    if (enCours && enCours.pause) enCours.pause();
    const v = document.createElement("video");
    v.controls = true; v.autoplay = true; v.playsInline = true;
    v.setAttribute("poster", b.querySelector("img").getAttribute("src"));
    const src = document.createElement("source");
    src.src = b.dataset.video; src.type = "video/mp4";
    v.appendChild(src);
    if (b.dataset.vtt) {{
      const t = document.createElement("track");
      t.kind = "subtitles"; t.srclang = "fr"; t.label = "Fran\u00e7ais";
      t.default = true; t.src = b.dataset.vtt;
      v.crossOrigin = "anonymous";
      v.appendChild(t);
    }}
    const carte = b.closest(".tu-capsule");
    b.replaceWith(v);
    if (carte) carte.classList.add("joue");
    enCours = v;
    v.focus({{ preventScroll: true }});
  }});
}})();
</script>
</body>
</html>
""")

poids = sum(f.stat().st_size for f in VIDEOS.iterdir()) / 1e6
print(f"{len(filmees)} capsules livrées dans assets/tutoriels/ ({poids:.1f} Mo)")
print(f"page : {PAGE.relative_to(DEPOT)}")
