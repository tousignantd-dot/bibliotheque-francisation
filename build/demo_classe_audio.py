#!/usr/bin/env python3
"""Les voix des dépôts oraux de la classe de présentation.

Une voix de catalogue ElevenLabs par élève qui a déposé — dix voix distinctes,
et distinctes de celles des personnages des modules : en présentation, on doit
entendre des élèves, pas les comédiens du dialogue. Le texte lu porte les
hésitations d'une prise de parole réelle ; la transcription gardée dans
demo_classe.py reste, elle, ce que la reconnaissance vocale a rendu.

    python3 build/demo_classe_audio.py            # ce qui manque seulement
    python3 build/demo_classe_audio.py --tout     # refait tout

Les MP3 sont écrits dans build/demo-voix-classe/ et non directement dans les
dépôts : demo_classe.py --install les y recopie, et une réinstallation ne
repaie donc pas la synthèse.
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from demo_classe import ORAUX, PAR_ID  # noqa: E402

RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "build" / "demo-voix-classe"
MODELE = "eleven_multilingual_v2"

# Une voix par élève déposant. Stability basse : une voix trop stable donne un
# débit de lecture, or on veut entendre quelqu'un qui cherche ses mots.
VOIX = {
    201: "XB0fDUnXU5powFXDhCwa",  # Charlotte
    202: "JBFqnCBsd6RMkjVDRZzb",  # George
    203: "N2lVS1w4EtoT3dr4eOWO",  # Callum
    205: "EXAVITQu4vr4xnSDxMaL",  # Sarah
    206: "pqHfZKP75CvOlQylNhV4",  # Bill
    207: "Xb7hH8MSUJpSbSDYk0k2",  # Alice
    209: "TX3LPaxmHKxFdv7VOQHJ",  # Liam
    211: "FGY2WhTYpPnrIDTdsKH5",  # Laura
    213: "XrExE9yKIg1WjnnlVkGX",  # Matilda
    215: "pFZP5JQG7iQjIQuC4Bku",  # Lily
}
REGLAGES = {"stability": 0.32, "similarity_boost": 0.75, "style": 0.28}

# Ce qui est réellement dit au micro : la transcription, mais hésitante. Un
# dépôt oral qui se lit sans une seule accroche ne ressemble à rien de ce
# qu'on entend en classe.
HESITATIONS = [
    "Bonjour… euh… j'ai mal à l'épaule droite depuis une semaine. La douleur augmente "
    "quand je lève le bras, et… je dors mal à cause de ça.",
    "J'ai mal au dos depuis… trois jours. Ça fait mal quand je me penche pour ramasser "
    "quelque chose. J'ai pas pris de médicament.",
    "Bonjour, euh… ma gorge est très irritée depuis lundi, et j'ai de la difficulté à "
    "avaler. Je fais… un peu de fièvre le soir.",
    "Moi j'ai mal la tête depuis… deux semaine. Je prend des pilule, mais… ça marche pas "
    "beaucoup.",
    "Hier au travail, mon collègue… il a tombé de l'escabeau. Il a se blessé au poignet. "
    "J'ai mis de la glace tout de suite.",
    "Ce matin, je me suis brûlé la main sur la plaque de cuisson. J'ai mis la main sous "
    "l'eau froide pendant… dix minutes, puis j'ai appelé Info-Santé.",
    "Une cliente a glissé sur le plancher mouillé. Elle s'est fait mal au genou. On a "
    "appelé l'ambulance et… j'ai resté avec elle.",
    "Mon fils… il a se coupé le doigt avec un couteau. Le sang il a arrêté après dix "
    "minute. On a pas allé à l'hôpital.",
    "Il y a un accident. Le monsieur a tombé. Moi… j'ai appeler le 911, et après… j'ai "
    "attendre.",
    "Bonjour, je m'appelle Étoile. Je voudrais un rendez-vous parce que je tousse depuis… "
    "cinq jours. Est-ce que vous avez une place jeudi matin ?",
]


def cle_api():
    cle = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if cle:
        return cle
    env = RACINE / ".env"
    if env.exists():
        trouve = re.search(r'ELEVENLABS_API_KEY\s*=\s*(\S+)', env.read_text(encoding="utf-8"))
        if trouve:
            return trouve.group(1).strip().strip('"').strip("'")
    return ""


def synthetiser(cle, voix, texte, destination):
    corps = json.dumps({
        "text": texte, "model_id": MODELE, "voice_settings": REGLAGES,
    }).encode("utf-8")
    requete = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voix}",
        data=corps, headers={"xi-api-key": cle, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(requete, timeout=90) as reponse:
            destination.write_bytes(reponse.read())
        return True
    except urllib.error.HTTPError as e:
        print(f"   ❌ {e.code} : {e.read()[:200].decode('utf-8', 'replace')}")
    except Exception as e:
        print(f"   ❌ {e}")
    return False


def main():
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument("--tout", action="store_true",
                         help="refaire même les prises déjà produites")
    args = parseur.parse_args()

    if len(HESITATIONS) != len(ORAUX):
        print(f"❌ {len(HESITATIONS)} prises pour {len(ORAUX)} dépôts : les deux listes "
              f"doivent aller de pair.")
        sys.exit(1)

    cle = cle_api()
    if not cle:
        print("❌ ELEVENLABS_API_KEY absente (.env à la racine du projet)")
        sys.exit(1)

    SORTIE.mkdir(parents=True, exist_ok=True)
    faits = sautes = 0
    for i, (depot, texte) in enumerate(zip(ORAUX, HESITATIONS), start=1):
        eleve = PAR_ID[depot["eleve"]]
        destination = SORTIE / f"{i:02d}-{eleve['code'].lower()}.mp3"
        if destination.exists() and not args.tout:
            sautes += 1
            continue
        print(f"🎙️  {i:02d} · {eleve['nom']} — {texte[:52]}…")
        if synthetiser(cle, VOIX[depot["eleve"]], texte, destination):
            print(f"   ✓ {destination.name} ({destination.stat().st_size // 1024} Ko)")
            faits += 1

    print(f"\n{faits} enregistrement(s) produit(s)"
          + (f", {sautes} déjà en place." if sautes else "."))
    if faits:
        print("Les poser dans la démonstration : python3 build/demo_classe.py --install")


if __name__ == "__main__":
    main()
