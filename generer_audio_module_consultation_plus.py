#!/usr/bin/env python3
"""
Générateur d'audio — boutons d'écoute des mini-leçons « Ouvrir la mini-leçon »
du module « module-consultation ».

fileId → texte lu ; doit correspondre aux appels playWord() générés par
plAudioId() dans le HTML. Pour régénérer cette liste après une modification de
l'objet PLUS : ouvrir le module dans le navigateur et lancer plAudioManifest()
dans la console — elle renvoie exactement ce dictionnaire.

Voix unique (enseignante) — même voix que les mots isolés du module.
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
    "plus_prPhon_ana1": "patient",
    "plus_prPhon_ana2": "front",
    "plus_prPhon_lab4_a": "patient",
    "plus_prPhon_lab4_b": "front",
    "plus_prPhon_lab4_c": "main",
    "plus_prPhon_lab4_d": "tendon",
    "plus_prPhon_ex5_0": "patient",
    "plus_prPhon_ex5_1": "jambe",
    "plus_prPhon_ex5_2": "temps",
    "plus_prPhon_ex5_3": "dent",
    "plus_prPhon_ex5_4": "tendon",
    "plus_prPhon_ex5_5": "front",
    "plus_prPhon_ex5_6": "nom",
    "plus_prPhon_ex5_7": "consultation",
    "plus_prPhon_ex5_8": "main",
    "plus_prPhon_ex5_9": "examen",
    "plus_prPhon_ex5_10": "médecin",
    "plus_t1cause_ana1": "je consulte parce que mon genou est enflé",
    "plus_t1cause_ana2": "je boite à cause de la douleur",
    "plus_t1cause_lab3_1": "Je consulte parce que mon genou est enflé.",
    "plus_t1cause_lab3_2": "Je boite à cause de la douleur.",
    "plus_t1cause_lab3_3": "Il ne travaille pas, car il doit se reposer.",
    "plus_t1cause_ex4_0": "Je consulte parce que j'ai mal au genou.",
    "plus_t1cause_ex4_1": "Je ne peux pas courir à cause de mon inflammation.",
    "plus_t1cause_ex4_2": "La salle est pleine parce que beaucoup de gens sont malades.",
    "plus_t1cause_ex4_3": "Elle porte une attelle à cause de sa blessure.",
    "plus_t1cause_ex4_4": "Il ne travaille pas, car il doit se reposer.",
    "plus_t1cause_ex4_5": "Je boite à cause de la douleur au genou.",
    "plus_t1quest_ana1": "Est-ce que vous avez mal ?",
    "plus_t1quest_ana2": "Depuis quand avez-vous mal ?",
    "plus_t1quest_lab4_e": "Est-ce que vous avez de la fièvre ?",
    "plus_t1quest_lab4_m": "Où est la douleur ?",
    "plus_t1quest_lab4_i": "Avez-vous de la fièvre ?",
    "plus_t1quest_ex5_0": "Est-ce que vous avez mal ?",
    "plus_t1quest_ex5_1": "Depuis quand avez-vous mal ?",
    "plus_t1quest_ex5_2": "Où est la douleur ?",
    "plus_t1quest_ex5_3": "Avez-vous de la fièvre ?",
    "plus_t1quest_ex5_4": "Sur une échelle de un à dix, où se situe votre douleur ?",
    "plus_t1quest_ex5_5": "Est-ce que vous prenez des médicaments ?",
    "plus_t2present_ana1": "il soulève",
    "plus_t2present_lab2_j": "je soulève",
    "plus_t2present_lab2_n": "nous soulevons",
    "plus_t2present_lab2_i": "ils soulèvent",
    "plus_t2present_ex3_0": "j'ai, tu as, il a",
    "plus_t2present_ex3_1": "nous avons, vous avez, ils ont",
    "plus_t2present_ex3_2": "je suis, tu es, il est",
    "plus_t2present_ex3_3": "nous sommes, vous êtes, ils sont",
    "plus_t2present_ex3_4": "je peux, tu peux, il peut",
    "plus_t2present_ex3_5": "nous pouvons, vous pouvez, ils peuvent",
    "plus_t2neg_ana1": "je ne travaille pas",
    "plus_t2neg_ana2": "je n'ai pas de fièvre",
    "plus_t2neg_lab3_p": "Je ne travaille pas aujourd'hui.",
    "plus_t2neg_lab3_l": "Il ne court plus depuis sa blessure.",
    "plus_t2neg_lab3_j": "Elle ne prend jamais ce médicament.",
    "plus_t2neg_ex4_0": "Il ne peut pas plier la jambe.",
    "plus_t2neg_ex4_1": "Je n'ai pas de fièvre.",
    "plus_t2neg_ex4_2": "Elle ne travaille pas cette semaine.",
    "plus_t2neg_ex4_3": "Yannick ne soulève plus de charges.",
    "plus_t3plur_ana1": "des tendons irrités",
    "plus_t3plur_ana2": "des maux généraux",
    "plus_t3plur_lab3_g": "des genoux enflés",
    "plus_t3plur_lab3_m": "des maux généraux",
    "plus_t3plur_lab3_b": "des nouveaux bureaux",
    "plus_t3plur_lab3_r": "des bras droits",
    "plus_t3plur_ex4_0": "des tendons irrités",
    "plus_t3plur_ex4_1": "des maux de tête",
    "plus_t3plur_ex4_2": "des genoux enflés",
    "plus_t3plur_ex4_3": "des nouveaux patients",
    "plus_t3plur_ex4_4": "des bras droits",
    "plus_t3plur_ex4_5": "des médicaments prescrits",
    "plus_t3devoir_ana1": "il doit se reposer",
    "plus_t3devoir_ana2": "il faut éviter de forcer",
    "plus_t3devoir_lab3_j": "Je dois me reposer.",
    "plus_t3devoir_lab3_v": "Vous devez revenir dans une semaine.",
    "plus_t3devoir_lab3_x": "Il faut éviter de forcer.",
    "plus_t3devoir_ex4_0": "Yannick doit se reposer quatre jours.",
    "plus_t3devoir_ex4_1": "Vous devez appliquer de la glace trois fois par jour.",
    "plus_t3devoir_ex4_2": "Il faut plier les genoux pour soulever une boîte.",
    "plus_t3devoir_ex4_3": "Je dois prendre un rendez-vous en physiothérapie.",
    "plus_t3devoir_ex4_4": "Il faut consulter si la douleur dure plus d'une semaine.",
    "plus_t3devoir_ex4_5": "Nous devons revenir la semaine prochaine.",
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

    out = Path(__file__).resolve().parent / "assets/interactive/module-consultation/sons"
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
