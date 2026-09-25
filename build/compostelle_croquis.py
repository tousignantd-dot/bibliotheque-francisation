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
    python3 build/compostelle_croquis.py meseta      # ces images-là (refaites)
    python3 build/compostelle_croquis.py mot:vaso portrait:marta

Depuis la construction de la trousse (25 sept. au soir), le même script
dessine aussi les 82 croquis du lexique (1:1, préambule OBJET de Francœur ou
CORPS/SCENE de sujets.py) et les portraits des gens du chemin.
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
    "pamplona": "The old town of Pamplona: a wide square lined with tall houses with glazed balconies "
            "and a café terrace under arcades, the old city walls and a stone gate in the background.",
    "leon": "The Gothic cathedral of León seen from its square: tall pointed facade with a large rose "
            "window, two towers, and inside the open portal a glimpse of bright blue and red stained glass.",
    "sarria": "A Galician country path near Sarria: a sunken lane between old mossy stone walls and big oak "
            "trees, green fields, a plain concrete waymarker post with a blue tile and a yellow scallop "
            "shell and NO numbers, two small pilgrims with backpacks walking ahead.",
    "santiago": "The Obradoiro facade of the cathedral of Santiago de Compostela: a grand "
            "baroque front with two tall ornate towers and a double staircase, a wide stone "
            "square in front with a few tiny figures of arriving pilgrims, one raising arms.",
}
ORDRE = list(SUJETS)

# Les croquis du lexique et les portraits des personnages : même appel, autre
# cadre (carré) et autre dossier. Les sujets vivent dans le CONTENU.
# Chargés sous un nom à eux : `sujets` et `lexique` existent aussi chez
# Francœur, que francoeur_croquis a déjà mis dans sys.modules — un import
# ordinaire rendait LEURS modules, en silence.
def _charger(nom):
    import importlib.util
    sp = importlib.util.spec_from_file_location(
        f"compostelle_{nom}", RACINE / "build" / "contenu" / "compostelle" / f"{nom}.py")
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m


SJ, PS = _charger("sujets"), _charger("personnages")
LEXIQUE = _charger("lexique").LEXIQUE
BASE = RACINE / "assets" / "interactive" / "compostelle"



def cibles_connues():
    """Toutes les images de la trousse : (genre, id) → (consigne, cadre, dossier, largeur servie)."""
    t = {}
    for k, quoi in SUJETS.items():
        t[("vignette", k)] = (REGISTRE + quoi, "3:2", BASE / "etapes", 1200)
    pre = {"objet": FC.PREAMBULES["objet"], "corps": SJ.CORPS, "scene": SJ.SCENE}
    for e in LEXIQUE:
        if e[4] == "croquis":
            if e[0] not in SJ.SUJETS:
                raise SystemExit(f"{e[0]} : croquis sans sujet dans sujets.py")
            fam, quoi = SJ.SUJETS[e[0]]
            t[("mot", e[0])] = (pre[fam] + quoi, "1:1", BASE / "croquis", 800)
    for k, quoi in PS.PORTRAITS.items():
        t[("portrait", k)] = (SJ.PORTRAIT + quoi, "1:1", BASE / "portraits", 600)
    return t


def journal(ident, statut, note):
    sys.path.insert(0, str(GEN))
    try:
        from journal_appels import enregistrer_appel
        enregistrer_appel("google", MODELE, module="compostelle",
                          cible=f"image {ident}", statut=statut,
                          estimation=0.067 if statut == "ok" else 0, note=note)
    except Exception as e:
        print("  (registre : %s)" % e)


def servir(dossier, ident, largeur):
    im = FC.blanchir(Image.open(dossier / f"{ident}.png").convert("RGB"))
    im.resize((largeur, round(im.height * largeur / im.width)), Image.LANCZOS).save(
        dossier / f"{ident}.jpg", "JPEG", quality=82)


def generer(cible, t):
    genre, ident = cible
    consigne, cadre, dossier, largeur = t[cible]
    corps = {"contents": [{"parts": [{"text": consigne}]}],
             "generationConfig": {"responseModalities": ["IMAGE"],
                                  "imageConfig": {"aspectRatio": cadre}}}
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
    dossier.mkdir(parents=True, exist_ok=True)
    png, orig = dossier / f"{ident}.png", dossier / f"{ident}.orig.png"
    if png.exists() and not orig.exists():
        png.rename(orig)
    Image.open(io.BytesIO(donnees)).convert("RGB").save(png)
    servir(dossier, ident, largeur)
    journal(ident, "ok", f"{genre} {cadre}")
    print(f"  {genre:8} {ident:16} {time.time()-t0:4.1f} s", flush=True)


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    args = sys.argv[1:]
    t = cibles_connues()
    noms = [a for a in args if not a.startswith("--")]
    if noms:
        cibles = [c for c in t if c[1] in noms or f"{c[0]}:{c[1]}" in noms]
        manque = set(noms) - {c[1] for c in cibles} - {f"{c[0]}:{c[1]}" for c in cibles}
        if manque:
            raise SystemExit(f"inconnus : {sorted(manque)}")
    else:
        cibles = [c for c in t if not (t[c][2] / f"{c[1]}.png").exists()]
    if "--essai" in args:
        from collections import Counter
        for c in cibles:
            print(f"  {c[0]:8} {c[1]:16} {len(t[c][0]):5} car.")
        print(dict(Counter(c[0] for c in cibles)))
        print(f"{len(cibles)} images, ≈ {len(cibles) * 0.067:.2f} $"); sys.exit(0)
    echecs = []
    def un(c):
        try:
            generer(c, t)
        except Exception as e:
            echecs.append(c); print(f"  {c} : {e}")
    with ThreadPoolExecutor(5) as ex:
        list(ex.map(un, cibles))
    print(f"{len(cibles) - len(echecs)} faites, échecs : {echecs}")
