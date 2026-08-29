#!/usr/bin/env python3
"""Les versions lentes des MP3, ralenties d'avance plutôt qu'à la lecture.

    python3 build/audio_lent.py                  # tout ce qui manque
    python3 build/audio_lent.py --module module-probleme
    python3 build/audio_lent.py --hors-sons      # dialogues seulement
    python3 build/audio_lent.py --etat           # ce qui existe, sans rien produire

Le bouton 🐢 de `build/greffe_vitesse.py` demandait au navigateur d'étirer le
son *pendant* la lecture (`playbackRate` + `preservesPitch`). Pour garder la
voix à sa hauteur, Chrome recolle des morceaux d'onde en temps réel, avec un
budget de calcul minuscule : à 0,8 ça s'entend, à 0,65 la voix devient
métallique et tremblée. C'est l'algorithme temps réel du navigateur, pas les
fichiers.

`atempo` de ffmpeg fait le même travail hors ligne, avec tout le temps qu'il
faut — c'est déjà lui qui pose la voix enseignante à 0,85 dans `voix_lente.py`.
Ce module produit donc, à côté de chaque original, un `<nom>.lent.mp3` et un
`<nom>.tres-lent.mp3` ; le bouton n'a plus qu'à changer d'URL.

En production, personne n'a besoin de lancer ce script : `server.py` fabrique
la variante à la première demande et la garde sur le volume
(`AUDIO_LENT_DIR`). Les produire toutes d'avance ferait 3 Go d'image et une
demi-heure de build à chaque déploiement, pour un fonds dont les élèves
n'écoutent au ralenti qu'une petite part. Ce script sert à préchauffer un
module en local, ou à écouter le résultat avant de le mettre en ligne.

Les fichiers produits ne sont **jamais versionnés** (voir `.gitignore`) : ils
se régénèrent. Le débit d'encodage est descendu à 96 kb/s — les originaux sont
à 160 kb/s en mono 24 kHz, ce qui est très large pour de la parole, et les
extraits lents durent jusqu'à une fois et demie plus longtemps.
"""

import argparse
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
INTERACTIF = BASE / "assets" / "interactive"

# Les crans du bouton, et le suffixe de fichier qui va avec. `greffe_vitesse.py`
# porte les mêmes valeurs côté navigateur : les changer ici oblige à les
# changer là-bas, sinon le bouton demande des fichiers qui n'existent pas.
CRANS = [("lent", 0.80), ("tres-lent", 0.65)]

SUFFIXES = tuple(".%s.mp3" % nom for nom, _ in CRANS)


def est_original(p: Path) -> bool:
    """Un original, c'est-à-dire ni un `.lent.mp3` ni un `.tres-lent.mp3`."""
    return p.suffix == ".mp3" and not p.name.endswith(SUFFIXES)


def variante(src: Path, cran: str) -> Path:
    return src.with_name(src.name[:-4] + "." + cran + ".mp3")


def a_produire(src: Path):
    """Les variantes manquantes ou plus vieilles que leur original."""
    manque = []
    for cran, tempo in CRANS:
        dst = variante(src, cran)
        if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
            manque.append((dst, tempo))
    return manque


def produire(src: Path, dst: Path, tempo: float) -> bool:
    """Écrit `dst` de façon atomique : un fichier à moitié écrit serait servi."""
    # `-f mp3` est obligatoire : sans lui, ffmpeg devine le format d'après
    # l'extension du fichier provisoire et cale sur un `.part-1234`.
    part = dst.with_name(dst.name + ".part-%d" % os.getpid())
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
           "-filter:a", "atempo=%s" % tempo,
           "-ac", "1", "-ar", "24000", "-b:a", "96k",
           "-f", "mp3", str(part)]
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        part.replace(dst)
        return True
    except Exception as e:
        part.unlink(missing_ok=True)
        print("   !! %s : %s" % (src.name, e), file=sys.stderr)
        return False


def originaux(module=None, hors_sons=False):
    racine = INTERACTIF / module if module else INTERACTIF
    if not racine.is_dir():
        sys.exit("!! introuvable : %s" % racine)
    for p in sorted(racine.rglob("*.mp3")):
        if not est_original(p):
            continue
        if hors_sons and p.parent.name == "sons":
            continue
        yield p


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--module", help="un seul module (nom du dossier)")
    p.add_argument("--hors-sons", action="store_true",
                   help="laisser de côté les pastilles de mots isolés")
    p.add_argument("--etat", action="store_true",
                   help="dire ce qui manque, sans rien produire")
    p.add_argument("--taches", type=int, default=os.cpu_count() or 4,
                   help="conversions menées de front")
    args = p.parse_args()

    if not shutil.which("ffmpeg"):
        sys.exit("!! ffmpeg est absent — rien ne peut être produit")

    sources = list(originaux(args.module, args.hors_sons))
    travail = [(src, dst, tempo) for src in sources for dst, tempo in a_produire(src)]
    total = len(sources) * len(CRANS)

    print("originaux : %d    variantes attendues : %d    à produire : %d"
          % (len(sources), total, len(travail)))
    if args.etat or not travail:
        return

    debut = time.time()
    with ThreadPoolExecutor(max_workers=args.taches) as ex:
        faits = list(ex.map(lambda t: produire(*t), travail))
    ok = sum(faits)
    print("produites : %d    ratées : %d    en %.0f s"
          % (ok, len(faits) - ok, time.time() - debut))


if __name__ == "__main__":
    main()
