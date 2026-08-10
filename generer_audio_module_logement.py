#!/usr/bin/env python3
"""
Générateur d'audio — Module « Comment est le logement ? » (Logement)
Lit la clé dans ELEVENLABS_API_KEY (fichier .env à la racine).
"""

import os
import sys
import unicodedata
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ requests n'est pas installé : pip install requests")
    sys.exit(1)

VOICES = {
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 Masculin #1 — Benoît / Simon
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2 — Carole
    "feminin_3":   "rCmVtv8cYU60uhlsOo1M",   # 👩 Féminine #3 — Maria
}

DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
VOICE_SETTINGS_OVERRIDES = {}

VOICE_ASSOC = {
    "CAROLE":  "feminin_2",
    "BENOÎT":  "masculin_1",
    "SIMON":   "masculin_1",
    "MARIA":   "feminin_3",
}

DIALOGUES = {
    "module-logement/prep": {
        "title": "Comment est le logement ? — Je me prépare (La visite du logement)",
        "lines": [
            ("CAROLE", "On a enfin terminé les rénovations dans notre duplex ! L'appartement du deuxième étage est superbe maintenant. Ces travaux étaient vraiment nécessaires."),
            ("BENOÎT", "Oui, tu as raison. Ce que je préfère, c'est le nouveau plancher de bois franc. J'espère que ça va plaire au couple qui vient visiter demain. À ton avis, l'appartement est-il prêt pour la location ?"),
            ("CAROLE", "Oui, absolument ! Les conditions de location restent-elles les mêmes que l'an dernier ?"),
            ("BENOÎT", "Oui. Le loyer sera encore de 1100 $ par mois. C'est un bel appartement, il est assez grand pour un couple avec un ou deux enfants. L'électricité et le chauffage seront aux frais des locataires. On fournit la cuisinière et le réfrigérateur. Les animaux sont interdits."),
            ("CAROLE", "Si les locataires veulent repeindre l'appartement, ils devront payer la peinture, car on vient tout juste de tout rénover."),
            ("BENOÎT", "Quand débutera le bail ?"),
            ("CAROLE", "Le 1er juillet. Il sera valide pour un an. Si tout se passe bien, on offrira aux locataires un renouvellement à long terme."),
            ("BENOÎT", "D'accord. C'est parfait !"),
        ],
    },
    "module-logement/t2": {
        "title": "Comment est le logement ? — Tâche 2 (Simon et Maria visitent l'appartement)",
        "lines": [
            ("SIMON", "J'ai vraiment hâte de voir cet appartement ! J'espère qu'il y a l'air climatisé, je crains d'avoir chaud l'été sans ça."),
            ("MARIA", "Je reviens justement de la visite, j'y suis allée avant toi. Il est très lumineux et douillet !"),
            ("SIMON", "Est-ce qu'il y a de la place pour un chat ? On pourrait peut-être en adopter un."),
            ("MARIA", "Je n'ai pas posé la question, mais l'appartement est assez grand. Pour la cuisine, j'aimerais des couleurs claires et chaleureuses."),
            ("SIMON", "Et pour le salon, j'aimerais une ambiance calme et cocooning."),
            ("MARIA", "Moi aussi ! On pourrait demander à ajouter une clause dans le bail pour les animaux, au cas où."),
            ("SIMON", "Bonne idée. Je pense qu'on devrait signer le bail rapidement, cet appartement est parfait pour nous."),
        ],
    },
}


def char_slug(name):
    """Doit correspondre exactement à charSlug() du HTML (accents retirés)."""
    s = unicodedata.normalize("NFD", name.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("'", "").replace(" ", "_")


def generate_audio(api_key, text, voice_id, output_path, voice_settings):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": voice_settings,
    }
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=45)
        if r.status_code != 200:
            print(f"   ❌ {r.status_code}: {r.text[:200]}")
            return False
        output_path.write_bytes(r.content)
        return True
    except Exception as e:
        print(f"   ❌ {e}")
        return False


def main():
    print("🎙️  Générateur d'audio — Comment est le logement ?\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente (source .env)")
        sys.exit(1)

    base_dir = Path(__file__).resolve().parent / "assets" / "interactive"
    total = success = 0

    only_character = None
    only_dialogue = None
    for i, a in enumerate(sys.argv):
        if a == "--character" and i + 1 < len(sys.argv):
            only_character = sys.argv[i + 1].upper()
        if a == "--dialogue" and i + 1 < len(sys.argv):
            only_dialogue = sys.argv[i + 1]

    for dial_id, data in DIALOGUES.items():
        if only_dialogue and dial_id != only_dialogue:
            continue
        print(f"\n📖 {data['title']}")
        dir_path = base_dir / dial_id
        dir_path.mkdir(parents=True, exist_ok=True)
        for i, (character, text) in enumerate(data["lines"], 1):
            if only_character and character.upper() != only_character:
                continue
            voice_key = VOICE_ASSOC.get(character, "feminin_2")
            voice_id = VOICES[voice_key]
            settings = VOICE_SETTINGS_OVERRIDES.get(voice_key, DEFAULT_VOICE_SETTINGS)
            filename = f"line_{i:02d}_{char_slug(character)}.mp3"
            print(f"  {i:2d}. {character[:16]:16s} → ", end="", flush=True)
            total += 1
            if generate_audio(api_key, text, voice_id, dir_path / filename, settings):
                print(f"✓ {filename}")
                success += 1
            else:
                print(f"✗ {filename}")

    print(f"\n{'='*60}\n✅ {success}/{total} fichiers générés")


if __name__ == "__main__":
    main()
