#!/usr/bin/env python3
"""Contrôle du mode séance — les routes, jouées par HTTP.

Le contrôle précédent appelle les fonctions ; celui-ci passe par le serveur,
et vérifie donc ce que les fonctions ne peuvent pas dire : que le chemin de la
requête est bien posé pour la liste blanche, que les routes sont branchées,
que l'enseignant est exigé là où il faut, et que la garde du module unique
répond bien 403 au lieu de laisser passer.
"""
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
BAC = Path(tempfile.mkdtemp(prefix="seances-http-"))
# Créés à la main : init_storage() ne recopie ni data/ ni assets/ quand ils
# existent, et ce contrôle n'a pas besoin des centaines de mégaoctets du dépôt.
(BAC / "data").mkdir()
(BAC / "assets").mkdir()
shutil.copy(RACINE / "data" / "sections.json", BAC / "data" / "sections.json")
# Le catalogue est semé à la main : la route qui ajoute une activité attend un
# multipart, et ce contrôle-ci ne porte pas sur elle.
(BAC / "data" / "activities.json").write_text(json.dumps([
    {"id": 12, "title": "Au travail", "categorie": "cours", "slug": "au-travail"},
    {"id": 13, "title": "À la clinique", "categorie": "cours", "slug": "clinique"},
], ensure_ascii=False))
ACT, AUTRE = 12, 13

ECHECS = []


def verifie(nom, condition, detail=""):
    if condition:
        print("  ok   %s" % nom)
    else:
        print("  RATÉ %s %s" % (nom, detail))
        ECHECS.append(nom)


def port_libre():
    with socket.socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]


