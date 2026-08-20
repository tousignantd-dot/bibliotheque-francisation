#!/usr/bin/env python3
"""Génère les 21 images du module-achat via fal.ai (Nano Banana 2).

Deux destinations, deux formats :
  · `images/` — les illustrations d'exercice, 1024 px, telles que rendues ;
  · `vocab/`  — les photos du banc de vocabulaire, réduites à 800 px / q. 82.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-achat/gen_images.py
  python3 build/contenu/module-achat/gen_images.py tournoi balcon
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-achat'
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

STYLE = ("Photographie réaliste, format carré, lumière naturelle de jour, faible "
         "profondeur de champ. Rue ou transport en commun d'une ville québécoise "
         "ordinaire, palette sobre. Aucun texte lisible, aucune écriture, aucun logo, "
         "aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format carré, scène de la vie quotidienne au Québec "
        "avec une ou deux personnes vues de dos, de trois quarts ou hors cadrage du "
        "visage. Lumière naturelle douce, faible profondeur de champ. Aucun visage "
        "reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Dans le magasin"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit images d'exercice ────────────────────────────────────────
 ('rayon-laveuses', 'images', P_EX, STYLE + " Trois laveuses blanches alignées côte à "
  "côte sur une estrade basse, dans un grand magasin. Éclairage au plafond, plancher de "
  "béton poli. Aucune étiquette lisible."),
 ('etiquette-energie', 'images', P_EX, STYLE + " Gros plan sur une étiquette autocollante "
  "rectangulaire posée sur la porte d'un appareil blanc, montrant une échelle de barres "
  "colorées. Aucun chiffre ni texte lisible."),
 ('ruban-mesurer', 'images', P_EX, STYLE + " Un ruban à mesurer jaune déroulé sur le sol "
  "devant l'ouverture d'un petit local, avec un carnet et un crayon posés à côté. "
  "Graduations floues."),
 ('local-sous-sol', 'images', P_EX, STYLE + " Un petit local de sous-sol vide, murs de "
  "béton peints en blanc, deux tuyaux et un renvoi au sol, une prise électrique au mur. "
  "Éclairage d'ampoule nue."),
 ('camion-livraison', 'images', P_EX, STYLE + " Un camion de livraison blanc stationné "
  "devant une maison de banlieue, porte arrière ouverte, diable de transport posé sur le "
  "trottoir. Aucune inscription sur le camion."),
 ('boulons-arriere', 'images', P_EX, STYLE + " Gros plan sur l'arrière d'un appareil "
  "électroménager blanc, montrant quatre gros boulons alignés et une clé posée à côté. "
  "Métal et plastique bien visibles."),
 ('mode-emploi-appareil', 'images', P_EX, STYLE + " Un livret épais ouvert à plat sur une "
  "table, montrant des schémas techniques et des colonnes de texte. Les caractères "
  "restent flous et illisibles."),
 ('terminal-paiement', 'images', P_EX, STYLE + " Gros plan sur un terminal de paiement "
  "tenu au-dessus d'un comptoir de magasin, écran allumé mais illisible, clavier "
  "numérique visible."),

 # ── Les treize mots du banc de vocabulaire ────────────────────────────
 ('electromenager', 'vocab', P_VOC, STYLE + " Un rayon d'électroménagers vu en enfilade : "
  "réfrigérateurs, laveuses et cuisinières blancs alignés le long d'un mur de magasin. "
  "Aucune étiquette lisible."),
 ('laveuse', 'vocab', P_VOC, STYLE + " Une laveuse frontale blanche vue de face, porte "
  "ronde fermée, panneau de commandes en haut. Fond neutre, éclairage doux."),
 ('capacite', 'vocab', P_VOC, STYLE + " L'intérieur d'un tambour de laveuse ouvert, vu de "
  "face, avec quelques vêtements repliés à l'intérieur. Acier inoxydable perforé."),
 ('dimensions', 'vocab', P_VOC, STYLE + " Un ruban à mesurer tendu horizontalement contre "
  "la largeur d'un appareil blanc, tenu par deux mains. Graduations floues, visages hors "
  "cadre."),
 ('garantie', 'vocab', P_VOC, STYLE + " Une chemise de carton ouverte sur une table, "
  "contenant deux feuilles et une facture agrafée. Aucun texte lisible."),
 ('versement', 'vocab', P_VOC, STYLE + " Un calendrier mural de bureau où douze cases "
  "sont marquées d'un point, posé à côté d'une calculatrice. Aucun chiffre lisible."),
 ('livraison', 'vocab', P_VOC, PERS + " Deux personnes en vêtements de travail, vues de "
  "dos, descendent un gros appareil blanc d'un camion à l'aide d'un diable. Rue "
  "résidentielle."),
 ('installation', 'vocab', P_VOC, PERS + " Une personne accroupie derrière un appareil "
  "blanc écarté du mur, raccordant un tuyau. Boîte à outils ouverte au sol, visage hors "
  "cadre."),
 ('bon-livraison', 'vocab', P_VOC, STYLE + " Une planchette à pince tenant une feuille "
  "imprimée, posée sur le dessus d'un carton d'emballage, avec un stylo en travers. "
  "Aucun texte lisible."),
 ('boulon', 'vocab', P_VOC, STYLE + " Gros plan sur quatre gros boulons métalliques posés "
  "sur une feuille de papier blanc, à côté d'une clé. Filetage bien visible."),
 ('niveau', 'vocab', P_VOC, STYLE + " Gros plan sur un niveau à bulle posé sur le dessus "
  "d'un appareil blanc, la bulle centrée entre deux traits. Sans aucune inscription."),
 ('cycle', 'vocab', P_VOC, STYLE + " Gros plan sur le panneau de commandes d'une laveuse "
  "avec un cadran rotatif et des voyants, sans aucune inscription lisible."),
 ('tableau-problemes', 'vocab', P_VOC, STYLE + " Une double page de livret ouverte "
  "montrant un tableau à deux colonnes avec de nombreuses lignes horizontales. Les "
  "caractères restent flous et illisibles."),
]


def genere(prompt):
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": "1:1",
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + FAL, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.loads(r.read())
    with urllib.request.urlopen(d["images"][0]["url"], timeout=240) as r:
        return r.read()


def reduire(data, cote=800, qualite=82):
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien."""
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert('RGB')
    im = im.resize((cote, cote), Image.LANCZOS)
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
        "params": {"num_images": 1, "aspect_ratio": "1:1",
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
