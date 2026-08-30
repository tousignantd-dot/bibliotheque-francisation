#!/usr/bin/env python3
"""Génère les 14 images de module-n1-presenter via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations d'exercice, telles que rendues ;
  · `vocab/`  — les huit photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage**, et non plus carré : la zone de glisser-déposer mesure
223 x 132 px, un rapport de 1,7. Une image carrée y était recadrée et perdait
le tiers du haut et du bas. Voir `docs/chantier-tous-niveaux.md`.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n1-presenter/gen_images.py
  python3 build/contenu/module-n1-presenter/gen_images.py carte-monde
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n1-presenter'
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
         "profondeur de champ. Intérieur d'un centre de formation pour adultes "
         "au Québec, palette sobre et claire. Aucun texte lisible, aucune "
         "écriture, aucun logo, aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Les mots du premier jour"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images d'exercice ─────────────────────────────────────────
 ('formulaire', 'images', P_EX, STYLE + " Gros plan sur un formulaire de papier posé "
  "sur une table, avec un stylo à côté. Des cases vides sont visibles, mais les mots "
  "imprimés restent flous et illisibles."),
 ('accueil-centre', 'images', P_EX, STYLE + " Le comptoir d'accueil d'un centre de "
  "formation : un comptoir clair, un ordinateur, quelques chaises en attente. Personne "
  "au premier plan."),
 ('carte-monde', 'images', P_EX, STYLE + " Une carte du monde affichée au mur d'une "
  "salle de classe, vue de trois quarts. Les noms de pays restent flous et illisibles."),
 ('salle-classe', 'images', P_EX, STYLE + " Une salle de classe d'adultes, vide : des "
  "tables en rangées, un tableau blanc, une fenêtre à gauche."),
 ('poignee-main', 'images', P_EX, PERS + " Deux personnes se serrent la main, cadrées "
  "sur les mains et les avant-bras seulement, dans un couloir clair."),
 ('porte-appartement', 'images', P_EX, STYLE + " Une porte d'appartement dans un couloir "
  "d'immeuble, avec une petite plaque de numéro à côté. Le chiffre reste flou."),

 # ── Les huit photos du banc de vocabulaire ────────────────────────────
 ('nom', 'vocab', P_VOC, STYLE + " Une étiquette de nom vierge, en papier blanc, posée "
  "sur une table de bois clair. Aucune écriture dessus."),
 ('epeler', 'vocab', P_VOC, STYLE + " Des lettres magnétiques en plastique alignées sur "
  "un tableau blanc, vues de près. Les lettres sont nettes mais ne forment aucun mot "
  "reconnaissable."),
 ('adresse', 'vocab', P_VOC, STYLE + " Gros plan sur un numéro civique de métal à trois "
  "chiffres, vissé sur le mur de brique à côté de la porte d'entrée d'une maison, "
  "extérieur de jour. Les chiffres sont le seul sujet net ; aucune boîte aux lettres, "
  "aucune plaque, aucun objet portant une inscription dans le champ."),
 ('pays', 'vocab', P_VOC, STYLE + " Un globe terrestre posé sur une table, vu de près. "
  "Les noms de pays sont flous et illisibles."),
 ('langue', 'vocab', P_VOC, STYLE + " Deux gros livres épais empilés sur une table de "
  "classe, vus de trois quarts avant, tranches de pages vers l'objectif et dos tournés à "
  "l'opposé. Aucune couverture ni aucun dos visible ; aucune étiquette, aucun nom "
  "d'éditeur dans le champ."),
 ('enfant', 'vocab', P_VOC, PERS + " Un adulte et un enfant marchent main dans la main "
  "sur un trottoir, vus de dos."),
 ('metier', 'vocab', P_VOC, STYLE + " Des outils de travail posés côte à côte sur un "
  "établi : une clé, un tournevis, des gants de travail."),
 ('bonjour', 'vocab', P_VOC, PERS + " Une personne vue de dos ouvre une porte vitrée "
  "pleine, la main levée en signe de salut. La vitrine et son enseigne sont entièrement "
  "hors cadre à droite ; aucun lettrage sur le verre, aucune affiche dans le champ."),
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
