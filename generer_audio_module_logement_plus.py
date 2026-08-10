#!/usr/bin/env python3
"""
Générateur d'audio — boutons d'écoute des mini-leçons « En apprendre plus »
du module « module-logement ».

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
    "plus_pr1_ana1": "un 3 et demi",
    "plus_pr1_lab2_1": "Une grande pièce, une cuisinette et une salle de bain",
    "plus_pr1_lab2_2": "Une chambre, un salon, une cuisinette et une salle de bain",
    "plus_pr1_lab2_4": "Trois chambres ou pièces, un salon et une salle de bain",
    "plus_pr1_ex3_0": "un 2 ½",
    "plus_pr1_ex3_1": "un 4 ½",
    "plus_pr5_ana1": "ce logement",
    "plus_pr5_lab2_c": "Cette cour arrière doit être clôturée",
    "plus_pr5_lab2_d": "Ces documents confirment notre solvabilité",
    "plus_pr5_lab2_v": "Cette visite nous permettra de voir l'appartement",
    "plus_pr5_ex3_0": "Ce lave-vaisselle doit être silencieux.",
    "plus_pr5_ex3_1": "Cet animal ne doit pas être bruyant.",
    "plus_pr6_ana1": "rénove-t-il",
    "plus_pr6_lab2_b": "Le bail est-il prêt pour la signature",
    "plus_pr6_lab2_l": "Les locataires ont-ils déménagé",
    "plus_pr6_lab2_e": "L'électricité est-elle comprise",
    "plus_pr6_ex3_0": "Les chats sont-ils acceptés ?",
    "plus_pr6_ex3_1": "La fin du bail est-elle dans un an ?",
    "plus_t2emph_ana1": "Celle que j'aime, c'est la chambre près du salon",
    "plus_t2emph_lab2_ce": "Ce que le propriétaire souhaite, c'est un paiement par virement",
    "plus_t2emph_lab2_cel": "Celui que nous voulons, c'est le logement au premier étage",
    "plus_t2emph_lab2_cq": "C'est Carole qui a rénové l'appartement",
    "plus_t2emph_ex3_0": "Celle que nous préférons, c'est la fenêtre dans la salle à manger.",
    "plus_t2emph_ex3_1": "Ce que l'appartement a d'intéressant, c'est la grandeur de la chambre.",
    "plus_t3cdci_ana1": "des références, avec le propriétaire",
    "plus_t3cdci_lab2_d": "Le propriétaire demande des références",
    "plus_t3cdci_lab2_i": "Émilio parle à son propriétaire",
    "plus_t3cdci_ex3_0": "Les voisins font des rénovations.",
    "plus_t3cdci_ex3_1": "Carole réfléchit à ses prochains achats.",
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

    out = Path(__file__).resolve().parent / "assets/interactive/module-logement/sons"
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
