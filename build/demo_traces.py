#!/usr/bin/env python3
"""Classe de démonstration : six élèves et leurs traces sur le module 1.

Sert à montrer, en présentation, ce que l'enseignant voit une fois que le
groupe a travaillé — tableau de progression, journal d'accès, enregistrements
oraux, vocabulaire, « Corrige-moi ! ». Rien ici n'est un vrai élève.

    python3 build/demo_traces.py --install   # pose la démonstration
    python3 build/demo_traces.py --purge     # enlève tout ce qu'elle a écrit

Les données réelles sont sauvegardées dans data/_sauvegarde-avant-demo/ au
premier --install, et --purge se contente de retirer les enregistrements dont
l'identifiant d'élève appartient à la démonstration : le reste n'est jamais
touché.
"""

import argparse
import json
import shutil
from datetime import date, datetime, timedelta
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DATA = RACINE / "data"
SAUVEGARDE = DATA / "_sauvegarde-avant-demo"
AUDIO_DEPOTS = RACINE / "assets" / "oral-submissions"
# Les trois prises produites par build/demo_audio.py — trois voix qui ne sont
# pas celles des personnages du module. À défaut (synthèse jamais lancée), on
# se rabat sur une réplique du dialogue : la démonstration a alors un fichier
# qui joue, mais on reconnaît le comédien.
AUDIO_VOIX = RACINE / "build" / "demo-voix"
AUDIO_SOURCE = RACINE / "assets" / "interactive" / "module-consultation" / "prep"

GROUPE = 1
ACTIVITE = 35
TITRE = "Module 1 — Consulter au bon endroit"
ZONES = 123  # nombre de zones réellement présentes dans le module

FICHIERS = [
    "students.json", "access_log.json", "progress.json",
    "vocab_progress.json", "corrige_moi.json", "oral_submissions.json",
    "written_submissions.json",
]

# ── Les six élèves ──────────────────────────────────────────────────────────
# Chaque profil illustre une colonne du tableau de l'enseignant : la classe
# n'est utile en présentation que si on y voit un élève en avance, un élève
# qui s'accroche, et un élève qui n'a pas commencé.
# Les élèves se donnent un pseudo, jamais leur vrai nom : la démonstration
# montre la convention en même temps qu'elle montre le portail.
ELEVES = [
    {"id": 101, "code": "ETOI42", "prenom": "Étoile", "nom": "Étoile"},
    {"id": 102, "code": "CACT47", "prenom": "Cactus", "nom": "Cactus"},
    {"id": 103, "code": "BAMB83", "prenom": "Bambou", "nom": "Bambou"},
    {"id": 104, "code": "TULI55", "prenom": "Tulipe", "nom": "Tulipe"},
    {"id": 105, "code": "ERAB23", "prenom": "Érable", "nom": "Érable"},
    {"id": 106, "code": "COLI94", "prenom": "Colibri", "nom": "Colibri"},
]
IDS_DEMO = {e["id"] for e in ELEVES}

# Travail fait sur le module par chaque élève.
#   jours   : décalage en jours par rapport à aujourd'hui pour la dernière trace
#   dialogue: a écouté les dialogues du « Je découvre »
#   zones   : zones réussies sur les 123 du module (None = n'a rien commencé)
TRAVAIL = [
    {"id": 101, "jours": 0, "dialogue": True,  "zones": 123, "premier": 108, "erreurs": 19, "heure": "10:42:11"},
    {"id": 102, "jours": 0, "dialogue": True,  "zones": 86,  "premier": 61,  "erreurs": 44, "heure": "11:05:38"},
    {"id": 103, "jours": 1, "dialogue": True,  "zones": 14,  "premier": 11,  "erreurs": 6,  "heure": "09:58:02"},
    {"id": 104, "jours": 0, "dialogue": True,  "zones": 123, "premier": 54,  "erreurs": 97, "heure": "13:27:45"},
    {"id": 105, "jours": 1, "dialogue": True,  "zones": 47,  "premier": 38,  "erreurs": 22, "heure": "14:12:29"},
    {"id": 106, "jours": 2, "dialogue": False, "zones": None, "premier": None, "erreurs": None, "heure": "08:47:53"},
]

