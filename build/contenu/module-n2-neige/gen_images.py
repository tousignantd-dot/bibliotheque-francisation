#!/usr/bin/env python3
"""Génère les 20 images de module-n2-neige via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer ;
  · `vocab/`  — les quatorze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdait le tiers du haut et du bas. Voir
`docs/chantier-tous-niveaux.md`.

La difficulté propre à ce module est l'inverse de celle de l'inscription :
le sujet n'est pas un papier couvert de mots, c'est **le ciel**, et vingt
photos de ciel se ressemblent toutes. Chaque prompt change donc de sujet au
sol autant que de temps — la rue, le trottoir, la fenêtre, l'entrée d'un
immeuble, une paire de bottes près de la porte — pour qu'un élève reconnaisse
la photo à ce qu'il y a dedans, pas seulement à la couleur du ciel.

Deuxième contrainte : le thermomètre. C'est le seul objet du module qui doit
montrer un nombre, et le générateur a l'ordre de n'en produire aucun de
lisible. Les prompts demandent donc une graduation floue et une colonne
descendue bas dans le tube : le froid se lit à la position, jamais au chiffre.
L'élève lit les vrais nombres dans le bandeau noir de l'exercice.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n2-neige/gen_images.py
  python3 build/contenu/module-n2-neige/gen_images.py temps-neige
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n2-neige'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
ENV  = pathlib.Path('/Users/danieltousignant/Claude/.env')
RATIO = "3:2"


def cle(nom):
    for ligne in ENV.read_text(encoding='utf-8').splitlines():
        ligne = ligne.strip()
        if ligne.startswith(nom + '='):
            return ligne.split('=', 1)[1].strip().strip('"\'')
    return ''


FAL = cle('FAL_KEY')
if not FAL:
    sys.exit('FAL_KEY absente de ~/Claude/.env')

SANS = ("Aucun texte lisible, aucun mot déchiffrable, aucune écriture "
        "reconnaissable, aucun chiffre, aucun nom, aucun logo, aucune marque, "
        "aucun filigrane, aucun visage, aucune personne identifiable — les "
        "personnes, s'il y en a, sont vues de dos ou cadrées sans le visage. "
        "L'écriture imprimée et les graduations, quand il y en a, se lisent "
        "comme des traits gris flous, hors foyer.")

# Le décor principal : une rue résidentielle de Montréal, en hiver.
RUE = ("Photographie réaliste, format paysage, lumière du jour d'hiver, "
       "douce et grise. Rue résidentielle de Montréal : immeubles de brique, "
       "escaliers extérieurs de métal, trottoir, arbres sans feuilles. "
       "Palette froide et sobre. " + SANS)

# Ce qui se photographie de près, à hauteur de main.
PRES = ("Photographie réaliste, format paysage, vue rapprochée en lumière "
        "naturelle douce, faible profondeur de champ, palette neutre et "
        "froide. " + SANS)

# L'intérieur : l'entrée d'un immeuble, une cuisine, une fenêtre.
DEDANS = ("Photographie réaliste, format paysage, lumière d'intérieur douce "
          "avec la clarté pâle de l'hiver par la fenêtre. Logement ordinaire "
          "de Montréal, mobilier simple, palette calme. " + SANS)

P_EX  = "Je découvre · Exercice 3 — Quel temps fait-il sur la photo ?"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('temps-neige', 'images', P_EX, RUE + " Il neige à gros flocons : les toits, "
  "les escaliers et les autos stationnées sont couverts de blanc, la rue vue "
  "en enfilade, l'air rempli de flocons en suspension."),
 ('temps-pluie', 'images', P_EX, RUE + " Il pleut : l'asphalte est mouillé et "
  "brillant, des flaques reflètent les immeubles, deux silhouettes de dos "
  "tiennent un parapluie ouvert au bout du trottoir."),
 ('temps-soleil', 'images', P_EX, RUE + " Il fait grand soleil : ciel bleu "
  "franc, sans un nuage, ombres nettes des arbres sur la neige, façades bien "
  "éclairées."),
 ('temps-vent', 'images', P_EX, RUE + " Il vente très fort : les branches nues "
  "sont penchées dans le même sens, la neige au sol est soulevée en traînées "
  "basses, une silhouette de dos se tient courbée contre le vent."),
 ('temps-froid', 'images', P_EX, PRES + " Gros plan sur un thermomètre "
  "extérieur rond fixé au cadre d'une fenêtre givrée, sa colonne descendue "
  "très bas, la graduation entièrement floue et illisible, du givre sur la "
  "vitre autour."),
 ('temps-glace', 'images', P_EX, PRES + " Gros plan en plongée sur un trottoir "
  "de béton couvert d'une plaque de glace lisse et luisante, quelques grains "
  "de sel gris dessus, le bas d'une rampe de métal dans le coin."),

 # ── Les quatorze photos du banc de vocabulaire ────────────────────────
 ('neige', 'vocab', P_VOC, PRES + " Vue en plongée sur une épaisse couche de "
  "neige fraîche et poudreuse posée sur un banc de parc, la surface intacte, "
  "quelques flocons encore en l'air."),
 ('pluie', 'vocab', P_VOC, DEDANS + " Vue à travers une fenêtre couverte de "
  "gouttes de pluie qui coulent, la rue derrière entièrement floue et grise."),
 ('vent', 'vocab', P_VOC, RUE + " Des branches nues et un fil électrique "
  "penchés dans le même sens, de la neige fine soulevée en traînées au ras "
  "du sol, ciel bas et uniforme."),
 ('soleil', 'vocab', P_VOC, RUE + " Le soleil bas de l'hiver derrière des "
  "branches nues, ciel bleu pâle et lumineux, longues ombres bleutées sur la "
  "neige."),
 ('nuage', 'vocab', P_VOC, "Photographie réaliste, format paysage. Ciel "
  "d'hiver couvert de gros nuages gris et blancs bien détachés, une ligne de "
  "toits sombres tout en bas du cadre. Palette froide. " + SANS),
 ('temperature', 'vocab', P_VOC, PRES + " Un thermomètre extérieur à colonne, "
  "vertical, accroché à un mur de brique, sa colonne rouge descendue bas dans "
  "le tube, les traits de graduation flous et sans aucun chiffre lisible."),
 ('bulletin-meteo', 'vocab', P_VOC, DEDANS + " Un petit poste de radio de "
  "cuisine posé sur un comptoir, vu de trois quarts, une tasse fumante à "
  "côté, la fenêtre blanche de neige derrière, hors foyer."),
 ('hiver', 'vocab', P_VOC, RUE + " Une rue entièrement enneigée après une "
  "bordée : bancs de neige le long du trottoir, autos ensevelies, escaliers "
  "de métal blancs, ciel gris."),
 ('ville', 'vocab', P_VOC, "Photographie réaliste, format paysage, lumière "
  "d'hiver. Vue large d'un quartier de Montréal depuis un point haut : toits "
  "plats enneigés, ruelles, clochers et tours au loin dans une brume froide. "
  "Palette froide. " + SANS),
 ('manteau', 'vocab', P_VOC, DEDANS + " Un gros manteau d'hiver matelassé "
  "suspendu à un crochet dans l'entrée d'un logement, vu de face et de près, "
  "capuchon bordé de fourrure, mur pâle derrière."),
 ('tuque', 'vocab', P_VOC, PRES + " Une tuque de laine tricotée posée à plat "
  "sur une table de bois clair, vue légèrement de biais, sa maille bien "
  "visible, aucune étiquette."),
 ('mitaines', 'vocab', P_VOC, PRES + " Une paire de mitaines de laine posées "
  "côte à côte sur un rebord de fenêtre enneigé, vues d'en haut, la neige "
  "autour."),
 ('bottes', 'vocab', P_VOC, DEDANS + " Une paire de bottes d'hiver hautes "
  "posées sur un tapis dans l'entrée d'un logement, encore mouillées de neige "
  "fondue, vues de trois quarts."),
 ('tempete', 'vocab', P_VOC, RUE + " Une tempête de neige en cours : "
  "visibilité très réduite, tout est blanc et flou, on devine à peine les "
  "immeubles et un lampadaire allumé au milieu du cadre."),
]


def genere(prompt):
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": RATIO,
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + FAL, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.loads(r.read())
    with urllib.request.urlopen(d["images"][0]["url"], timeout=240) as r:
        return r.read()


def reduire(data, largeur=800, qualite=82):
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien."""
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert('RGB')
    hauteur = max(1, round(largeur * im.height / im.width))
    im = im.resize((largeur, hauteur), Image.LANCZOS)
    tampon = io.BytesIO()
    im.save(tampon, 'JPEG', quality=qualite, optimize=True)
    return tampon.getvalue()


