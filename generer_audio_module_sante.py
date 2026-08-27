#!/usr/bin/env python3
"""
Générateur d'audio — Module « Prendre rendez-vous et aller à la pharmacie » (Santé)
Lit la clé dans AZURE_SPEECH_KEY (fichier .env à la racine).

Ce module n'a ni mini-leçons « Ouvrir la mini-leçon » (PLUS est vide) ni boutons
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

import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))

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


# L'audio du cours vient d'Azure Speech depuis le 26 août 2026. La fonction
# ci-dessous garde son nom et sa signature — `main()` l'appelle telle quelle —
# mais délègue. La clé ElevenLabs et le contexte `avant`/`apres` sont acceptés
# et ignorés : le `xml:lang="fr-CA"` du SSML rend ce dernier inutile.
from azure_voix import parle_compat  # noqa: E402


def generate_audio(api_key, text, voice_id, output_path, *reste, **nommes):
    # `voice_settings`, `avant`, `apres` : avalés et ignorés. Les deux
    # derniers étaient le contexte français d'ElevenLabs, le premier une
    # dérogation de stabilité qui n'a pas d'équivalent en SSML.
    return parle_compat(api_key, text, voice_id, output_path)
def main():
    print("🎙️  Générateur d'audio — Santé (rendez-vous et pharmacie)\n")
    api_key = os.environ.get("AZURE_SPEECH_KEY", "").strip()
    if not api_key:
        # Repli sur `~/Claude/.env`, où vit la clé Azure avec les autres clés
        # de génération. Sans ça, ces générateurs de forme ancienne — qui ne
        # lisaient que l'environnement — échouaient dès qu'ils étaient lancés
        # autrement qu'à la main dans un shell où la clé était exportée.
        _env = Path.home() / "Claude" / ".env"
        if _env.exists():
            for _l in _env.read_text(encoding="utf-8").splitlines():
                if _l.strip().startswith("AZURE_SPEECH_KEY="):
                    api_key = _l.split("=", 1)[1].strip().strip("\"'")
    if not api_key:
        print("❌ AZURE_SPEECH_KEY absente (source .env)")
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
            # La réplique d'avant et celle d'après partent avec
            # l'extrait, en `previous_text` / `next_text` : du français qui
            # conditionne la synthèse sans être prononcé.
            avant = data["lines"][i - 2][1] if i >= 2 else None
            apres = data["lines"][i][1] if i < len(data["lines"]) else None
            if only_character and character.upper() != only_character:
                continue
            voice_key = VOICE_ASSOC.get(character, "feminin_2")
            voice_id = VOICES[voice_key]
            settings = VOICE_SETTINGS_OVERRIDES.get(voice_key, DEFAULT_VOICE_SETTINGS)
            filename = f"line_{i:02d}_{char_slug(character)}.mp3"
            print(f"  {i:2d}. {character[:18]:18s} → ", end="", flush=True)
            total += 1
            if generate_audio(api_key, text, voice_id, dir_path / filename,
                              settings, avant, apres):
                print(f"✓ {filename}")
                success += 1
            else:
                print(f"✗ {filename}")

    print(f"\n{'='*60}\n✅ {success}/{total} fichiers générés")


if __name__ == "__main__":
    main()
