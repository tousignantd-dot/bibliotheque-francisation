#!/usr/bin/env python3
"""
Générateur d'audio — Module « Prendre rendez-vous et aller à la pharmacie » (Santé)
Lit la clé dans ELEVENLABS_API_KEY (fichier .env à la racine).

Ce module n'a ni mini-leçons « En apprendre plus » (PLUS est vide) ni boutons
d'écoute mot à mot : il n'y a donc rien à mettre dans sons/, seulement les
répliques des deux dialogues.
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

from voix_lente import ralentir_si_enseignante
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés

VOICES = {
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 Féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2
    "feminin_3":   "rCmVtv8cYU60uhlsOo1M",   # 👩 Féminine #3
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 Masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 Narrateur
}

DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
VOICE_SETTINGS_OVERRIDES = {}

# Lina traverse les deux dialogues : sa voix ne bouge pas d'une scène à
# l'autre, sinon l'élève croirait entendre deux personnes. Ses deux
# interlocuteurs prennent des voix distinctes de la sienne.
VOICE_ASSOC = {
    "LINA":              "feminin_2",
    "LA RÉCEPTIONNISTE": "enseignante",
    "LE PHARMACIEN":     "masculin_1",
}

DIALOGUES = {
    "module-sante/prep": {
        "title": "Santé — Je découvre (Appeler la clinique)",
        "lines": [
            ("LA RÉCEPTIONNISTE", "Clinique Notre-Dame, bonjour."),
            ("LINA", "Bonjour, je voudrais prendre un rendez-vous avec un médecin, s'il vous plaît."),
            ("LA RÉCEPTIONNISTE", "Bien sûr. Est-ce que vous êtes déjà venue à notre clinique ?"),
            ("LINA", "Oui, l'année dernière. Je m'appelle Lina Ferreira."),
            ("LA RÉCEPTIONNISTE", "Parfait. Quelle est la raison de votre visite ?"),
            ("LINA", "Je me sens fatiguée depuis deux semaines et j'ai souvent mal à la tête."),
            ("LA RÉCEPTIONNISTE", "Je comprends. Le docteur Tremblay est libre jeudi à onze heures. Est-ce que ça vous convient ?"),
            ("LINA", "Oui, c'est parfait. Merci beaucoup !"),
            ("LA RÉCEPTIONNISTE", "N'oubliez pas votre carte d'assurance maladie. À jeudi !"),
        ],
    },
    "module-sante/t1": {
        "title": "Santé — À la pharmacie",
        "lines": [
            ("LE PHARMACIEN", "Bonjour, est-ce que je peux vous aider ?"),
            ("LINA", "Oui, j'ai une ordonnance du médecin pour des antibiotiques."),
            ("LE PHARMACIEN", "D'accord. Est-ce que vous avez déjà pris ce médicament avant ?"),
            ("LINA", "Non, c'est la première fois. Comment est-ce que je dois le prendre ?"),
            ("LE PHARMACIEN", "Prenez un comprimé deux fois par jour, matin et soir, pendant sept jours."),
            ("LINA", "Est-ce que je peux le prendre avec de la nourriture ?"),
            ("LE PHARMACIEN", "Oui, c'est même recommandé. Ne buvez pas d'alcool pendant le traitement."),
            ("LINA", "Merci beaucoup pour vos conseils !"),
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
        ralentir_si_enseignante(output_path, voice_id)
        return True
    except Exception as e:
        print(f"   ❌ {e}")
        return False


def main():
    print("🎙️  Générateur d'audio — Santé (rendez-vous et pharmacie)\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente (source .env)")
        sys.exit(1)

    base_dir = Path(__file__).resolve().parent / "assets" / "interactive"
    total = success = 0

    # --character NOM : ne régénère que les répliques de ce personnage.
    # --dialogue id  : limite à un dialogue (ex. module-sante/prep).
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
            print(f"  {i:2d}. {character[:18]:18s} → ", end="", flush=True)
            total += 1
            if generate_audio(api_key, text, voice_id, dir_path / filename, settings):
                print(f"✓ {filename}")
                success += 1
            else:
                print(f"✗ {filename}")

    print(f"\n{'='*60}\n✅ {success}/{total} fichiers générés")


if __name__ == "__main__":
    main()
