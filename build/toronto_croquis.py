#!/usr/bin/env python3
"""Les croquis d'« Une semaine à Toronto » — même appel que Compostelle, autre contenu.

    python3 build/toronto_croquis.py --essai        # consignes et coût, sans appel
    python3 build/toronto_croquis.py streetcar      # ces images-là
    python3 build/toronto_croquis.py --temoins      # les trois témoins du cadrage

Le registre est le préambule OBJET de Francœur. Les sujets vivent dans
build/contenu/toronto/sujets.py. Coût : 0,067 $ l'image, registre des appels tenu.
"""
import importlib.util, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import compostelle_croquis as CC  # noqa: E402  (appel Google, blanchiment, registre)
import francoeur_croquis as FC  # noqa: E402

sp = importlib.util.spec_from_file_location("toronto_sujets", RACINE / "build/contenu/toronto/sujets.py")
SJ = importlib.util.module_from_spec(sp); sp.loader.exec_module(SJ)
DEST = RACINE / "assets" / "interactive" / "toronto" / "croquis"


def cibles():
    pre = {"objet": FC.PREAMBULES["objet"], "scene": SJ.SCENE, "corps": SJ.CORPS, "geste": SJ.GESTE}
    # Chaque croquis du lexique doit avoir son sujet (et aucun sujet ne doit être orphelin).
    sp2 = importlib.util.spec_from_file_location("toronto_lexique", RACINE / "build/contenu/toronto/lexique.py")
    LX = importlib.util.module_from_spec(sp2); sp2.loader.exec_module(LX)
    voulus = {e[0] for e in LX.LEXIQUE if e[4] == "croquis"}
    assert voulus == set(SJ.SUJETS), ("croquis sans sujet", voulus - set(SJ.SUJETS), "sujets orphelins", set(SJ.SUJETS) - voulus)
    return {("mot", k): (pre[f] + q, "1:1", DEST, 800) for k, (f, q) in SJ.SUJETS.items()}


if __name__ == "__main__":
    t = cibles()
    args = sys.argv[1:]
    noms = SJ.TEMOINS if "--temoins" in args else [a for a in args if not a.startswith("--")]
    cib = [c for c in t if c[1] in noms] if noms else [c for c in t if not (DEST / f"{c[1]}.png").exists()]
    if "--essai" in args:
        for c in cib:
            print(f"  {c[1]:12} {len(t[c][0])} car.")
        print(f"{len(cib)} images, ≈ {len(cib) * 0.067:.2f} $"); sys.exit(0)
    for c in cib:
        CC.generer(c, t)
