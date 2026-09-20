#!/usr/bin/env python3
"""Les images du bloc A — démonstration détail (Chaussures Rivard).

    python3 build/images_blocA.py --essai
    python3 build/images_blocA.py

REGISTRE TRANCHÉ LE 19 SEPTEMBRE 2026 : la PHOTO, sur le banc des trois
(assets/presentations/chaussure/banc/). Elle gagne contre le crayon et l'encre,
et la série de l'offre est déjà dans ce registre : une seule bibliothèque.

CE QUE LE BANC A MESURÉ, ET QU'IL FAUT DONC RÉPARER ICI : la photo a écrit sur
la porte — une enseigne de sortie de secours, pictogramme et lettres — alors
que la consigne l'interdisait en toutes lettres. Un registre photographique
traîne la signalétique du monde réel avec lui, parce qu'un vrai commerce en
porte. La parade n'est pas de répéter l'interdiction : c'est de CADRER. Ici,
aucune de ces trois images ne montre le haut de la porte.

LES PERSONNES SONT PERMISES, ce qui est nouveau. Les cinq images de l'offre
n'en portaient aucune — mais c'était à moitié une contrainte du registre, et le
banc a montré que la photo tient très bien un client au comptoir.

LE CLIENT EST UN HOMME, dans les trois, et ce n'est pas un détail : les
extraits du bloc le font parler avec `masculin_1`. Une image qui montrerait une
cliente contredirait ce que l'élève entend au même écran.

ON NE VOIT JAMAIS SON VISAGE EN ENTIER, et c'est une contrainte technique, pas
un principe : `route_images.py` est TEXTE-VERS-IMAGE, sans référence. On ne
peut donc pas tenir un personnage d'une image à l'autre. Trois visages nets
seraient trois clients différents dans une même histoire. De dos, de trois
quarts, coupé : c'est le même homme par implication.

Sortie : assets/interactive/entreprise-chaussure/images/
"""
import io, json, pathlib, sys, time

RACINE = pathlib.Path(__file__).resolve().parents[1]
GEN  = pathlib.Path.home() / 'Claude' / 'generations'
MODULE = 'entreprise-chaussure'
BASE = RACINE / 'assets' / 'interactive' / MODULE / 'images'
RATIO = "3:2"

sys.path.insert(0, str(RACINE / 'build'))
from route_images import generer_image, ESTIMATIONS

MAGASIN = ("Photographie réaliste, format paysage, objectif 35 mm, lumière "
           "douce et chaude de commerce, faible profondeur de champ. Un magasin "
           "de chaussures ordinaire de quartier, au Québec : plancher de bois "
           "clair, murs blancs nus, étagères de bois blond. Ni luxe ni boutique "
           "de mode. ")

SANS = ("Aucun texte, aucun mot, aucun chiffre, aucune lettre, aucune étiquette "
        "de prix, aucune affiche, aucune pancarte, aucun écriteau, aucune "
        "enseigne, aucun logo, aucune marque, aucun autocollant. Les boîtes sont "
        "de carton uni et lisse, sans impression. Les chaussures sont unies, sans "
        "logo, sans bande latérale, sans motif reconnaissable. Le haut de la "
        "porte n'entre pas dans le cadre.")

IMAGES = [
    ('client-sort', "écran 1 — « le monsieur est reparti »",
     MAGASIN +
     "Vue depuis l'intérieur du magasin, à hauteur d'yeux, vers la porte vitrée "
     "de l'entrée. Un homme adulte en manteau ordinaire vient de sortir&nbsp;: on "
     "le voit de DOS, à contre-jour, déjà sur le trottoir, à travers la vitre. Il "
     "s'éloigne. Le cadre est coupé à hauteur du linteau&nbsp;: on ne voit ni le "
     "haut de la porte ni le mur au-dessus. Au premier plan à gauche, floue, "
     "l'extrémité d'une étagère de bois portant deux chaussures. Le magasin est "
     "vide derrière lui. " + SANS),

    ('au-comptoir', "écran 3 — l'échange, fait comme il faut",
     MAGASIN +
     "Vue par-dessus l'épaule d'une vendeuse debout derrière le comptoir&nbsp;: on "
     "voit son épaule et sa nuque au premier plan à gauche, de dos, floues — "
     "jamais son visage. De l'autre côté du comptoir de bois clair, un homme "
     "adulte en vêtements ordinaires, vu de trois quarts et cadré de la poitrine "
     "aux épaules, une main posée à plat sur une boîte de carton uni. Sa tête est "
     "coupée par le bord supérieur du cadre&nbsp;: on ne voit pas son visage. Le "
     "comptoir occupe le bas de l'image. Derrière lui, le plancher de vente, flou. " + SANS),

    ('je-regarde', "écran 5 — « non, non, je regarde »",
     MAGASIN +
     "Un homme adulte, seul, debout devant un mur d'étagères de bois portant des "
     "chaussures sur de petits supports inclinés. On le voit de DOS, en entier, à "
     "quelques pas&nbsp;: il regarde les rayons, les mains dans les poches, sans "
     "rien toucher. La lumière vient de la gauche. Le reste du magasin est vide et "
     "flou. Aucune porte dans le cadre. " + SANS),
]


def reduire(data, largeur=1200, qualite=85):
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert('RGB')
    h = max(1, round(largeur * im.height / im.width))
    im = im.resize((largeur, h), Image.LANCZOS)
    t = io.BytesIO(); im.save(t, 'JPEG', quality=qualite, optimize=True)
    return t.getvalue()


essai = '--essai' in sys.argv
voulus = set(a for a in sys.argv[1:] if not a.startswith('--'))
if not essai:
    GEN.mkdir(parents=True, exist_ok=True); BASE.mkdir(parents=True, exist_ok=True)
horodatage = time.strftime('%Y%m%d-%H%M%S')
faits, sautes, echecs, cout = [], [], [], 0.0

for nom, ecran, prompt in IMAGES:
    if voulus and nom not in voulus:
        continue
    cible = BASE / (nom + '.jpg')
    if cible.exists() and cible.stat().st_size > 1000:
        sautes.append(nom); continue
    if essai:
        print('  %-12s %4d caractères · %s' % (nom, len(prompt), ecran)); continue
    try:
        data, route = generer_image(prompt, ratio=RATIO, resolution="1K",
                                    module=MODULE, cible=nom)
    except Exception as e:
        echecs.append('%s : %s' % (nom, e)); continue
    brut = data
    try:
        data = reduire(data)
    except Exception as e:
        echecs.append('%s : réduction impossible (%s)' % (nom, e))
    base = '%s_images-%s_%s' % (MODULE, nom, horodatage)
    (GEN / (base + '.jpg')).write_bytes(brut)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "nano-banana-2", "prompt": prompt, "refs": [],
        "params": {"num_images": 1, "aspect_ratio": RATIO,
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": route, "cost_estimate_usd": ESTIMATIONS.get(route, 0.08),
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation", "module": MODULE, "page": ecran,
        "destination": "assets/interactive/%s/images/%s.jpg" % (MODULE, nom),
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data); faits.append(nom)
    cout += ESTIMATIONS.get(route, 0.08)
    print('  ✓ %-12s %6.1f Ko   %s' % (nom, len(data)/1024, route), flush=True)

print()
print("  À BLANC — rien n'a été engendré." if essai else
      '%d produite(s), %d sautée(s), %d échec(s) · environ %.2f $'
      % (len(faits), len(sautes), len(echecs), cout))
for e in echecs: print('  ✗ ' + e)
