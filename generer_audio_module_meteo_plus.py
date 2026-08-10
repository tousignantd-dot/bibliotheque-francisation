#!/usr/bin/env python3
"""
Générateur d'audio — boutons d'écoute des mini-leçons « En apprendre plus »
du module « module-meteo ».

fileId → texte lu ; doit correspondre aux appels playWord() générés par
plAudioId() dans le HTML. Pour régénérer cette liste après une modification de
l'objet PLUS : ouvrir le module dans le navigateur et lancer plAudioManifest()
dans la console — elle renvoie exactement ce dictionnaire.

Voix unique (enseignante) — même voix que les mots isolés des autres modules.
"""
import os, sys, time
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ pip install requests"); sys.exit(1)

VOICE = "K7gx0ylJdff0yjM2uVQS"

CLIPS = {
    "plus_prPhon_ana1": "table",
    "plus_prPhon_lab2_t": "table",
    "plus_prPhon_lab2_c": "chapitre",
    "plus_prPhon_lab2_a": "acceptable",
    "plus_prPhon_lab2_h": "théâtre",
    "plus_prPhon_ex3_0": "possible",
    "plus_prPhon_ex3_1": "autre",
    "plus_prPhon_ex3_2": "quatre",
    "plus_prPhon_ex3_3": "membre",
    "plus_prPhon_ex3_4": "exemple",
    "plus_t1prep_ana1": "il y a cinq semaines, voilà cinq semaines",
    "plus_t1prep_lab2_p": "Le soleil brillera pendant toute la fin de semaine",
    "plus_t1prep_lab2_e": "Le ciel se dégage en après-midi",
    "plus_t1prep_lab2_i": "Il a neigé il y a deux jours",
    "plus_t1prep_ex3_0": "Le soleil brillera pendant toute la fin de semaine.",
    "plus_t1prep_ex3_1": "Je pars en vacances en novembre.",
    "plus_t1prep_ex3_2": "Farida est sortie de l'hôpital voilà cinq semaines.",
    "plus_t2ci_ana1": "Je lui parle",
    "plus_t2ci_lab2_l": "Je lui parle",
    "plus_t2ci_lab2_e": "Je leur fais confiance",
    "plus_t2ci_lab2_s": "Je compte sur lui",
    "plus_t2ci_ex3_0": "Amina fait confiance à elle pour ses conseils.",
    "plus_t2ci_ex3_1": "Karim parle avec eux pendant la fin de semaine.",
    "plus_t2ci_ex3_2": "Je me fie à eux.",
    "plus_t2condition_ana1": "si la météo le permet, nous irons marcher",
    "plus_t2condition_lab2_b": "S'il fait beau, j'irai marcher",
    "plus_t2condition_lab2_n": "S'il neige beaucoup, reste à la maison",
    "plus_t2condition_lab2_f": "Tu prendras une journée de congé si la météo est belle",
    "plus_t2condition_ex3_0": "S'il fait froid, apporte un chandail.",
    "plus_t2condition_ex3_1": "Tu prendras une journée de congé si la météo est belle.",
    "plus_t2condition_ex3_2": "J'irai marcher s'il fait beau.",
    "plus_t2futcond_ana1": "je porterai, je porterais",
    "plus_t2futcond_lab2_f": "Demain, je porterai un manteau chaud",
    "plus_t2futcond_lab2_c": "J'irais marcher si le soleil brille",
    "plus_t2futcond_ex3_0": "Je serai là samedi, c'est certain.",
    "plus_t2futcond_ex3_1": "J'arriverais vers 15 h si la circulation le permet.",
    "plus_t2futcond_ex3_2": "J'irais à la plage si le soleil brille.",
}

# Les mots isolés du bloc « ana » de prPhon (table, chapitre, théâtre…)
# illustrent la prononciation relâchée elle-même : lus seuls, sans article,
# c'est justement le point pédagogique (montrer le mot tel qu'on l'entend).
# Pas de TEXT_OVERRIDES ici : contrairement aux mots-tests de discrimination
# de son, l'absence de contexte ne nuit pas au sens de la leçon.
TEXT_OVERRIDES = {}


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
    return True


def main():
    print(f"🔊 Mini-leçons « En apprendre plus » — {len(CLIPS)} extraits\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / "assets/interactive/module-meteo/sons"
    out.mkdir(parents=True, exist_ok=True)

    force = "--force" in sys.argv
    only = []
    for i, a in enumerate(sys.argv):
        if a == "--only" and i + 1 < len(sys.argv):
            only = [x.strip() for x in sys.argv[i + 1].split(",") if x.strip()]

    ok = skip = fail = 0
    for file_id, text in CLIPS.items():
        if only and not any(file_id.startswith(o) for o in only):
            continue
        dest = out / f"{file_id}.mp3"
        if dest.exists() and not force and not only:
            skip += 1
            continue
        spoken = TEXT_OVERRIDES.get(file_id, text)
        print(f"  {file_id:26s} « {spoken[:44]} » → ", end="", flush=True)
        if generate(api_key, spoken, dest):
            print("✓"); ok += 1
        else:
            print("✗"); fail += 1
        time.sleep(0.35)

    print(f"\n✅ {ok} générés · {skip} déjà présents · {fail} en échec")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
