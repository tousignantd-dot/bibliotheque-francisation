#!/usr/bin/env python3
"""Monte les capsules à partir des films d'écran.

Ce que ça change par rapport au montage d'images fixes : la durée de chaque
image vient de son horodatage réel, relevé pendant le tournage. Le
`screencast` de Chrome n'émet une image que lorsque la page change — un
écran immobile n'en produit aucune. Poser une cadence constante ferait donc
défiler les mouvements trop vite et escamoterait les temps d'arrêt.

Trois pièces montées bout à bout :
  carton de titre → film de la capsule → carton de fin,
plus la narration mixée en une seule piste, et un fichier de sous-titres.

`python3 monter_film.py [idCapsule]`
"""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ICI = Path(__file__).parent
FILMS, VOIX = ICI / "films", ICI / "voix"
TRAVAIL, SORTIE = ICI / "travail", ICI / "capsules"
L, H, IPS = 1920, 1080, 30
CRF = 23          # défaut ; une capsule peut le relever dans le manifeste
RESPIRATION = 0.7
TITRE_S, FIN_S = 2.6, 2.2

ENCRE = (23, 24, 26)
PAPIER = (247, 247, 245)
VERT = (10, 143, 91)
GRIS = (110, 113, 117)


def duree(f):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(f)],
        capture_output=True, text=True, check=True).stdout.strip())


def police(taille, gras=True):
    """Nunito est la police du système de design ; on retombe sur la police
    du système si elle n'est pas installée — un carton illisible vaut mieux
    qu'un montage qui s'arrête."""
    for nom in (("Nunito-Black.ttf", "Nunito-Bold.ttf") if gras
                else ("Nunito-SemiBold.ttf", "Nunito-Regular.ttf")):
        for base in (Path.home() / "Library/Fonts", Path("/Library/Fonts")):
            if (base / nom).exists():
                return ImageFont.truetype(str(base / nom), taille)
    for repli in ("/System/Library/Fonts/Helvetica.ttc",
                  "/System/Library/Fonts/Supplemental/Arial.ttf"):
        if Path(repli).exists():
            return ImageFont.truetype(repli, taille)
    return ImageFont.load_default()


def carton(chemin, surtitre, titre, pied=None, inverse=False):
    fond, encre = (ENCRE, PAPIER) if inverse else (PAPIER, ENCRE)
    img = Image.new("RGB", (L, H), fond)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, L, 10], fill=VERT)
    d.text((140, H / 2 - 150), surtitre.upper(), font=police(26), fill=VERT)
    y = H / 2 - 95
    for ligne in titre.split("\n"):
        d.text((140, y), ligne, font=police(76), fill=encre)
        y += 92
    if pied:
        d.text((140, H / 2 + 130), pied, font=police(30, gras=False),
               fill=PAPIER if inverse else GRIS)
    img.save(chemin)


def segment_fixe(image, secondes, sortie):
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-framerate", str(IPS),
        "-t", f"{secondes:.3f}", "-i", str(image),
        "-f", "lavfi", "-t", f"{secondes:.3f}", "-i", "anullsrc=r=48000:cl=stereo",
        "-vf", f"scale={L}:{H},format=yuv420p",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
        "-shortest", str(sortie),
    ], check=True)


def horodatage(s):
    h, r = divmod(s, 3600)
    m, r = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{r:06.3f}"


