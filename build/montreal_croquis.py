#!/usr/bin/env python3
"""Les vignettes du guide de Montréal — une par lieu, en 3:2.

Demande de Daniel, 29 septembre 2026 : un guide touristique de Montréal en
trois langues, « avec des images créées à l'image de celles de Compostelle ».
Même registre que build/compostelle_croquis.py (carnet de voyage, encre et
lavis, fond blanc, AUCUN texte) ; les enseignes célèbres (Schwartz's, la
grosse orange) se reconnaissent à leur forme, jamais à leurs lettres.

    python3 build/montreal_croquis.py --essai     # consignes et coût, sans appel
    python3 build/montreal_croquis.py             # tout ce qui manque sur le disque
    python3 build/montreal_croquis.py schwartz    # ces images-là (refaites)
"""
import pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import compostelle_croquis as CC  # noqa: E402  (REGISTRE, generer, servir)

BASE = RACINE / "assets" / "interactive" / "montreal" / "lieux"

SUJETS = {
    "accueil": "Montreal seen from the lookout on Mount Royal in late summer: the city's downtown towers below, "
        "the wide Saint Lawrence River beyond with a long steel truss bridge, green treetops of the mountain "
        "in the foreground with a stone balustrade, a few tiny figures leaning on it.",
    "vieux-port": "The Old Port of Montreal: a wide waterfront promenade along the river, a big observation "
        "Ferris wheel, a slender white stone clock tower at the end of a pier, sailboats and a small ferry, "
        "people strolling and cycling.",
    "notre-dame": "The Notre-Dame Basilica of Montreal seen from Place d'Armes: a Gothic Revival grey stone "
        "facade with two tall square towers and three arched portals, a horse-drawn calèche in the square "
        "and a bronze statue on a pedestal in the foreground.",
    "place-jacques-cartier": "Place Jacques-Cartier in Old Montreal: a sloping cobbled square lined with old "
        "grey stone houses with café terraces and flower baskets, a tall slender stone column with a small "
        "statue on top at the upper end, street performers and strollers.",
    "pointe-a-calliere": "The Pointe-à-Callière museum in Old Montreal: a modern pale stone building with a "
        "tall thin lookout tower shaped like a ship's prow, on a small triangular square, old stone warehouses "
        "and the river port nearby.",
    "mont-royal": "The Mount Royal chalet and Kondiaronk lookout: a large stone chalet with a wide terrace, "
        "autumn maples, people sitting on the stone wall, and on a wooded summit nearby a tall steel lattice "
        "cross.",
    "oratoire": "Saint Joseph's Oratory on the slope of Mount Royal: a huge domed basilica with a green copper "
        "dome, reached by long flights of wide stone stairs with pilgrims climbing, trees on both sides.",
    "parc-olympique": "Montreal's Olympic Stadium: a sweeping white concrete oval stadium with a tall, strongly "
        "inclined tower leaning over it like a swan's neck, a wide empty esplanade in front with a few figures.",
    "jardin-botanique": "The Chinese Garden of the Montreal Botanical Garden: a pavilion with curved tiled roofs "
        "beside a calm pond, a zigzag bridge, rocks and weeping willows, glowing red silk lanterns at dusk.",
    "habitat-67": "Habitat 67 seen from across the water: a hill-like stack of dozens of pale concrete box "
        "houses piled irregularly with terraces and gaps between them, on a narrow peninsula in the river, "
        "the city skyline far behind.",
    "biosphere": "The Biosphere on Île Sainte-Hélène: a huge transparent geodesic sphere made of a steel "
        "lattice of triangles, among green trees and lawns, a small path with cyclists in front.",
    "mbam": "The Montreal Museum of Fine Arts on Sherbrooke Street: a neoclassical white marble building with "
        "tall columns and wide steps, and across the street a modern glass-fronted pavilion, pedestrians and "
        "old grey stone mansions.",
    "quartier-spectacles": "The Quartier des spectacles on a summer festival night: a wide pedestrian square "
        "full of people facing an outdoor stage, fountains of water jets in the paving, coloured light "
        "projections on the facade of a modern building, strings of lights.",
    "canal-lachine": "The Lachine Canal in summer: a calm straight canal with an old stone lock, a cycling "
        "path along the bank with cyclists on sturdy shared bikes, old red brick factory buildings converted "
        "into lofts, a small tower of an Art Deco market in the distance.",
    "plateau": "A residential street of the Plateau Mont-Royal: rows of two-storey brick row houses with "
        "curved outdoor wrought-iron staircases painted in bright colours, small balconies with flowers, "
        "maple trees, a cyclist passing.",
    "mile-end": "A street corner in Mile End: a huge colourful mural painted on the side of a brick building "
        "(abstract shapes and a large face, no letters), small shops and a café, a man in a long black coat "
        "and a young woman with a bicycle on the sidewalk.",
    "quartier-chinois": "Montreal's Chinatown: an ornate Chinese gate (paifang) with green tiled roofs and red "
        "pillars spanning a pedestrian street, red lanterns hanging above, small restaurants and grocery "
        "stalls with fruit.",
    "marche-jean-talon": "The Jean-Talon Market in autumn: long open-air aisles of farmers' stalls under a "
        "canopy, crates of apples, pumpkins, corn, tomatoes and flowers, shoppers with baskets.",
    "marche-atwater": "The Atwater Market: a long red brick market hall with a tall slender Art Deco clock "
        "tower, beside a canal, flower and plant stalls in front under awnings.",
    "romados": "A Portuguese rotisserie counter: a glass counter full of golden grilled chickens and small "
        "custard tarts, a cook brushing chickens on a charcoal grill behind, blue and white tiles on the wall.",
    "schwartz": "A classic Montreal smoked meat deli: a narrow old-fashioned storefront with a long front "
        "window and a plain awning, a line of people waiting on the sidewalk, and in the foreground a thick "
        "smoked meat sandwich on rye bread with mustard, a pickle beside it.",
    "bagels": "A Montreal bagel bakery: a baker sliding a long wooden plank loaded with rows of sesame bagels "
        "into a glowing wood-fired brick oven, a pile of fresh bagels in a wooden bin in front, paper bags.",
    "la-banquise": "A plate of poutine: thick golden french fries topped with squeaky cheese curds and glossy "
        "brown gravy in a paper-lined dish, a fork stuck in it, a lively little diner counter behind at night.",
    "wilenskys": "An old-fashioned lunch counter from the 1930s: a worn wooden counter with round swivel "
        "stools, a vintage soda fountain and grill, and in front a small pressed grilled bologna-and-salami "
        "sandwich on a roll, uncut, with a bottle of mustard.",
    "orange-julep": "The Orange Julep: a giant bright orange sphere-shaped building, three storeys tall, "
        "beside a roadside parking lot, a few classic cars parked, people holding tall frothy orange drinks.",
    "cafe-olimpico": "An Italian café in Mile End: a busy sidewalk terrace with small bistro tables, people "
        "chatting over espresso cups, inside a gleaming chrome espresso machine, Italian flags as bunting "
        "(without text).",
    "cafe-italia": "A small old-school Italian espresso bar: a narrow room with a long counter, a chrome "
        "espresso machine, an old television on the wall showing a football match, men standing at the bar "
        "with tiny cups.",
    "santropol": "A hidden café garden: a lush green courtyard behind an old house, wooden tables under "
        "climbing plants and a tree, a thick layered sandwich and a teapot on a table, a stone wall with ivy.",
    "dieu-du-ciel": "A cosy Montreal microbrewery pub: a wooden bar with a row of beer taps, glasses of "
        "beers of different colours from pale gold to black, a chalkboard showing only simple drawings of "
        "hops (no words), friends at a table.",
    # Les scènes « Parler » qui ne tiennent à aucun lieu du guide (30 sept. 2026).
    "metro": "A Montreal metro station: a ticket booth window with an attendant inside, turnstiles, a "
        "distinctive rounded blue-and-white metro train arriving at the platform behind, a traveller with "
        "a small backpack at the booth, plain signs shown only as blank coloured shapes.",
    "depanneur": "A small Montreal corner store (dépanneur) interior: a narrow counter with a cash register, "
        "a clerk behind it, shelves of snacks, a glass fridge of drinks and a small rack of wine bottles, a "
        "customer putting a bottle of water on the counter.",
    "pharmacie": "A neighbourhood pharmacy counter: a pharmacist in a white coat behind the counter handing a "
        "small box to a customer, shelves of plain boxes and bottles behind, a small bell on the counter.",
}
ORDRE = list(SUJETS)


