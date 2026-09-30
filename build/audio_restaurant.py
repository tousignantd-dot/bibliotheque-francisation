#!/usr/bin/env python3
"""La voix de chaque mot du lexique de Chez Jocelyne (restauration, étape 1).

    python3 build/audio_restaurant.py             # ce qui manque seulement
    python3 build/audio_restaurant.py --compter   # extraits et caractères, sans rien payer
    python3 build/audio_restaurant.py --controle  # retranscrit tout, relevé des douteux
    python3 build/audio_restaurant.py mot.mp3     # refaire ces fichiers

Feu vert de Daniel le 30 septembre 2026 (« feu vert pour les voix »). Même
règle que Francœur (audio_francoeur.py) : Sylvie HD au taux des sons, le mot
dit AVEC son article, l'autre mot dit aussi ; chaque tirage HD se contrôle par
retranscription (la HD n'est pas déterministe et choisit sa langue mot à mot).

Seul le français se dit : l'espagnol et l'anglais sont des langues d'appui
écrites (décision du 30 sept. 2026), le nombre de langues ne change rien ici.

Sortie : assets/interactive/restaurant/sons/<id>.mp3 et sons/autre/<id>.mp3 ;
relevé : build/contenu/entreprise-restaurant/ecoute.json
"""
import argparse, difflib, json, pathlib, re, sys
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-restaurant"
sys.path.insert(0, str(CONTENU))
sys.path.insert(0, str(RACINE / "build"))
import azure_voix  # noqa: E402
from lexique import LEXIQUE  # noqa: E402

SORTIE = RACINE / "assets" / "interactive" / "restaurant" / "sons"
RELEVE = CONTENU / "ecoute.json"
VOIX_MOTS = "hd_feminin"

# Le texte DIT peut différer du texte affiché (à remplir à l'oreille, comme
# PRONONCIATION chez Francœur). {id: texte dit}
PRONONCIATION = {}


def dit(texte):
    # Ce qui est entre parenthèses est une glose, pas un texte à dire.
    return re.sub(r"\s*\([^)]*\)", "", texte).strip()


def travaux():
    t = []
    for e in LEXIQUE:
        t.append((f"{e[0]}.mp3", PRONONCIATION.get(e[0], dit(e[2])), e[2]))
        if e[3] and len(e[3]) > 2:
            t.append((f"autre/{e[0]}.mp3", dit(e[3]), e[3]))
    return t


def controle():
    import francoeur_ecoute as FE
    cle, region = azure_voix.cle_region()

    def un(x):
        chemin, _dit, affiche = x
        entendu, conf = FE.retranscrire(SORTIE / chemin, cle, region)
        sim = difflib.SequenceMatcher(None, FE.plat(affiche), FE.plat(entendu)).ratio()
        return {"fichier": chemin, "attendu": affiche, "entendu": entendu,
                "similitude": round(sim, 2), "confiance": round(conf, 2),
                "douteux": sim < FE.SEUIL_SIMILITUDE or conf < FE.SEUIL_CONFIANCE}

    with ThreadPoolExecutor(6) as pool:
        rel = list(pool.map(un, [x for x in travaux() if (SORTIE / x[0]).exists()]))
    RELEVE.write_text(json.dumps(rel, ensure_ascii=False, indent=1), encoding="utf-8")
    dout = [r for r in rel if r["douteux"]]
    print(f"{len(rel)} retranscrits, {len(dout)} douteux")
    for r in sorted(dout, key=lambda r: r["similitude"]):
        print(f"  {r['fichier']:28} {r['similitude']:.2f} {r['confiance']:.2f}  {r['attendu']!r} → {r['entendu']!r}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--compter", action="store_true")
    ap.add_argument("--controle", action="store_true")
    ap.add_argument("fichiers", nargs="*")
    a = ap.parse_args()
    tout = travaux()
    if a.compter:
        manquent = [x for x in tout if not (SORTIE / x[0]).exists()]
        print("%d extraits, %d caractères ; %d manquent (%d caractères)"
              % (len(tout), sum(len(x[1]) for x in tout), len(manquent), sum(len(x[1]) for x in manquent)))
        return
    if a.controle:
        return controle()
    cle, region = azure_voix.cle_region()
    a_faire = [x for x in tout if x[0] in a.fichiers or (not a.fichiers and not (SORTIE / x[0]).exists())]

    def un(x):
        chemin, texte, _ = x
        dest = SORTIE / chemin
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            d = azure_voix.parle(texte, VOIX_MOTS, dest, cle=cle, region=region, reference=azure_voix.TAUX_SONS)
            print("  %-28s %4.2f s  %s" % (chemin, d, texte[:50]), flush=True)
        except Exception as e:
            print("  %-28s ÉCHEC %s" % (chemin, e), flush=True)
            return chemin

    with ThreadPoolExecutor(4) as pool:
        echecs = [r for r in pool.map(un, a_faire) if r]
    print("%d produits, %d échecs %s" % (len(a_faire) - len(echecs), len(echecs), echecs or ""))


if __name__ == "__main__":
    main()
