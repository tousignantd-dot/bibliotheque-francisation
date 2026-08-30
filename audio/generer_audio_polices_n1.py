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

import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))

RACINE = Path(__file__).resolve().parent
DOSSIER = RACINE / "assets/interactive/polices-n1"
MOTS = DOSSIER / "mots.json"

VOIX_ENSEIGNANTE = "mActWQg9kibLro6Z2ouY"   # 👩 féminine #1, ralentie à 0,85

ESSAIS = 5           # tentatives par extrait
ATTENTE_BASE_S = 4   # doublée à chaque échec : 4, 8, 16, 32 s


# L'audio du cours vient d'Azure Speech depuis le 26 août 2026. La fonction
# ci-dessous garde son nom et sa signature — `main()` l'appelle telle quelle —
# mais délègue. La clé ElevenLabs et le contexte `avant`/`apres` sont acceptés
# et ignorés : le `xml:lang="fr-CA"` du SSML rend ce dernier inutile.
from azure_voix import parle_compat  # noqa: E402


def parle(cle, texte, voix, chemin):
    return parle_compat(cle, texte, voix, chemin)
def main():
    cle = os.environ.get("AZURE_SPEECH_KEY", "").strip()
    if not cle:
        env = Path.home() / "Claude" / ".env"
        if env.exists():
            for ligne in env.read_text(encoding="utf-8").splitlines():
                if ligne.strip().startswith("AZURE_SPEECH_KEY="):
                    cle = ligne.split("=", 1)[1].strip().strip("\"'")
    if not cle:
        print("❌ AZURE_SPEECH_KEY absente (variable d'environnement ou .env)")
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
