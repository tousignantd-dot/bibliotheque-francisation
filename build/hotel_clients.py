#!/usr/bin/env python3
"""Les clients du comptoir de l'Hôtel Rive-Claire — quatre humeurs chacun.

    python3 build/hotel_clients.py --neutres     # les sept visages neutres (7 appels)
    python3 build/hotel_clients.py --humeurs     # les trois autres humeurs (21 appels)
    python3 build/hotel_clients.py --detourer    # refait les PNG servis, sans appel
    python3 build/hotel_clients.py plainte       # un client : ce qui manque

LA MÉTHODE est celle de Francœur (build/francoeur_clients.py, compétence
croquis-sequence) : le NEUTRE en texte seul, puis chaque humeur en RETOUCHE du
neutre, passé en référence, avec la consigne d'invariance.

CE QUI CHANGE : le client ne vit pas sur une carte blanche, il se tient DEVANT
LE COMPTOIR, sur le décor fixe de l'étape 1 (comptoir.jpg). Le décor ne bouge
pas ; seul le client change. Plutôt que de faire redessiner le décor à chaque
client (il dériverait d'un tirage à l'autre — « le cadre qui bouge »), on
dessine le client seul sur fond blanc, coupé net à mi-poitrine, puis on le
DÉTOURE : le blanc relié au bord devient transparent. L'écran le pose derrière
le rebord du comptoir.

Le client au téléphone n'a pas de visage : c'est voulu.

Sortie : assets/interactive/hotel/clients/<id>-<humeur>.png (source, hors git)
         et <id>-<humeur>.webp (servi, détouré, 720 px de haut).
"""
import base64, io, json, pathlib, sys, time, urllib.request

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
from francoeur_croquis import cle, MODELE, GEN  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402
import importlib.util  # noqa: E402

_s = importlib.util.spec_from_file_location("hotel_clients_contenu",
                                            RACINE / "build/contenu/entreprise-hotel/clients.py")
C = importlib.util.module_from_spec(_s); _s.loader.exec_module(C)
DEST = RACINE / "assets" / "interactive" / "hotel" / "clients"
AVEC_VISAGE = [c for c in C.CLIENTS if c[8]]

PORTRAIT = (
    "A clean flat illustration in the same style as a hotel reception line drawing: crisp black "
    "ink outline of even weight, soft flat colour fills, no shading, no gradient, no photograph, "
    "no 3D rendering. ONE hotel guest standing at a reception desk, seen from the front by the "
    "receptionist behind the desk: head, shoulders and upper chest, facing the viewer straight "
    "on, centred. The figure is cut perfectly straight and horizontal at mid-chest by the bottom "
    "edge of the frame. The head is in the upper half of the square frame, with white space "
    "above it. Pure white background, nothing behind the person: no desk, no wall, no furniture. "
    "No hands visible. No text, no letters, no logo, no name tag, no sign, no frame, no border.\n\n"
    "THE PERSON: ")

EXPRESSION = {
    "neutre": "a calm, neutral, attentive expression, mouth closed, looking at the viewer.",
    "contente": "a warm, satisfied smile with the mouth slightly open, relaxed eyebrows, "
                "looking at the viewer — clearly pleased.",
    "hesitante": "a doubtful, unsure expression: eyebrows raised in the middle, mouth pulled "
                 "to one side, head tilted slightly — clearly not sure they understood.",
    "impatiente": "an impatient, annoyed expression: eyebrows lowered and drawn together, lips "
                  "pressed tight, eyes looking slightly aside — clearly losing patience.",
}

TENIR = (
    "\n\nABSOLUTE RULE — this is the SAME PERSON as in the reference image, drawn again for a "
    "sequence. Keep EVERYTHING identical: the same face, the same age, the same hair, the same "
    "skin tone, the same glasses and earrings if any, the same clothes and colours, the same "
    "framing, crop and scale, the straight cut at mid-chest, the same pose of the head and "
    "shoulders, the same line and colour technique, the same pure white background. Do not "
    "zoom, do not recompose, do not add hands.\n"
    "THE ONLY CHANGE is the facial expression, which becomes: ")


