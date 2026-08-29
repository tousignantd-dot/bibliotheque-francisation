#!/usr/bin/env python3
"""Contrôle du mode séance — le socle, joué geste par geste.

Ce que le contrôle vérifie n'est pas que le code s'exécute, mais que les
gardes **refusent** : un participant qui vise un autre module, une route hors
liste blanche, une séance fermée, pleine, ou un identifiant qui empiéterait
sur celui d'un vrai élève. Un test qui ne fait qu'entrer dans une séance
passerait aussi avec toutes les gardes retirées.
"""
import os
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
BAC = tempfile.mkdtemp(prefix="seances-")
os.environ["STORAGE_DIR"] = BAC
os.environ.pop("DATABASE_URL", None)
sys.path.insert(0, str(RACINE))
import server as S                                            # noqa: E402

ECHECS = []


def verifie(nom, condition, detail=""):
    if condition:
        print("  ok   %s" % nom)
    else:
        print("  RATÉ %s %s" % (nom, detail))
        ECHECS.append(nom)


def route(chemin):
    """Se place sur une route, comme le fait `do_GET` / `do_POST`."""
    S._REQUETE.chemin = chemin


# ── Le décor : un centre, un groupe, un élève, deux modules ─────────────────
S.save_organisations([
    {"id": 1, "type": "reseau", "nom": "francis", "parentId": None},
    {"id": 2, "type": "centre", "nom": "Centre d'essai", "parentId": 1,
     "ia": "interdite"},
])
S.save_groups([{"id": 7, "nom": "Niveau 4 — matin", "teacherId": 1, "centreId": 2},
               {"id": 8, "nom": "Niveau 4 — soir", "teacherId": 1, "centreId": 2}])
S.save_students([{"id": 1, "code": "ABCDEF", "label": "Colibri", "groupId": 7}])
S.save_activities([{"id": 12, "title": "Au travail"},
                   {"id": 13, "title": "À la clinique"}])
PROF = {"id": 1, "courriel": "prof@essai.test", "role": "admin"}

print("\n— Ouvrir une séance —")
seance = S.creer_seance(PROF, 7, 12, titre="Au travail")
verifie("code à six caractères", len(seance["code"]) == 6, seance["code"])
verifie("code sans caractère ambigu",
        not set(seance["code"]) & set("OI01"), seance["code"])
verifie("ouverte le jour même", S.seance_ouverte(seance))
verifie("aucun participant au départ", seance["participants"] == [])

print("\n— Un code de séance ne peut pas être celui d'un élève —")
eleves = [{"id": i, "code": c, "label": "E%d" % i, "groupId": 7}
          for i, c in enumerate(S.SEANCE_ALPHABET, start=1)]
# On sature volontairement : tous les codes à un caractère près sont pris par
# des élèves, et le tirage doit quand même en trouver un libre.
S.save_students(eleves + [{"id": 99, "code": seance["code"], "label": "Piège",
                           "groupId": 7}])
autre = S.creer_seance(PROF, 7, 13, titre="À la clinique")
codes_eleves = {e["code"] for e in S.load_students()}
verifie("le nouveau code évite ceux des élèves",
        autre["code"] not in codes_eleves, autre["code"])
S.save_students([{"id": 1, "code": "ABCDEF", "label": "Colibri", "groupId": 7}])

print("\n— Entrer dans la séance —")
p1, s1, err1 = S.entrer_dans_seance(seance["code"])
p2, s2, err2 = S.entrer_dans_seance(seance["code"].lower())
verifie("première entrée acceptée", err1 is None, str(err1))
verifie("le code marche en minuscules", err2 is None, str(err2))
verifie("numéros qui se suivent", (p1["numero"], p2["numero"]) == (1, 2))
verifie("jetons distincts", p1["jeton"] != p2["jeton"])
verifie("jeton en majuscules", p1["jeton"] == p1["jeton"].upper(), p1["jeton"])
verifie("jeton de 17 caractères", len(p1["jeton"]) == 17, p1["jeton"])
verifie("identifiants négatifs", p1["id"] < 0 and p2["id"] < 0)
verifie("identifiants distincts", p1["id"] != p2["id"])
verifie("aucune collision avec un élève",
        {p1["id"], p2["id"]}.isdisjoint({e["id"] for e in S.load_students()}))
_, s3, _ = S.entrer_dans_seance(autre["code"])
p3 = S.load_seances()[1]["participants"][0]
verifie("les séances ne partagent pas leurs identifiants",
        p3["id"] not in (p1["id"], p2["id"]))

print("\n— La couture : le jeton passe pour une identité d'élève —")
route("/api/student/progress")
ident = S.validate_student_code(p1["jeton"])
verifie("le jeton est reconnu", ident is not None)
verifie("il porte le vrai groupe", ident and ident["groupId"] == 7)
verifie("il est marqué anonyme", ident and ident.get("anonyme") is True)
verifie("il s'appelle Participant 1", ident and ident["label"] == "Participant 1")
verifie("aucun nom, aucun pseudo", ident and ident.get("prenom") == "")
verifie("le code d'un vrai élève marche toujours",
        (S.validate_student_code("ABCDEF") or {}).get("label") == "Colibri")