def monter(capsule, decalage_titre):
    dossier = FILMS / capsule["id"]
    releve = json.loads((dossier / "images.json").read_text())
    images, reperes = releve["images"], releve["reperes"]
    if not images:
        raise SystemExit(f"{capsule['id']} : aucune image filmée")

    t0 = images[0]["t"]
    fin = reperes[-1]["fin"] / 1000.0

    # Chaque image tient jusqu'à la suivante ; la dernière tient jusqu'à la
    # fin du dernier plan. C'est le relevé du tournage qui commande.
    lignes = []
    for i, im in enumerate(images):
        depart = im["t"] - t0
        suivant = (images[i + 1]["t"] - t0) if i + 1 < len(images) else (
            fin - (reperes[0]["debut"] / 1000.0 - t0) + RESPIRATION)
        d = max(1.0 / IPS, suivant - depart)
        lignes.append(f"file '{im['nom']}'\nduration {d:.4f}\n")
    lignes.append(f"file '{images[-1]['nom']}'\n")
    liste = dossier / "montage.txt"
    liste.write_text("".join(lignes))

    # Le taux de compression se règle par capsule : une capsule qui défile
    # beaucoup pèse trois fois une capsule immobile, à qualité égale. Sur du
    # texte d'interface, monter le CRF de 23 à 27 ne se voit pas et divise le
    # poids par deux. `crf` dans le manifeste l'emporte sur le défaut.
    crf = str(capsule.get("crf", CRF))
    corps = TRAVAIL / f"{capsule['id']}-corps.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", "montage.txt",
        "-vf", f"scale={L}:{H}:flags=lanczos,fps={IPS},format=yuv420p",
        "-c:v", "libx264", "-preset", "slow", "-crf", crf,
        # Surtout PAS `-tune stillimage` : réglé pour des images figées, il
        # coûte 3 Mo sur une capsule qui défile (mesuré : 11,8 contre 8,8 à
        # CRF 27) sans rien apporter à la lisibilité.
        str(corps),
    ], check=True, cwd=dossier)

    # La narration : chaque MP3 posé à l'instant où son plan a commencé.
    entrees, filtres = ["-i", str(corps)], []
    for i, repere in enumerate(reperes):
        son = VOIX / f"{capsule['id']}_{repere['plan']}.mp3"
        entrees += ["-i", str(son)]
        ms = int(repere["debut"] - reperes[0]["debut"])
        filtres.append(f"[{i + 1}:a]adelay={ms}|{ms}[a{i}]")
    melange = "".join(f"[a{i}]" for i in range(len(reperes)))
    filtres.append(f"{melange}amix=inputs={len(reperes)}:normalize=0[voix]")

    avec_voix = TRAVAIL / f"{capsule['id']}-voix.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", *entrees,
        "-filter_complex", ";".join(filtres),
        "-map", "0:v", "-map", "[voix]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
        str(avec_voix),
    ], check=True)

    titre_png, fin_png = TRAVAIL / f"{capsule['id']}-t.png", TRAVAIL / "fin.png"
    carton(titre_png, f"Espace enseignant · capsule {decalage_titre}",
           capsule["titre"], "Francisation · Niveau 4")
    carton(fin_png, "Pour aller plus loin",
           "Le guide complet\nest dans le portail",
           "Bouton « Tutoriels », barre de groupe", inverse=True)
    t_mp4, f_mp4 = TRAVAIL / f"{capsule['id']}-t.mp4", TRAVAIL / f"{capsule['id']}-f.mp4"
    segment_fixe(titre_png, TITRE_S, t_mp4)
    segment_fixe(fin_png, FIN_S, f_mp4)

    liste2 = TRAVAIL / f"{capsule['id']}-tout.txt"
    liste2.write_text("".join(f"file '{p.name}'\n" for p in (t_mp4, avec_voix, f_mp4)))
    film = SORTIE / f"{capsule['id']}.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
        "-i", str(liste2.name), "-c", "copy", str(film),
    ], check=True, cwd=TRAVAIL)

    # Sous-titres : une réplique par plan, décalée du carton de titre.
    # Public en apprentissage du français — lire pendant qu'on écoute aide.
    vtt = ["WEBVTT", ""]
    for repere, plan in zip(reperes, capsule["plans"]):
        d = (repere["debut"] - reperes[0]["debut"]) / 1000.0 + TITRE_S
        f = (repere["fin"] - reperes[0]["debut"]) / 1000.0 + TITRE_S
        vtt += [f"{horodatage(d)} --> {horodatage(f)}", plan["texte"], ""]
    (SORTIE / f"{capsule['id']}.vtt").write_text("\n".join(vtt))

    return film


def main():
    seule = sys.argv[1] if len(sys.argv) > 1 else None
    TRAVAIL.mkdir(exist_ok=True)
    SORTIE.mkdir(exist_ok=True)
    manifeste = json.loads((ICI / "manifeste.json").read_text())
    for n, capsule in enumerate(manifeste["capsules"], 1):
        if seule and capsule["id"] != seule:
            continue
        film = monter(capsule, n)
        print(f"✓ {film.name} — {duree(film):.0f} s, {film.stat().st_size / 1e6:.1f} Mo")


if __name__ == "__main__":
    main()
