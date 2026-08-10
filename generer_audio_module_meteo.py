#!/usr/bin/env python3
"""
Générateur d'audio — Module « Quelles sont les prévisions ? » (Vie quotidienne)
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
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 Narrateur — Le présentateur
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 Masculin #1 — Karim
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2 — Farida
    "feminin_3":   "rCmVtv8cYU60uhlsOo1M",   # 👩 Féminine #3 — Amina
    "enseignante": "K7gx0ylJdff0yjM2uVQS",   # 👩 Féminine #1 — Chantal
}

DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
VOICE_SETTINGS_OVERRIDES = {}

VOICE_ASSOC = {
    "LE PRÉSENTATEUR": "narrateur",
    "KARIM":           "masculin_1",
    "FARIDA":          "feminin_2",
    "AMINA":           "feminin_3",
    "CHANTAL":         "enseignante",
}

DIALOGUES = {
    "module-meteo/prep": {
        "title": "Quelles sont les prévisions ? — Je me prépare (Une promenade malgré le froid)",
        "lines": [
            ("FARIDA", "Karim, si on allait marcher un peu après le souper ? Le médecin dit que je dois bouger davantage pour bien récupérer."),
            ("KARIM", "Tu es sérieuse ? Il fait -18 aujourd'hui !"),
            ("FARIDA", "On va s'habiller chaudement : un gros manteau, une tuque, des mitaines et de bonnes bottes."),
            ("KARIM", "Bon, si tu te sens capable, une petite marche, d'accord."),
            ("KARIM", "Je ne veux surtout pas que tu te blesses de nouveau. Ça fait seulement cinq semaines que tu es sortie de l'hôpital."),
            ("FARIDA", "Je me sens vraiment bien, je te le promets."),
            ("KARIM", "Je sais, mais la physiothérapeute a été claire : il faut y aller doucement."),
            ("FARIDA", "Je suis restée assise pendant plus d'un mois, ça suffit ! En plus, on annonce du soleil tout l'après-midi. Il fera plus chaud que maintenant."),
            ("KARIM", "D'accord, d'accord... allons-y, mais pas trop longtemps !"),
        ],
    },
    "module-meteo/t1": {
        "title": "Quelles sont les prévisions ? — Tâche 1 (Bulletin météo de la semaine)",
        "lines": [
            ("LE PRÉSENTATEUR", "Bonjour à tous, voici les prévisions pour le reste de la semaine. Aujourd'hui, mercredi, le mercure affiche moins dix degrés sous un ciel dégagé."),
            ("LE PRÉSENTATEUR", "Ce soir, le ciel restera dégagé, sans précipitation prévue."),
            ("LE PRÉSENTATEUR", "Demain jeudi, une accumulation de neige de cinq centimètres est attendue en matinée."),
            ("LE PRÉSENTATEUR", "Le mercure chutera à moins vingt-deux degrés jeudi, avec des vents forts qui rendront l'air encore plus froid : habillez-vous chaudement !"),
            ("LE PRÉSENTATEUR", "Vendredi, le temps se radoucira un peu, autour de moins huit degrés."),
            ("LE PRÉSENTATEUR", "En fin de semaine, le ciel se dégagera progressivement et les températures remonteront : une excellente occasion de sortir profiter du plein air !"),
        ],
    },
    "module-meteo/t2": {
        "title": "Quelles sont les prévisions ? — Tâche 2 (Amina et Chantal parlent de l'hiver)",
        "lines": [
            ("AMINA", "C'est mon premier hiver ici, à Québec. J'ai du mal à m'habituer !"),
            ("CHANTAL", "Je comprends, ça prend du temps de s'acclimater à notre climat."),
            ("AMINA", "Je ne sais jamais comment m'habiller. Un jour il fait doux, le lendemain il gèle !"),
            ("CHANTAL", "C'est vrai que la météo change vite ici. Le mieux, c'est d'écouter les prévisions chaque matin."),
            ("AMINA", "Je viens de Tunis, alors je ne suis vraiment pas habituée à ça !"),
            ("CHANTAL", "Pour ne pas être prise par surprise, habille-toi comme un oignon : plusieurs couches que tu peux enlever si tu as chaud."),
            ("AMINA", "Ah, bonne idée, merci !"),
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
    print("🎙️  Générateur d'audio — Quelles sont les prévisions ?\n")
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
