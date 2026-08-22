#!/usr/bin/env python3
"""
Générateur d'audio — Module « Comment est le logement ? » (Logement)
Lit la clé dans ELEVENLABS_API_KEY (fichier .env à la racine).
"""

import os
import sys
import unicodedata
from pathlib import Path
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés

try:
    import requests
except ImportError:
    print("❌ requests n'est pas installé : pip install requests")
    sys.exit(1)

VOICES = {
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 Masculin #1 — Ibrahim
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2 — Ginette (propriétaire)
    "feminin_3":   "rCmVtv8cYU60uhlsOo1M",   # 👩 Féminine #3 — Leyla (la sœur)
}

DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
VOICE_SETTINGS_OVERRIDES = {}

VOICE_ASSOC = {
    "IBRAHIM": "masculin_1",
    "GINETTE": "feminin_2",
    "LEYLA":   "feminin_3",
}

DIALOGUES = {
    "module-logement/prep": {
        "title": "Comment est le logement ? — Je découvre (La visite du 4 ½ de la rue Galt)",
        "lines": [
            ("IBRAHIM", "Bonjour madame Ginette. J'ai répondu à votre annonce pour le 4 et demi au-dessus de la boulangerie. Je commence un poste de préposé au centre hospitalier le mois prochain, alors je cherche assez vite."),
            ("GINETTE", "Entrez, entrez. Le logement est au deuxième étage. Il se libère le 1er septembre et le bail dure douze mois."),
            ("IBRAHIM", "Et le loyer, il est de combien exactement ?"),
            ("GINETTE", "Huit cent quatre-vingt-dix dollars par mois. Le chauffage et l'eau chaude sont inclus ; l'électricité est à votre charge. La buanderie est au sous-sol et vous avez une place de stationnement dans la ruelle."),
            ("IBRAHIM", "Je travaille de soir et je dors le matin. Est-ce qu'on entend beaucoup la boulangerie d'en bas ?"),
            ("GINETTE", "Je ne vous cacherai rien : le camion de farine arrive vers cinq heures, trois matins par semaine. Par contre, la chambre donne sur la cour, jamais sur la rue."),
            ("IBRAHIM", "D'accord. Et si je voulais repeindre le salon ?"),
            ("GINETTE", "Aucun problème, je fournis la peinture. Les chats sont acceptés, mais pas les chiens. Prenez le temps de réfléchir et rappelez-moi avant vendredi."),
        ],
    },
    "module-logement/t2": {
        "title": "Comment est le logement ? — Défi 2 (Ibrahim en parle à sa sœur Leyla)",
        "lines": [
            ("LEYLA", "Alors, ce logement au-dessus de la boulangerie ? Tu as l'air content, toi."),
            ("IBRAHIM", "Ce qui m'a plu, c'est la chambre : elle donne sur la cour, loin de la rue. Je vais pouvoir dormir le matin après mes quarts."),
            ("LEYLA", "Et l'odeur du pain chaud à cinq heures, ça ne va pas te déranger ?"),
            ("IBRAHIM", "Ça, c'est un cadeau ! Celui que je crains, c'est plutôt le camion de farine qui recule dans la ruelle."),
            ("LEYLA", "Mets des rideaux épais et un ventilateur, le bruit passe au deuxième plan. Et la cuisine, elle est comment ?"),
            ("IBRAHIM", "Petite, mais claire. Ce que je changerais, c'est la couleur des murs : un vert olive un peu triste."),
            ("LEYLA", "Ginette fournit la peinture, non ? Rappelle-la avant vendredi : les logements tranquilles partent vite à Sherbrooke."),
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
        r = requests.post(url, json=enrichir(payload), headers=headers, timeout=45)
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
