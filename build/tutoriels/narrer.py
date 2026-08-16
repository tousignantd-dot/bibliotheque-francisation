#!/usr/bin/env python3
"""Narration des capsules par ElevenLabs, voix « narrateur ».

Le même modèle et les mêmes réglages que les dialogues des modules
(`eleven_multilingual_v2`), pour que le tutoriel ne détonne pas à côté du
reste de la bibliothèque. Un MP3 par plan : c'est sa durée qui fixera la
durée du plan au montage.

Relançable : un plan déjà narré n'est pas repayé. Effacer son MP3 suffit à
le refaire.
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

ICI = Path(__file__).parent
VOIX = "IPgYtHTNLjC7Bq7IPHrm"          # 👨 Narrateur
MODELE = "eleven_multilingual_v2"
REGLAGES = {"stability": 0.5, "similarity_boost": 0.75}
SORTIE = ICI / "voix"


def cle():
    if os.environ.get("ELEVENLABS_API_KEY"):
        return os.environ["ELEVENLABS_API_KEY"]
    env = ICI.parent.parent / ".env"
    for ligne in env.read_text().splitlines():
        if ligne.startswith("ELEVENLABS_API_KEY="):
            return ligne.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("ELEVENLABS_API_KEY introuvable")


def dire(api, texte, destination):
    corps = json.dumps({
        "text": texte,
        "model_id": MODELE,
        "voice_settings": REGLAGES,
    }).encode()
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOIX}",
        data=corps, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("xi-api-key", api)
    req.add_header("Accept", "audio/mpeg")
    with urllib.request.urlopen(req, timeout=120) as r:
        destination.write_bytes(r.read())


def main():
    api = cle()
    SORTIE.mkdir(exist_ok=True)
    manifeste = json.loads((ICI / "manifeste.json").read_text())
    faits = payes = 0
    for capsule in manifeste["capsules"]:
        for plan in capsule["plans"]:
            base = f"{capsule['id']}_{plan['id']}"
            chemin = SORTIE / f"{base}.mp3"
            # Le texte dit est gardé à côté du son. Se fier à la seule
            # présence du MP3 laisserait un plan réécrit garder l'ancienne
            # narration — l'erreur ne s'entend qu'au visionnement final.
            trace = SORTIE / f"{base}.txt"
            faits += 1
            inchange = (chemin.exists() and chemin.stat().st_size > 1000
                        and trace.exists() and trace.read_text() == plan["texte"])
            if inchange:
                continue
            dire(api, plan["texte"], chemin)
            trace.write_text(plan["texte"])
            nom = chemin.name
            payes += len(plan["texte"])
            print(f"  {nom}  ({chemin.stat().st_size // 1024} ko)")
    print(f"{faits} plans narrés, {payes} caractères facturés cette fois")


if __name__ == "__main__":
    main()
