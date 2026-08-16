#!/usr/bin/env python3
"""
Générateur d'audio — mini-leçons du module « Prendre rendez-vous et aller à
la pharmacie » (Santé).

fileId → texte lu ; doit correspondre aux appels playWord() générés par
plAudioId() dans le HTML. Pour régénérer cette liste après une modification de
l'objet PLUS : ouvrir le module dans le navigateur et lancer plAudioManifest()
dans la console — elle renvoie exactement ce dictionnaire, prêt à coller.
"""
import os, sys, time
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ pip install requests"); sys.exit(1)

MODULE_SLUG = "module-sante"
# Quatrième voix du module, distincte des trois personnages des dialogues
# (Lina feminin_2, la réceptionniste enseignante, le pharmacien masculin_1) :
# la mini-leçon n'est la parole de personne dans l'histoire. Voix féminine
# parce que les phrases portent les accords de Lina — « je suis très fatiguée ».
VOICE = "rCmVtv8cYU60uhlsOo1M"        # 👩 Féminine #3

CLIPS = {
    # Produit par plAudioManifest() dans la console du module.
    "plus_l1_ana1": "je vais voir",
    "plus_l1_lab2_jerdv": "je vais prendre un rendez-vous",
    "plus_l1_lab2_jeattendre": "je vais attendre",
    "plus_l1_lab2_jeappeler": "je vais appeler la clinique",
    "plus_l1_lab2_nousrdv": "nous allons prendre un rendez-vous",
    "plus_l1_lab2_nousattendre": "nous allons attendre",
    "plus_l1_lab2_nousappeler": "nous allons appeler la clinique",
    "plus_l1_lab2_ellesrdv": "elles vont prendre un rendez-vous",
    "plus_l1_lab2_ellesattendre": "elles vont attendre",
    "plus_l1_lab2_ellesappeler": "elles vont appeler la clinique",
    "plus_l1_ex3_0": "Je vais prendre un rendez-vous demain.",
    "plus_l1_ex3_1": "Tu vas appeler Info-Santé 811.",
    "plus_l1_ex3_2": "Le docteur Tremblay va voir Lina jeudi.",
    "plus_l1_ex3_3": "Nous allons attendre dans la salle d'attente.",
    "plus_l1_ex3_4": "Vous allez recevoir votre ordonnance.",
    "plus_l1_ex3_5": "Les patients vont arriver à neuf heures.",
    "plus_l2_ana1": "je me sens",
    "plus_l2_lab2_jesentir": "je me sens",
    "plus_l2_lab2_jereposer": "je me repose",
    "plus_l2_lab2_jereveiller": "je me réveille",
    "plus_l2_lab2_noussentir": "nous nous sentons",
    "plus_l2_lab2_nousreposer": "nous nous reposons",
    "plus_l2_lab2_nousreveiller": "nous nous réveillons",
    "plus_l2_lab2_ilssentir": "ils se sentent",
    "plus_l2_lab2_ilsreposer": "ils se reposent",
    "plus_l2_lab2_ilsreveiller": "ils se réveillent",
    "plus_l2_ex3_0": "Je me sens fatiguée depuis deux semaines.",
    "plus_l2_ex3_1": "Tu te reposes après le travail.",
    "plus_l2_ex3_2": "Lina se réveille avec mal à la tête.",
    "plus_l2_ex3_3": "Nous nous reposons le week-end.",
    "plus_l2_ex3_4": "Vous vous sentez mieux aujourd'hui ?",
    "plus_l2_ex3_5": "Les patients se sentent nerveux avant l'examen.",
    "plus_l3_ana1": "j'ai besoin d'un rendez-vous",
    "plus_l3_lab2_rdv": "J'ai besoin d'un rendez-vous",
    "plus_l3_lab2_medicaments": "J'ai besoin de médicaments",
    "plus_l3_lab2_reposer": "J'ai besoin de me reposer",
    "plus_l3_lab2_aide": "J'ai besoin d'aide",
    "plus_l3_ex3_0": "J'ai besoin d'un rendez-vous cette semaine.",
    "plus_l3_ex3_1": "J'ai besoin de médicaments pour la fièvre.",
    "plus_l3_ex3_2": "J'ai besoin de me reposer deux jours.",
    "plus_l3_ex3_3": "J'ai besoin de dormir plus longtemps.",
    "plus_l3_ex3_4": "Nous avons besoin d'aide pour remplir le formulaire.",
    "plus_l3_ex3_5": "Vous avez besoin de votre carte d'assurance maladie.",
    "plus_l4_ana1": "je suis très fatiguée",
    "plus_l4_lab2_peufatigue": "Je suis un peu fatiguée",
    "plus_l4_lab2_peutete": "J'ai un peu mal à la tête",
    "plus_l4_lab2_assezfatigue": "Je suis assez fatiguée",
    "plus_l4_lab2_asseztete": "J'ai assez mal à la tête",
    "plus_l4_lab2_tresfatigue": "Je suis très fatiguée",
    "plus_l4_lab2_trestete": "J'ai très mal à la tête",
    "plus_l4_lab2_tropfatigue": "Je suis trop fatiguée",
    "plus_l4_lab2_troptete": "J'ai trop mal à la tête",
    "plus_l4_ex3_0": "J'ai un peu mal à la tête depuis ce matin.",
    "plus_l4_ex3_1": "Ce médicament est assez efficace.",
    "plus_l4_ex3_2": "Je suis très fatiguée depuis deux semaines.",
    "plus_l4_ex3_3": "J'ai trop de travail, je suis épuisée.",
    "plus_l4_ex3_4": "La salle d'attente est un peu bruyante.",
    "plus_l4_ex3_5": "Le comprimé est trop gros, je n'arrive pas à l'avaler.",
}

