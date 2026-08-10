#!/usr/bin/env python3
"""
Générateur d'audio — Module « Des publicités efficaces » (Culture et médias)
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
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 Masculin #1 — Vincent
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2 — Nadia
}

DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
VOICE_SETTINGS_OVERRIDES = {}

VOICE_ASSOC = {
    "NADIA":   "feminin_2",
    "VINCENT": "masculin_1",
}

DIALOGUES = {
    "module-pub/prep": {
        "title": "Des publicités efficaces — Je me prépare (Des projets de vacances)",
        "lines": [
            ("NADIA", "Quand mon père, ma sœur et mon neveu Mateo vont venir au Québec en juillet, j'aimerais leur montrer les plus beaux coins de la province. J'adore organiser des voyages !"),
            ("VINCENT", "Parmi les endroits merveilleux à visiter, il y a les parcs nationaux, comme le parc de la Jacques-Cartier et le parc du Bic."),
            ("NADIA", "Oui, tu as raison. Il y a aussi les chutes Montmorency, une beauté naturelle de la province, que je n'ai pas encore vues. On pourrait aussi visiter la ville de Québec, une ville plus vieille que Montréal !"),
            ("NADIA", "Il y a tellement de beaux endroits à visiter ! Je ne suis jamais allée aux Îles-de-la-Madeleine, en Gaspésie… Connais-tu de plus beaux paysages ?"),
            ("VINCENT", "Woh ! Calme-toi, Nadia ! Nous ne pourrons pas visiter tous ces endroits. Nous allons devoir faire des choix. N'oublie pas que leurs vacances seront moins longues que nos vacances. Il faut aussi prévoir du temps pour se reposer un peu…"),
            ("NADIA", "C'est vrai ! Hier, je suis tombée sur de belles affiches publicitaires à l'agence de voyages du quartier. J'ai toujours rêvé de leur faire découvrir toute la province. Leur visite, c'est la parfaite occasion. Je vais retourner à l'agence pour demander conseil."),
            ("VINCENT", "Quelle excellente idée !"),
        ],
    },
    "module-pub/t1": {
        "title": "Des publicités efficaces — Tâche 1 (Planifier les activités)",
        "lines": [
            ("VINCENT", "Nadia, à Trois-Rivières, on pourrait visiter le Boréalis et se promener sur les berges du fleuve."),
            ("NADIA", "Bonne idée ! Et à Val-David, il y a un parc d'aventure avec de la tyrolienne."),
            ("VINCENT", "Mateo va adorer ça ! Et à Tadoussac, on pourrait faire une excursion pour observer les baleines."),
            ("NADIA", "Mon père va être content, il adore la nature. Et toi, Mateo, qu'est-ce que tu préfères : la tyrolienne ou l'observation des baleines ?"),
            ("VINCENT", "La tyrolienne, ça coûte moins cher que l'excursion aux baleines, mais je pense que Mateo va préférer les baleines !"),
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
    print("🎙️  Générateur d'audio — Des publicités efficaces\n")
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
