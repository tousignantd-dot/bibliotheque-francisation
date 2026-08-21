#!/usr/bin/env python3
"""Génère les 18 images de module-n2-bonjour via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer,
    telles que rendues ;
  · `vocab/`  — les douze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdait le tiers du haut et du bas. Voir
`docs/chantier-tous-niveaux.md`.

La difficulté propre à ce module : **il porte sur des gens qui se parlent**,
et le générateur a l'ordre de ne montrer aucune personne identifiable. Les
prompts demandent donc des silhouettes de dos, des mains, des pieds, ou la
pièce juste après que la personne est passée. Le geste se lit — se croiser,
tenir une porte, marcher — sans qu'aucun visage n'apparaisse.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n2-bonjour/gen_images.py
  python3 build/contenu/module-n2-bonjour/gen_images.py entree-immeuble
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n2-bonjour'
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

SANS = ("Aucun texte lisible, aucune écriture, aucun logo, aucune marque, "
        "aucun filigrane, aucun visage, aucune personne identifiable — les "
        "personnes, s'il y en a, sont vues de dos ou cadrées sans le visage.")

# Le décor principal : un petit immeuble locatif de quartier, à Montréal.
IMMEUBLE = ("Photographie réaliste, format paysage, lumière naturelle douce. "
            "Petit immeuble locatif de quartier au Québec : brique, boiseries "
            "peintes, plancher usé, palette sobre et chaude. " + SANS)

# Ce qui se passe à la maison, autour de la table.
CUISINE = ("Photographie réaliste, format paysage, lumière naturelle de jour "
           "par une fenêtre. Table de cuisine en bois d'un appartement "
           "modeste. Palette chaude et sobre. " + SANS)

# La rue du quartier, et le trajet à pied.
RUE = ("Photographie réaliste, format paysage, lumière naturelle. Rue "
       "résidentielle d'un quartier de Montréal : escaliers extérieurs, "
       "trottoir, arbres. Palette sobre. " + SANS)

# Le centre de formation des adultes.
CENTRE = ("Photographie réaliste, format paysage, lumière naturelle et néons "
          "doux. Salle de classe d'un centre de formation pour adultes : "
          "tables simples, chaises, tableau blanc, palette neutre. " + SANS)

P_EX  = "Je découvre · Exercice 3 — Le moment et le lieu"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('entree-immeuble', 'images', P_EX, IMMEUBLE + " Le hall d'entrée : une rangée "
  "de boîtes aux lettres de métal, une porte vitrée qui donne sur la rue, et "
  "deux silhouettes de dos qui se croisent près de la porte."),
 ('matin-dejeuner', 'images', P_EX, CUISINE + " Le déjeuner du matin : une "
  "assiette de rôties, une tasse de café fumante, un couteau, la lumière "
  "rasante du matin sur la nappe."),
 ('apres-midi-centre', 'images', P_EX, CENTRE + " La salle vue depuis le fond : "
  "des cahiers ouverts et des crayons sur les tables, quelques silhouettes de "
  "dos assises, la lumière d'après-midi par les fenêtres."),
 ('soir-fenetre', 'images', P_EX, IMMEUBLE + " Le soir dans un logement : une "
  "fenêtre où il fait noir dehors, le reflet d'une lampe allumée dans la "
  "vitre, une tasse posée sur le rebord."),
 ('porte-tenue', 'images', P_EX, IMMEUBLE + " Une main tient ouverte la porte "
  "d'entrée de l'immeuble pendant qu'une silhouette de dos passe avec deux "
  "sacs d'épicerie en papier."),
 ('carte-table', 'images', P_EX, CUISINE + " Une carte de vœux ouverte, posée "
  "debout sur la table à côté d'un stylo. L'écriture manuscrite se devine "
  "comme forme mais aucun mot ne se lit."),

 # ── Les douze photos du banc de vocabulaire ───────────────────────────
 ('voisin', 'vocab', P_VOC, IMMEUBLE + " Deux silhouettes de dos qui se croisent "
  "dans un couloir d'étage, l'une la main levée pour saluer l'autre."),
 ('immeuble', 'vocab', P_VOC, RUE + " La façade d'un immeuble de trois étages en "
  "brique, avec son escalier extérieur en fer et ses balcons, vue de la rue."),
 ('matin', 'vocab', P_VOC, RUE + " La même rue au petit matin : lumière rasante "
  "et dorée, trottoir vide, longues ombres."),
 ('soir', 'vocab', P_VOC, RUE + " La même rue le soir : ciel bleu foncé, "
  "lampadaires allumés, fenêtres éclairées."),
 ('apres-midi', 'vocab', P_VOC, CUISINE + " Des cahiers et un manuel ouverts sur "
  "la table, un crayon posé dessus, la lumière jaune du milieu de l'après-midi."),
 ('dejeuner', 'vocab', P_VOC, CUISINE + " Gros plan sur une assiette de rôties "
  "beurrées et une tasse de café, vue de trois quarts."),
 ('centre', 'vocab', P_VOC, CENTRE + " Le devant de la classe : un tableau blanc "
  "vide, un bureau, deux rangées de tables inoccupées."),
 ('a-pied', 'vocab', P_VOC, RUE + " Gros plan sur des pieds en bottes qui "
  "marchent sur un trottoir, cadré aux genoux, en mouvement."),
 ('travailler', 'vocab', P_VOC, "Photographie réaliste, format paysage, lumière "
  "de néons doux. Le comptoir d'une petite pharmacie de quartier, vu de "
  "derrière : des mains rangent des boîtes sur une tablette. " + SANS),
 ('porte', 'vocab', P_VOC, IMMEUBLE + " La porte d'entrée d'un logement, "
  "entrouverte, avec sa poignée de laiton usée, vue du palier."),
 ('carte-voeux', 'vocab', P_VOC, CUISINE + " Une carte de vœux blanche, ouverte "
  "et debout sur la table, avec une petite fleur imprimée sur le devant et "
  "une enveloppe à côté."),
 ('fete', 'vocab', P_VOC, CUISINE + " Un petit gâteau rond posé sur une "
  "assiette, avec deux bougies allumées, dans une pièce un peu sombre."),
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
