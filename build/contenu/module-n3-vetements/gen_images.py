#!/usr/bin/env python3
"""Génère les 22 images de module-n3-vetements via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les huit illustrations de l'exercice 3 de « Je découvre » ;
  · `vocab/`  — les quatorze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdrait le tiers du haut et du bas.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n3-vetements/gen_images.py
  python3 build/contenu/module-n3-vetements/gen_images.py cabine-essayage
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n3-vetements'
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
         "profondeur de champ. Intérieur d'un magasin de vêtements québécois "
         "ordinaire, palette sobre. Aucun texte lisible, aucune écriture, "
         "aucun logo, aucun filigrane, aucune personne identifiable.")

MAISON = ("Photographie réaliste, format paysage, intérieur d'un logement "
          "québécois ordinaire, lumière naturelle douce, faible profondeur de "
          "champ. Aucun texte lisible, aucun logo, aucun filigrane, aucune "
          "personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Dans le magasin de linge"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit images d'exercice ────────────────────────────────────────
 ('manteaux-suspendus', 'images', P_EX, STYLE + " Une longue rangée de manteaux "
  "d'hiver accrochés à des cintres sur un présentoir métallique, vus en enfilade. "
  "Couleurs sombres et sobres, tissus mats."),
 ('cabine-essayage', 'images', P_EX, STYLE + " Une cabine d'essayage fermée par un "
  "rideau de tissu épais, entrouvert, avec un petit banc et un miroir à l'intérieur. "
  "Vue de face, dans un couloir de magasin."),
 ('etiquette-taille', 'images', P_EX, STYLE + " Gros plan sur une petite étiquette "
  "cousue à l'intérieur du col d'un manteau, tenue entre deux doigts. Le lettrage "
  "reste flou et illisible."),
 ('affiche-rabais', 'images', P_EX, STYLE + " Une grande affiche cartonnée suspendue "
  "au-dessus d'un présentoir de vêtements, coupée par le bord haut de l'image : seule "
  "sa bordure inférieure et sa tranche paraissent au-dessus du présentoir, la face "
  "écrite hors du cadre. Aucune inscription, aucun lettrage, aucun chiffre visible "
  "nulle part dans l'image."),
 ('etiquette-prix-reduit', 'images', P_EX, STYLE + " Gros plan sur un petit carton de "
  "prix attaché par une ficelle à la manche d'un manteau. Deux lignes de chiffres y "
  "sont visibles comme des traits gris, entièrement illisibles."),
 ('pictogrammes-entretien', 'images', P_EX, STYLE + " Gros plan sur une étiquette de "
  "tissu blanc cousue dans le col d'un chandail, portant une rangée de petits "
  "symboles noirs — un bassin, un carré, un triangle, un fer. Aucun mot lisible."),
 ('secheuse-buanderie', 'images', P_EX, MAISON + " Une sécheuse blanche à hublot rond, "
  "porte entrouverte, dans une buanderie de sous-sol avec un panier de linge posé "
  "à côté."),
 ('terminal-paiement', 'images', P_EX, STYLE + " Un terminal de paiement posé sur un "
  "comptoir de caisse de magasin de vêtements, clavier et écran visibles. L'écran "
  "reste sombre et illisible. Aucune personne au premier plan."),

 # ── Les quatorze photos du banc de vocabulaire ────────────────────────
 ('manteau', 'vocab', P_VOC, STYLE + " Un manteau d'hiver bleu foncé matelassé, "
  "suspendu seul à un cintre devant un mur clair, vu de face."),
 ('tuque', 'vocab', P_VOC, STYLE + " Une tuque de laine grise à côtes, posée à plat "
  "sur une table de bois clair, vue de trois quarts."),
 ('chandail', 'vocab', P_VOC, STYLE + " Un chandail de laine beige plié sur une "
  "tablette de magasin, à côté de deux autres chandails unis."),
 ('bottes', 'vocab', P_VOC, STYLE + " Une paire de bottes d'hiver brunes, doublées, "
  "posées côte à côte sur un plancher de bois."),
 ('raye', 'vocab', P_VOC, STYLE + " Gros plan sur un chandail à rayures horizontales "
  "de deux couleurs, plié, à côté d'un chandail uni. Aucun lettrage."),
 ('taille', 'vocab', P_VOC, STYLE + " Gros plan sur l'intérieur d'un col de chandail "
  "où pend une petite étiquette de tissu. Le lettrage reste flou et illisible."),
 ('cabine', 'vocab', P_VOC, STYLE + " L'intérieur d'une cabine d'essayage vide : "
  "miroir, crochets au mur, petit banc, rideau tiré."),
 ('cintre', 'vocab', P_VOC, STYLE + " Trois cintres de bois vides accrochés à une "
  "tringle métallique, en gros plan, arrière-plan flou."),
 ('rabais', 'vocab', P_VOC, STYLE + " Un présentoir de vêtements surmonté d'un grand "
  "carton de couleur vive suspendu. Le lettrage est flou et illisible."),
 ('etiquette-prix', 'vocab', P_VOC, STYLE + " Un petit carton de prix attaché par une "
  "ficelle blanche à un vêtement, tenu entre deux doigts. Chiffres illisibles."),
 ('liquidation', 'vocab', P_VOC, STYLE + " Un bac de magasin rempli de vêtements pêle-mêle, "
  "avec un panneau de carton planté dedans. Le lettrage est flou et illisible."),
 ('etiquette-entretien', 'vocab', P_VOC, STYLE + " Gros plan sur une étiquette de tissu "
  "blanche cousue dans un vêtement, portant quatre petits symboles noirs alignés. "
  "Aucun mot lisible."),
 ('secheuse', 'vocab', P_VOC, MAISON + " Une sécheuse blanche à hublot rond, vue de "
  "face, dans une buanderie de sous-sol."),
 ('facture', 'vocab', P_VOC, PERS + " Un reçu de caisse tenu entre deux doigts devant "
  "un arrière-plan flou de magasin de vêtements. Lignes de texte illisibles."),
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
