#!/usr/bin/env python3
"""Génère les 14 images de module-n2-autobus via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer,
    telles que rendues ;
  · `vocab/`  — les huit photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdait le tiers du haut et du bas. Voir
`docs/chantier-tous-niveaux.md`.

Le module se passe dehors, dans la rue et à l'arrêt : le décor n'est pas le
centre de formation, contrairement aux modules précédents. Les six photos de
l'exercice doivent rester **reconnaissables du premier coup d'œil** — un élève
de niveau 2 les associe à une phrase de cinq mots, sans lire de légende.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n2-autobus/gen_images.py
  python3 build/contenu/module-n2-autobus/gen_images.py feu-circulation
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n2-autobus'
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

# Le décor commun : un quartier résidentiel de Montréal, hors du centre-ville.
RUE = ("Photographie réaliste, format paysage, lumière naturelle de jour. "
       "Quartier résidentiel de Montréal : briques, escaliers extérieurs, "
       "érables, trottoirs de béton. Palette sobre. Aucun texte lisible, "
       "aucune écriture, aucun logo, aucun filigrane, aucune personne "
       "identifiable.")

# Quand une personne est nécessaire, elle reste de dos ou hors cadrage.
PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne "
        "dans un quartier de Montréal, avec une ou deux personnes vues de dos "
        "ou de trois quarts, visage hors cadrage. Lumière naturelle douce, "
        "faible profondeur de champ. Aucun visage reconnaissable, aucun texte, "
        "aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Dans la rue"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 # Chacune doit se lire seule : c'est l'objet même de l'exercice.
 ('arret-autobus', 'images', P_EX, RUE + " Un abribus vitré au bord d'un trottoir, "
  "vu de trois quarts, avec un banc à l'intérieur et un poteau d'arrêt à côté. "
  "Aucun panneau écrit lisible. Personne au premier plan."),
 ('feu-circulation', 'images', P_EX, RUE + " Un feu de circulation vu d'en bas contre "
  "le ciel, à un carrefour. Le feu rouge est allumé, nettement visible."),
 ('plan-quartier', 'images', P_EX, RUE + " Un panneau-plan de quartier sous vitre, "
  "planté au bord d'un trottoir. Le plan montre des lignes de rues et des formes "
  "colorées, mais aucun mot n'est lisible."),
 ('horaire-affiche', 'images', P_EX, RUE + " Gros plan sur un panneau d'horaire "
  "d'autobus fixé à un poteau d'arrêt : des colonnes de chiffres alignées sous "
  "vitre. Les chiffres restent flous et illisibles."),
 ('coin-rue', 'images', P_EX, RUE + " Le coin de deux rues résidentielles, vu du "
  "trottoir opposé : deux trottoirs qui se rencontrent à angle droit, un lampadaire, "
  "un bâtiment de brique à l'angle."),
 ('avis-porte', 'images', P_EX, RUE + " Une feuille de papier blanche scotchée sur "
  "la porte vitrée d'un édifice public. Le papier est net, mais le texte imprimé "
  "dessus reste flou et illisible."),

 # ── Les huit photos du banc de vocabulaire ────────────────────────────
 ('arret', 'vocab', P_VOC, RUE + " Un poteau d'arrêt d'autobus seul au bord d'un "
  "trottoir, vu de près contre un fond de rue floue. Aucun chiffre lisible."),
 ('coin', 'vocab', P_VOC, RUE + " L'angle d'un bâtiment de brique là où deux "
  "trottoirs se rejoignent, vu de trois quarts."),
 ('feu', 'vocab', P_VOC, RUE + " Un feu de circulation vu de près, le feu vert "
  "allumé, le reste de la rue flou derrière."),
 ('trottoir', 'vocab', P_VOC, RUE + " Un trottoir de béton bordé d'arbres, vu au "
  "niveau du sol, qui s'éloigne vers le fond de l'image. Personne dessus."),
 ('plan', 'vocab', P_VOC, RUE + " Un plan de quartier sur papier, déplié sur un "
  "banc de parc. Les tracés de rues sont nets, les noms illisibles."),
 ('horaire', 'vocab', P_VOC, RUE + " Un dépliant d'horaire d'autobus tenu à la "
  "main, cadré sur le papier seul : des colonnes de chiffres flous."),
 ('correspondance', 'vocab', P_VOC, RUE + " Gros plan sur un petit billet de papier "
  "mince tenu entre deux doigts, devant un fond d'intérieur d'autobus flou. "
  "Aucune écriture lisible sur le billet."),
 ('avis', 'vocab', P_VOC, PERS + " Une personne vue de dos lit une feuille affichée "
  "sur une porte vitrée de commerce. Le texte de la feuille est flou."),
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
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien.

    La hauteur suit le rapport de l'image reçue, au lieu d'être forcée à un
    carré comme dans les modules précédents — c'est tout l'objet du passage
    au 3:2.
    """
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
