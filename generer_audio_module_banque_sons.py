#!/usr/bin/env python3
"""
Générateur d'audio — mots isolés du module « Besoin d'un compte bancaire ? ».
fileId → texte lu ; doit correspondre aux appels playWord() du HTML.
Voix unique (enseignante) pour tous les mots : c'est un modèle de
prononciation, pas un dialogue.
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
    # Tableau savoir (prPhon) — PHRASE PORTEUSE complète (CARRIER_PHRASES du
    # HTML), pas le mot seul : un mot isolé ne donne aucun indice de langue
    # au moteur — voir TEXT_OVERRIDES plus bas pour le détail du problème.
    "prPhon_savoir_0_0": "Le dépôt entre dans le compte.",
    "prPhon_savoir_0_1": "Mon compte épargne rapporte un peu.",
    "prPhon_savoir_0_2": "Elle range son chéquier dans un tiroir.",
    "prPhon_savoir_1_0": "Je dépose un chèque au guichet.",
    "prPhon_savoir_1_1": "La caisse ouvre à neuf heures.",
    "prPhon_savoir_1_2": "Le guichet automatique est à l'entrée.",
    "prPhon_savoir_2_0": "Le retrait est de quarante dollars.",
    "prPhon_savoir_2_1": "Son relevé arrive le premier du mois.",
    "prPhon_savoir_2_2": "Il travaille cinq jours par semaine.",
    # Exercice 2 — mots à écouter (cartes)
    "prPhon_pha": "dépôt",
    "prPhon_phb": "chèque",
    "prPhon_phc": "épargne",
    "prPhon_phd": "guichet",
    "prPhon_phe": "chéquier",
    "prPhon_phf": "billet",
    "prPhon_phg": "vérifier",
    "prPhon_phh": "caisse",
}

# Un mot seul, sans contexte, ne donne au moteur aucun indice de langue —
# « dent » ou « table » se sont fait lire en anglais ou en espagnol sur
# d'autres modules. Un déterminant suffit à lever l'ambiguïté sans donner
# d'indice sur la réponse.
#
# Ici l'exercice teste [e] contre [ɛ] : « le » se dit [lə], un schwa, donc il
# n'introduit aucun des deux sons jugés. Pour « vérifier », qui est un verbe,
# « il faut » joue le même rôle — et le mot testé reste en fin de phrase.
TEXT_OVERRIDES = {
    "prPhon_pha": "le dépôt",
    "prPhon_phb": "le chèque",
    "prPhon_phc": "l'épargne",
    "prPhon_phd": "le guichet",
    "prPhon_phe": "le chéquier",
    "prPhon_phf": "le billet",
    "prPhon_phg": "il faut vérifier",
    "prPhon_phh": "la caisse",
}

manque = [k for k, v in CLIPS.items()
          if len(v.split()) <= 2 and k not in TEXT_OVERRIDES]
if manque:
    print("❌ mots isolés sans déterminant :", ", ".join(manque))
    sys.exit(1)


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
    print("🔊 Mots isolés — Besoin d'un compte bancaire ?\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / "assets/interactive/module-banque/sons"
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
