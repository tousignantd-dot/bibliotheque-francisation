#!/usr/bin/env python3
"""« Lentement » veut-il dire deux fois la même chose ? Cinq tirages par palier.

    python3 build/essai_ralenti.py

Ce que le banc précédent laissait ouvert
----------------------------------------
`essai_gemini_tts.py` a montré que la consigne en langue naturelle produit des
paliers propres — 1,00 / 0,65 / 0,50 — mais sur **un seul tirage chacun**. Or
c'est justement ce qui sépare Gemini d'Azure : le SSML `<prosody rate="-20%">`
est un nombre, la consigne « lentement » est une intention, et rien ne promet
qu'elle soit honorée deux fois pareil. Un cours entier bâti sur une intention
instable donnerait des mini-leçons dont le débit change d'un extrait à
l'autre — pire qu'un débit trop rapide mais constant.

Ce que ce banc mesure, et pourquoi le recouvrement compte plus que l'écart-type
------------------------------------------------------------------------------
Cinq tirages de la **même phrase** avec la **même consigne**, pour chacun des
trois paliers. On en tire la moyenne et la dispersion, mais le verdict tient à
une question plus simple : **les paliers se chevauchent-ils ?**

Un écart-type de 8 % est sans conséquence si le tirage le plus lent de
« normal » reste plus rapide que le tirage le plus rapide de « lent » — l'élève
entendra toujours trois vitesses distinctes. Le même écart-type devient
rédhibitoire si les nuages se recoupent : deux extraits voisins de la même
leçon pourraient alors sortir dans le désordre, un « lent » plus rapide qu'un
« normal ». C'est ce que la ligne RECOUVREMENT tranche.

La durée est mesurée sur le MP3 par `ffprobe`, pas estimée : les silences de
début et de fin comptent dans ce que l'élève attend, et c'est le débit perçu
qu'on juge, non le débit d'articulation.
"""
import pathlib
import statistics
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from essai_gemini_tts import (PALIERS, PHRASE, Transitoire,  # noqa: E402
                              avec_reprises, cle, synthese)

SORTIE = pathlib.Path.home() / "Claude" / "generations" / "essai-ralenti"
TIRAGES = 5
VOIX = "Kore"


def main():
    k = cle()
    if not k:
        print("GOOGLE_API_KEY absente de ~/Claude/.env")
        return 1
    SORTIE.mkdir(parents=True, exist_ok=True)

    mesures = {}
    for nom, consigne in PALIERS:
        mesures[nom] = []
        for i in range(1, TIRAGES + 1):
            f = SORTIE / ("%s-%d.mp3" % (nom, i))
            try:
                d, _ = avec_reprises(
                    lambda: synthese(consigne, PHRASE, VOIX, k, f))
            except (Transitoire, subprocess.CalledProcessError) as e:
                print("  %-12s %d  ÉCHEC %s" % (nom, i, e))
                continue
            cs = len(PHRASE) / d
            mesures[nom].append((d, cs))
            print("  %-12s %d  %5.2f s  %5.1f c/s" % (nom, i, d, cs))

    print("\n%-12s %8s %8s %8s %8s %7s" %
          ("palier", "moy s", "min s", "max s", "moy c/s", "écart"))
    ref = None
    for nom, _ in PALIERS:
        m = mesures[nom]
        if len(m) < 2:
            print("%-12s  trop peu de tirages" % nom)
            continue
        ds = [x[0] for x in m]
        css = [x[1] for x in m]
        moy = statistics.mean(ds)
        # Le coefficient de variation dit la dispersion en proportion, ce qui
        # est la seule façon de comparer un palier lent à un palier rapide.
        cv = statistics.stdev(ds) / moy * 100
        if ref is None:
            ref = moy
        print("%-12s %8.2f %8.2f %8.2f %8.1f %6.1f%%  ratio %.2f"
              % (nom, moy, min(ds), max(ds), statistics.mean(css), cv, ref / moy))

    # Le verdict : deux paliers voisins se chevauchent-ils ?
    print()
    ok = True
    noms = [n for n, _ in PALIERS]
    for a, b in zip(noms, noms[1:]):
        if len(mesures[a]) < 2 or len(mesures[b]) < 2:
            continue
        pire_a = max(x[0] for x in mesures[a])     # le plus lent des rapides
        pire_b = min(x[0] for x in mesures[b])     # le plus rapide des lents
        marge = (pire_b - pire_a) / pire_a * 100
        verdict = "séparés" if pire_b > pire_a else "SE CHEVAUCHENT"
        ok = ok and pire_b > pire_a
        print("RECOUVREMENT %-10s → %-10s  %5.2f s vs %5.2f s  %+6.1f%%  %s"
              % (a, b, pire_a, pire_b, marge, verdict))
    print("\n%s" % ("Les paliers sont distincts à tous les tirages."
                    if ok else
                    "Au moins deux paliers se recoupent : la consigne seule "
                    "ne suffit pas, il faudrait vérifier chaque extrait."))
    print("Fichiers dans %s" % SORTIE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
