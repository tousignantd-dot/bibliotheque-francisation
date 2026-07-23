#!/usr/bin/env python3
"""
Générateur d'audio — Module « Comment elle va ? » (SA2 — Urgence et hospitalisation)
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
    "ÉRIC LALIBERTÉ": "masculin_1",
    "HAMID": "narrateur",
    "LE MÉDECIN": "masculin_1",
    "L'URGENTOLOGUE": "narrateur",
    "LÉO": "masculin_1",
    "LA RÉCEPTIONNISTE": "enseignante",
}

# ── DIALOGUES ─────────────────────────────────────────────────────────
DIALOGUES = {
    "module-urgence/prep": {
        "title": "Comment elle va — Je me prépare (Un accident)",
        "lines": [
            ("ÉRIC LALIBERTÉ", "Bonjour Monsieur. Je vous appelle parce que j'ai trouvé votre numéro dans le cellulaire de Madame Leila."),
            ("HAMID", "Leila est ma femme. Qu'est-ce qui se passe ?"),
            ("ÉRIC LALIBERTÉ", "Votre femme a causé un accident en traversant la rue. Elle n'a pas vu le feu rouge. Une auto l'a heurtée et elle est tombée au sol."),
            ("HAMID", "Est-ce qu'elle va bien ?"),
            ("ÉRIC LALIBERTÉ", "J'ai appelé le 911. Une ambulance est arrivée en dix minutes. On l'a transportée à l'hôpital. Je suis avec elle."),
            ("HAMID", "Oui, bien sûr. J'arrive !"),
        ]
    },
    "module-urgence/t1": {
        "title": "Comment elle va — Tâche 1 (Docteur, j'ai mal à...)",
        "lines": [
            ("HAMID", "Docteur, ma femme entend très mal depuis l'accident. Je pense qu'elle a un problème d'audition."),
            ("LE MÉDECIN", "Depuis quand a-t-elle ce problème exactement ?"),
            ("HAMID", "Depuis l'accident, il y a deux heures. Avant, elle entendait très bien."),
            ("LE MÉDECIN", "C'est possible que le choc ait affecté son oreille interne. Est-ce qu'elle prend des médicaments ?"),
            ("HAMID", "Non, elle ne prend pas de médicament."),
            ("LE MÉDECIN", "Je vais demander à un audiologiste d'examiner Leila pour comprendre la cause."),
            ("HAMID", "Merci beaucoup, docteur."),
        ]
    },
    "module-urgence/t2": {
        "title": "Comment elle va — Tâche 2 (Ce n'est pas dangereux)",
        "lines": [
            ("L'URGENTOLOGUE", "Monsieur, je viens vous parler de l'état de Leila. Elle est stable."),
            ("HAMID", "Est-ce qu'elle doit rester longtemps à l'hôpital ?"),
            ("L'URGENTOLOGUE", "Elle a subi un traumatisme, mais ce n'est pas grave. Elle devra rester en observation pour la nuit."),
            ("HAMID", "Est-ce que je peux la voir maintenant ?"),
            ("L'URGENTOLOGUE", "Elle est avec l'audiologiste en ce moment. Vous pourrez la voir dans une heure."),
            ("HAMID", "D'accord, je vais attendre. Merci docteur."),
        ]
    },
    "module-urgence/t3": {
        "title": "Comment elle va — Tâche 3 (À l'accueil de l'hôpital)",
        "lines": [
            ("LA RÉCEPTIONNISTE", "Bonjour, je peux vous aider ?"),
            ("LÉO", "Bonjour, je viens voir ma grand-mère. Quelles sont les heures de visite ?"),
            ("LA RÉCEPTIONNISTE", "En semaine, c'est de 10 h à 20 h. La fin de semaine, c'est de 11 h à 18 h."),
            ("LÉO", "Est-ce que mon petit frère de huit ans peut venir avec moi ?"),
            ("LA RÉCEPTIONNISTE", "Un enfant doit être accompagné d'un adulte pour visiter un patient."),
            ("LÉO", "D'accord. Combien de personnes peuvent entrer dans la chambre en même temps ?"),
            ("LA RÉCEPTIONNISTE", "Maximum deux visiteurs à la fois, s'il vous plaît."),
            ("LÉO", "Merci beaucoup !"),
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
    print("🎙️  Générateur d'audio — Module Comment elle va ?\n")

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
