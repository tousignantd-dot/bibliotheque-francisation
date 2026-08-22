#!/usr/bin/env python3
"""Les 15 images de module-n6-emploi (niveau 6, activité 100).

Deux destinations :
  · `images/` — les cinq photos de l'exercice 4 de « Je découvre », réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les dix photos du banc de vocabulaire, réduites à 800 px
    qualité 82.

**Non exécuté au moment de la livraison du module** : les images coûtent de
l'argent réel et l'agent qui a produit le module n'était pas autorisé à les
générer. `node build/coherence.js module-n6-emploi` sort donc 15 écarts
« image absente du disque », tous attendus, et aucun autre.

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix mesuré le 21 août 2026 — Google direct,
puis fal.ai, puis WaveSpeed — rend le nom de celle qui a servi, et inscrit
chaque tentative au registre `~/Claude/generations/journal_appels.py`. Un
fournisseur facture des **appels**, pas des fichiers présents : une image
régénérée est payée chaque fois.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu écrit à la
main : ce fichier vit dans `build/contenu/<slug>/`, donc trois niveaux sous la
racine du dépôt. Les générateurs des modules précédents portaient le chemin en
dur et cessaient de fonctionner dès qu'on travaillait dans un worktree.

**Le sujet est l'écrit du milieu de travail** : presque chaque image contient
du papier, un babillard ou un formulaire. Chaque prompt exige donc que toute
ligne de texte soit réduite à un trait gris. Une image où l'on peut lire un
mot — un mot d'anglais surtout — est à refaire. C'est la contrainte la plus
forte de ce module : un babillard sans texte lisible demande d'insister.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n6-emploi/gen_images.py
  python3 build/contenu/module-n6-emploi/gen_images.py babillard-usine
  python3 build/contenu/module-n6-emploi/gen_images.py vocab/formulaire
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n6-emploi'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 4 — Les lieux et les papiers de la démarche"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : une usine d'emballages alimentaires de Saint-Hyacinthe,
# ordinaire, lumière de néon et lumière de fenêtre. Rien de spectaculaire,
# rien de publicitaire.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle ou "
         "éclairage de néon, faible profondeur de champ. Petite usine "
         "d'emballages alimentaires d'une ville moyenne du Québec, locaux "
         "ordinaires et un peu usés, palette sobre. Aucun texte lisible, "
         "aucun mot déchiffrable, aucun logo, aucune marque, aucun "
         "filigrane, aucune personne identifiable, aucun visage "
         "reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène de travail ordinaire au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts "
        "arrière ou hors cadrage du visage. Lumière naturelle douce, faible "
        "profondeur de champ. Aucun visage reconnaissable, aucun texte, aucun "
        "logo, aucun filigrane.")

# Le sujet du module oblige à cette phrase : presque toutes les images
# contiennent du papier imprimé, et un modèle d'image écrit volontiers de
# l'anglais sur un formulaire.
SANS_MOTS = (" Strictly no letters, no words, no readable characters anywhere "
             "in the image: every line of text, including any headline, form "
             "field or label, must be an abstract grey stroke. Aucun mot "
             "d'anglais nulle part.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les cinq images de l'exercice 4 ───────────────────────────────────
 ('babillard-usine', 'images', P_EX, STYLE + " Un babillard de liège fixé au mur "
  "d'un couloir d'usine, à côté d'une porte de vestiaire. Quelques feuilles blanches "
  "punaisées, dont une plus grande et plus récente, légèrement de travers. Un cadre "
  "d'aluminium, une lumière de néon au plafond, un plancher de béton peint. Aucune "
  "personne. Toutes les lignes des feuilles sont des traits gris entièrement "
  "illisibles." + SANS_MOTS),
 ('bureau-ressources-humaines', 'images', P_EX, STYLE + " Un petit bureau administratif "
  "au bout d'un couloir d'usine : une table de travail, un écran d'ordinateur éteint, "
  "un classeur métallique à tiroirs, deux chaises dont une du côté visiteur, un "
  "présentoir de formulaires aux feuilles blanches. Une fenêtre donnant sur un "
  "stationnement. Aucune personne, aucune inscription lisible." + SANS_MOTS),
 ('atelier-conditionnement', 'images', P_EX, STYLE + " L'intérieur d'un atelier "
  "d'emballage alimentaire : un convoyeur à rouleaux, des boîtes de carton brun "
  "ouvertes, une balance de plancher, des étagères de rangement en arrière-plan. "
  "Plancher de béton, éclairage de néon. Aucune personne, aucune étiquette lisible sur "
  "les boîtes." + SANS_MOTS),
 ('formulaire-rempli', 'images', P_EX, STYLE + " Gros plan en légère plongée sur une "
  "feuille de papier blanche posée sur une table, remplie à la main au stylo bleu. On "
  "distingue nettement la disposition d'un formulaire — un bandeau en haut, des cases "
  "rectangulaires, une ligne de signature en bas — mais chaque ligne écrite et chaque "
  "libellé sont des traits gris entièrement illisibles. Un stylo posé à côté." + SANS_MOTS),
 ('cafeteria-rencontre', 'images', P_EX, STYLE + " La cafétéria d'une petite usine, "
  "vide, en milieu d'après-midi : de longues tables et des chaises de plastique "
  "alignées face à un mur nu, une machine à café au fond, de grandes fenêtres à droite. "
  "Quelques chaises sont tournées vers l'avant de la salle, comme pour une réunion. "
  "Aucune personne, aucune affiche lisible." + SANS_MOTS),

 # ── Les dix photos du banc de vocabulaire ─────────────────────────────
 ('babillard', 'vocab', P_VOC, STYLE + " Gros plan sur un babillard de liège avec "
  "quatre ou cinq feuilles blanches punaisées à des hauteurs différentes, et des "
  "punaises de couleur. Toutes les lignes des feuilles sont des traits gris "
  "illisibles." + SANS_MOTS),
 ('affichage-interne', 'vocab', P_VOC, STYLE + " Gros plan sur une seule feuille "
  "blanche punaisée au centre d'un babillard, plus grande que les autres et bien "
  "droite. On voit la disposition d'une annonce — un titre en haut, un bloc de "
  "paragraphes, une liste à puces — mais toutes les lignes sont des traits gris "
  "illisibles." + SANS_MOTS),
 ('candidature-interne', 'vocab', P_VOC, PERS + " Une personne vue de dos, debout "
  "devant un comptoir de bureau, qui tend une feuille de papier par-dessus le "
  "comptoir. Les visages sont hors cadrage et la feuille ne porte que des traits gris "
  "illisibles." + SANS_MOTS),
 ('ressources-humaines', 'vocab', P_VOC, STYLE + " Le coin d'un petit bureau "
  "administratif : un classeur métallique à tiroirs entrouvert, des chemises de carton "
  "debout à l'intérieur, une plante et une lampe sur le dessus. Aucune personne, aucune "
  "étiquette lisible sur les chemises." + SANS_MOTS),
 ('formulaire', 'vocab', P_VOC, STYLE + " Gros plan serré sur une feuille de "
  "formulaire vierge posée sur une table de bois, avec ses cases rectangulaires, ses "
  "lignes à remplir et un stylo posé en travers. Tous les libellés sont des traits gris "
  "illisibles." + SANS_MOTS),
 ('comite-selection', 'vocab', P_VOC, PERS + " Deux personnes assises côte à côte "
  "derrière une table, vues de trois quarts arrière depuis le fond de la salle, face à "
  "une chaise vide de l'autre côté. Des feuilles et deux tasses sur la table. Les "
  "visages sont hors cadrage." + SANS_MOTS),
 ('periode-essai', 'vocab', P_VOC, PERS + " Une personne vue de dos, en sarrau clair "
  "et filet à cheveux, debout devant un convoyeur d'atelier d'emballage, une planchette "
  "à pince à la main. Le visage est hors cadrage et la feuille de la planchette ne "
  "porte que des traits gris." + SANS_MOTS),
 ('note-de-service', 'vocab', P_VOC, STYLE + " Gros plan sur une feuille blanche "
  "imprimée posée à plat sur une table de cafétéria, à côté d'une tasse. On distingue "
  "la disposition d'une note — trois lignes d'en-tête, un paragraphe, trois puces, un "
  "encadré gris en bas — mais chaque ligne est un trait gris entièrement "
  "illisible." + SANS_MOTS),
 ('compte-rendu', 'vocab', P_VOC, STYLE + " Gros plan sur deux feuilles agrafées "
  "posées sur une table, montrant la disposition d'un compte rendu : un bloc d'en-tête, "
  "une liste numérotée, des paragraphes courts séparés par des blancs. Toutes les "
  "lignes sont des traits gris illisibles." + SANS_MOTS),
 ('ordre-du-jour', 'vocab', P_VOC, STYLE + " Gros plan sur une petite feuille posée "
  "sur une table de réunion, montrant trois lignes numérotées bien espacées et rien "
  "d'autre, à côté d'un stylo. Les trois lignes sont des traits gris "
  "illisibles." + SANS_MOTS),
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
