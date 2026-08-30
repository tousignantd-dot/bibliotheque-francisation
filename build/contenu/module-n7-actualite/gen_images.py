#!/usr/bin/env python3
"""Génère les 13 images de module-n7-actualite via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer ;
  · `vocab/`  — les sept photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Voir `docs/chantier-tous-niveaux.md`.

La précaution du niveau 6 vaut doublement ici : le sujet est l'information
écrite et parlée, donc presque chaque image contient du papier, un écran ou
un micro. Chaque prompt exige que toute ligne de texte soit réduite à un
trait gris. Une image où l'on peut lire un mot — surtout un mot d'anglais —
est à refaire.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n7-actualite/gen_images.py
  python3 build/contenu/module-n7-actualite/gen_images.py studio-radio
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n7-actualite'
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
         "profondeur de champ. Quartier résidentiel québécois ordinaire — "
         "petit studio de radio communautaire, salle municipale, rue "
         "commerçante —, palette sobre. Aucun texte lisible, aucune écriture "
         "déchiffrable, aucun logo, aucun filigrane, aucune personne "
         "identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie de quartier "
        "au Québec avec une ou deux personnes vues de dos, de trois quarts ou "
        "hors cadrage du visage. Lumière naturelle douce, faible profondeur "
        "de champ. Aucun visage reconnaissable, aucun texte, aucun logo, "
        "aucun filigrane.")

P_EX  = "Je découvre · Exercice 5 — Les lieux et les gestes de l'information"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('studio-radio', 'images', P_EX, STYLE + " L'intérieur d'un petit studio de radio "
  "communautaire : une console de mixage avec ses glissières, un micro sur bras "
  "articulé au premier plan, un casque d'écoute posé sur la table. Mur de mousse "
  "acoustique en arrière-plan. Aucune personne, aucune inscription lisible sur la "
  "console."),
 ('local-vide', 'images', P_EX, STYLE + " La devanture d'un local commercial vide au coin "
  "d'une rue, vitrine en partie placardée de panneaux de contreplaqué, porte fermée, "
  "affiche « à louer » réduite à un rectangle blanc sans aucune lettre. Trottoir de "
  "béton, fin d'automne, lumière grise."),
 ('salle-conseil', 'images', P_EX, STYLE + " Une salle de conseil municipal modeste vue "
  "du fond : une longue tribune surélevée avec des sièges vides et des micros sur pied, "
  "et devant elle des rangées de chaises pliantes pour le public. Aucune personne, "
  "aucune écriture lisible sur les panneaux."),
 ('contenants-sac', 'images', P_EX, STYLE + " Gros plan sur un grand sac de plastique "
  "transparent, posé sur un perron de béton, rempli de canettes d'aluminium et de "
  "bouteilles vides écrasées. Les étiquettes sont froissées et entièrement illisibles, "
  "sans aucune marque reconnaissable."),
 ('journal-etale', 'images', P_EX, STYLE + " Un journal de papier ouvert à plat sur une "
  "table de cuisine, à côté d'une tasse. La page montre un grand bandeau de titre en "
  "haut, une photographie et trois colonnes de texte. Strictly no letters, no words, no "
  "readable characters anywhere in the image: every line of text, including the "
  "headline, must be an abstract grey stroke. Aucun mot d'anglais nulle part."),
 ('micro-trottoir', 'images', P_EX, PERS + " Un journaliste vu de dos qui tend un micro "
  "à main vers une passante, sur un trottoir de rue commerçante. Les deux visages sont "
  "hors cadrage. Le micro n'a aucune inscription ni logo."),

 # ── Les sept photos du banc de vocabulaire ────────────────────────────
 ('reportage', 'vocab', P_VOC, PERS + " Sur le trottoir d'une rue commerçante, une journaliste vue de dos "
  "tend un enregistreur numérique vers une passante qui lui répond, "
  "cadrée de trois quarts arrière, visage hors champ, une main ouverte "
  "en l'air. L'enregistreur est net, boîtier nu, aucune inscription. La "
  "façade derrière elles est entièrement hors mise au point : aucune "
  "enseigne nette, aucun néon allumé."),
 ('blogue', 'vocab', P_VOC, STYLE + " Un ordinateur portable posé sur une table de "
  "cuisine le soir, affichant une page de blogue — un bloc de paragraphes et une zone "
  "de commentaires en dessous. L'écran est vu en biais et son contenu est délavé par "
  "le reflet de la fenêtre : aucun caractère n'est formé, tout se réduit à des bandes "
  "grises hors mise au point. Boîtier nu, aucun nom de fabricant."),
 ('source', 'vocab', P_VOC, STYLE + " Gros plan sur un carnet de notes à spirale ouvert, "
  "posé à côté d'un téléphone et d'un enregistreur, sur une table de café. Les lignes "
  "manuscrites du carnet sont des traits gris illisibles."),
 ('porte-parole', 'vocab', P_VOC, PERS + " Une personne debout derrière un lutrin de "
  "bois clair, vue de trois quarts arrière, le visage hors cadrage, devant deux micros. "
  "Mur neutre en arrière-plan. Aucune affiche, aucun logo, aucune écriture."),
 ('consigne', 'vocab', P_VOC, STYLE + " Gros plan sur deux mains qui déposent une canette "
  "d'aluminium vide dans l'ouverture d'une machine de retour de contenants, dans une "
  "petite salle éclairée au néon. Aucune étiquette lisible sur la canette, aucune "
  "inscription sur la machine."),
 ('entrevue-radio', 'vocab', P_VOC, PERS + " Deux personnes assises face à face de chaque "
  "côté d'une table de studio, chacune devant un micro sur bras articulé, vues de côté "
  "et de loin, les visages hors cadrage. Casques d'écoute sur les oreilles."),
 ('conseil', 'vocab', P_VOC, PERS + " Vue de dos, depuis les rangées du public, de "
  "quelques personnes assises sur des chaises pliantes qui regardent vers une tribune "
  "éclairée. Salle municipale ordinaire. Aucun visage, aucune écriture lisible."),
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
