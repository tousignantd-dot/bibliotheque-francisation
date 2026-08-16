#!/usr/bin/env python3
"""Monte une capsule MP4 par section du manifeste.

Trois partis pris.

1. **La durée d'un plan est celle de sa narration**, mesurée à l'`ffprobe`,
   plus une demi-seconde de respiration. Fixer des durées à la main les
   ferait dériver au premier mot changé dans le texte.
2. **Les images sont normalisées avant le montage**, pas pendant : un plan
   cadré (zoom) n'a pas les mêmes dimensions qu'un plein écran, et
   `concat` refuse des flux de tailles différentes. Pillow les ramène toutes
   à 1920 × 1080, sur le fond de page du système de design.
3. **Un fondu d'un quart de seconde entre les plans**, jamais plus : au delà
   on ne lit plus le texte de l'écran, qui est le sujet du film.
"""
import json
import subprocess
import shutil
import sys
from pathlib import Path

from PIL import Image

ICI = Path(__file__).parent
PLANS, VOIX = ICI / "plans", ICI / "voix"
TRAVAIL, SORTIE = ICI / "travail", ICI / "capsules"
L, H = 1920, 1080
FOND = (247, 247, 245)          # --paper-100
RESPIRATION = 0.55
FONDU = 0.25


def duree(fichier):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(fichier)],
        capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def normaliser(source, destination):
    """Ramène une capture à 1920 × 1080 sans la déformer ni la rogner."""
    img = Image.open(source).convert("RGB")
    img.thumbnail((L, H), Image.LANCZOS)
    toile = Image.new("RGB", (L, H), FOND)
    toile.paste(img, ((L - img.width) // 2, (H - img.height) // 2))
    toile.save(destination, "PNG")


def main():
    # `python3 monter.py [idCapsule]` — remonter une seule capsule. Les
    # autres MP4 restent en place : les refaire tous pour un plan changé
    # coûte plusieurs minutes d'encodage pour rien.
    seule = sys.argv[1] if len(sys.argv) > 1 else None
    if seule:
        TRAVAIL.mkdir(parents=True, exist_ok=True)
        SORTIE.mkdir(parents=True, exist_ok=True)
    else:
        for d in (TRAVAIL, SORTIE):
            shutil.rmtree(d, ignore_errors=True)
            d.mkdir(parents=True)
    manifeste = json.loads((ICI / "manifeste.json").read_text())

    for capsule in manifeste["capsules"]:
        if seule and capsule["id"] != seule:
            continue
        bouts = []
        for plan in capsule["plans"]:
            base = f"{capsule['id']}_{plan['id']}"
            image, son = PLANS / f"{base}.png", VOIX / f"{base}.mp3"
            if not image.exists() or not son.exists():
                raise SystemExit(f"manque {base} : capture ou narration absente")

            cadre = TRAVAIL / f"{base}.png"
            normaliser(image, cadre)
            secondes = duree(son) + RESPIRATION
            bout = TRAVAIL / f"{base}.mp4"

            # `-loop 1` fige l'image ; `-shortest` n'est pas utilisable ici,
            # la respiration finale doit survivre à la fin de la narration.
            subprocess.run([
                "ffmpeg", "-y", "-loglevel", "error",
                "-loop", "1", "-framerate", "30", "-t", f"{secondes:.3f}", "-i", str(cadre),
                "-i", str(son),
                "-filter_complex",
                f"[0:v]fade=t=in:st=0:d={FONDU},"
                f"fade=t=out:st={secondes - FONDU:.3f}:d={FONDU},format=yuv420p[v];"
                f"[1:a]apad=pad_dur={RESPIRATION}[a]",
                "-map", "[v]", "-map", "[a]",
                "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
                "-t", f"{secondes:.3f}", str(bout),
            ], check=True)
            bouts.append(bout)

        liste = TRAVAIL / f"{capsule['id']}.txt"
        liste.write_text("".join(f"file '{b.name}'\n" for b in bouts))
        film = SORTIE / f"{capsule['id']}.mp4"
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error",
            "-f", "concat", "-safe", "0", "-i", str(liste),
            "-c", "copy", str(film),
        ], check=True, cwd=TRAVAIL)
        print(f"✓ {film.name}  —  {duree(film):.0f} s")

    total = sum(duree(f) for f in SORTIE.glob("*.mp4"))
    print(f"{len(list(SORTIE.glob('*.mp4')))} capsules, {total / 60:.1f} min en tout")


if __name__ == "__main__":
    main()
