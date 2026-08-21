#!/usr/bin/env python3
"""Génère les 24 images de module-n3-restaurant via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les huit illustrations de l'exercice 3 de « Je découvre » ;
  · `vocab/`  — les seize photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdrait le tiers du haut et du bas.

**La difficulté propre à ce module est que son objet central est un
tableau écrit** — le menu au-dessus de la caisse —, alors que le générateur a
l'ordre de ne produire aucun texte lisible. Les prompts demandent donc des
panneaux dont la *forme* est nette : colonnes, lignes régulières, prix alignés
à droite, sans qu'aucun mot ne se lise. L'élève reconnaît l'objet ; c'est
l'exercice qui en donne le contenu.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n3-restaurant/gen_images.py
  python3 build/contenu/module-n3-restaurant/gen_images.py trois-formats
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n3-restaurant'
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
         "profondeur de champ. Intérieur d'un petit casse-croûte québécois "
         "ordinaire : comptoir de stratifié, tabourets, murs clairs, palette "
         "sobre. Aucun texte lisible, aucune écriture, aucun logo, aucun "
         "filigrane, aucune personne identifiable.")

TABLE = ("Photographie réaliste, format paysage, gros plan sur une table ou un "
         "plateau de casse-croûte, lumière naturelle douce, faible profondeur "
         "de champ. Aucun texte lisible, aucun logo, aucun filigrane, aucune "
         "personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Dans le casse-croûte"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit images d'exercice ────────────────────────────────────────
 ('file-comptoir', 'images', P_EX, PERS + " Trois personnes debout en file "
  "devant un comptoir de casse-croûte, vues de dos, plateaux vides à la main. "
  "L'arrière-plan du comptoir est net, aucun panneau lisible."),
 ('tableau-menu-haut', 'images', P_EX, STYLE + " Vue en contre-plongée d'un "
  "grand panneau de menu accroché au mur, au-dessus d'une caisse. Trois "
  "colonnes de lignes régulières avec des prix alignés à droite ; le lettrage "
  "est flou et entièrement illisible."),
 ('plateau-repas', 'images', P_EX, TABLE + " Un plateau de plastique brun posé "
  "sur une table, avec un sandwich coupé en deux dans un papier, un bol de "
  "soupe fumante et un verre de jus."),
 ('bac-ustensiles', 'images', P_EX, STYLE + " Gros plan sur trois bacs de "
  "plastique ouverts posés sur un comptoir, remplis de fourchettes, de "
  "couteaux et de cuillères en acier, manches vers le haut."),
 ('sachets-condiments', 'images', P_EX, TABLE + " Gros plan sur une poignée de "
  "petits sachets de condiments — sel, poivre, ketchup, moutarde — éparpillés "
  "sur un comptoir clair. Les sachets sont unis, sans aucune inscription."),
 ('trois-formats', 'images', P_EX, TABLE + " Trois verres de carton vides posés "
  "côte à côte sur un comptoir, du plus petit au plus grand, vus de face, sans "
  "aucune inscription sur le carton."),
 ('sac-emporter', 'images', P_EX, TABLE + " Un sac de papier brun ouvert posé "
  "sur un comptoir, un contenant de soupe fermé d'un couvercle blanc qui "
  "dépasse du haut. Le papier est uni, sans aucune impression."),
 ('recu-numero', 'images', P_EX, TABLE + " Gros plan sur un petit reçu de "
  "papier blanc posé sur un comptoir, à côté d'un plateau. Les lignes "
  "d'impression sont des traits gris entièrement illisibles."),

 # ── Les seize photos du banc de vocabulaire ───────────────────────────
 ('casse-croute', 'vocab', P_VOC, STYLE + " Vue d'ensemble d'une petite salle "
  "de casse-croûte vide : comptoir au fond, quelques tables et chaises, "
  "fenêtre à gauche."),
 ('comptoir', 'vocab', P_VOC, STYLE + " Un long comptoir de service vu de "
  "trois quarts, surface claire, caisse enregistreuse au bout, tabourets "
  "devant."),
 ('tableau-menu', 'vocab', P_VOC, STYLE + " Un panneau de menu accroché au mur "
  "derrière un comptoir, deux colonnes de lignes régulières et une colonne de "
  "prix à droite. Le lettrage est flou et illisible."),
 ('plateau', 'vocab', P_VOC, TABLE + " Une pile de plateaux de plastique brun "
  "empilés au bout d'un comptoir, vus de trois quarts."),
 ('format', 'vocab', P_VOC, TABLE + " Trois contenants de soupe de carton "
  "blanc, du plus petit au plus grand, alignés sur un comptoir, couvercles "
  "posés dessus, sans aucune inscription."),
 ('portion', 'vocab', P_VOC, TABLE + " Un bol de soupe rempli à ras bord posé "
  "sur une table, cuillère appuyée sur le bord."),
 ('breuvage', 'vocab', P_VOC, TABLE + " Un verre de jus d'orange, une tasse de "
  "café et un petit carton de lait posés côte à côte sur un comptoir clair, "
  "aucune inscription visible."),
 ('accompagnement', 'vocab', P_VOC, TABLE + " Une assiette avec une petite "
  "salade verte d'un côté et une portion de frites de l'autre, vue de dessus."),
 ('trio', 'vocab', P_VOC, TABLE + " Un plateau avec un sandwich dans son "
  "papier, une portion de frites et un verre de boisson, disposés ensemble, "
  "vus de trois quarts."),
 ('caisse', 'vocab', P_VOC, STYLE + " Gros plan sur une caisse enregistreuse "
  "posée au bout d'un comptoir, avec un terminal de paiement à côté, écran "
  "sombre."),
 ('pour-emporter', 'vocab', P_VOC, PERS + " Une main tenant un sac de papier "
  "brun fermé par le haut, sur le trottoir devant une vitrine. Le sac est uni, "
  "sans impression."),
 ('numero-commande', 'vocab', P_VOC, TABLE + " Gros plan sur un petit reçu de "
  "papier tenu entre deux doigts au-dessus d'un comptoir. Les lignes "
  "d'impression sont grises et illisibles."),
 ('ustensile', 'vocab', P_VOC, TABLE + " Gros plan sur une fourchette, un "
  "couteau et une cuillère en acier posés côte à côte sur une serviette de "
  "papier blanche."),
 ('serviette-table', 'vocab', P_VOC, TABLE + " Un distributeur de métal posé "
  "sur une table, rempli de serviettes de papier blanches dont quelques-unes "
  "dépassent."),
 ('condiment', 'vocab', P_VOC, TABLE + " Une salière, une poivrière et deux "
  "bouteilles souples posées ensemble au bout d'un comptoir. Les bouteilles "
  "sont unies, sans aucune étiquette."),
 ('couvercle', 'vocab', P_VOC, TABLE + " Gros plan sur un contenant de soupe "
  "de carton blanc dont on pose le couvercle de plastique, vu de trois quarts, "
  "aucune inscription."),
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
