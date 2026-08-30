#!/usr/bin/env python3
"""Contrôle des points express — le cycle entier, joué par HTTP.

Constater · envoyer · faire · refermer. Ce qui compte ici n'est pas que
l'envoi passe : c'est que les **refus refusent**. Un contrôle qui se contente
d'envoyer un point express passerait aussi bien toutes gardes retirées.

    python3 build/controles/points_express.py

Serveur jetable, `STORAGE_DIR` à part : rien n'est écrit dans le dépôt.
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
BAC = Path(tempfile.mkdtemp(prefix="points-express-"))
(BAC / "data").mkdir()
(BAC / "assets").mkdir()
for f in ("sections.json", "points_express.json"):
    if (RACINE / "data" / f).exists():
        shutil.copy(RACINE / "data" / f, BAC / "data" / f)

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
        brut = e.read()
        try:
            return e.code, json.loads(brut or b"{}")
        except json.JSONDecodeError:
            return e.code, {"brut": brut[:200].decode("utf-8", "replace")}


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
    # Le compte s'ouvre par un CODE de six caractères, plus par un courriel :
    # voir « Les comptes enseignants : un code, pas un courriel » dans CLAUDE.md.
    st, r = appel("POST", "/api/prof/setup",
                  {"code": "PE1234", "motDePasse": "motdepasse1",
                   "nom": "Prof d'essai"})
    verifie("compte fondateur créé", st in (200, 201), str(r))
    JETON = r.get("token")

    st, r = appel("POST", "/api/prof/groupes", {"nom": "Niveau 5 — matin"}, JETON)
    GROUPE = r["groupe"]["id"]
    verifie("groupe créé", st in (200, 201), str(r))

    st, r = appel("POST", "/api/admin/students",
                  {"groupId": GROUPE, "count": 2}, JETON)
    eleves = r.get("students") or r.get("eleves") or []
    verifie("deux élèves inscrits", len(eleves) == 2, str(r)[:200])
    A, B = eleves[0], eleves[1]

    print("\n— L'étagère —")
    st, etagere = appel("GET", "/api/prof/points-express", jeton=JETON)
    verifie("l'étagère se lit", st == 200 and isinstance(etagere, list), str(etagere)[:120])
    verifie("et elle porte des points express", len(etagere) >= 1,
            "%d point(s)" % len(etagere or []))
    verifie("chacun porte son savoir et ses écrans",
            all(p.get("slug") and p.get("ecrans") for p in etagere), str(etagere)[:200])
    POINT = etagere[0]["slug"]
    AUTRE = etagere[1]["slug"] if len(etagere) > 1 else POINT

    st, r = appel("GET", "/api/prof/points-express")
    verifie("sans jeton, l'étagère refuse", st == 401, str(r))

    print("\n— L'envoi —")
    st, r = appel("POST", "/api/prof/envois",
                  {"groupId": GROUPE, "eleveIds": [A["id"]], "parcours": POINT,
                   "mot": "Regarde ça avant jeudi."}, JETON)
    verifie("l'envoi passe", st == 201 and len(r.get("envois", [])) == 1, str(r)[:200])
    ENVOI = r["envois"][0]
    verifie("il porte le titre du point, pas seulement son slug",
            bool(ENVOI.get("titre")), str(ENVOI))
    verifie("et il part à l'état « envoyé »", ENVOI.get("etat") == "envoye", str(ENVOI))

    st, r = appel("POST", "/api/prof/envois",
                  {"groupId": GROUPE, "eleveIds": [A["id"]], "parcours": POINT}, JETON)
    verifie("un même point non terminé ne se renvoie pas",
            st == 201 and len(r.get("envois", [])) == 0 and r.get("deja") == 1, str(r))

    st, r = appel("POST", "/api/prof/envois",
                  {"groupId": GROUPE, "eleveIds": [A["id"]], "parcours": "point-invente"},
                  JETON)
    verifie("un point inconnu est refusé", st == 400, str(r))

    st, r = appel("POST", "/api/prof/envois",
                  {"groupId": GROUPE, "eleveIds": [], "parcours": POINT}, JETON)
    verifie("un envoi sans élève est refusé", st == 400, str(r))

    st, r = appel("POST", "/api/prof/envois",
                  {"groupId": GROUPE, "eleveIds": [A["id"]], "parcours": POINT})
    verifie("sans jeton, l'envoi refuse", st == 401, str(r))

    # Vu à l'écran, pas ici : `Prof.body` rend déjà une chaîne JSON, et
    # l'envelopper une seconde fois envoyait une chaîne là où le serveur
    # attend un objet — le fil de la requête mourait sur un AttributeError et
    # le navigateur ne recevait rien. Un corps mal formé doit se REFUSER.
    st, r = appel("POST", "/api/prof/envois", "une chaine, pas un objet", JETON)
    verifie("un corps mal formé est refusé, pas fatal", st == 400, str(r))
    st, r = appel("POST", "/api/student/envois/1", "idem")
    verifie("idem côté élève", st == 400, str(r))
    st, r = appel("GET", "/api/health")
    verifie("et le serveur est toujours debout", st == 200, str(r))

    print("\n— Ce que l'élève voit —")
    st, miens = appel("GET", "/api/student/envois?code=%s" % A["code"])
    verifie("l'élève voit son point express", st == 200 and len(miens) == 1, str(miens)[:150])
    verifie("avec le mot de l'enseignant",
            miens[0].get("mot", "").startswith("Regarde"), str(miens[0])[:150])
    verifie("et le chemin du fichier à ouvrir",
            miens[0].get("fichier", "").startswith("modules-autonomes/"), str(miens[0])[:150])

    st, autres = appel("GET", "/api/student/envois?code=%s" % B["code"])
    verifie("l'autre élève ne voit rien", st == 200 and autres == [], str(autres))

    st, r = appel("GET", "/api/student/envois?code=ZZZZZZ")
    verifie("un code inconnu refuse", st == 401, str(r))

    print("\n— Le parcours referme —")
    st, r = appel("POST", "/api/student/envois/%d" % ENVOI["id"],
                  {"code": A["code"], "etat": "commence"})
    verifie("le début se rapporte", st == 200 and r.get("etat") == "commence", str(r))

    st, r = appel("POST", "/api/student/envois/%d" % ENVOI["id"],
                  {"code": B["code"], "etat": "termine"})
    verifie("un autre élève ne peut pas refermer l'envoi", st == 404, str(r))

    st, r = appel("POST", "/api/student/envois/%d" % ENVOI["id"],
                  {"code": A["code"], "etat": "n-importe-quoi"})
    verifie("un état inventé est refusé", st == 400, str(r))

    st, r = appel("POST", "/api/student/envois/%d" % ENVOI["id"],
                  {"code": A["code"], "etat": "termine",
                   "resultat": {"reussiSeul": 7, "avecRattrapage": 2,
                                "rattrapages": ["depart", "tri-fin"], "minutes": 9,
                                "reponses": ["une réponse d'élève"]}})
    verifie("la fin se rapporte", st == 200 and r.get("etat") == "termine", str(r))

    st, vus = appel("GET", "/api/prof/envois?groupId=%d" % GROUPE, jeton=JETON)
    ferme = next(e for e in vus if e["id"] == ENVOI["id"])
    verifie("l'enseignant voit le résultat",
            (ferme.get("resultat") or {}).get("reussiSeul") == 7, str(ferme)[:200])
    verifie("et sait quels écrans ont été rouverts",
            (ferme.get("resultat") or {}).get("rattrapages") == ["depart", "tri-fin"],
            str(ferme)[:200])
    verifie("AUCUNE réponse d'élève n'est gardée",
            "reponses" not in (ferme.get("resultat") or {}), str(ferme)[:250])

    st, r = appel("POST", "/api/student/envois/%d" % ENVOI["id"],
                  {"code": A["code"], "etat": "commence"})
    verifie("rouvrir un point terminé ne le rouvre pas",
            st == 200 and r.get("etat") == "termine", str(r))

    print("\n— Ce qui est terminé se renvoie —")
    st, r = appel("POST", "/api/prof/envois",
                  {"groupId": GROUPE, "eleveIds": [A["id"], B["id"]], "parcours": POINT},
                  JETON)
    verifie("le même point se renvoie une fois réglé",
            st == 201 and len(r.get("envois", [])) == 2, str(r)[:200])

    print("\n— Retirer —")
    st, r = appel("DELETE", "/api/prof/envois/%d" % ENVOI["id"])
    verifie("sans jeton, retirer refuse", st == 401, str(r))
    st, r = appel("DELETE", "/api/prof/envois/%d" % ENVOI["id"], jeton=JETON)
    verifie("l'envoi se retire", st == 200, str(r))
    st, vus = appel("GET", "/api/prof/envois?groupId=%d" % GROUPE, jeton=JETON)
    verifie("et il a bien disparu",
            all(e["id"] != ENVOI["id"] for e in vus), str(vus)[:150])
    st, r = appel("DELETE", "/api/prof/envois/999999", jeton=JETON)
    verifie("retirer un envoi inexistant rend 404", st == 404, str(r))

finally:
    serveur.terminate()
    try:
        serveur.wait(timeout=5)
    except subprocess.TimeoutExpired:
        serveur.kill()
    shutil.rmtree(BAC, ignore_errors=True)

print()
if ECHECS:
    print("%d écart(s) : %s" % (len(ECHECS), " · ".join(ECHECS)))
    sys.exit(1)
print("Aucun écart.")
