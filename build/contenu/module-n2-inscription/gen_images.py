#!/usr/bin/env python3
"""Génère les 17 images de module-n2-inscription via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer ;
  · `vocab/`  — les onze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdait le tiers du haut et du bas. Voir
`docs/chantier-tous-niveaux.md`.

La difficulté propre à ce module est la pire de toutes pour un générateur
d'images : **le sujet est un papier couvert de mots**. Un formulaire, une
annonce, un calendrier, une carte d'identité — tout ce que l'élève doit
regarder porte du texte, et le générateur a l'ordre de n'en produire aucun de
lisible. Les prompts demandent donc partout des lignes d'écriture qui « se
lisent comme des traits gris flous », des cases vides, des étiquettes hors
foyer. L'élève lit les vrais mots dans le bandeau noir de l'exercice, jamais
sur la photo.

Deuxième difficulté : dix-sept images de bureau se ressemblent. Chaque prompt
change donc de distance — le comptoir vu de trois quarts, la feuille posée à
plat vue d'en haut, la main qui écrit en gros plan, le babillard vu de face,
le classeur vu de la porte.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n2-inscription/gen_images.py
  python3 build/contenu/module-n2-inscription/gen_images.py formulaire-vide
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n2-inscription'
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

SANS = ("Aucun texte lisible, aucun mot déchiffrable, aucune écriture "
        "reconnaissable, aucun chiffre, aucun nom, aucun logo, aucune marque, "
        "aucun filigrane, aucun visage, aucune personne identifiable — les "
        "personnes, s'il y en a, sont vues de dos ou cadrées sans le visage. "
        "L'écriture imprimée et manuscrite, quand il y en a, se lit comme des "
        "traits gris flous, hors foyer.")

# Le décor principal : le comptoir du secrétariat d'un centre de formation
# pour adultes, au Québec. Néons, mobilier simple, palette neutre.
BUREAU = ("Photographie réaliste, format paysage, lumière de néons douce. "
          "Secrétariat d'un centre de formation pour adultes au Québec : "
          "comptoir de mélamine claire, classeurs de métal, murs pâles. "
          "Palette neutre et calme. " + SANS)

# Ce qui se photographie posé sur une table, vu de près.
PAPIER = ("Photographie réaliste, format paysage, vue rapprochée en lumière "
          "naturelle douce. Objet posé à plat sur un bureau de bois clair, "
          "faible profondeur de champ, palette neutre. " + SANS)

# Les endroits publics du centre et du quartier.
MUR = ("Photographie réaliste, format paysage, lumière du jour. Mur d'un lieu "
       "public au Québec : surface simple, éclairage égal, palette sobre. "
       + SANS)

P_EX  = "Je découvre · Exercice 3 — Ce qu'on voit au secrétariat"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('comptoir-secretariat', 'images', P_EX, BUREAU + " Le comptoir vu de trois "
  "quarts depuis le corridor, dessus dégagé, une chaise derrière, un "
  "présentoir de dépliants vierges sur le côté, personne dedans."),
 ('formulaire-vide', 'images', P_EX, PAPIER + " Une feuille imprimée couverte "
  "de rectangles vides alignés en colonnes, comme un formulaire administratif, "
  "les étiquettes réduites à de fins traits gris flous, un stylo posé en "
  "diagonale à côté."),
 ('babillard-annonce', 'images', P_EX, MUR + " Un tableau de liège brun "
  "couvert de petites feuilles blanches et colorées tenues par des punaises, "
  "vu de face, les feuilles portant des traits gris hors foyer au lieu de "
  "mots."),
 ('calendrier-septembre', 'images', P_EX, PAPIER + " Un calendrier mural "
  "ouvert sur une grille de cases carrées régulières, vu légèrement de biais, "
  "les chiffres illisibles et flous, une case entourée au crayon rouge."),
 ('main-signature', 'images', P_EX, PAPIER + " Gros plan sur une main tenant "
  "un stylo au-dessus d'une ligne tracée au bas d'une feuille, le geste "
  "suspendu, la manche visible, aucun visage."),
 ('carte-identite', 'images', P_EX, PAPIER + " Une petite carte plastifiée "
  "rectangulaire posée sur un bureau, coin arrondi, bande de couleur pâle, la "
  "zone de la photo et les lignes de texte entièrement floues."),

 # ── Les onze photos du banc de vocabulaire ────────────────────────────
 ('inscription', 'vocab', P_VOC, BUREAU + " Un comptoir vu de biais avec deux "
  "chaises devant, une pile de feuilles et un porte-crayons, une silhouette de "
  "dos qui attend son tour."),
 ('formulaire', 'vocab', P_VOC, PAPIER + " Une feuille de formulaire vue d'en "
  "haut, à plat, ses cases vides bien visibles, un crayon posé sur le bord "
  "droit."),
 ('case', 'vocab', P_VOC, PAPIER + " Très gros plan sur deux rectangles vides "
  "imprimés côte à côte sur une feuille, la pointe d'un stylo posée dans le "
  "premier, le reste de la page hors foyer."),
 ('secretariat', 'vocab', P_VOC, BUREAU + " Le bureau vu depuis la porte : un "
  "comptoir bas, un classeur de métal, une chaise de bureau vide, lumière "
  "douce."),
 ('signature', 'vocab', P_VOC, PAPIER + " Gros plan sur le bas d'une feuille : "
  "une ligne horizontale et un trait manuscrit ondulé au-dessus, indéchiffrable, "
  "un stylo posé à côté."),
 ('annonce', 'vocab', P_VOC, MUR + " Une seule petite feuille blanche punaisée "
  "sur un tableau de liège, vue de face et de près, ses lignes réduites à des "
  "traits gris flous, les coins légèrement relevés."),
 ('cours', 'vocab', P_VOC, "Photographie réaliste, format paysage, lumière de "
  "néons. Salle de classe d'adultes au Québec vue du fond : pupitres en "
  "rangées, chaises, grand tableau blanc vide au mur, salle vide. Palette "
  "neutre. " + SANS),
 ('date', 'vocab', P_VOC, PAPIER + " Un calendrier de table ouvert, sa grille "
  "de cases carrées vue de trois quarts, une case marquée d'une croix au "
  "crayon, les chiffres flous."),
 ('horaire', 'vocab', P_VOC, PAPIER + " Une grille imprimée à colonnes et à "
  "rangées, comme un tableau d'horaire, vue d'en haut, ses cellules vides, "
  "les en-têtes réduits à des traits gris."),
 ('adresse', 'vocab', P_VOC, "Photographie réaliste, format paysage, lumière "
  "du jour. Façade d'un immeuble à logements de Montréal : brique, escalier "
  "extérieur de métal, plaque de numéro civique près de la porte, la plaque "
  "hors foyer. Palette neutre. " + SANS),
 ('courriel', 'vocab', P_VOC, PAPIER + " Un ordinateur portable ouvert sur un "
  "bureau, vu de trois quarts au-dessus du clavier, l'écran affichant une "
  "surface claire uniforme sans aucun contenu lisible."),
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
