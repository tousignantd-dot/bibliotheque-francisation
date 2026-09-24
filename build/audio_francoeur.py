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

LES DEMANDES DES CLIENTS (étape 2, l'exercice « Ce que le client veut ») sont
dans `demandes.py` : trois voix de clients, au débit NORMAL — TAUX_GLOBAL, sans
palier lent. Le client parle vite, c'est la leçon ; l'écran offre « Plus
lentement ». Sortie : sons/demandes/<id>.mp3.

LE TEST (étape 3, `test.py`) : les clients des parties B et D au débit normal,
la gérante (Sylvie) au débit normal elle aussi — une consigne au travail ne se
dit pas lentement. Sortie : sons/test/<id>.mp3.
"""
import argparse, pathlib, sys
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
sys.path.insert(0, str(RACINE / "build" / "contenu" / "entreprise-francoeur"))
import azure_voix  # noqa: E402
from lexique import LEXIQUE  # noqa: E402
from demandes import DEMANDES  # noqa: E402
import test as TEST  # noqa: E402

SORTIE = RACINE / "assets" / "interactive" / "francoeur" / "sons"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refaire", action="store_true")
    ap.add_argument("--compter", action="store_true")
    a = ap.parse_args()
    if a.compter:
        print("%d mots, %d caractères" % (len(LEXIQUE), sum(len(e[2]) for e in LEXIQUE)))
        print("%d demandes, %d caractères" % (len(DEMANDES), sum(len(d[2]) for d in DEMANDES)))
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

    # Les demandes des clients : voix de client, débit normal (pas de TAUX_SONS).
    DEM = SORTIE / "demandes"
    DEM.mkdir(exist_ok=True)
    dem = [d for d in DEMANDES if a.refaire or not (DEM / f"{d[0]}.mp3").exists()]

    def une_demande(d):
        try:
            duree = azure_voix.parle(d[2], d[1], DEM / f"{d[0]}.mp3", cle=cle, region=region)
            print("  %-5s %-11s %4.2f s  %s" % (d[0], d[1], duree, d[2]), flush=True)
        except Exception as x:
            print("  %-5s ÉCHEC %s" % (d[0], x), flush=True)
            return d[0]

    # Le test : (id, voix, phrase) pour B, C et D, dans sons/test/.
    TST = SORTIE / "test"
    TST.mkdir(exist_ok=True)
    test = ([(b[0], b[2], b[3]) for b in TEST.B] + [(c[0], TEST.VOIX_GERANTE, c[2]) for c in TEST.C]
            + [(d[0], d[1], d[2]) for d in TEST.D])
    test = [t for t in test if a.refaire or not (TST / f"{t[0]}.mp3").exists()]

    def un_test(t):
        try:
            duree = azure_voix.parle(t[2], t[1], TST / f"{t[0]}.mp3", cle=cle, region=region)
            print("  %-5s %-11s %4.2f s  %s" % (t[0], t[1], duree, t[2][:60]), flush=True)
        except Exception as x:
            print("  %-5s ÉCHEC %s" % (t[0], x), flush=True)
            return t[0]

    with ThreadPoolExecutor(4) as pool:
        echecs = [r for r in pool.map(un, a_faire) if r]
        echecs += [r for r in pool.map(une_demande, dem) if r]
        echecs += [r for r in pool.map(un_test, test) if r]
    a_faire = a_faire + dem + test
    print("%d produits, %d échecs %s → %s" % (len(a_faire) - len(echecs), len(echecs),
                                              echecs or "", SORTIE.relative_to(RACINE)))


if __name__ == "__main__":
    main()
