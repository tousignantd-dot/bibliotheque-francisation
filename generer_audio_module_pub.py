#!/usr/bin/env python3
"""
Générateur d'audio — Module « Des publicités efficaces » (Culture et médias)
Lit la clé dans AZURE_SPEECH_KEY (fichier .env à la racine).
"""

import os
import sys
import unicodedata
from pathlib import Path
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))

try:
    import requests
except ImportError:
    print("❌ requests n'est pas installé : pip install requests")
    sys.exit(1)

VOICES = {
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 Masculin #1 — Omar
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2 — Solange
}

DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
VOICE_SETTINGS_OVERRIDES = {}

VOICE_ASSOC = {
    "SOLANGE": "feminin_2",
    "OMAR":    "masculin_1",
}

DIALOGUES = {
    "module-pub/prep": {
        "title": "Des publicités efficaces — Je découvre (Trente secondes en ondes)",
        "lines": [
            ("SOLANGE", "Omar, j'ai écrit le texte pour annoncer notre atelier de réparation. Je l'ai lu à voix haute : il dure une minute quarante."),
            ("OMAR", "Une minute quarante ! Solange, une capsule à Radio Limoilou, c'est trente secondes, pas une de plus. Il va falloir couper."),
            ("SOLANGE", "Couper quoi ? Je parle des grille-pain, des lampes, des vélos, des vêtements déchirés, des bénévoles, du café gratuit…"),
            ("OMAR", "Justement, tu parles de tout. À qui veux-tu parler, au juste ? Choisis les gens que tu veux rejoindre, puis garde seulement ce qui les touche."),
            ("SOLANGE", "Aux gens du quartier qui gardent un appareil brisé dans une armoire parce qu'ils n'osent pas le jeter. C'est eux, mon récepteur."),
            ("OMAR", "Alors garde l'objet brisé, la date et l'adresse. Termine par une phrase courte, facile à retenir. Le reste, tu l'écriras sur l'affiche."),
            ("SOLANGE", "« Rien ne se jette, tout se répare. » Voilà, je viens de la trouver, ma phrase courte !"),
        ],
    },
    "module-pub/t1": {
        "title": "Des publicités efficaces — Défi 1 (Deux capsules déjà diffusées)",
        "lines": [
            ("OMAR", "Avant d'enregistrer, écoute les deux capsules du mois passé. Celle de la friperie dure vingt secondes ; celle de la cuisine collective, quarante."),
            ("SOLANGE", "À la friperie, on parle plus vite que sur l'autre capsule. On comprend moins bien, je trouve."),
            ("OMAR", "Tu as raison. La capsule de la cuisine collective est plus longue, mais elle est aussi plus claire que celle de la friperie."),
            ("SOLANGE", "Et la musique ? Celle de la friperie est plus forte que la musique de la cuisine collective. Elle couvre la voix."),
            ("OMAR", "Alors baisse la musique, ralentis un peu, et insiste sur un seul mot : gratuit. C'est celui-là que les gens vont retenir."),
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
    print("🎙️  Générateur d'audio — Des publicités efficaces\n")
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
            print(f"  {i:2d}. {character[:16]:16s} → ", end="", flush=True)
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
