#!/usr/bin/env python3
"""Les traces d'élèves du bac à sable : une classe qui a travaillé.

    python3 build/tutoriels/traces_demo.py <port>
    python3 build/tutoriels/traces_demo.py <port> --etat     # ce qu'il y a
    python3 build/tutoriels/traces_demo.py <port> --rafraichir  # rien que le direct

`peupler_demo.py` fabrique des groupes, des élèves et des dates : de quoi
filmer la planification. Mais **personne n'a jamais rien fait** — chaque élève
y est « jamais venu · dernière étape : — », et les trois écrans qui racontent
la classe (progression du groupe, dossier d'un élève, direct) n'ont donc rien
à montrer. On ne peut pas expliquer un tableau de bord vide.

Ce script pose donc des traces, **par les routes publiques de l'élève**, avec
le code de chacun — exactement ce que fait un module dans un navigateur. Rien
n'est écrit à la main dans le volume : une trace posée à la main ne prouverait
pas que la chaîne fonctionne, et c'est elle qu'on filme.

Tout est inventé, et volontairement **inégal** : c'est le seul état d'écran
qui apprenne quelque chose. Une classe où tout le monde est à 100 % ne montre
ni le taux du premier coup, ni la question ratée par la moitié du groupe, ni
l'élève qui n'est jamais venu — donc rien de ce que l'enseignante vient
chercher.

Idempotent : `progress.json` et `direct.json` gardent **un** enregistrement
par (élève, activité, événement) et par (élève, activité, zone). Le relancer
réécrit les mêmes lignes au lieu d'en empiler.
"""
import json
import os
import random
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

PORT = sys.argv[1] if len(sys.argv) > 1 else "5321"
BASE = "http://localhost:%s" % PORT
ETAT = "--etat" in sys.argv
REPARTIR = "--repartir" in sys.argv
# Reposer les seules réponses du direct, à l'identique. Le compte « en ligne »
# du portail ne retient que dix minutes (`DIRECT_EN_LIGNE_MIN`) et se lit sur
# ces réponses-là, pas sur les accès : un bac à sable peuplé avant le tournage
# affiche « 0 élève en ligne » dès la douzième minute, et la capsule qui parle
# de la classe au travail montrait une classe vide. Le hasard étant semé et le
# serveur ne gardant qu'un enregistrement par (élève, activité, zone), rejouer
# la même boucle réécrit les mêmes lignes : seule leur heure change.
RAFRAICHIR = "--rafraichir" in sys.argv

# Le hasard est **semé** : deux passages donnent la même classe. Sans cela, la
# copie d'écran du guide changerait à chaque relance et on ne saurait jamais
# si un écart vient du code ou du tirage.
DE = random.Random(47)


def identifiants():
    bac = Path(os.environ.get(
        "STORAGE_DIR", Path(tempfile.gettempdir()) / "francisation-demo-tutoriels"))
    f = bac / "identifiants-demo.json"
    if f.exists():
        return json.loads(f.read_text())
    if os.environ.get("PROF_CODE") and os.environ.get("PROF_MOTDEPASSE"):
        return {"code": os.environ["PROF_CODE"], "motDePasse": os.environ["PROF_MOTDEPASSE"]}
    sys.exit("Identifiants introuvables. Lancez d'abord ./build/tutoriels/lancer_demo.sh")


def repartir():
    """Vide les traces avant d'en reposer — **bac à sable seulement**.

    L'avancement et le direct sont idempotents (un enregistrement par élève et
    par zone, réécrit), mais les productions écrites et les participants de
    séance s'ajoutent : relancer cinq fois montrait le même texte cinq fois
    sous la rangée d'un élève, et « 10 élèves sur 33 en ligne » pour une classe
    de douze. Une copie d'écran qui donne cette impression-là dessert le guide.

    On efface donc les fichiers du **volume jetable**, jamais par une route :
    le portail n'offre pas de « tout effacer », et il n'a pas à en offrir une
    pour les besoins d'un tournage. Le garde-fou est le chemin lui-même — si
    `STORAGE_DIR` n'est pas le bac des tutoriels, on refuse.
    """
    bac = Path(os.environ.get(
        "STORAGE_DIR", Path(tempfile.gettempdir()) / "francisation-demo-tutoriels"))
    if "demo-tutoriels" not in bac.name:
        sys.exit("STORAGE_DIR (%s) n'est pas le bac des tutoriels — refus." % bac)
    for nom in ("direct.json", "written_submissions.json", "oral_submissions.json",
                "progress.json", "seances.json", "access_log.json"):
        f = bac / "data" / nom
        if f.exists():
            f.unlink()
            print("  effacé %s" % nom)


def appel(chemin, corps=None, methode=None, jeton=None):
    donnees = json.dumps(corps).encode() if corps is not None else None
    req = urllib.request.Request(BASE + chemin, data=donnees,
                                 method=methode or ("POST" if donnees else "GET"))
    req.add_header("Content-Type", "application/json")
    if jeton:
        req.add_header("X-Prof-Token", jeton)
    try:
        with urllib.request.urlopen(req) as r:
            brut = r.read().decode()
    except urllib.error.HTTPError as e:
        raise SystemExit("%s %s → %s %s" % (methode or "GET", chemin, e.code,
                                            e.read().decode()[:200]))
    return json.loads(brut) if brut else {}