PORT = port_libre()
env = dict(os.environ, STORAGE_DIR=str(BAC), PORT=str(PORT))
env.pop("DATABASE_URL", None)
env.pop("ANTHROPIC_API_KEY", None)
serveur = subprocess.Popen([sys.executable, str(RACINE / "server.py")], env=env,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
BASE = "http://127.0.0.1:%d" % PORT


def appel(methode, chemin, corps=None, jeton=None):
    req = urllib.request.Request(
        BASE + chemin, method=methode,
        data=json.dumps(corps).encode() if corps is not None else None,
        headers={"Content-Type": "application/json",
                 **({"X-Prof-Token": jeton} if jeton else {})})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        corps_err = e.read()
        try:
            return e.code, json.loads(corps_err or b"{}")
        except json.JSONDecodeError:
            return e.code, {"brut": corps_err[:200].decode("utf-8", "replace")}


try:
    for _ in range(100):
        try:
            appel("GET", "/api/health")
            break
        except Exception:
            time.sleep(0.1)
    else:
        raise SystemExit("le serveur n'a pas démarré")

    print("\n— Le décor —")
    st, r = appel("POST", "/api/prof/setup",
                  {"courriel": "prof@essai.test", "motDePasse": "motdepasse1",
                   "nom": "Prof d'essai"})
    verifie("compte fondateur créé", st in (200, 201), str(r))
    JETON = r.get("token")
    st, r = appel("POST", "/api/prof/groupes", {"nom": "Niveau 4 — matin"}, JETON)
    verifie("groupe créé", st in (200, 201), str(r))
    GROUPE = r["groupe"]["id"]

    print("\n— Ouvrir une séance —")
    st, r = appel("POST", "/api/prof/seances",
                  {"groupId": GROUPE, "activityId": ACT})
    verifie("sans session enseignante : refusé", st == 401, str(st))
    st, r = appel("POST", "/api/prof/seances",
                  {"groupId": GROUPE, "activityId": 9999}, JETON)
    verifie("module inexistant : refusé", st == 404, str(st))
    st, r = appel("POST", "/api/prof/seances",
                  {"groupId": GROUPE + 999, "activityId": ACT}, JETON)
    verifie("groupe d'autrui : refusé", st == 403, str(st))
    st, r = appel("POST", "/api/prof/seances",
                  {"groupId": GROUPE, "activityId": ACT}, JETON)
    verifie("séance ouverte", st in (200, 201), str(r))
    SEANCE = r["seance"]
    CODE = SEANCE["code"]
    verifie("la réponse porte le code", len(CODE) == 6, CODE)
    verifie("la réponse ne porte aucun jeton", "jeton" not in json.dumps(r))

    print("\n— L'état public d'une séance —")
    st, r = appel("GET", "/api/seance?code=" + CODE)
    verifie("ouverte, sans authentification", st == 200 and r["ouverte"], str(r))
    verifie("le titre du module est dit", r.get("activityTitle") == "Au travail")
    verifie("le groupe n'est pas dit", "groupId" not in r and "groupe" not in r)
    st, r = appel("GET", "/api/seance?code=ZZZZZZ")
    verifie("code inconnu : 404", st == 404, str(st))

    print("\n— Entrer —")
    st, r = appel("POST", "/api/seance/entrer", {"code": CODE})
    verifie("entrée acceptée", st == 200, str(r))
    JET = r.get("jeton")
    verifie("un jeton est rendu", bool(JET), str(r))
    verifie("le module de la séance est dit", r.get("activityId") == ACT)
    st, r = appel("POST", "/api/seance/entrer", {"code": "ZZZZZZ"})
    verifie("code inconnu : 404", st == 404, str(st))

    print("\n— Ce que le jeton ouvre —")
    st, r = appel("GET", "/api/student/ia?code=" + JET)
    verifie("le module sait à quoi s'en tenir", st == 200, str(r))
    verifie("l'IA est autorisée par défaut", r.get("ia") is True, str(r))
    st, r = appel("GET", "/api/student/sections?code=%s&activityId=%d" % (JET, ACT))
    verifie("les sections de son module", st == 200, str(r))
    st, r = appel("POST", "/api/student/progress",
                  {"code": JET, "activityId": ACT, "event": "exercise_completed",
                   "zones": 10, "zonesDone": 3, "firstTry": 2, "totalErrors": 1})
    verifie("sa progression est reçue", st == 200, str(r))
    st, r = appel("POST", "/api/student/progress",
                  {"code": JET, "activityId": ACT, "event": "zone_repondue",
                   "zone": "t1pc", "reussi": True})
    verifie("le direct de la classe est reçu", st == 200, str(r))
    st, r = appel("POST", "/api/student/progress",
                  {"code": JET, "activityId": ACT, "event": "aide_proposee",
                   "exercice": "Défi 1"})
    verifie("les signaux d'aide sont reçus", st == 200, str(r))
    st, r = appel("POST", "/api/student/access",
                  {"code": JET, "activityId": ACT, "activityTitle": "Au travail"})
    verifie("son ouverture est journalisée", st == 200, str(r))

    print("\n— Ce que le jeton n'ouvre pas —")
    st, r = appel("GET", "/api/student/sections?code=%s&activityId=%d" % (JET, AUTRE))
    verifie("un autre module : 403", st == 403, str(st))
    verifie("le message parle à l'élève",
            "un seul module" in (r.get("error") or ""), str(r))
    st, r = appel("POST", "/api/student/progress",
                  {"code": JET, "activityId": AUTRE, "event": "exercise_completed"})
    verifie("progression sur un autre module : 403", st == 403, str(st))
    st, r = appel("GET", "/api/student/dashboard?code=" + JET)
    verifie("le tableau de bord : refusé", st in (401, 403), str(st))
    st, r = appel("GET", "/api/student/activities?code=" + JET)
    verifie("le catalogue : refusé", st in (401, 403), str(st))
    st, r = appel("GET", "/api/vocab/session?code=" + JET)
    verifie("le vocabulaire : refusé", st in (401, 403), str(st))
    st, r = appel("POST", "/api/ecrit/submit",
                  {"code": JET, "texte": "Bonjour, je m'appelle X.", "theme": "essai"})
    verifie("l'écrit s'envoie", st == 200, str(r))
    st, dep = appel("GET", "/api/admin/written-submissions?groupId=%d" % GROUPE,
                    jeton=JETON)
    depots = dep if isinstance(dep, list) else (dep.get("submissions") or [])
    verifie("l'enseignant le reçoit", len(depots) == 1, str(dep)[:200])
    verifie("sous un nom anonyme",
            depots and depots[0].get("studentLabel", "").startswith("Participant"),
            str(depots[0] if depots else ""))
    verifie("et le jeton n'y est pas", JET not in json.dumps(dep))
    st, r = appel("GET", "/api/prof/seances?groupId=%d" % GROUPE, jeton=JET)
    verifie("les séances de l'enseignant : refusé", st == 401, str(st))

    print("\n— L'oral ne part pas —")
    limite = urllib.request.Request(
        BASE + "/api/oral/submit", method="POST",
        data=b"--x\r\nContent-Disposition: form-data; name=\"code\"\r\n\r\n"
             + JET.encode() + b"\r\n--x--\r\n",
        headers={"Content-Type": "multipart/form-data; boundary=x"})
    try:
        with urllib.request.urlopen(limite, timeout=10) as rep:
            verifie("le dépôt oral est refusé", False, "reçu %d" % rep.status)
    except urllib.error.HTTPError as e:
        verifie("le dépôt oral est refusé", e.code == 401, str(e.code))

    print("\n— Fermer —")
    st, r = appel("POST", "/api/prof/seances/fermer", {"id": SEANCE["id"]}, JETON)
    verifie("séance fermée", st == 200 and not r["seance"]["ouverte"], str(r))
    st, r = appel("POST", "/api/student/progress",
                  {"code": JET, "activityId": ACT, "event": "exercise_completed"})
    verifie("le jeton ne vaut plus rien", st == 401, str(st))
    st, r = appel("POST", "/api/seance/entrer", {"code": CODE})
    verifie("et plus personne n'entre", st == 403, str(st))
    st, r = appel("GET", "/api/prof/seances?groupId=%d" % GROUPE, jeton=JETON)
    verifie("l'enseignant retrouve sa séance", st == 200 and r["seances"], str(r))
    verifie("avec son compte de participants",
            r["seances"][0]["participants"] == 1, str(r["seances"][0]))
    verifie("et toujours aucun jeton", "jeton" not in json.dumps(r))

    print("\n— Le débit des entrées —")
    st, r = appel("POST", "/api/prof/seances",
                  {"groupId": GROUPE, "activityId": ACT}, JETON)
    NEUF = r["seance"]["code"]
    refuse = 0
    for _ in range(30):
        st, _ = appel("POST", "/api/seance/entrer", {"code": "ZZZZZZ"})
        if st == 429:
            refuse += 1
    verifie("les essais en rafale sont bornés", refuse > 0, "aucun 429")
finally:
    serveur.terminate()
    try:
        serveur.wait(timeout=5)
    except subprocess.TimeoutExpired:
        serveur.kill()
    shutil.rmtree(BAC, ignore_errors=True)

print()
if ECHECS:
    print("%d contrôle(s) en échec : %s" % (len(ECHECS), ", ".join(ECHECS)))
    sys.exit(1)
print("Tous les contrôles passent.")
