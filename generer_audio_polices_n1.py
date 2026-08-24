#!/usr/bin/env python3
"""
Générateur d'audio — atelier « Même mot, autre police » (polices-n1).

Quinze extraits, un par mot : `assets/interactive/polices-n1/audio/<slug>.mp3`.
La source est `mots.json`, jamais une liste recopiée ici — c'est la faute que
les premiers générateurs du dépôt ont faite et payée à la première correction.

Ce qui est prononcé est le **terme**, avec son déterminant — « les toilettes »,
« le prénom » — et non le mot nu qui s'affiche dans les six écritures. Un
élève de niveau 1 apprend le mot avec son article ; c'est aussi ce que porte
l'en-tête de la fiche, juste au-dessus du bouton d'écoute.

La voix est celle de l'enseignante, ralentie à 0,85 par `voix_lente` — la
même que les mots isolés des quatre modules du niveau 1, pour qu'un mot ne
change pas de bouche en changeant d'activité.

    python3 generer_audio_polices_n1.py [--force]

Relançable : un fichier déjà présent est sauté, sauf avec `--force`.

**Le bac à sable réseau bloque api.elevenlabs.io.** Lancer avec
`dangerouslyDisableSandbox`, comme le dit `docs/deux-agents-en-parallele.md` :

    nohup python3 generer_audio_polices_n1.py > /private/tmp/audio_polices.log 2>&1 &
"""
import json
import os
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ pip install requests"); sys.exit(1)

from voix_lente import ralentir_si_enseignante
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés

RACINE = Path(__file__).resolve().parent
DOSSIER = RACINE / "assets/interactive/polices-n1"
MOTS = DOSSIER / "mots.json"

VOIX_ENSEIGNANTE = "mActWQg9kibLro6Z2ouY"   # 👩 féminine #1, ralentie à 0,85

ESSAIS = 5           # tentatives par extrait
ATTENTE_BASE_S = 4   # doublée à chaque échec : 4, 8, 16, 32 s


def parle(cle, texte, voix, chemin):
    """Un extrait, avec reprise sur coupure réseau.

    Copiée de `generer_audio_module_n2_autobus.py`, comme le demande
    `docs/deux-agents-en-parallele.md` : ElevenLabs coupe la liaison par
    intermittence, plusieurs fois par jour. Une panne passagère du
    fournisseur n'est pas une erreur du programme — on réessaie en doublant
    l'attente, et on ne déclare l'échec qu'après cinq tentatives.
    """
    for essai in range(1, ESSAIS + 1):
        try:
            r = requests.post(
                f"https://api.elevenlabs.io/v1/text-to-speech/{voix}",
                json=enrichir({"text": texte, "model_id": "eleven_multilingual_v2",
                               "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}),
                headers={"xi-api-key": cle, "Content-Type": "application/json"},
                timeout=60)
        except requests.exceptions.RequestException as e:
            if essai == ESSAIS:
                print(f"   ❌ réseau après {ESSAIS} essais : {type(e).__name__}")
                return False
            attente = ATTENTE_BASE_S * (2 ** (essai - 1))
            print(f"⏳{attente}s", end="", flush=True)
            time.sleep(attente)
            continue

        # 429 (débit) et 5xx (panne du service) valent une reprise ; un 401 ou
        # un 422 sont des erreurs à nous, inutile d'insister.
        if r.status_code in (429, 500, 502, 503, 504) and essai < ESSAIS:
            attente = ATTENTE_BASE_S * (2 ** (essai - 1))
            print(f"⏳{r.status_code}/{attente}s", end="", flush=True)
            time.sleep(attente)
            continue
        if r.status_code != 200:
            print(f"   ❌ {r.status_code}: {r.text[:150]}")
            return False

        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_bytes(r.content)
        ralentir_si_enseignante(chemin, voix)
        return True
    return False


def main():
    cle = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not cle:
        env = RACINE / ".env"
        if env.exists():
            for ligne in env.read_text(encoding="utf-8").splitlines():
                if ligne.strip().startswith("ELEVENLABS_API_KEY="):
                    cle = ligne.split("=", 1)[1].strip().strip("\"'")
    if not cle:
        print("❌ ELEVENLABS_API_KEY absente (variable d'environnement ou .env)")
        sys.exit(1)

    force = "--force" in sys.argv

    if not MOTS.exists():
        sys.exit(f"❌ {MOTS} introuvable")
    mots = json.loads(MOTS.read_text(encoding="utf-8"))

    print(f"🔊 polices-n1 — {len(mots)} extraits\n")
    ok = saute = echec = 0
    for m in mots:
        chemin = DOSSIER / m["audio"]
        if chemin.exists() and not force:
            saute += 1
            continue
        print(f"  · {m['terme']:<24}", end="", flush=True)
        if parle(cle, m["terme"], VOIX_ENSEIGNANTE, chemin):
            print(" ✅")
            ok += 1
        else:
            echec += 1

    print(f"\n{ok} écrits · {saute} déjà là · {echec} en échec")
    return 1 if echec else 0


if __name__ == "__main__":
    sys.exit(main())
