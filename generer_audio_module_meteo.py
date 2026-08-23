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

from voix_lente import ralentir_si_enseignante
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés

VOICES = {
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 Narrateur — Le météorologue
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 Masculin #1 — Diego
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2 — Josée
    "feminin_3":   "rCmVtv8cYU60uhlsOo1M",   # 👩 Féminine #3 — Prisca
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 Féminine #1 — Mado
}

DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
VOICE_SETTINGS_OVERRIDES = {}

VOICE_ASSOC = {
    "LE MÉTÉOROLOGUE": "narrateur",
    "DIEGO":           "masculin_1",
    "JOSÉE":           "feminin_2",
    "PRISCA":          "feminin_3",
    "MADO":            "enseignante",
}

DIALOGUES = {
    "module-meteo/prep": {
        "title": "Quelles sont les prévisions ? — Je découvre (Monte-t-on sur le toit demain ?)",
        "lines": [
            ("JOSÉE", "Diego, j'annule la journée de demain sur le toit de l'école. On annonce du verglas avant six heures."),
            ("DIEGO", "Du verglas ? Mais on a déjà trois jours de retard sur le chantier..."),
            ("JOSÉE", "Notre règle est claire : personne ne monte si les rafales dépassent quarante kilomètres à l'heure ou si la membrane est glacée."),
            ("DIEGO", "J'ai des crampons dans mon coffre. Je pourrais essayer, au moins sur la pente sud."),
            ("JOSÉE", "Non. Voilà deux ans, un couvreur de l'équipe s'est fracturé le poignet sur une pente gelée. Je ne recommencerai pas ça."),
            ("DIEGO", "D'accord. Qu'est-ce qu'on fait, alors ?"),
            ("JOSÉE", "On rentre à l'atelier : il y a du bardeau à préparer pendant toute la matinée. Si la pluie verglaçante cesse en après-midi, on remonte."),
            ("DIEGO", "Je préviens Prisca ? Elle part de Longueuil vers cinq heures, d'habitude."),
            ("JOSÉE", "Oui, téléphone-lui tout de suite. Elle te remerciera."),
        ],
    },
    "module-meteo/t1": {
        "title": "Quelles sont les prévisions ? — Défi 1 (Le bulletin de six heures)",
        "lines": [
            ("LE MÉTÉOROLOGUE", "Il est six heures. Voici le bulletin spécial pour la Montérégie : une pluie verglaçante recouvre déjà les routes de la Rive-Sud."),
            ("LE MÉTÉOROLOGUE", "Le mercure se maintiendra autour de zéro degré jusqu'au milieu de l'avant-midi, ce qui gardera la chaussée glissante."),
            ("LE MÉTÉOROLOGUE", "Des rafales de soixante kilomètres à l'heure balaieront la région dès neuf heures, et la poudrerie réduira la visibilité par moments."),
            ("LE MÉTÉOROLOGUE", "En après-midi, le vent tombera et le mercure descendra à moins six degrés : la pluie verglaçante se changera alors en neige."),
            ("LE MÉTÉOROLOGUE", "Deux à quatre centimètres d'accumulation sont attendus avant la fin de la soirée."),
            ("LE MÉTÉOROLOGUE", "Demain samedi, le ciel se dégagera et le vent sera faible : une journée idéale pour les travaux en hauteur."),
        ],
    },
    "module-meteo/t2": {
        "title": "Quelles sont les prévisions ? — Défi 2 (Prisca et Mado avant le départ)",
        "lines": [
            ("PRISCA", "Mado, je pars pour le chantier de Granby. Est-ce que l'autoroute 10 est praticable ?"),
            ("MADO", "Attends, je regarde le site du ministère des Transports... Il y a un avertissement de poudrerie entre Sainte-Julie et Marieville."),
            ("PRISCA", "Est-ce qu'on ferme la route ?"),
            ("MADO", "Non, elle reste ouverte, mais la visibilité tombe à moins de deux cents mètres par moments."),
            ("PRISCA", "Je devrais peut-être attendre que le vent faiblisse."),
            ("MADO", "C'est ce que je conseille à tout le monde ce matin. Je leur envoie un message dès que l'avertissement sera levé."),
            ("PRISCA", "Parfait. Je vais préparer les feuilles de temps pendant ce temps-là."),
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
