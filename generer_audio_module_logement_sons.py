#!/usr/bin/env python3
"""
Générateur d'audio — mots isolés de l'exercice « Le son [ɑ̃] ou [ɔ̃] » (module-logement).
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

VOICE = "K7gx0ylJdff0yjM2uVQS"   # 👩 enseignante

CLIPS = {
    # Bandeau « Des sons et des lettres » : on lit la PHRASE PORTEUSE
    # (CARRIER_PHRASES dans le HTML), jamais le mot seul.
    "prSons_savoir_0_0": "Le logement est chauffé et éclairé.",
    "prSons_savoir_0_1": "La chambre donne sur la cour.",
    "prSons_savoir_0_2": "Le bail commence le premier septembre.",
    "prSons_savoir_1_0": "Le salon est petit mais lumineux.",
    "prSons_savoir_1_1": "Le camion de farine arrive très tôt.",
    "prSons_savoir_1_2": "La maison a une buanderie au sous-sol.",
    # Cartes de l'exercice — un mot par carte.
    "prSons_psa": "logement",
    "prSons_psb": "salon",
    "prSons_psc": "chambre",
    "prSons_psd": "camion",
    "prSons_pse": "buanderie",
    "prSons_psf": "maison",
    "prSons_psg": "septembre",
    "prSons_psh": "répondu",
}

# Un mot seul ne donne au moteur aucun indice de langue et se fait lire à
# l'anglaise. On ajoute le plus court contexte possible. Le contexte ne doit
# jamais contenir le son testé, sinon il souffle la réponse : d'où « le / la »
# plutôt que « un / une » dans les exercices sur les voyelles nasales, et
# jamais « les » dans celui qui oppose [e] et [ɛ].
TEXT_OVERRIDES = {
    "prSons_psa": "le logement",
    "prSons_psb": "le salon",
    "prSons_psc": "la chambre",
    "prSons_psd": "le camion",
    "prSons_pse": "la buanderie",
    "prSons_psf": "la maison",
    "prSons_psg": "le mois de septembre",
    "prSons_psh": "il a répondu",
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
    print("🔊 Mots isolés — Le son [ɑ̃] ou [ɔ̃] (module-logement)\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / "assets/interactive/module-logement/sons"
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
