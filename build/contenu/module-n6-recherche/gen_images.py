#!/usr/bin/env python3
"""Génère les 15 images de module-n6-recherche via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer ;
  · `vocab/`  — les neuf photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Voir `docs/chantier-tous-niveaux.md`.

Le sujet oblige à une précaution que les modules précédents n'avaient pas :
tout ce qu'on photographie ici est du **papier écrit** — une offre d'emploi,
un formulaire, une lettre. Le style interdit le texte lisible, donc chaque
prompt demande explicitement des lignes de texte réduites à des traits gris.
Une image où l'on peut lire un mot d'anglais est à refaire.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n6-recherche/gen_images.py
  python3 build/contenu/module-n6-recherche/gen_images.py entrevue-table
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n6-recherche'
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

P_EX  = "Je découvre · Exercice 4 — Les lieux et les gestes de la recherche"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('offre-ecran', 'images', P_EX, STYLE + " Un ordinateur portable posé sur une table "
  "de bois clair, vu de trois quarts, affichant une page d'offre d'emploi réduite à "
  "des blocs gris hors mise au point : aucun caractère n'est formé, ni dans le corps "
  "du texte ni en haut de la page. Boîtier nu : aucun logo de fabricant sur "
  "l'ordinateur, le repose-poignet et le cadre de l'écran sont entièrement lisses et "
  "nus, aucun nom de marque nulle part. Une tasse de café à côté."),
 ('entrepot', 'images', P_EX, STYLE + " L'intérieur d'un entrepôt de taille moyenne : "
  "de hautes étagères métalliques chargées de boîtes de carton et de palettes de bois, "
  "une allée centrale dégagée, un chariot élévateur au fond. Aucune personne au premier "
  "plan, aucune inscription lisible sur les boîtes."),
 ('entrevue-table', 'images', P_EX, STYLE + " Deux personnes assises de chaque côté d'une "
  "petite table de bureau, vues de côté et de loin, les visages hors cadrage. L'une tient "
  "un stylo au-dessus d'une feuille, l'autre a les mains posées sur la table. Cloison "
  "vitrée en arrière-plan. Aucune écriture lisible sur la feuille."),
 ('formulaire-papier', 'images', P_EX, STYLE + " Gros plan sur deux mains qui remplissent "
  "un formulaire de plusieurs pages avec un stylo bleu, sur une table claire. Le formulaire "
  "montre des cases et des lignes vides ; le peu de texte imprimé est flou et illisible."),
 ('conseillere-bureau', 'images', P_EX, PERS + " Deux personnes assises côte à côte devant "
  "un écran d'ordinateur, dans un petit bureau de centre d'emploi de quartier. L'une montre "
  "quelque chose à l'écran du doigt. Vues de dos et de trois quarts. Écran flou."),
 ('inventaire-tablette', 'images', P_EX, PERS + " Une personne vue de dos, dans une allée "
  "d'entrepôt, qui compte des boîtes sur une étagère en tenant une tablette électronique "
  "d'une main. Écran de la tablette flou et illisible."),

 # ── Les neuf photos du banc de vocabulaire ────────────────────────────
 ('cv', 'vocab', P_VOC, PERS + " Gros plan sur une main qui tend deux feuilles "
  "agrafées par-dessus un comptoir, vers une autre main qui vient les prendre. Les feuilles "
  "montrent une mise en page en colonnes, entièrement floue et illisible."),
 ('horaire', 'vocab', P_VOC, STYLE + " Un calendrier mural de papier vu de face, "
  "punaisé sur un mur clair, montrant une grille de cases de la semaine. Trois cases "
  "seulement portent une grande croix tracée au crayon rouge ; les autres sont vides. "
  "Aucune lettre, aucun chiffre lisible : les en-têtes sont des traits gris."),
 ('offre-emploi', 'vocab', P_VOC, STYLE + " Gros plan en biais sur une seule "
  "feuille de papier blanc punaisée sur un panneau de liège, dans un corridor. La feuille "
  "montre un bandeau plus foncé en haut et quatre blocs de paragraphes. Strictly no "
  "letters, no words, no readable characters anywhere in the image: every line of text "
  "must be an abstract grey stroke. Aucun mot d'anglais nulle part."),
 ('taches', 'vocab', P_VOC, STYLE + " Un carnet à spirale ouvert sur une table d'entrepôt, "
  "avec une liste de six lignes précédées de petites cases à cocher, dont deux sont cochées "
  "au crayon. Les lignes écrites sont des traits gris illisibles."),
 ('contrat', 'vocab', P_VOC, STYLE + " Un document de deux pages posé sur un bureau, avec "
  "un stylo noir déposé en travers et une ligne de signature vide en bas de la page. Tout "
  "le texte imprimé est flou et illisible."),
 ('formulaire', 'vocab', P_VOC, STYLE + " Une tablette électronique tenue à deux "
  "mains, montrant un formulaire en ligne : une suite de champs rectangulaires vides et de "
  "petites étiquettes. L'écran est net mais aucun mot n'est lisible — les étiquettes sont "
  "des traits gris."),
 ('lettre-motivation', 'vocab', P_VOC, STYLE + " Une feuille de papier pliée en "
  "trois, à demi glissée dans une enveloppe blanche posée sur un bureau sombre. On devine "
  "trois blocs de paragraphes sur la partie visible, entièrement illisibles."),
 ('entrevue', 'vocab', P_VOC, PERS + " Une poignée de main au-dessus d'une table de bureau, "
  "en gros plan sur les mains, les personnes coupées au niveau des épaules. Un dossier de "
  "papier fermé sur la table."),
 ('assurance', 'vocab', P_VOC, STYLE + " Une carte de plastique format portefeuille tenue "
  "entre deux doigts au-dessus d'un comptoir, sans aucune inscription lisible, avec un "
  "dépliant de papier flou en arrière-plan."),
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
