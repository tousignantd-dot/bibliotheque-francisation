#!/usr/bin/env python3
"""
Générateur d'audio — Module « C'est l'heure des nouvelles ? » (Culture et médias)
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

from voix_lente import ralentir_si_enseignante
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés

VOICES = {
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 Narrateur — Le journaliste
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 Masculin #1 — Marc
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2 — Sophie
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 Féminine #1 — Dany
}

DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
VOICE_SETTINGS_OVERRIDES = {}

VOICE_ASSOC = {
    "LE JOURNALISTE": "narrateur",
    "MARC":           "masculin_1",
    "SOPHIE":         "feminin_2",
    "DANY":           "enseignante",
}

DIALOGUES = {
    "module-nouvelles/prep": {
        "title": "C'est l'heure des nouvelles ? — Je découvre (Le bulletin de nouvelles)",
        "lines": [
            ("MARC", "Chut, écoutez ! Ils parlent de la collecte de mitaines organisée par la classe de Sophie !"),
            ("LE JOURNALISTE", "Hier, dans une école de Longueuil, des élèves de 3e secondaire ont amassé plus de deux cents paires de mitaines et de tuques pour les enfants du quartier. L'activité a été organisée avec l'aide de l'organisme Les Cœurs d'hiver."),
            ("DANY", "Ah, c'est vrai ! C'était avant-hier, la collecte !"),
            ("SOPHIE", "C'est Noah qui a eu l'idée. Il en a parlé à son enseignante dès septembre !"),
            ("DANY", "Noah était tellement content quand il a vu toutes les boîtes pleines."),
            ("MARC", "Regarde, la caméra montre justement la classe de Noah !"),
            ("DANY", "C'est vraiment touchant. Un jour, en repensant à cette collecte, il va être fier de lui."),
            ("SOPHIE", "Et dire qu'avant-hier, il n'y avait que trente paires de mitaines dans les boîtes. Aujourd'hui, il y en a plus de deux cents !"),
            ("MARC", "C'est Noah qu'on doit remercier pour cette belle initiative !"),
        ],
    },
    "module-nouvelles/t1": {
        "title": "C'est l'heure des nouvelles ? — Défi 1 (Une fillette retrouve son chat)",
        "lines": [
            ("LE JOURNALISTE", "À Gatineau, une fillette de six ans a retrouvé son chat disparu grâce à une affiche fabriquée dans le cadre d'un projet scolaire."),
            ("LE JOURNALISTE", "Le chat, prénommé Mistigri, s'était sauvé par une fenêtre entrouverte il y a trois jours."),
            ("LE JOURNALISTE", "La fillette a distribué des affiches dans le quartier avec l'aide de sa classe."),
            ("LE JOURNALISTE", "Une voisine a reconnu l'animal dans sa cour hier matin et a aussitôt averti la famille."),
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
    print("🎙️  Générateur d'audio — C'est l'heure des nouvelles ?\n")
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
