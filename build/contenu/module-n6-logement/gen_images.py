#!/usr/bin/env python3
"""Les 15 images de module-n6-logement (niveau 6, activité 105).

Deux destinations :
  · `images/` — les cinq photos de l'exercice 4 de « Je découvre », réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les dix photos du banc de vocabulaire, réduites à 800 px
    qualité 82.

**Non exécuté au moment de la livraison du module** : les images coûtent de
l'argent réel et l'agent qui a produit le module n'était pas autorisé à les
générer. `node build/coherence.js module-n6-logement` sort donc 15 écarts
« image absente du disque », tous attendus, et aucun autre.

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix mesuré le 21 août 2026 — Google direct,
puis fal.ai, puis WaveSpeed — rend le nom de celle qui a servi, et inscrit
chaque tentative au registre `~/Claude/generations/journal_appels.py`. Un
fournisseur facture des **appels**, pas des fichiers présents : une image
régénérée est payée chaque fois.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu écrit à la
main : ce fichier vit dans `build/contenu/<slug>/`, donc trois niveaux sous la
racine du dépôt. Les générateurs des premiers modules portaient le chemin en
dur et cessaient de fonctionner dès qu'on travaillait dans un worktree.

**Le sujet est le papier officiel**, et c'est la contrainte forte de ce module :
un bail, un avis, une lettre de refus, une page Web. Un modèle d'image écrit
volontiers de l'anglais sur un document. Chaque prompt exige donc que toute
ligne de texte soit réduite à un trait gris illisible. Une image où l'on peut
lire un mot est à refaire — à plus forte raison une image où l'on croirait lire
le nom d'un tribunal réel, ce qui en ferait un faux document.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n6-logement/gen_images.py
  python3 build/contenu/module-n6-logement/gen_images.py immeuble-canardiere
  python3 build/contenu/module-n6-logement/gen_images.py vocab/bail
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n6-logement'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 4 — Les lieux et les papiers du dossier"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : un quartier ancien de Québec en novembre, des logements
# ordinaires, une lumière basse. Rien de spectaculaire, rien de publicitaire.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle de fin "
         "d'automne ou éclairage domestique chaud, faible profondeur de champ. "
         "Quartier ancien d'une ville du Québec : immeubles de brique de deux "
         "ou trois étages, escaliers extérieurs, ruelles, logements ordinaires "
         "un peu usés, palette sobre. Aucun texte lisible, aucun mot "
         "déchiffrable, aucun logo, aucune marque, aucun filigrane, aucune "
         "personne identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène domestique ordinaire au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts "
        "arrière ou hors cadrage du visage. Lumière naturelle douce, faible "
        "profondeur de champ. Aucun visage reconnaissable, aucun texte, aucun "
        "logo, aucun filigrane.")

# Le sujet du module oblige à cette phrase : presque toutes les images
# contiennent du papier imprimé ou un écran, et un modèle d'image écrit
# volontiers de l'anglais sur un formulaire.
SANS_MOTS = (" Strictly no letters, no words, no readable characters anywhere "
             "in the image: every line of text, including any headline, form "
             "field, screen interface or label, must be an abstract grey "
             "stroke. Aucun mot d'anglais nulle part, aucun nom d'organisme.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les cinq images de l'exercice 4 ───────────────────────────────────
 ('immeuble-canardiere', 'images', P_EX, STYLE + " La façade d'un immeuble de "
  "brique rouge de trois étages, six logements, avec un escalier extérieur en "
  "métal peint qui monte en tournant, des fenêtres à guillotine et de petites "
  "galeries. Fin d'après-midi de novembre, arbres nus, trottoir mouillé. Aucune "
  "personne, aucune inscription lisible." + SANS_MOTS),
 ('boites-aux-lettres', 'images', P_EX, STYLE + " Gros plan sur un bloc de six "
  "boîtes aux lettres métalliques encastrées dans le mur d'un hall d'entrée, "
  "chacune avec une petite fente et une serrure. D'une des boîtes dépasse le coin "
  "d'une enveloppe blanche. Plaquettes de numéros illisibles, lumière de "
  "plafonnier." + SANS_MOTS),
 ('page-a-lecran', 'images', P_EX, STYLE + " Un ordinateur portable ouvert sur une "
  "table de cuisine, tard le soir, à côté d'une tasse et d'un carnet ouvert avec "
  "un crayon. L'écran montre la disposition d'une page Web — un bandeau en haut, "
  "un titre, plusieurs paragraphes, une liste à puces, un encadré gris — mais "
  "chaque ligne de l'écran est un trait gris entièrement illisible. Aucune "
  "personne." + SANS_MOTS),
 ('logement-a-moitie-vide', 'images', P_EX, STYLE + " Un salon de logement ancien "
  "à moitié vidé : plancher de bois franc, plinthes hautes, une fenêtre sans "
  "rideau, cinq ou six boîtes de carton fermées empilées près du mur, une chaise "
  "seule. Lumière grise de fin de journée. Aucune personne, aucune étiquette "
  "lisible sur les boîtes." + SANS_MOTS),
 ('palier-du-deuxieme', 'images', P_EX, STYLE + " Le palier d'un escalier "
  "intérieur d'immeuble ancien : rampe de bois vernis, marches usées, deux portes "
  "de logement face à face avec un petit numéro de métal, un tapis d'entrée. "
  "Éclairage jaune d'un plafonnier. Aucune personne, aucun numéro "
  "déchiffrable." + SANS_MOTS),

 # ── Les dix photos du banc de vocabulaire ─────────────────────────────
 ('locateur', 'vocab', P_VOC, PERS + " Une personne d'une soixantaine d'années "
  "vue de dos, en veste de laine, debout sur la galerie d'un immeuble de brique, "
  "un trousseau de clés à la main, regardant la rue. Le visage est hors cadrage." + SANS_MOTS),
 ('bail', 'vocab', P_VOC, STYLE + " Gros plan en légère plongée sur un contrat de "
  "plusieurs pages agrafées, posé à plat sur une table de bois, un stylo en "
  "travers. On distingue nettement la disposition d'un formulaire de contrat — un "
  "bandeau, des sections encadrées, des cases, une ligne de signature — mais "
  "chaque ligne écrite est un trait gris entièrement illisible." + SANS_MOTS),
 ('avis', 'vocab', P_VOC, STYLE + " Gros plan sur une seule feuille blanche pliée "
  "en trois puis rouverte, posée sur une table, montrant la disposition d'une "
  "lettre : une date en haut à droite, un bloc d'adresse, une ligne d'objet, trois "
  "paragraphes, une signature manuscrite. Toutes les lignes sont des traits gris "
  "illisibles." + SANS_MOTS),
 ('delai', 'vocab', P_VOC, STYLE + " Gros plan sur un calendrier mural de cuisine "
  "ouvert sur un mois d'hiver, avec deux cases entourées au crayon rouge à quinze "
  "jours d'intervalle. Les chiffres et les noms des jours sont des traits gris "
  "illisibles ; seuls les cercles rouges se voient nettement." + SANS_MOTS),
 ('sous-location', 'vocab', P_VOC, PERS + " Deux personnes vues de dos dans "
  "l'embrasure d'une porte de logement, l'une tendant un trousseau de clés à "
  "l'autre. Couloir clair, plancher de bois. Les visages sont hors cadrage." + SANS_MOTS),
 ('cession-de-bail', 'vocab', P_VOC, STYLE + " Gros plan sur deux mains hors "
  "cadrage du visage qui font glisser un contrat agrafé d'un côté à l'autre d'une "
  "table de cuisine, vers une deuxième personne dont on ne voit que l'avant-bras. "
  "Toutes les lignes du contrat sont des traits gris illisibles." + SANS_MOTS),
 ('motif-serieux', 'vocab', P_VOC, STYLE + " Gros plan sur une feuille posée sur "
  "un bureau, dont deux passages sont soulignés au crayon et un troisième marqué "
  "d'un trait vertical dans la marge, à côté d'une paire de lunettes de lecture. "
  "Le texte est fait de traits gris entièrement illisibles." + SANS_MOTS),
 ('accuse-de-reception', 'vocab', P_VOC, PERS + " Gros plan sur une main hors "
  "cadrage du visage qui signe au bas d'une feuille tenue par une autre personne, "
  "debout dans un couloir d'immeuble. Le stylo est visible, la feuille ne porte "
  "que des traits gris illisibles." + SANS_MOTS),
 ('dommages', 'vocab', P_VOC, STYLE + " Gros plan sur un coin de plancher de bois "
  "franc abîmé près d'une plinthe : lattes gonflées, vernis écaillé, une auréole "
  "sombre. Lumière rasante de fenêtre. Aucune personne, aucun texte." + SANS_MOTS),
 ('defaut-de-paiement', 'vocab', P_VOC, STYLE + " Gros plan sur trois enveloppes "
  "non ouvertes posées les unes sur les autres au bord d'une table, à côté d'un "
  "chéquier fermé. Les adresses et les mentions imprimées sont des traits gris "
  "entièrement illisibles." + SANS_MOTS),
]


def reduire(data, largeur, qualite):
    """L'image d'exercice occupe 223 x 132 px à l'écran, la photo du banc moins.

    La route Google directe rend des JPEG bien plus lourds que fal.ai ; les
    deux se réduisent, seulement pas au même format. La hauteur suit le rapport
    de l'image reçue au lieu d'être forcée à un carré — c'est tout l'objet du
    passage au 3:2.
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
faits, sautes, echecs, routes = [], [], [], {}

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
        data, route = generer_image(prompt, ratio=RATIO, resolution="1K",
                                    module=MODULE, cible=etiquette)
    except Exception as e:
        echecs.append('%s : %s' % (etiquette, e)); continue

    brut = data
    try:
        data = reduire(data, *((800, 82) if dossier == 'vocab' else (1200, 85)))
    except Exception as e:
        echecs.append('%s : réduction impossible (%s) — image brute gardée'
                      % (etiquette, e))

    base = '%s_%s-%s_%s' % (MODULE, dossier, nom, horodatage)
    (GEN / (base + '.jpg')).write_bytes(brut)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "nano-banana-2 (Gemini 3.1 Flash Image)",
        "prompt": prompt,
        "refs": [],
        "params": {"num_images": 1, "aspect_ratio": RATIO,
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": route,
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation",
        "module": MODULE,
        "page": page,
        "destination": "assets/interactive/%s/%s/%s.jpg" % (MODULE, dossier, nom),
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(etiquette)
    routes[route] = routes.get(route, 0) + 1
    print('  ✓ %-24s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('   ✗ ' + e)