voulus = set(sys.argv[1:])
GEN.mkdir(parents=True, exist_ok=True)
horodatage = time.strftime('%Y%m%d-%H%M%S')
faits, sautes, echecs = [], [], []

for nom, dossier, page, prompt in IMAGES:
    etiquette = '%s/%s' % (dossier, nom)
    if voulus and nom not in voulus and etiquette not in voulus:
        continue
    dest = BASE / dossier
    dest.mkdir(parents=True, exist_ok=True)
    cible = dest / (nom + '.jpg')
    if cible.exists() and cible.stat().st_size > 1000:
        sautes.append(etiquette); continue
    try:
        data = genere(prompt)
    except urllib.error.HTTPError as e:
        echecs.append('%s : HTTP %s %s' % (etiquette, e.code, e.read()[:180])); continue
    except Exception as e:
        echecs.append('%s : %s' % (etiquette, e)); continue

    brut = data
    if dossier == 'vocab':
        try:
            data = reduire(data)
        except Exception as e:
            echecs.append('%s : réduction impossible (%s) — image brute gardée'
                          % (etiquette, e))

    base = '%s_%s-%s_%s' % (MODULE, dossier, nom, horodatage)
    (GEN / (base + '.jpg')).write_bytes(brut)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "fal-ai/nano-banana-2",
        "prompt": prompt,
        "refs": [],
        "params": {"num_images": 1, "aspect_ratio": RATIO,
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": "fal.ai",
        "cost_estimate_usd": 0.034,
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation",
        "module": MODULE,
        "page": page,
        "destination": "assets/interactive/%s/%s/%s.jpg" % (MODULE, dossier, nom),
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(etiquette)
    print('  ✓ %-28s %6.1f Ko' % (etiquette, len(data) / 1024), flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s) · environ %.2f $'
      % (len(faits), len(sautes), len(echecs), 0.034 * len(faits)))
for e in echecs:
    print('  !! ' + e)
