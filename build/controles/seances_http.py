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
# Un arbre minimal : le réseau, un centre, et l'enseignant rattaché au centre.
# C'est ce rattachement qui fait descendre l'autorisation du mode séance.
(BAC / "data" / "organisations.json").write_text(json.dumps([
    {"id": 1, "type": "reseau", "nom": "francis", "parentId": None, "actif": True},
    {"id": 2, "type": "centre", "nom": "Centre d'essai", "parentId": 1, "actif": True},
], ensure_ascii=False))
(BAC / "data" / "acces.json").write_text(json.dumps([
    {"teacherId": 1, "orgId": 2, "role": "enseignant", "actif": True},
], ensure_ascii=False))

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
    # Le catalogue est celui du dépôt : `init_storage()` recopie le sien sur le
    # volume au démarrage, et un catalogue semé à la main serait écrasé en
    # pleine course — c'est ce qui a fait échouer ce contrôle une première fois.
    # `init_storage()` tourne en arrière-plan au démarrage : le catalogue
    # arrive une fraction de seconde après le premier appel, et lire trop tôt
    # rendait une liste vide.
    for _ in range(100):
        st, cat = appel("GET", "/api/activities?catalogue=1", jeton=JETON)
        liste = cat if isinstance(cat, list) else cat.get("activities", [])
        # `?catalogue=1` rend les enregistrements bruts : les chemins y sont à
        # plat, comme le serveur les lit.
        modules = [a for a in liste if a.get("interactive")]
        if len(modules) >= 2:
            break
        time.sleep(0.2)
    verifie("le catalogue du dépôt porte des modules", len(modules) >= 2,
            "%d module(s)" % len(modules))
    ACT, AUTRE = modules[0]["id"], modules[1]["id"]
    TITRE = modules[0]["title"]
    FICHIER = modules[0]["interactive"]
    st, r = appel("POST", "/api/prof/groupes", {"nom": "Niveau 4 — matin"}, JETON)
    verifie("groupe créé", st in (200, 201), str(r))
    GROUPE = r["groupe"]["id"]


    print("\n— La direction autorise, l'enseignant choisit —")
    st, r = appel("GET", "/api/prof/me", jeton=JETON)
    verifie("l'écran sait qu'il a le droit", r.get("seanceAutorisee") is True, str(r))
    st, arbre = appel("GET", "/api/admin/organisations", jeton=JETON)
    racine = next(o for o in arbre["organisations"] if o["type"] == "reseau")
    RACINE = racine["id"]
    verifie("l'arbre porte le réglage", racine.get("seance") == "herite", str(racine))
    verifie("et son état effectif", racine.get("seanceEffective") == "autorisee",
            str(racine))
    st, r = appel("PATCH", "/api/admin/organisations/%d" % RACINE,
                  {"seance": "interdite"}, JETON)
    verifie("le réseau ferme le mode", st == 200, str(r))
    st, r = appel("GET", "/api/prof/me", jeton=JETON)
    verifie("l'écran ne l'offre plus", r.get("seanceAutorisee") is False, str(r))
    verifie("et sait qui a fermé", bool(r.get("seanceDecidePar")), str(r))
    st, r = appel("POST", "/api/prof/seances",
                  {"groupId": GROUPE, "activityId": ACT}, JETON)
    verifie("et le serveur refuse d'ouvrir", st == 403, str(r))
    verifie("le message nomme le décideur", "francis" in (r.get("error") or ""), str(r))
    st, r = appel("PATCH", "/api/admin/organisations/%d" % RACINE,
                  {"seance": "herite"}, JETON)
    verifie("la racine n'hérite de personne", st == 400, str(r))
    st, r = appel("PATCH", "/api/admin/organisations/%d" % RACINE,
                  {"seance": "n'importe quoi"}, JETON)
    verifie("un état inconnu est refusé", st == 400, str(r))
    st, r = appel("PATCH", "/api/admin/organisations/%d" % RACINE,
                  {"seance": "autorisee"}, JETON)
    verifie("le réseau rouvre le mode", st == 200, str(r))
    st, r = appel("POST", "/api/prof/seances",
                  {"groupId": GROUPE, "activityId": ACT}, JETON)
    verifie("et l'enseignant peut de nouveau ouvrir", st in (200, 201), str(r))
    appel("POST", "/api/prof/seances/fermer", {"id": r["seance"]["id"]}, JETON)

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
    verifie("le titre du module est dit", r.get("activityTitle") == TITRE, str(r))
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



    print("\n— La feuille à imprimer —")
    st, r = appel("GET", "/api/prof/seances/feuille?code=" + CODE)
    verifie("sans session enseignante : refusé", st == 401, str(st))
    st, r = appel("GET", "/api/prof/seances/feuille?code=ZZZZZZ", jeton=JETON)
    verifie("code inconnu : 404", st == 404, str(st))
    st, r = appel("GET", "/api/prof/seances/feuille?code=" + CODE, jeton=JETON)
    verifie("la feuille est servie", st == 200, str(r)[:160])
    verifie("elle porte le code", r.get("code") == CODE, str(r.get("code")))
    verifie("et le nom du groupe", r.get("groupe") == "Niveau 4 — matin",
            str(r.get("groupe")))
    verifie("l'adresse courte n'a pas de protocole",
            "://" not in r.get("adresseCourte", "://"), str(r.get("adresseCourte")))
    verifie("elle finit par l'adresse courte de la séance",
            r.get("adresseCourte", "").endswith("/s/" + CODE),
            str(r.get("adresseCourte")))
    verifie("le carré est un SVG", r.get("qr", "").startswith("<svg"),
            r.get("qr", "")[:40])
    verifie("le carré ne va chercher aucune image ailleurs",
            "http" not in r.get("qr", "").replace(
                'xmlns="http://www.w3.org/2000/svg"', ""))

    # Aucun nom de domaine n'est écrit dans le code : l'adresse imprimée est
    # celle par laquelle le navigateur est arrivé. C'est ce qui fera qu'un
    # domaine acheté plus tard n'obligera à toucher à rien.
    req = urllib.request.Request(
        BASE + "/api/prof/seances/feuille?code=" + CODE,
        headers={"X-Prof-Token": JETON, "Host": "francis.quebec",
                 "X-Forwarded-Proto": "https"})
    with urllib.request.urlopen(req, timeout=10) as rep:
        feuille = json.loads(rep.read())
    verifie("l'adresse suit l'hôte de la requête",
            feuille["adresse"] == "https://francis.quebec/s/" + CODE,
            feuille["adresse"])
    with urllib.request.urlopen(BASE + "/feuille-seance.html", timeout=10) as rep:
        page = rep.read().decode()
    verifie("la page de la feuille est servie", "Vise ce carré" in page)
    verifie("elle s'imprime sans couleur",
            "@page" in page and "size: letter" in page)

    print("\n— L'adresse courte et la page d'entrée —")
    req = urllib.request.Request(BASE + "/s/" + CODE, method="GET")
    class SansSuivi(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None
    ouvreur = urllib.request.build_opener(SansSuivi)
    try:
        ouvreur.open(req, timeout=10)
        verifie("l'adresse courte redirige", False, "aucune redirection")
    except urllib.error.HTTPError as e:
        verifie("l'adresse courte redirige", e.code == 302, str(e.code))
        verifie("vers la page d'entrée, code en main",
                e.headers.get("Location") == "/seance.html?c=" + CODE,
                str(e.headers.get("Location")))
    try:
        ouvreur.open(urllib.request.Request(BASE + "/s/" + CODE.lower()), timeout=10)
    except urllib.error.HTTPError as e:
        verifie("le code minuscule est remis en majuscules",
                e.headers.get("Location") == "/seance.html?c=" + CODE,
                str(e.headers.get("Location")))
    try:
        ouvreur.open(urllib.request.Request(BASE + "/s/..%2fetc"), timeout=10)
        verifie("une adresse courte tordue ne redirige pas", False, "redirigé")
    except urllib.error.HTTPError as e:
        verifie("une adresse courte tordue ne redirige pas",
                e.code != 302 or "seance.html" not in (e.headers.get("Location") or ""),
                str(e.code) + " " + str(e.headers.get("Location")))
    with urllib.request.urlopen(BASE + "/seance.html", timeout=10) as rep:
        page = rep.read().decode()
    verifie("la page d'entrée est servie", "Le code de la feuille" in page)
    verifie("elle ne parle jamais de compte",
            "compte" not in page.replace("pas besoin de compte", "")
                                .replace("Tu n'as pas besoin de compte", "")
            or "sans compte" in page)

    print("\n— Revenir sur le même appareil —")
    st, r = appel("POST", "/api/seance/entrer", {"code": CODE, "jeton": JET})
    verifie("le même jeton rend le même participant",
            st == 200 and r.get("numero") == 1, str(r))
    verifie("et aucun participant n'est créé", r.get("jeton") == JET, str(r))
    st, r = appel("POST", "/api/seance/entrer", {"code": CODE})
    verifie("sans jeton, c'est un participant de plus", r.get("numero") == 2, str(r))
    JET2 = r["jeton"]
    st, r = appel("POST", "/api/seance/entrer", {"code": "ZZZZZZ", "jeton": JET})
    verifie("un jeton d'une autre séance ne sert à rien", st == 404, str(st))
    st, r = appel("POST", "/api/seance/entrer", {"code": CODE, "jeton": "S" + "Z" * 16})
    verifie("un jeton inventé retombe sur une entrée neuve",
            st == 200 and r.get("numero") == 3, str(r))

    print("\n— Ce que l'appareil reçoit pour ouvrir le module —")
    verifie("le fichier du module est dit", r.get("fichier") == FICHIER,
            str(r.get("fichier")))
    verifie("le titre aussi", r.get("activityTitle") == TITRE, str(r))

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
    mienne = next((x for x in r.get("seances", []) if x["id"] == SEANCE["id"]), None)
    verifie("l'enseignant retrouve sa séance", st == 200 and mienne, str(r))
    # Trois entrées, pas cinq : les deux retours avec le jeton d'un appareil
    # déjà entré n'ont créé personne. C'est tout l'intérêt de la reprise.
    verifie("avec son compte de participants",
            mienne and mienne["participants"] == 3, str(mienne))
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
