#!/usr/bin/env python3
"""Peuple l'instance de démonstration pour la capture d'écran du tutoriel.

Tout est inventé : les noms d'élèves, les groupes, les dates. Rien ne vient
des données réelles de l'utilisateur — le bac à sable a été purgé avant.
On vise un état d'écran *plausible et varié* : des activités ouvertes, une
fermée, deux à venir, et un bon paquet sans date, pour que les quatre
pastilles paraissent toutes à l'écran.
"""
import json
import os
import sys
import tempfile
import urllib.request
import uuid
from datetime import date, timedelta
from pathlib import Path

BASE = f"http://localhost:{sys.argv[1]}"
AUJ = date.today()
DEPOT = Path(__file__).resolve().parent.parent.parent


def identifiants():
    """Le compte de démonstration, lu dans le bac à sable — jamais écrit ici.

    `lancer_demo.sh` tire le mot de passe au hasard au premier lancement et
    le dépose à côté du stockage jetable. L'écrire dans ce fichier le ferait
    partir sur GitHub à chaque commit."""
    bac = Path(os.environ.get(
        "STORAGE_DIR", Path(tempfile.gettempdir()) / "francisation-demo-tutoriels"))
    fichier = bac / "identifiants-demo.json"
    if fichier.exists():
        return json.loads(fichier.read_text())
    if os.environ.get("PROF_CODE") and os.environ.get("PROF_MOTDEPASSE"):
        return {"code": os.environ["PROF_CODE"],
                "motDePasse": os.environ["PROF_MOTDEPASSE"]}
    sys.exit(f"Identifiants introuvables ({fichier}). Lancez d'abord "
             "./build/tutoriels/lancer_demo.sh")


def appel(chemin, corps=None, methode=None, jeton=None):
    donnees = json.dumps(corps).encode() if corps is not None else None
    req = urllib.request.Request(
        BASE + chemin, data=donnees,
        method=methode or ("POST" if donnees else "GET"))
    req.add_header("Content-Type", "application/json")
    if jeton:
        req.add_header("X-Prof-Token", jeton)
    with urllib.request.urlopen(req) as r:
        brut = r.read().decode()
    return json.loads(brut) if brut else {}


# ── Session ──
jeton = appel("/api/prof/login", identifiants())["token"]
print("session ouverte")

# ── Groupes ──
#
# Une installation neuve n'a **aucun groupe** : le groupe historique ne se crée
# plus tout seul (il ne se créait que pour ranger des élèves d'avant le
# multi-groupes, et en fabriquer un vide laissait un orphelin sans centre). Ce
# script partait de `groupes[0]` et tombait sur une liste vide. Il les crée
# donc lui-même — et il leur donne un **niveau**, devenu obligatoire : c'est
# lui qui borne le catalogue, le matériel et la séance sans compte.
def groupe(nom, niveau):
    reponse = appel("/api/prof/groupes", jeton=jeton)
    existants = reponse["groupes"] if isinstance(reponse, dict) else reponse
    deja = [g for g in existants if g["nom"] == nom]
    if deja:
        return deja[0]["id"]
    return appel("/api/prof/groupes", {"nom": nom, "niveau": niveau},
                 jeton=jeton)["groupe"]["id"]

g1 = groupe("Niveau 4 — avant-midi", "Niveau 4")
g2 = groupe("Niveau 4 — soir", "Niveau 4")
print(f"groupes : {g1} (historique), {g2} (soir)")

# ── Élèves du groupe 1 ──
# Des PSEUDONYMES, et c'est le sujet même de la capsule des élèves : le champ
# demande « un pseudo, pas le vrai nom ». Peupler la démonstration de vrais
# noms faisait filmer, dans le tutoriel officiel, le geste que le portail
# refuse. Corrigé le 2 septembre 2026.
NOMS = ["Colibri", "Érable", "Cardinal", "Bouleau", "Harfang", "Lynx",
        "Épervier", "Baleine", "Renard", "Caribou"]
deja = appel(f"/api/admin/students?groupId={g1}", jeton=jeton)
deja = deja["students"] if isinstance(deja, dict) else deja
if not deja:
    for nom in NOMS:
        appel("/api/admin/students", {"groupId": g1, "label": nom, "count": 1}, jeton=jeton)
    # Deux codes préparés d'avance, sans nom.
    appel("/api/admin/students", {"groupId": g1, "count": 2}, jeton=jeton)
print(f"{len(NOMS)} élèves nommés + 2 codes d'avance")

# ── Planification : on repart de zéro pour maîtriser les états ──
brut = appel(f"/api/activities?groupId={g1}", jeton=jeton)
activites = brut["activities"] if isinstance(brut, dict) else brut
cours = [a for a in activites if a.get("categorie") == "cours"]
ateliers = [a for a in activites if a.get("categorie") != "cours"]
print(f"catalogue : {len(cours)} cours, {len(ateliers)} ateliers")

