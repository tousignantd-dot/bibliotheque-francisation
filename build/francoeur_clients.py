#!/usr/bin/env python3
"""Les portraits des huit clients du magasin — quatre humeurs chacun.

    python3 build/francoeur_clients.py --neutres     # les huit visages neutres (8 appels)
    python3 build/francoeur_clients.py --humeurs     # les trois autres humeurs, par client (24)
    python3 build/francoeur_clients.py presse        # un client : ce qui manque
    python3 build/francoeur_clients.py --essai       # longueurs, sans appel

L'ORDRE EST LA MÉTHODE (compétence croquis-sequence) : on engendre d'abord le
visage NEUTRE, en texte seul ; on le regarde ; puis chaque humeur se fait en
RETOUCHE du neutre, passé en référence, avec la consigne d'invariance — même
personne, même cadre, seule l'expression change. Engendrer les quatre en texte
seul donnerait quatre personnes différentes.

LE REGISTRE est celui des croquis du magasin : trait noir net, aplats doux,
fond blanc. Portrait en buste, de face, comme le vendeur voit le client : c'est
le client qui se montre, jamais le vendeur.

Sortie : assets/interactive/francoeur/clients/<id>-<humeur>.png (+ .jpg servi).
Les .png restent hors git, comme les croquis.
"""
import base64, io, json, pathlib, sys, time, urllib.request

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build" / "contenu" / "entreprise-francoeur"))
sys.path.insert(0, str(RACINE / "build"))
from clients import CLIENTS, HUMEURS  # noqa: E402
from francoeur_croquis import cle, blanchir, MODELE, GEN  # noqa: E402
from PIL import Image  # noqa: E402

DEST = RACINE / "assets" / "interactive" / "francoeur" / "clients"

PORTRAIT = (
    "A clean flat illustration portrait in the style of a fashion flat sketch: crisp black ink "
    "outline of even weight, soft flat colour fills, no shading, no gradient, no photograph, no "
    "3D rendering. Head and shoulders of ONE customer in a clothing store, facing the viewer "
    "straight on, as a salesperson standing in front of them would see them, centred, the head "
    "filling about 45 % of a square frame, on a pure white background. No hands visible. No "
    "text, no letters, no logo, no brand name, no sign, no frame, no border.\n\n"
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
    "framing, crop and scale, the same pose of the head and shoulders, the same line and colour "
    "technique, the same white background. Do not zoom, do not recompose, do not add hands.\n"
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
        enregistrer_appel("google", MODELE, module="entreprise-francoeur", cible=f"client {ident}",
                          statut="echec", estimation=0, note=str(e)[:120])
        raise
    cand = (d.get("candidates") or [{}])[0]
    for part in cand.get("content", {}).get("parts", []):
        ligne = part.get("inlineData") or part.get("inline_data")
        if ligne:
            enregistrer_appel("google", MODELE, module="entreprise-francoeur",
                              cible=f"client {ident}", statut="ok", estimation=0.067, note=note)
            return base64.b64decode(ligne["data"])
    raison = cand.get("finishReason") or d.get("promptFeedback", {}).get("blockReason")
    enregistrer_appel("google", MODELE, module="entreprise-francoeur", cible=f"client {ident}",
                      statut="echec", estimation=0, note=f"refus : {raison}")
    raise RuntimeError(f"refus : {raison}")


def poser(ident, humeur, donnees):
    DEST.mkdir(parents=True, exist_ok=True)
    cible = DEST / f"{ident}-{humeur}.png"
    orig = DEST / f"{ident}-{humeur}.orig.png"
    if cible.exists() and not orig.exists():
        cible.rename(orig)
    im = Image.open(io.BytesIO(donnees)).convert("RGB")
    im.save(cible)
    blanchir(im).resize((640, 640), Image.LANCZOS).save(DEST / f"{ident}-{humeur}.jpg", "JPEG", quality=82)


def neutre(c):
    ident, _nom, _v, _p, _carte, portrait, _f = c
    t0 = time.time()
    poser(ident, "neutre", appeler([{"text": PORTRAIT + portrait + ". Expression: " + EXPRESSION["neutre"]}],
                                   ident, "neutre, texte seul"))
    print(f"  {ident:11} neutre    {time.time()-t0:4.1f} s", flush=True)


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
    print(f"  {ident:11} {h:10} {time.time()-t0:4.1f} s", flush=True)


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    args = sys.argv[1:]
    noms = [a for a in args if not a.startswith("--")]
    choisis = [c for c in CLIENTS if not noms or c[0] in noms]
    if "--essai" in args:
        for c in choisis:
            print(f"  {c[0]:11} {len(PORTRAIT + c[5]):5} car.")
        sys.exit(0)
    taches = []
    if "--neutres" in args or noms:
        taches += [(neutre, (c,)) for c in choisis if not (DEST / f"{c[0]}-neutre.png").exists()]
    if "--humeurs" in args or noms:
        pass
    with ThreadPoolExecutor(4) as pool:
        list(pool.map(lambda t: t[0](*t[1]), taches))
    if "--humeurs" in args or noms:
        taches = [(c, h) for c in choisis for h in HUMEURS[1:]
                  if not (DEST / f"{c[0]}-{h}.png").exists()]
        with ThreadPoolExecutor(4) as pool:
            list(pool.map(lambda t: humeur(*t), taches))
    print("fait")
