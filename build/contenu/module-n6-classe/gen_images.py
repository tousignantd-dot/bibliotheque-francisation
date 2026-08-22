#!/usr/bin/env python3
"""Les 20 images de module-n6-classe (niveau 6, activité 107).

Deux destinations :
  · `images/` — les six photos de l'exercice 4 de « Je découvre », réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les quatorze photos du banc de vocabulaire, réduites à 800 px
    qualité 82.

**Non exécuté au moment de la livraison du module** : les images coûtent de
l'argent réel et l'agent qui a produit le module n'était pas autorisé à les
générer. `node build/coherence.js module-n6-classe` sort donc 20 écarts
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

**Le sujet est le papier écrit** — une consigne, une grille, un plan au crayon,
un journal, une bibliographie. Chaque prompt exige donc que toute ligne de
texte soit réduite à un trait gris. Une image où l'on peut lire un mot — un mot
d'anglais surtout — est à refaire. C'est la contrainte la plus dure des
vingt.

**Aucun nom d'établissement réel, aucun logo, aucun visage.** Le centre, la
ville et le bulletin municipal du module sont inventés : une page municipale
qui porterait le nom d'une vraie ville serait un faux document, et un élève la
citerait de bonne foi dans un vrai travail.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n6-classe/gen_images.py
  python3 build/contenu/module-n6-classe/gen_images.py feuille-consigne
  python3 build/contenu/module-n6-classe/gen_images.py vocab/bibliographie
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n6-classe'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 4 — Les lieux et les objets d'une recherche"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : un centre d'éducation des adultes ordinaire d'une petite
# ville du Québec, lumière naturelle, rien de spectaculaire.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle, faible "
         "profondeur de champ. Petite ville du Québec, intérieurs scolaires "
         "ordinaires et sans luxe, palette sobre. Aucun texte lisible, aucun "
         "mot déchiffrable, aucun logo, aucune marque, aucun filigrane, "
         "aucune personne identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire dans un centre "
        "d'éducation des adultes au Québec, avec une ou plusieurs personnes "
        "vues de dos, de trois quarts arrière ou hors cadrage du visage. "
        "Lumière naturelle douce, faible profondeur de champ. Aucun visage "
        "reconnaissable, aucun texte, aucun logo, aucun filigrane.")

# Le sujet du module oblige à cette phrase : presque toutes les images
# contiennent du papier écrit ou imprimé, et un modèle d'image écrit
# volontiers de l'anglais dessus.
SANS_MOTS = (" Strictly no letters, no words, no readable characters anywhere "
             "in the image: every line of text, including any heading, label, "
             "handwriting or form field, must be an abstract grey stroke. "
             "Aucun mot d'anglais nulle part, aucun nom d'établissement, "
             "aucun nom de ville.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 4 ────────────────────────────────────
 ('classe-annonce', 'images', P_EX, PERS + " Une classe d'adultes vue du fond : "
  "des tables occupées par une dizaine de personnes de dos, une enseignante debout "
  "près d'un tableau blanc entièrement vierge, une pile de feuilles dans ses mains. "
  "Fenêtres à gauche, lumière de matin." + SANS_MOTS),
 ('feuille-consigne', 'images', P_EX, STYLE + " Gros plan sur une feuille imprimée "
  "posée sur un pupitre d'école : on distingue un en-tête, quatre paragraphes et une "
  "courte liste, et quelques lignes sont soulignées au crayon de plomb. Un crayon "
  "repose en travers de la feuille. Toutes les lignes sont des traits gris "
  "entièrement illisibles." + SANS_MOTS),
 ('bibliotheque-centre', 'images', P_EX, STYLE + " Une petite bibliothèque "
  "d'établissement scolaire : deux rangées d'étagères basses garnies de livres aux dos "
  "unis, une table ronde de bois clair, une chaise tirée, une fenêtre au fond. Aucune "
  "personne, aucune affiche lisible." + SANS_MOTS),
 ('trois-documents', 'images', P_EX, STYLE + " Trois documents étalés côte à côte sur "
  "une table de bois : un journal plié en deux, une page imprimée agrafée et une "
  "feuille simple. Toutes leurs lignes sont des traits gris illisibles. Un carnet "
  "ouvert et un stylo à côté." + SANS_MOTS),
 ('plan-au-crayon', 'images', P_EX, STYLE + " Très gros plan sur une feuille "
  "quadrillée écrite à la main au crayon de plomb : une liste courte de six lignes "
  "décalées, deux ratures et deux traits de liaison entre les lignes. L'écriture est "
  "un tracé gris entièrement illisible, sans aucune lettre reconnaissable." + SANS_MOTS),
 ('expose-classe', 'images', P_EX, PERS + " Deux personnes debout devant un groupe "
  "d'adultes assis, vues de dos depuis le fond de la classe, l'une tenant une feuille. "
  "Un tableau blanc vierge derrière elles. Aucun visage visible." + SANS_MOTS),

 # ── Les quatorze photos du banc de vocabulaire ───────────────────────────
 ('travail-de-recherche', 'vocab', P_VOC, PERS + " Trois adultes assis autour d'une "
  "table, vus de trois quarts arrière, penchés sur des papiers étalés et un carnet "
  "ouvert. Les pages ne portent que des traits gris illisibles." + SANS_MOTS),
 ('sujet-de-recherche', 'vocab', P_VOC, STYLE + " Gros plan sur une feuille posée sur "
  "une table, portant une liste numérotée de huit lignes courtes dont une est entourée "
  "au crayon. Toutes les lignes sont des traits gris entièrement illisibles." + SANS_MOTS),
 ('compte-rendu', 'vocab', P_VOC, STYLE + " Gros plan sur deux feuilles agrafées "
  "posées sur un bureau, montrant la disposition d'un texte court : un titre, trois "
  "paragraphes séparés par des blancs, une liste au bas de la page. Chaque ligne est "
  "un trait gris illisible." + SANS_MOTS),
 ('expose', 'vocab', P_VOC, PERS + " Une personne debout devant un groupe assis dans "
  "une classe, vue de dos et de loin, une petite feuille à la main, l'autre main "
  "ouverte en train d'expliquer. Tableau blanc vierge au fond." + SANS_MOTS),
 ('echeance', 'vocab', P_VOC, STYLE + " Gros plan sur un calendrier mural de bureau, "
  "une case entourée deux fois au marqueur rouge pâle. Les chiffres et les noms de "
  "jours sont des traits gris entièrement illisibles. Une punaise en haut." + SANS_MOTS),
 ('consigne-de-travail', 'vocab', P_VOC, STYLE + " Une feuille imprimée recto tenue "
  "à la verticale contre une table claire : un en-tête, cinq paragraphes de longueurs "
  "inégales, une dernière ligne isolée en bas. Toutes les lignes sont des traits gris "
  "illisibles." + SANS_MOTS),
 ('grille-evaluation', 'vocab', P_VOC, STYLE + " Gros plan sur une feuille portant un "
  "tableau à deux colonnes et quatre rangées, avec une rangée de total en bas, tracé "
  "en traits fins. Chaque cellule ne contient que des traits gris illisibles. Un stylo "
  "repose sur le coin." + SANS_MOTS),
 ('plan-de-travail', 'vocab', P_VOC, STYLE + " Gros plan sur un carnet à spirale "
  "ouvert, page de gauche vierge, page de droite portant une liste manuscrite de cinq "
  "lignes avec des puces. L'écriture est un tracé gris entièrement illisible." + SANS_MOTS),
 ('source', 'vocab', P_VOC, STYLE + " Gros plan sur trois documents empilés en "
  "éventail sur une table : un journal, une page imprimée et une brochure pliée, de "
  "sorte qu'on voie un coin de chacun. Toutes les lignes sont des traits gris "
  "illisibles." + SANS_MOTS),
 ('article-informatif', 'vocab', P_VOC, STYLE + " Gros plan sur une page de journal "
  "ouverte à plat : deux colonnes de texte, un titre en haut et une petite photo "
  "carrée floue en médaillon. Chaque ligne de texte est un trait gris entièrement "
  "illisible." + SANS_MOTS),
 ('bulletin-municipal', 'vocab', P_VOC, STYLE + " Gros plan sur un journal mince en "
  "papier glacé posé sur une table de cuisine, plié en deux, à côté d'une enveloppe "
  "et d'une tasse. On distingue la disposition d'une première page — bandeau, grande "
  "image, trois blocs de texte — dont chaque ligne est un trait gris illisible." + SANS_MOTS),
 ('courrier-des-lecteurs', 'vocab', P_VOC, STYLE + " Gros plan sur une page de "
  "journal montrant quatre courts blocs de texte séparés par des filets, chacun suivi "
  "d'une ligne plus courte en italique. Toutes les lignes sont des traits gris "
  "entièrement illisibles." + SANS_MOTS),
 ('bibliographie', 'vocab', P_VOC, STYLE + " Très gros plan sur le bas d'une page "
  "imprimée : un petit titre, un filet horizontal, puis trois entrées de deux lignes "
  "chacune, la deuxième ligne décalée vers la droite. Toutes les lignes sont des "
  "traits gris entièrement illisibles." + SANS_MOTS),
 ('citation', 'vocab', P_VOC, STYLE + " Très gros plan sur un paragraphe imprimé où "
  "une phrase est encadrée par deux guillemets français bien visibles et surlignée au "
  "marqueur jaune pâle. Le reste des lignes, guillemets exceptés, est un trait gris "
  "entièrement illisible." + SANS_MOTS),
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
