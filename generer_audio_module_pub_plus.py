#!/usr/bin/env python3
"""
Générateur d'audio — boutons d'écoute des mini-leçons « En apprendre plus »
du module « module-pub ».

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
    "plus_prAccent_ana1": "Cet endroit est tout simplement le plus spectaculaire",
    "plus_prAccent_lab2_s": "Cet endroit est tout simplement le plus spectaculaire",
    "plus_prAccent_lab2_a": "Il faut absolument visiter ce site historique",
    "plus_prAccent_lab2_m": "Vous avez trouvé la meilleure auberge",
    "plus_prAccent_ex3_0": "Cette région est la plus enchanteresse de la province.",
    "plus_prAccent_ex3_1": "Tu as eu la bonne idée d'aller à ce parc.",
    "plus_prPub_ana1": "La ferme Belle-Récolte vous invite à sa fête des récoltes annuelle",
    "plus_prPub_lab2_r": "Les gens qui veulent cueillir des citrouilles",
    "plus_prPub_lab2_m": "Une fête des récoltes avec tartes maison",
    "plus_prPub_lab2_c": "Une affiche publicitaire",
    "plus_prPub_ex3_0": "Le récepteur : les gens qui aiment les produits locaux.",
    "plus_prPub_ex3_1": "Le canal : la radio, une affiche, une vidéo.",
    "plus_t1compare_ana1": "la ville de Québec est plus vieille que la ville de Montréal",
    "plus_t1compare_lab2_v": "Vous voyagez plus souvent que nous",
    "plus_t1compare_lab2_r": "Le restaurant thaï ferme plus tard que le restaurant mexicain",
    "plus_t1compare_lab2_s": "Le spectacle de vendredi était plus divertissant que le spectacle de samedi",
    "plus_t1compare_ex3_0": "Le climat de la Gaspésie est plus rigoureux que le climat de Montréal.",
    "plus_t1compare_ex3_1": "Les billets sont en vente plus tôt que l'an passé.",
    "plus_t1prefixe_ana1": "réorganiser",
    "plus_t1prefixe_lab2_a": "antigel",
    "plus_t1prefixe_lab2_r": "repartir",
    "plus_t1prefixe_lab2_i": "interprovincial",
    "plus_t1prefixe_ex3_0": "inconfortable",
    "plus_t1prefixe_ex3_1": "préhistoire",
    "plus_t1suffixe_ana1": "chanteur",
    "plus_t1suffixe_lab2_a": "aimable",
    "plus_t1suffixe_lab2_b": "beauté",
    "plus_t1suffixe_lab2_e": "élégance",
    "plus_t1suffixe_ex3_0": "transportable",
    "plus_t1suffixe_ex3_1": "voyageur",
    "plus_t2determinant_ana1": "la musique que j'entends",
    "plus_t2determinant_lab2_g": "J'aime les fruits de mer",
    "plus_t2determinant_lab2_s": "Je prends les fruits de mer au menu",
    "plus_t2determinant_ex3_0": "Nous aimons les plages.",
    "plus_t2determinant_ex3_1": "Elle choisit le forfait familial.",
    "plus_t2negatif_ana1": "je n'ai pas visité",
    "plus_t2negatif_lab2_j": "Je n'ai pas aimé la visite",
    "plus_t2negatif_lab2_i": "Ils ne sont pas arrivés hier",
    "plus_t2negatif_lab2_v": "Vous n'êtes pas allés à Tadoussac",
    "plus_t2negatif_ex3_0": "Nous n'avons pas voyagé pendant deux semaines.",
    "plus_t2negatif_ex3_1": "Ils ne sont pas arrivés à destination hier.",
}

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

    out = Path(__file__).resolve().parent / "assets/interactive/module-pub/sons"
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
