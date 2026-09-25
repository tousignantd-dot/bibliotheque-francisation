#!/usr/bin/env python3
"""Les vignettes des étapes du Camino francés — une par lieu, en 3:2.

Demande de Daniel, 25 septembre 2026 : « quelque chose d'un peu ludique »,
les étapes du chemin de Saint-Jean-Pied-de-Port à Santiago, en images.
Elles illustrent le plan, puis la credencial du jeu de rôle (un tampon par
étape réussie).

Même famille de trait que les croquis de Francœur et de l'hôtel (encre noire,
aplat discret), mais un PAYSAGE de carnet de voyage : le lieu se reconnaît à
sa silhouette, jamais à un panneau. D'où le « no text » nommé objet par objet
(borne, enseigne, panneau), défaut connu de la série de l'hôtel.

    python3 build/compostelle_croquis.py --essai     # consignes et coût, sans appel
    python3 build/compostelle_croquis.py             # tout ce qui manque sur le disque
    python3 build/compostelle_croquis.py meseta      # ces vignettes-là (refaites)
"""
import base64, io, json, pathlib, sys, time, urllib.request
from PIL import Image

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import francoeur_croquis as FC  # noqa: E402  (clé, blanchiment)

DEST = RACINE / "assets" / "interactive" / "compostelle" / "etapes"
GEN = pathlib.Path.home() / "Claude" / "generations"
MODELE = FC.MODELE

REGISTRE = (
    "A travel-sketchbook landscape vignette in ink and light wash: crisp black ink line of "
    "even weight, a few flat, soft, slightly muted colour fills (warm ochre, sage green, sky "
    "blue, terracotta), no gradient, no photographic rendering, no heavy shading. Wide 3:2 "
    "landscape frame; the scene fades softly into a pure white background at its edges, like "
    "a drawing on paper. A flat scan of the drawing itself, NOT a photograph of a sketchbook: "
    "no page edge, no binding, no paper shadow, no grey around it.\n"
    "NO TEXT ANYWHERE: no letters, no numbers, no words on signs, milestones, shop fronts or "
    "banners, no signature, no caption, no logo. No frame, no border, no box around the "
    "drawing.\n\n"
    "THE PLACE: "
)

SUJETS = {
    "sjpp": "Saint-Jean-Pied-de-Port, in the French Basque Country: a narrow cobbled street "
            "running down to an old stone arched gate and a small stone bridge over a river, "
            "tall white houses with red wooden shutters and balconies, green Pyrenean hills behind.",
    "roncesvalles": "The crossing of the Pyrenees towards Roncesvalles: a wide grassy mountain "
            "pass under drifting mist, a dirt path climbing across it, two small hikers with "
            "backpacks and walking sticks seen from behind, a few horses grazing.",
    "puente-la-reina": "The medieval Romanesque stone footbridge of Puente la Reina: six "
            "rounded arches with a humped deck over a calm river, reflected in the water, "
            "poplar trees on the banks.",
    "rioja": "The vineyards of La Rioja near Logroño: rows of low vines on gentle red-earth "
            "slopes, a dirt path between them, bunches of dark grapes in the foreground.",
    "burgos": "The Gothic cathedral of Burgos seen from a small square: two tall openwork "
            "spires, pointed arches, pale stone, a few tiny figures in the square.",
    "meseta": "The Meseta of Castile: endless flat golden wheat fields under a huge sky, a "
            "straight dirt track to the horizon, a single hiker with a backpack far away, and in "
            "the foreground a plain stone waymarker post with a painted yellow arrow and a "
            "scallop shell shape (no numbers on it).",
    "cruz-de-ferro": "The Cruz de Ferro in the mountains of León: a small iron cross on top "
            "of a tall wooden pole, standing on a large mound of pebbles and stones left by "
            "pilgrims, heather and hills around, early morning light.",
    "o-cebreiro": "O Cebreiro in Galicia: a round stone house with a conical thatched roof "
            "(a palloza) beside a small stone church, green mountains in soft fog behind.",
    "santiago": "The Obradoiro facade of the cathedral of Santiago de Compostela: a grand "
            "baroque front with two tall ornate towers and a double staircase, a wide stone "
            "square in front with a few tiny figures of arriving pilgrims, one raising arms.",
}
ORDRE = list(SUJETS)


def journal(ident, statut, note):
    sys.path.insert(0, str(GEN))
    try:
        from journal_appels import enregistrer_appel
        enregistrer_appel("google", MODELE, module="compostelle",
                          cible=f"vignette {ident}", statut=statut,
                          estimation=0.067 if statut == "ok" else 0, note=note)
    except Exception as e:
        print("  (registre : %s)" % e)


def servir(ident):
    im = FC.blanchir(Image.open(DEST / f"{ident}.png").convert("RGB"))
    im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS).save(
        DEST / f"{ident}.jpg", "JPEG", quality=82)


def generer(ident):
    corps = {"contents": [{"parts": [{"text": REGISTRE + SUJETS[ident]}]}],
             "generationConfig": {"responseModalities": ["IMAGE"],
                                  "imageConfig": {"aspectRatio": "3:2"}}}
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           f"{MODELE}:generateContent?key=" + FC.cle("GOOGLE_API_KEY"))
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
        raison = cand.get("finishReason") or d.get("promptFeedback", {}).get("blockReason")
        journal(ident, "echec", f"sans image : {raison}")
        raise RuntimeError(f"sans image : {raison}")
    DEST.mkdir(parents=True, exist_ok=True)
    cible, orig = DEST / f"{ident}.png", DEST / f"{ident}.orig.png"
    if cible.exists() and not orig.exists():
        cible.rename(orig)
    Image.open(io.BytesIO(donnees)).convert("RGB").save(cible)
    servir(ident)
    journal(ident, "ok", "3:2")
    print(f"  {ident:16} {time.time()-t0:4.1f} s", flush=True)


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    args = sys.argv[1:]
    cibles = [a for a in args if not a.startswith("--")] or \
             [i for i in ORDRE if not (DEST / f"{i}.png").exists()]
    for c in cibles:
        if c not in SUJETS:
            raise SystemExit(f"{c} : aucun sujet")
    if "--essai" in args:
        for c in cibles:
            print(f"  {c:16} {len(REGISTRE + SUJETS[c]):5} car.")
        print(f"{len(cibles)} vignettes, ≈ {len(cibles) * 0.067:.2f} $"); sys.exit(0)
    echecs = []
    def un(c):
        try:
            generer(c)
        except Exception as e:
            echecs.append(c); print(f"  {c} : {e}")
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(un, cibles))
    print(f"{len(cibles) - len(echecs)} faites, échecs : {echecs}")
