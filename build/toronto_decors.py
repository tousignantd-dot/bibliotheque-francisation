#!/usr/bin/env python3
"""Les images de la semaine d'« Une semaine à Toronto » — décors, cartes postales, portraits.

    python3 build/toronto_decors.py --essai            # ce qui manque, combien, sans appel
    python3 build/toronto_decors.py                    # tout ce qui manque sur le disque
    python3 build/toronto_decors.py decor:union carte:iles portrait:maya

Étape 3 (1er oct. 2026). Le contenu vit dans build/contenu/toronto/semaine.py.
- Décors : 3:2, servis à 1600 px, vus de la place du touriste ; la place de la
  personne reste VIDE (elle y est posée, détourée, à l'étape 5 — méthode
  croquis-sequence de l'hôtel : le décor ne bouge pas, les gens changent devant).
- Cartes postales : 3:2, servies à 1200 px, le recto de la carte gagnée.
- Portraits : le NEUTRE à partir du texte, PUIS chaque humeur en RETOUCHE du neutre
  avec la consigne d'invariance (recette de Francœur, 32 sur 32 du premier coup) ;
  coupés net à mi-poitrine sur fond blanc, pour le détourage.
Google en direct (gemini-3.1-flash-image), 0,067 $ l'image, registre des appels tenu.
"""
import base64, importlib.util, io, json, pathlib, sys, time, urllib.request

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import francoeur_croquis as FC  # noqa: E402  (clé, modèle, blanchiment)
from PIL import Image  # noqa: E402

sp = importlib.util.spec_from_file_location("toronto_semaine", RACINE / "build/contenu/toronto/semaine.py")
SE = importlib.util.module_from_spec(sp); sp.loader.exec_module(SE)
BASE = RACINE / "assets" / "interactive" / "toronto"
GEN = pathlib.Path.home() / "Claude" / "generations"

DECOR = (
    "A wide travel-sketchbook illustration in ink and light wash, full frame 3:2, seen at eye level from "
    "the place of a visitor standing in front of the scene: crisp black ink line of even weight, a few "
    "flat, soft, slightly muted colour fills, no gradient, no photographic rendering. The background is "
    "drawn edge to edge (no white margin, no vignette). IMPORTANT: the area where a person would stand "
    "behind the counter or in the middle of the scene is left EMPTY — nobody there. No people in the "
    "foreground. NO TEXT ANYWHERE: no signs, no letters, no numbers, no prices, no screens with text, no "
    "logo, no brand. No frame, no border.\n\nTHE SCENE: ")
CARTE = (
    "A picture-postcard illustration of a city landmark in ink and light wash, full frame 3:2: crisp black "
    "ink line of even weight, bright but soft flat colour fills, a sunny sky, drawn edge to edge like the "
    "front of a postcard. A flat scan of the drawing, not a photograph. NO TEXT ANYWHERE: no greeting, no "
    "city name, no letters, no signs, no logo. No frame, no border, no stamp.\n\nTHE VIEW: ")
PORTRAIT = (
    "A travel-sketchbook portrait in ink and light wash: ONE person seen from the front, head and upper "
    "body, CUT CLEANLY at mid-chest by the bottom edge of the frame, as a customer standing at a counter "
    "would see them; crisp black ink line of even weight, a few flat, soft, slightly muted colour fills; "
    "on a PURE WHITE background (nothing behind the person), centred, the head filling about 35 % of a "
    "square frame. No hands visible. No text, no letters, no logo, no badge text. No frame, no border.\n\n"
    "THE PERSON: ")
EXPRESSION = {
    "neutre": "a calm, neutral, attentive expression, mouth closed, looking at the viewer.",
    "contente": "a warm, friendly smile with the mouth slightly open, relaxed eyebrows, looking at the viewer — clearly pleased.",
    "hesitante": "a doubtful, unsure expression: eyebrows raised in the middle, mouth pulled to one side, head tilted slightly — clearly not sure they understood.",
    "impatiente": "an impatient expression: eyebrows lowered and drawn together, lips pressed tight, eyes looking slightly aside — clearly in a hurry.",
}
TENIR = (
    "\n\nABSOLUTE RULE — this is the SAME PERSON as in the reference image, drawn again for a sequence. "
    "Keep EVERYTHING identical: the same face, age, hair, skin tone, glasses and earrings if any, the same "
    "clothes and colours, the same framing, crop at mid-chest and scale, the same pose, the same line and "
    "colour technique, the same pure white background. Do not zoom, do not recompose, do not add hands.\n"
    "THE ONLY CHANGE is the facial expression, which becomes: ")


