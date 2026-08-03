#!/usr/bin/env python3
"""
Générateur d'audio — Module « C'est une absence ou un retard ? »
Section « Je me prépare » : mots isolés (tableau des sons + exercice 2)
et phrases (exercice 3). Une seule voix narratrice (pas un dialogue).
Sortie : assets/interactive/module-travail/sons/<fileId>.mp3
"""

import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ requests n'est pas installé. Installe-le :")
    print("   pip install requests")
    sys.exit(1)

VOICE_ID = "IPgYtHTNLjC7Bq7IPHrm"  # Narrateur — même voix pour toute la page, cohérence pédagogique

# Voix de secours pour des clips précis où le narrateur prononçait mal
# (ex. « hiver » incompréhensible avec le narrateur — signalé 2026-08-02).
VOICE_OVERRIDES = {
    "prPhon_savoir_0_5": "lpWJhr15teNWHhRqdTOQ",  # hiver
    "prPhon_savoir_1_3": "lpWJhr15teNWHhRqdTOQ",  # hiver
    "prPhon_phf": "lpWJhr15teNWHhRqdTOQ",         # hiver
}
# Orthographe phonétique envoyée à ElevenLabs pour ces fileId — le texte
# français correct ("hiver") est mal prononcé par le modèle ; on envoie une
# graphie homophone qui se prononce correctement, tout en gardant "hiver"
# affiché à l'élève dans le tableau des sons.
TEXT_OVERRIDES = {
    "prPhon_savoir_0_5": "i-vair",
    "prPhon_savoir_1_3": "i-vair",
    "prPhon_phf": "i-vair",
}

# fileId → texte à lire (doit correspondre exactement aux appels playWord()
# dans module-travail-activite-interactive.html)
CLIPS = {
    # Tableau « Des sons et des lettres » (savoir de prPhon)
    "prPhon_savoir_0_0": "père",
    "prPhon_savoir_0_1": "tête",
    "prPhon_savoir_0_2": "treize",
    "prPhon_savoir_0_3": "semaine",
    "prPhon_savoir_0_4": "nouvelle",
    "prPhon_savoir_0_5": "hiver",
    "prPhon_savoir_1_0": "dépanné",
    "prPhon_savoir_1_1": "je travaillerai",
    "prPhon_savoir_1_2": "dépanner",
    "prPhon_savoir_1_3": "hiver",
    "prPhon_savoir_1_4": "mer",
    "prPhon_savoir_2_0": "poste",
    "prPhon_savoir_2_1": "dépôt",
    "prPhon_savoir_2_2": "tôt",
    "prPhon_savoir_2_3": "rôle",
    # Exercice 2 — graphie-phonie (mots à écouter)
    "prPhon_pha": "père",
    "prPhon_phb": "travaillerai",
    "prPhon_phc": "nouvelle",
    "prPhon_phd": "dépanné",
    "prPhon_phe": "semaine",
    "prPhon_phf": "hiver",
    "prPhon_phg": "dépanner",
    "prPhon_phh": "treize",
    # Exercice 3 — dictée de phrases
    "prAccent_0": "J'aimerais être plus patient avec mes collègues.",
    "prAccent_1": "Le rendez-vous se passe demain matin, dans son bureau.",
    "prAccent_2": "Elle observe la lettre avec attention.",
    "prAccent_3": "Cet hiver, je dois prévenir mon superviseur et rester à la maison.",
}


def generate_audio(api_key, text, voice_id, output_path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        if response.status_code != 200:
            print(f"   ❌ Erreur {response.status_code}: {response.text[:200]}")
            return False
        with open(output_path, "wb") as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"   ❌ Erreur : {e}")
        return False


def main():
    print("🎙️  Générateur d'audio — Je me prépare (mots et phrases isolés)\n")

    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        api_key = input("Colle ta clé ElevenLabs : ").strip()
        if not api_key:
            print("❌ Clé API requise")
            sys.exit(1)

    dir_path = Path("/Users/danieltousignant/Claude/bibliotheque-francisation/assets/interactive/module-travail/sons")
    dir_path.mkdir(parents=True, exist_ok=True)

    total = 0
    success = 0
    for file_id, text in CLIPS.items():
        output_path = dir_path / f"{file_id}.mp3"
        print(f"  {file_id:22s} → ", end="", flush=True)
        total += 1
        voice_id = VOICE_OVERRIDES.get(file_id, VOICE_ID)
        text_to_speak = TEXT_OVERRIDES.get(file_id, text)
        if generate_audio(api_key, text_to_speak, voice_id, output_path):
            print(f"✓ {text}" + (f" (envoyé: {text_to_speak})" if text_to_speak != text else ""))
            success += 1
        else:
            print(f"✗ {text}")

    print(f"\n{'='*60}")
    print(f"✅ {success}/{total} fichiers générés")


if __name__ == "__main__":
    main()