verifie("un jeton inventé est refusé",
        S.validate_student_code("S" + "Z" * 16) is None)

print("\n— La liste blanche des routes —")
for chemin in sorted(S.ROUTES_SEANCE):
    route(chemin)
    if S.validate_student_code(p1["jeton"]) is None:
        verifie("ouverte : %s" % chemin, False)
verifie("les %d routes de la liste sont ouvertes" % len(S.ROUTES_SEANCE), True)
FERMEES = ["/api/oral/submit", "/api/vocab/session", "/api/vocab/answer",
           "/api/student/dashboard", "/api/student/activities",
           "/api/corrige-moi/seance", "/api/vocab/translate",
           "/api/admin/students", "/api/prof/seances"]
for chemin in FERMEES:
    route(chemin)
    verifie("fermée : %s" % chemin, S.validate_student_code(p1["jeton"]) is None)
route("/api/route/inventee/demain")
verifie("une route inconnue est fermée d'office",
        S.validate_student_code(p1["jeton"]) is None)
S._REQUETE.chemin = ""
verifie("hors requête, rien ne passe", S.validate_student_code(p1["jeton"]) is None)

print("\n— La garde du module unique —")
route("/api/student/progress")
ident = S.validate_student_code(p1["jeton"])
verifie("son propre module passe", S.activite_de_la_seance(ident, 12))
verifie("son propre module en texte passe", S.activite_de_la_seance(ident, "12"))
verifie("un autre module est refusé", not S.activite_de_la_seance(ident, 13))
verifie("un module absent passe", S.activite_de_la_seance(ident, None))
verifie("un module illisible est refusé",
        not S.activite_de_la_seance(ident, "douze"))
verifie("un vrai élève n'est jamais borné",
        S.activite_de_la_seance(S.validate_student_code("ABCDEF"), 13))

print("\n— L'héritage : le refus d'IA du centre s'applique au participant —")
autorisee, decideur = S.ia_pour_eleve(ident)
verifie("l'IA est refusée au participant", autorisee is False)
verifie("le décideur est le centre",
        (decideur or {}).get("nom") == "Centre d'essai")
S.save_organisations([
    {"id": 1, "type": "reseau", "nom": "francis", "parentId": None},
    {"id": 2, "type": "centre", "nom": "Centre d'essai", "parentId": 1,
     "ia": "autorisee", "depot": "ferme"},
])
autorisee, _ = S.ia_pour_eleve(ident)
etat_depot, _ = S.depot_pour_eleve(ident)
verifie("le centre rouvert rouvre aussi le participant", autorisee is True)
verifie("le réglage de dépôt descend jusqu'au participant",
        etat_depot == "ferme", etat_depot)

print("\n— Le plafond, la fermeture, l'expiration —")
petite = S.creer_seance(PROF, 8, 12, titre="Au travail", plafond=2)
S.entrer_dans_seance(petite["code"])
S.entrer_dans_seance(petite["code"])
_, _, err = S.entrer_dans_seance(petite["code"])
verifie("la troisième entrée est refusée", err is not None and err[1] == 403)
verifie("le message parle à l'élève", err and "pleine" in err[0], str(err))
verifie("plafond borné vers le haut",
        S.creer_seance(PROF, 8, 12, plafond=99999)["plafond"]
        == S.SEANCE_PLAFOND_MAX)

seances = S.load_seances()
for s in seances:
    if s["id"] == petite["id"]:
        s["ouverte"] = False
S.save_seances(seances)
_, _, err = S.entrer_dans_seance(petite["code"])
verifie("une séance fermée refuse l'entrée", err is not None and err[1] == 403)

seances = S.load_seances()
for s in seances:
    if s["id"] == seance["id"]:
        s["expire"] = "2020-01-01"
S.save_seances(seances)
_, _, err = S.entrer_dans_seance(seance["code"])
verifie("une séance expirée refuse l'entrée", err is not None)
route("/api/student/progress")
verifie("et le jeton déjà donné cesse de valoir",
        S.validate_student_code(p1["jeton"]) is None)
_, _, err = S.entrer_dans_seance("ZZZZZZ")
verifie("un code inconnu répond 404", err is not None and err[1] == 404)

print("\n— Le fichier des séances ne fuit pas —")
brut = (Path(BAC) / "data" / "seances.json").read_text()
verifie("aucun code d'élève dans le fichier", "ABCDEF" not in brut)

print()
if ECHECS:
    print("%d contrôle(s) en échec : %s" % (len(ECHECS), ", ".join(ECHECS)))
    sys.exit(1)
print("Tous les contrôles passent.")
