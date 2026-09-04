#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le montage du film de 90 secondes.

    python3 build/film_90_montage.py

Quatorze images fixes, une voix off par plan, des fondus enchaînés, et un
mouvement de caméra lent sur chaque plan (`zoompan`), alternativement en
avancée et en recul pour que la suite ne se lise pas comme un diaporama.

LE PIÈGE DU FONDU, ET IL A DÉJÀ COÛTÉ UN MONTAGE
`xfade` rend une sortie **plus courte que la somme de ses entrées, de la durée
du fondu**. Deux conséquences, et les manquer fait dériver la voix off par
rapport à l'image — ce qui ne se voit qu'à la fin du film :

  · chaque segment est allongé du fondu (`d_i + FONDU`), sauf le dernier, qui
    n'a plus rien à recouvrir ;
  · le décalage de chaque fondu vaut la **somme des durées voulues** des plans
    précédents, jamais celle des fichiers réels.

Le son, lui, est monté à part et par bout à bout exact : chaque réplique est
retardée d'un souffle, puis complétée de silence jusqu'à la durée exacte de son
plan. La somme fait donc 90 s au centième, quoi qu'il arrive à l'image.
"""

import pathlib
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "film-90-secondes"
FILM = SORTIE / "film-90-secondes.mp4"

FONDU = 0.5
LARGEUR, HAUTEUR, IPS = 1920, 1080, 25
SOUFFLE = 0.35        # le silence avant chaque réplique : on n'attaque pas sur la coupe

# (numéro, durée en secondes)
PLANS = [("01", 5), ("02", 7), ("03", 6), ("04", 6), ("05", 5), ("06", 5),
         ("07", 8), ("08", 6), ("09", 7), ("10", 4), ("11", 6), ("12", 6),
         ("13", 13), ("14", 6)]


def image(num):
    for ext in (".jpg", ".png"):
        p = SORTIE / ("plan-%s%s" % (num, ext))
        if p.exists():
            return p
    raise SystemExit("image manquante pour le plan %s" % num)


def monter():
    n = len(PLANS)
    total = sum(d for _, d in PLANS)
    entrees, filtres, chaine = [], [], []

    for i, (num, duree) in enumerate(PLANS):
        # Toutes les entrées sont allongées du fondu, sauf la dernière.
        longueur = duree + (FONDU if i < n - 1 else 0)
        entrees += ["-loop", "1", "-t", "%.3f" % longueur, "-i", str(image(num))]
        images = int(round(longueur * IPS))
        # Un mouvement lent, alterné : on avance sur les plans pairs, on recule
        # sur les impairs. Un même sens partout donne un diaporama.
        if i % 2 == 0:
            z = "min(zoom+0.00035,1.10)"
        else:
            z = "if(eq(on,1),1.10,max(zoom-0.00035,1.0))"
        filtres.append(
            "[%d:v]scale=3840:2160:force_original_aspect_ratio=increase,"
            "crop=3840:2160,zoompan=z='%s':x='iw/2-(iw/zoom/2)':"
            "y='ih/2-(ih/zoom/2)':d=%d:s=%dx%d:fps=%d,setsar=1[v%d]"
            % (i, z, images, LARGEUR, HAUTEUR, IPS, i))

    # La chaîne de fondus. Le décalage est la somme des durées VOULUES.
    cumul, precedent = 0.0, "v0"
    for i in range(1, n):
        cumul += PLANS[i - 1][1]
        sortie = "x%d" % i
        chaine.append("[%s][v%d]xfade=transition=fade:duration=%.3f:offset=%.3f[%s]"
                      % (precedent, i, FONDU, cumul, sortie))
        precedent = sortie
    filtres += chaine

    # Le son : une réplique par plan, décalée du souffle, complétée de silence.
    for i, (num, duree) in enumerate(PLANS):
        entrees += ["-i", str(SORTIE / ("vo-%s.mp3" % num))]
        filtres.append(
            "[%d:a]adelay=%d|%d,apad=whole_dur=%.3f,aformat=sample_fmts=fltp:"
            "sample_rates=48000:channel_layouts=stereo[a%d]"
            % (n + i, int(SOUFFLE * 1000), int(SOUFFLE * 1000), duree, i))
    filtres.append("%sconcat=n=%d:v=0:a=1[son]"
                   % ("".join("[a%d]" % i for i in range(n)), n))

    graphe = ";".join(filtres)
    (SORTIE / "_montage.txt").write_text(graphe, encoding="utf-8")
    cmd = (["ffmpeg", "-y"] + entrees +
           ["-filter_complex_script", str(SORTIE / "_montage.txt"),
            "-map", "[%s]" % precedent, "-map", "[son]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "19",
            "-pix_fmt", "yuv420p", "-r", str(IPS),
            "-c:a", "aac", "-b:a", "192k",
            "-t", "%.3f" % total, str(FILM)])
    print("Montage de %d plans, %d s attendues…" % (n, total))
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2500:])
        return 1
    (SORTIE / "_montage.txt").unlink(missing_ok=True)

    duree = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(FILM)], capture_output=True, text=True).stdout.strip()
    print("→ %s · %.2f Mo · %s s (attendu %d)"
          % (FILM.relative_to(RACINE), FILM.stat().st_size / 1e6, duree, total))
    return 0


if __name__ == "__main__":
    sys.exit(monter())
