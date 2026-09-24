#!/usr/bin/env python3
"""La voix de chaque mot du lexique de la Maison Francœur.

    python3 build/audio_francoeur.py            # ce qui manque seulement
    python3 build/audio_francoeur.py --compter  # extraits et caractères, sans rien payer
    python3 build/audio_francoeur.py --refaire  # tout, de nouveau

Feu vert de Daniel pour ces voix neuves le 24 septembre 2026 (le gel des MP3
porte sur la RÉGÉNÉRATION des modules existants, pas sur celles-ci).

UNE VOIX, UN DÉBIT : Sylvie HD (voir HD plus bas) au taux de la famille des
sons, TAUX_SONS. Un mot que
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

# AZURE HD PARTOUT — décision de Daniel, 24 septembre 2026. Il n'y a que deux
# voix HD fr-CA : Sylvie et Thierry. Les rôles écrits dans le contenu
# (demandes.py, test.py) gardent leurs noms de personnages ; c'est ici qu'ils
# tombent sur une voix HD. Deux clients du même genre partagent donc une voix,
# ce qui est permis : ils ne se répondent jamais dans un même extrait.
#
# Deux choses à savoir sur la HD (mémoire voix-hd-langue-et-hasard) : elle
# choisit la langue MOT À MOT — `ssml()` enveloppe tout le corps dans <lang>,
# c'est la seule parade qui porte — et elle n'est pas déterministe : deux
# tirages du même texte ne sonnent pas pareil. D'où le contrôle par
# retranscription, build/francoeur_ecoute.py, à passer après chaque tirage.
HD = {"enseignante": "hd_feminin", "feminin_2": "hd_feminin",
      "masculin_1": "hd_masculin", "narrateur": "hd_masculin"}
VOIX_MOTS = "hd_feminin"

# LES PRONONCIATIONS CHOISIES À L'OREILLE (build/francoeur_reprises.py, choix de
# Daniel du 24 septembre 2026). Le TEXTE ENVOYÉ À LA VOIX peut différer de ce
# que l'écran affiche : une graphie qui ne peut se lire qu'en français empêche
# la HD de basculer à l'anglaise. L'écran garde l'orthographe du lexique.
# {id: (texte dit, rôle)} — un rôle neural (« enseignante ») est permis ici,
# par exception à « HD partout », si c'est lui qui sonne juste.
PRONONCIATION = {
    "lin": ("le lin", "hd_feminin"),              # nouvelle prise HD retenue
    "polyester": ("le polyestère", "hd_feminin"),
    "rose": ("rôse", "hd_feminin"),
}


RAPIDE = "+20%"   # le client qui parle trop vite : c'est ce qu'on fait répéter
VENDEUR = "hd_masculin"   # le vendeur modèle : toujours la même voix (Thierry HD)
CLIENT_MODELE = "hd_feminin"


def mot_dit(ident, texte):
    """Le texte envoyé à la voix pour un mot du lexique (PRONONCIATION d'abord)."""
    return PRONONCIATION.get(ident, (texte, VOIX_MOTS))[0]


def travaux():
    """Tout ce qui se synthétise, en une liste : (fichier, texte, rôle, taux).
    Un seul chemin pour tout, pour que tout se régénère de la même façon."""
    import gerante as G, modeles as MO, fiche as FI
    t = []
    for e in LEXIQUE:
        texte, role = PRONONCIATION.get(e[0], (e[2], VOIX_MOTS))
        t.append((f"{e[0]}.mp3", texte, role, azure_voix.TAUX_SONS))
        # L'autre mot se fait entendre aussi (audit A2 : « des bobettes »,
        # « un zipper » n'étaient jamais dits). Pas les codes (XS, M…).
        if e[3] and len(e[3]) > 2:
            t.append((f"autre/{e[0]}.mp3", e[3], VOIX_MOTS, azure_voix.TAUX_SONS))
    for d in DEMANDES:
        t.append((f"demandes/{d[0]}.mp3", d[2], HD[d[1]], None))
    for b in list(TEST.B) + list(TEST.B2):
        t.append((f"test/{b[0]}.mp3", b[3], HD[b[2]], None))
    for c in list(TEST.C) + list(TEST.C2):
        t.append((f"test/{c[0]}.mp3", c[2], HD[TEST.VOIX_GERANTE], None))
    for d in TEST.D:
        t.append((f"test/{d[0]}.mp3", d[2], HD[d[1]], RAPIDE if d[5] else None))
    # La partie A du test dite par une VOIX DE CLIENT, jamais celle des planches
    # (audit F1 : le test rejouait les mêmes MP3 que l'apprentissage).
    lex = {e[0]: e for e in LEXIQUE}
    cibles = (TEST.A_CRAN1 + TEST.A_CRAN2 + [x for x, _ in TEST.A_CRAN3]
              + TEST.A2_CRAN1 + TEST.A2_CRAN2 + [x for x, _ in TEST.A2_CRAN3])
    for i in cibles:
        t.append((f"test/a-{i}.mp3", mot_dit(i, lex[i][2]), "hd_masculin", azure_voix.TAUX_SONS))
    for c in G.CONSIGNES:
        t.append((f"gerante/{c[0]}.mp3", c[1], HD[TEST.VOIX_GERANTE], None))
    for m in MO.MODELES:
        for n, (qui, texte) in enumerate(m[2], 1):
            role = VENDEUR if qui == "vendeur" else CLIENT_MODELE
            t.append((f"modeles/{m[0]}-{n}.mp3", texte, role, RAPIDE if qui == "client-rapide" else None))
    for r in MO.REPONSES:
        t.append((f"reponses/{r[0]}-client.mp3", r[2], CLIENT_MODELE, RAPIDE if r[1] == "client-rapide" else None))
        t.append((f"reponses/{r[0]}-bonne.mp3", r[3], VENDEUR, None))
    for i, texte, _q in FI.PHRASES:
        t.append((f"phrases/{i}.mp3", texte.replace("…", ","), VENDEUR, None))
    t.append(("accueil.mp3", "Bonjour ! Avez-vous des tuques ?", CLIENT_MODELE, None))
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refaire", action="store_true")
    ap.add_argument("--compter", action="store_true")
    ap.add_argument("fichiers", nargs="*", help="refaire seulement ces fichiers (chemins sous sons/)")
    a = ap.parse_args()
    tout = travaux()
    if a.compter:
        manquent = [x for x in tout if not (SORTIE / x[0]).exists()]
        print("%d extraits, %d caractères ; %d manquent (%d caractères)"
              % (len(tout), sum(len(x[1]) for x in tout), len(manquent), sum(len(x[1]) for x in manquent)))
        return
    cle, region = azure_voix.cle_region()
    a_faire = [x for x in tout if a.refaire or x[0] in a.fichiers or not (SORTIE / x[0]).exists()]

    def un(x):
        chemin, texte, role, taux = x
        dest = SORTIE / chemin
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            d = azure_voix.parle(texte, role, dest, cle=cle, region=region, reference=taux)
            print("  %-28s %4.2f s  %s" % (chemin, d, texte[:50]), flush=True)
        except Exception as e:
            print("  %-28s ÉCHEC %s" % (chemin, e), flush=True)
            return chemin

    with ThreadPoolExecutor(4) as pool:
        echecs = [r for r in pool.map(un, a_faire) if r]
    print("%d produits, %d échecs %s → %s" % (len(a_faire) - len(echecs), len(echecs),
                                              echecs or "", SORTIE.relative_to(RACINE)))


if __name__ == "__main__":
    main()
