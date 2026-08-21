#!/usr/bin/env python3
"""Génère les 17 images de module-n8-emploi via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer ;
  · `vocab/`  — les onze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Voir `docs/chantier-tous-niveaux.md`.

Même précaution qu'au niveau 6, et pour la même raison : presque tout ce qu'on
photographie ici est du **papier écrit** — un relevé de paie, un ordre du jour,
un compte rendu. Le style interdit le texte lisible, donc chaque prompt demande
que les lignes de texte soient réduites à des traits gris. Une image où l'on
peut lire un mot d'anglais est à refaire.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n8-emploi/gen_images.py
  python3 build/contenu/module-n8-emploi/gen_images.py salle-reunion
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n8-emploi'
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
         "profondeur de champ. Milieu de travail québécois ordinaire — petit "
         "bureau, entrepôt, centre d'emploi de quartier —, palette sobre. "
         "Aucun texte lisible, aucune écriture déchiffrable, aucun logo, "
         "aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de travail au Québec "
        "avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de "
        "champ. Aucun visage reconnaissable, aucun texte, aucun logo, aucun "
        "filigrane.")

P_EX  = "Je découvre · Exercice 4 — Les lieux et les objets d'une semaine de travail"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('bons-commande', 'images', P_EX, STYLE + " Une pile de feuilles de bons de commande "
  "posée sur un bureau clair, à côté d'un clavier et d'une tasse. La feuille du dessus "
  "montre un tableau à colonnes et une dizaine de lignes. Strictly no letters, no words, "
  "no readable characters: chaque ligne de texte est un trait gris abstrait."),
 ('releve-paie-ecran', 'images', P_EX, STYLE + " Un écran d'ordinateur de bureau vu de "
  "trois quarts, affichant un tableau de chiffres en colonnes serrées sur fond blanc. "
  "Les chiffres et les en-têtes sont flous, illisibles, réduits à des traits gris. "
  "Une lampe de bureau à droite, un carnet fermé devant le clavier."),
 ('machine-cafe', 'images', P_EX, STYLE + " Un coin cuisine de petite entreprise : une "
  "machine à café posée sur un comptoir, deux tasses dépareillées, un évier et une "
  "armoire. Lumière de fin de matinée par une fenêtre latérale. Aucune personne, aucune "
  "inscription lisible."),
 ('salle-reunion', 'images', P_EX, STYLE + " Une petite salle de réunion vide : une table "
  "ovale, six chaises, un tableau blanc au fond portant quelques traits et une liste de "
  "trois lignes entièrement illisibles. Des feuilles et deux tasses sur la table. "
  "Lumière naturelle par une fenêtre à gauche."),
 ('entrepot-quincaillerie', 'images', P_EX, STYLE + " Des étagères métalliques d'atelier "
  "vues de près, chargées de petits bacs de plastique contenant des charnières, des vis "
  "et des poignées de métal. Étiquettes des bacs floues et illisibles. Éclairage d'atelier, "
  "aucune personne."),
 ('cours-du-soir', 'images', P_EX, PERS + " Une salle de classe d'adultes en début de "
  "soirée, vue du fond : quelques personnes assises de dos devant des ordinateurs "
  "portables, un écran de projection allumé mais flou au fond de la salle. Fenêtres "
  "sombres. Aucun visage, aucun texte lisible."),

 # ── Les onze photos du banc de vocabulaire ────────────────────────────
 ('description-taches', 'vocab', P_VOC, STYLE + " Un document de deux pages agrafées, "
  "posé à plat sur un bureau, montrant quatre blocs séparés par des intertitres plus "
  "foncés. Un stylo posé en travers. Tout le texte est flou et illisible."),
 ('suivi', 'vocab', P_VOC, PERS + " Une personne vue de dos, debout près d'une fenêtre "
  "de bureau, un téléphone à l'oreille et un carnet ouvert dans l'autre main. Le carnet "
  "montre quelques lignes manuscrites illisibles."),
 ('releve-paie', 'vocab', P_VOC, STYLE + " Une feuille de relevé de paie tenue entre deux "
  "doigts au-dessus d'une table, montrant deux colonnes de chiffres et un total encadré "
  "en bas. Aucun chiffre lisible : les colonnes sont des traits gris réguliers."),
 ('heures-supplementaires', 'vocab', P_VOC, STYLE + " Une horloge murale ronde de bureau "
  "indiquant une heure tardive, photographiée en légère contre-plongée devant une "
  "fenêtre où le jour tombe. Cadran sans chiffres lisibles, aiguilles nettes."),
 ('accuse-reception', 'vocab', P_VOC, STYLE + " Un écran de téléphone tenu à la main, "
  "montrant une courte fenêtre de message avec un en-tête et deux lignes. Le texte est "
  "flou et illisible ; une petite coche ronde est nette en bas à droite."),
 ('ordre-du-jour', 'vocab', P_VOC, STYLE + " Une feuille unique posée au centre d'une "
  "table de réunion, montrant une liste numérotée de cinq points bien espacés. Les "
  "numéros sont nets mais les libellés sont des traits gris illisibles. Deux tasses "
  "de café floues de part et d'autre."),
 ('compte-rendu', 'vocab', P_VOC, STYLE + " Un document d'une page posé sur un clavier "
  "d'ordinateur, montrant un titre, puis trois lignes courtes séparées par des espaces. "
  "Tout le texte est flou et illisible. Lumière douce de bureau."),
 ('echeance', 'vocab', P_VOC, STYLE + " Un calendrier de bureau de papier, vu de face, "
  "montrant une grille de cases. Une seule case porte un large cercle tracé au crayon "
  "rouge. Aucune lettre ni aucun chiffre lisible : les en-têtes sont des traits gris."),
 ('perfectionnement', 'vocab', P_VOC, PERS + " Deux personnes assises côte à côte devant "
  "un ordinateur portable, vues de dos, l'une montrant l'écran du doigt à l'autre. Petit "
  "bureau, fin de journée. Écran flou et illisible."),
 ('conge-formation', 'vocab', P_VOC, STYLE + " Un sac à dos posé sur une chaise de bureau, "
  "avec un cahier neuf et un étui à crayons à côté, dans un bureau en fin de journée. "
  "Manteau accroché derrière. Aucune inscription lisible."),
 ('reconnaissance-acquis', 'vocab', P_VOC, STYLE + " Une chemise cartonnée ouverte sur une "
  "table, contenant plusieurs documents de formats différents légèrement décalés les uns "
  "sur les autres. Un des documents porte un sceau rond en relief, sans aucune lettre "
  "lisible. Le reste du texte est flou."),
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