def appeler(parts, ident, note):
    corps = {"contents": [{"parts": parts}],
             "generationConfig": {"responseModalities": ["IMAGE"],
                                  "imageConfig": {"aspectRatio": "1:1"}}}
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           f"{MODELE}:generateContent?key=" + cle("GOOGLE_API_KEY"))
    req = urllib.request.Request(url, data=json.dumps(corps).encode(),
                                 headers={"Content-Type": "application/json"})
    sys.path.insert(0, str(GEN))
    from journal_appels import enregistrer_appel
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.loads(r.read())
    except Exception as e:
        enregistrer_appel("google", MODELE, module="entreprise-hotel", cible=f"client {ident}",
                          statut="echec", estimation=0, note=str(e)[:120])
        raise
    cand = (d.get("candidates") or [{}])[0]
    for part in cand.get("content", {}).get("parts", []):
        ligne = part.get("inlineData") or part.get("inline_data")
        if ligne:
            enregistrer_appel("google", MODELE, module="entreprise-hotel",
                              cible=f"client {ident}", statut="ok", estimation=0.067, note=note)
            return base64.b64decode(ligne["data"])
    raison = cand.get("finishReason") or d.get("promptFeedback", {}).get("blockReason")
    enregistrer_appel("google", MODELE, module="entreprise-hotel", cible=f"client {ident}",
                      statut="echec", estimation=0, note=f"refus : {raison}")
    raise RuntimeError(f"refus : {raison}")


def detourer(src):
    """Le blanc RELIÉ AU BORD devient transparent ; le blanc intérieur (yeux,
    chemise) reste. Remplissage depuis les bords haut, gauche et droit — jamais
    le bas, où la coupe à mi-poitrine touche le cadre et doit rester opaque.

    Audit du comptoir joué, tour 1 (C2) : deux défauts corrigés ici.
    - Les POCHES de fond enfermées entre les cheveux et les épaules (Hoang)
      restaient blanches : une poche de blanc pur, loin du centre, est du fond.
    - Le trait horizontal du bas débordait du corps et le buste flottait : on
      efface, dans les 6 % du bas, tout ce qui sort de la largeur du corps.
    Puis on recadre au plus juste et on ramène à 720 px de haut."""
    import numpy as np
    im = Image.open(src).convert("RGB")
    w, h = im.size
    a = np.asarray(im).copy()
    a[(a >= 238).all(axis=2)] = 255
    im = Image.fromarray(a)
    trace = im.copy()
    FOND = (255, 0, 255)
    graines = [(x, 0) for x in range(0, w, 8)] + [(0, y) for y in range(0, h - 4, 8)] \
        + [(w - 1, y) for y in range(0, h - 4, 8)]
    for sx, sy in graines:
        if trace.getpixel((sx, sy)) == (255, 255, 255):
            ImageDraw.floodfill(trace, (sx, sy), FOND, thresh=0)
    # Les poches : blanc pur restant, dans le tiers extérieur de chaque côté.
    t = np.asarray(trace)
    blanc = (t == 255).all(axis=2)
    k = 0
    for x in list(range(0, int(w * 0.45), 4)) + list(range(int(w * 0.55), w, 4)):
        for y in range(0, int(h * 0.97), 4):
            if blanc[y, x]:
                k += 1
                couleur = (1, (k * 37) % 250 + 1, (k * 91) % 250 + 1)
                ImageDraw.floodfill(trace, (x, y), couleur, thresh=0)
                t = np.asarray(trace)
                zone = (t == couleur).all(axis=2)
                ys, xs = np.nonzero(zone)
                cx, cy = xs.mean() / w, ys.mean() / h
                # Loin du centre, ou sous le menton entre cheveux et épaules — jamais
                # à hauteur des yeux, dont le blanc est intérieur.
                exterieur = cx < 0.3 or cx > 0.7 or (cy > 0.5 and (cx < 0.42 or cx > 0.58))
                ImageDraw.floodfill(trace, (x, y), FOND if (exterieur and zone.sum() > 150) else (254, 254, 254), thresh=0)
                t = np.asarray(trace)
                blanc = (t == 255).all(axis=2)
    alpha = np.where((np.asarray(trace) == FOND).all(axis=2), 0, 255).astype("uint8")
    # Le bas : rien au-delà de la largeur du corps.
    ref = int(h * 0.92)
    xs = np.nonzero(alpha[ref])[0]
    if len(xs):
        g, d = max(0, xs.min() - 3), min(w, xs.max() + 4)
        alpha[int(h * 0.94):, :g] = 0
        alpha[int(h * 0.94):, d:] = 0
    rgba = Image.fromarray(np.dstack([a, alpha]).astype("uint8"))
    boite = Image.fromarray(alpha).getbbox()
    if boite:
        rgba = rgba.crop((boite[0], boite[1], boite[2], boite[3]))
    H = 720
    rgba = rgba.resize((round(rgba.width * H / rgba.height), H), Image.LANCZOS)
    rgba.save(src.with_suffix(".webp"), "WEBP", quality=86, method=6)


