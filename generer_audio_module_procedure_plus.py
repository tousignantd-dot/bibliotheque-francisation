#!/usr/bin/env python3
"""
Générateur d'audio — boutons d'écoute des mini-leçons « Ouvrir la mini-leçon »
du module « module-procedure ».

fileId → texte lu ; doit correspondre aux appels playWord() générés par
plAudioId() dans le HTML. Pour régénérer cette liste après une modification de
l'objet PLUS : ouvrir le module dans le navigateur et lancer plAudioManifest()
dans la console — elle renvoie exactement ce dictionnaire.

Voix unique (enseignante) — même voix que les mots isolés du module.
"""
import os, sys, time
from pathlib import Path

import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))

VOICE = "mActWQg9kibLro6Z2ouY"

CLIPS = {
    "plus_prPhon_ana1": "nuit",
    "plus_prPhon_ana2": "ligne",
    "plus_prPhon_lab3_h": "aujourd'hui et nuit",
    "plus_prPhon_lab3_j": "juillet et orangé",
    "plus_prPhon_lab3_g": "gagner et ligne",
    "plus_prPhon_ex4_0": "aujourd'hui",
    "plus_prPhon_ex4_1": "nuit",
    "plus_prPhon_ex4_2": "juillet",
    "plus_prPhon_ex4_3": "orangé",
    "plus_prPhon_ex4_4": "joindre",
    "plus_prPhon_ex4_5": "gagner",
    "plus_prPhon_ex4_6": "ligne",
    "plus_prPhon_ex4_7": "signature",
    "plus_prVocab_ana1": "des jours ouvrables",
    "plus_prVocab_lab2_j": "Joignez le reçu à la demande",
    "plus_prVocab_lab2_r": "Remplissez le formulaire en ligne",
    "plus_prVocab_lab2_s": "Soumettez votre demande dans l'application",
    "plus_prVocab_lab2_a": "Le superviseur doit approuver la demande",
    "plus_prVocab_ex3_0": "une procédure",
    "plus_prVocab_ex3_1": "un remboursement",
    "plus_prVocab_ex3_2": "un reçu",
    "plus_prVocab_ex3_3": "un onglet",
    "plus_prVocab_ex3_4": "un jour ouvrable",
    "plus_prVocab_ex3_5": "un formulaire",
    "plus_aEtapes_ana1": "D'abord, tu ouvres l'application",
    "plus_aEtapes_lab2_1": "D'abord vous ouvrez l'application",
    "plus_aEtapes_lab2_2": "Ensuite vous prenez une photo du reçu",
    "plus_aEtapes_lab2_3": "Puis vous inscrivez le montant",
    "plus_aEtapes_lab2_4": "Enfin vous attendez l'approbation",
    "plus_aEtapes_ex3_0": "D'abord, ouvrez l'application Ressources+.",
    "plus_aEtapes_ex3_1": "Ensuite, prenez une photo de votre reçu.",
    "plus_aEtapes_ex3_2": "Puis, inscrivez le montant exact.",
    "plus_aEtapes_ex3_3": "Enfin, attendez l'approbation de votre superviseur.",
    "plus_t1que_ana1": "le reçu que je dois joindre",
    "plus_t1que_lab2_f": "Voici le formulaire que vous devez remplir",
    "plus_t1que_lab2_r": "Voici le reçu que je dois joindre",
    "plus_t1que_lab2_a": "C'est l'application que Diane m'a montrée",
    "plus_t1que_lab2_d": "J'approuve la demande que vous avez soumise",
    "plus_t1que_ex3_0": "Voici le reçu que je dois joindre.",
    "plus_t1que_ex3_1": "C'est l'application que vous devez utiliser.",
    "plus_t1que_ex3_2": "Elle suit la procédure qu'on lui a montrée.",
    "plus_t1que_ex3_3": "Je vais approuver la demande que vous avez soumise.",
    "plus_t2pendant_ana1": "Je remplis le formulaire pendant que tu prends la photo",
    "plus_t2pendant_lab2_pr": "Je remplis le formulaire pendant que tu cherches le reçu",
    "plus_t2pendant_lab2_pa": "Pendant que je remplissais la demande, Diane a vérifié le montant",
    "plus_t2pendant_lab2_fu": "Nous allons soumettre la demande pendant que le superviseur sera au bureau",
    "plus_t2pendant_ex3_0": "La commis explique la procédure pendant que Samuel prend des notes.",
    "plus_t2pendant_ex3_1": "Je remplis le formulaire pendant que tu cherches le reçu.",
    "plus_t2pendant_ex3_2": "Il attend l'approbation pendant qu'il continue son travail.",
    "plus_t2gerond_ana1": "en suivant les étapes",
    "plus_t2gerond_lab2_s": "Samuel remplit le formulaire en suivant les étapes",
    "plus_t2gerond_lab2_l": "Diane a trouvé la réponse en lisant la directive",
    "plus_t2gerond_lab2_a": "Il parle à son collègue en attendant son tour",
    "plus_t2gerond_lab2_v": "Le technicien a réglé le problème en vérifiant chaque pièce",
    "plus_t2gerond_ex3_0": "Elle travaille en écoutant une baladodiffusion.",
    "plus_t2gerond_ex3_1": "J'aime discuter avec Diane en marchant vers le bureau.",
    "plus_t2gerond_ex3_2": "Samuel prend une pause en attendant l'approbation.",
    "plus_t2gerond_ex3_3": "La commis a corrigé l'erreur en relisant le formulaire.",
    "plus_t2imper_ana1": "Remplissez le formulaire",
    "plus_t2imper_lab2_tu": "Remplis le formulaire",
    "plus_t2imper_lab2_nous": "Remplissons le formulaire",
    "plus_t2imper_lab2_vous": "Remplissez le formulaire",
    "plus_t2imper_ex3_0": "Arrêtez la machine immédiatement.",
    "plus_t2imper_ex3_1": "Prenez une photo du bris.",
    "plus_t2imper_ex3_2": "Avertissez votre superviseur.",
    "plus_t2imper_ex3_3": "Ne réparez pas la machine vous-même.",
    "plus_t2pronom_ana1": "Soumettez-la",
    "plus_t2pronom_lab2_la": "Soumettez-la",
    "plus_t2pronom_lab2_le": "Joignez-le",
    "plus_t2pronom_lab2_moi": "Remettez-moi le formulaire",
    "plus_t2pronom_lab2_lui": "Demandez-le-lui",
    "plus_t2pronom_ex3_0": "Avisez-le de ce changement.",
    "plus_t2pronom_ex3_1": "Préparez-les.",
    "plus_t2pronom_ex3_2": "Appelle-moi dès que la demande est approuvée.",
    "plus_t2pronom_ex3_3": "Contactez-moi si vous avez des questions.",
}

