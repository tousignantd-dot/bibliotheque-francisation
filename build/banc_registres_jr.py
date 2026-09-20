#!/usr/bin/env python3
"""Banc de registres pour l'écran du jeu de rôle « détail ».

    python3 build/banc_registres_jr.py --essai
    python3 build/banc_registres_jr.py

POURQUOI UN BANC. Le réalisme des cinq images de l'offre a été choisi par
COHÉRENCE avec Belrive, pas par le critère. Or le critère — « quelle est la
nature du signe que l'apprenant doit voir ? » — ne tranche pas ici : dans un
jeu de rôle il n'y a rien à lire dans l'image, la compétence est d'écouter et
de parler. Quand aucun signe ne commande, un registre se GAGNE, il ne se
choisit pas.

LA SCÈNE EST LE CAS DIFFICILE, pas une salle vide : un client en face du
vendeur. C'est précisément ce que la photo interdisait — j'avais exclu les
personnes pour ne pas castrer un visage, un âge et une origine, et mon concept
« le client ne se montre jamais » était donc à moitié une contrainte du
registre plutôt qu'un choix. Le banc met cette contrainte à l'épreuve.

MÊME SCÈNE, MOT POUR MOT, pour les trois. Un banc dont les scènes diffèrent ne
compare rien. Les préambules s'IMPORTENT du catalogue — une copie se corrige et
l'original pas, et rien ne le signale.

RÉSERVE : ces préambules ont été éprouvés sur la route image-à-image du
simulateur, jamais sur route_images.py. C'est du texte, donc ça devrait passer ;
le banc est aussi ce qui le vérifie.

Sortie : assets/presentations/chaussure/banc/
"""
import io, json, pathlib, sys, time

RACINE = pathlib.Path(__file__).resolve().parents[1]
GEN  = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'presentations' / 'chaussure' / 'banc'
RATIO = "3:2"
MODULE = 'banc-registres-jr'

sys.path.insert(0, str(RACINE / 'build'))
sys.path.insert(0, str(pathlib.Path.home() / 'Claude' / 'portfolio-conception' / 'registres'))
from route_images import generer_image, ESTIMATIONS
from catalogue import REGISTRES          # importé, jamais recopié

# ── La scène, identique pour les trois ───────────────────────────────────
# Écrite en anglais parce que les préambules éprouvés le sont : mêler deux
# langues dans une consigne est une variable de plus dans un banc.
SCENE = (
 "\n\nThe view is that of a shop assistant standing behind the counter of an "
 "ordinary neighbourhood shoe shop, looking out at a customer. Across the "
 "counter, an adult customer in ordinary everyday clothes stands facing the "
 "assistant, seen from the chest up, three quarters on. The customer has just "
 "set a plain smooth shoe box down on the counter and still has one hand "
 "resting on it; the other hand hangs at their side. They are looking towards "
 "the viewer and speaking, with an ordinary neutral everyday expression — "
 "neither angry nor delighted. The near edge of the wooden counter runs across "
 "the bottom of the frame. Behind the customer, the shop: a wall of shelves "
 "with single shoes on small slanted stands, a low wooden fitting bench, and "
 "the glazed front door with daylight coming through it. Nobody else is in the "
 "shop.\n"
 "The shoe box is smooth and completely blank. The shoes on the shelves are "
 "plain, with no logo, no side stripe and no recognisable pattern. The walls "
 "and the door carry nothing written.")

PHOTO = ("Realistic photograph, landscape format, 35 mm lens, soft warm shop "
         "light, shallow depth of field.")

BANCS = [
    ('crayon',  REGISTRES['crayon']['preambule']),
    ('encre',   REGISTRES['encre']['preambule']),
    ('photo',   PHOTO),                   # le témoin
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

for nom, preambule in BANCS:
    if voulus and nom not in voulus:
        continue
    prompt = preambule + SCENE
    cible = BASE / (nom + '.jpg')
    if cible.exists() and cible.stat().st_size > 1000:
        sautes.append(nom); continue
    if essai:
        print('  %-8s %4d caractères  (préambule %d + scène %d)'
              % (nom, len(prompt), len(preambule), len(SCENE)))
        continue
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
    base = '%s_%s_%s' % (MODULE, nom, horodatage)
    (GEN / (base + '.jpg')).write_bytes(brut)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "nano-banana-2", "prompt": prompt, "refs": [],
        "params": {"num_images": 1, "aspect_ratio": RATIO,
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": route, "cost_estimate_usd": ESTIMATIONS.get(route, 0.08),
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation", "module": MODULE,
        "page": "banc de registres — écran du jeu de rôle détail",
        "destination": "assets/presentations/chaussure/banc/%s.jpg" % nom,
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data); faits.append(nom)
    cout += ESTIMATIONS.get(route, 0.08)
    print('  ✓ %-8s %6.1f Ko   %s' % (nom, len(data)/1024, route), flush=True)

print()
print("  À BLANC — rien n'a été engendré." if essai else
      '%d produite(s), %d sautée(s), %d échec(s) · environ %.2f $'
      % (len(faits), len(sautes), len(echecs), cout))
for e in echecs:
    print('  ✗ ' + e)
