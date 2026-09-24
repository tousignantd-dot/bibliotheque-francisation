#!/usr/bin/env python3
"""La voix de chaque mot du lexique de la Maison Francœur.

    python3 build/audio_francoeur.py            # ce qui manque seulement
    python3 build/audio_francoeur.py --compter  # extraits et caractères, sans rien payer
    python3 build/audio_francoeur.py --refaire  # tout, de nouveau

Feu vert de Daniel pour ces voix neuves le 24 septembre 2026 (le gel des MP3
porte sur la RÉGÉNÉRATION des modules existants, pas sur celles-ci).

UNE VOIX, UN DÉBIT : `enseignante` (Sylvie, neurale — reproductible, à la
différence des voix HD) au taux de la famille des sons, TAUX_SONS. Un mot que
l'employé doit imiter gagne à être plus posé que la parole courante ; c'est le
client, au jeu de rôle, qui parlera vite.

LE MOT SE DIT AVEC SON ARTICLE, tel qu'il est écrit au lexique : un mot nu
court se fait dire à l'anglaise (« polo », « short »), l'article le tient en
français. Les couleurs et les tailles, qui n'en ont pas, sont à ÉCOUTER sur la
page des planches avant de conclure.

Sortie : assets/interactive/francoeur/sons/<id>.mp3
"""
import argparse, pathlib, sys
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
sys.path.insert(0, str(RACINE / "build" / "contenu" / "entreprise-francoeur"))
import azure_voix  # noqa: E402
from lexique import LEXIQUE  # noqa: E402

SORTIE = RACINE / "assets" / "interactive" / "francoeur" / "sons"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refaire", action="store_true")
    ap.add_argument("--compter", action="store_true")
    a = ap.parse_args()
    if a.compter:
        print("%d extraits, %d caractères" % (len(LEXIQUE), sum(len(e[2]) for e in LEXIQUE)))
        return
    SORTIE.mkdir(parents=True, exist_ok=True)
    cle, region = azure_voix.cle_region()
    a_faire = [e for e in LEXIQUE if a.refaire or not (SORTIE / f"{e[0]}.mp3").exists()]

    def un(e):
        dest = SORTIE / f"{e[0]}.mp3"
        try:
            d = azure_voix.parle(e[2], "enseignante", dest, cle=cle, region=region,
                                 reference=azure_voix.TAUX_SONS)
            print("  %-16s %4.2f s  %s" % (e[0], d, e[2]), flush=True)
        except Exception as x:
            print("  %-16s ÉCHEC %s" % (e[0], x), flush=True)
            return e[0]

    with ThreadPoolExecutor(4) as pool:
        echecs = [r for r in pool.map(un, a_faire) if r]
    print("%d produits, %d échecs %s → %s" % (len(a_faire) - len(echecs), len(echecs),
                                              echecs or "", SORTIE.relative_to(RACINE)))


if __name__ == "__main__":
    main()
