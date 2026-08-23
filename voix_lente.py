#!/usr/bin/env python3
"""
Ralentissement de la voix « enseignante ».

Cette voix narre les mini-leçons et les mots isolés de presque tous les
modules, en plus de rôles de dialogue : c'est la voix que l'élève entend le
plus, et c'est donc celle dont le débit compte le plus.

**Elle a changé le 23 août 2026.** L'ancienne (`K7gx0ylJdff0yjM2uVQS`) est
abandonnée : mesurée sur une même phrase contre les trois autres du dépôt,
elle sortait à 20,8 caractères par seconde quand les autres tenaient 18 à 19
— la plus rapide des quatre, et ralentie à 0,85 elle restait au niveau des
autres non ralenties. La remplaçante (`mActWQg9kibLro6Z2ouY`) débite 17,7 c/s
sans aucun traitement, soit exactement ce que l'ancienne donnait *après*
`atempo` — et ralentie à son tour, elle descend à 15,1. Le facteur reste donc
appliqué, mais il part de plus bas. Ne pas revenir à l'ancienne : la plainte
portait sur elle, y compris ralentie.

Le paramètre `speed` d'ElevenLabs ne corrige rien ici : avec
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

VOIX_ENSEIGNANTE = "mActWQg9kibLro6Z2ouY"
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