# ── Le module travaillé, et les zones du direct ──────────────────────────────
# Tirés de `module-travail` (activité 39), exercice `pr1` — le vrai texte du
# vrai module. Le serveur ne connaît pas les modules : l'énoncé voyage avec la
# réponse, c'est donc au module (ici, à ce script) de le fournir. `verifier()`
# relit le module et prévient si un énoncé n'y est plus, pour que la fixture ne
# dérive pas en silence.
MODULE = 39
MODULE_TITRE = "Module 4 — Absent ou en retard : que faire ?"
MODULE_HTML = ("assets/interactive/module-travail/"
               "module-travail-activite-interactive.html")
ATELIER = 4
ATELIER_TITRE = "À la clinique"

ZONES = [
    {"zone": "pr1a", "type": "vf", "bonne": "FAUX",
     "enonce": "C'est Nadia qui appelle Karim pour lui dire que sa fille est malade."},
    {"zone": "pr1b", "type": "vf", "bonne": "VRAI",
     "enonce": "Karim doit aller chercher sa fille à l'école."},
    {"zone": "pha", "type": "vf", "bonne": "[ɛ]", "enonce": "père"},
    {"zone": "phb", "type": "vf", "bonne": "[e]", "enonce": "travaillerai"},
]
# La zone que la classe rate : c'est elle qui donne son sens à l'écran. Une
# grille toute verte n'apprend rien à personne.
ZONE_RATEE = "phb"


def verifier(racine):
    """La fixture cite le module : on vérifie qu'elle le cite encore juste."""
    fichier = racine / MODULE_HTML
    if not fichier.exists():
        print("  ⚠ module introuvable (%s) — énoncés non vérifiés" % MODULE_HTML)
        return
    html = fichier.read_text(encoding="utf-8")
    for z in ZONES:
        if z["enonce"] not in html:
            print("  ⚠ « %s » n'est plus dans le module : la fixture a dérivé"
                  % z["enonce"][:50])


# ── Ce que chaque élève a fait ───────────────────────────────────────────────
# Inégal par construction. `avance` est la part des zones faites, `premier` le
# taux de bonnes réponses du premier coup. Les trois derniers de la liste ne
# reçoivent rien : une classe a toujours des absents, et l'écran doit le dire.
PARCOURS = [
    {"avance": 1.00, "premier": 0.92, "atelier": True,  "ecrit": True},
    {"avance": 1.00, "premier": 0.71, "atelier": True},
    {"avance": 0.85, "premier": 0.83, "atelier": True,  "ecrit": True},
    {"avance": 0.72, "premier": 0.55},
    {"avance": 0.66, "premier": 0.78, "atelier": True},
    {"avance": 0.55, "premier": 0.40},
    {"avance": 0.44, "premier": 0.62},
    {"avance": 0.33, "premier": 0.85},
    {"avance": 0.16, "premier": 0.50},
]

ECRITS = [
    ("Bonjour madame Tremblay, je vous écris parce que je serai absent demain "
     "matin. Mon fils est malade et je dois aller à la clinique avec lui. "
     "Je vais rattraper les exercices du défi 2 en soirée. Merci de votre "
     "compréhension."),
    ("Bonjour, je vais arriver en retard jeudi. J'ai un rendez-vous à neuf "
     "heures et l'autobus 55 passe seulement aux vingt minutes. Je serai là "
     "vers dix heures. Bonne journée."),
]


def direct(eleves):
    """Les réponses de la classe, question par question.

    Sortie en fonction pour être rejouable seule (`--rafraichir`). Elle doit
    tirer le hasard **dans le même ordre** qu'un passage complet, sans quoi la
    classe changerait de visage : rien avant elle ne consomme `DE`, et rien ne
    doit s'y glisser.
    """
    lignes = 0
    for eleve, part in zip(eleves, PARCOURS):
        for z in ZONES:
            # Ceux qui n'ont pas fini n'ont pas atteint les dernières zones.
            if DE.random() > part["avance"]:
                continue
            rate = z["zone"] == ZONE_RATEE
            ok = DE.random() < (0.25 if rate else part["premier"])
            appel("/api/student/progress", {
                "code": eleve["code"], "activityId": MODULE,
                "activityTitle": MODULE_TITRE, "event": "zone_repondue",
                "section": "prep", "exo": z["zone"][:3], "exoNum": "Exercice 1",
                "exoTitre": "Vrai ou Faux — Un départ précipité",
                "type": z["type"], "zone": z["zone"], "enonce": z["enonce"],
                "bonne": z["bonne"],
                "reponse": z["bonne"] if ok else "(autre réponse)",
                "ok": ok, "essais": 1 if ok else DE.choice([2, 2, 3])})
            lignes += 1
    return lignes


