#!/usr/bin/env python3
"""Génère les 15 images de module-n5-emmenagement via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les huit illustrations de l'exercice `prImg` ;
  · `vocab/`  — les sept photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

Le module parle d'un déménagement : des objets ordinaires, du carton, un
escalier extérieur, un sous-sol d'immeuble. Rien de publicitaire, aucun logo
de compagnie de déménagement — d'où l'interdiction de texte dans le style.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-emmenagement/gen_images.py
  python3 build/contenu/module-n5-emmenagement/gen_images.py diable-charge
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n5-emmenagement'
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

STYLE = ("Photographie réaliste, format paysage, lumière naturelle, faible "
         "profondeur de champ. Logement locatif québécois ordinaire, ni luxueux "
         "ni délabré, palette sobre. Aucun texte lisible, aucune écriture, "
         "aucun logo, aucun filigrane, aucune personne identifiable.")

DEHORS = ("Photographie réaliste, format paysage, extérieur d'un petit immeuble "
          "à logements du Québec, lumière de fin de journée en été, faible "
          "profondeur de champ. Aucun texte lisible, aucun logo, aucune plaque "
          "d'immatriculation lisible, aucune personne identifiable.")

P_EX1 = "Je découvre · Exercice 3 — Les choses du déménagement"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les huit images de `prImg` ──────────────────────────
 ('pile-de-cartons', 'images', P_EX1, STYLE + " Une pile de boîtes de carton brun "
  "fermées avec du ruban adhésif, empilées dans un salon presque vide, près d'une "
  "fenêtre. Aucune inscription lisible sur les boîtes."),
 ('diable-charge', 'images', P_EX1, STYLE + " Un diable de déménagement à deux roues, "
  "chargé de trois boîtes de carton sanglées, immobile dans un corridor d'immeuble au "
  "plancher de bois."),
 ('camion-demenagement', 'images', P_EX1, DEHORS + " Un camion de déménagement blanc, "
  "porte arrière relevée et rampe posée sur le trottoir, stationné devant un immeuble "
  "à logements. Camion sans aucune inscription ni logo."),
 ('escalier-exterieur', 'images', P_EX1, DEHORS + " Un escalier extérieur de métal en "
  "colimaçon, typique des immeubles de Québec, montant vers le balcon d'un deuxième "
  "étage, vu d'en bas."),
 ('compteur-electrique', 'images', P_EX1, STYLE + " Un compteur d'électricité gris fixé "
  "au mur de béton d'un sous-sol d'immeuble, éclairage d'ampoule nue. Les chiffres du "
  "cadran sont flous et illisibles."),
 ('bac-brun-trottoir', 'images', P_EX1, DEHORS + " Un bac de compostage brun à roulettes "
  "posé sur le trottoir devant un immeuble, un matin. Aucune inscription lisible sur le "
  "bac."),
 ('salle-de-lavage', 'images', P_EX1, STYLE + " Une petite salle de lavage commune au "
  "sous-sol d'un immeuble : deux laveuses et deux sécheuses côte à côte, une table de "
  "pliage, un plancher de béton peint."),
 ('logement-vide', 'images', P_EX1, STYLE + " Un salon complètement vide dans un "
  "logement locatif, plancher de bois franc, deux fenêtres sans rideau, murs beiges. "
  "Aucun meuble, aucune boîte."),

 # ── Le banc de vocabulaire ────────────────────────────────────────────
 ('carton', 'vocab', P_VOC, STYLE + " Une seule boîte de carton brun fermée avec du "
  "ruban adhésif, posée seule sur un plancher de bois, vue de trois quarts."),
 ('diable', 'vocab', P_VOC, STYLE + " Un diable de déménagement à deux roues, vide, "
  "appuyé contre un mur clair dans une entrée."),
 ('egratignure', 'vocab', P_VOC, STYLE + " Vue rapprochée et rasante d'une longue "
  "égratignure claire dans le vernis d'un plancher de bois franc, près d'une plinthe."),
 ('couverture', 'vocab', P_VOC, STYLE + " Une couverture de déménagement matelassée "
  "grise enveloppant le coin d'un meuble de bois, avec une sangle, dans un logement "
  "vide."),
 ('compteur', 'vocab', P_VOC, STYLE + " Vue rapprochée d'un compteur électrique gris "
  "sur un mur de béton, cadran rond, chiffres flous et illisibles."),
 ('bac-brun', 'vocab', P_VOC, DEHORS + " Un bac brun de compostage à roulettes, "
  "couvercle fermé, sur le gazon près d'une entrée d'immeuble. Aucune inscription "
  "lisible."),
 ('deneigement', 'vocab', P_VOC, DEHORS + " Une rue résidentielle enneigée au petit "
  "matin d'hiver au Québec, bancs de neige de chaque côté et une souffleuse municipale "
  "au loin, hors foyer. Aucune plaque ni inscription lisible."),
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
