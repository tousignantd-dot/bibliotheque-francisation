#!/usr/bin/env python3
"""
Ralentissement de la voix « enseignante » (👩 féminine #1).

Cette voix narre les mini-leçons et les mots isolés de presque tous les
modules, en plus de rôles de dialogue : c'est la voix que l'élève entend le
plus, et elle débitait ~18,6 caractères par seconde — trop vite pour du
niveau 4. Le paramètre `speed` d'ElevenLabs ne la corrige pas : avec
`eleven_multilingual_v2`, l'API renvoie le même fichier octet pour octet
avec ou sans `"speed": 0.85`. On ralentit donc après coup, avec le filtre
`atempo` de ffmpeg, qui étire la durée sans toucher à la hauteur : même
timbre, débit posé.

À appeler juste après l'écriture d'un MP3, dans chaque générateur. Sans
ffmpeg, le fichier reste tel quel et un avertissement s'affiche — mieux
vaut un module rapide qu'un module muet.
"""
import shutil
import subprocess
from pathlib import Path

VOIX_ENSEIGNANTE = "K7gx0ylJdff0yjM2uVQS"
FACTEUR = 0.85          # 1,0 = débit d'origine ; 0,85 ≈ 15 % plus lent
_averti = False


def ralentir(chemin):
    """Ralentit un MP3 sur place. Rend True si le fichier a été réécrit."""
    global _averti
    chemin = Path(chemin)
    if not shutil.which("ffmpeg"):
        if not _averti:
            print("   ⚠️  ffmpeg absent : voix laissée au débit d'origine")
            _averti = True
        return False
    tmp = chemin.with_suffix(".ralenti.mp3")
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", str(chemin),
         "-filter:a", f"atempo={FACTEUR}",
         "-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", "-ac", "1",
         str(tmp)],
        capture_output=True, text=True)
    if r.returncode != 0 or not tmp.exists() or tmp.stat().st_size == 0:
        tmp.unlink(missing_ok=True)
        print(f"   ⚠️  ralentissement impossible : {r.stderr.strip()[:120]}")
        return False
    tmp.replace(chemin)
    return True


def ralentir_si_enseignante(chemin, voice_id):
    """Ne ralentit que la voix de l'enseignante : les autres sont à leur place."""
    if voice_id != VOIX_ENSEIGNANTE:
        return False
    return ralentir(chemin)
