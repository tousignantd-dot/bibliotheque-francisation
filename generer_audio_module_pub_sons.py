#!/usr/bin/env python3
"""
Générateur d'audio — mots isolés de l'exercice « Le son [ʃ] ou [ʒ] » (module-pub).
fileId → texte lu ; doit correspondre aux appels playWord() du HTML.
Voix unique (enseignante) : c'est un modèle de prononciation, pas un dialogue.
"""
import os, sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ pip install requests"); sys.exit(1)

from voix_lente import ralentir_si_enseignante
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés

VOICE = "mActWQg9kibLro6Z2ouY"   # 👩 enseignante

CLIPS = {
    # Bandeau « Des sons et des lettres » : on lit la PHRASE PORTEUSE
    # (CARRIER_PHRASES dans le HTML), jamais le mot seul.
    "prSons_savoir_0_0": "L'affiche annonce un atelier gratuit.",
    "prSons_savoir_0_1": "Choisis une seule idée par capsule.",
    "prSons_savoir_0_2": "La capsule passe sur la chaîne de radio.",
    "prSons_savoir_1_0": "Les gens du quartier écoutent la radio.",
    "prSons_savoir_1_1": "Le message doit tenir en trente secondes.",
    "prSons_savoir_1_2": "Ce slogan va rejoindre beaucoup de monde.",
    "prSons_savoir_2_0": "L'atelier de réparation est gratuit.",
    # Cartes de l'exercice — un mot par carte.
    "prSons_psa": "affiche",
    "prSons_psb": "message",
    "prSons_psc": "choisis",
    "prSons_psd": "gens",
    "prSons_pse": "chaîne",
    "prSons_psf": "justement",
    "prSons_psg": "déchirés",
    "prSons_psh": "rejoindre",
}

# Un mot seul ne donne au moteur aucun indice de langue et se fait lire à
# l'anglaise. On ajoute le plus court contexte possible. Le contexte ne doit
# jamais contenir le son testé, sinon il souffle la réponse : d'où « le / la »
# plutôt que « un / une » dans les exercices sur les voyelles nasales, et
# jamais « les » dans celui qui oppose [e] et [ɛ].
TEXT_OVERRIDES = {
    "prSons_psa": "l'affiche",
    "prSons_psb": "le message",
    "prSons_psc": "tu choisis",
    "prSons_psd": "les gens",
    "prSons_pse": "la chaîne",
    "prSons_psf": "oui, justement",
    "prSons_psg": "des vêtements déchirés",
    "prSons_psh": "il faut rejoindre",
}


def generate(api_key, text, path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}"
    payload = {"text": text, "model_id": "eleven_multilingual_v2",
               "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
    r = requests.post(url, json=enrichir(payload),
                      headers={"xi-api-key": api_key, "Content-Type": "application/json"},
                      timeout=45)
    if r.status_code != 200:
        print(f"   ❌ {r.status_code}: {r.text[:150]}")
        return False
    path.write_bytes(r.content)
    ralentir_si_enseignante(path, VOICE)
    return True


def main():
    print("🔊 Mots isolés — Le son [ʃ] ou [ʒ] (module-pub)\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / "assets/interactive/module-pub/sons"
    out.mkdir(parents=True, exist_ok=True)

    ok = 0
    for file_id, text in CLIPS.items():
        spoken = TEXT_OVERRIDES.get(file_id, text)
        print(f"  {file_id:24s} « {spoken} » → ", end="", flush=True)
        if generate(api_key, spoken, out / f"{file_id}.mp3"):
            print("✓"); ok += 1
        else:
            print("✗")
    print(f"\n✅ {ok}/{len(CLIPS)} fichiers générés")


if __name__ == "__main__":
    main()
