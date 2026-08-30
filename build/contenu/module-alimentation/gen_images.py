#!/usr/bin/env python3
"""Génère les 21 images du module-alimentation via fal.ai (Nano Banana 2).

Deux destinations, deux formats :
  · `images/` — les illustrations d'exercice, 1024 px, telles que rendues ;
  · `vocab/`  — les photos du banc de vocabulaire, réduites à 800 px / q. 82.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-alimentation/gen_images.py
  python3 build/contenu/module-alimentation/gen_images.py tournoi balcon
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-alimentation'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
ENV  = pathlib.Path('/Users/danieltousignant/Claude/.env')


def cle(nom):
    for ligne in ENV.read_text(encoding='utf-8').splitlines():
        ligne = ligne.strip()
        if ligne.startswith(nom + '='):
            return ligne.split('=', 1)[1].strip().strip('"\'')
    return ''


FAL = cle('FAL_KEY')
if not FAL:
    sys.exit('FAL_KEY absente de ~/Claude/.env')

# Le décor est celui de CE module. La phrase « Rue ou transport en commun »
# qui tenait ici venait de module-deplacement, recopiée par erreur : le
# générateur la prenait au mot et servait les assiettes dans un autobus.
STYLE = ("Photographie réaliste, format paysage 3:2, lumière naturelle de jour, faible "
         "profondeur de champ. Épicerie de quartier ou cuisine d'un logement "
         "québécois ordinaire, palette sobre. "
         "Aucun texte lisible, aucune écriture, aucun logo, "
         "aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage 3:2, scène de la vie quotidienne au Québec "
        "avec une ou deux personnes vues de dos, de trois quarts ou hors cadrage du "
        "visage. Lumière naturelle douce, faible profondeur de champ. Aucun visage "
        "reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Où ça se trouve"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit lieux de l'épicerie (exercice 3) ─────────────────────────
 ('allee-conserves', 'images', P_EX, STYLE + " Une allée d'épicerie vue en enfilade : "
  "deux rangées d'étagères remplies de boîtes de conserve alignées, plancher de "
  "linoléum clair, éclairage au plafond. Les étiquettes des boîtes sont unies et sans "
  "aucune inscription."),
 ('comptoir-boucherie', 'images', P_EX, STYLE + " Un comptoir de boucherie d'épicerie : "
  "vitrine réfrigérée où sont disposées des pièces de viande rouge et de volaille sur "
  "des plateaux, balance blanche posée sur le comptoir. Aucune personne."),
 ('comptoir-poisson', 'images', P_EX, STYLE + " Un comptoir de poissonnerie : filets de "
  "poisson disposés sur un lit de glace pilée derrière une vitre, avec des pinces "
  "métalliques posées à côté. Éclairage froid."),
 ('fruits-legumes', 'images', P_EX, STYLE + " Le rayon des fruits et légumes d'une "
  "épicerie : bacs inclinés remplis de pommes, d'oranges, de poivrons et de laitues, "
  "sous un éclairage vif. Sacs de plastique sur un rouleau au bout du bac."),
 ('produits-entretien', 'images', P_EX, STYLE + " Une allée de produits d'entretien : "
  "bouteilles de plastique de différentes tailles et couleurs alignées sur trois "
  "tablettes, sans aucune étiquette lisible. Plancher clair."),
 ('etiquette-dos', 'images', P_EX, STYLE + " Gros plan sur le dos d'une boîte de conserve "
  "tenue de côté, montrant un tableau imprimé en noir sur fond blanc, encadré, avec des "
  "lignes régulières. Les caractères restent flous et illisibles."),
 ('frigo-bas', 'images', P_EX, STYLE + " L'intérieur d'un réfrigérateur ouvert, vu de "
  "face : trois tablettes de verre, un tiroir à légumes en bas, quelques contenants de "
  "plastique fermés. Lumière intérieure allumée."),
 ('balance', 'images', P_EX, STYLE + " Gros plan sur une balance de comptoir d'épicerie, "
  "plateau d'acier inoxydable, écran numérique éteint et illisible. Papier d'emballage "
  "blanc à côté."),

 # ── Les treize mots du banc de vocabulaire ────────────────────────────
 ('allee', 'vocab', P_VOC, STYLE + " Une allée d'épicerie vide vue de bout en bout, "
  "étagères de chaque côté remplies de boîtes et de sacs unis, sans aucune écriture. "
  "Perspective centrale."),
 ('etiquette', 'vocab', P_VOC, STYLE + " Gros plan sur une petite étiquette de prix "
  "blanche collée sur le rebord d'une tablette d'épicerie. Elle ne porte aucun chiffre "
  "ni texte lisible."),
 ('valeur-nutritive', 'vocab', P_VOC, STYLE + " Gros plan sur un tableau imprimé en noir "
  "et blanc au dos d'un emballage de carton : un cadre rectangulaire avec des lignes "
  "horizontales régulières. Aucun caractère lisible."),
 ('conserve', 'vocab', P_VOC, STYLE + " Trois boîtes de conserve de métal posées sur une "
  "tablette de garde-manger, étiquettes de papier uni sans aucune inscription. "
  "Éclairage doux d'intérieur."),
 ('comptoir', 'vocab', P_VOC, STYLE + " Un comptoir de service d'épicerie vu de face : "
  "vitrine réfrigérée basse, dessus d'acier inoxydable, rouleau de papier d'emballage "
  "et balance. Aucune personne."),
 ('livre', 'vocab', P_VOC, STYLE + " Gros plan en plongée sur une balance de cuisine "
  "numérique portant un morceau de viande emballé dans du papier blanc. L'écran est "
  "éteint et illisible."),
 ('boeuf-hache', 'vocab', P_VOC, STYLE + " Gros plan sur un plateau de bœuf haché frais "
  "recouvert d'une pellicule transparente, posé sur un comptoir de cuisine. Texture bien "
  "visible."),
 ('congeler', 'vocab', P_VOC, STYLE + " L'intérieur d'un tiroir de congélateur ouvert, "
  "avec trois sacs de plastique refermables contenant des aliments, couverts d'une fine "
  "couche de givre. Aucune inscription."),
 ('date', 'vocab', P_VOC, STYLE + " Gros plan sur le dessus d'un contenant de plastique "
  "de produit laitier, où une zone imprimée est visible mais floue et illisible. "
  "Éclairage de réfrigérateur."),
 ('mode-emploi', 'vocab', P_VOC, STYLE + " Gros plan sur l'arrière d'une bouteille de "
  "produit nettoyant, montrant trois blocs de texte séparés par des filets. Les "
  "caractères restent flous et illisibles."),
 ('diluer', 'vocab', P_VOC, STYLE + " Un seau de plastique rempli d'eau posé sur un "
  "plancher de céramique, à côté d'une bouteille de nettoyant avec son bouchon doseur "
  "dévissé. Aucune étiquette lisible."),
 ('avertissement', 'vocab', P_VOC, STYLE + " Gros plan sur un pictogramme triangulaire "
  "noir sur fond jaune, imprimé sur une bouteille de plastique blanche. Aucun texte "
  "autour, seulement le symbole."),
 ('produit-entretien', 'vocab', P_VOC, STYLE + " Trois bouteilles de produits d'entretien "
  "de tailles différentes, alignées sous un évier de cuisine, portes ouvertes. "
  "Étiquettes unies, sans inscription."),
]


def genere(prompt):
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": "3:2",
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + FAL, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.loads(r.read())
    with urllib.request.urlopen(d["images"][0]["url"], timeout=240) as r:
        return r.read()


def reduire(data, cote=800, qualite=82):
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien.

    En 3:2, comme le gabarit qui les affiche — `.imgzone`, `.imgtile` et
    `.vc-photo` sont tous en `aspect-ratio:3/2`. Redimensionner en carré
    faisait recadrer d'un tiers à l'affichage, et c'était le sujet qui
    partait."""
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert('RGB')
    im = im.resize((cote, round(cote * 2 / 3)), Image.LANCZOS)
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
        "params": {"num_images": 1, "aspect_ratio": "3:2",
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

print('\n%d générées, %d déjà présentes, %d en échec'
      % (len(faits), len(sautes), len(echecs)))
for e in echecs:
    print('  ✗ ' + e)
print('coût estimé : %.2f $' % (len(faits) * 0.034))
