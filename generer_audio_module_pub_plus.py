#!/usr/bin/env python3
"""
Générateur d'audio — boutons d'écoute des mini-leçons « Ouvrir la mini-leçon »
du module « module-pub ».

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
    "plus_prAccent_ana1": "Cet atelier est complètement gratuit",
    "plus_prAccent_lab2_g": "Cet atelier est complètement gratuit",
    "plus_prAccent_lab2_a": "Nos bénévoles réparent absolument tout",
    "plus_prAccent_lab2_f": "Vous repartirez avec un grille-pain qui fonctionne",
    "plus_prAccent_ex3_0": "C'est la dernière occasion avant l'été.",
    "plus_prAccent_ex3_1": "Quelle belle idée de quartier !",
    "plus_prPub_ana1": "L'Atelier Roues Libres ouvre sa clinique de printemps",
    "plus_prPub_lab2_r": "Les gens du quartier qui ont un vélo",
    "plus_prPub_lab2_m": "Une clinique de vélo avec des bénévoles",
    "plus_prPub_lab2_c": "Une affiche sur le babillard",
    "plus_prPub_ex3_0": "Le récepteur : les gens qui réparent leurs objets eux-mêmes.",
    "plus_prPub_ex3_1": "Le canal : une affiche, la radio, une infolettre.",
    "plus_t1compare_ana1": "la capsule de la friperie est plus courte que celle de la cuisine collective",
    "plus_t1compare_lab2_r": "La radio du quartier rejoint moins d'auditeurs que la radio de la ville",
    "plus_t1compare_lab2_a": "L'affiche du babillard coûte moins cher que l'annonce dans le journal",
    "plus_t1compare_lab2_b": "Les bénévoles du samedi arrivent plus tôt que ceux du dimanche",
    "plus_t1compare_ex3_0": "Une lampe réparée dure plus longtemps qu'une lampe achetée à rabais.",
    "plus_t1compare_ex3_1": "Le grille-pain de Solange est plus vieux que celui d'Omar.",
    "plus_t1prefixe_ana1": "réutiliser",
    "plus_t1prefixe_lab2_d": "débrancher",
    "plus_t1prefixe_lab2_s": "surchauffer",
    "plus_t1prefixe_lab2_i": "interurbain",
    "plus_t1prefixe_ex3_0": "irréparable",
    "plus_t1prefixe_ex3_1": "préinscription",
    "plus_t1suffixe_ana1": "réparable",
    "plus_t1suffixe_lab2_b": "bricoleur",
    "plus_t1suffixe_lab2_s": "solidité",
    "plus_t1suffixe_lab2_c": "confiance",
    "plus_t1suffixe_ex3_0": "jetable",
    "plus_t1suffixe_ex3_1": "animatrice",
    "plus_t2determinant_ana1": "les vieux objets que tu répares",
    "plus_t2determinant_lab2_g": "On écoute la radio le matin",
    "plus_t2determinant_lab2_s": "On écoute la capsule de Solange",
    "plus_t2determinant_ex3_0": "Je déteste le gaspillage.",
    "plus_t2determinant_ex3_1": "Je prends le cours de couture du vendredi soir.",
    "plus_t2negatif_ana1": "je n'ai pas entendu",
    "plus_t2negatif_lab2_n": "Nous n'avons pas annoncé l'atelier",
    "plus_t2negatif_lab2_l": "Les bénévoles ne sont pas arrivés avant neuf heures",
    "plus_t2negatif_lab2_v": "Vous n'êtes pas venus à la clinique",
    "plus_t2negatif_ex3_0": "Nous n'avons pas annoncé l'atelier dans l'infolettre.",
    "plus_t2negatif_ex3_1": "Les bénévoles ne sont pas arrivés avant neuf heures.",
    # Items de l'exercice « L'accent d'insistance » (Je découvre) —
    # playWord() les cherche sous sons/<idExo>_<index>.mp3.
    "prAccent_0": "Cet atelier est complètement gratuit.",
    "prAccent_1": "Nos bénévoles réparent absolument tout.",
    "prAccent_2": "C'est la dernière occasion avant l'été.",
    "prAccent_3": "Vous repartirez avec un grille-pain qui fonctionne.",
    "prAccent_4": "Quelle belle idée de quartier !",

}

# Un mot seul, envoyé sans contexte, ne donne au moteur aucun indice de
# langue (voir phase2-audio.md du skill module-parite). Le mot affiché à
# l'élève ne change pas ; seul le texte envoyé à l'API reçoit un
# déterminant ou un tout petit contexte français.
TEXT_OVERRIDES = {
    "plus_t1prefixe_ana1": "on peut réutiliser",
    "plus_t1prefixe_lab2_d": "on peut débrancher",
    "plus_t1prefixe_lab2_s": "on peut surchauffer",
    "plus_t1prefixe_lab2_i": "le transport interurbain",
    "plus_t1prefixe_ex3_0": "c'est irréparable",
    "plus_t1prefixe_ex3_1": "la préinscription",
    "plus_t1suffixe_ana1": "c'est réparable",
    "plus_t1suffixe_lab2_b": "le bricoleur",
    "plus_t1suffixe_lab2_s": "la solidité",
    "plus_t1suffixe_lab2_c": "la confiance",
    "plus_t1suffixe_ex3_0": "c'est jetable",
    "plus_t1suffixe_ex3_1": "l'animatrice",
    # Accent d'insistance : le mot à accentuer est écrit en majuscules dans
    # le texte envoyé au moteur (il l'allonge au lieu de l'épeler, vérifié).
    # Sans ça, la phrase est lue à plat et l'exercice n'a plus de réponse.
    "prAccent_0": "Cet atelier est complètement GRATUIT.",
    "prAccent_1": "Nos bénévoles réparent ABSOLUMENT tout.",
    "prAccent_2": "C'est la DERNIÈRE occasion avant l'été.",
    "prAccent_3": "Vous repartirez avec un grille-pain qui FONCTIONNE.",
    "prAccent_4": "Quelle BELLE idée de quartier !",

}


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
        print("❌ AZURE_SPEECH_KEY absente"); sys.exit(1)

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
