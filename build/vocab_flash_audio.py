#!/usr/bin/env python3
"""
Générateur d'audio des activités « Flash vocabulaire ».

Trois clips par mot — le mot, la définition, l'exemple — déposés dans
`assets/interactive/vocab-flash-<thème>/audio/`, aux noms que mots.json
attend déjà (`<slug>-mot.mp3`, `-definition.mp3`, `-exemple.mp3`).

Voix unique : l'enseignante. Ces clips sont un modèle de prononciation,
pas un dialogue ; ils passent donc par le ralentissement maison de
voix_lente (le paramètre `speed` d'ElevenLabs est sans effet sur
eleven_multilingual_v2).

Un mot lu seul ne donne au moteur aucun indice de langue : il ressort avec
un accent anglais. Les termes qui portent déjà un déterminant s'en tirent ;
les autres reçoivent ici le plus court contexte français possible, sans
jamais changer la forme enseignée (DITS ci-dessous).
"""
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ pip install requests"); sys.exit(1)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from voix_lente import ralentir_si_enseignante  # noqa: E402

RACINE = Path(__file__).resolve().parent.parent
VOICE = "K7gx0ylJdff0yjM2uVQS"   # 👩 enseignante
THEMES = ("conso", "sante")

# slug → ce qui est réellement lu pour le clip « mot ».
# Uniquement pour les termes sans déterminant : adjectifs et verbes.
DITS = {
    "fraiches": "très fraîches",
    "tousser": "tousser beaucoup",
    "empirer": "laisser empirer",
}


def generer(api_key, texte, chemin):
    r = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}",
        json={"text": texte, "model_id": "eleven_multilingual_v2",
              "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}},
        headers={"xi-api-key": api_key, "Content-Type": "application/json"},
        timeout=45)
    if r.status_code != 200:
        print(f"   ❌ {r.status_code}: {r.text[:150]}")
        return False
    chemin.write_bytes(r.content)
    ralentir_si_enseignante(chemin, VOICE)
    return True


def main():
    import json
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente"); sys.exit(1)

    themes = sys.argv[1:] or list(THEMES)
    total = ok = 0
    for theme in themes:
        dossier = RACINE / "assets/interactive" / f"vocab-flash-{theme}"
        mots = json.loads((dossier / "mots.json").read_text(encoding="utf-8"))
        sortie = dossier / "audio"
        sortie.mkdir(parents=True, exist_ok=True)
        print(f"\n🔊 Flash vocabulaire — {theme} ({len(mots)} mots)\n")
        for mot in mots:
            slug = mot["slug"]
            clips = {
                "mot": DITS.get(slug, mot["term"]),
                "definition": mot["definition"],
                "exemple": mot["example"],
            }
            for cle, texte in clips.items():
                total += 1
                print(f"  {slug}-{cle:11s} « {texte[:48]} » → ", end="", flush=True)
                if generer(api_key, texte, sortie / f"{slug}-{cle}.mp3"):
                    print("✓"); ok += 1
                else:
                    print("✗")
    print(f"\n✅ {ok}/{total} fichiers générés")


if __name__ == "__main__":
    main()
