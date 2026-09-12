#!/usr/bin/env python3
"""Contrôle de la recherche dans le contenu.

Il ne lit pas le code : il dépouille le dépôt pour de vrai, puis pose les
questions auxquelles cette recherche existe pour répondre. Chacune a coûté
quelque chose — un piège vu à l'écran, une mesure, un résultat aberrant.

    python3 build/controles/recherche.py

Sort en code 1 au premier écart, comme les autres contrôles du dépôt.
"""
import json
import sys
import time
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RACINE))

import recherche as R   # noqa: E402

ECHECS = []


def verifie(nom, condition, detail=""):
    if condition:
        print("  ok   %s" % nom)
    else:
        print("  RATÉ %s %s" % (nom, detail))
        ECHECS.append(nom)


def titres(resultat):
    return [e["titre"] for e in resultat["extraits"]]


print("— Le dépouillement —")
activites = json.loads((RACINE / "data" / "activities.json").read_text("utf-8"))
debut = time.time()
index = R.construire(RACINE, activites)
duree = time.time() - debut
modules = [d for d in index.documents if d["type"] == "module"]
fiches = [d for d in index.documents if d["type"] == "fiche"]
print("  %d documents (%d modules, %d fiches) en %.1f s"
      % (len(index.documents), len(modules), len(fiches), duree))
verifie("les modules sont dépouillés", len(modules) > 150, str(len(modules)))
verifie("les fiches aussi", len(fiches) > 1000, str(len(fiches)))
verifie("aucun fichier illisible", not index.erreurs, str(index.erreurs[:2]))

# Le piège central : le contenu d'un module vit dans des constantes
# JavaScript. Un extracteur qui retire les scripts rend un module vide, et la
# recherche ne trouve jamais une réplique de dialogue.
gros = max(modules, key=lambda d: len(d["texte"]))
verifie("un module porte plus que son habillage", len(gros["texte"]) > 20000,
        "%d caractères pour %s" % (len(gros["texte"]), gros["titre"]))
verifie("les modules ne sont pas vides",
        all(len(d["texte"]) > 500 for d in modules),
        str([d["chemin"] for d in modules if len(d["texte"]) <= 500][:3]))

print("\n— L'aplatissement garde la longueur —")
# C'est la condition de l'extrait : il se découpe dans le texte d'origine, aux
# positions trouvées dans le texte aplati. Un seul caractère d'écart et
# l'extrait glisse, puis se coupe au milieu d'un mot. Mesuré une fois à quatre
# caractères d'écart sur un module, à cause de sélecteurs de variante.
ecarts = [d["chemin"] for d in index.documents if len(d["plat"]) != len(d["texte"])]
verifie("aucun document en écart", not ecarts, str(ecarts[:3]))
verifie("les accents tombent",
        R.sans_accents("La Visite du Quatre et Demie — ÉTÉ, Ça va ?")
        == "la visite du quatre et demie — ete, ca va ?")

print("\n— Ce que l'utilisateur a demandé —")
res = R.chercher(index, "la visite du quatre et demie")
verifie("« la visite du quatre et demie » trouve quelque chose", bool(res))
premier = res[0] if res else {"extraits": []}
verifie("et la fiche de séance est en tête",
        any("quatre et demie" in t.lower() for t in titres(premier)),
        str(titres(premier)))
verifie("le module qui porte le dialogue est là aussi",
        any(e["type"] == "module" for e in premier["extraits"]),
        str([e["type"] for e in premier["extraits"]]))
verifie("l'extrait montre la phrase, pas le début du document",
        any("quatre et demie" in e["extrait"].lower() for e in premier["extraits"]),
        str([e["extrait"][:60] for e in premier["extraits"]]))

print("\n— Les mots ne se rencontrent pas par hasard —")
# Sans la fenêtre, « visite » au début d'un module et « quatre » à la fin
# faisaient un résultat : huit modules sans rapport remontaient devant la bonne
# fiche. La borne est la seule chose qui distingue une recherche d'un filtre.
verifie("la recherche reste courte", len(res) <= 6,
        "%d activités" % len(res))
eparpille = R.chercher(index, "pharmacie olympique")
verifie("deux mots sans rapport ne se rejoignent pas", len(eparpille) <= 2,
        "%d activités" % len(eparpille))

print("\n— Les mots vides —")
verifie("ils ne portent pas la recherche",
        R.mots_pleins("la visite du quatre et demie") == ["visite", "quatre", "demie"],
        str(R.mots_pleins("la visite du quatre et demie")))
# « Je me lance » est le nom d'une section : une recherche qui n'a que des mots
# vides doit quand même chercher, au lieu de ne rien exiger et tout rendre.
verifie("une requête qui n'a qu'eux les garde",
        R.mots_pleins("je me lance") == ["lance"] or "lance" in R.mots_pleins("je me lance"),
        str(R.mots_pleins("je me lance")))
verifie("une recherche vide ne rend rien", R.chercher(index, "   ") == [])
verifie("un mot introuvable ne rend rien",
        R.chercher(index, "zzzqwerty") == [])

print("\n— Le bornage —")
# Une recherche qui rendrait le titre, ou même seulement le nombre, apprendrait
# ce qu'il y a derrière une porte fermée.
permises = {res[0]["activiteId"]} if res else set()
borne = R.chercher(index, "la visite du quatre et demie", permises)
verifie("rien ne sort de ce qui est permis",
        all(r["activiteId"] in permises for r in borne), str(borne[:1]))
verifie("et une permission vide ne rend rien",
        R.chercher(index, "la visite du quatre et demie", set()) == [])

print("\n— Le coût —")
# L'index vit en mémoire dans le conteneur : ce contrôle est l'endroit où on
# s'en aperçoit si un jour il double.
octets = sum(len(d["texte"]) + len(d["plat"]) for d in index.documents)
print("  %d Mo de texte, %.1f s de dépouillement" % (octets // 1024 // 1024, duree))
verifie("le texte gardé reste raisonnable", octets < 60 * 1024 * 1024,
        "%d Mo" % (octets // 1024 // 1024))
t0 = time.time()
for q in ("bail", "mise en demeure", "la visite du quatre et demie"):
    R.chercher(index, q)
verifie("une recherche reste sous la demi-seconde",
        (time.time() - t0) / 3 < 0.5, "%.0f ms" % ((time.time() - t0) / 3 * 1000))

print()
if ECHECS:
    print("%d contrôle(s) en échec : %s" % (len(ECHECS), ", ".join(ECHECS)))
    sys.exit(1)
print("Tous les contrôles passent.")
