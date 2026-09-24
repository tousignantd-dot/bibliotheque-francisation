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
    python3 build/francoeur_croquis.py --tous           # tout ce qui manque sur le disque
    python3 build/francoeur_croquis.py --servir         # refait les .jpg depuis les .png, gratuit
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
    "no price tag, no clothing tag anywhere. No frame, no border, no box around the drawing.\n\n"
    "THE GARMENT: "
)

# Ce que chaque croquis montre vit dans le CONTENU, pas ici :
# build/contenu/entreprise-francoeur/sujets.py — (famille, description).
from sujets import SUJETS  # noqa: E402

# Le détail : le vêtement entier en gris pâle, seule la partie nommée en
# couleur. Même trait, même cadre que les autres croquis.
DETAIL = REGISTRE.replace(
    "COLOUR: one flat, soft, slightly muted fill of the colour named below, inside the outline "
    "only, with at most one lighter tone for the inside of a collar or a lining.",
    "COLOUR: the whole garment is filled in ONE flat, very pale neutral grey, EXCEPT the one part "
    "named below, which is filled in the bright colour named. That coloured part is the whole "
    "point of the drawing: it must stand out at a glance.")

# L'objet du magasin : même trait, même aplat, sans la phrase qui exclut les
# cintres et les mannequins — certains objets en SONT.
OBJET = (
    "A clean flat illustration in the style of a fashion flat sketch: the object ALONE, seen "
    "straight on or at a slight three-quarter angle, centred, filling about 70 % of a square "
    "frame, on a pure white background.\n"
    "LINE: crisp black ink outline of even weight, with thin inner lines for details. No sketchy "
    "strokes, no hatching, no pencil texture.\n"
    "COLOUR: flat, soft, slightly muted fills of the colours named below, inside the outlines "
    "only. No gradient, no shading, no shadow on the background, no 3D rendering, no photograph.\n"
    "NOTHING ELSE IN THE FRAME: no person, no hand, no background scene beyond what is named. No "
    "text, no letters, no numbers, no logo, no brand name, no sign anywhere. No frame, no border, no box around the drawing.\n\n"
    "THE OBJECT: ")
PREAMBULES = {"vetement": REGISTRE, "detail": DETAIL, "objet": OBJET}
TEMOINS = ["chandail", "parka", "espadrilles"]


def cle(nom):
    for l in (pathlib.Path.home() / "Claude" / ".env").read_text().splitlines():
        if l.startswith(nom + "="):
            return l.split("=", 1)[1].strip().strip('"').strip("'")


def consigne(ident):
    if ident not in SUJETS:
        raise SystemExit(f"{ident} : aucun sujet décrit dans sujets.py")
    famille, quoi = SUJETS[ident]
    return PREAMBULES[famille] + quoi


def blanchir(im):
    """Le fond rendu est souvent un blanc cassé (≈ 248) : sur la planche, chaque
    carte montrait alors son rectangle. On pousse au blanc pur ce qui est déjà
    presque blanc — au-dessus de 243 sur les trois canaux, ce qui laisse
    intacts le crème des rayures (≈ 232) et les aplats pâles."""
    import numpy as np
    a = np.asarray(im).copy()
    a[(a >= 243).all(axis=2)] = 255
    # Et une marge de 1,5 % remise à blanc : six croquis sur cent cinq sont
    # sortis avec un filet de cadre collé au bord, malgré « no frame ». Le
    # dessin occupe ~70 % du cadre, la marge ne touche jamais le vêtement.
    m = max(2, round(a.shape[0] * 0.015))
    a[:m], a[-m:], a[:, :m], a[:, -m:] = 255, 255, 255, 255
    return Image.fromarray(a)


def servir(ident):
    """La version servie, refaite depuis la source : 800 px, JPEG 82 — la règle
    des images de vocabulaire — et le fond blanchi."""
    im = blanchir(Image.open(DEST / f"{ident}.png").convert("RGB"))
    im.resize((800, round(im.height * 800 / im.width)), Image.LANCZOS).save(
        DEST / f"{ident}.jpg", "JPEG", quality=82)


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
    servir(ident)
    journal(ident, "ok", "1:1")
    print(f"  {ident:14} {len(donnees)/1024:5.0f} ko  {time.time()-t0:4.1f} s", flush=True)


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    args = sys.argv[1:]
    essai = "--essai" in args
    cibles = [a for a in args if not a.startswith("--")]
    a_dessiner = [e[0] for e in LEXIQUE if e[4] == "croquis"]
    if "--servir" in args:
        # Refait tous les .jpg depuis les .png, sans aucun appel payé.
        for e in LEXIQUE:
            if e[4] == "croquis" and (DEST / f"{e[0]}.png").exists():
                servir(e[0])
        print("versions servies refaites"); sys.exit(0)
    if "--manquants" in args:
        manque = [i for i in a_dessiner if i not in SUJETS]
        print(f"{len(a_dessiner)} croquis au lexique, {len(manque)} sans sujet : {manque}")
        sys.exit(1 if manque else 0)
    if "--tous" in args:
        # Ce qui est déjà sur le disque ne se repaie pas.
        cibles = [i for i in a_dessiner if not (DEST / f"{i}.png").exists()]
    elif not cibles:
        cibles = TEMOINS
    connus = {e[0] for e in LEXIQUE}
    for c in cibles:
        if c not in connus:
            raise SystemExit(f"{c} : absent du lexique")
        consigne(c)  # refuse tôt un sujet manquant, avant le premier appel payé
    if essai:
        for c in cibles:
            print(f"  {c:16} {SUJETS[c][0]:8} {len(consigne(c)):5} car.")
        print(f"{len(cibles)} croquis, ≈ {len(cibles) * 0.067:.2f} $")
        sys.exit(0)
    echecs = []
    def un(c):
        try:
            generer(c)
        except Exception as e:
            echecs.append(c); print(f"  {c:16} ÉCHEC {e}", flush=True)
    with ThreadPoolExecutor(4) as pool:
        list(pool.map(un, cibles))
    print(f"{len(cibles) - len(echecs)} produits, {len(echecs)} échecs {echecs or ''}")
