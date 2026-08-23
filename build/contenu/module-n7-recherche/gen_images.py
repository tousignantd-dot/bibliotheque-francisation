#!/usr/bin/env python3
"""Génère les 15 images de module-n7-recherche via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer ;
  · `vocab/`  — les neuf photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Voir `docs/chantier-tous-niveaux.md`.

La précaution vaut ici autant qu'au module de l'actualité, et pour la même
raison : le sujet est le monde du travail écrit — offres punaisées, curriculum
vitæ sur une table, écrans de recherche. Presque chaque image contient donc du
papier ou un écran. Chaque prompt exige que toute ligne de texte soit réduite
à un trait gris. Une image où l'on peut lire un mot — surtout un mot
d'anglais — est à refaire.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n7-recherche/gen_images.py
  python3 build/contenu/module-n7-recherche/gen_images.py usine-aluminium
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n7-recherche'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = (pathlib.Path(__file__).resolve().parents[3]
        / 'assets' / 'interactive' / MODULE)
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
         "profondeur de champ. Québec ordinaire — bureau public, usine de "
         "région, cuisine d'appartement, route de campagne —, palette sobre. "
         "Aucun texte lisible, aucune écriture déchiffrable, aucun logo, "
         "aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie ordinaire au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou "
        "hors cadrage du visage. Lumière naturelle douce, faible profondeur "
        "de champ. Aucun visage reconnaissable, aucun texte, aucun logo, "
        "aucun filigrane.")

SANS_MOT = (" Strictly no letters, no words, no readable characters anywhere "
            "in the image: every line of text must be an abstract grey "
            "stroke. Aucun mot d'anglais nulle part.")

P_EX  = "Je découvre · Exercice 4 — Les lieux de la recherche et du travail"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('salle-ordinateurs', 'images', P_EX, STYLE + " Une salle publique de bureau "
  "gouvernemental : six postes informatiques alignés sur deux longues tables, "
  "écrans allumés mais entièrement flous, chaises pivotantes vides, une "
  "imprimante multifonction au fond. Éclairage au néon, moquette grise. Aucune "
  "personne." + SANS_MOT),
 ('laboratoire-controle', 'images', P_EX, STYLE + " Un laboratoire de contrôle "
  "de la qualité en milieu industriel : une paillasse d'acier inoxydable, une "
  "rangée d'éprouvettes dans un support, une balance de précision sous cloche, "
  "un microscope au second plan. Aucune personne, aucune étiquette lisible sur "
  "les flacons."),
 ('usine-aluminium', 'images', P_EX, STYLE + " L'extérieur d'une grande usine "
  "de transformation des métaux vue de la route : longs bâtiments de tôle "
  "grise, deux cheminées, un réseau de conduits aériens, un stationnement "
  "d'employés à moitié plein. Ciel couvert de fin d'automne, forêt d'épinettes "
  "à l'arrière-plan. Aucune enseigne lisible."),
 ('babillard-offres', 'images', P_EX, STYLE + " Un babillard de liège couvert "
  "de feuilles de papier blanc punaisées les unes sur les autres, certaines "
  "pendant de travers, quelques languettes découpées au bas d'une feuille. "
  "Photographié **de loin et de trois quarts**, dans un couloir "
  "institutionnel : le babillard occupe le tiers gauche du cadre et le "
  "couloir fuit vers la droite. Ouverture très grande, mise au point sur le "
  "cadre de bois : **les feuilles sont hors du plan de netteté**, on ne "
  "distingue que des blocs gris flous. Aucun en-tête, aucun titre, aucune "
  "majuscule lisible sur aucune feuille." + SANS_MOT),
 ('table-cv', 'images', P_EX, STYLE + " Une table de cuisine en bois clair, "
  "vue du dessus en légère plongée : deux feuilles imprimées posées côte à "
  "côte, un stylo bleu, une tasse de café, un téléphone retourné. Lumière de "
  "fin de journée par une fenêtre hors champ." + SANS_MOT),
 ('route-region', 'images', P_EX, STYLE + " Une route régionale à deux voies "
  "bordée de forêt d'épinettes, vue depuis l'accotement, avec les toits d'un "
  "village et un clocher au loin dans la vallée. Fin d'automne, lumière basse. "
  "Aucun panneau lisible."),

 # ── Les neuf photos du banc de vocabulaire ────────────────────────────
 ('marche-du-travail', 'vocab', P_VOC, PERS + " Un salon de l'emploi dans un "
  "gymnase d'école secondaire québécoise, vu **de haut et de loin, depuis le "
  "fond de la salle** : deux rangées de kiosques à tables pliantes le long "
  "des murs, une quinzaine de personnes qui circulent entre eux, toutes vues "
  "de dos ou de très loin, aucun visage discernable. Panneaux de kiosque "
  "entièrement unis, sans une seule inscription. Plancher de bois verni, "
  "estrade repliée, éclairage de plafonniers." + SANS_MOT),
 ('salle-multiservice', 'vocab', P_VOC, PERS + " Une personne vue de dos assise "
  "à un poste informatique dans une salle publique, l'écran entièrement flou "
  "devant elle, une imprimante et un téléphone mural derrière." + SANS_MOT),
 ('evaluation-comparative', 'vocab', P_VOC, STYLE + " Une seule feuille "
  "officielle **posée à plat sur un bureau de bois, sans personne et sans "
  "aucune main dans le cadre**, vue en légère plongée de trois quarts. Un "
  "bandeau d'en-tête, un bloc de lignes, et un sceau gaufré en relief dans le "
  "coin inférieur droit. Une enveloppe ouverte à côté. Toutes les lignes sont "
  "des traits gris entièrement illisibles." + SANS_MOT),
 ('curriculum-vitae', 'vocab', P_VOC, STYLE + " Gros plan sur deux feuilles "
  "imprimées agrafées, posées à plat sur une table de bois : un bandeau en "
  "haut, des blocs séparés par des filets, une colonne de dates à droite. "
  "Toutes les lignes de texte sont des traits gris illisibles." + SANS_MOT),
 ('transformation', 'vocab', P_VOC, STYLE + " Intérieur d'une halle "
  "industrielle : des lingots de métal empilés sur des palettes au premier "
  "plan, un pont roulant au plafond, une lueur orangée de four au fond. "
  "Aucune personne, aucune inscription."),
 ('usine', 'vocab', P_VOC, STYLE + " Une usine de tôle grise vue de face "
  "depuis son stationnement, deux portes de quai de chargement, un camion "
  "remorque reculé contre l'une d'elles. Ciel gris. Aucune enseigne lisible."),
 ('quart-de-travail', 'vocab', P_VOC, PERS + " Deux personnes en vêtements de "
  "travail et casque de sécurité, vues de dos, franchissant une porte "
  "d'usine à l'aube, l'une entrant et l'autre sortant. Éclairage extérieur "
  "bleuté." + SANS_MOT),
 ('portrait-economique', 'vocab', P_VOC, STYLE + " Un document imprimé broché "
  "ouvert à plat sur une table de bois, vu **de trois quarts et en plongée**, "
  "montrant un diagramme à barres et un diagramme circulaire côte à côte. Les "
  "barres et les secteurs sont des aplats de couleur **sans aucune étiquette, "
  "sans aucun chiffre, sans aucune légende et sans axe gradué** ; les titres "
  "et tous les blocs de texte autour sont de simples traits gris. Aucun "
  "crochet, aucun caractère, aucun pourcentage nulle part." + SANS_MOT),
 ('offre-emploi', 'vocab', P_VOC, STYLE + " Gros plan sur une feuille "
  "d'annonce punaisée seule au centre d'un babillard de liège, un peu "
  "gondolée, avec un titre en gras en haut et trois blocs de lignes en "
  "dessous." + SANS_MOT),
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
    carré — c'est tout l'objet du passage au 3:2.
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