def poser(ident, humeur, donnees):
    DEST.mkdir(parents=True, exist_ok=True)
    cible = DEST / f"{ident}-{humeur}.png"
    orig = DEST / f"{ident}-{humeur}.orig.png"
    if cible.exists() and not orig.exists():
        cible.rename(orig)
    Image.open(io.BytesIO(donnees)).convert("RGB").save(cible)
    detourer(cible)


def neutre(c):
    ident, portrait = c[0], c[8]
    t0 = time.time()
    poser(ident, "neutre", appeler([{"text": PORTRAIT + portrait + ". Expression: " + EXPRESSION["neutre"]}],
                                   ident, "neutre, texte seul"))
    print(f"  {ident:14} neutre     {time.time()-t0:4.1f} s", flush=True)


def humeur(c, h):
    ident = c[0]
    ref = DEST / f"{ident}-neutre.png"
    if not ref.exists():
        raise SystemExit(f"{ident} : le neutre manque — il se fait d'abord")
    b = io.BytesIO(); Image.open(ref).convert("RGB").save(b, "JPEG", quality=92)
    t0 = time.time()
    poser(ident, h, appeler([{"inline_data": {"mime_type": "image/jpeg",
                                              "data": base64.b64encode(b.getvalue()).decode()}},
                             {"text": PORTRAIT.split("\n\nTHE PERSON")[0] + TENIR + EXPRESSION[h]}],
                            ident, f"{h}, retouche du neutre"))
    print(f"  {ident:14} {h:10} {time.time()-t0:4.1f} s", flush=True)


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    args = sys.argv[1:]
    noms = [a for a in args if not a.startswith("--")]
    choisis = [c for c in AVEC_VISAGE if not noms or c[0] in noms]
    if "--detourer" in args:
        for f in sorted(DEST.glob("*.png")):
            if not f.name.endswith(".orig.png"):
                detourer(f)
        print("détourés"); sys.exit(0)
    if "--neutres" in args or noms:
        with ThreadPoolExecutor(4) as pool:
            list(pool.map(neutre, [c for c in choisis if not (DEST / f"{c[0]}-neutre.png").exists()]))
    if "--humeurs" in args or noms:
        taches = [(c, h) for c in choisis for h in C.HUMEURS[1:] if not (DEST / f"{c[0]}-{h}.png").exists()]
        with ThreadPoolExecutor(4) as pool:
            list(pool.map(lambda t: humeur(*t), taches))
