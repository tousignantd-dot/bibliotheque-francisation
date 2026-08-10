#!/usr/bin/env python3
"""
Générateur d'audio — Module « Consulter au bon endroit » (Santé)
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
    "enseignante": "K7gx0ylJdff0yjM2uVQS",   # 👩 Féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2
    "feminin_3":   "rCmVtv8cYU60uhlsOo1M",   # 👩 Féminine #3 — Rosalie (2e essai de voix ; la 1re, u5l0VNCfzO5oqrKTuA1e, corrigeait bien « est-ce que » mais son réglage d'émotion n'a pas convenu)
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 Masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 Narrateur
}

# Réglages par défaut : stability haute → débit régulier mais plat.
# stability basse et style > 0 augmentent l'expressivité (ElevenLabs : « lower
# stability introduces broader emotional range », « style amplifies the
# original speaker's style »). Réglage par voix, pas global : on ne veut pas
# changer le ton des personnages déjà approuvés en touchant à un seul.
DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
VOICE_SETTINGS_OVERRIDES = {
    # Nouvelle voix pour Rosalie (rCmVtv8cYU60uhlsOo1M) : on repart des
    # réglages par défaut plutôt que de garder l'ajustement d'émotion trouvé
    # pour l'ancienne voix — un dosage stability/style qui convenait à une
    # voix ne se transpose pas forcément à une autre.
}

# Chaque personnage a une voix distincte de son interlocuteur, pour qu'on
# reconnaisse qui parle sans jamais entendre le nom du personnage.
VOICE_ASSOC = {
    "YANNICK":       "masculin_1",
    "ROSALIE":       "feminin_3",
    "L'INFIRMIÈRE":  "enseignante",
    "LA DOCTEURE":   "feminin_2",
}

DIALOGUES = {
    "module-consultation/prep": {
        "title": "Consulter au bon endroit — Je me prépare (Le genou de Yannick)",
        "lines": [
            ("YANNICK", "Rosalie, je me suis réveillé ce matin avec le genou tout enflé. J'ai fini mon quart à l'entrepôt à minuit et je n'avais rien senti sur le coup."),
            ("ROSALIE", "Est-ce que tu peux marcher dessus ?"),
            ("YANNICK", "Un peu, mais ça élance dès que je plie la jambe."),
            ("ROSALIE", "Tu n'as pas de fièvre ? La peau n'est pas rouge ?"),
            ("YANNICK", "Non, seulement enflé et chaud."),
            ("ROSALIE", "Alors ce n'est pas un cas pour l'urgence. Va plutôt à la clinique sans rendez-vous du quartier : elle ouvre à sept heures et tu vas passer plus vite."),
            ("YANNICK", "Je pensais appeler mon médecin de famille."),
            ("ROSALIE", "Tu aurais un rendez-vous dans trois semaines. Pour une blessure comme celle-là, il faut voir quelqu'un aujourd'hui."),
            ("YANNICK", "Tu as raison. Je prends ma carte d'assurance maladie et j'y vais tout de suite."),
        ],
    },
    "module-consultation/t1": {
        "title": "Consulter au bon endroit — Tâche 1 (Au triage de la clinique)",
        "lines": [
            ("L'INFIRMIÈRE", "Bonjour, asseyez-vous. Qu'est-ce qui vous amène ce matin ?"),
            ("YANNICK", "J'ai le genou droit enflé depuis cette nuit. Je travaille dans un entrepôt et je soulève des boîtes toute la soirée."),
            ("L'INFIRMIÈRE", "Est-ce que vous vous êtes cogné ou tordu la jambe ?"),
            ("YANNICK", "Je ne me souviens pas d'un coup précis. La douleur est arrivée peu à peu."),
            ("L'INFIRMIÈRE", "Sur une échelle de un à dix, où se situe votre douleur ?"),
            ("YANNICK", "Environ six quand je marche, deux quand je reste assis."),
            ("L'INFIRMIÈRE", "Très bien. Prenez ce numéro, la docteure Beaulieu va vous appeler."),
        ],
    },
    "module-consultation/t2": {
        "title": "Consulter au bon endroit — Tâche 2 (L'examen de la docteure)",
        "lines": [
            ("LA DOCTEURE", "Étendez la jambe, s'il vous plaît. Est-ce que ça fait mal quand j'appuie ici ?"),
            ("YANNICK", "Oui, juste là, sur le côté."),
            ("LA DOCTEURE", "Vous avez une inflammation du tendon. Ce n'est pas une fracture, mais il ne faut pas forcer."),
            ("YANNICK", "Est-ce que je peux retourner travailler demain ?"),
            ("LA DOCTEURE", "Pas tout de suite. Je vous donne un billet pour quatre jours de repos et je vous réfère en physiothérapie."),
            ("YANNICK", "Qu'est-ce que je fais en attendant ?"),
            ("LA DOCTEURE", "De la glace vingt minutes, trois fois par jour, et vous évitez de soulever des charges."),
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
    print("🎙️  Générateur d'audio — Consulter au bon endroit\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente (source .env)")
        sys.exit(1)

    base_dir = Path(__file__).resolve().parent / "assets" / "interactive"
    total = success = 0

    # --character NOM : ne régénère que les répliques de ce personnage
    # (utile pour tester une nouvelle voix sans repayer tout le dialogue).
    # --dialogue id : limite à un seul dialogue (ex. module-consultation/prep).
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