def journal(ident, statut, note):
    sys.path.insert(0, str(CC.GEN))
    try:
        from journal_appels import enregistrer_appel
        enregistrer_appel("google", CC.MODELE, module="montreal",
                          cible=f"image {ident}", statut=statut,
                          estimation=0.067 if statut == "ok" else 0, note=note)
    except Exception as e:
        print("  (registre : %s)" % e)


CC.journal = journal  # generer() appelle journal() du module : inscrire sous « montreal »


# Les mascottes candidates de la version enfants (proposition du 30 sept. 2026).
MASCOTTE = (
    "A friendly children's-book character drawn in the same travel-sketchbook style: crisp black ink line of "
    "even weight, a few flat, soft, slightly muted colour fills, no gradient, no heavy shading. Full body, "
    "standing, three-quarter view, centred on a PURE WHITE background with nothing else around it: no ground "
    "shadow, no scenery, no frame, no border. Warm, curious and kind expression, big round eyes, NOT scary, NOT "
    "cartoonish-plastic. NO TEXT ANYWHERE: no letters, no logo, no badge with writing.\n\nTHE CHARACTER: ")
MASCOTTES = {
    "raton": "A young raccoon from Mount Royal park, standing upright, wearing a small canvas explorer satchel "
        "across the body and holding a folded paper map, one paw raised as if saying hello.",
    "ecureuil": "A small black squirrel (the black-furred squirrels common in Montreal parks), standing upright, "
        "bushy tail curled high, wearing a tiny red scarf and a small canvas explorer satchel, holding a magnifying glass.",
    "castor": "A young beaver standing upright, wearing a small red tuque and a canvas explorer satchel, holding a "
        "little compass in one paw, flat tail visible behind.",
}


