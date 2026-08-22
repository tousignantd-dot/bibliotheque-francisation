#!/usr/bin/env python3
"""Les 16 images de module-n6-habitation (niveau 6, activité 106).

Deux destinations :
  · `images/` — les cinq photos de l'exercice 4 de « Je découvre », réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les onze photos du banc de vocabulaire, réduites à 800 px
    qualité 82.

**Non exécuté au moment de la livraison du module** : les images coûtent de
l'argent réel et l'agent qui a produit le module n'était pas autorisé à les
générer. `node build/coherence.js module-n6-habitation` sort donc 16 écarts
« image absente du disque », tous attendus, et aucun autre.

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix mesuré le 21 août 2026 — Google direct,
puis fal.ai, puis WaveSpeed — rend le nom de celle qui a servi, et inscrit
chaque tentative au registre `~/Claude/generations/journal_appels.py`. Un
fournisseur facture des **appels**, pas des fichiers présents : une image
régénérée est payée chaque fois.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu écrit à la
main : ce fichier vit dans `build/contenu/<slug>/`, donc trois niveaux sous la
racine du dépôt. Les générateurs des modules les plus anciens portaient le
chemin en dur et cessaient de fonctionner dès qu'on travaillait dans un
worktree — ce qui est précisément le cas ici.

**Le sujet est le bâtiment ordinaire, pas le chantier de magazine.** Une
maison de 1961 dans une petite ville des Laurentides : du béton gris, de la
terre, du carton et de la poussière. Aucune image ne doit ressembler à une
publicité de rénovation — c'est le défaut vers lequel le modèle penche dès
qu'on lui parle de travaux. Les prompts insistent sur l'usure, l'éclairage
pauvre et l'absence de toute personne identifiable.

**Deux images contiennent du papier**, et le papier attire l'anglais : les
prompts de la soumission, du rapport et de l'échéancier exigent que chaque
ligne de texte soit un trait gris. Une image où l'on peut lire un mot est à
refaire.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n6-habitation/gen_images.py
  python3 build/contenu/module-n6-habitation/gen_images.py mur-de-fondation
  python3 build/contenu/module-n6-habitation/gen_images.py vocab/soumission
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n6-habitation'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 4 — Les lieux du chantier, avant qu'il commence"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : une petite maison de 1961 dans une ville des Laurentides,
# en fin d'automne. Rien de spectaculaire, rien de publicitaire, aucune
# rénovation terminée.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle grise de "
         "fin d'automne ou éclairage d'ampoule nue, faible profondeur de "
         "champ. Petite maison unifamiliale de 1961 dans une ville moyenne "
         "du Québec, matériaux ordinaires et un peu usés, palette sobre de "
         "gris, de bruns et de beiges. Aucun texte lisible, aucun mot "
         "déchiffrable, aucun logo, aucune marque, aucun filigrane, aucune "
         "personne identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire de maison au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts "
        "arrière ou hors cadrage du visage. Lumière naturelle douce, faible "
        "profondeur de champ. Aucun visage reconnaissable, aucun texte, aucun "
        "logo, aucun filigrane.")

# Trois images contiennent du papier imprimé, et un modèle d'image écrit
# volontiers de l'anglais sur un document.
SANS_MOTS = (" Strictly no letters, no words, no readable characters anywhere "
             "in the image: every line of text, including any headline, table "
             "heading or label, must be an abstract grey stroke. Aucun mot "
             "d'anglais nulle part.")

# La contrainte inverse : ne pas rendre le chantier joli.
BRUT = (" Ni décor de magazine, ni rénovation terminée, ni éclairage "
        "publicitaire : de la poussière, des traces d'usure, des matériaux "
        "bruts.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les cinq images de l'exercice 4 ───────────────────────────────────
 ('sous-sol-non-amenage', 'images', P_EX, STYLE + " Le sous-sol non aménagé "
  "d'une maison des années soixante : plancher de béton nu, murs de fondation "
  "gris apparents, une fournaise et un chauffe-eau dans un coin, des boîtes de "
  "carton et une étagère de métal le long d'un mur, une ampoule nue au plafond, "
  "une petite fenêtre en hauteur. Aucune personne." + BRUT + SANS_MOTS),
 ('mur-de-fondation', 'images', P_EX, STYLE + " Gros plan sur un mur de "
  "fondation en béton coulé, vu de l'intérieur, au ras du plancher de béton. "
  "Une fissure fine et oblique monte en biais sur environ un mètre. Une trace "
  "d'humidité plus sombre autour. Lumière rasante d'ampoule nue. Aucune "
  "personne, aucune inscription." + BRUT + SANS_MOTS),
 ('terrain-le-long-du-mur', 'images', P_EX, STYLE + " Vue extérieure en légère "
  "plongée sur la bande de terre le long du mur d'une maison : sol tassé, "
  "herbe rare, une flaque d'eau stagnante contre la fondation, une descente de "
  "gouttière en aluminium qui se termine à quelques centimètres du mur. Ciel "
  "couvert, feuilles mortes. Aucune personne." + BRUT + SANS_MOTS),
 ('table-couverte-de-papiers', 'images', P_EX, STYLE + " Une table de cuisine "
  "en fin de soirée, vue de trois quarts au-dessus : deux documents ouverts "
  "côte à côte, l'un agrafé et plus épais, l'autre d'une seule feuille, une "
  "calculatrice, un crayon, une tasse. Une lampe basse. On distingue nettement "
  "la disposition des documents — des titres, des colonnes, une ligne de total "
  "— mais chaque ligne écrite est un trait gris entièrement illisible. Aucune "
  "personne." + SANS_MOTS),
 ('plancher-ouvert', 'images', P_EX, STYLE + " Le plancher d'un sous-sol "
  "ouvert en plein travail : une dalle de béton cassée sur environ deux mètres "
  "carrés, des morceaux de béton empilés à côté, de la pierre concassée et de "
  "la terre brune dessous, un trou sombre dans un coin, une pelle appuyée au "
  "mur, de la poussière dans l'air. Aucune personne." + BRUT + SANS_MOTS),

 # ── Les onze photos du banc de vocabulaire ────────────────────────────
 ('entrepreneur-general', 'vocab', P_VOC, PERS + " Un homme de métier d'une "
  "cinquantaine d'années, vu de dos et de trois quarts arrière, debout au "
  "milieu d'un sous-sol non fini, un ruban à mesurer à la ceinture, la main "
  "levée vers un mur de béton comme s'il montrait quelque chose. Casquette, "
  "veste de travail usée. Le visage est hors cadrage." + BRUT + SANS_MOTS),
 ('soumission', 'vocab', P_VOC, STYLE + " Gros plan en légère plongée sur une "
  "feuille de papier blanche posée sur une table de bois. On distingue "
  "nettement la disposition d'un devis — un bandeau en haut, une liste de "
  "postes numérotés, une colonne de chiffres alignés à droite, une ligne de "
  "total soulignée, un bloc plus petit tout en bas — mais chaque ligne écrite "
  "est un trait gris entièrement illisible. Un stylo posé en travers." + SANS_MOTS),
 ('corps-de-metier', 'vocab', P_VOC, STYLE + " Nature morte d'outils de "
  "quatre métiers posés côte à côte sur une feuille de contreplaqué : une "
  "truelle de maçon, une clé à tuyau, une pince d'électricien et un couteau à "
  "gypse. Poussière fine, lumière latérale. Aucune personne, aucune marque "
  "visible sur les manches." + BRUT + SANS_MOTS),
 ('fondation', 'vocab', P_VOC, STYLE + " Vue extérieure du bas d'une maison : "
  "la partie visible du mur de fondation en béton gris, entre le revêtement du "
  "rez-de-chaussée et le sol, sur trois ou quatre mètres de long. Herbe et "
  "terre au premier plan. Aucune personne." + BRUT + SANS_MOTS),
 ('fissure', 'vocab', P_VOC, STYLE + " Très gros plan sur une fissure fine et "
  "oblique dans un mur de béton gris, avec la texture du coffrage encore "
  "visible autour. Une légère efflorescence blanche le long de la fente. "
  "Lumière rasante. Aucune personne." + BRUT + SANS_MOTS),
 ('descente-de-gouttiere', 'vocab', P_VOC, STYLE + " Le bas d'une descente de "
  "gouttière en aluminium au coin d'une maison, vue de près, se terminant à "
  "quelques centimètres du mur, au-dessus d'un sol détrempé et d'une petite "
  "flaque. Feuilles mortes collées au sol. Aucune personne." + BRUT + SANS_MOTS),
 ('pente-du-terrain', 'vocab', P_VOC, STYLE + " Vue au ras du sol le long "
  "d'une maison, montrant l'inclinaison de la bande de terre : le sol descend "
  "vers la fondation au lieu de s'en éloigner, et l'eau s'accumule au pied du "
  "mur. Herbe clairsemée, terre brune. Aucune personne." + BRUT + SANS_MOTS),
 ('rapport-inspection', 'vocab', P_VOC, STYLE + " Gros plan sur un document "
  "agrafé d'une dizaine de pages, ouvert à une page du milieu, posé sur une "
  "table. On distingue la disposition d'un rapport technique — un titre de "
  "section, des paragraphes numérotés, deux petites photographies "
  "rectangulaires insérées dans la page — mais chaque ligne écrite est un "
  "trait gris entièrement illisible et les deux photographies sont des aplats "
  "gris. Aucune personne." + SANS_MOTS),
 ('echeancier', 'vocab', P_VOC, STYLE + " Un calendrier mural de papier "
  "punaisé au mur d'une cuisine, vu de face et légèrement de biais, avec "
  "plusieurs cases marquées de traits de crayon et deux zones surlignées en "
  "jaune pâle qui s'étendent sur plusieurs jours. Les chiffres et les mots "
  "sont des traits gris entièrement illisibles. Aucune personne." + SANS_MOTS),
 ('dalle-de-beton', 'vocab', P_VOC, STYLE + " Vue à hauteur de genou sur une "
  "dalle de béton de sous-sol, nue, grise, avec les traces de la truelle et "
  "une fine poussière. Un joint de retrait traverse l'image en diagonale. "
  "Aucun revêtement, aucune personne." + BRUT + SANS_MOTS),
 ('membrane', 'vocab', P_VOC, STYLE + " Gros plan sur un rouleau de membrane "
  "de polyéthylène partiellement déroulé sur une dalle de béton de sous-sol, "
  "avec le pli du rouleau bien visible et un ruban adhésif de chantier posé à "
  "côté. Lumière d'ampoule nue. Aucune personne, aucune inscription sur le "
  "rouleau." + BRUT + SANS_MOTS),
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
    print('  ✓ %-28s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('   ✗ ' + e)
