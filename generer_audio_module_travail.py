#!/usr/bin/env python3
"""
Générateur d'audio — Module « C'est une absence ou un retard ? » (Monde du travail)
Exécute ce script et rentre ta clé API quand demandé.
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
    "enseignante": "K7gx0ylJdff0yjM2uVQS",      # 👩 Féminine #1
    "feminin_2": "WW0JfNPk5DgcQdM0d6X6",        # 👩 Féminine #2
    "masculin_1": "93nuHbke4dTER9x2pDwE",       # 👨 Masculin #1
    "narrateur": "IPgYtHTNLjC7Bq7IPHrm",        # 👨 Narrateur
}

VOICE_ASSOC = {
    "SOFIA": "feminin_2",
    "MIGUEL": "masculin_1",
    "MIRNA": "enseignante",
}

# ── DIALOGUES ─────────────────────────────────────────────────────────
DIALOGUES = {
    "module-travail/prep": {
        "title": "C'est une absence ou un retard — Je me prépare (Remplacer une collègue)",
        "lines": [
            ("SOFIA", "J'ai eu un appel de madame Labonté, ma superviseure à la pharmacie. Ma collègue Tanya est malade aujourd'hui. Je dois la remplacer, mais j'ai un cours de francisation qui dure toute la journée. Qu'est-ce que je dois faire ? Je rentre au travail ou je vais à mon cours ?"),
            ("MIGUEL", "Selon moi, il faut aller à ton cours. La pharmacie peut appeler une autre employée."),
            ("SOFIA", "Non, il n'y a personne d'autre pour remplacer Tanya aujourd'hui. En plus, elle a bien voulu me remplacer la semaine passée. J'ai promis de lui rendre service à mon tour une prochaine fois…"),
            ("MIGUEL", "Je comprends. Appelle la personne responsable des absences au centre de formation et explique-lui la situation. Puis, rappelle madame Labonté pour lui donner ton accord, mais seulement pour aujourd'hui. Elle doit trouver une autre personne pour remplacer demain, au besoin. Qu'est-ce que tu en penses ?"),
            ("SOFIA", "Oui, bonne idée ! C'est vraiment un bon compromis."),
        ]
    },
    "module-travail/t1": {
        "title": "C'est une absence ou un retard — Tâche 1 (Boîte vocale de Mirna)",
        "lines": [
            ("MIRNA", "Bonjour, c'est Mirna. Je vous appelle parce que j'ai un rendez-vous à l'école de mon fils avec l'enseignante d'Édouard, et avec l'orthopédagogue de l'école, madame Martine Dulac."),
            ("MIRNA", "Le rendez-vous est à 10 h 15 demain. Mon fils a de la difficulté en lecture, et je dois apporter une preuve pour justifier mon absence au cours de francisation."),
            ("MIRNA", "La rencontre va durer environ une heure. Je devrais être de retour au centre de formation vers 10 h 45. Merci de votre compréhension."),
        ]
    },
}


def generate_audio(api_key, text, voice_id, output_path):
    """Génère un fichier audio avec ElevenLabs."""
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
    print("🎙️  Générateur d'audio — Module C'est une absence ou un retard ?\n")

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
            filename = f"line_{i:02d}_{character.lower().replace(' ', '_').replace(chr(39), '')}.mp3"
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