# Filou, la mascotte retenue (30 sept. 2026) : ses poses se dessinent en
# RETOUCHE du croquis « filou » (le raton, une seule sacoche) passé en
# référence — texte seul, le modèle redessinerait un autre raton à chaque fois.
POSE = ("Redraw EXACTLY this same raccoon character — same face, same markings, same proportions, same colours, "
        "same ink-and-wash style, same single canvas satchel worn across the body — in a new pose. Pure white "
        "background, full body, no ground shadow, no scenery, no frame, no text.\n\nTHE NEW POSE: ")
POSES = {
    "salut": "standing, waving hello with one paw raised high, big friendly smile.",
    "raconte": "standing, telling a story: one paw open and pointing to the side as if showing something, mouth open, lively.",
    "loupe": "leaning forward curiously, looking through a magnifying glass held in one paw, one eyebrow raised, thinking.",
    "surprise": "jumping slightly with surprise and delight, both paws on the cheeks, eyes wide and happy.",
    "bravo": "jumping for joy with both arms raised in victory, eyes closed with a huge happy grin.",
}


def cibles_connues():
    t = {("vignette", k): (CC.REGISTRE + quoi, "3:2", BASE, 1200) for k, quoi in SUJETS.items()}
    for k, quoi in MASCOTTES.items():
        t[("mascotte", k)] = (MASCOTTE + quoi, "1:1", BASE.parent / "mascottes", 700)
    t[("mascotte", "filou")] = (MASCOTTE + MASCOTTES["raton"].replace(
        "wearing a small canvas explorer satchel", "wearing ONE single small canvas explorer satchel (only one bag, "
        "on one hip, strap across the chest)"), "1:1", BASE.parent / "mascottes", 700)
    for k, quoi in POSES.items():
        t[("pose", k)] = (POSE + quoi, "1:1", BASE.parent / "filou", 600)
    return t


