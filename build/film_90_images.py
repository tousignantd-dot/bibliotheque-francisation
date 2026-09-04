#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Les images du film de 90 secondes — cinq générées, le reste composé.

    python3 build/film_90_images.py --devis      # ce que ça coûterait
    python3 build/film_90_images.py              # génère ce qui manque

**Cinq images seulement passent par un modèle.** Les quatre autres — le point
du « i », les quatre interrupteurs, les flèches qui cessent de sortir, la
signature — sont de la géométrie et du texte : elles se composent en HTML et se
photographient par Chrome, comme les pictogrammes des banques. C'est la règle
du dépôt : un modèle d'image écrit du charabia dès qu'une inscription entre
dans le cadre, et ces quatre plans-là en portent forcément.

Les quatre règles de prompt du dépôt s'appliquent : aucun texte dans l'image,
pas de mains ni de visages en gros plan, un décor québécois nommé, et l'image
montre **ce que dit sa réplique** — pas le thème du film. La parade aux deux
premières n'est pas de les répéter mais de **cadrer** : on décrit ce qu'on
veut voir, jamais ce qu'on ne veut pas.

Sortie à plat dans ~/Claude/generations avec son journal .json, comme l'impose
la compétence /generate, puis recopie dans le dossier du film.
"""

import argparse
import base64
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.request

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "film-90-secondes"
GENERATIONS = pathlib.Path.home() / "Claude" / "generations"
ENV = pathlib.Path.home() / "Claude" / ".env"

MODELE = "gemini-3.1-flash-lite-image"      # brouillon, 0,0336 $ en direct
PRIX_UNITAIRE = 0.0336

STYLE = (" Illustration vectorielle plate, sans contour épais, fond crème uni "
         "#F7F7F5, palette sobre et chaude avec un seul accent bleu acier. "
         "Les personnes sont des silhouettes pleines, sans aucun trait de "
         "visage. Aucune lettre, aucun chiffre, aucune enseigne, aucun "
         "panneau, aucun écran allumé : les surfaces sont nues. Cadrage large, "
         "beaucoup d'air autour du sujet. Format paysage 16:9.")

PLANS = {
    "02": ("Un comptoir de service public vu de trois quarts, dans un édifice "
           "québécois ordinaire. Devant le comptoir, une personne debout vue "
           "de dos. Derrière, une employée qui attend, penchée en avant. "
           "Au-dessus de la personne de dos, une grande bulle de dialogue "
           "entièrement VIDE, contour fin, intérieur blanc." + STYLE),
    "03": ("Au premier plan, une grande bulle de dialogue entièrement VIDE, "
           "contour fin, intérieur blanc, qui occupe le tiers du cadre. "
           "Derrière elle, très adoucie et en retrait, une petite file "
           "d'attente de silhouettes dans un couloir de bureau." + STYLE),
    "04": ("Une table de cuisine en bois clair vue de haut, dans un logement "
           "québécois modeste. Posé dessus, un téléphone à plat dont l'écran "
           "est éteint et sombre. À côté, une tasse et un trousseau de clés. "
           "La pièce est vide, la lumière vient d'une fenêtre hors champ." + STYLE),
    "07": ("Une bande horizontale de quatre petites vignettes carrées de même "
           "taille, séparées par un mince filet clair : une salle d'attente de "
           "clinique avec ses chaises alignées ; une table avec des feuilles "
           "de papier et un stylo posé ; l'intérieur d'un autobus urbain avec "
           "ses barres verticales ; un comptoir de bureau de poste avec des "
           "boîtes empilées. Style pictogramme détaillé." + STYLE),
    "10": ("Une salle de classe en vue isométrique, légèrement en plongée. "
           "Quinze pupitres alignés en rangées régulières, vides. Devant eux, "
           "seule, la silhouette debout d'une enseignante vue de dos. "
           "Au-dessus de chaque pupitre flotte une petite barre horizontale "
           "arrondie, chacune d'une couleur différente et remplie à un niveau "
           "différent." + STYLE),
}


def cle(nom):
    for ligne in ENV.read_text(encoding="utf-8").splitlines():
        if ligne.startswith(nom + "="):
            return ligne.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def demander_google(prompt, clef):
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           "%s:generateContent?key=%s" % (MODELE, clef))
    corps = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
    req = urllib.request.Request(url, data=corps,
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": "film90/1.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.load(r)
    for p in d["candidates"][0]["content"]["parts"]:
        if "inlineData" in p:
            return base64.b64decode(p["inlineData"]["data"])
        if "inline_data" in p:
            return base64.b64decode(p["inline_data"]["data"])
    raise RuntimeError("aucune image dans la réponse")


def demander_fal(prompt, clef):
    """Repli. Il coûte plus du double du direct — on le dit quand on l'emprunte."""
    corps = json.dumps({"prompt": prompt, "num_images": 1,
                        "aspect_ratio": "16:9", "resolution": "1K",
                        "output_format": "jpeg"}).encode()
    req = urllib.request.Request("https://fal.run/fal-ai/nano-banana-2",
                                 data=corps,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Key " + clef,
                                          "User-Agent": "film90/1.0"})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.load(r)
    u = d["images"][0]["url"]
    with urllib.request.urlopen(u, timeout=120) as r:
        return r.read()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--devis", action="store_true")
    ap.add_argument("--refaire", nargs="*", default=None,
                    help="numéros de plan à refaire malgré leur présence")
    a = ap.parse_args()

    refaire = set(a.refaire or [])
    a_faire = [n for n in sorted(PLANS)
               if n in refaire or not (SORTIE / ("plan-%s.jpg" % n)).exists()]
    if a.devis or not a_faire:
        print("À générer : %d image(s) — %s" % (len(a_faire), ", ".join(a_faire) or "aucune"))
        print("Coût estimé : %.2f $ US (route Google directe, %.4f $ l'unité)"
              % (len(a_faire) * PRIX_UNITAIRE, PRIX_UNITAIRE))
        if a.devis:
            return 0
        if not a_faire:
            return 0

    SORTIE.mkdir(parents=True, exist_ok=True)
    GENERATIONS.mkdir(parents=True, exist_ok=True)
    gk, fk = cle("GOOGLE_API_KEY"), cle("FAL_KEY")
    depense = 0.0
    for num in a_faire:
        prompt = PLANS[num]
        print("  plan %s …" % num, end="", flush=True)
        octets, route = None, None
        if gk:
            try:
                octets, route = demander_google(prompt, gk), "google"
            except Exception as e:
                print(" (google refuse : %s)" % str(e)[:60], end="", flush=True)
        if octets is None and fk:
            octets, route = demander_fal(prompt, fk), "fal.ai"
        if octets is None:
            print(" ÉCHEC — aucune route disponible")
            continue
        horo = time.strftime("%Y%m%d-%H%M%S")
        base = GENERATIONS / ("film90_plan-%s_%s" % (num, horo))
        base.with_suffix(".jpg").write_bytes(octets)
        base.with_suffix(".json").write_text(json.dumps(
            {"projet": "film90", "plan": num, "modele": MODELE, "route": route,
             "prompt": prompt, "cout_estime_usd": PRIX_UNITAIRE}, ensure_ascii=False,
            indent=1), encoding="utf-8")
        (SORTIE / ("plan-%s.jpg" % num)).write_bytes(octets)
        depense += PRIX_UNITAIRE
        print(" %s · %d ko · %s" % (route, len(octets) // 1000, base.name))
    print("\nDépense estimée : %.2f $ US" % depense)
    return 0


if __name__ == "__main__":
    sys.exit(main())
