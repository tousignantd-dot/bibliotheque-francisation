#!/usr/bin/env python3
"""
Générateur d'audio — boutons d'écoute des mini-leçons « Ouvrir la mini-leçon »
du module « module-nouvelles ».

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
    "plus_prClass_lab1_fd": "Un orignal traverse la route principale du village",
    "plus_prClass_lab1_nr": "Une nouvelle patinoire ouvre à Longueuil",
    "plus_prClass_lab1_nn": "Le prix de l'essence augmente partout au pays",
    "plus_prClass_lab1_ni": "Un séisme frappe le sud de l'Italie",
    "plus_prClass_ex2_0": "Un cycliste entre en collision avec un chevreuil.",
    "plus_prClass_ex2_1": "Une nouvelle piste cyclable aménagée à Alma.",
    "plus_prClass_ex2_2": "L'endettement des ménages canadiens augmente.",
    "plus_prClass_ex2_3": "Des feux de forêt forcent une évacuation en Australie.",
    "plus_prMarq_ana1": "avant-hier, après-demain",
    "plus_prMarq_lab2_pa": "La collecte a eu lieu avant-hier",
    "plus_prMarq_lab2_pr": "La collecte se déroule en ce moment",
    "plus_prMarq_lab2_fu": "La prochaine collecte aura lieu dans une semaine",
    "plus_prMarq_ex3_0": "hier, la semaine dernière, il y a trois jours",
    "plus_prMarq_ex3_1": "maintenant, en ce moment, présentement",
    "plus_prMarq_ex3_2": "demain, bientôt, dans une semaine",
    "plus_t1souligne_ana1": "C'est Noah qui a eu l'idée",
    "plus_t1souligne_lab2_n": "C'est Noah qui a eu l'idée",
    "plus_t1souligne_lab2_v": "C'est la voisine qui a reconnu le chat",
    "plus_t1souligne_lab2_h": "C'est hier matin que la voisine a vu le chat",
    "plus_t1souligne_ex3_0": "C'est cette voisine qui a reconnu le chat.",
    "plus_t1souligne_ex3_1": "Ce sont les élèves qui ont fabriqué les affiches.",
    "plus_t1souligne_ex3_2": "C'est hier matin que la voisine a vu le chat.",
    "plus_t1passive_ana1": "a été retrouvé par une fillette",
    "plus_t1passive_lab2_c": "Le chat a été retrouvé par une fillette",
    "plus_t1passive_lab2_m": "Les mitaines ont été amassées par les élèves",
    "plus_t1passive_lab2_s": "La sculpture a été admirée par des centaines de curieux",
    "plus_t1passive_ex3_0": "Le prix a été remis à l'équipe gagnante.",
    "plus_t1passive_ex3_1": "L'affiche a été fabriquée par la classe.",
    "plus_t1passive_ex3_2": "Le documentaire a été présenté devant toute école.",
    "plus_t2etre_ana1": "j'étais",
    "plus_t2etre_lab2_je": "j'étais curieux",
    "plus_t2etre_lab2_nous": "nous étions curieux",
    "plus_t2etre_lab2_ils": "ils étaient curieux",
    "plus_t2etre_ex3_0": "j'étais",
    "plus_t2etre_ex3_1": "tu étais",
    "plus_t2etre_ex3_2": "il était",
    "plus_t2etre_ex3_3": "nous étions",
    "plus_t2etre_ex3_4": "vous étiez",
    "plus_t2etre_ex3_5": "ils étaient",
    "plus_t2accord_ana1": "elle est sortie",
    "plus_t2accord_lab2_m": "Il est arrivé",
    "plus_t2accord_lab2_f": "Elle est arrivée",
    "plus_t2accord_lab2_mp": "Ils sont arrivés",
    "plus_t2accord_lab2_fp": "Elles sont arrivées",
    "plus_t2accord_ex3_0": "Les élèves sont arrivés tôt.",
    "plus_t2accord_ex3_1": "La fillette est sortie chercher son chat.",
    "plus_t2accord_ex3_2": "L'équipe gagnante est revenue chercher son trophée.",
    "plus_t2accord_ex3_3": "Les visiteurs sont restés jusqu'au soir.",
    "plus_t2auxiliaire_ana1": "a décidé, est venue",
    "plus_t2auxiliaire_lab2_d": "Les élèves ont décidé",
    "plus_t2auxiliaire_lab2_v": "Une journaliste est venue",
    "plus_t2auxiliaire_lab2_r": "Les organisateurs sont restés",
    "plus_t2auxiliaire_lab2_a": "Les élèves ont amassé",
    "plus_t2auxiliaire_ex3_0": "Les élèves ont décidé d'organiser une collecte.",
    "plus_t2auxiliaire_ex3_1": "Elle est arrivée en retard au concours.",
    "plus_t2auxiliaire_ex3_2": "La tempête a retardé le concours.",
    "plus_t2auxiliaire_ex3_3": "Les organisateurs sont restés jusqu'à la fin.",
}

TEXT_OVERRIDES = {}


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
    print(f"🔊 Mini-leçons « Ouvrir la mini-leçon » — {len(CLIPS)} extraits\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / "assets/interactive/module-nouvelles/sons"
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