def generer_pose(cible, t):
    """Une pose de Filou : la même requête que CC.generer, avec le croquis de référence."""
    import base64, io, json, urllib.request
    from PIL import Image
    genre, ident = cible
    consigne, cadre, dossier, largeur = t[cible]
    ref = base64.b64encode((BASE.parent / "mascottes" / "filou.jpg").read_bytes()).decode()
    corps = {"contents": [{"parts": [{"inline_data": {"mime_type": "image/jpeg", "data": ref}}, {"text": consigne}]}],
             "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": cadre}}}
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           f"{CC.MODELE}:generateContent?key=" + CC.FC.cle("GOOGLE_API_KEY"))
    req = urllib.request.Request(url, data=json.dumps(corps).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.loads(r.read())
    parts = (d.get("candidates") or [{}])[0].get("content", {}).get("parts", [])
    donnees = next((base64.b64decode((p.get("inlineData") or p.get("inline_data"))["data"])
                    for p in parts if p.get("inlineData") or p.get("inline_data")), None)
    if not donnees:
        journal(ident, "echec", "sans image"); raise RuntimeError("sans image")
    dossier.mkdir(parents=True, exist_ok=True)
    Image.open(io.BytesIO(donnees)).convert("RGB").save(dossier / f"{ident}.png")
    CC.servir(dossier, ident, largeur)
    journal(ident, "ok", f"pose {cadre}")
    print(f"  pose     {ident}", flush=True)


def detourer(dossier=None, largeur=420):
    """Filou sur fond transparent (<pose>-d.webp), pour les fonds de couleur du
    mode famille. Le blanc est retiré par REMPLISSAGE depuis les bords : un
    seuil global mangerait aussi le blanc du museau et du ventre."""
    from PIL import Image, ImageDraw
    dossier = dossier or BASE.parent / "filou"
    for src in sorted(dossier.glob("*.png")):
        if src.stem.endswith("-d") or src.stem.endswith(".orig"):
            continue
        im = Image.open(src).convert("RGBA")
        w, h = im.size
        for xy in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2)):
            if im.getpixel(xy)[3] and min(im.getpixel(xy)[:3]) > 225:
                ImageDraw.floodfill(im, xy, (255, 255, 255, 0), thresh=40)
        im = im.crop(im.getbbox())
        im.thumbnail((largeur, largeur), Image.LANCZOS)
        im.save(dossier / f"{src.stem}-d.webp", quality=86, method=6)
        print("  détouré", src.stem)


if __name__ == "__main__":
    if "--detourer" in sys.argv:
        detourer(); sys.exit(0)
    from concurrent.futures import ThreadPoolExecutor
    args = sys.argv[1:]
    t = cibles_connues()
    noms = [a for a in args if not a.startswith("--")]
    cibles = ([c for c in t if c[1] in noms] if noms
              else [c for c in t if not (t[c][2] / f"{c[1]}.png").exists()])
    if "--essai" in args:
        for c in cibles:
            print(f"  {c[1]:22} {len(t[c][0]):5} car.")
        print(f"{len(cibles)} images, ≈ {len(cibles) * 0.067:.2f} $"); sys.exit(0)
    echecs = []
    def un(c):
        try:
            (generer_pose if c[0] == "pose" else CC.generer)(c, t)
        except Exception as e:
            echecs.append(c); print(f"  {c} : {e}")
    with ThreadPoolExecutor(5) as ex:
        list(ex.map(un, cibles))
    print(f"{len(cibles) - len(echecs)} faites, échecs : {echecs}")
