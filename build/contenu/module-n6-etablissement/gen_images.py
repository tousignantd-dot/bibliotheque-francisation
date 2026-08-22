#!/usr/bin/env python3
"""Les 18 images de module-n6-etablissement (niveau 6, activité 102).

Deux destinations :
  · `images/` — les six photos de l'exercice 4 de « Je découvre », réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les douze photos du banc de vocabulaire, réduites à 800 px
    qualité 82.

**Non exécuté au moment de la livraison du module** : les images coûtent de
l'argent réel et l'agent qui a produit le module n'était pas autorisé à les
générer. `node build/coherence.js module-n6-etablissement` sort donc 18 écarts
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

**Le sujet est le papier administratif** : presque chaque image de ce module
contient une feuille, un formulaire, un dépliant ou un tableau. Chaque prompt
exige donc que toute ligne de texte soit réduite à un trait gris. Une image où
l'on peut lire un mot — un mot d'anglais surtout — est à refaire. C'est la
contrainte la plus dure du module, et elle vaut pour les dix-huit.

**Aucun nom d'établissement réel, aucun logo, aucun visage.** Un avis officiel
qui porterait le nom d'un vrai centre serait un faux document ; les scènes
sont des lieux ordinaires et anonymes.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n6-etablissement/gen_images.py
  python3 build/contenu/module-n6-etablissement/gen_images.py comptoir-accueil
  python3 build/contenu/module-n6-etablissement/gen_images.py vocab/encadre
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n6-etablissement'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 4 — Les lieux d'un établissement"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : un centre d'éducation des adultes ordinaire d'une ville
# moyenne du Québec, lumière naturelle, rien de spectaculaire. Repris tel quel
# d'un module à l'autre, seule la palette change quand le thème l'exige.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle, faible "
         "profondeur de champ. Ville moyenne du Québec, intérieurs "
         "institutionnels ordinaires et sans luxe, palette sobre. Aucun texte "
         "lisible, aucun mot déchiffrable, aucun logo, aucune marque, aucun "
         "filigrane, aucune personne identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire dans un centre "
        "d'éducation des adultes au Québec, avec une ou deux personnes vues de "
        "dos, de trois quarts arrière ou hors cadrage du visage. Lumière "
        "naturelle douce, faible profondeur de champ. Aucun visage "
        "reconnaissable, aucun texte, aucun logo, aucun filigrane.")

# Le sujet du module oblige à cette phrase : presque toutes les images
# contiennent du papier imprimé, et un modèle d'image écrit volontiers de
# l'anglais dessus.
SANS_MOTS = (" Strictly no letters, no words, no readable characters anywhere "
             "in the image: every line of text, including any heading, label "
             "or form field, must be an abstract grey stroke. Aucun mot "
             "d'anglais nulle part, aucun nom d'établissement.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 4 ────────────────────────────────────
 ('comptoir-accueil', 'images', P_EX, PERS + " Le comptoir d'accueil d'un centre "
  "d'éducation des adultes : un plan de travail stratifié, une vitre basse, un "
  "présentoir de formulaires aux couvertures unies, deux personnes qui attendent de "
  "dos, à distance l'une de l'autre. Mur institutionnel neutre." + SANS_MOTS),
 ('bureau-orientation', 'images', P_EX, STYLE + " Un petit bureau fermé sans fenêtre : "
  "une table de travail, deux chaises face à face, un classeur à tiroirs, une pile de "
  "dépliants aux couvertures unies sur le coin de la table, une plante. Aucune "
  "personne, aucune affiche lisible au mur." + SANS_MOTS),
 ('classe-individualisee', 'images', P_EX, PERS + " Une classe d'adultes vue du fond : "
  "des tables individuelles espacées, chacune avec un cahier ouvert, quelques adultes "
  "penchés sur leur travail, vus de dos. Un tableau blanc au fond. Les pages des "
  "cahiers ne portent que des traits gris illisibles." + SANS_MOTS),
 ('avis-sur-table', 'images', P_EX, STYLE + " Une feuille officielle blanche posée sur "
  "une table de cuisine, à côté d'une tasse et d'un stylo, en fin d'après-midi. On "
  "distingue la disposition d'une lettre — un en-tête, un bloc d'adresse, trois "
  "paragraphes, un passage entouré d'un cadre, une ligne de signature — mais chaque "
  "ligne est un trait gris entièrement illisible." + SANS_MOTS),
 ('salle-de-rencontre', 'images', P_EX, STYLE + " Un local de réunion sans fenêtre : "
  "une table ovale, quatre chaises tournées vers elle, un tableau blanc vierge au fond, "
  "un chariot à projecteur dans un coin. Éclairage au plafond. Aucune personne, aucune "
  "inscription au tableau." + SANS_MOTS),
 ('laboratoire-pharmacie', 'images', P_EX, STYLE + " Un laboratoire d'école "
  "professionnelle : des comptoirs blancs alignés, des tiroirs à poignées numérotées "
  "sans chiffres lisibles, deux balances de précision, des contenants de plastique "
  "transparent vides et des étagères. Aucune personne, aucune étiquette lisible." + SANS_MOTS),

 # ── Les douze photos du banc de vocabulaire ───────────────────────────
 ('conseillere-orientation', 'vocab', P_VOC, PERS + " Une personne assise à un bureau "
  "dans un petit local fermé, vue de trois quarts arrière, penchée vers une feuille "
  "qu'elle annote, une deuxième chaise vide en face. Le visage est hors cadrage." + SANS_MOTS),
 ('dossier-scolaire', 'vocab', P_VOC, STYLE + " Gros plan sur un tiroir de classeur "
  "ouvert, rempli de chemises de carton beige aux onglets vierges, dans un bureau "
  "administratif. Une chemise est légèrement sortie. Aucune écriture lisible sur les "
  "onglets." + SANS_MOTS),
 ('releve-de-notes', 'vocab', P_VOC, STYLE + " Gros plan sur une feuille imprimée posée "
  "sur une table de bois : on distingue un en-tête et un tableau à trois colonnes, "
  "chaque rangée étant une suite de traits gris entièrement illisibles. Un stylo repose "
  "à côté." + SANS_MOTS),
 ('enseignement-individualise', 'vocab', P_VOC, PERS + " Un adulte vu de dos, seul à sa "
  "table dans une classe, penché sur un cahier d'exercices ouvert, une autre table "
  "occupée en arrière-plan flou. Les pages ne portent que des traits gris illisibles." + SANS_MOTS),
 ('programme-etudes', 'vocab', P_VOC, STYLE + " Gros plan sur un dépliant institutionnel "
  "ouvert, posé à plat sur une table : une photo en médaillon, deux colonnes de texte et "
  "un encadré, toutes les lignes étant des traits gris illisibles. Couverture unie, sans "
  "logo." + SANS_MOTS),
 ('formation-professionnelle', 'vocab', P_VOC, STYLE + " Un atelier d'école "
  "professionnelle vu de l'entrée : des postes de travail alignés, des tabourets, des "
  "outils rangés sur un panneau perforé, un éclairage industriel. Aucune personne, "
  "aucune affiche lisible." + SANS_MOTS),
 ('evaluation-comparative', 'vocab', P_VOC, STYLE + " Gros plan sur deux documents "
  "posés côte à côte sur une table : un diplôme ancien légèrement jauni et une feuille "
  "officielle récente, toutes leurs lignes étant des traits gris illisibles. Un sceau "
  "en relief sans motif reconnaissable sur le premier." + SANS_MOTS),
 ('avis-officiel', 'vocab', P_VOC, STYLE + " Gros plan sur une enveloppe blanche ouverte "
  "et la feuille qu'on en a tirée, posées sur une table de cuisine. La feuille montre la "
  "disposition d'une lettre officielle, chaque ligne étant un trait gris illisible." + SANS_MOTS),
 ('admission-conditionnelle', 'vocab', P_VOC, STYLE + " Gros plan sur une feuille "
  "officielle où un paragraphe est entouré d'un cadre net et souligné au crayon, le "
  "reste de la page restant pâle. Toutes les lignes sont des traits gris illisibles." + SANS_MOTS),
 ('encadre', 'vocab', P_VOC, STYLE + " Très gros plan sur une partie de document "
  "imprimé : un rectangle tramé en gris pâle, bordé d'un trait plus foncé, contenant "
  "trois lignes plus courtes que celles du reste de la page. Toutes les lignes sont des "
  "traits gris entièrement illisibles." + SANS_MOTS),
 ('rencontre-de-suivi', 'vocab', P_VOC, PERS + " Quatre personnes assises autour d'une "
  "table ovale dans un local de réunion, vues de loin et de dos ou de trois quarts "
  "arrière, des papiers devant chacune. Les visages sont hors cadrage." + SANS_MOTS),
 ('plan-de-formation', 'vocab', P_VOC, STYLE + " Gros plan sur une feuille posée sur une "
  "table, montrant un tableau à quatre colonnes et huit rangées, avec deux cases "
  "surlignées au marqueur pâle. Toutes les lignes sont des traits gris illisibles. Un "
  "crayon repose en travers." + SANS_MOTS),
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
