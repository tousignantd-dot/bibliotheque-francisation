#!/usr/bin/env python3
"""Les trois enregistrements oraux de la classe de démonstration.

Trois voix ElevenLabs distinctes de celles des personnages du module : en
présentation, on doit entendre trois élèves, pas les comédiens du dialogue.
Le texte lu porte les hésitations d'une prise de parole réelle ; la
transcription gardée dans demo_traces.py reste, elle, la phrase propre.

    python3 build/demo_audio.py

Les MP3 sont écrits dans build/demo-voix/ et non directement dans les dépôts :
demo_traces.py --install les y recopie, et une réinstallation n'oblige donc
pas à repayer la synthèse.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "build" / "demo-voix"
MODELE = "eleven_multilingual_v2"

# Voix de catalogue ElevenLabs, distinctes des cinq voix du module.
# Réglages : stability basse pour laisser passer de la variation, style léger.
# Une voix trop stable donne un débit de lecture — or on veut entendre
# quelqu'un qui cherche ses mots.
PRISES = [
    {
        "code": "ETOI42", "voix": "XB0fDUnXU5powFXDhCwa",  # Charlotte
        "reglages": {"stability": 0.35, "similarity_boost": 0.75, "style": 0.25},
        "texte": "Bonjour... j'ai mal au genou depuis trois jours. "
                 "La douleur est forte quand je monte les escaliers, "
                 "et le genou est enflé.",
    },
    {
        "code": "ERAB23", "voix": "N2lVS1w4EtoT3dr4eOWO",  # Callum
        "reglages": {"stability": 0.3, "similarity_boost": 0.75, "style": 0.3},
        "texte": "Euh... j'ai mal à la gorge depuis lundi, et je tousse beaucoup. "
                 "J'ai pas de fièvre, mais... ça empire le soir.",
    },
    {
        "code": "CACT47", "voix": "JBFqnCBsd6RMkjVDRZzb",  # George
        "reglages": {"stability": 0.35, "similarity_boost": 0.75, "style": 0.25},
        "texte": "Bonjour, je voudrais prendre un rendez-vous. "
                 "Ma fille... elle a de la fièvre depuis hier soir.",
    },
]


def cle_api():
    cle = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if cle:
        return cle
    env = RACINE / ".env"
    if env.exists():
        trouve = re.search(r'ELEVENLABS_API_KEY\s*=\s*(\S+)', env.read_text(encoding="utf-8"))
        if trouve:
            return trouve.group(1).strip().strip('"').strip("'")
    return ""


def synthetiser(cle, prise, destination):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{prise['voix']}"
    corps = json.dumps({
        "text": prise["texte"],
        "model_id": MODELE,
        "voice_settings": prise["reglages"],
    }).encode("utf-8")
    requete = urllib.request.Request(url, data=corps, headers={
        "xi-api-key": cle, "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(requete, timeout=60) as reponse:
            destination.write_bytes(reponse.read())
        return True
    except urllib.error.HTTPError as e:
        print(f"   ❌ {e.code} : {e.read()[:200].decode('utf-8', 'replace')}")
    except Exception as e:
        print(f"   ❌ {e}")
    return False


def main():
    cle = cle_api()
    if not cle:
        print("❌ ELEVENLABS_API_KEY absente (.env à la racine du projet)")
        sys.exit(1)

    SORTIE.mkdir(parents=True, exist_ok=True)
    faits = 0
    for prise in PRISES:
        destination = SORTIE / f"{prise['code'].lower()}.mp3"
        print(f"🎙️  {prise['code']} — {prise['texte'][:50]}…")
        if synthetiser(cle, prise, destination):
            print(f"   ✓ {destination.relative_to(RACINE)} ({destination.stat().st_size // 1024} Ko)")
            faits += 1

    print(f"\n{faits}/{len(PRISES)} enregistrements produits.")
    if faits:
        print("Les poser dans la démonstration : python3 build/demo_traces.py --install")


if __name__ == "__main__":
    main()
