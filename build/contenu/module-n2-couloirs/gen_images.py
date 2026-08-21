#!/usr/bin/env python3
"""Génère les 18 images de module-n2-couloirs via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer ;
  · `vocab/`  — les douze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdait le tiers du haut et du bas. Voir
`docs/chantier-tous-niveaux.md`.

La difficulté propre à ce module est l'inverse de celle du module de la salle
de classe : ici, **tout est un couloir**, et un couloir ressemble à un
couloir. Les prompts changent donc de point de vue à chaque fois — le corridor
en enfilade, la cage d'escalier vue d'en bas, la porte d'ascenseur en gros
plan, le comptoir d'accueil de trois quarts, la rangée de casiers rasante.

Deuxième difficulté, et elle est sérieuse ici : **le sujet du module est un
numéro écrit sur une porte**, et le générateur a l'ordre de ne produire aucun
texte lisible. On ne demande donc jamais le chiffre. Les plaques, les affiches
et le plan mural sont demandés flous, de biais ou hors foyer : l'élève lit les
numéros dans le bandeau noir de l'exercice, pas sur la photo. Aucune personne
identifiable non plus — les silhouettes sont de dos.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n2-couloirs/gen_images.py
  python3 build/contenu/module-n2-couloirs/gen_images.py corridor-etage
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n2-couloirs'
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

SANS = ("Aucun texte lisible, aucun mot déchiffrable, aucune écriture "
        "reconnaissable, aucun chiffre, aucun numéro, aucun logo, aucune "
        "marque, aucun filigrane, aucun visage, aucune personne identifiable "
        "— les personnes, s'il y en a, sont vues de dos ou cadrées sans le "
        "visage. L'écriture et les numéros, quand il y en a, se lisent comme "
        "des traits gris flous, hors foyer.")

# Le décor principal : le corridor d'un centre de formation aux adultes, au
# Québec. Néons, blocs de béton peints, tuiles de plancher, portes de bois.
CORRIDOR = ("Photographie réaliste, format paysage, lumière de néons. "
            "Corridor d'un centre de formation pour adultes au Québec : murs "
            "de blocs peints pâles, plancher de tuiles, portes de bois clair "
            "alignées. Palette neutre et froide, calme. " + SANS)

# La cage d'escalier et les circulations verticales.
ESCALIER = ("Photographie réaliste, format paysage, lumière mêlée de néons et "
            "de fenêtre. Cage d'escalier d'un bâtiment public : marches de "
            "béton, main courante de métal peint, mur pâle. Palette sobre. "
            + SANS)

# Les endroits ouverts du rez-de-chaussée.
ENTREE = ("Photographie réaliste, format paysage, lumière du jour entrant par "
          "de grandes portes vitrées. Hall d'entrée d'un centre de formation "
          "pour adultes : sol de tuiles, mobilier simple, palette neutre. "
          + SANS)

P_EX  = "Je découvre · Exercice 3 — Les endroits du centre"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('corridor-etage', 'images', P_EX, CORRIDOR + " Le corridor vu en enfilade "
  "depuis le milieu, portes fermées des deux côtés, point de fuite au fond, "
  "personne dedans."),
 ('escalier-centre', 'images', P_EX, ESCALIER + " L'escalier vu d'en bas, les "
  "marches montant vers un palier éclairé, main courante au premier plan."),
 ('ascenseur-porte', 'images', P_EX, CORRIDOR + " Gros plan de trois quarts "
  "sur une porte d'ascenseur en acier brossé fermée, avec son bouton d'appel "
  "rond éclairé sur le mur à côté."),
 ('salle-casiers', 'images', P_EX, CORRIDOR + " Une longue rangée de casiers "
  "de métal peints, vue en perspective rasante le long du mur, une porte de "
  "casier entrouverte au premier plan."),
 ('cafeteria-centre', 'images', P_EX, ENTREE + " Une salle à manger de centre "
  "de formation vue du fond : tables rectangulaires et chaises légères, "
  "grandes fenêtres à gauche, salle vide."),
 ('comptoir-accueil', 'images', P_EX, ENTREE + " Un comptoir d'accueil de "
  "trois quarts, dessus dégagé, une chaise derrière, un présentoir de "
  "dépliants sur le côté."),

 # ── Les douze photos du banc de vocabulaire ───────────────────────────
 ('corridor', 'vocab', P_VOC, CORRIDOR + " Le corridor vu de côté, la lumière "
  "des néons se reflétant sur le plancher de tuiles ciré, portes fermées."),
 ('escalier', 'vocab', P_VOC, ESCALIER + " Les marches vues d'en haut, en "
  "plongée, tournant vers le palier de l'étage du dessous."),
 ('ascenseur', 'vocab', P_VOC, CORRIDOR + " Une porte d'ascenseur ouverte sur "
  "une cabine vide éclairée, vue de face depuis le corridor."),
 ('porte', 'vocab', P_VOC, CORRIDOR + " Gros plan sur une porte de classe "
  "fermée avec sa petite fenêtre vitrée et sa plaque de métal vierge à côté, "
  "la plaque hors foyer."),
 ('plan', 'vocab', P_VOC, ENTREE + " Un grand panneau mural encadré montrant "
  "un plan schématique d'étage, vu de biais : des rectangles et des lignes "
  "grises, aucune inscription lisible."),
 ('casier', 'vocab', P_VOC, CORRIDOR + " Gros plan sur trois portes de casier "
  "de métal peint avec leurs loquets, cadenas absents, peinture un peu usée."),
 ('secretariat', 'vocab', P_VOC, ENTREE + " Un petit bureau administratif vu "
  "depuis la porte : un comptoir bas, un classeur, une chaise de bureau "
  "vide, lumière douce."),
 ('accueil', 'vocab', P_VOC, ENTREE + " Le hall d'entrée vu de la porte : "
  "comptoir à droite, quelques chaises contre le mur, sol de tuiles clair."),
 ('cafeteria', 'vocab', P_VOC, ENTREE + " Gros plan sur deux tables de "
  "cafétéria avec leurs chaises, un plateau vide posé sur l'une d'elles."),
 ('toilettes', 'vocab', P_VOC, CORRIDOR + " Une porte de toilettes publiques "
  "entrouverte au bout d'un corridor, laissant voir un mur de tuiles et un "
  "lavabo, plaque de porte floue."),
 ('sortie', 'vocab', P_VOC, ENTREE + " Des portes vitrées de sortie vues de "
  "l'intérieur, la lumière du jour derrière, barre horizontale d'ouverture "
  "au premier plan."),
 ('bibliotheque', 'vocab', P_VOC, ENTREE + " Une petite bibliothèque de "
  "centre de formation : deux rayonnages de livres, une table de travail "
  "avec quatre chaises, lampe allumée, salle vide."),
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
