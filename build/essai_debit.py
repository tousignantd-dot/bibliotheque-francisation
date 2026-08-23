#!/usr/bin/env python3
"""Les quatre voix sur le même texte, au débit d'origine et ralenties.

    python3 build/essai_debit.py

« Une voix est toujours trop vite » ne se règle pas en devinant laquelle :
les quatre disent ici **la même phrase**, ce qui est la seule façon de les
comparer — un texte différent change la durée, et donc l'impression de
vitesse. Chaque voix sort deux fois, telle quelle et passée à `atempo`, et
le script imprime les caractères par seconde mesurés.

Le débit se lit, mais il s'entend surtout : une voix à 16 c/s peut sembler
plus posée qu'une autre à 15 selon son articulation. Le chiffre sert à
classer, l'oreille à trancher.

Ce qu'on en fait ensuite : `voix_lente.py` ne ralentit aujourd'hui que la
voix « enseignante ». Ajouter une voix à sa liste, ou changer son facteur,
est un geste unique — puis il faut repasser les MP3 déjà produits avec cette
voix.
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from voix import MODELE, charge_utile, url            # noqa: E402

VOIX = {
    "enseignante": "K7gx0ylJdff0yjM2uVQS",   # féminine 1 — déjà ralentie à 0,85
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # féminine 2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # masculin 1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # masculin 2 — jamais ralenti
}

# Une phrase de module, ni courte ni longue, avec des liaisons et une
# question : c'est ce que l'élève entend vraiment, pas un mot isolé.
PHRASE = ("Bonjour, je viens pour mon rendez-vous de neuf heures. "
          "Est-ce que je dois attendre ici ou monter au deuxième étage ?")

FACTEUR = 0.85
SORTIE = pathlib.Path.home() / "Claude" / "generations" / "essai-debit"


def cle_api():
    cle = os.environ.get("ELEVENLABS_API_KEY")
    env = pathlib.Path.home() / "Claude" / ".env"
    if not cle and env.exists():
        for ligne in env.read_text(encoding="utf-8").splitlines():
            if ligne.strip().startswith("ELEVENLABS_API_KEY"):
                cle = ligne.split("=", 1)[1].strip().strip('"').strip("'")
    return cle


def duree(mp3):
    if not shutil.which("ffprobe"):
        return None
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "json", str(mp3)],
                       capture_output=True, text=True)
    try:
        return float(json.loads(r.stdout)["format"]["duration"])
    except Exception:
        return None


def ralentir(src, dst, facteur=FACTEUR):
    if not shutil.which("ffmpeg"):
        return False
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src),
                        "-filter:a", "atempo=%s" % facteur,
                        "-c:a", "libmp3lame", "-b:a", "128k",
                        "-ar", "44100", "-ac", "1", str(dst)],
                       capture_output=True)
    return r.returncode == 0


def main():
    cle = cle_api()
    if not cle:
        print("✗ aucune clé ELEVENLABS_API_KEY")
        return 2
    # Un identifiant passé en argument s'ajoute aux quatre : c'est ainsi qu'on
    # éprouve une voix candidate avant de la faire entrer dans le dépôt.
    for i, vid in enumerate(sys.argv[1:], start=1):
        VOIX["candidate_%d" % i if len(sys.argv) > 2 else "candidate"] = vid
    SORTIE.mkdir(parents=True, exist_ok=True)
    n = len(PHRASE)
    print("Phrase de %d caractères, la même pour les quatre voix.\n" % n)
    mesures = []
    for nom, vid in VOIX.items():
        brut = SORTIE / ("%s-normal.mp3" % nom)
        req = urllib.request.Request(
            url(vid), data=json.dumps(charge_utile(PHRASE, vid)).encode(),
            headers={"xi-api-key": cle, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                brut.write_bytes(r.read())
        except urllib.error.HTTPError as e:
            print("  ✗ %-12s HTTP %s %s"
                  % (nom, e.code, e.read()[:140].decode("utf-8", "replace")))
            return 1
        lent = SORTIE / ("%s-ralenti.mp3" % nom)
        ralentir(brut, lent)
        d, dl = duree(brut), duree(lent)
        mesures.append((nom, d, dl))
        if d:
            print("  ✓ %-12s %5.2f s · %4.1f car/s   →  ralenti %5.2f s · "
                  "%4.1f car/s" % (nom, d, n / d, dl or 0,
                                   n / dl if dl else 0))
        else:
            print("  ✓ %-12s (ffprobe absent, durée non mesurée)" % nom)

    connues = [m for m in mesures if m[1]]
    if connues:
        rapide = max(connues, key=lambda m: 1 / m[1])
        print("\nLa plus rapide au débit d'origine : « %s » (%.1f car/s)."
              % (rapide[0], n / rapide[1]))
    print("À écouter dans %s" % SORTIE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
