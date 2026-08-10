#!/usr/bin/env python3
"""
Générateur d'audio — Module « Quelle est la procédure ? » (Monde du travail)
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
    "enseignante": "K7gx0ylJdff0yjM2uVQS",   # 👩 Féminine #1 — La commis
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2 — Diane
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 Masculin #1 — Samuel
}

DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
VOICE_SETTINGS_OVERRIDES = {}

VOICE_ASSOC = {
    "SAMUEL":     "masculin_1",
    "DIANE":      "feminin_2",
    "LA COMMIS":  "enseignante",
}

DIALOGUES = {
    "module-procedure/prep": {
        "title": "Quelle est la procédure ? — Je me prépare (Des lunettes de sécurité)",
        "lines": [
            ("SAMUEL", "Diane, j'ai dû acheter des lunettes de sécurité pour mon nouveau poste à l'entrepôt. Ça m'a coûté quarante dollars. Est-ce que l'entreprise rembourse ce genre de dépense ?"),
            ("DIANE", "Oui, bien sûr ! Il y a une procédure à suivre. Tu dois remplir une demande de remboursement sur l'application de l'entreprise."),
            ("SAMUEL", "Ah bon ? Je ne savais pas qu'on avait une application pour ça."),
            ("DIANE", "Oui, elle s'appelle Ressources+. Tu prends une photo de ton reçu, tu entres le montant, puis tu envoies ta demande."),
            ("SAMUEL", "D'accord. Est-ce qu'il faut l'approbation de quelqu'un avant ?"),
            ("DIANE", "Oui, ton superviseur doit approuver la demande avant que les finances la traitent."),
            ("SAMUEL", "Combien de temps ça prend, habituellement ?"),
            ("DIANE", "En général, une dizaine de jours. Garde ton reçu original, au cas où."),
        ],
    },
    "module-procedure/t1": {
        "title": "Quelle est la procédure ? — Tâche 1 (Samuel et la commis aux finances)",
        "lines": [
            ("SAMUEL", "Bonjour, j'aimerais savoir comment faire une demande de remboursement pour du matériel de sécurité."),
            ("LA COMMIS", "Bonjour. Vous devez remplir le formulaire dans l'application Ressources+, sous l'onglet Dépenses."),
            ("SAMUEL", "D'accord. Est-ce que je dois joindre mon reçu ?"),
            ("LA COMMIS", "Oui, une photo claire du reçu est obligatoire, sinon la demande est refusée."),
            ("SAMUEL", "Combien de temps faut-il pour recevoir le remboursement ?"),
            ("LA COMMIS", "Environ dix jours ouvrables, une fois que votre superviseur a approuvé la demande."),
        ],
    },
    "module-procedure/t2": {
        "title": "Quelle est la procédure ? — Tâche 2 (Diane explique comment soumettre une demande)",
        "lines": [
            ("DIANE", "D'abord, tu ouvres l'application Ressources+ et tu appuies sur Nouvelle demande."),
            ("SAMUEL", "D'accord, et ensuite ?"),
            ("DIANE", "Tu prends une photo claire de ton reçu directement avec l'application."),
            ("SAMUEL", "Et pour le montant ?"),
            ("DIANE", "Tu inscris le montant exact, tu choisis la catégorie « équipement de sécurité », puis tu appuies sur Envoyer."),
            ("SAMUEL", "Merci, Diane, c'est très clair !"),
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
    print("🎙️  Générateur d'audio — Quelle est la procédure ?\n")
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