def main():
    racine = Path(__file__).resolve().parent.parent.parent
    jeton = appel("/api/prof/login", identifiants())["token"]
    groupes = appel("/api/prof/groupes", jeton=jeton)
    groupes = groupes if isinstance(groupes, list) else groupes.get("groupes", [])
    groupe = next((g for g in groupes
                   if "avant-midi" in (g.get("name") or g.get("nom") or "")), groupes[0])
    gid = groupe["id"]
    eleves = appel("/api/admin/students?groupId=%s" % gid, jeton=jeton)
    eleves = eleves if isinstance(eleves, list) else eleves.get("students", [])
    eleves = [e for e in eleves if e.get("code")]

    if ETAT:
        print("groupe %s · %d élèves" % (groupe.get("name") or groupe.get("nom"), len(eleves)))
        for chemin, nom in (("/api/direct?groupId=%s&activityId=%s" % (gid, MODULE), "direct"),
                            ("/api/admin/written-submissions?groupId=%s" % gid, "écrits"),
                            ("/api/prof/seances?groupId=%s" % gid, "séances")):
            try:
                r = appel(chemin, jeton=jeton)
                print("  %-8s %s" % (nom, json.dumps(r, ensure_ascii=False)[:120]))
            except SystemExit as e:
                print("  %-8s %s" % (nom, e))
        return

    if RAFRAICHIR:
        print("  %d réponses au direct reposées" % direct(eleves))
        return

    if REPARTIR:
        repartir()
    verifier(racine)

    # ── L'avancement, par les routes de l'élève ──
    pose = 0
    for eleve, part in zip(eleves, PARCOURS):
        code = eleve["code"]
        zones, faites = 24, max(1, round(24 * part["avance"]))
        appel("/api/student/access", {"code": code, "activityId": MODULE,
                                      "activityTitle": MODULE_TITRE})
        appel("/api/student/progress", {
            "code": code, "activityId": MODULE, "activityTitle": MODULE_TITRE,
            "event": "dialogue_listened"})
        appel("/api/student/progress", {
            "code": code, "activityId": MODULE, "activityTitle": MODULE_TITRE,
            "event": "exercise_completed", "zones": zones, "zonesDone": faites,
            "firstTry": round(faites * part["premier"]),
            "totalErrors": round(faites * (1 - part["premier"]) * 1.6)})
        if part.get("atelier"):
            appel("/api/student/access", {"code": code, "activityId": ATELIER,
                                          "activityTitle": ATELIER_TITRE})
            appel("/api/student/progress", {
                "code": code, "activityId": ATELIER, "activityTitle": ATELIER_TITRE,
                "event": "exercise_completed", "zones": 12, "zonesDone": 12,
                "firstTry": 9, "totalErrors": 4})
        pose += 1
    print("  %d élèves ont travaillé, %d ne sont jamais venus"
          % (pose, len(eleves) - pose))

    # ── Le direct : la classe répond, question par question ──
    print("  %d réponses au direct" % direct(eleves))

    # ── Deux textes envoyés ──
    envois = 0
    for eleve, part in zip(eleves, PARCOURS):
        if not part.get("ecrit"):
            continue
        appel("/api/ecrit/submit", {
            "code": eleve["code"], "theme": "Absence et retard",
            "taskId": "module-travail-pe", "taskLabel": "Écrire à son superviseur",
            "question": "Écrivez un court message pour annoncer une absence.",
            "texte": ECRITS[envois % len(ECRITS)]})
        envois += 1
    print("  %d productions écrites déposées" % envois)

    # ── Une séance ouverte, et trois appareils entrés dessus ──
    # Les participants écrivent dans le même tampon que les élèves inscrits :
    # c'est le fait à montrer, pas un effet de bord. Un téléphone prêté n'a pas
    # de compte, et sa réponse compte quand même dans le tableau de la classe.
    seances = appel("/api/prof/seances?groupId=%s" % gid, jeton=jeton)
    seances = seances.get("seances", seances if isinstance(seances, list) else [])
    ouverte = next((s for s in seances
                    if s.get("ouverte") and s.get("activityId") == MODULE), None)
    if not ouverte:
        ouverte = appel("/api/prof/seances", {"groupId": gid, "activityId": MODULE},
                        jeton=jeton).get("seance", {})
    code = ouverte.get("code", "")
    entres = 0
    for _ in range(3):
        jetonz = appel("/api/seance/entrer", {"code": code}).get("jeton")
        if not jetonz:
            continue
        entres += 1
        for z in ZONES[:2]:
            ok = DE.random() < 0.6
            appel("/api/student/progress", {
                "code": jetonz, "activityId": MODULE, "activityTitle": MODULE_TITRE,
                "event": "zone_repondue", "section": "prep", "exo": z["zone"][:3],
                "exoNum": "Exercice 1", "exoTitre": "Vrai ou Faux — Un départ précipité",
                "type": z["type"], "zone": z["zone"], "enonce": z["enonce"],
                "bonne": z["bonne"], "reponse": z["bonne"] if ok else "(autre réponse)",
                "ok": ok, "essais": 1 if ok else 2})
    print("  séance ouverte · code %s · %d appareils entrés" % (code, entres))


if __name__ == "__main__":
    main()