# Voir phase2-audio.md : un mot envoyé nu à l'API se fait lire dans une autre
# langue. Rien à corriger ici — le plus court des 58 extraits est « je vais
# voir », un groupe complet avec pronom sujet. Aucun mot isolé dans ce module.
TEXT_OVERRIDES = {}

DEFAULT_VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75}


def generate(api_key, text, path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}"
    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": DEFAULT_VOICE_SETTINGS,
    }
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=45)
        if r.status_code != 200:
            print(f"   ❌ {r.status_code}: {r.text[:160]}")
            return False
    except Exception as e:
        print(f"   ❌ {e}")
        return False
    path.write_bytes(r.content)
    return True


def main():
    print(f"🔊 Mini-leçons « En apprendre plus » — {len(CLIPS)} extraits\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / f"assets/interactive/{MODULE_SLUG}/sons"
    out.mkdir(parents=True, exist_ok=True)

    # --force régénère tout ; --only id1,id2 cible des extraits précis ;
    # sans option, on saute ce qui existe déjà.
    force = "--force" in sys.argv
    only = None
    for i, a in enumerate(sys.argv):
        if a == "--only" and i + 1 < len(sys.argv):
            only = set(x.strip() for x in sys.argv[i + 1].split(",") if x.strip())

    ok = skip = fail = 0
    for file_id, text in CLIPS.items():
        if only and file_id not in only:
            continue
        dest = out / f"{file_id}.mp3"
        if dest.exists() and not force and not only:
            skip += 1
            continue
        spoken = TEXT_OVERRIDES.get(file_id, text)
        print(f"  {file_id:28s} « {spoken[:42]} » → ", end="", flush=True)
        if generate(api_key, spoken, dest):
            print("✓"); ok += 1
        else:
            print("✗"); fail += 1
        time.sleep(0.35)   # ne pas saturer l'API

    # Un disque macOS est insensible à la casse : deux clés qui ne diffèrent
    # que par la casse donneraient un seul fichier, et le second bouton
    # servirait le son du premier. Le contrôle coûte moins cher que le bug.
    noms = {p.stem for p in out.glob("*.mp3")}
    manquants = sorted(set(CLIPS) - noms)
    print(f"\n✅ {ok} générés · {skip} déjà présents · {fail} en échec")
    if manquants:
        print(f"⚠️  {len(manquants)} fichier(s) attendu(s) absent(s) : {manquants[:6]}")
    if fail or manquants:
        sys.exit(1)


if __name__ == "__main__":
    main()
