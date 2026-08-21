#!/usr/bin/env python3
"""Génère les 24 images de module-n3-pharmacie via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les huit illustrations de l'exercice 3 de « Je découvre » ;
  · `vocab/`  — les seize photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdrait le tiers du haut et du bas.

**La difficulté propre à ce module est que ses objets portent des mots** —
une étiquette de flacon, une carte d'assurance maladie, une boîte de sirop —,
alors que le générateur a l'ordre de ne produire aucun texte lisible. Les
prompts demandent donc des objets dont la *forme* est nette : un petit flacon
orange, une étiquette blanche aux lignes régulières, une carte de plastique
tenue à la main, sans qu'aucun mot ne se lise. L'élève reconnaît l'objet ;
c'est l'exercice qui en donne le contenu. Aucune marque de médicament n'est
demandée : les boîtes et les bouteilles sont unies.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n3-pharmacie/gen_images.py
  python3 build/contenu/module-n3-pharmacie/gen_images.py flacon-etiquette
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n3-pharmacie'
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
         "profondeur de champ. Intérieur d'une pharmacie de quartier "
         "québécoise ordinaire : tablettes claires, sol pâle, comptoir de "
         "stratifié, palette sobre. Aucun texte lisible, aucune écriture, "
         "aucun logo, aucun filigrane, aucune personne identifiable.")

OBJET = ("Photographie réaliste, format paysage, gros plan sur un objet posé "
         "sur un comptoir clair, lumière naturelle douce, faible profondeur "
         "de champ. Aucun texte lisible, aucun logo, aucune marque, aucun "
         "filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Dans la pharmacie"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit images d'exercice ────────────────────────────────────────
 ('comptoir-fond', 'images', P_EX, STYLE + " Vue du fond d'une pharmacie : un "
  "comptoir surélevé devant un mur de tablettes remplies de petites boîtes "
  "unies, sans aucune inscription. Le comptoir est vide et net."),
 ('allee-sirops', 'images', P_EX, STYLE + " Une allée étroite entre deux "
  "rangées de tablettes, remplie de bouteilles et de boîtes de tailles "
  "différentes, toutes unies et sans étiquette lisible."),
 ('carte-main', 'images', P_EX, PERS + " Gros plan sur une main qui tend une "
  "carte de plastique par-dessus un comptoir. La carte est unie, d'un vert "
  "pâle, sans aucune inscription ni photo."),
 ('flacon-etiquette', 'images', P_EX, OBJET + " Un petit flacon de plastique "
  "orange avec un couvercle blanc, debout, une étiquette blanche collée "
  "dessus dont les lignes d'impression sont des traits gris illisibles."),
 ('pansement-doigt', 'images', P_EX, PERS + " Gros plan sur une main dont "
  "l'index porte un pansement beige, posée sur une table de bois clair."),
 ('thermometre', 'images', P_EX, OBJET + " Un thermomètre numérique blanc posé "
  "en diagonale sur un comptoir, son petit écran éteint et vide."),
 ('sac-pharmacie', 'images', P_EX, OBJET + " Un petit sac de papier blanc "
  "agrafé en haut, posé sur un comptoir, avec un flacon orange qui dépasse "
  "légèrement. Le papier est uni, sans impression."),
 ('salle-attente', 'images', P_EX, STYLE + " Trois chaises vides alignées "
  "contre un mur clair, près d'un comptoir, avec une petite table basse. "
  "Personne n'est assis."),

 # ── Les seize photos du banc de vocabulaire ───────────────────────────
 ('ordonnance', 'vocab', P_VOC, OBJET + " Une petite feuille de papier blanc "
  "pliée en deux, posée sur un comptoir à côté d'un stylo. Les lignes "
  "d'écriture sont des traits bleus entièrement illisibles."),
 ('comptoir-ordonnances', 'vocab', P_VOC, STYLE + " Un comptoir de pharmacie "
  "vu de trois quarts, un peu plus haut que les autres, avec un écran "
  "d'ordinateur sombre de côté et un mur de tiroirs derrière."),
 ('carte-assurance', 'vocab', P_VOC, OBJET + " Une carte de plastique vert "
  "pâle, unie, posée à plat sur un comptoir blanc, sans aucune inscription "
  "ni photo ni puce."),
 ('vente-libre', 'vocab', P_VOC, STYLE + " Une tablette de pharmacie à hauteur "
  "des yeux, remplie de bouteilles de sirop de tailles différentes, toutes "
  "unies et sans étiquette lisible."),
 ('tousser', 'vocab', P_VOC, PERS + " Une personne vue de trois quarts arrière, "
  "assise sur un divan, la main devant la bouche, une couverture sur les "
  "épaules. Le visage n'est pas reconnaissable."),
 ('fievre', 'vocab', P_VOC, PERS + " Une main qui pose un thermomètre "
  "numérique sur le front d'un enfant couché, vu de dos. Aucun visage "
  "reconnaissable, aucun chiffre lisible."),
 ('rhume', 'vocab', P_VOC, OBJET + " Une boîte de mouchoirs de papier blanche "
  "et unie posée sur une table de chevet, à côté d'une tasse fumante."),
 ('pansement', 'vocab', P_VOC, OBJET + " Trois pansements beiges de tailles "
  "différentes posés côte à côte sur une surface blanche, encore dans leur "
  "papier uni."),
 ('renouvellement', 'vocab', P_VOC, OBJET + " Deux flacons orange identiques "
  "posés côte à côte sur un comptoir, l'un vide et ouvert, l'autre plein et "
  "fermé. Les étiquettes sont blanches et illisibles."),
 ('dossier', 'vocab', P_VOC, STYLE + " Gros plan sur un écran d'ordinateur de "
  "comptoir vu de biais, affichant des lignes grises régulières entièrement "
  "illisibles, à côté d'un clavier."),
 ('assurance-medicaments', 'vocab', P_VOC, OBJET + " Un petit reçu de papier "
  "blanc posé à côté d'une carte de plastique verte unie, sur un comptoir. "
  "Les lignes du reçu sont des traits gris illisibles."),
 ('pharmacien', 'vocab', P_VOC, PERS + " Une personne en sarrau blanc, vue de "
  "trois quarts arrière derrière un comptoir de pharmacie, penchée sur des "
  "flacons. Aucun visage reconnaissable, aucun insigne lisible."),
 ('posologie', 'vocab', P_VOC, OBJET + " Gros plan très rapproché sur une "
  "étiquette blanche collée sur un flacon orange, dont les lignes de texte "
  "sont des traits gris parfaitement illisibles."),
 ('comprime', 'vocab', P_VOC, OBJET + " Trois comprimés blancs ronds posés "
  "dans le creux d'une main ouverte, au-dessus d'un comptoir clair. Aucune "
  "inscription sur les comprimés."),
 ('etiquette', 'vocab', P_VOC, OBJET + " Une bouteille de sirop brune couchée "
  "sur un comptoir, une étiquette blanche rectangulaire collée sur le côté, "
  "aux lignes grises illisibles."),
 ('effet-secondaire', 'vocab', P_VOC, PERS + " Une personne assise à une table "
  "de cuisine, vue de trois quarts arrière, la tête appuyée sur une main, un "
  "verre d'eau et un flacon orange devant elle."),
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
