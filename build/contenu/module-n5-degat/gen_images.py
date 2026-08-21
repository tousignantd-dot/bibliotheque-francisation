#!/usr/bin/env python3
"""Génère les 20 images de module-n5-degat via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les huit illustrations de l'exercice `prImg` ;
  · `vocab/`  — les douze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

La contrainte propre à ce module est le dosage du sinistre : un dégât d'eau
se photographie facilement en catastrophe spectaculaire, ce qui n'aide pas un
élève à reconnaître un cerne ou une latte gondolée. Les prompts demandent donc
des dommages ordinaires, nets et lisibles, dans un logement locatif québécois
banal — pas une scène de désastre. Et comme le défi 2 porte sur un avis
affiché, ce document-là est photographié de biais, ses lignes réduites à des
traits gris : un élève ne doit pas lire un faux avis approximatif sur une
photo.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-degat/gen_images.py
  python3 build/contenu/module-n5-degat/gen_images.py cerne-plafond
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n5-degat'
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
         "profondeur de champ. Logement locatif québécois ordinaire, ni luxueux "
         "ni délabré, palette sobre. Le dommage est net et lisible, jamais "
         "spectaculaire. Aucun texte lisible, aucune écriture, aucun logo, "
         "aucun filigrane, aucune personne identifiable.")

DOC = ("Photographie réaliste, format paysage, vue rapprochée d'une feuille de "
       "papier affichée ou posée, prise de biais, éclairage doux et rasant, "
       "faible profondeur de champ. Les lignes de texte apparaissent comme des "
       "traits gris entièrement illisibles. Aucun mot déchiffrable, aucun logo, "
       "aucun filigrane, aucune personne.")

P_EX = "Je découvre · Exercice 3 — Ce qu'on voit après un dégât"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les huit images de `prImg` ──────────────────────────
 ('cerne-plafond', 'images', P_EX, STYLE + " Vue en contre-plongée du plafond blanc d'une "
  "chambre : une auréole brune d'environ un mètre, plus foncée sur son pourtour, dans le "
  "coin de la pièce. Le reste du plafond est intact."),
 ('plancher-gondole', 'images', P_EX, STYLE + " Gros plan en plongée sur un plancher de bois "
  "franc dont trois lames se sont soulevées et déformées le long d'une plinthe, lumière "
  "rasante de fenêtre qui révèle le relief."),
 ('chaudiere-sous-fuite', 'images', P_EX, STYLE + " Une chaudière de plastique blanche posée "
  "au milieu d'une chambre, à moitié pleine d'eau, avec une serviette pliée autour de sa "
  "base et un plafond taché au-dessus, hors mise au point."),
 ('chauffe-eau-sous-sol', 'images', P_EX, STYLE + " Un chauffe-eau électrique cylindrique de "
  "couleur crème, dans un placard technique de logement, tuyaux de cuivre au-dessus, "
  "petite flaque d'eau à sa base."),
 ('peinture-cloque', 'images', P_EX, STYLE + " Gros plan sur un mur de cuisine peint en "
  "beige dont la peinture cloque et se décolle en petites bulles sur une trentaine de "
  "centimètres, à mi-hauteur."),
 ('assecheur-chambre', 'images', P_EX, STYLE + " Un appareil d'assèchement industriel rond "
  "et bas, posé au sol d'une chambre vidée de ses meubles, orienté vers un mur, avec un "
  "fil électrique qui court sur le plancher."),
 ('avis-entree-immeuble', 'images', P_EX, DOC + " Une feuille de papier blanche fixée avec "
  "du ruban adhésif sur le mur d'une entrée d'immeuble, à côté d'une rangée de boîtes aux "
  "lettres de métal, vue de trois quarts."),
 ('boite-documents-trempee', 'images', P_EX, DOC + " Une boîte de carton ouverte posée par "
  "terre, ses papiers gonflés d'eau et gondolés, le carton foncé par l'humidité sur le "
  "bas des parois."),

 # ── Le banc de vocabulaire ────────────────────────────────────────────
 ('degat-eau', 'vocab', P_VOC, STYLE + " Une chambre de logement dont le plafond porte une "
  "grande auréole brune et dont le plancher est mouillé sur un mètre, meubles tassés au "
  "fond, fin de matinée."),
 ('cerne', 'vocab', P_VOC, STYLE + " Gros plan sur une auréole brune bien ronde au plafond "
  "blanc d'une pièce, son pourtour plus foncé que son centre."),
 ('plafond', 'vocab', P_VOC, STYLE + " Vue en contre-plongée du plafond blanc et lisse d'une "
  "pièce vide, avec le haut de deux murs et un plafonnier simple éteint."),
 ('chaudiere', 'vocab', P_VOC, STYLE + " Une chaudière de plastique blanche de vingt litres "
  "posée sur un plancher de bois, à moitié remplie d'eau claire."),
 ('gondoler', 'vocab', P_VOC, STYLE + " Gros plan sur des lames de plancher de bois franc "
  "qui se soulèvent en vagues le long d'un mur, lumière latérale accentuant le relief."),
 ('chauffe-eau', 'vocab', P_VOC, STYLE + " Un chauffe-eau électrique cylindrique dans un "
  "placard de service, avec ses deux tuyaux de cuivre et sa valve d'arrêt, éclairage "
  "d'ampoule nue."),
 ('fuite', 'vocab', P_VOC, STYLE + " Gros plan sur un raccord de tuyau de cuivre d'où perle "
  "une goutte d'eau, avec une trace de calcaire blanchâtre en dessous."),
 ('infiltration', 'vocab', P_VOC, STYLE + " Un mur intérieur dont le bas est assombri par "
  "l'humidité sur une trentaine de centimètres, la limite du mouillé bien visible, "
  "plinthe légèrement décollée."),
 ('dommages', 'vocab', P_VOC, STYLE + " Une chambre vidée de ses meubles après un dégât : "
  "plafond taché, plancher marqué, un matelas appuyé debout contre un mur."),
 ('avis', 'vocab', P_VOC, DOC + " Une feuille blanche affichée au mur d'une entrée "
  "d'immeuble, un coin légèrement relevé, prise de trois quarts."),
 ('assechement', 'vocab', P_VOC, STYLE + " Deux appareils d'assèchement posés au sol d'une "
  "pièce vide dont un mur a été ouvert au bas, fils électriques sur le plancher, "
  "atmosphère de chantier propre."),
 ('assecheur', 'vocab', P_VOC, STYLE + " Un seul appareil d'assèchement rond et bas, vu de "
  "trois quarts sur un plancher de bois, sa grille de sortie d'air orientée vers un mur."),
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
