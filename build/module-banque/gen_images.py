#!/usr/bin/env python3
"""Génère les 6 images du module-banque via fal.ai (Nano Banana 2).

Même recette que build/module-probleme/gen_images.py : une image à la fois,
journal .json adjacent dans ~/Claude/generations, puis copie vers le module.
Relançable : une image déjà présente dans le module est sautée.

Les scènes bancaires sont pleines d'écriture (montants, enseignes, écrans).
Chaque prompt exige donc explicitement l'absence de texte lisible : un chiffre
inventé sur un relevé serait un fait que le module n'a jamais énoncé.
"""
import json, pathlib, sys, time, urllib.request, urllib.error

GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
DEST = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/module-banque/images')
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

STYLE = ("Photographie réaliste, format carré, lumière naturelle douce, faible "
         "profondeur de champ. Palette sobre et froide. Aucun texte lisible, "
         "aucun chiffre lisible, aucune écriture nette, aucun logo, aucune "
         "marque, aucun filigrane.")

PAGE = "Je découvre · Exercice 5 — Associer l'image à l'opération"

IMAGES = [
 ('guichet', PAGE, STYLE + " Une femme d'une trentaine d'années, vue de trois quarts "
  "arrière, retire de l'argent à un guichet automatique encastré dans un mur, dans le "
  "hall vitré d'une institution financière. Sa main est sur le clavier, quelques billets "
  "sortent de la fente. L'écran est flou et sans texte lisible."),
 ('comptoir', PAGE, STYLE + " Une conseillère d'une quarantaine d'années, chemisier "
  "sobre, reçoit un client assis en face d'elle à un comptoir de bureau clair. Un écran "
  "d'ordinateur de dos, un dossier ouvert entre eux. Les deux personnes discutent "
  "calmement. Aucun document lisible."),
 ('terminal', PAGE, STYLE + " Gros plan sur les mains d'un client qui approche une carte "
  "de paiement d'un terminal de point de vente noir, sur le comptoir de bois d'un petit "
  "commerce. L'écran du terminal est allumé mais flou, sans texte lisible. La carte est "
  "unie, sans logo ni numéro."),
 ('application', PAGE, STYLE + " Gros plan sur les mains d'une femme assise à une table "
  "de cuisine, qui consulte une application bancaire sur son téléphone. L'écran montre "
  "une interface épurée floue — des barres et des cercles de couleur — sans aucun texte "
  "ni chiffre lisible. Une tasse de café à côté."),
 ('releve', PAGE, STYLE + " Gros plan en plongée sur les mains d'un homme qui tient une "
  "feuille imprimée à en-tête, posée sur une table de bois. Le document ressemble à un "
  "relevé bancaire : des lignes de texte gris uniformément floues et illisibles, aucun "
  "chiffre net. Un stylo posé à côté."),
 ('comptant', PAGE, STYLE + " Gros plan sur les mains d'une caissière qui compte des "
  "billets de banque dans un tiroir-caisse ouvert, où sont aussi rangées des pièces de "
  "monnaie. Les billets sont de couleurs claires, sans motif ni chiffre reconnaissable, "
  "sans aucun texte lisible."),
]

def genere(prompt):
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": "1:1",
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + FAL, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.loads(r.read())
    url = d["images"][0]["url"]
    with urllib.request.urlopen(url, timeout=180) as r:
        return r.read()

GEN.mkdir(parents=True, exist_ok=True)
DEST.mkdir(parents=True, exist_ok=True)
horodatage = time.strftime('%Y%m%d-%H%M%S')
faits, sautes, echecs = [], [], []

for nom, page, prompt in IMAGES:
    cible = DEST / (nom + '.jpg')
    if cible.exists() and cible.stat().st_size > 1000:
        sautes.append(nom); continue
    try:
        data = genere(prompt)
    except urllib.error.HTTPError as e:
        echecs.append('%s : HTTP %s %s' % (nom, e.code, e.read()[:180])); continue
    except Exception as e:
        echecs.append('%s : %s' % (nom, e)); continue

    base = 'module-banque_%s_%s' % (nom, horodatage)
    (GEN / (base + '.jpg')).write_bytes(data)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "fal-ai/nano-banana-2",
        "prompt": prompt,
        "refs": [],
        "params": {"num_images": 1, "aspect_ratio": "1:1",
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": "fal.ai",
        "cost_estimate_usd": 0.034,
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation",
        "module": "module-banque",
        "page": page,
        "destination": "assets/interactive/module-banque/images/%s.jpg" % nom,
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(nom)
    print('  ✓ %-16s %6.1f Ko' % (nom, len(data) / 1024), flush=True)

print('\n%d générées, %d déjà présentes, %d en échec' % (len(faits), len(sautes), len(echecs)))
for e in echecs:
    print('  ✗ ' + e)
print('coût estimé : %.2f $' % (len(faits) * 0.034))
