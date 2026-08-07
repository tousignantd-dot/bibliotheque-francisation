#!/usr/bin/env python3
"""
Générateur d'audio — mots isolés du module « Consulter au bon endroit ».
fileId → texte lu ; doit correspondre aux appels playWord() du HTML.
Voix unique (enseignante) pour tous les mots : c'est un modèle de
prononciation, pas un dialogue.
"""
import os, sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ pip install requests"); sys.exit(1)

VOICE = "K7gx0ylJdff0yjM2uVQS"   # 👩 enseignante

CLIPS = {
    # Tableau « Des sons et des lettres » (savoir de prPhon)
    "prPhon_savoir_0_0": "patient",
    "prPhon_savoir_0_1": "jambe",
    "prPhon_savoir_0_2": "temps",
    "prPhon_savoir_0_3": "dent",
    "prPhon_savoir_1_0": "tendon",
    "prPhon_savoir_1_1": "front",
    "prPhon_savoir_1_2": "nom",
    "prPhon_savoir_2_0": "main",
    "prPhon_savoir_2_1": "examen",
    "prPhon_savoir_2_2": "médecin",
    # Exercice 2 — mots à écouter (cartes)
    "prPhon_pha": "patient",
    "prPhon_phb": "tendon",
    "prPhon_phc": "jambe",
    "prPhon_phd": "front",
    "prPhon_phe": "temps",
    "prPhon_phf": "nom",
    "prPhon_phg": "dent",
    "prPhon_phh": "consultation",
}

# Orthographe phonétique quand ElevenLabs prononce mal le mot réel.
TEXT_OVERRIDES = {}


def generate(api_key, text, path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}"
    payload = {"text": text, "model_id": "eleven_multilingual_v2",
               "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
    r = requests.post(url, json=payload,
                      headers={"xi-api-key": api_key, "Content-Type": "application/json"},
                      timeout=45)
    if r.status_code != 200:
        print(f"   ❌ {r.status_code}: {r.text[:150]}")
        return False
    path.write_bytes(r.content)
    return True


def main():
    print("🔊 Mots isolés — Consulter au bon endroit\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / "assets/interactive/module-consultation/sons"
    out.mkdir(parents=True, exist_ok=True)

    ok = 0
    for file_id, text in CLIPS.items():
        spoken = TEXT_OVERRIDES.get(file_id, text)
        print(f"  {file_id:24s} « {spoken} » → ", end="", flush=True)
        if generate(api_key, spoken, out / f"{file_id}.mp3"):
            print("✓"); ok += 1
        else:
            print("✗")
    print(f"\n✅ {ok}/{len(CLIPS)} fichiers générés")


if __name__ == "__main__":
    main()
