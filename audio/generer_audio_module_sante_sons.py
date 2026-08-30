#!/usr/bin/env python3
"""
Générateur d'audio — mots isolés de l'exercice « Le son [ɑ̃] ou [ɛ̃] » (module-sante).
fileId → texte lu ; doit correspondre aux appels playWord() du HTML.
Voix unique (enseignante) : c'est un modèle de prononciation, pas un dialogue.
"""
import os, sys
from pathlib import Path

import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))

VOICE = "mActWQg9kibLro6Z2ouY"   # 👩 enseignante

CLIPS = {
    # Bandeau « Des sons et des lettres » : on lit la PHRASE PORTEUSE
    # (CARRIER_PHRASES dans le HTML), jamais le mot seul.
    "prSons_savoir_0_0": "La salle d'attente est pleine ce matin.",
    "prSons_savoir_0_1": "Prenez le comprimé pendant sept jours.",
    "prSons_savoir_0_2": "Le médecin me donne une ordonnance.",
    "prSons_savoir_1_0": "Le médecin vous recevra à onze heures.",
    "prSons_savoir_1_1": "Le pharmacien explique la posologie.",
    "prSons_savoir_1_2": "Un comprimé le matin, avant le repas.",
    "prSons_savoir_2_0": "Je me sens bien mieux depuis hier.",
    # Cartes de l'exercice — un mot par carte.
    "prSons_psa": "attente",
    "prSons_psb": "pharmacien",
    "prSons_psc": "ordonnance",
    "prSons_psd": "médecin",
    "prSons_pse": "traitement",
    "prSons_psf": "matin",
    "prSons_psg": "pendant",
    "prSons_psh": "bien",
}

# Un mot seul ne donne au moteur aucun indice de langue et se fait lire à
# l'anglaise. On ajoute le plus court contexte possible. Le contexte ne doit
# jamais contenir le son testé, sinon il souffle la réponse : d'où « le / la »
# plutôt que « un / une » dans les exercices sur les voyelles nasales, et
# jamais « les » dans celui qui oppose [e] et [ɛ].
TEXT_OVERRIDES = {
    "prSons_psa": "l'attente",
    "prSons_psb": "le pharmacien",
    "prSons_psc": "l'ordonnance",
    "prSons_psd": "le médecin",
    "prSons_pse": "le traitement",
    "prSons_psf": "le matin",
    "prSons_psg": "pendant sept jours",
    "prSons_psh": "très bien",
}


# L'audio du cours vient d'Azure Speech depuis le 26 août 2026. La fonction
# ci-dessous garde son nom et sa signature — `main()` l'appelle telle quelle —
# mais délègue. La clé ElevenLabs et le contexte `avant`/`apres` sont acceptés
# et ignorés : le `xml:lang="fr-CA"` du SSML rend ce dernier inutile.
from azure_voix import parle_compat  # noqa: E402


def generate(api_key, text, path):
    return parle_compat(api_key, text, VOICE, path)
def main():
    print("🔊 Mots isolés — Le son [ɑ̃] ou [ɛ̃] (module-sante)\n")
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
        print("❌ AZURE_SPEECH_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / "assets/interactive/module-sante/sons"
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
