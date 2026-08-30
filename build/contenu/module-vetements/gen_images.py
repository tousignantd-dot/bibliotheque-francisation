#!/usr/bin/env python3
"""Génère les 21 images du module-vetements via fal.ai (Nano Banana 2).

Deux destinations, deux formats :
  · `images/` — les illustrations d'exercice, 1024 px, telles que rendues ;
  · `vocab/`  — les photos du banc de vocabulaire, réduites à 800 px / q. 82.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-vetements/gen_images.py
  python3 build/contenu/module-vetements/gen_images.py tournoi balcon
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-vetements'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
ENV  = pathlib.Path('/Users/danieltousignant/Claude/.env')


def cle(nom):
    for ligne in ENV.read_text(encoding='utf-8').splitlines():
        ligne = ligne.strip()
        if ligne.startswith(nom + '='):
            return ligne.split('=', 1)[1].strip().strip('"\'')
    return ''


FAL = cle('FAL_KEY')
if not FAL:
    sys.exit('FAL_KEY absente de ~/Claude/.env')

# Le décor est celui de CE module. La phrase « Rue ou transport en commun »
# qui tenait ici venait de module-deplacement, recopiée par erreur : le
# générateur la prenait au mot et servait les assiettes dans un autobus.
STYLE = ("Photographie réaliste, format paysage 3:2, lumière naturelle de jour, faible "
         "profondeur de champ. Magasin de vêtements de quartier au Québec, "
         "présentoirs et portants ordinaires, palette sobre. "
         "Aucun texte lisible, aucune écriture, aucun logo, "
         "aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage 3:2, scène de la vie quotidienne au Québec "
        "avec une ou deux personnes vues de dos, de trois quarts ou hors cadrage du "
        "visage. Lumière naturelle douce, faible profondeur de champ. Aucun visage "
        "reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Dans le magasin"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit images d'exercice ────────────────────────────────────────
 ('rayon-manteaux', 'images', P_EX, STYLE + " Un présentoir de manteaux d'hiver suspendus "
  "sur une tringle, vus de face : parkas foncés à capuchon, alignés serrés. Éclairage de "
  "magasin, plancher clair."),
 ('cabines', 'images', P_EX, STYLE + " Une rangée de cabines d'essayage fermées par des "
  "rideaux de tissu foncé, dans un couloir de magasin. Petit banc et miroir au bout du "
  "couloir."),
 ('etiquette-col', 'images', P_EX, STYLE + " Gros plan sur une petite étiquette de tissu "
  "blanche cousue dans le col d'un manteau, portant une série de petits pictogrammes "
  "noirs alignés. Les symboles sont visibles mais les mots restent illisibles."),
 ('bottes-hiver', 'images', P_EX, STYLE + " Une paire de bottes d'hiver noires posées côte "
  "à côte sur un plancher de magasin, l'une inclinée pour montrer la semelle à gros "
  "relief."),
 ('miroir-essayage', 'images', P_EX, STYLE + " Un grand miroir sur pied dans un coin de "
  "magasin de vêtements, avec un tabouret bas à côté et un portemanteau vide. Personne "
  "dans le reflet."),
 ('comptoir-service', 'images', P_EX, STYLE + " Un comptoir de service à la clientèle dans "
  "un magasin : dessus de mélamine claire, terminal de paiement, petite pile de sacs "
  "pliés. Aucune inscription."),
 ('facture-sac', 'images', P_EX, STYLE + " Un sac de magasin en papier posé sur une table, "
  "avec un ruban de caisse dépassant du haut. Les chiffres du reçu restent flous et "
  "illisibles."),
 ('capuchon-fourrure', 'images', P_EX, STYLE + " Gros plan sur le capuchon d'un manteau "
  "d'hiver bordé de fourrure épaisse, vu de trois quarts, posé sur un mannequin sans "
  "tête."),

 # ── Les treize mots du banc de vocabulaire ────────────────────────────
 ('manteau', 'vocab', P_VOC, STYLE + " Un manteau d'hiver noir à capuchon, suspendu seul "
  "sur un cintre devant un mur clair, vu de face. Fermeture éclair visible."),
 ('cabine', 'vocab', P_VOC, STYLE + " Une cabine d'essayage ouverte, rideau tiré de côté, "
  "montrant un miroir, un crochet et un petit banc de bois."),
 ('taille', 'vocab', P_VOC, STYLE + " Gros plan sur une rangée de cintres portant des "
  "petites étiquettes rondes de taille, sans aucune inscription lisible."),
 ('pointure', 'vocab', P_VOC, STYLE + " Gros plan en plongée sur une boîte de chaussures "
  "ouverte, avec du papier de soie et une paire de bottes à l'intérieur. Aucune "
  "inscription sur la boîte."),
 ('manche', 'vocab', P_VOC, STYLE + " Gros plan sur la manche d'un manteau d'hiver, "
  "montrant le poignet ajusté et la fermeture à bouton-pression."),
 ('duvet', 'vocab', P_VOC, STYLE + " Gros plan sur les compartiments matelassés d'un "
  "manteau en duvet, montrant les coutures horizontales et le gonflant du tissu."),
 ('capuchon', 'vocab', P_VOC, STYLE + " Un capuchon de manteau relevé, vu de dos, bordé "
  "d'une fourrure épaisse. Fond neutre."),
 ('entretien', 'vocab', P_VOC, STYLE + " Gros plan sur une étiquette de tissu portant "
  "quatre pictogrammes d'entretien alignés : un bac, un triangle, un carré, un fer. "
  "Symboles visibles, texte illisible."),
 ('secheuse', 'vocab', P_VOC, STYLE + " Une sécheuse blanche vue de face, porte "
  "entrouverte, dans une petite salle de lavage. Panier de linge posé devant."),
 ('echange', 'vocab', P_VOC, STYLE + " Un vêtement plié posé sur un comptoir de service à "
  "côté d'un ruban de caisse et d'un sac de magasin. Aucune inscription lisible."),
 ('remboursement', 'vocab', P_VOC, STYLE + " Un terminal de paiement posé sur un comptoir "
  "à côté d'une carte de plastique retournée, face vierge visible. Écran illisible."),
 ('mise-de-cote', 'vocab', P_VOC, STYLE + " Deux vêtements suspendus à part sur une tringle "
  "isolée, avec une petite étiquette de carton attachée à chacun. Aucune écriture "
  "lisible."),
 ('depot', 'vocab', P_VOC, STYLE + " Quelques billets et un reçu posés sur un comptoir de "
  "magasin, à côté d'un stylo. Les billets sont vus de biais, sans détail lisible."),
]


def genere(prompt):
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": "3:2",
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + FAL, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.loads(r.read())
    with urllib.request.urlopen(d["images"][0]["url"], timeout=240) as r:
        return r.read()


def reduire(data, cote=800, qualite=82):
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien.

    En 3:2, comme le gabarit qui les affiche — `.imgzone`, `.imgtile` et
    `.vc-photo` sont tous en `aspect-ratio:3/2`. Redimensionner en carré
    faisait recadrer d'un tiers à l'affichage, et c'était le sujet qui
    partait."""
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert('RGB')
    im = im.resize((cote, round(cote * 2 / 3)), Image.LANCZOS)
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
        "params": {"num_images": 1, "aspect_ratio": "3:2",
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

print('\n%d générées, %d déjà présentes, %d en échec'
      % (len(faits), len(sautes), len(echecs)))
for e in echecs:
    print('  ✗ ' + e)
print('coût estimé : %.2f $' % (len(faits) * 0.034))
