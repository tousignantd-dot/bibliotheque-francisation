#!/usr/bin/env python3
"""
Générateur d'audio — boutons d'écoute des mini-leçons « Ouvrir la mini-leçon »
du module « module-travail ».

fileId → texte lu ; doit correspondre aux appels playWord() générés par
plAudioId() dans le HTML. Pour régénérer cette liste après une modification de
l'objet PLUS : ouvrir le module dans le navigateur et lancer plAudioManifest()
dans la console — elle renvoie exactement ce dictionnaire.

Voix unique (narrateur) — même voix que les mots isolés du module.
"""
import os, sys, time
from pathlib import Path
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés

try:
    import requests
except ImportError:
    print("❌ pip install requests"); sys.exit(1)

VOICE = "IPgYtHTNLjC7Bq7IPHrm"

CLIPS = {
    "plus_prPhon_ana1": "père",
    "plus_prPhon_ana2": "dépanné",
    "plus_prPhon_lab3_a": "père",
    "plus_prPhon_lab3_b": "dépanné",
    "plus_prPhon_lab3_c": "hiver",
    "plus_prPhon_lab3_d": "je travaillerai",
    "plus_prPhon_ex4_0": "père",
    "plus_prPhon_ex4_1": "tête",
    "plus_prPhon_ex4_2": "treize",
    "plus_prPhon_ex4_3": "semaine",
    "plus_prPhon_ex4_4": "nouvelle",
    "plus_prPhon_ex4_5": "hiver",
    "plus_prPhon_ex4_6": "dépanné",
    "plus_prPhon_ex4_7": "je travaillerai",
    "plus_prPhon_ex4_8": "dépanner",
    "plus_prPhon_ex4_9": "mer",
    "plus_t1qui_ana1": "le rapport qui doit être signé",
    "plus_t1qui_lab2_c": "Le collègue qui remplace Karim s'appelle Omar.",
    "plus_t1qui_lab2_s": "J'ai trouvé la salle qui convient pour la réunion.",
    "plus_t1qui_lab2_e": "L'entreprise qui embauche est au centre-ville.",
    "plus_t1qui_ex3_0": "Voici le rapport qui doit être signé.",
    "plus_t1qui_ex3_1": "Le collègue qui remplace Karim s'appelle Omar.",
    "plus_t1qui_ex3_2": "J'ai trouvé la salle qui convient.",
    "plus_t1qui_ex3_3": "C'est l'infirmière qui nous a appelés.",
    "plus_t1qui_ex3_4": "L'entreprise qui embauche est au centre-ville.",
    "plus_t1qui_ex3_5": "La direction a averti les employés qui étaient en retard.",
    "plus_t1situ_ana1": "Sofian est en retard à cause d'un rendez-vous chez le dentiste",
    "plus_t1situ_ana2": "Karim est absent parce que sa fille est malade",
    "plus_t1situ_lab3_r": "un retard",
    "plus_t1situ_lab3_a": "une absence",
    "plus_t1situ_lab3_b": "un abandon",
    "plus_t1situ_ex4_0": "Sofian arrive en retard à cause d'un rendez-vous chez le dentiste.",
    "plus_t1situ_ex4_1": "Karim reste à la maison parce que sa fille est malade.",
    "plus_t1situ_ex4_2": "Une famille déménage loin du centre de formation.",
    "plus_t1situ_ex4_3": "Une personne part trois semaines voir sa famille à l'étranger.",
    "plus_t1situ_ex4_4": "Une personne a manqué son autobus et attend le suivant.",
    "plus_t2connect_ana1": "il a parlé à la responsable et elle lui a donné les informations",
    "plus_t2connect_ana2": "j'aimerais prendre ce cours, mais il se donne seulement à l'hiver",
    "plus_t2connect_lab3_e": "J'ai révisé mes verbes, et demain je réviserai le vocabulaire.",
    "plus_t2connect_lab3_o": "Tu choisis maintenant ou tu attends à demain.",
    "plus_t2connect_lab3_m": "J'aimerais t'accompagner, mais je dois travailler.",
    "plus_t2connect_ex4_0": "Tu préviens ton superviseur ou tu envoies un courriel ?",
    "plus_t2connect_ex4_1": "J'aimerais t'accompagner, mais je dois travailler.",
    "plus_t2connect_ex4_2": "Elle fait du bénévolat, mais elle préfère le plein air.",
    "plus_t2connect_ex4_3": "À midi, tu manges à la cafétéria ou tu apportes ton repas ?",
    "plus_t2connect_ex4_4": "J'aimerais suivre ce cours, mais l'horaire ne convient pas.",
    "plus_t2connect_ex4_5": "Hier, j'ai révisé mes verbes, et demain je réviserai le vocabulaire.",
    "plus_t2quel_ana1": "Quelle est la raison de ton retard ?",
    "plus_t2quel_ana2": "Quels sont les avantages de ton nouvel horaire ?",
    "plus_t2quel_lab3_ms": "Quel est ton objectif ?",
    "plus_t2quel_lab3_mp": "Quels sont les critères ?",
    "plus_t2quel_lab3_fs": "Quelle est ton adresse ?",
    "plus_t2quel_lab3_fp": "Quelles sont tes habiletés ?",
    "plus_t2quel_ex4_0": "Quelle est la raison de ton retard ?",
    "plus_t2quel_ex4_1": "Quels sont les avantages de ton horaire ?",
    "plus_t2quel_ex4_2": "Quelles sont tes habitudes le matin ?",
    "plus_t2quel_ex4_3": "Quel est ton objectif principal ?",
    "plus_t2quel_ex4_4": "Quels sont les inconvénients de ce trajet ?",
    "plus_t2quel_ex4_5": "Quelles sont les matières que tu préfères ?",
    "plus_t2quel_ex4_6": "Quel est le but de ta demande ?",
    "plus_t2quel_ex4_7": "Quelle est ton opinion sur ce règlement ?",
    "plus_t3formel_ana1": "Bonjour Madame, Sincères salutations",
    "plus_t3formel_ana2": "Bonjour Karim, à bientôt",
    "plus_t3formel_lab3_o": "Bonjour Madame, Sincères salutations",
    "plus_t3formel_lab3_f": "Salut Nadia, à bientôt",
    "plus_t3formel_ex4_0": "Message à un collègue avec qui on prend souvent la pause.",
    "plus_t3formel_ex4_1": "Message à l'infirmière de l'école, rencontrée une seule fois.",
    "plus_t3formel_ex4_2": "Message à un voisin qui garde parfois notre chat.",
    "plus_t3formel_ex4_3": "Message à une superviseure depuis deux semaines.",
    "plus_t3formel_ex4_4": "Message à la directrice du centre de formation.",
    "plus_t3formel_ex4_5": "Message à un enseignant avec qui on a fait du bénévolat.",
    "plus_t3devoir_ana1": "je dois m'inscrire aujourd'hui",
    "plus_t3devoir_ana2": "il faut remplir le formulaire jaune",
    "plus_t3devoir_lab3_j": "Je dois arriver à l'heure.",
    "plus_t3devoir_lab3_n": "Nour doit demander une explication.",
    "plus_t3devoir_lab3_x": "Il faut justifier son retard par écrit.",
    "plus_t3devoir_ex4_0": "Je dois aller chez le dentiste dans vingt minutes.",
    "plus_t3devoir_ex4_1": "Nour doit demander une explication à sa collègue.",
    "plus_t3devoir_ex4_2": "Il faut expliquer la procédure aux nouveaux employés.",
    "plus_t3devoir_ex4_3": "Il faut justifier votre retard par écrit avant midi.",
    "plus_t3devoir_ex4_4": "J'écris un courriel à mon enseignante : je dois le faire aujourd'hui.",
}

TEXT_OVERRIDES = {}


def generate(api_key, text, path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}"
    payload = {"text": text, "model_id": "eleven_multilingual_v2",
               "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
    r = requests.post(url, json=enrichir(payload),
                      headers={"xi-api-key": api_key, "Content-Type": "application/json"},
                      timeout=45)
    if r.status_code != 200:
        print(f"   ❌ {r.status_code}: {r.text[:150]}")
        return False
    path.write_bytes(r.content)
    return True


def main():
    print(f"🔊 Mini-leçons « Ouvrir la mini-leçon » — {len(CLIPS)} extraits\n")
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        print("❌ ELEVENLABS_API_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / "assets/interactive/module-travail/sons"
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
