#!/usr/bin/env python3
"""Génère les 19 images de module-n3-epicerie via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les huit illustrations d'exercice, telles que rendues ;
  · `vocab/`  — les onze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage**, et non plus carré : la zone de glisser-déposer mesure
223 x 132 px, un rapport de 1,7. Une image carrée y était recadrée et perdait
le tiers du haut et du bas. Voir `docs/chantier-tous-niveaux.md`.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n3-epicerie/gen_images.py
  python3 build/contenu/module-n3-epicerie/gen_images.py circulaire-ouverte
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n3-epicerie'
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
         "profondeur de champ. Intérieur d'une épicerie québécoise ordinaire, "
         "palette sobre. Aucun texte lisible, aucune écriture, aucun logo, "
         "aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Dans l'épicerie"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit images d'exercice ────────────────────────────────────────
 ('allee-numerotee', 'images', P_EX, STYLE + " Vue en enfilade d'une allée d'épicerie "
  "bordée de tablettes garnies, avec un grand panneau suspendu au bout de la rangée "
  "portant un chiffre. Le chiffre reste flou et illisible."),
 ('affichette-rayon', 'images', P_EX, STYLE + " Un panneau d'allée suspendu au-dessus "
  "d'une allée, vu d'en dessous en légère contre-plongée, portant uniquement un grand "
  "chiffre peint : aucune ligne de texte sous le chiffre, aucune liste de catégories. "
  "Tablettes garnies en arrière-plan."),
 ('circulaire-ouverte', 'images', P_EX, STYLE + " Un dépliant publicitaire de papier ouvert "
  "à plat sur une table de cuisine, montrant une grille de photos de produits et de "
  "pastilles de prix. Tous les chiffres et tous les mots restent flous et illisibles."),
 ('caisse-tapis', 'images', P_EX, STYLE + " Un comptoir de caisse d'épicerie avec un tapis "
  "roulant noir sur lequel sont posés quelques articles, et un terminal de paiement. "
  "Aucune personne au premier plan."),
 ('pictogramme-poison', 'images', P_EX, STYLE + " Gros plan sur une bouteille de plastique "
  "de produit nettoyant posée sur un comptoir, avec une étiquette portant un pictogramme "
  "d'avertissement en losange, noir sur blanc. Les mots de l'étiquette restent illisibles."),
 ('balance-fruits', 'images', P_EX, STYLE + " Une balance suspendue au-dessus d'un étal de "
  "fruits et légumes, avec un sac de pommes posé dessus. Cadran flou."),
 ('sacs-reutilisables', 'images', P_EX, STYLE + " Trois sacs d'épicerie réutilisables en "
  "tissu épais, pliés et posés debout sur un comptoir clair. Couleurs sobres, aucun "
  "logo ni lettrage."),
 ('facture-epicerie', 'images', P_EX, STYLE + " Un long ruban de papier de caisse posé sur "
  "une table de bois, légèrement enroulé au bout. Les lignes de texte sont visibles comme "
  "des traits gris, entièrement illisibles."),

 # ── Les onze photos du banc de vocabulaire ────────────────────────────
 ('allee', 'vocab', P_VOC, STYLE + " Une allée d'épicerie vide vue de face, tablettes "
  "garnies des deux côtés, plancher de béton poli qui fuit vers le fond."),
 ('affichette', 'vocab', P_VOC, STYLE + " Un panneau de signalisation suspendu au plafond "
  "d'une épicerie, vu de trois quarts, avec des tablettes floues derrière. Lettrage "
  "illisible."),
 ('tablette', 'vocab', P_VOC, STYLE + " Gros plan sur trois niveaux de tablettes garnies de "
  "boîtes et de sacs de formats différents, les plus gros en bas."),
 ('panier', 'vocab', P_VOC, STYLE + " Un panier d'épicerie de plastique rouge tenu à la "
  "main, contenant trois articles, dans une allée floue."),
 ('circulaire', 'vocab', P_VOC, STYLE + " Un dépliant publicitaire plié en deux, posé sur "
  "le comptoir d'une cuisine à côté d'une tasse. Photos de produits visibles, texte "
  "illisible."),
 ('paquet', 'vocab', P_VOC, STYLE + " Un paquet de pâtes en plastique transparent posé sur "
  "un comptoir clair, vu de trois quarts. Aucune marque ni lettrage."),
 ('conserve', 'vocab', P_VOC, STYLE + " Deux boîtes de conserve en métal posées côte à côte "
  "sur une tablette, étiquettes unies sans écriture."),
 ('mise-en-garde', 'vocab', P_VOC, STYLE + " Gros plan sur le losange d'avertissement d'une "
  "étiquette de produit d'entretien : pictogramme noir sur fond blanc, contour épais. "
  "Aucun mot lisible."),
 ('caisse', 'vocab', P_VOC, STYLE + " Cadrage rapproché sur le tapis roulant d'une caisse "
  "d'épicerie et quelques articles en emballage neutre sans étiquette. Aucune enseigne, "
  "aucun sac imprimé, aucun personnel dans le champ : seules deux mains hors mise au "
  "point poussent un article."),
 ('facture', 'vocab', P_VOC, STYLE + " Un reçu de caisse tenu entre deux doigts, en gros "
  "plan, devant un arrière-plan flou de magasin. Lignes de texte illisibles."),
 ('sac', 'vocab', P_VOC, PERS + " Une personne vue de dos qui porte deux sacs d'épicerie "
  "réutilisables en tissu, sur un trottoir de quartier."),
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
