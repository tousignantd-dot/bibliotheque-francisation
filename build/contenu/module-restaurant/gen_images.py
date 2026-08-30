#!/usr/bin/env python3
"""Génère les 21 images du module-restaurant via fal.ai (Nano Banana 2).

Deux destinations, deux formats :
  · `images/` — les illustrations d'exercice, 1024 px, telles que rendues ;
  · `vocab/`  — les photos du banc de vocabulaire, réduites à 800 px / q. 82.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-restaurant/gen_images.py
  python3 build/contenu/module-restaurant/gen_images.py tournoi balcon
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-restaurant'
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
         "profondeur de champ. Restaurant de quartier ou casse-croûte "
         "ordinaire au Québec, salle simple et un peu usée, palette sobre. "
         "Aucun texte lisible, aucune écriture, aucun logo, "
         "aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage 3:2, scène de la vie quotidienne au Québec "
        "avec une ou deux personnes vues de dos, de trois quarts ou hors cadrage du "
        "visage. Lumière naturelle douce, faible profondeur de champ. Aucun visage "
        "reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Au restaurant"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit images d'exercice ────────────────────────────────────────
 ('salle-manger', 'images', P_EX, STYLE + " Une salle à manger de restaurant de quartier "
  "vide avant le service : tables de bois dressées, chaises alignées, nappes claires, "
  "lumière du soir par une grande fenêtre."),
 ('ardoise-menu', 'images', P_EX, STYLE + " Une ardoise noire encadrée de bois, accrochée "
  "à un mur de brique, avec des traits de craie blanche formant des lignes. Aucun mot "
  "lisible."),
 ('table-deux', 'images', P_EX, STYLE + " Une petite table pour deux près d'une fenêtre, "
  "avec deux couverts dressés, deux verres et une petite bougie. Rue floue derrière la "
  "vitre."),
 ('assiette-plat', 'images', P_EX, STYLE + " Salle à manger d'un restaurant de quartier "
  "au Québec, table dressée. Plongée serrée sur une assiette blanche posée sur la "
  "table, avec un filet de poisson grillé, du riz et des légumes verts ; fourchette et "
  "couteau à côté. L'assiette remplit le cadre, l'arrière-plan réduit à un flou de "
  "salle — aucun siège, aucune fenêtre de véhicule."),
 ('carafe-eau', 'images', P_EX, STYLE + " Une carafe de verre remplie d'eau posée sur une "
  "table de restaurant, à côté de deux verres. Reflets de lumière sur le verre."),
 ('facture-table', 'images', P_EX, STYLE + " Une petite assiette ou un porte-addition de "
  "cuir posé sur une table, avec un papier plié dessus et un stylo. Aucun chiffre "
  "lisible."),
 ('terminal-pourboire', 'images', P_EX, STYLE + " Un terminal de paiement portatif tenu "
  "au-dessus d'une table de restaurant, écran allumé mais illisible, clavier visible."),
 ('comptoir-midi', 'images', P_EX, STYLE + " Un comptoir de restaurant vu de côté, avec "
  "des tabourets hauts alignés et une machine à café en arrière-plan. Lumière du midi."),

 # ── Les treize mots du banc de vocabulaire ────────────────────────────
 ('carte', 'vocab', P_VOC, STYLE + " Un menu de restaurant relié de cuir, ouvert à plat "
  "sur une table, montrant deux colonnes de lignes imprimées. Aucun caractère lisible."),
 ('menu-jour', 'vocab', P_VOC, STYLE + " Une petite ardoise posée sur un chevalet de bois "
  "sur une table de restaurant, avec quelques traits de craie. Aucun mot lisible."),
 ('table-hote', 'vocab', P_VOC, STYLE + " Table dressée d'un restaurant de quartier au "
  "Québec. Trois petites assiettes alignées — une soupe, un plat de viande et un "
  "dessert — vues de dessus, à la verticale, sur une nappe claire qui remplit tout le "
  "cadre. Aucun siège, aucune fenêtre, aucune tablette de véhicule."),
 ('entree', 'vocab', P_VOC, STYLE + " Un bol de soupe fumante posé sur une assiette, avec "
  "une cuillère à côté et un petit pain. Table de restaurant."),
 ('plat', 'vocab', P_VOC, STYLE + " Salle à manger d'un restaurant de quartier au "
  "Québec, table dressée, nappe blanche, chaise de bois. Une assiette de poulet avec "
  "pommes de terre et légumes, vue de trois quarts sur la nappe. Aucun siège de "
  "véhicule, aucune fenêtre d'autobus, aucune tablette : rien que la table du "
  "restaurant et un fond de salle flou."),
 ('plat-jour', 'vocab', P_VOC, STYLE + " Salle à manger d'un restaurant de quartier au "
  "Québec, table dressée, nappe claire. Un filet de truite grillée avec du riz et des "
  "légumes verts, dans une assiette blanche vue de dessus. L'assiette est posée sur "
  "une table, jamais sur un siège, un dossier, un rebord ou une tablette de véhicule."),
 ('carafe', 'vocab', P_VOC, STYLE + " Salle à manger d'un restaurant de quartier au "
  "Québec. Gros plan sur une carafe de verre transparente remplie d'eau, posée sur une "
  "table de bois dressée, deux verres à côté. Fond de salle flou — aucun siège de "
  "véhicule, aucune poignée suspendue, aucune rue derrière une vitre."),
 ('robinet', 'vocab', P_VOC, STYLE + " Un verre d'eau rempli au robinet d'un évier de "
  "cuisine, en gros plan, l'eau coulant encore."),
 ('accompagnement', 'vocab', P_VOC, STYLE + " Salle à manger d'un restaurant de "
  "quartier au Québec, table dressée, nappe claire, chaise de bois. Un petit bol de "
  "riz et un petit bol de légumes verts posés à côté d'une assiette principale. Tout "
  "repose sur la table du restaurant, jamais sur un siège, un rebord ou une tablette "
  "de véhicule."),
 ('addition', 'vocab', P_VOC, STYLE + " Un porte-addition de cuir noir ouvert sur une "
  "table, avec un papier plié à l'intérieur. Aucun chiffre lisible."),
 ('pourboire', 'vocab', P_VOC, STYLE + " Quelques billets et pièces de monnaie posés sur "
  "un porte-addition de cuir, sur une table de restaurant. Billets vus de biais, sans "
  "détail lisible."),
 ('taxes', 'vocab', P_VOC, STYLE + " Gros plan sur un ruban de caisse imprimé posé sur une "
  "table, montrant plusieurs lignes de chiffres flous et illisibles."),
 ('separement', 'vocab', P_VOC, STYLE + " Deux porte-additions de cuir posés côte à côte "
  "sur une table de restaurant, chacun avec son papier. Deux verres derrière."),
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
