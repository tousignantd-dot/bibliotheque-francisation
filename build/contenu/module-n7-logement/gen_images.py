#!/usr/bin/env python3
"""Les 17 images de module-n7-logement (niveau 7, activité 111).

Deux destinations :
  · `images/` — les cinq photos de l'exercice 4 de « Je découvre », réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les douze photos du banc de vocabulaire, réduites à 800 px
    qualité 82 (quatre des seize cartes n'ont pas d'image : « la fixation du
    loyer », « une contrepartie », « un compromis » et « un contrat de
    courtage » sont des abstractions qui s'illustrent mal).

**Les quatre règles de prompt du 22 août 2026 sont appliquées ici**, et elles
sont écrites dans `CLAUDE.md` (« Les images d'un module ») :

1. aucun texte lisible — et ce module en est plein, puisque son sujet est un
   avis, une fiche, une promesse d'achat. D'où `SANS_MOTS`, exigé sur chaque
   image qui montre du papier ou un écran ;
2. pas de mains ni de visages en gros plan ;
3. un décor québécois nommé — brique, escalier extérieur, duplex, plancher de
   bois franc, fenêtre à guillotine — plutôt qu'« appartement moderne » ;
4. **l'image montre ce que dit son énoncé.** Les cinq prompts d'exercice sont
   écrits à partir de la phrase exacte de la rangée `ok` de `prImg`, recopiée
   en commentaire au-dessus de chacun. Le contrôle avant livraison :

       node build/contexte_images.js module-n7-logement

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix — Google direct, puis fal.ai, puis
WaveSpeed —, rend le nom de celle qui a servi et inscrit chaque tentative au
registre `~/Claude/generations/journal_appels.py`. Un fournisseur facture des
**appels**, pas des fichiers présents.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu : ce fichier
vit dans `build/contenu/<slug>/`, donc trois niveaux sous la racine — sans
quoi il cesserait de fonctionner dans un worktree.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n7-logement/gen_images.py
  python3 build/contenu/module-n7-logement/gen_images.py pancarte-a-vendre
  python3 build/contenu/module-n7-logement/gen_images.py vocab/mise-de-fonds
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n7-logement'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 4 — Les lieux du dossier de Sokhna"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : Saint-Hyacinthe au début du printemps, des logements
# ordinaires, une lumière franche mais basse. Rien de publicitaire, rien de
# « moderne » : le générique américain vient de là.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle de fin "
         "d'hiver ou de début de printemps, faible profondeur de champ. Ville "
         "moyenne du Québec : duplex et triplex de brique rouge ou beige, "
         "escaliers extérieurs en métal peint, fenêtres à guillotine, "
         "plancher de bois franc et plinthes hautes à l'intérieur, mobilier "
         "ordinaire un peu usé, palette sobre. Aucun texte lisible, aucun mot "
         "déchiffrable, aucun logo, aucune marque, aucun filigrane, aucune "
         "personne identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire au Québec avec "
        "une ou deux personnes vues de loin, de dos ou de trois quarts "
        "arrière, jamais en gros plan et jamais les mains seules au premier "
        "plan. Lumière naturelle douce, faible profondeur de champ. Aucun "
        "visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

# Le sujet de ce module est fait de papiers : avis, fiche, promesse d'achat,
# relevé. Un modèle d'image écrit volontiers de l'anglais sur un formulaire, et
# l'élève le lit.
SANS_MOTS = (" Strictly no letters, no words, no readable characters anywhere "
             "in the image: every line of text, including any headline, form "
             "field, sign, screen interface or label, must be an abstract grey "
             "stroke. Aucun mot d'anglais nulle part, aucun nom d'organisme, "
             "aucune enseigne lisible.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les cinq images de l'exercice 4 ───────────────────────────────────
 # « Une enveloppe blanche coincée entre une porte de logement et son cadre. »
 ('enveloppe-dans-la-porte', 'images', P_EX, STYLE + " Gros plan sur une porte "
  "de logement d'un immeuble ancien, peinture crème un peu écaillée, poignée de "
  "laiton : une enveloppe blanche est coincée verticalement entre le battant et "
  "le cadre, à hauteur de serrure. Palier d'escalier intérieur, éclairage de "
  "plafonnier. Aucune personne, aucune inscription sur l'enveloppe." + SANS_MOTS),
 # « Une table de cuisine où deux tasses refroidissent à côté d'un papier plié. »
 ('cuisine-rue-bourdages', 'images', P_EX, STYLE + " Une table de cuisine de "
  "logement ancien, nappe de toile cirée, deux tasses de café à moitié pleines "
  "l'une en face de l'autre, et entre les deux une feuille pliée en trois puis "
  "rouverte, posée à plat avec un crayon dessus. Fenêtre à guillotine derrière, "
  "lumière grise de fin d'après-midi. Aucune personne ; toutes les lignes de la "
  "feuille sont des traits gris illisibles." + SANS_MOTS),
 # « Une pancarte plantée devant un immeuble de brique, un samedi matin. »
 ('pancarte-a-vendre', 'images', P_EX, STYLE + " Un panneau rectangulaire vierge "
  "monté sur deux poteaux de bois, planté dans un carré de gazon jauni devant un "
  "petit immeuble de brique rouge de deux étages avec escalier extérieur. Le "
  "panneau est entièrement uni, d'une seule couleur, sans la moindre inscription "
  "ni le moindre logo. Matin clair de printemps, neige fondante au bord du "
  "trottoir. Aucune personne." + SANS_MOTS),
 # « Un salon vide et clair, avec une porte-fenêtre qui donne sur un balcon. »
 ('visite-du-condo', 'images', P_EX, STYLE + " Un salon entièrement vide dans un "
  "immeuble en copropriété des années quatre-vingt-dix : plancher de bois franc "
  "clair, murs blancs, plinthes électriques, et une grande porte-fenêtre "
  "coulissante qui donne sur un petit balcon de béton avec une rampe de métal. "
  "Lumière du matin, aucun meuble, aucune personne." + SANS_MOTS),
 # « Un bureau d'institution financière, deux chaises et un écran tourné vers le client. »
 ('bureau-de-la-caisse', 'images', P_EX, STYLE + " Un petit bureau fermé "
  "d'institution financière de quartier : une table claire, deux chaises "
  "rembourrées vides côte à côte du côté visiteur, un écran d'ordinateur pivoté "
  "vers elles, une chemise cartonnée fermée et une boîte de mouchoirs. Cloison "
  "vitrée derrière. Aucune personne ; l'écran montre des blocs et des colonnes "
  "gris entièrement illisibles." + SANS_MOTS),

 # ── Les douze photos du banc de vocabulaire ───────────────────────────
 ('avis-de-modification', 'vocab', P_VOC, STYLE + " Une seule feuille blanche "
  "posée à plat sur une table de bois, montrant la disposition d'un avis "
  "officiel : un bandeau en haut, deux blocs d'adresse, des sections numérotées, "
  "deux cases à cocher côte à côte en bas. Chaque ligne écrite est un trait gris "
  "entièrement illisible. Aucune personne." + SANS_MOTS),
 ('hausse-de-loyer', 'vocab', P_VOC, STYLE + " Un carnet à colonnes ouvert sur "
  "une table de cuisine, où deux montants ont été inscrits l'un au-dessus de "
  "l'autre au crayon et reliés par une flèche montante tracée à la main. Les "
  "chiffres et les mots sont des traits gris illisibles ; seule la flèche se voit "
  "nettement. Une calculatrice à côté. Aucune personne." + SANS_MOTS),
 ('delai-de-reponse', 'vocab', P_VOC, STYLE + " Gros plan sur un calendrier "
  "mural de cuisine ouvert sur un mois de fin d'hiver, avec une case entourée au "
  "crayon rouge et une seconde case entourée un mois plus loin, reliées par un "
  "trait. Les chiffres et les noms de jours sont des traits gris illisibles ; "
  "seuls les cercles rouges se voient." + SANS_MOTS),
 ('contre-proposition', 'vocab', P_VOC, STYLE + " Deux feuilles posées côte à "
  "côte sur une table de cuisine, la seconde couverte d'annotations manuscrites "
  "dans la marge et d'un chiffre entouré au crayon. Un stylo en travers. Toutes "
  "les lignes sont des traits gris entièrement illisibles ; seuls le cercle et "
  "les traits de marge se distinguent. Aucune personne." + SANS_MOTS),
 ('entente-ecrite', 'vocab', P_VOC, STYLE + " Gros plan en légère plongée sur un "
  "bout de papier quadrillé posé sur une table, portant trois lignes manuscrites "
  "et deux petites signatures en bas, avec un stylo à côté. Les lignes "
  "manuscrites sont des traits d'encre entièrement illisibles. Aucune personne, "
  "aucune main dans le cadre." + SANS_MOTS),
 ('courtier-immobilier', 'vocab', P_VOC, PERS + " Une personne en manteau, vue "
  "de dos et de loin, debout sur le perron d'un duplex de brique, en train "
  "d'ouvrir la porte à une autre personne également vue de dos. Trottoir de "
  "ville moyenne du Québec, matin de printemps. Aucun visage, aucune enseigne, "
  "aucune inscription." + SANS_MOTS),
 ('frais-de-copropriete', 'vocab', P_VOC, STYLE + " La façade d'un petit "
  "immeuble en copropriété de deux étages en brique beige, avec une entrée "
  "commune vitrée, une allée déneigée, un bac de recyclage rangé sur le côté et "
  "une haie taillée. Fin d'hiver, ciel clair. Aucune personne, aucune enseigne, "
  "aucun numéro lisible." + SANS_MOTS),
 ('fonds-de-prevoyance', 'vocab', P_VOC, STYLE + " Un toit plat d'immeuble de "
  "deux étages en cours de réfection, vu de trois quarts depuis une hauteur "
  "voisine : membrane neuve déroulée sur une partie, rouleaux en attente, une "
  "échelle appuyée, un conteneur à débris en bas dans le stationnement. Aucune "
  "personne, aucun logo sur le conteneur." + SANS_MOTS),
 ('promesse-dachat', 'vocab', P_VOC, STYLE + " Un document de plusieurs pages "
  "agrafées posé à plat sur une table claire, ouvert à une page où l'on distingue "
  "des sections numérotées, des cases et deux lignes de signature en bas. Un "
  "stylo posé en travers. Chaque ligne écrite est un trait gris entièrement "
  "illisible. Aucune personne." + SANS_MOTS),
 ('mise-de-fonds', 'vocab', P_VOC, STYLE + " Un livret d'épargne fermé et une "
  "petite pile de billets pliés posés sur une table de cuisine, à côté d'une "
  "calculatrice et d'un trousseau de clés de maison. Lumière chaude de lampe. "
  "Aucune personne ; aucune inscription lisible sur le livret ni sur les "
  "billets, dont les motifs restent flous." + SANS_MOTS),
 ('inspection-preachat', 'vocab', P_VOC, STYLE + " Un sous-sol de maison "
  "québécoise éclairé par une lampe de travail posée au sol : mur de fondation "
  "de béton, une tache d'humidité au bas du mur, un ruban à mesurer déroulé et "
  "une lampe de poche posée sur une caisse. Aucune personne, aucune inscription." + SANS_MOTS),
 ('droits-de-mutation', 'vocab', P_VOC, STYLE + " Une enveloppe brune non "
  "ouverte posée sur une pile de courrier, au bord d'une table d'entrée, à côté "
  "d'un trousseau de clés de maison neuves. Lumière de fin de journée par une "
  "fenêtre. Les adresses et les mentions imprimées sont des traits gris "
  "entièrement illisibles. Aucune personne." + SANS_MOTS),
]


def reduire(data, largeur, qualite):
    """L'image d'exercice occupe 223 x 132 px à l'écran, la photo du banc moins.

    La hauteur suit le rapport de l'image reçue plutôt que d'être forcée à un
    carré — c'est l'objet du passage au 3:2.
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
    print('  ✓ %-26s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('   ✗ ' + e)