for a in activites:
    appel(f"/api/activities/{a['id']}/dates",
          {"groupId": g1, "datePrevue": "", "dateFin": "", "dateVue": ""}, jeton=jeton)

j = lambda n: (AUJ + timedelta(days=n)).isoformat()


def date_activite(aid, ouverture="", fermeture="", vue="", section=""):
    corps = {"groupId": g1, "datePrevue": ouverture, "dateFin": fermeture, "dateVue": vue}
    if section:
        corps["sectionId"] = section
    appel(f"/api/activities/{aid}/dates", corps, jeton=jeton)


# Trois cours ouverts, un qui ferme bientôt, deux à venir, le reste sans date.
if len(cours) >= 6:
    date_activite(cours[0]["id"], j(-14), vue=j(-12))
    date_activite(cours[1]["id"], j(-7), vue=j(-5))
    date_activite(cours[2]["id"], j(-2))
    date_activite(cours[3]["id"], j(-21), j(-3), vue=j(-19))   # fermée
    date_activite(cours[4]["id"], j(7))                        # à venir
    date_activite(cours[5]["id"], j(14))                       # à venir

# Quelques ateliers ouverts, pour que « Aujourd'hui » ne soit pas vide.
for a in ateliers[:4]:
    date_activite(a["id"], j(-10))

# Des sections datées sur un module qui en a : c'est ce que montre le chevron.
carte = appel(f"/api/sections?groupId={g1}", jeton=jeton)
carte = carte.get("sections", carte) if isinstance(carte, dict) else {}
avec_sections = [c for c in cours if str(c["id"]) in carte]
if avec_sections:
    module = avec_sections[0]
    date_activite(module["id"], j(-14), vue=j(-12))
    liste = carte[str(module["id"])]["sections"]
    for i, sec in enumerate(liste[:3]):
        date_activite(module["id"], j(-14 + i * 4), section=sec["id"])
    print(f"{len(liste[:3])} sections datées sur « {module['title']} »")
else:
    print("aucun module découpé au catalogue")


# ── Dépôts d'enseignant ──
# La capsule « Dépôt de matériel » parle de déposer sa propre version d'une
# séance : sans dépôt à l'écran, la voix décrit quelque chose d'invisible.
# On en pose donc deux, en réutilisant de vrais fichiers officiels comme
# contenu — ce qui compte à l'image, c'est l'entrée, pas les octets.

def televerser(chemins_champs, fichier, nom_affiche, jeton):
    """POST multipart sans dépendance : `urllib` ne sait pas le faire seul."""
    limite = f"----francisation{uuid.uuid4().hex}"
    morceaux = []
    for cle, valeur in chemins_champs.items():
        morceaux.append(
            f"--{limite}\r\nContent-Disposition: form-data; name=\"{cle}\"\r\n\r\n"
            f"{valeur}\r\n".encode())
    morceaux.append(
        f"--{limite}\r\nContent-Disposition: form-data; name=\"fichier\"; "
        f"filename=\"{nom_affiche}\"\r\n"
        "Content-Type: application/octet-stream\r\n\r\n".encode())
    morceaux.append(fichier.read_bytes())
    morceaux.append(f"\r\n--{limite}--\r\n".encode())
    corps = b"".join(morceaux)

    req = urllib.request.Request(BASE + "/api/materiel/depot", data=corps, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={limite}")
    req.add_header("X-Prof-Token", jeton)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


inventaire = appel("/api/materiel", jeton=jeton)["materiel"]
# Un module de cours produit : c'est le seul qui montre ses seize séances
# codées à l'écran, donc le seul sur lequel un dépôt se voit.
porteur = next((p for p in inventaire.get("porteurs", [])
                if p.get("categorie") == "cours"
                and len([s for s in p.get("seances", []) if s.get("code")]) > 4), None)
if porteur:
    seances = [s for s in porteur["seances"] if s.get("code") and s.get("fichiers")]
    poses = 0
    for seance, genre, nom, note in (
        (seances[2] if len(seances) > 2 else seances[0], "presentation",
         "version-retravaillee-groupe-du-soir.pptx",
         "Diapositives allégées : deux exemples de moins, plus de temps de parole."),
        (seances[3] if len(seances) > 3 else seances[-1], "fiche",
         "exercice-supplementaire-conjugaison.pdf",
         "Un exercice de plus pour les personnes qui finissent avant les autres."),
    ):
        officiel = next((f for f in seance["fichiers"] if f.get("chemin")), None)
        if not officiel:
            continue
        source = DEPOT / officiel["chemin"]
        if not source.exists():
            continue
        televerser({
            "activiteId": str(porteur["activiteId"]),
            "seanceCode": seance.get("code", ""),
            "type": genre,
            "note": note,
        }, source, nom, jeton)
        poses += 1
    titre = next((a["title"] for a in activites if a["id"] == porteur["activiteId"]), "?")
    print(f"{poses} dépôts d'enseignant posés sur « {titre} »")
else:
    print("aucun module porteur : pas de dépôt posé")

print("terminé")
