#!/usr/bin/env python3
"""
Générateur d'audio — boutons d'écoute des mini-leçons « Ouvrir la mini-leçon »
du module « module-logement ».

fileId → texte lu ; doit correspondre aux appels playWord() générés par
plAudioId() dans le HTML. Pour régénérer cette liste après une modification de
l'objet PLUS : ouvrir le module dans le navigateur et lancer plAudioManifest()
dans la console — elle renvoie exactement ce dictionnaire.

Voix unique (enseignante) — même voix que les mots isolés des autres modules.
"""
import os, sys, time
from pathlib import Path

import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))

VOICE = "mActWQg9kibLro6Z2ouY"

CLIPS = {
    "plus_pr1_ana1": "un quatre et demi",
    "plus_pr1_lab2_1": "Une seule pièce avec une cuisinette et une salle de bain",
    "plus_pr1_lab2_3": "Une chambre, un salon, une cuisine et une salle de bain",
    "plus_pr1_lab2_5": "Trois chambres, un salon, une cuisine et une salle de bain",
    "plus_pr1_ex3_0": "un trois et demi",
    "plus_pr1_ex3_1": "un cinq et demi",
    "plus_pr5_ana1": "un bail, ce bail",
    "plus_pr5_lab2_p": "Cette place est réservée au locataire du deuxième",
    "plus_pr5_lab2_f": "Ces fenêtres arrêtent bien le bruit",
    "plus_pr5_lab2_b": "Ce bail commence le 1er septembre",
    "plus_pr5_ex3_0": "Cette peinture couvre bien le vert olive.",
    "plus_pr5_ex3_1": "Ce camion recule dans la ruelle vers cinq heures.",
    "plus_pr6_ana1": "la boulangerie ouvre-t-elle",
    "plus_pr6_lab2_b": "Le bail commence-t-il le 1er septembre",
    "plus_pr6_lab2_c": "Les chats sont-ils acceptés dans l'immeuble",
    "plus_pr6_lab2_f": "Les fenêtres donnent-elles sur la cour",
    "plus_pr6_ex3_0": "La buanderie est-elle au sous-sol ?",
    "plus_pr6_ex3_1": "Le camion de farine arrive-t-il avant six heures ?",
    "plus_t2emph_ana1": "Celui que je crains, c'est le camion de farine",
    "plus_t2emph_lab2_ce": "Ce que je changerais, c'est la couleur des murs",
    "plus_t2emph_lab2_cel": "Celui que je crains, c'est le camion de farine",
    "plus_t2emph_lab2_cq": "C'est Ginette qui fournit la peinture",
    "plus_t2emph_ex3_0": "Ce qui presse le plus, c'est la signature du bail.",
    "plus_t2emph_ex3_1": "Celle que Leyla a remarquée, c'est la fenêtre de la cuisine.",
    "plus_t3cdci_ana1": "un logement lumineux, à son frère",
    "plus_t3cdci_lab2_d": "La propriétaire fournit la peinture",
    "plus_t3cdci_lab2_i": "Ibrahim pense à son déménagement",
    "plus_t3cdci_ex3_0": "Le boulanger reçoit une livraison de farine.",
    "plus_t3cdci_ex3_1": "Ginette montre le sous-sol aux nouveaux locataires.",
}

TEXT_OVERRIDES = {}


# L'audio du cours vient d'Azure Speech depuis le 26 août 2026. La fonction
# ci-dessous garde son nom et sa signature — `main()` l'appelle telle quelle —
# mais délègue. La clé ElevenLabs et le contexte `avant`/`apres` sont acceptés
# et ignorés : le `xml:lang="fr-CA"` du SSML rend ce dernier inutile.
from azure_voix import parle_compat  # noqa: E402


def generate(api_key, text, path):
    return parle_compat(api_key, text, VOICE, path)
def main():
    print(f"🔊 Mini-leçons « Ouvrir la mini-leçon » — {len(CLIPS)} extraits\n")
    api_key = os.environ.get("AZURE_SPEECH_KEY", "").strip()
    if not api_key:
        # Repli sur `~/Claude/.env`, où vit la clé Azure avec les autres clés
        # de génération. Sans ça, ces générateurs de forme ancienne — qui ne
        # lisaient que l'environnement — échouaient dès qu'ils étaient lancés
        # autrement qu'à la main dans un shell où la clé était exportée.
        _env = Path.home() / "Claude" / ".env"
        if _env.exists():
            for _l in _env.read_text(encoding="utf-8").splitlines():
                if _l.strip().startswith("AZURE_SPEECH_KEY="):
                    api_key = _l.split("=", 1)[1].strip().strip("\"'")
    if not api_key:
        print("❌ AZURE_SPEECH_KEY absente"); sys.exit(1)

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
