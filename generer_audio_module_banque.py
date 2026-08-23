#!/usr/bin/env python3
"""
Générateur d'audio — Module « Besoin d'un compte bancaire ? » (Module 17)
Lit la clé dans ELEVENLABS_API_KEY (fichier .env à la racine).

Trois personnages, trois voix féminines distinctes : sans cela, l'élève ne
peut pas suivre qui parle dans un dialogue à deux voix du même timbre.
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
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 Féminine #1 — La conseillère
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2 — Murielle
    "feminin_3":   "rCmVtv8cYU60uhlsOo1M",   # 👩 Féminine #3 — Nour
}

DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}
VOICE_SETTINGS_OVERRIDES = {}

VOICE_ASSOC = {
    "NOUR":            "feminin_3",
    "MURIELLE":        "feminin_2",
    "LA CONSEILLÈRE":  "enseignante",
}

DIALOGUES = {
    "module-banque/prep": {
        "title": "Besoin d'un compte bancaire ? — Je découvre (La première paie de Nour)",
        "lines": [
            ("NOUR", "Murielle, mon premier talon de paie de la résidence est prêt, mais la responsable me demande un spécimen de chèque. Je n'ai pas encore de compte à mon nom."),
            ("MURIELLE", "À mon arrivée ici, j'ai vécu la même chose. Tu es arrivée il y a cinq semaines, c'est normal. Est-ce que tu as tes papiers ?"),
            ("NOUR", "J'ai mon passeport et ma carte d'assurance maladie."),
            ("MURIELLE", "Ça suffit. À la caisse du boulevard, on demande deux pièces d'identité."),
            ("NOUR", "On m'a parlé d'un compte chèque et d'un compte épargne. Je ne vois pas la différence."),
            ("MURIELLE", "Le compte chèque sert tous les jours : la paie entre, le loyer sort. L'épargne, c'est l'argent qu'on laisse de côté et qui rapporte un peu d'intérêt."),
            ("NOUR", "Alors j'ouvre les deux ?"),
            ("MURIELLE", "Commence par le compte chèque, avec le dépôt direct. Tu ajouteras l'épargne quand tu auras de l'argent à mettre de côté."),
            ("NOUR", "Je passe à la caisse demain matin, avant mon quart."),
        ],
    },
    "module-banque/t1": {
        "title": "Besoin d'un compte bancaire ? — Défi 1 (Au comptoir de la caisse)",
        "lines": [
            ("LA CONSEILLÈRE", "Bonjour, asseyez-vous. Qu'est-ce qui vous amène aujourd'hui ?"),
            ("NOUR", "Je viens ouvrir un compte. Mon employeur a besoin d'un spécimen de chèque pour le dépôt direct."),
            ("LA CONSEILLÈRE", "Très bien. Il me faut deux pièces d'identité et une preuve d'adresse."),
            ("NOUR", "Voici mon passeport, ma carte d'assurance maladie et mon bail."),
            ("LA CONSEILLÈRE", "Parfait. Le forfait de base donne douze opérations par mois pour quatre dollars."),
            ("NOUR", "Je paie mon loyer et mon téléphone par prélèvement automatique. Douze, ce serait juste."),
            ("LA CONSEILLÈRE", "Alors prenez le forfait illimité à onze dollars, sans frais si vous gardez mille dollars dans le compte. Signez ici et je vous remets votre carte."),
        ],
    },
    "module-banque/t2": {
        "title": "Besoin d'un compte bancaire ? — Défi 2 (Les opérations du compte)",
        "lines": [
            ("LA CONSEILLÈRE", "Votre carte est activée. Choisissez maintenant un NIP de quatre chiffres, et ne le notez nulle part."),
            ("NOUR", "Est-ce que je peux déposer un chèque au guichet automatique ?"),
            ("LA CONSEILLÈRE", "Oui, ou avec l'application : vous photographiez le chèque et le montant entre dans le compte en deux jours ouvrables."),
            ("NOUR", "Et pour envoyer de l'argent à ma sœur, à Sherbrooke ?"),
            ("LA CONSEILLÈRE", "Vous faites un virement avec son adresse courriel. C'est immédiat, et sans frais avec votre forfait."),
            ("NOUR", "Qu'est-ce qui arrive si je retire plus d'argent que j'en ai ?"),
            ("LA CONSEILLÈRE", "Le compte passe à découvert et des frais s'ajoutent chaque jour. Vérifiez votre solde dans l'application avant un gros achat."),
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
    print("🎙️  Générateur d'audio — Besoin d'un compte bancaire ?\n")
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
