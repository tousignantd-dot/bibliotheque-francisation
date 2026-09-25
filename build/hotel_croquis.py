#!/usr/bin/env python3
"""Les croquis de la réception d'hôtel — même registre que la Maison Francœur.

Reprend le préambule « objet », l'appel à Google, le blanchiment et le
registre des appels de `francoeur_croquis.py` ; seuls le lexique, les sujets
et le dossier changent. Le comptoir, lui, est une scène 3:2.

    python3 build/hotel_croquis.py --essai        # prompts, sans appel
    python3 build/hotel_croquis.py --temoins      # les témoins + le comptoir
    python3 build/hotel_croquis.py carte-cle      # ces entrées
    python3 build/hotel_croquis.py --comptoir     # le comptoir seul
"""
import base64, importlib.util, io, json, pathlib, sys, time, urllib.request
from PIL import Image

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import francoeur_croquis as FC  # noqa: E402  (préambules, clé, blanchiment)

def _charger(nom):
    p = RACINE / "build" / "contenu" / "entreprise-hotel" / f"{nom}.py"
    spec = importlib.util.spec_from_file_location(f"hotel_{nom}", p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

LEX = _charger("lexique")
SUJ = _charger("sujets")
DEST = RACINE / "assets" / "interactive" / "hotel" / "croquis"


def consigne(ident):
    if ident == "comptoir":
        return SUJ.COMPTOIR
    famille, quoi = SUJ.SUJETS[ident]
    if famille == "personne":
        # Le seul croquis avec une personne : le préambule « objet » sans la
        # phrase qui les exclut.
        return FC.PREAMBULES["objet"].replace("no person, no hand, ", "no other person, no hand in close-up, ").replace("THE OBJECT: ", "THE PERSON: ") + quoi
    return FC.PREAMBULES[famille] + quoi


def journal(ident, statut, note):
    sys.path.insert(0, str(FC.GEN))
    try:
        from journal_appels import enregistrer_appel
        enregistrer_appel("google", FC.MODELE, module="entreprise-hotel",
                          cible=f"croquis {ident}", statut=statut,
                          estimation=0.067 if statut == "ok" else 0, note=note)
    except Exception as e:
        print("  (registre : %s)" % e)


def servir(ident, largeur):
    im = FC.blanchir(Image.open(DEST / f"{ident}.png").convert("RGB"))
    im.resize((largeur, round(im.height * largeur / im.width)), Image.LANCZOS).save(
        DEST / f"{ident}.jpg", "JPEG", quality=82)


def generer(ident):
    ratio = "3:2" if ident == "comptoir" else "1:1"
    corps = {"contents": [{"parts": [{"text": consigne(ident)}]}],
             "generationConfig": {"responseModalities": ["IMAGE"],
                                  "imageConfig": {"aspectRatio": ratio}}}
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           f"{FC.MODELE}:generateContent?key=" + FC.cle("GOOGLE_API_KEY"))
    req = urllib.request.Request(url, data=json.dumps(corps).encode(),
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.loads(r.read())
    except Exception as e:
        journal(ident, "echec", str(e)[:120]); raise
    cand = (d.get("candidates") or [{}])[0]
    donnees = None
    for part in cand.get("content", {}).get("parts", []):
        ligne = part.get("inlineData") or part.get("inline_data")
        if ligne:
            donnees = base64.b64decode(ligne["data"])
    if not donnees:
        journal(ident, "echec", "sans image"); raise RuntimeError(cand.get("finishReason"))
    DEST.mkdir(parents=True, exist_ok=True)
    cible, orig = DEST / f"{ident}.png", DEST / f"{ident}.orig.png"
    if cible.exists() and not orig.exists():
        cible.rename(orig)
    Image.open(io.BytesIO(donnees)).convert("RGB").save(cible)
    # Le comptoir se sert plus large : c'est un décor plein écran.
    servir(ident, 1600 if ident == "comptoir" else 800)
    journal(ident, "ok", ratio)
    print(f"  {ident:14} {len(donnees)/1024:5.0f} ko  {time.time()-t0:4.1f} s", flush=True)


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    args = sys.argv[1:]
    cibles = [a for a in args if not a.startswith("--")]
    if "--temoins" in args:
        cibles = SUJ.TEMOINS + ["comptoir"]
    if "--tous" in args:
        # Ce qui est déjà sur le disque ne se repaie pas.
        cibles = [e[0] for e in LEX.LEXIQUE if e[5] == "croquis" and not (DEST / f"{e[0]}.png").exists()]
    if "--comptoir" in args:
        cibles = ["comptoir"]
    for c in cibles:
        consigne(c)
    if "--essai" in args:
        for c in cibles or SUJ.TEMOINS + ["comptoir"]:
            print(f"  {c:14} {len(consigne(c)):5} car.")
        sys.exit(0)
    with ThreadPoolExecutor(4) as pool:
        list(pool.map(generer, cibles))
