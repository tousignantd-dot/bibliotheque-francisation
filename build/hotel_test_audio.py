#!/usr/bin/env python3
"""Les voix du test de la réception (étape 3), dans les trois langues.

    python3 build/hotel_test_audio.py     # ce qui manque, puis contrôle

Les clients alternent une voix d'homme et une voix de femme (id pair / impair).
- A (la demande) : au débit d'un client, +10 %, comme « Ce que le client veut ».
- B (au téléphone) : débit normal, puis le FILTRE DU TÉLÉPHONE (300-3400 Hz) ;
  au cran 3, le nom épelé est ASSEMBLÉ lettre par lettre (hotel_audio.assembler)
  et filtré lui aussi.
- C et D : débit normal.

Contrôle : retranscription dans la langue de l'extrait (sauf les noms épelés),
et recherche des durées aberrantes (> 3 × la médiane) — la HD déraille parfois.

Sortie : assets/interactive/hotel/sons/test/<partie>/<langue>/<id>.mp3
"""
import difflib, importlib.util, pathlib, shutil, statistics, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
_s = importlib.util.spec_from_file_location("hotel_audio", RACINE / "build/hotel_audio.py")
HA = importlib.util.module_from_spec(_s); _s.loader.exec_module(HA)
_t = importlib.util.spec_from_file_location("hotel_test", RACINE / "build/contenu/entreprise-hotel/test.py")
T = importlib.util.module_from_spec(_t); _t.loader.exec_module(T)
DEST = HA.SONS / "test"
L = ("fr", "en", "es")


def voix(l, ident):
    return HA.VOIX_CLIENTS[l] if int("".join(c for c in ident if c.isdigit())) % 2 else HA.VOIX_MOTS[l]


def telephone(f):
    tmp = f.with_name(f.stem + ".tel.mp3")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(f), "-af",
                    "highpass=f=300,lowpass=f=3400,acompressor=threshold=-18dB:ratio=3",
                    "-ar", "24000", "-ac", "1", "-b:a", "96k", str(tmp)], check=True)
    shutil.move(tmp, f)


def taches():
    """(chemin, langue, texte, voix, débit, téléphone, à retranscrire)."""
    for forme in (1, 2):
        for i, _, dit, *_ in T.A[forme]:
            for l in L:
                yield DEST / "a" / l / f"{i}.mp3", l, dit[l], voix(l, i), "+10%", False, True
        for item in T.B[forme]:
            if item[1] != "nom":
                i, _, dit = item[:3]
                for l in L:
                    yield DEST / "b" / l / f"{i}.mp3", l, dit[l], voix(l, i), "0%", True, True
        for i, _, dit, _ in T.C[forme]:
            for l in L:
                yield DEST / "c" / l / f"{i}.mp3", l, dit[l], voix(l, i), "0%", False, True
        for i, _, dit, _, _ in T.D[forme]:
            for l in L:
                yield DEST / "d" / l / f"{i}.mp3", l, dit[l], voix(l, i), "0%", False, True


def duree(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout or 0)


if __name__ == "__main__":
    cle, region = HA.cle_region()
    a_faire = [t for t in taches() if not t[0].exists()]

    def une(t):
        f, l, texte, v, taux, tel, _ = t
        HA.synth(l, texte, f, cle, region, v, taux)
        if tel:
            telephone(f)
    with ThreadPoolExecutor(6) as pool:
        list(pool.map(une, a_faire))
    print(f"{len(a_faire)} extraits du test produits")

    # Les noms épelés du cran 3 de B : assemblés, puis filtrés (téléphone).
    for forme in (1, 2):
        for item in T.B[forme]:
            if item[1] == "nom":
                i, _, nom = item
                for l in L:
                    dest = DEST / "b" / l / f"{i}.mp3"
                    if not dest.exists():
                        src = HA.assembler(l, nom, cle, region)
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(src, dest)
                        if nom not in HA.EX.TELEPHONE:
                            telephone(dest)
    print("noms épelés du test assemblés")

    # Contrôle 1 : retranscription.
    def ecoute(t):
        f, l, texte = t[0], t[1], t[2]
        e, c = HA.retranscrire(f, l, cle, region)
        return f, texte, e, difflib.SequenceMatcher(None, HA.plat(texte), HA.plat(e)).ratio()
    with ThreadPoolExecutor(6) as pool:
        rel = list(pool.map(ecoute, [t for t in taches() if t[6]]))
    faibles = sorted([r for r in rel if r[3] < 0.8], key=lambda r: r[3])
    print(f"retranscription : {len(rel)} extraits, {len(faibles)} sous 0,8")
    for f, t, e, sm in faibles:
        print(f"  {f.relative_to(HA.SONS)}  {sm:.2f}  « {t} » → « {e} »")
    # Contrôle 2 : durées aberrantes.
    for partie in "abcd":
        fs = list((DEST / partie).glob("*/*.mp3"))
        ds = {f: duree(f) for f in fs}
        med = statistics.median(ds.values())
        ab = [(str(f.relative_to(HA.SONS)), round(v, 1)) for f, v in ds.items() if v > 3 * med]
        print(f"durées {partie} : {len(fs)} extraits, médiane {med:.1f} s, aberrants {ab or 'aucun'}")
