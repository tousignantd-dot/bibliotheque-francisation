#!/usr/bin/env python3
"""Les croquis de la Maison Francœur — un vêtement par image, sur fond blanc.

LE REGISTRE (décision du 24 septembre 2026) : trait noir et aplat de couleur
discret. Les couleurs et les motifs sont du vocabulaire de vente — « rayé »,
« marine » — donc un trait seul ne peut pas les enseigner. La fiche imprimée
restera en noir et blanc et renverra la couleur à l'écran.

LA FORME DU DESSIN : le « dessin à plat » des catalogues de mode (fashion
flat) — le vêtement seul, de face, symétrique, sans corps ni mannequin. C'est
la convention du métier ; elle fixe d'avance la pose, le cadre et l'échelle,
donc la cohérence d'une planche à l'autre ne dépend pas de la chance.

UN CROQUIS PAR APPEL, JAMAIS UNE PLANCHE D'UN BLOC : la planche se COMPOSE
ensuite par script. Une planche engendrée d'un coup donne douze vêtements
qu'aucun exercice ne peut désigner un par un, et qu'on ne corrige qu'en
refaisant les onze autres.

CARRÉ 1:1 : un pantalon et une robe sont hauts, une ceinture est large. Sur
fond blanc, `object-fit: contain` dans une tuile 3:2 ne coupe rien.

    python3 build/francoeur_croquis.py --essai          # prompts, longueurs, sans appel
    python3 build/francoeur_croquis.py chandail parka   # ces entrées
    python3 build/francoeur_croquis.py --temoins        # les trois croquis d'essai
"""
import base64, io, json, pathlib, sys, time, urllib.request
from PIL import Image

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build" / "contenu" / "entreprise-francoeur"))
from lexique import LEXIQUE  # noqa: E402

DEST = RACINE / "assets" / "interactive" / "francoeur" / "croquis"
GEN = pathlib.Path.home() / "Claude" / "generations"
MODELE = "gemini-3.1-flash-image"

# Le préambule commun. Chaque membre de phrase répond à un défaut connu des
# séries précédentes : le texte qui s'écrit malgré l'interdiction (d'où
# « no label, no tag » nommés comme objets), l'ombre portée qui salit le fond,
# le mannequin qui revient si on ne l'exclut pas.
REGISTRE = (
    "A clean fashion flat sketch, the kind used in clothing catalogues and tech packs: the "
    "garment ALONE, seen straight from the front, perfectly symmetrical, laid flat, centred, "
    "filling about 70 % of a square frame, on a pure white background.\n"
    "LINE: crisp black ink outline of even weight, with thin inner lines for seams, stitching, "
    "folds and details. No sketchy strokes, no hatching, no pencil texture.\n"
    "COLOUR: one flat, soft, slightly muted fill of the colour named below, inside the outline "
    "only, with at most one lighter tone for the inside of a collar or a lining. No gradient, no "
    "shading, no shadow on the background, no 3D rendering, no photograph.\n"
    "NOTHING ELSE IN THE FRAME: no person, no body, no mannequin, no hanger, no hand, no "
    "background object. No text, no letters, no numbers, no logo, no brand name, no size label, "
    "no price tag, no clothing tag anywhere.\n\n"
    "THE GARMENT: "
)

# Ce que chaque croquis montre. Décrire la FORME, pas le mot — un mot
# polysémique se dessine selon son autre sens (le « courrier des lecteurs »
# est revenu en carnet d'alphabet).
SUJETS = {
    "chandail": "a long-sleeved crew-neck knit sweater with ribbed cuffs, ribbed hem and ribbed "
                "round neckline. HORIZONTAL STRIPES all over: navy blue stripes alternating with "
                "off-white stripes of equal width, the stripes running straight across the body "
                "and around the sleeves.",
    "parka":    "a long hooded winter parka reaching mid-thigh, in solid dark forest "
                "green. A hood with a faux-fur trim around the face opening, a central front "
                "zipper covered by a snap-button placket, two large flap pockets at the hips, "
                "two chest pockets, and elastic storm cuffs at the wrists. The hood is up and "
                "empty, seen from the front.",
    "espadrilles": "ONE PAIR of casual lace-up athletic sneakers, the two shoes side by side, "
                "seen from the outer side in profile, toes pointing left: white rubber sole, "
                "light grey upper, white laces, a small padded collar at the heel. Plain, "
                "without any stripes or logo on the side.",
}
TEMOINS = ["chandail", "parka", "espadrilles"]