# Traces sur d'autres activités, les jours précédents. Sans elles, la série de
# jours consécutifs et la régularité de la semaine resteraient à un seul jour :
# le tableau de bord de l'élève compte des dates, pas des exercices.
ANNEXES = [
    # (élève, activité, titre, jours, heure, zones faites sur le total, 1er coup, erreurs)
    (101, 4,  "À la clinique", 1, "09:20:14", 18, 22, 16, 8),
    (101, 31, "Vocabulaire — Cartes mémoire", 2, "19:05:33", None, None, None, None),
    (102, 4,  "À la clinique", 2, "10:44:09", 22, 22, 14, 17),
    (102, 31, "Vocabulaire — Cartes mémoire", 1, "18:32:57", None, None, None, None),
    (104, 4,  "À la clinique", 1, "13:11:26", 12, 22, 5, 31),
    (104, 29, "Corrige-moi ! (assistant oral)", 2, "13:48:40", None, None, None, None),
    (105, 4,  "À la clinique", 3, "15:02:51", 19, 22, 15, 11),
    (103, 31, "Vocabulaire — Cartes mémoire", 2, "09:36:12", None, None, None, None),
]

# Journal d'accès : les fichiers de séance ouverts depuis le portail élève.
CONSULTATIONS = [
    (101, 0, "10:31:04", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (101, 1, "16:20:47", "assets/powerpoints/module-consultation/A1-le-genou-de-yannick.pptx"),
    (102, 0, "10:58:12", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (102, 2, "09:14:33", "assets/documents/module-consultation-a2-trois-sons-dans-le-nez.html"),
    (103, 1, "09:41:19", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (104, 0, "13:02:55", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (104, 1, "17:38:21", "assets/documents/module-consultation-a2-trois-sons-dans-le-nez.html"),
    (105, 1, "13:55:07", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
    (106, 2, "08:46:30", "assets/documents/module-consultation-a1-le-genou-de-yannick.html"),
]

# Productions orales déposées (« Je me lance »). La transcription est celle que
# l'élève a lue à l'écran ; la rétroaction, celle que la correction lui a rendue.
ORAUX = [
    {
        "eleve": 101, "jours": 0, "heure": "10:47:52", "audio": "line_02_rosalie.mp3",
        "transcription": "Bonjour, j'ai mal au genou depuis trois jours. La douleur est forte quand je monte les escaliers et le genou est enflé.",
        "feedback": "Phrase correcte : Bonjour, j'ai mal au genou depuis trois jours. La douleur est forte quand je monte les escaliers et le genou est enflé.",
    },
    {
        "eleve": 105, "jours": 1, "heure": "14:19:36", "audio": "line_03_yannick.mp3",
        "transcription": "J'ai mal à la gorge depuis lundi et je tousse beaucoup. J'ai pas de fièvre mais ça empire le soir.",
        "feedback": "Correction : J'ai mal à la gorge depuis lundi et je tousse beaucoup. Je n'ai pas de fièvre, mais ça empire le soir. | À l'écrit et devant un professionnel, on garde le « ne » : « je n'ai pas de fièvre ». Une virgule avant « mais » sépare les deux idées.",
    },
    {
        "eleve": 102, "jours": 1, "heure": "11:12:04", "audio": "line_04_rosalie.mp3",
        "transcription": "Je voudrais prendre un rendez-vous. Ma fille elle a de la fièvre depuis hier soir.",
        "feedback": "Correction : Je voudrais prendre un rendez-vous. Ma fille a de la fièvre depuis hier soir. | On ne répète pas le sujet : « ma fille a », et non « ma fille elle a ».",
    },
]

# Productions écrites déposées (« Je me lance », deuxième carte).
ECRITS = [
    {
        "eleve": 101, "jours": 0, "heure": "10:55:31",
        "texte": "Bonjour,\nJe vous écris pour demander un rendez-vous. J'ai mal au genou "
                 "depuis trois jours et la douleur ne passe pas. Je suis disponible mercredi "
                 "après-midi et jeudi toute la journée. Est-ce que vous avez une place cette "
                 "semaine ?\nMerci beaucoup,\nÉtoile",
        "feedback": "Correction : Bonjour, Je vous écris pour demander un rendez-vous. J'ai mal au "
                    "genou depuis trois jours et la douleur ne passe pas. Je suis disponible mercredi "
                    "après-midi et jeudi toute la journée. Auriez-vous une place cette semaine ? "
                    "| « Est-ce que vous avez » est correct, mais « auriez-vous » est plus poli dans "
                    "un courriel à une clinique.",
    },
    {
        "eleve": 104, "jours": 0, "heure": "13:52:09",
        "texte": "Bonjour,\nJe veux un rendez-vous. Ça fait deux semaine que j'ai mal au dos. "
                 "Je peux venir le matin. Merci.",
        "feedback": "Correction : Bonjour, Je voudrais un rendez-vous. Ça fait deux semaines que j'ai "
                    "mal au dos. Je peux venir le matin. Merci. | « Je veux » est trop direct : on "
                    "écrit « je voudrais ». Après « deux », le nom se met au pluriel : « deux semaines ».",
    },
    {
        "eleve": 102, "jours": 1, "heure": "11:34:22",
        "texte": "Bonjour,\nMa fille a de la fièvre depuis hier soir et elle tousse. Je voudrais "
                 "un rendez-vous aujourd'hui si c'est possible. Je suis libre après quinze heures.\n"
                 "Merci,\nCactus",
        "feedback": "Phrase correcte : Bonjour, Ma fille a de la fièvre depuis hier soir et elle tousse. "
                    "Je voudrais un rendez-vous aujourd'hui si c'est possible. Je suis libre après "
                    "quinze heures. Merci, Cactus",
    },
]

# « Corrige-moi ! » : cumul par thème, comme le tient le serveur.
CORRIGE_MOI = [
    {"eleve": 101, "reponses": 24, "premier": 19, "jours": 0, "heure": "10:52:18"},
    {"eleve": 102, "reponses": 16, "premier": 9,  "jours": 1, "heure": "11:21:47"},
    {"eleve": 104, "reponses": 11, "premier": 4,  "jours": 0, "heure": "13:41:02"},
    {"eleve": 105, "reponses": 8,  "premier": 5,  "jours": 1, "heure": "14:26:55"},
]

# Cartes mémoire du domaine Santé (w1 à w11 de la banque du serveur).
# box 0 = à revoir tout de suite, 5 = su. On donne un profil par élève.
VOCABULAIRE = {
    101: [5, 5, 4, 5, 4, 4, 5, 3, 4, 3, 2],
    102: [4, 3, 3, 2, 3, 2, 4, 1, 2, 1],
    103: [2, 1, 1, 0],
    104: [3, 2, 1, 1, 2, 0, 2, 0, 1],
    105: [3, 3, 2, 2, 1, 1, 2],
}
INTERVALLES = [1, 2, 4, 8, 16, 32]


def horodatage(jours, heure):
    return f"{(date.today() - timedelta(days=jours)).isoformat()}T{heure}"


def charger(nom, defaut):
    chemin = DATA / nom
    if not chemin.exists():
        return defaut
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def ecrire(nom, contenu):
    DATA.mkdir(parents=True, exist_ok=True)
    with open(DATA / nom, "w", encoding="utf-8") as f:
        json.dump(contenu, f, ensure_ascii=False, indent=2)


def sauvegarder():
    """Copie les fichiers réels une seule fois, avant la première démonstration."""
    if SAUVEGARDE.exists():
        return False
    SAUVEGARDE.mkdir(parents=True)
    for nom in FICHIERS:
        source = DATA / nom
        if source.exists():
            shutil.copy2(source, SAUVEGARDE / nom)
    return True


def sans_demo(entrees, cle="studentId"):
    return [e for e in entrees if e.get(cle) not in IDS_DEMO]


def installer():
    neuve = sauvegarder()

    # ── Élèves ──────────────────────────────────────────────────────────
    eleves = sans_demo(charger("students.json", []), "id")
    aujourdhui = date.today().isoformat()
    for e in ELEVES:
        eleves.append({
            "id": e["id"], "code": e["code"], "label": e["nom"],
            "prenom": e["prenom"], "groupId": GROUPE, "createdAt": aujourdhui,
        })
    ecrire("students.json", eleves)
    par_id = {e["id"]: e for e in ELEVES}

    # ── Progression sur le module ───────────────────────────────────────
    progression = sans_demo(charger("progress.json", []))
    for t in TRAVAIL:
        e = par_id[t["id"]]
        base = {
            "studentId": e["id"], "studentLabel": e["nom"], "groupId": GROUPE,
            "activityId": ACTIVITE, "activityTitle": TITRE,
            "score": None, "zones": None, "zonesDone": None,
            "firstTry": None, "totalErrors": None,
        }
        ouverture = horodatage(t["jours"], t["heure"])
        progression.append(dict(base, event="file_opened", timestamp=ouverture))
        if t["dialogue"]:
            progression.append(dict(base, event="dialogue_listened", timestamp=ouverture))
        if t["zones"] is not None:
            progression.append(dict(
                base, event="exercise_completed", zones=ZONES, zonesDone=t["zones"],
                firstTry=t["premier"], totalErrors=t["erreurs"], timestamp=ouverture,
            ))
    for eleve_id, act_id, titre, jours, heure, faites, total, premier, erreurs in ANNEXES:
        e = par_id[eleve_id]
        moment = horodatage(jours, heure)
        base = {
            "studentId": e["id"], "studentLabel": e["nom"], "groupId": GROUPE,
            "activityId": act_id, "activityTitle": titre,
            "score": None, "zones": None, "zonesDone": None,
            "firstTry": None, "totalErrors": None,
        }
        progression.append(dict(base, event="file_opened", timestamp=moment))
        if faites is not None:
            progression.append(dict(
                base, event="exercise_completed", zones=total, zonesDone=faites,
                firstTry=premier, totalErrors=erreurs, timestamp=moment,
            ))
    progression.sort(key=lambda p: p.get("timestamp", ""))
    ecrire("progress.json", progression)

    # ── Journal d'accès ─────────────────────────────────────────────────
    journal = sans_demo(charger("access_log.json", []))
    for eleve_id, jours, heure, fichier in CONSULTATIONS:
        e = par_id[eleve_id]
        journal.append({
            "studentId": e["id"], "studentLabel": e["nom"], "groupId": GROUPE,
            "activityId": ACTIVITE, "activityTitle": TITRE,
            "file": fichier, "timestamp": horodatage(jours, heure),
        })
    journal.sort(key=lambda x: x.get("timestamp", ""))
    ecrire("access_log.json", journal)

    # ── Enregistrements oraux ───────────────────────────────────────────
    AUDIO_DEPOTS.mkdir(parents=True, exist_ok=True)
    depots = sans_demo(charger("oral_submissions.json", []))
    for i, o in enumerate(ORAUX, start=1):
        e = par_id[o["eleve"]]
        nom_fichier = f"demo{i}-{e['code'].lower()}.mp3"
        voix = AUDIO_VOIX / f"{e['code'].lower()}.mp3"
        source = voix if voix.exists() else AUDIO_SOURCE / o["audio"]
        if source.exists():
            shutil.copy2(source, AUDIO_DEPOTS / nom_fichier)
            if source is not voix:
                print(f"[!] {e['code']} : pas de voix de démonstration, "
                      f"réplique du module utilisée (python3 build/demo_audio.py)")
        else:
            print(f"[!] audio introuvable : {source}")
        depots.append({
            "id": f"demo-{e['code'].lower()}",
            "studentId": e["id"], "studentCode": e["code"], "groupId": GROUPE,
            "prenom": e["prenom"], "theme": "Santé",
            "taskId": "module-consultation-po",
            "taskLabel": "Production orale — décrire une douleur",
            "question": "Décrire une douleur à un professionnel de la santé",
            "transcription": o["transcription"], "feedback": o["feedback"],
            "audioUrl": f"/assets/oral-submissions/{nom_fichier}",
            "createdAt": horodatage(o["jours"], o["heure"]),
        })
    ecrire("oral_submissions.json", depots)

    # ── Productions écrites ─────────────────────────────────────────────
    textes = sans_demo(charger("written_submissions.json", []))
    for e_ecrit in ECRITS:
        e = par_id[e_ecrit["eleve"]]
        textes.append({
            "id": f"demo-ecrit-{e['code'].lower()}",
            "studentId": e["id"], "studentCode": e["code"], "groupId": GROUPE,
            "prenom": e["prenom"], "theme": "Santé",
            "taskId": "module-consultation-pe",
            "taskLabel": "Écris pour demander un rendez-vous",
            "question": "Ta douleur ne passe pas. Écris à la clinique sans rendez-vous pour "
                        "obtenir un rendez-vous cette semaine.",
            "texte": e_ecrit["texte"], "feedback": e_ecrit["feedback"],
            "createdAt": horodatage(e_ecrit["jours"], e_ecrit["heure"]),
        })
    ecrire("written_submissions.json", textes)

    # ── « Corrige-moi ! » ───────────────────────────────────────────────
    cumuls = sans_demo(charger("corrige_moi.json", []))
    for c in CORRIGE_MOI:
        e = par_id[c["eleve"]]
        cumuls.append({
            "studentId": e["id"], "studentLabel": e["nom"], "groupId": GROUPE,
            "themeId": "sante", "themeLabel": "Santé",
            "answers": c["reponses"], "firstTryOk": c["premier"],
            "lastSeen": horodatage(c["jours"], c["heure"]),
        })
    ecrire("corrige_moi.json", cumuls)

    # ── Cartes mémoire ──────────────────────────────────────────────────
    vocab = sans_demo(charger("vocab_progress.json", []))
    for eleve_id, boites in VOCABULAIRE.items():
        for i, boite in enumerate(boites, start=1):
            revu = horodatage(i % 3, "12:00:00")
            vocab.append({
                "studentId": eleve_id, "wordId": f"w{i}", "box": boite,
                "dueDate": (date.fromisoformat(revu[:10])
                            + timedelta(days=INTERVALLES[boite])).isoformat(),
                "lastReview": revu,
            })
    ecrire("vocab_progress.json", vocab)

    print(f"Démonstration posée : {len(ELEVES)} élèves sur « {TITRE} ».")
    for e in ELEVES:
        print(f"  {e['code']}  {e['nom']}")
    if neuve:
        print(f"Données réelles sauvegardées dans {SAUVEGARDE.relative_to(RACINE)}/")
    print("Retrait : python3 build/demo_traces.py --purge")


def purger():
    for nom in ("students.json",):
        ecrire(nom, sans_demo(charger(nom, []), "id"))
    for nom in ("progress.json", "access_log.json", "corrige_moi.json",
                "vocab_progress.json", "oral_submissions.json",
                "written_submissions.json"):
        ecrire(nom, sans_demo(charger(nom, [])))
    for fichier in AUDIO_DEPOTS.glob("demo*-*.mp3"):
        fichier.unlink()
    print("Démonstration retirée. Les autres élèves et leurs traces sont intacts.")
    if SAUVEGARDE.exists():
        print(f"(La sauvegarde d'avant la démonstration reste dans "
              f"{SAUVEGARDE.relative_to(RACINE)}/)")


if __name__ == "__main__":
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument("--install", action="store_true", help="poser la classe de démonstration")
    parseur.add_argument("--purge", action="store_true", help="retirer la classe de démonstration")
    args = parseur.parse_args()
    if args.purge:
        purger()
    elif args.install:
        installer()
    else:
        parseur.print_help()
