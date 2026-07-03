#!/usr/bin/env python3
"""
Générateur d'audio pour Visite du Vieux-Montréal — ElevenLabs
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

# ── VOICES ────────────────────────────────────────────────────────────
VOICES = {
    "feminin_2": "WW0JfNPk5DgcQdM0d6X6",
    "masculin_1": "93nuHbke4dTER9x2pDwE",
    "narrateur": "IPgYtHTNLjC7Bq7IPHrm",
}

VOICE_ASSOC = {
    "LÉA": "feminin_2",
    "KARIM": "masculin_1",
    "LE GUIDE": "narrateur",
    "LE PASSANT": "masculin_1",
}

# ── DIALOGUES ─────────────────────────────────────────────────────────
DIALOGUES = {
    "visite-vieux-montreal/dialogue-1": {
        "title": "Visite Vieux-Montréal - Dialogue 1",
        "lines": [
            ("LÉA", "Karim, ce week-end, j'aimerais visiter le Vieux-Montréal. Tu veux venir avec moi ?"),
            ("KARIM", "Oui, avec plaisir ! Je ne connais pas bien ce quartier. Qu'est-ce qu'on peut voir ?"),
            ("LÉA", "Il y a beaucoup de choses ! La place Jacques-Cartier, la basilique Notre-Dame, le Vieux-Port…"),
            ("KARIM", "Super ! Est-ce qu'il y a des visites guidées ?"),
            ("LÉA", "Oui. On peut suivre un guide. Il explique l'histoire et il montre les beaux bâtiments."),
            ("KARIM", "Bonne idée ! Comment est-ce qu'on va là-bas ?"),
            ("LÉA", "On prend le métro, direction Champ-de-Mars. Après, on marche cinq minutes."),
            ("KARIM", "Parfait. On part à quelle heure ?"),
            ("LÉA", "On part à dix heures. Comme ça, on a toute la journée. Ça te va ?"),
            ("KARIM", "Ça me va ! J'ai hâte. Je vais apporter mon appareil photo."),
        ]
    },
    "visite-vieux-montreal/dialogue-2": {
        "title": "Visite Vieux-Montréal - Dialogue 2",
        "lines": [
            ("LE GUIDE", "Bonjour à tous ! Bienvenue dans le Vieux-Montréal, le quartier le plus ancien de la ville."),
            ("LÉA", "C'est vraiment vieux ?"),
            ("LE GUIDE", "Oui ! On fonde Montréal ici, en 1642. C'est le début de la ville."),
            ("LÉA", "Wow ! Et ces rues, elles sont anciennes aussi ?"),
            ("LE GUIDE", "Exactement. Regardez : ce sont des rues pavées, avec de vieilles maisons en pierre."),
            ("LÉA", "C'est magnifique ! On dirait un autre siècle."),
            ("LE GUIDE", "D'abord, on visite la place. Ensuite, on va voir la grande basilique. Suivez-moi !"),
        ]
    },
    "visite-vieux-montreal/dialogue-3": {
        "title": "Visite Vieux-Montréal - Dialogue 3",
        "lines": [
            ("LE GUIDE", "Nous voici sur la place Jacques-Cartier. C'est une grande place très animée."),
            ("KARIM", "Qu'est-ce qu'il y a autour de la place ?"),
            ("LE GUIDE", "À gauche, il y a des restaurants avec des terrasses. En face, vous voyez l'hôtel de ville."),
            ("KARIM", "Et ce grand bâtiment en pierre, à droite ?"),
            ("LE GUIDE", "C'est un ancien édifice. Il date de plus de cent ans. Il est en pierre grise."),
            ("KARIM", "Il est magnifique ! Et où est la basilique ?"),
            ("LE GUIDE", "Continuez tout droit, puis tournez à droite. La basilique Notre-Dame est au coin de la place d'Armes."),
            ("KARIM", "Parfait, merci ! On y va."),
        ]
    },
    "visite-vieux-montreal/dialogue-4": {
        "title": "Visite Vieux-Montréal - Dialogue 4",
        "lines": [
            ("LÉA", "Excusez-moi, monsieur. On visite le quartier. Qu'est-ce que vous nous conseillez ?"),
            ("LE PASSANT", "Ah, vous devez voir la basilique Notre-Dame ! L'intérieur est magnifique, tout en bleu et or."),
            ("LÉA", "Super ! Et pour manger ?"),
            ("LE PASSANT", "Je vous conseille les petits restaurants de la place. La nourriture est bonne et l'ambiance est agréable."),
            ("LÉA", "Merci beaucoup ! Et le soir, qu'est-ce qu'il faut voir ?"),
            ("LE PASSANT", "Le soir, allez au Vieux-Port. Il y a de belles lumières et une vue sur le fleuve. C'est mon endroit préféré."),
            ("LÉA", "Merci pour vos conseils, monsieur ! Bonne journée."),
            ("LE PASSANT", "Bonne visite ! Profitez bien du Vieux-Montréal."),
        ]
    },
}

# ── GÉNÉRATION ────────────────────────────────────────────────────────
def generate_audio(api_key, text, voice_id, output_path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
    }
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
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
    print("🎙️  Générateur d'audio — Visite du Vieux-Montréal\n")

    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        api_key = input("Colle ta clé ElevenLabs : ").strip()
        if not api_key:
            print("❌ Clé API requise")
            sys.exit(1)

    base_dir = Path("/Users/danieltousignant/Claude/bibliotheque-francisation/assets/interactive")

    total = 0
    success = 0

    for dial_id, dial_data in DIALOGUES.items():
        print(f"\n📖 {dial_data['title']}")

        dir_path = base_dir / dial_id
        dir_path.mkdir(parents=True, exist_ok=True)

        for i, (character, text) in enumerate(dial_data["lines"], 1):
            voice_name = VOICE_ASSOC.get(character, "feminin_2")
            voice_id = VOICES[voice_name]

            filename = f"line_{i:02d}_{character.lower().replace(' ', '_')}.mp3"
            output_path = dir_path / filename

            print(f"  {i:2d}. {character[:20]:20s} → ", end="", flush=True)
            total += 1

            if generate_audio(api_key, text, voice_id, output_path):
                print(f"✓ {filename}")
                success += 1
            else:
                print(f"✗ {filename}")

    print(f"\n{'='*60}")
    print(f"✅ {success}/{total} fichiers générés")

if __name__ == "__main__":
    main()