# Les entrées de prPhon (ana1/ana2/ex4_*) sont des mots isolés dans le
# manifeste (le mini-lesson les affiche seuls pour illustrer un son), mais un
# mot seul sans contexte ne donne au moteur aucun indice de langue — même
# piège que dans les cartes de l'exercice de phonétique. On les fait parler
# via la phrase porteuse complète du module (CARRIER_PHRASES dans le HTML) :
# ici ce ne sont pas des cartes à isoler pour l'élève, juste des exemples
# audio, donc une vraie phrase ne nuit à rien.
TEXT_OVERRIDES = {
    "plus_prPhon_ana1": "Le bris s'est produit pendant la nuit.",
    "plus_prPhon_ana2": "Remplissez chaque ligne du formulaire.",
    "plus_prPhon_ex4_0": "Il faut soumettre la demande aujourd'hui.",
    "plus_prPhon_ex4_1": "Le bris s'est produit pendant la nuit.",
    "plus_prPhon_ex4_2": "La formation a lieu en juillet.",
    "plus_prPhon_ex4_3": "Le voyant orangé signale un bris.",
    "plus_prPhon_ex4_4": "N'oubliez pas de joindre votre reçu.",
    "plus_prPhon_ex4_5": "Elle fait ça pour gagner du temps.",
    "plus_prPhon_ex4_6": "Remplissez chaque ligne du formulaire.",
    "plus_prPhon_ex4_7": "La demande attend votre signature.",
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

    out = Path(__file__).resolve().parent / "assets/interactive/module-procedure/sons"
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
