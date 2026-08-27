#!/usr/bin/env python3
"""
Générateur d'audio — mots isolés du module « Quelle est la procédure ? ».
fileId → texte lu ; doit correspondre aux appels playWord() du HTML.
Voix unique (enseignante) pour tous les mots : c'est un modèle de
prononciation, pas un dialogue.
"""
import os, sys
from pathlib import Path

import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))

VOICE = "mActWQg9kibLro6Z2ouY"   # 👩 enseignante

CLIPS = {
    # Tableau savoir (prPhon) — PHRASE PORTEUSE complète (CARRIER_PHRASES du
    # HTML), pas le mot seul : un mot isolé ne donne aucun indice de langue
    # au moteur — voir TEXT_OVERRIDES plus bas pour le détail du problème.
    "prPhon_savoir_0_0": "Il faut soumettre la demande aujourd'hui.",
    "prPhon_savoir_0_1": "Le bris s'est produit pendant la nuit.",
    "prPhon_savoir_1_0": "La formation a lieu en juillet.",
    "prPhon_savoir_1_1": "Le voyant orangé signale un bris.",
    "prPhon_savoir_1_2": "N'oubliez pas de joindre votre reçu.",
    "prPhon_savoir_2_0": "Elle fait ça pour gagner du temps.",
    "prPhon_savoir_2_1": "Remplissez chaque ligne du formulaire.",
    "prPhon_savoir_2_2": "La demande attend votre signature.",
    # Exercice 2 — mots à écouter (cartes)
    "prPhon_pha": "aujourd'hui",
    "prPhon_phb": "nuit",
    "prPhon_phc": "juillet",
    "prPhon_phd": "orangé",
    "prPhon_phe": "joindre",
    "prPhon_phf": "gagner",
    "prPhon_phg": "ligne",
    "prPhon_phh": "signature",
}

# Un mot seul, sans contexte, ne donne au moteur aucun indice de langue —
# « dent » ou « consultation » se sont fait lire en anglais ou en espagnol
# sur d'autres modules. Un déterminant ou une préposition idiomatique (le/la,
# jamais un/une : « un » se prononce lui-même comme une voyelle nasale) suffit
# à lever l'ambiguïté sans donner d'indice sur la réponse.
TEXT_OVERRIDES = {
    "prPhon_pha": "dès aujourd'hui",
    "prPhon_phb": "la nuit",
    "prPhon_phc": "en juillet",
    "prPhon_phd": "plutôt orangé",
    "prPhon_phe": "à joindre",
    "prPhon_phf": "pour gagner",
    "prPhon_phg": "la ligne",
    "prPhon_phh": "la signature",
}


# L'audio du cours vient d'Azure Speech depuis le 26 août 2026. La fonction
# ci-dessous garde son nom et sa signature — `main()` l'appelle telle quelle —
# mais délègue. La clé ElevenLabs et le contexte `avant`/`apres` sont acceptés
# et ignorés : le `xml:lang="fr-CA"` du SSML rend ce dernier inutile.
from azure_voix import parle_compat  # noqa: E402


def generate(api_key, text, path):
    return parle_compat(api_key, text, VOICE, path)
def main():
    print("🔊 Mots isolés — Quelle est la procédure ?\n")
    api_key = os.environ.get("AZURE_SPEECH_KEY", "").strip()
    if not api_key:
        print("❌ AZURE_SPEECH_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / "assets/interactive/module-procedure/sons"
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
