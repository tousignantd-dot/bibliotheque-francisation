#!/usr/bin/env python3
"""
Générateur d'audio — Module « Une urgence au travail » (Santé)
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

from voix_lente import ralentir_si_enseignante
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés

VOICES = {
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 Féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 Féminine #2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 Masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 Narrateur
}

# Chaque personnage a une voix distincte de son interlocuteur, pour qu'on
# reconnaisse qui parle sans jamais entendre le nom du personnage.
VOICE_ASSOC = {
    "FATOU":              "feminin_2",
    "MATHIEU":             "masculin_1",
    "L'INFIRMIÈRE":        "enseignante",
    "L'URGENTOLOGUE":      "narrateur",
    "AMINATA":             "enseignante",
    "LA RÉCEPTIONNISTE":   "feminin_2",
}

DIALOGUES = {
    "module-urgence/prep": {
        "title": "Une urgence au travail — Je découvre (Une brûlure en cuisine)",
        "lines": [
            ("FATOU", "Mathieu ! L'huile a éclaboussé, je me suis brûlé l'avant-bras."),
            ("MATHIEU", "Ne touche à rien. Viens à l'évier, on met ça sous l'eau froide tout de suite."),
            ("FATOU", "Ça chauffe beaucoup… et la peau devient rouge."),
            ("MATHIEU", "On laisse couler quinze minutes, c'est ce qu'il faut faire. Pendant ce temps, j'appelle Info-Santé au 811."),
            ("FATOU", "Pourquoi pas le 911 ?"),
            ("MATHIEU", "Le 911, c'est quand la vie est en danger. Là, une infirmière va nous dire quoi faire."),
            ("L'INFIRMIÈRE", "Info-Santé, bonjour. Décrivez-moi la brûlure."),
            ("MATHIEU", "Une brûlure à l'avant-bras avec de l'huile chaude. La peau est rouge et il y a de petites cloques."),
            ("L'INFIRMIÈRE", "Des cloques, c'est une brûlure du deuxième degré. Continuez l'eau froide, ne percez rien, et rendez-vous à l'urgence aujourd'hui."),
            ("FATOU", "D'accord, merci. J'y vais."),
        ],
    },
    "module-urgence/t1": {
        "title": "Une urgence au travail — Défi 1 (À l'urgence)",
        "lines": [
            ("L'URGENTOLOGUE", "Bonjour. Racontez-moi ce qui s'est passé."),
            ("FATOU", "Je travaillais en cuisine. L'huile a éclaboussé et je me suis brûlé l'avant-bras droit."),
            ("L'URGENTOLOGUE", "À quelle heure est-ce arrivé ?"),
            ("FATOU", "Vers onze heures. J'ai mis mon bras sous l'eau froide pendant quinze minutes."),
            ("L'URGENTOLOGUE", "Vous avez bien réagi. Est-ce que vous avez percé les cloques ?"),
            ("FATOU", "Non, l'infirmière d'Info-Santé m'a dit de ne pas y toucher."),
            ("L'URGENTOLOGUE", "Parfait. Je vais nettoyer la plaie et poser un pansement."),
        ],
    },
    "module-urgence/t2": {
        "title": "Une urgence au travail — Défi 2 (Les soins et le suivi)",
        "lines": [
            ("L'URGENTOLOGUE", "C'est une brûlure du deuxième degré, superficielle. Ce n'est pas dangereux."),
            ("FATOU", "Est-ce que je vais garder une cicatrice ?"),
            ("L'URGENTOLOGUE", "Probablement pas, si vous protégez la peau du soleil pendant six mois."),
            ("FATOU", "Est-ce que je peux retourner en cuisine demain ?"),
            ("L'URGENTOLOGUE", "Non. Je vous donne un congé de maladie de trois jours et une crème à appliquer deux fois par jour."),
            ("FATOU", "Et le pansement, je le change moi-même ?"),
            ("L'URGENTOLOGUE", "Vous le changez chaque matin. Si la douleur augmente ou si la plaie devient jaune, revenez nous voir."),
        ],
    },
    "module-urgence/t3": {
        "title": "Une urgence au travail — Défi 3 (À l'accueil de l'hôpital)",
        "lines": [
            ("AMINATA", "Bonjour, je viens chercher ma sœur. Elle est à l'urgence depuis ce matin."),
            ("LA RÉCEPTIONNISTE", "Pourriez-vous me donner son nom, s'il vous plaît ?"),
            ("AMINATA", "Fatou Diarra. Est-ce que je pourrais monter la rejoindre ?"),
            ("LA RÉCEPTIONNISTE", "Un accompagnateur à la fois, et seulement quand le personnel vous appelle."),
            ("AMINATA", "Auriez-vous un endroit où attendre ?"),
            ("LA RÉCEPTIONNISTE", "La salle d'attente est au fond du corridor, à droite, après l'ascenseur."),
            ("AMINATA", "Et pour le stationnement, est-ce que c'est payant ?"),
            ("LA RÉCEPTIONNISTE", "Oui, mais gardez votre billet : à l'urgence, les quatre premières heures sont gratuites."),
        ],
    },
}


def char_slug(name):
    """Doit correspondre exactement à charSlug() du HTML (accents retirés)."""
    s = unicodedata.normalize("NFD", name.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("'", "").replace(" ", "_")


def generate_audio(api_key, text, voice_id, output_path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
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
    print("🎙️  Générateur d'audio — Une urgence au travail\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente (source .env)")
        sys.exit(1)

    base_dir = Path(__file__).resolve().parent / "assets" / "interactive"
    total = success = 0

    for dial_id, data in DIALOGUES.items():
        print(f"\n📖 {data['title']}")
        dir_path = base_dir / dial_id
        dir_path.mkdir(parents=True, exist_ok=True)
        for i, (character, text) in enumerate(data["lines"], 1):
            voice_id = VOICES[VOICE_ASSOC.get(character, "feminin_2")]
            filename = f"line_{i:02d}_{char_slug(character)}.mp3"
            print(f"  {i:2d}. {character[:18]:18s} → ", end="", flush=True)
            total += 1
            if generate_audio(api_key, text, voice_id, dir_path / filename):
                print(f"✓ {filename}")
                success += 1
            else:
                print(f"✗ {filename}")

    print(f"\n{'='*60}\n✅ {success}/{total} fichiers générés")


if __name__ == "__main__":
    main()
