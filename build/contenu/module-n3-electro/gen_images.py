#!/usr/bin/env python3
"""Génère les 23 images de module-n3-electro via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les huit illustrations de l'exercice 3 de « Je découvre » ;
  · `vocab/`  — les quinze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdrait le tiers du haut et du bas.

**La difficulté propre à ce module est que trois de ses objets sont du
papier** — la circulaire, l'affichette, le bon de livraison — alors que le
générateur a l'ordre de ne produire aucun texte lisible. Les prompts demandent
donc des papiers dont la *forme* est nette (colonnes, cases, gros chiffre au
milieu) sans qu'aucun mot ne se lise : l'élève reconnaît l'objet, et c'est
l'exercice qui en donne le contenu.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n3-electro/gen_images.py
  python3 build/contenu/module-n3-electro/gen_images.py circulaire-table
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n3-electro'
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
         "profondeur de champ. Intérieur d'un grand magasin d'électroménagers "
         "québécois ordinaire, palette sobre, planchers gris. Aucun texte "
         "lisible, aucune écriture, aucun logo, aucun filigrane, aucune "
         "personne identifiable.")

MAISON = ("Photographie réaliste, format paysage, intérieur d'un logement "
          "québécois ordinaire, lumière naturelle douce, faible profondeur de "
          "champ. Aucun texte lisible, aucun logo, aucun filigrane, aucune "
          "personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Dans le magasin des appareils"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit images d'exercice ────────────────────────────────────────
 ('rangee-laveuses', 'images', P_EX, STYLE + " Une rangée de laveuses blanches "
  "posées côte à côte sur le plancher du magasin, vues en enfilade, hublots "
  "ronds visibles."),
 ('refrigerateurs-alignes', 'images', P_EX, STYLE + " Plusieurs grands "
  "réfrigérateurs en acier inoxydable et en blanc, alignés contre un mur du "
  "magasin, portes fermées, vus de trois quarts."),
 ('circulaire-table', 'images', P_EX, MAISON + " Un dépliant publicitaire de "
  "magasin ouvert à plat sur une table de cuisine, à côté d'une tasse. La mise "
  "en page se devine — cases, photos d'appareils, gros chiffres — mais aucun "
  "mot ni aucun chiffre n'est lisible."),
 ('affichette-appareil', 'images', P_EX, STYLE + " Gros plan sur un petit "
  "carton rectangulaire posé sur un support, devant un électroménager blanc. "
  "Les lignes de texte apparaissent comme des traits gris, entièrement "
  "illisibles."),
 ('affiche-rayon', 'images', P_EX, STYLE + " La scène est prise sous une grande "
  "affiche suspendue au plafond au-dessus d'un rayon d'électroménagers : seules "
  "sa face inférieure et ses chaînes de suspension entrent dans le champ, "
  "l'affiche étant coupée par le bord haut du cadre. Aucune surface écrite "
  "visible."),
 ('ruban-mesurer', 'images', P_EX, MAISON + " Un ruban à mesurer jaune déroulé "
  "sur le plancher entre un mur et l'encadrement d'une porte, dans une cuisine "
  "vide. Les chiffres du ruban restent flous."),
 ('camion-livraison', 'images', P_EX, PERS + " Un camion de livraison blanc "
  "arrêté devant un immeuble à logements, hayon ouvert, une diable de "
  "transport posée à côté. Aucun logo sur le camion."),
 ('comptoir-caisse', 'images', P_EX, STYLE + " Un comptoir de caisse de grand "
  "magasin avec un terminal de paiement posé dessus, écran sombre. Aucune "
  "personne au premier plan."),

 # ── Les quatorze photos du banc de vocabulaire ────────────────────────
 ('laveuse', 'vocab', P_VOC, STYLE + " Une laveuse blanche à hublot rond, vue "
  "de face, seule devant un mur clair."),
 ('secheuse', 'vocab', P_VOC, MAISON + " Une sécheuse blanche à hublot rond, "
  "porte entrouverte, dans une buanderie de sous-sol avec un panier de linge."),
 ('refrigerateur', 'vocab', P_VOC, MAISON + " Un grand réfrigérateur en acier "
  "inoxydable, porte fermée, dans une cuisine ordinaire, vu de trois quarts."),
 ('cuisiniere', 'vocab', P_VOC, MAISON + " Une cuisinière blanche avec quatre "
  "ronds sur le dessus et un four en dessous, vue de face dans une cuisine."),
 ('micro-ondes', 'vocab', P_VOC, MAISON + " Un four à micro-ondes noir posé "
  "sur un comptoir de cuisine, porte fermée, vu de trois quarts."),
 ('aspirateur', 'vocab', P_VOC, MAISON + " Un aspirateur vertical posé sur un "
  "tapis de salon, manche relevé, vu de trois quarts."),
 ('ordinateur-portable', 'vocab', P_VOC, MAISON + " Un ordinateur portable "
  "ouvert sur une table de cuisine, écran éteint et sombre, à côté d'un "
  "cahier fermé."),
 ('circulaire', 'vocab', P_VOC, MAISON + " Un dépliant publicitaire de magasin "
  "ouvert sur une table et vu de biais, son bandeau de titre sortant du cadre "
  "par le haut : seules les cases de produits, avec leurs photos d'appareils, "
  "restent visibles. Aucun mot ni chiffre lisible."),
 ('prix-regulier', 'vocab', P_VOC, STYLE + " Gros plan sur un petit carton de "
  "prix devant un électroménager, où deux lignes de chiffres se devinent, "
  "l'une barrée. Les chiffres restent entièrement illisibles."),
 ('special', 'vocab', P_VOC, STYLE + " Un présentoir d'électroménagers "
  "surmonté d'un grand carton de couleur vive suspendu. Le lettrage est flou "
  "et illisible."),
 ('rayon', 'vocab', P_VOC, STYLE + " Une allée large d'un magasin "
  "d'électroménagers, appareils blancs alignés de chaque côté, plancher gris, "
  "vue en enfilade."),
 ('affichette', 'vocab', P_VOC, STYLE + " Gros plan sur un petit carton posé "
  "sur son support devant une laveuse blanche. Les lignes de texte sont des "
  "traits gris illisibles."),
 ('modele', 'vocab', P_VOC, STYLE + " Gros plan sur une petite plaque "
  "métallique collée à l'arrière d'un électroménager, avec des rangées de "
  "caractères flous et illisibles."),
 ('livraison', 'vocab', P_VOC, PERS + " Un camion de livraison blanc arrêté "
  "devant un immeuble, hayon ouvert, un gros appareil blanc emballé sur une "
  "diable de transport. Aucun logo."),
 ('bon-livraison', 'vocab', P_VOC, STYLE + " Gros plan en plongée sur un "
  "formulaire imprimé posé sur un comptoir de mélamine claire, mise en page en "
  "colonnes et cases, lignes de texte réduites à des traits gris. Rien d'autre "
  "n'entre dans le champ : aucun mur, aucune tablette, aucun présentoir."),
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
