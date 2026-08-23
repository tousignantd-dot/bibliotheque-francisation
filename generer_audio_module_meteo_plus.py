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

from voix_lente import ralentir_si_enseignante
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés

VOICE = "mActWQg9kibLro6Z2ouY"

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
    "plus_t1prep_ana1": "il y a deux ans, voilà deux ans",
    "plus_t1prep_lab2_p": "Les rafales ont soufflé pendant toute la nuit",
    "plus_t1prep_lab2_e": "L'atelier ferme en juillet",
    "plus_t1prep_lab2_i": "Le verglas a coupé le courant il y a trois jours",
    "plus_t1prep_ex3_0": "Les rafales ont soufflé pendant toute la nuit.",
    "plus_t1prep_ex3_1": "L'atelier ferme en juillet.",
    "plus_t1prep_ex3_2": "Diego a commencé son apprentissage voilà deux ans.",
    "plus_t2ci_ana1": "Je lui parle",
    "plus_t2ci_lab2_l": "Je lui parle",
    "plus_t2ci_lab2_e": "Je leur fais confiance",
    "plus_t2ci_lab2_s": "Je compte sur lui",
    "plus_t2ci_ex3_0": "Diego compte sur elle pour la sécurité de l'équipe.",
    "plus_t2ci_ex3_1": "Prisca part avec eux en camionnette.",
    "plus_t2ci_ex3_2": "Je me fie à eux.",
    "plus_t2condition_ana1": "si le vent tombe, nous poserons la membrane",
    "plus_t2condition_lab2_b": "S'il fait beau, nous monterons sur le toit",
    "plus_t2condition_lab2_n": "S'il tombe du verglas, reste à l'atelier",
    "plus_t2condition_lab2_f": "Prisca prendra la route si la visibilité s'améliore",
    "plus_t2condition_ex3_0": "S'il commence à grésiller, descends de l'échelle.",
    "plus_t2condition_ex3_1": "Prisca prendra la route si la visibilité s'améliore.",
    "plus_t2condition_ex3_2": "Nous monterons sur le toit s'il fait beau.",
    "plus_t2futcond_ana1": "je porterai, je porterais",
    "plus_t2futcond_lab2_f": "Lundi, je commencerai la toiture du garage",
    "plus_t2futcond_lab2_c": "Je partirais plus tôt si la poudrerie le permet",
    "plus_t2futcond_ex3_0": "Je finirai le rapport avant midi, c'est certain.",
    "plus_t2futcond_ex3_1": "Je partirais plus tôt si la poudrerie le permet.",
    "plus_t2futcond_ex3_2": "Je prendrais l'autoroute 10 si la visibilité s'améliorait.",
}

# Un mot seul ne donne au moteur aucun indice de langue — voir
# phase2-audio.md du skill module-parite. Ces mots-là (« table », « autre »,
# « membre »…) se faisaient lire en anglais ou en espagnol : signalé par
# l'utilisateur le 2026-08-10, après qu'un commentaire de ce script eut
# affirmé à tort qu'ils n'en avaient pas besoin.
#
# Déterminant le/la/l', jamais un/une (nasal). Le mot testé reste TOUJOURS
# en fin de phrase : c'est là que la consonne finale s'efface, et c'est tout
# le point de la leçon. Pour les adjectifs et les nombres, « c'est… » ou
# « il y en a… » jouent le rôle du déterminant.
#
# Le mot affiché à l'élève ne change pas — seul le texte envoyé à l'API.
TEXT_OVERRIDES = {
    "plus_prPhon_ana1": "la table",
    "plus_prPhon_lab2_t": "la table",
    "plus_prPhon_lab2_c": "le chapitre",
    "plus_prPhon_lab2_a": "c'est acceptable",
    "plus_prPhon_lab2_h": "le théâtre",
    "plus_prPhon_ex3_0": "c'est possible",
    "plus_prPhon_ex3_1": "l'autre",
    "plus_prPhon_ex3_2": "il y en a quatre",
    "plus_prPhon_ex3_3": "le membre",
    "plus_prPhon_ex3_4": "l'exemple",
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
