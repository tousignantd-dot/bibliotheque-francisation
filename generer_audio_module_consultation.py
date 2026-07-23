#!/usr/bin/env python3
"""
Générateur d'audio — Module « Quel spécialiste dois-je consulter ? » (SA1)
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
    "LEILA": "feminin_2",
    "HAMID": "masculin_1",
    "LE MÉDECIN": "narrateur",
    "LA RÉCEPTIONNISTE": "enseignante",
}

# ── DIALOGUES ─────────────────────────────────────────────────────────
DIALOGUES = {
    "module-consultation/prep": {
        "title": "Quel spécialiste — Je me prépare (Leila n'entend pas bien)",
        "lines": [
            ("LEILA", "Qu'est-ce que tu dis, chéri ? Peux-tu répéter ? Peux-tu parler plus fort ? Je n'entends plus très bien depuis deux semaines."),
            ("HAMID", "As-tu les oreilles bouchées ?"),
            ("LEILA", "Non."),
            ("HAMID", "As-tu mal ?"),
            ("LEILA", "Non."),
            ("HAMID", "Ce n'est pas normal. Tu devrais aller consulter le docteur Tan."),
            ("LEILA", "Oui, tu as raison. Je ne suis pas certaine d'avoir un rendez-vous dans les prochains jours à cause de l'achalandage dans les hôpitaux. Le temps d'attente est parfois long. Est-ce que tu as son numéro de téléphone ?"),
            ("HAMID", "Oui, voilà !"),
            ("LEILA", "Merci ! Oui, bonjour, j'aimerais prendre un rendez-vous avec le docteur Tan parce que j'ai un problème aux oreilles."),
            ("LA RÉCEPTIONNISTE", "Ah ! Vous tombez bien : j'ai une annulation cet après-midi, à 14 heures. Êtes-vous disponible ?"),
            ("LEILA", "Oui, c'est parfait, merci ! Au revoir !"),
        ]
    },
    "module-consultation/t1": {
        "title": "Quel spécialiste — Tâche 1 (Une chute à vélo)",
        "lines": [
            ("LEILA", "Docteur, je n'entends plus très bien depuis ma chute à vélo, il y a trois jours."),
            ("LE MÉDECIN", "Est-ce que vous portiez un casque au moment de votre chute ?"),
            ("LEILA", "Non, je ne portais pas de casque."),
            ("LE MÉDECIN", "Je vais vous prescrire un anti-inflammatoire et vous référer pour un test d'audition, pour vérifier si la chute a endommagé votre oreille."),
            ("LEILA", "D'accord, merci docteur."),
        ]
    },
    "module-consultation/t2": {
        "title": "Quel spécialiste — Tâche 2 (Le suivi du docteur Tan)",
        "lines": [
            ("LEILA", "Bonjour docteur, le problème d'oreilles persiste depuis ma dernière visite il y a deux semaines."),
            ("LE MÉDECIN", "Qu'est-ce que j'observe en vous examinant… je vois que vos oreilles sont un peu enflées."),
            ("LEILA", "Qu'est-ce que vous recommandez ?"),
            ("LE MÉDECIN", "Je vous prescris un antibiotique à prendre trois fois par jour, pendant sept jours. Je vous recommande aussi de ne pas mettre d'eau dans vos oreilles."),
            ("LEILA", "Pourquoi dois-je passer un test d'audition ?"),
            ("LE MÉDECIN", "Pour vérifier si votre audition s'est améliorée et écarter un problème plus sérieux."),
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
    print("🎙️  Générateur d'audio — Module Quel spécialiste dois-je consulter ?\n")

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
