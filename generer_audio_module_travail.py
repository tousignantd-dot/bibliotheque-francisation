#!/usr/bin/env python3
"""
Générateur d'audio — Module « C'est une absence ou un retard ? » (Monde du travail)
Exécute ce script et rentre ta clé API quand demandé.
"""

import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ requests n'est pas installé. Installe-le :")
    print("   pip install requests")
    sys.exit(1)

# ── VOICES ────────────────────────────────────────────────────────────
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))

VOICES = {
    "enseignante": "mActWQg9kibLro6Z2ouY",      # 👩 Féminine #1
    "feminin_2": "WW0JfNPk5DgcQdM0d6X6",        # 👩 Féminine #2
    "masculin_1": "93nuHbke4dTER9x2pDwE",       # 👨 Masculin #1
    "narrateur": "IPgYtHTNLjC7Bq7IPHrm",        # 👨 Narrateur
}

# Chaque personnage doit avoir une voix distincte de son ou sa
# partenaire de dialogue, pour qu'on puisse reconnaître qui parle
# sans jamais entendre le nom du personnage à voix haute.
VOICE_ASSOC = {
    "KARIM": "masculin_1",
    "NADIA": "feminin_2",
    "FARIDA": "enseignante",
    "SECRETAIRE": "feminin_2",
    "OMAR": "masculin_1",
    "EMPLOYEUSE": "enseignante",
    "AZIZ": "narrateur",
}

# ── DIALOGUES ─────────────────────────────────────────────────────────
DIALOGUES = {
    "module-travail/prep": {
        "title": "C'est une absence ou un retard — Je découvre (Un départ précipité)",
        "lines": [
            ("KARIM", "Nadia, je viens de recevoir un appel de l'école. Ma fille Sarah a de la fièvre, je dois aller la chercher tout de suite. Mais c'est déjà ma deuxième absence ce mois-ci… j'ai peur que mon superviseur soit fâché."),
            ("NADIA", "Ne t'inquiète pas, la santé de ta fille passe avant tout. L'important, c'est de prévenir ton superviseur tout de suite, avant de partir, pas après."),
            ("KARIM", "Tu as raison. Mais qu'est-ce que je dis si on me demande pourquoi c'est déjà la deuxième fois ce mois-ci ?"),
            ("NADIA", "Explique la situation calmement, sans t'excuser trop longtemps, et propose de reprendre les heures manquées plus tard dans la semaine. Ça montre ta bonne volonté."),
            ("KARIM", "D'accord, je l'appelle maintenant. Merci pour le conseil, Nadia."),
        ]
    },
    "module-travail/t1": {
        "title": "C'est une absence ou un retard — Défi 1 (Boîte vocale de Farida)",
        "lines": [
            ("FARIDA", "Bonjour, c'est Farida. Je vous appelle parce que j'ai un rendez-vous à l'hôpital avec le spécialiste de ma fille, le docteur Bernard, orthopédiste."),
            ("FARIDA", "Le rendez-vous est à 9 h 30 demain matin. Ma fille s'est blessée au bras la semaine dernière, et je dois apporter une preuve pour justifier mon absence au cours de francisation."),
            ("FARIDA", "La consultation devrait durer environ 45 minutes. Je devrais être de retour au centre de formation vers 10 h 15. Merci de votre compréhension."),
        ]
    },
    "module-travail/dial1": {
        "title": "C'est une absence ou un retard — Exercice 4 (Un changement d'horaire)",
        "lines": [
            ("SECRETAIRE", "Bonjour, centre de formation, je vous écoute."),
            ("OMAR", "Bonjour, j'aimerais savoir s'il est possible de changer mon horaire de cours."),
            ("SECRETAIRE", "Oui, c'est possible. Vous devez seulement apporter une preuve d'emploi et remplir un formulaire signé."),
            ("OMAR", "D'accord, et la nouvelle grille horaire s'applique à partir de quand ?"),
            ("SECRETAIRE", "Dès le mois prochain."),
        ]
    },
    "module-travail/dial2": {
        "title": "C'est une absence ou un retard — Exercice 5 (Une confirmation de poste)",
        "lines": [
            ("EMPLOYEUSE", "Bonjour, je vous appelle pour confirmer votre entrevue pour le poste d'aide-cuisinier."),
            ("AZIZ", "Ah oui, parfait, merci de me rappeler."),
            ("EMPLOYEUSE", "Est-ce que quinze heures cet après-midi vous convient ?"),
            ("AZIZ", "Oui, tout à fait, je serai là."),
            ("EMPLOYEUSE", "Très bien, à tout à l'heure."),
        ]
    },
}


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
    print("🎙️  Générateur d'audio — Module C'est une absence ou un retard ?\n")

    api_key = os.environ.get("AZURE_SPEECH_KEY", "").strip()
    if not api_key:
        api_key = input("Colle ta clé ElevenLabs : ").strip()
        if not api_key:
            print("❌ Clé API requise")
            sys.exit(1)

    base_dir = Path("/Users/danieltousignant/Claude/bibliotheque-francisation/assets/interactive")

    total = 0
    success = 0

    for dial_id, dial_data in DIALOGUES.items():
        print(f"\n📖 {dial_data['title']}")
        dir_path = base_dir / dial_id
        dir_path.mkdir(parents=True, exist_ok=True)

        for i, (character, text) in enumerate(dial_data["lines"], 1):
            # La réplique d'avant et celle d'après partent avec
            # l'extrait, en `previous_text` / `next_text` : du français qui
            # conditionne la synthèse sans être prononcé.
            avant = dial_data["lines"][i - 2][1] if i >= 2 else None
            apres = (dial_data["lines"][i][1]
                     if i < len(dial_data["lines"]) else None)
            voice_name = VOICE_ASSOC.get(character, "feminin_2")
            voice_id = VOICES[voice_name]
            filename = f"line_{i:02d}_{character.lower().replace(' ', '_').replace(chr(39), '')}.mp3"
            output_path = dir_path / filename

            print(f"  {i:2d}. {character[:20]:20s} → ", end="", flush=True)
            total += 1

            if generate_audio(api_key, text, voice_id, output_path,
                              avant, apres):
                print(f"✓ {filename}")
                success += 1
            else:
                print(f"✗ {filename}")

    print(f"\n{'='*60}")
    print(f"✅ {success}/{total} fichiers générés")


if __name__ == "__main__":
    main()