def cibles():
    t = {}
    for l in SE.LIEUX:
        t[("decor", l[0])] = (DECOR + l[7], "3:2", BASE / "decors", 1600)
        t[("carte", l[0])] = (CARTE + l[8], "3:2", BASE / "cartes", 1200)
    for g in SE.GENS:
        for h in SE.HUMEURS:
            t[("portrait", f"{g[0]}-{h}")] = (g[4], "1:1", BASE / "gens", 640)
    return t


def journal(cible, statut, note):
    sys.path.insert(0, str(GEN))
    try:
        from journal_appels import enregistrer_appel
        enregistrer_appel("google", FC.MODELE, module="toronto", cible=cible, statut=statut,
                          estimation=0.067 if statut == "ok" else 0, note=note)
    except Exception as e:
        print("  (registre : %s)" % e)


def appeler(parts, cadre, cible, note):
    corps = {"contents": [{"parts": parts}],
             "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": cadre}}}
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           f"{FC.MODELE}:generateContent?key=" + FC.cle("GOOGLE_API_KEY"))
    req = urllib.request.Request(url, data=json.dumps(corps).encode(), headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.loads(r.read())
    except Exception as e:
        journal(cible, "echec", str(e)[:120]); raise
    cand = (d.get("candidates") or [{}])[0]
    for part in cand.get("content", {}).get("parts", []):
        ligne = part.get("inlineData") or part.get("inline_data")
        if ligne:
            journal(cible, "ok", note)
            return base64.b64decode(ligne["data"])
    raison = cand.get("finishReason") or d.get("promptFeedback", {}).get("blockReason")
    journal(cible, "echec", f"refus : {raison}")
    raise RuntimeError(f"refus : {raison}")


def poser(dossier, ident, donnees, largeur, blanc):
    dossier.mkdir(parents=True, exist_ok=True)
    png, orig = dossier / f"{ident}.png", dossier / f"{ident}.orig.png"
    if png.exists() and not orig.exists():
        png.rename(orig)
    im = Image.open(io.BytesIO(donnees)).convert("RGB"); im.save(png)
    if blanc:
        im = FC.blanchir(im)
    im.resize((largeur, round(im.height * largeur / im.width)), Image.LANCZOS).save(dossier / f"{ident}.jpg", "JPEG", quality=82)


def faire(cible, t):
    genre, ident = cible
    texte, cadre, dossier, largeur = t[cible]
    t0 = time.time()
    if genre == "portrait":
        qui, h = ident.rsplit("-", 1)
        if h == "neutre":
            d = appeler([{"text": PORTRAIT + texte + ". Expression: " + EXPRESSION["neutre"]}], cadre, f"portrait {ident}", "neutre, texte seul")
        else:
            ref = dossier / f"{qui}-neutre.png"
            if not ref.exists():
                raise RuntimeError(f"{qui} : le neutre se fait d'abord")
            b = io.BytesIO(); Image.open(ref).convert("RGB").save(b, "JPEG", quality=92)
            d = appeler([{"inline_data": {"mime_type": "image/jpeg", "data": base64.b64encode(b.getvalue()).decode()}},
                         {"text": PORTRAIT.split("\n\nTHE PERSON")[0] + TENIR + EXPRESSION[h]}], cadre, f"portrait {ident}", f"{h}, retouche du neutre")
        poser(dossier, ident, d, largeur, True)
    else:
        d = appeler([{"text": texte}], cadre, f"{genre} {ident}", f"{genre} {cadre}")
        poser(dossier, ident, d, largeur, genre == "carte")
    print(f"  {genre:8} {ident:20} {time.time()-t0:4.1f} s", flush=True)


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    args = sys.argv[1:]
    t = cibles()
    noms = [a for a in args if not a.startswith("--")]
    if noms:
        cib = [c for c in t if f"{c[0]}:{c[1]}" in noms or (c[0] == "portrait" and f"portrait:{c[1].rsplit('-', 1)[0]}" in noms)]
    else:
        cib = [c for c in t if not (t[c][2] / f"{c[1]}.png").exists()]
    if "--essai" in args:
        from collections import Counter
        print(dict(Counter(c[0] for c in cib)), f"{len(cib)} images ≈ {len(cib) * 0.067:.2f} $"); sys.exit(0)
    # Les neutres d'abord : les humeurs en sont des retouches.
    neutres = [c for c in cib if c[0] != "portrait" or c[1].endswith("-neutre")]
    reste = [c for c in cib if c not in neutres]
    echecs = []
    def un(c):
        try:
            faire(c, t)
        except Exception as e:
            echecs.append(c); print(f"  {c} : {e}")
    for lot in (neutres, reste):
        with ThreadPoolExecutor(4) as ex:
            list(ex.map(un, lot))
    print(f"{len(cib) - len(echecs)} faites, échecs : {echecs}")
