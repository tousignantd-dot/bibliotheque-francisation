#!/usr/bin/env python3
"""Audio de l'activité « Qu'est-ce qu'une tornade ? » (LAN-2029-4, niveau 2).

Relancer ce script refabrique exactement les fichiers livrés, à côté de
`activite.html`, que la page appelle en liens relatifs.

**Le texte prononcé vit dans `textes.py`, et nulle part ailleurs.** La première
version de ce script portait aussi ses propres copies des mots, du bulletin et
du dialogue — sans accents, et jamais utilisées, puisque tout passe par `TXT`.
Deux versions du même texte dont une seule est lue : on finit par corriger celle
qui ne sert pas. Ici, les listes ne portent donc que la structure (les noms de
fichiers, l'ordre des voix) ; les mots viennent de `textes.py`.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

import requests

from textes import TXT

# Les fichiers vont à la racine du dossier, avec `activite.html` : la page les
# appelle en liens relatifs et la publication recopie l'arborescence telle quelle.
OUT = Path(__file__).resolve().parent

V_METEO = "IPgYtHTNLjC7Bq7IPHrm"   # narrateur
V_NADIA = "WW0JfNPk5DgcQdM0d6X6"   # féminin 2
V_MARC = "93nuHbke4dTER9x2pDwE"    # masculin 1
V_MOT = "mActWQg9kibLro6Z2ouY"     # enseignante (mots isolés, ralentie)

# L'ordre de la liste de vocabulaire. Le texte de chaque mot est dans TXT.
MOTS = ["mot-tornade", "mot-vent", "mot-nuage", "mot-pluie",
        "mot-ciel", "mot-abri", "mot-radio", "mot-danger"]

# Qui parle, réplique par réplique. Le texte est dans TXT sous « d1 », « d2»…
DIALOGUE = ["nadia", "marc", "nadia", "marc", "nadia", "marc",
            "nadia", "marc", "nadia", "marc", "nadia"]

# Un mot isolé ne donne au modèle aucun contexte de langue. Ces deux-là existent
# tels quels en espagnol — `abrí` (« j'ai ouvert ») et `radio` — et sortaient
# donc avec l'accent espagnol, alors que les six autres mots, absents de
# l'espagnol, étaient justes. Ce n'est pas une affaire d'accents : aucun des huit
# n'en porte. `eleven_multilingual_v2` n'accepte ni les balises `<phoneme>` ni le
# paramètre `language_code` ; le seul levier est l'orthographe. On écrit donc le
# mot d'une façon qui n'existe pas en espagnol mais se prononce pareil :
#   un abri  [œ̃n abʁi]  →  un abris   (pluriel muet)
#   la radio [la ʁadjo]  →  la radiot  (-iot = [jo], comme « idiot »)
# Même technique que TEXT_OVERRIDES dans generer_audio_module_urgence_sons.py.
# À revoir mot par mot si la liste de vocabulaire change.
PRONONCIATION = {
    "mot-abri": "un abris",
    "mot-radio": "la radiot",
}


def texte(slug):
    return PRONONCIATION.get(slug, TXT[slug])


def tts(text, voice, path, slow=False):
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    r = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
        headers={"xi-api-key": key, "Content-Type": "application/json"},
        json={"text": text, "model_id": "eleven_multilingual_v2",
              "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}},
        timeout=90)
    if r.status_code != 200:
        print(f"   X {r.status_code} {r.text[:160]}")
        return False
    path.write_bytes(r.content)
    if slow and shutil.which("ffmpeg"):
        tmp = path.with_suffix(".tmp.mp3")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(path),
                        "-filter:a", "atempo=0.85", "-c:a", "libmp3lame",
                        "-b:a", "128k", "-ar", "44100", "-ac", "1", str(tmp)], check=True)
        tmp.replace(path)
    return True


def main():
    if not os.environ.get("ELEVENLABS_API_KEY", "").strip():
        print("ELEVENLABS_API_KEY absente (fichier .env de la bibliothèque)")
        sys.exit(1)
    ok = tot = 0

    for slug in MOTS:
        tot += 1
        print(f"  {slug:14s} ", end="", flush=True)
        good = tts(texte(slug), V_MOT, OUT / f"{slug}.mp3", slow=True)
        ok += good
        print("ok" if good else "echec")

    tot += 1
    print("  bulletin       ", end="", flush=True)
    good = tts(TXT["bulletin"], V_METEO, OUT / "bulletin.mp3")
    ok += good
    print("ok" if good else "echec")

    parts = []
    for i, who in enumerate(DIALOGUE, 1):
        tot += 1
        name = f"dialogue-{i:02d}-{who}.mp3"
        print(f"  {name:22s} ", end="", flush=True)
        good = tts(TXT[f"d{i}"], V_NADIA if who == "nadia" else V_MARC, OUT / name)
        ok += good
        print("ok" if good else "echec")
        if good:
            parts.append(OUT / name)

    if parts and shutil.which("ffmpeg"):
        sil = OUT / "_sil.mp3"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
                        "anullsrc=r=44100:cl=mono", "-t", "0.55", "-c:a", "libmp3lame",
                        "-b:a", "128k", str(sil)], check=True)
        lst = OUT / "_liste.txt"
        seq = []
        for p in parts:
            seq += [p, sil]
        lst.write_text("".join(f"file '{p.name}'\n" for p in seq[:-1]))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                        "-i", str(lst), "-c:a", "libmp3lame", "-b:a", "128k",
                        "-ar", "44100", "-ac", "1", str(OUT / "dialogue.mp3")],
                       check=True, cwd=OUT)
        lst.unlink()
        sil.unlink()
        print("  dialogue.mp3   assemble")

    print(f"\n{ok}/{tot} fichiers")


if __name__ == "__main__":
    main()
