#!/usr/bin/env python3
"""
Générateur d'audio — mots isolés du module « Consulter au bon endroit ».
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
    # Tableau « Des sons et des lettres » (savoir de prPhon). On lit la
    # PHRASE PORTEUSE (CARRIER_PHRASES dans le HTML), pas le mot seul : un
    # mot isolé ne donne aucun indice de langue au moteur — voir le
    # commentaire de TEXT_OVERRIDES plus bas pour le détail du problème.
    "prPhon_savoir_0_0": "Le patient attend son tour.",
    "prPhon_savoir_0_1": "Ma jambe me fait mal.",
    "prPhon_savoir_0_2": "Le temps d'attente est long.",
    "prPhon_savoir_0_3": "J'ai une dent qui me fait souffrir.",
    "prPhon_savoir_1_0": "Le tendon est enflammé.",
    "prPhon_savoir_1_1": "Il a le front chaud.",
    "prPhon_savoir_1_2": "Écrivez votre nom ici.",
    "prPhon_savoir_2_0": "Je me suis blessé à la main.",
    "prPhon_savoir_2_1": "L'examen dure dix minutes.",
    "prPhon_savoir_2_2": "Le médecin arrive bientôt.",
    # Exercice 2 — mots à écouter (cartes)
    "prPhon_pha": "patient",
    "prPhon_phb": "tendon",
    "prPhon_phc": "jambe",
    "prPhon_phd": "front",
    "prPhon_phe": "temps",
    "prPhon_phf": "nom",
    "prPhon_phg": "dent",
    "prPhon_phh": "consultation",
}

# Un mot seul, sans contexte, ne donne au moteur aucun indice de langue —
# « dent » ou « consultation » se sont fait lire en anglais ou en espagnol
# (signalé 2026-08-10). Un déterminant (le/la, jamais un/une : « un » se
# prononce lui-même comme une voyelle nasale, ce qui brouillerait justement
# le son qu'on teste) suffit à lever l'ambiguïté sans donner d'indice sur
# la réponse — la voyelle testée est dans le nom, pas dans l'article.
# Plus fiable qu'une réorthographie phonétique : celle-ci ne garantit rien
# et a déjà échoué deux fois de suite sur « hiver » dans module-travail.
TEXT_OVERRIDES = {
    "prPhon_pha": "le patient",
    "prPhon_phb": "le tendon",
    "prPhon_phc": "la jambe",
    "prPhon_phd": "le front",
    "prPhon_phe": "le temps",
    "prPhon_phf": "le nom",
    "prPhon_phg": "la dent",
    "prPhon_phh": "la consultation",
}


# L'audio du cours vient d'Azure Speech depuis le 26 août 2026. La fonction
# ci-dessous garde son nom et sa signature — `main()` l'appelle telle quelle —
# mais délègue. La clé ElevenLabs et le contexte `avant`/`apres` sont acceptés
# et ignorés : le `xml:lang="fr-CA"` du SSML rend ce dernier inutile.
from azure_voix import parle_compat  # noqa: E402


def generate(api_key, text, path):
    return parle_compat(api_key, text, VOICE, path)
def main():
    print("🔊 Mots isolés — Consulter au bon endroit\n")
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

    out = Path(__file__).resolve().parent / "assets/interactive/module-consultation/sons"
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
