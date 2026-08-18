#!/usr/bin/env python3
"""
Générateur d'audio — mots isolés du module « Une urgence au travail ».
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

VOICE = "K7gx0ylJdff0yjM2uVQS"   # 👩 enseignante

CLIPS = {
    # Tableau « Des voyelles orales » (savoir de prPhon).
    # On lit la PHRASE PORTEUSE, pas le mot seul : c'est ce que la pastille
    # affiche à l'élève, et un mot isolé ne donne aucun indice de langue au
    # moteur — « urgence » et « minute » se faisaient lire à l'anglaise.
    "prPhon_savoir_0_0": "La brûlure est superficielle.",
    "prPhon_savoir_0_1": "Je vais à l'urgence.",
    "prPhon_savoir_0_2": "Attendez une minute.",
    "prPhon_savoir_0_3": "Le sucre est sur la table.",
    "prPhon_savoir_1_0": "La douleur augmente le soir.",
    "prPhon_savoir_1_1": "Il s'est coupé le pouce.",
    "prPhon_savoir_1_2": "La soupe est trop chaude.",
    "prPhon_savoir_1_3": "Merci pour ton soutien.",
    "prPhon_savoir_2_0": "Elle travaille en cuisine.",
    "prPhon_savoir_2_1": "L'infirmière arrive tout de suite.",
    # Exercice 5 — mots à écouter (cartes, [y] ou [u]).
    # Ceux-là doivent rester ISOLÉS : l'élève doit juger la voyelle sans
    # indice de contexte. Voir TEXT_OVERRIDES pour les cas problématiques.
    "prPhon_pha": "brûlure",
    "prPhon_phb": "douleur",
    "prPhon_phc": "urgence",
    "prPhon_phd": "pouce",
    "prPhon_phe": "minute",
    "prPhon_phf": "soupe",
    "prPhon_phg": "sucre",
    "prPhon_phh": "soutien",
}

# Réécriture « à la française » quand ElevenLabs lit un mot isolé à l'anglaise.
# Le modèle eleven_multilingual_v2 n'accepte ni les balises <phoneme> IPA
# (réservées à eleven_flash_v2, anglais seulement) ni le paramètre language_code.
# Le seul levier est donc l'orthographe : on écrit le mot d'une façon qui
# n'existe pas en anglais, ce qui force une lecture française.
#   urgence [yʁʒɑ̃s]  →  urjance
#   minute  [minyt]   →  minutte
TEXT_OVERRIDES = {
    "prPhon_phc": "urjance",
    "prPhon_phe": "minutte",
}


def generate(api_key, text, path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}"
    payload = {"text": text, "model_id": "eleven_multilingual_v2",
               "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
    r = requests.post(url, json=payload,
                      headers={"xi-api-key": api_key, "Content-Type": "application/json"},
                      timeout=45)
    if r.status_code != 200:
        print(f"   ❌ {r.status_code}: {r.text[:150]}")
        return False
    path.write_bytes(r.content)
    ralentir_si_enseignante(path, VOICE)
    return True


def main():
    print("🔊 Mots isolés — Une urgence au travail\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / "assets/interactive/module-urgence/sons"
    out.mkdir(parents=True, exist_ok=True)

    # --only pref1,pref2 : ne régénère que les identifiants correspondants,
    # pour corriger un fichier fautif sans repayer tous les autres.
    only = []
    for i, a in enumerate(sys.argv):
        if a == "--only" and i + 1 < len(sys.argv):
            only = [x.strip() for x in sys.argv[i + 1].split(",") if x.strip()]

    force = "--force" in sys.argv

    ok = skip = 0
    for file_id, text in CLIPS.items():
        if only and not any(file_id.startswith(o) for o in only):
            continue
        dest = out / f"{file_id}.mp3"
        if dest.exists() and not force and not only:
            skip += 1
            continue
        spoken = TEXT_OVERRIDES.get(file_id, text)
        print(f"  {file_id:24s} « {spoken} » → ", end="", flush=True)
        if generate(api_key, spoken, dest):
            print("✓"); ok += 1
        else:
            print("✗")
    print(f"\n✅ {ok} générés · {skip} déjà présents")


if __name__ == "__main__":
    main()
