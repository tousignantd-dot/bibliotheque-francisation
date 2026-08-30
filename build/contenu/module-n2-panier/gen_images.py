#!/usr/bin/env python3
"""Génère les 18 images de module-n2-panier via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer,
    telles que rendues ;
  · `vocab/`  — les douze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdait le tiers du haut et du bas. Voir
`docs/chantier-tous-niveaux.md`.

Le décor est une épicerie de quartier, et une cuisine pour ce qui se lit à la
maison. La difficulté propre à ce module : **il porte sur des papiers écrits**
— circulaire, étiquette, affichette — et le générateur a l'ordre de ne
produire aucun texte lisible. Les prompts demandent donc des papiers dont la
*forme* est nette (colonnes, encadrés, gros chiffres flous) sans qu'aucun mot
ne se lise. Un élève de niveau 2 reconnaît l'objet, pas son contenu ; le
contenu, c'est l'exercice qui le donne.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n2-panier/gen_images.py
  python3 build/contenu/module-n2-panier/gen_images.py allee-epicerie
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n2-panier'
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

# Le décor commun : une épicerie de quartier, pas une grande surface clinquante.
EPICERIE = ("Photographie réaliste, format paysage, lumière naturelle et "
            "néons doux d'une épicerie de quartier au Québec. Tablettes de "
            "métal clair, plancher de béton poli, palette sobre. Aucun texte "
            "lisible, aucune écriture, aucun logo, aucune marque, aucun "
            "filigrane, aucune personne identifiable.")

# Ce qui se lit à la maison : la table de cuisine, avant de partir.
CUISINE = ("Photographie réaliste, format paysage, lumière naturelle de jour "
           "par une fenêtre. Table de cuisine en bois d'un appartement "
           "modeste. Palette chaude et sobre. Aucun texte lisible, aucune "
           "écriture, aucun logo, aucune marque, aucun filigrane, aucune "
           "personne identifiable.")

P_EX  = "Je découvre · Exercice 3 — À l'épicerie"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 # Chacune doit se lire seule : c'est l'objet même de l'exercice.
 ('circulaire-table', 'images', P_EX, CUISINE + " Un grand dépliant publicitaire "
  "de papier journal, déplié sur la table, montrant une grille de photos de "
  "légumes et de gros chiffres. Les chiffres et les mots restent flous et "
  "illisibles ; seule la grille se voit."),
 ('allee-epicerie', 'images', P_EX, EPICERIE + " Une allée vide entre deux hautes "
  "rangées de tablettes garnies de conserves et de boîtes, vue en enfilade "
  "depuis le bout de l'allée. Aucune étiquette lisible."),
 ('panier-plein', 'images', P_EX, EPICERIE + " Un panier de magasinage en "
  "plastique posé au sol, à moitié plein : des légumes, une bouteille de lait, "
  "une boîte. Vu de trois quarts, de près."),
 ('balance-fruits', 'images', P_EX, EPICERIE + " Une balance de comptoir en gros "
  "plan, avec un sac de plastique transparent rempli de pommes posé dessus. "
  "Cadrage serré à hauteur de comptoir, le fond entièrement flou : aucun mur, "
  "aucune enseigne, aucun néon dans l'image. L'afficheur de la balance est "
  "allumé mais ses chiffres sont flous."),
 ('produits-entretien', 'images', P_EX, EPICERIE + " Une tablette entière de "
  "bouteilles de savon et de nettoyants colorés, vue de face, avec des "
  "rouleaux de papier essuie-tout au-dessus. Aucune étiquette lisible, aucune "
  "marque reconnaissable."),
 ('caisse-epicerie', 'images', P_EX, EPICERIE + " Le tapis roulant d'une caisse, "
  "vu de près, avec quelques articles dessus et le séparateur de plastique. "
  "L'écran de la caisse est flou à l'arrière-plan."),

 # ── Les douze photos du banc de vocabulaire ───────────────────────────
 ('circulaire', 'vocab', P_VOC, CUISINE + " Un dépliant publicitaire de papier "
  "journal, plié en deux sur la table, à côté d'une tasse. La grille de cases "
  "se devine, aucun mot ne se lit."),
 ('panier', 'vocab', P_VOC, EPICERIE + " Un panier de magasinage vide, en "
  "plastique rouge foncé, tenu à la main, sur fond d'allée floue."),
 ('allee', 'vocab', P_VOC, EPICERIE + " Une allée de magasin vue en enfilade, "
  "les tablettes des deux côtés qui filent vers le fond."),
 ('tablette', 'vocab', P_VOC, EPICERIE + " Gros plan sur une seule tablette de "
  "métal garnie de boîtes et de sacs de riz, vue de face, sans étiquette "
  "lisible."),
 ('liste', 'vocab', P_VOC, CUISINE + " Un petit carnet ouvert avec une courte "
  "liste manuscrite et un crayon posé à côté. L'écriture est nette comme forme "
  "mais illisible comme mots."),
 ('douzaine', 'vocab', P_VOC, CUISINE + " Une boîte de carton ouverte contenant "
  "douze œufs bruns, vue de trois quarts, posée sur la table."),
 ('kilo', 'vocab', P_VOC, EPICERIE + " Un sac de plastique transparent rempli de "
  "pommes rouges, posé sur le plateau d'une balance de comptoir."),
 ('etiquette', 'vocab', P_VOC, EPICERIE + " Macro sur un autocollant blanc collé "
  "sur un emballage de plastique : l'étiquette remplit le cadre, seul le "
  "code-barres est net et les lignes de caractères sont réduites à des traits "
  "gris. Le fond est entièrement flou, aucun emballage de marque "
  "reconnaissable."),
 ('affichette', 'vocab', P_VOC, EPICERIE + " Gros plan sur un petit carton de "
  "prix glissé dans un rail de tablette, vu de trois quarts très rasant, sa "
  "face imprimée presque parallèle à l'objectif, si bien qu'aucun caractère "
  "n'est déchiffrable. Aucun emballage lisible sur la tablette au-dessus."),
 ('litre', 'vocab', P_VOC, EPICERIE + " Un carton de lait d'un litre et une "
  "bouteille de jus, debout côte à côte sur une tablette réfrigérée. Aucune "
  "marque, aucun texte lisible."),
 ('savon-vaisselle', 'vocab', P_VOC, EPICERIE + " Une bouteille de savon à "
  "vaisselle liquide, sans étiquette lisible, posée au bord d'un évier de "
  "cuisine avec des bulles de mousse."),
 ('essuie-tout', 'vocab', P_VOC, CUISINE + " Un gros rouleau de papier "
  "essuie-tout blanc posé debout sur le comptoir, la première feuille "
  "légèrement déroulée."),
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
