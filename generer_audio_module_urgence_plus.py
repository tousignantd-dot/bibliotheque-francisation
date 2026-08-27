#!/usr/bin/env python3
"""
Générateur d'audio — boutons d'écoute des mini-leçons « Ouvrir la mini-leçon »
du module « Une urgence au travail ».

fileId → texte lu ; doit correspondre aux appels playWord() générés par
plAudioId() dans le HTML. Pour régénérer cette liste après une modification de
l'objet PLUS : ouvrir le module dans le navigateur et lancer plAudioManifest()
dans la console — elle renvoie exactement ce dictionnaire.

Voix unique (enseignante), comme pour les mots isolés : ce sont des modèles de
prononciation, pas des dialogues.
"""
import os, sys, time
from pathlib import Path

import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))

VOICE = "mActWQg9kibLro6Z2ouY"   # 👩 enseignante — même voix que les mots isolés

CLIPS = {
    # ── Mini-leçon « Les groupes de mots » ──
    "plus_prGrp_ana1": "une brûlure superficielle",
    "plus_prGrp_ana2": "de petites cloques douloureuses",
    "plus_prGrp_lab3_sm": "un doigt enflé",
    "plus_prGrp_lab3_pm": "des doigts enflés",
    "plus_prGrp_lab3_sf": "une main enflée",
    "plus_prGrp_lab3_pf": "des mains enflées",
    "plus_prGrp_ex4_0": "une brûlure superficielle",
    "plus_prGrp_ex4_1": "des cloques douloureuses",
    "plus_prGrp_ex4_2": "un pansement propre",
    "plus_prGrp_ex4_3": "des gants jetables",
    "plus_prGrp_ex4_4": "une compresse stérile",
    "plus_prGrp_ex4_5": "l'avant-bras droit",
    "plus_prGrp_ex4_6": "une petite coupure profonde",
    "plus_prGrp_ex4_7": "des soins urgents",
    # ── Mini-leçon « Le son [y] et le son [u] » ──
    "plus_prPhon_ana1": "une brûlure",
    "plus_prPhon_ana2": "une douleur",
    "plus_prPhon_lab4_1": "tout, tu",
    "plus_prPhon_lab4_2": "la roue, la rue",
    "plus_prPhon_lab4_3": "vous, vu",
    "plus_prPhon_lab4_4": "la boule, la bulle",
    "plus_prPhon_ex5_0": "une brûlure",
    "plus_prPhon_ex5_1": "l'urgence",
    "plus_prPhon_ex5_2": "quinze minutes",
    "plus_prPhon_ex5_3": "le sucre",
    "plus_prPhon_ex5_4": "la douleur",
    "plus_prPhon_ex5_5": "le pouce",
    "plus_prPhon_ex5_6": "de la soupe",
    "plus_prPhon_ex5_7": "du soutien",
    # ── Mini-leçon « Le passé composé » ──
    "plus_t1pc_ana1": "j'ai mis mon bras sous l'eau froide",
    "plus_t1pc_ana2": "elle est arrivée",
    "plus_t1pc_lab4_ea": "elle a appelé",
    "plus_t1pc_lab4_ia": "ils ont appelé",
    "plus_t1pc_lab4_ja": "j'ai appelé",
    "plus_t1pc_lab4_ee": "elle est arrivée",
    "plus_t1pc_lab4_ie": "ils sont arrivés",
    "plus_t1pc_lab4_je": "je suis arrivé",
    "plus_t1pc_ex5_0": "appeler, j'ai appelé",
    "plus_t1pc_ex5_1": "finir, j'ai fini",
    "plus_t1pc_ex5_2": "attendre, j'ai attendu",
    "plus_t1pc_ex5_3": "mettre, j'ai mis",
    "plus_t1pc_ex5_4": "prendre, j'ai pris",
    "plus_t1pc_ex5_5": "faire, j'ai fait",
    "plus_t1pc_ex5_6": "dire, j'ai dit",
    "plus_t1pc_ex5_7": "voir, j'ai vu",
    # ── Mini-leçon « Les verbes pronominaux au passé composé » ──
    "plus_t1pron_ana1": "elle s'est coupée",
    "plus_t1pron_lab2_e0": "elle s'est brûlée",
    "plus_t1pron_lab2_i0": "ils se sont brûlés",
    "plus_t1pron_lab2_e1": "elle s'est brûlé le bras",
    "plus_t1pron_lab2_i1": "ils se sont brûlé les mains",
    "plus_t1pron_ex3_0": "je me suis brûlé la main",
    "plus_t1pron_ex3_1": "il s'est coupé le doigt",
    "plus_t1pron_ex3_2": "elle s'est blessée au travail",
    "plus_t1pron_ex3_3": "il s'est cassé le bras",
    "plus_t1pron_ex3_4": "elle s'est foulé la cheville",
    "plus_t1pron_ex3_5": "je me suis cogné la tête",
    "plus_t1pron_ex3_6": "elle s'est évanouie dans la salle",
    "plus_t1pron_ex3_7": "ils se sont soignés à la maison",
    # ── Mini-leçon « Les pronoms compléments » ──
    "plus_t2pcom_ana1": "je le change",
    "plus_t2pcom_lab3_d": "Je le change.",
    "plus_t2pcom_lab3_i": "Je lui parle.",
    "plus_t2pcom_lab3_e": "J'en ai besoin.",
    "plus_t2pcom_lab3_y": "J'y vais.",
    "plus_t2pcom_ex4_0": "Je change le pansement. Je le change.",
    "plus_t2pcom_ex4_1": "Je regarde la plaie. Je la regarde.",
    "plus_t2pcom_ex4_2": "Je prends les médicaments. Je les prends.",
    "plus_t2pcom_ex4_3": "Je parle au médecin. Je lui parle.",
    "plus_t2pcom_ex4_4": "Je réponds aux infirmières. Je leur réponds.",
    "plus_t2pcom_ex4_5": "J'ai besoin de crème. J'en ai besoin.",
    "plus_t2pcom_ex4_6": "Je vais à l'urgence. J'y vais.",
    "plus_t2pcom_ex4_7": "Je pense à mon rendez-vous. J'y pense.",
    # ── Mini-leçon « Le lien d'appartenance » ──
    "plus_t2app_ana1": "le dossier de Fatou",
    "plus_t2app_lab2_jm": "mon dossier",
    "plus_t2app_lab2_jf": "ma sœur",
    "plus_t2app_lab2_jp": "mes clés",
    "plus_t2app_lab2_im": "son dossier",
    "plus_t2app_lab2_if": "sa sœur",
    "plus_t2app_lab2_ip": "ses clés",
    "plus_t2app_lab2_em": "leur dossier",
    "plus_t2app_lab2_ef": "leur sœur",
    "plus_t2app_lab2_ep": "leurs clés",
    "plus_t2app_ex4_0": "Auriez-vous votre carte d'assurance maladie ?",
    "plus_t2app_ex4_1": "C'est le dossier de madame Diarra.",
    "plus_t2app_ex4_2": "Je viens chercher ma sœur.",
    "plus_t2app_ex4_3": "Son rendez-vous est à quinze heures.",
    "plus_t2app_ex4_4": "Les patients attendent leur tour.",
    "plus_t2app_ex4_5": "Les infirmières ont fini leurs quarts de travail.",
    "plus_t2app_ex4_6": "Elle s'est brûlé le bras.",
    "plus_t2app_ex4_7": "J'ai mal à la tête depuis ce matin.",
    # ── Mini-leçon « Poser une question polie » ──
    "plus_t3poli_ana1": "Pourriez-vous me donner son nom ?",
    "plus_t3poli_lab2_1x": "Donnez-moi son nom.",
    "plus_t3poli_lab2_1p": "Pourriez-vous me donner son nom ?",
    "plus_t3poli_lab2_2x": "Il y a un endroit où attendre ?",
    "plus_t3poli_lab2_2p": "Auriez-vous un endroit où attendre ?",
    "plus_t3poli_lab2_3x": "Je veux la rejoindre.",
    "plus_t3poli_lab2_3p": "Est-ce que je pourrais la rejoindre ?",
    "plus_t3poli_ex3_0": "Excusez-moi de vous déranger.",
    "plus_t3poli_ex3_1": "Pourriez-vous répéter, s'il vous plaît ?",
    "plus_t3poli_ex3_2": "Auriez-vous un formulaire à remplir ?",
    "plus_t3poli_ex3_3": "Est-ce que je pourrais avoir un reçu ?",
    "plus_t3poli_ex3_4": "Je voudrais parler à l'infirmière.",
    "plus_t3poli_ex3_5": "Sauriez-vous où se trouve la radiologie ?",
    "plus_t3poli_ex3_6": "Est-ce qu'il serait possible d'attendre ici ?",
    "plus_t3poli_ex3_7": "Merci beaucoup de votre aide.",
}

# Orthographe phonétique quand ElevenLabs prononce mal le mot réel.
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
        print("❌ AZURE_SPEECH_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / "assets/interactive/module-urgence/sons"
    out.mkdir(parents=True, exist_ok=True)

    # --force régénère tout ; sans l'option, on saute ce qui existe déjà, pour
    # pouvoir relancer après une coupure sans repayer les extraits déjà faits.
    force = "--force" in sys.argv

    ok = skip = fail = 0
    for file_id, text in CLIPS.items():
        dest = out / f"{file_id}.mp3"
        if dest.exists() and not force:
            skip += 1
            continue
        spoken = TEXT_OVERRIDES.get(file_id, text)
        print(f"  {file_id:26s} « {spoken[:44]} » → ", end="", flush=True)
        if generate(api_key, spoken, dest):
            print("✓"); ok += 1
        else:
            print("✗"); fail += 1
        time.sleep(0.35)   # ne pas saturer l'API

    print(f"\n✅ {ok} générés · {skip} déjà présents · {fail} en échec")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