def cle(nom):
    for l in (pathlib.Path.home() / "Claude" / ".env").read_text().splitlines():
        if l.startswith(nom + "="):
            return l.split("=", 1)[1].strip().strip('"').strip("'")


def consigne(ident):
    if ident not in SUJETS:
        raise SystemExit(f"{ident} : aucun sujet décrit dans SUJETS")
    return REGISTRE + SUJETS[ident]


def journal(ident, statut, note):
    sys.path.insert(0, str(GEN))
    try:
        from journal_appels import enregistrer_appel
        enregistrer_appel("google", MODELE, module="entreprise-francoeur",
                          cible=f"croquis {ident}", statut=statut,
                          estimation=0.067 if statut == "ok" else 0, note=note)
    except Exception as e:
        print("  (registre : %s)" % e)


def generer(ident):
    corps = {"contents": [{"parts": [{"text": consigne(ident)}]}],
             "generationConfig": {"responseModalities": ["IMAGE"],
                                  "imageConfig": {"aspectRatio": "1:1"}}}
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           f"{MODELE}:generateContent?key=" + cle("GOOGLE_API_KEY"))
    req = urllib.request.Request(url, data=json.dumps(corps).encode(),
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.loads(r.read())
    except Exception as e:
        journal(ident, "echec", str(e)[:120]); raise
    cand = (d.get("candidates") or [{}])[0]
    if "parts" not in cand.get("content", {}):
        raison = cand.get("finishReason") or d.get("promptFeedback", {}).get("blockReason")
        journal(ident, "echec", f"refus : {raison}")
        raise RuntimeError(f"refus du modèle : {raison}")
    donnees = None
    for part in cand["content"]["parts"]:
        ligne = part.get("inlineData") or part.get("inline_data")
        if ligne:
            donnees = base64.b64decode(ligne["data"])
    if not donnees:
        journal(ident, "echec", "réponse sans image"); raise RuntimeError("réponse sans image")
    DEST.mkdir(parents=True, exist_ok=True)
    cible = DEST / f"{ident}.png"
    # Ne jamais écraser une source : l'original part sous .orig au premier
    # remplacement, et n'est plus touché ensuite.
    orig = DEST / f"{ident}.orig.png"
    if cible.exists() and not orig.exists():
        cible.rename(orig)
    im = Image.open(io.BytesIO(donnees)).convert("RGB")
    im.save(cible)
    # La version servie : 800 px, JPEG 82 — la règle des images de vocabulaire.
    im.resize((800, round(im.height * 800 / im.width)), Image.LANCZOS).save(
        DEST / f"{ident}.jpg", "JPEG", quality=82)
    journal(ident, "ok", "1:1")
    print(f"  {ident:14} {len(donnees)/1024:5.0f} ko  {time.time()-t0:4.1f} s", flush=True)


if __name__ == "__main__":
    args = sys.argv[1:]
    essai = "--essai" in args
    cibles = [a for a in args if not a.startswith("--")]
    if "--temoins" in args or not cibles:
        cibles = cibles or TEMOINS
    connus = {e[0] for e in LEXIQUE}
    for c in cibles:
        if c not in connus:
            raise SystemExit(f"{c} : absent du lexique")
    for c in cibles:
        if essai:
            print(f"  {c:14} {len(consigne(c)):5} car.")
        else:
            generer(c)
