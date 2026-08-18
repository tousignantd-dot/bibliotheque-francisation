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

cartes, sommaire = [], []
for i, capsule in enumerate(manifeste["capsules"], 1):
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
    cartes.append(f"""
    <section class="tu-capsule" id="c{i}">
      <div class="tu-num">Capsule {i} sur {len(manifeste['capsules'])} · {d}</div>
      <h2>{titre}</h2>
      <video controls preload="none" playsinline crossorigin="anonymous"
             poster="../tutoriels/{capsule['id']}.jpg">
        <source src="../tutoriels/{capsule['id']}.mp4" type="video/mp4" />
        <track kind="subtitles" srclang="fr" label="Français" default
               src="../tutoriels/{capsule['id']}.vtt" />
        Votre navigateur ne peut pas lire cette vidéo.
        <a href="../tutoriels/{capsule['id']}.mp4">Téléchargez-la</a>.
      </video>
      <details class="tu-texte">
        <summary>Lire la transcription</summary>
        {transcription}
      </details>
    </section>""")

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
  .tu-retour {{ margin: 0 0 var(--sp-4); }}
</style>
</head>
<body>
<div class="page">
  <header class="band">
    <div class="container">
      <a class="btn btn--ghost btn--sm tu-retour" href="../../enseignant.html"><span aria-hidden="true">←</span> Retour à l’espace enseignant</a>
      <div class="band__eyebrow">Espace enseignant · Francisation Niveau 4</div>
      <h1 style="margin:var(--sp-3) 0 0;font-size:var(--fs-h2);font-weight:var(--fw-black)">Tutoriels en vidéo</h1>
      <p class="band__lead">Six capsules courtes, filmées dans le portail, avec narration
         et sous-titres. Regardez celle dont vous avez besoin — elles ne se suivent
         pas obligatoirement.</p>
    </div>
  </header>
  <div class="container">
    <div class="tu-pile">
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
</script>
</body>
</html>
""")

poids = sum(f.stat().st_size for f in VIDEOS.iterdir()) / 1e6
print(f"{len(manifeste['capsules'])} capsules livrées dans assets/tutoriels/ ({poids:.1f} Mo)")
print(f"page : {PAGE.relative_to(DEPOT)}")
