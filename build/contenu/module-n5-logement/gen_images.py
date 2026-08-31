#!/usr/bin/env python3
"""Génère les 30 images de module-n5-logement via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les quatorze illustrations d'exercice, telles que rendues ;
  · `vocab/`  — les seize photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

Le sujet impose une contrainte inhabituelle : ce module parle de documents —
un bail, un avis, une annonce. Or les prompts interdisent tout texte lisible.
Les documents sont donc photographiés de biais ou en faible profondeur de
champ, les lignes réduites à des traits gris. C'est voulu : un élève ne doit
pas lire un faux bail approximatif sur une photo.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-logement/gen_images.py
  python3 build/contenu/module-n5-logement/gen_images.py buanderie-sous-sol
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n5-logement'
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
         "ni délabré, palette sobre. Aucun texte lisible, aucune écriture, "
         "aucun logo, aucun filigrane, aucune personne identifiable.")

DOC = ("Photographie réaliste, format paysage, vue rapprochée d'un document de "
       "papier posé à plat, éclairage doux et rasant, faible profondeur de "
       "champ. Les lignes de texte apparaissent comme des traits gris "
       "entièrement illisibles. Aucun mot déchiffrable, aucun logo, aucun "
       "filigrane, aucune personne.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX1 = "Je découvre · Exercice 3 — Les mots du logement"
P_EX2 = "Défi 2 · Exercice 5 — Ce qu'on regarde pendant une visite"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les huit images de `prImg` ──────────────────────────
 ('boite-aux-lettres', 'images', P_EX1, STYLE + " Une rangée de boîtes aux lettres de "
  "métal dans l'entrée commune d'un petit immeuble à logements, avec une enveloppe qui "
  "dépasse de l'une d'elles. Numéros flous et illisibles."),
 ('panneau-a-louer', 'images', P_EX1, STYLE + " Un carton « à louer » posé dans la fenêtre "
  "d'un logement au deuxième étage, en légère contre-plongée, cadrage resserré sur la "
  "façade et cette fenêtre. Le lettrage du carton reste flou et illisible. Aucun "
  "véhicule dans le champ, aucun sigle ni nom de constructeur visible."),
 ('buanderie-sous-sol', 'images', P_EX1, STYLE + " Une buanderie commune au sous-sol d'un "
  "immeuble : deux laveuses et deux sécheuses blanches côte à côte, un panier de linge "
  "posé dessus, murs de béton peint, éclairage au plafond."),
 ('plancher-bois-franc', 'images', P_EX1, STYLE + " Gros plan en plongée sur un plancher de "
  "bois franc verni dans une pièce vide, les lames en enfilade, lumière de fenêtre en "
  "diagonale."),
 ('salon-ensoleille', 'images', P_EX1, STYLE + " Un salon vide et lumineux avec deux "
  "grandes fenêtres, le soleil de fin d'après-midi qui trace des rectangles clairs sur le "
  "plancher de bois."),
 ('case-stationnement', 'images', P_EX1, STYLE + " Une case de stationnement asphaltée "
  "derrière un petit immeuble à logements, délimitée par des lignes peintes pâlies, avec "
  "un muret de béton au fond."),
 ('formulaire-bail', 'images', P_EX1, DOC + " Un formulaire officiel de plusieurs pages "
  "posé sur une table de bois avec un stylo à côté, vu de trois quarts."),
 ('remise-balcon', 'images', P_EX1, STYLE + " Une petite remise de rangement fermée par une "
  "porte de bois, au bout d'un balcon arrière en bois d'un immeuble à logements, avec un "
  "vélo appuyé à côté."),

 # ── Défi 2 · les six images de `t2img` ────────────────────────────────
 ('fenetre-double', 'images', P_EX2, STYLE + " Gros plan sur une fenêtre à guillotine "
  "entrouverte dans un mur intérieur, poignée de métal visible, lumière du jour au "
  "travers, cadre de bois peint en blanc."),
 ('hotte-cuisiniere', 'images', P_EX2, STYLE + " Une hotte de cuisine en acier inoxydable "
  "installée au-dessus d'une cuisinière dans une cuisine de logement ordinaire, vue "
  "légèrement de biais. Aucune marque ni lettrage."),
 ('plinthe-electrique', 'images', P_EX2, STYLE + " Gros plan au ras du sol sur une plinthe "
  "chauffante électrique blanche fixée le long d'un mur, avec le bas d'un rideau à "
  "proximité et un plancher de bois."),
 ('panneau-disjoncteurs', 'images', P_EX2, STYLE + " Un panneau électrique gris ouvert dans "
  "un mur, montrant deux colonnes de disjoncteurs alignés. Les étiquettes sont floues et "
  "illisibles."),
 ('tache-humidite', 'images', P_EX2, STYLE + " Gros plan en contre-plongée sur une tache "
  "d'humidité brunâtre au plafond blanc d'une pièce, près du coin d'un mur."),
 ('escalier-exterieur', 'images', P_EX2, STYLE + " Un escalier extérieur de bois menant au "
  "deuxième étage d'un immeuble à logements québécois, rampe de métal, vu d'en bas, ciel "
  "gris d'automne."),

 # ── Les seize photos du banc de vocabulaire ───────────────────────────
 ('bail', 'vocab', P_VOC, DOC + " Un contrat de plusieurs pages agrafées posé sur une "
  "table, avec un stylo posé en travers, pris de biais. Le cadrage commence au "
  "deuxième tiers de la page : aucun titre, aucun en-tête, aucun bandeau dans le "
  "champ, seulement des lignes de texte réduites à des traits gris."),
 # Refait le 31 août 2026. Le prompt disait « une lettre » : le modèle a rendu
 # une **lettre manuscrite personnelle en anglais**, « Dear… / Sincerely, ».
 # `DOC` interdisait pourtant tout texte lisible — la garde était là, le modèle
 # est passé outre. Le coupable est le mot, pas la garde : « lettre » appelle
 # une lettre. Un avis de modification du bail est un **formulaire imprimé**,
 # et un élève doit reconnaître celui-là dans sa boîte aux lettres. On nomme
 # donc l'objet, et on interdit nommément l'écriture à la main.
 ('avis-modification', 'vocab', P_VOC, DOC + " Un formulaire administratif imprimé "
  "d'une seule page, posé sur une table de cuisine à côté de son enveloppe ouverte. "
  "Mise en page officielle : un bandeau d'en-tête, des cases rectangulaires vides, "
  "des lignes pointillées à remplir, un tableau à deux colonnes dans le bas. "
  "Texte entièrement illisible, uniquement des traits gris. "
  "Aucune écriture manuscrite, aucune cursive, aucune signature à la main, "
  "aucun papier vieilli ou froissé."),
 ('loyer', 'vocab', P_VOC, STYLE + " Une enveloppe blanche non affranchie et quelques "
  "billets de banque canadiens posés sur la table d'une cuisine de logement québécois, "
  "un trousseau de clés à côté. Aucun chiffre, aucune inscription, aucun calendrier "
  "dans le champ."),
 ('quatre-et-demie', 'vocab', P_VOC, STYLE + " Vue en enfilade d'un logement vide depuis le "
  "corridor : on aperçoit une cuisine à gauche, un salon au fond et deux portes de "
  "chambre fermées."),
 ('chauffe-eclaire', 'vocab', P_VOC, STYLE + " Une plinthe chauffante électrique le long "
  "d'un mur et, au-dessus, une lampe allumée au plafond d'une pièce vide, en fin de "
  "journée."),
 ('date-occupation', 'vocab', P_VOC, PERS + " Des boîtes de carton empilées près d'une "
  "porte d'entrée ouverte, jour de déménagement d'été. Les boîtes présentent leurs "
  "faces vierges à la caméra, les faces annotées tournées vers le mur ; le trousseau "
  "de clés bien net sur la boîte du dessus."),
 ('electromenagers', 'vocab', P_VOC, STYLE + " Une cuisinière et un réfrigérateur blancs "
  "côte à côte dans une cuisine de logement vide, comptoir dégagé, sans marque ni "
  "lettrage."),
 ('buanderie', 'vocab', P_VOC, STYLE + " Deux laveuses et deux sécheuses alignées contre un "
  "mur de sous-sol, avec un panier de linge posé sur l'une d'elles."),
 ('case-stationnement', 'vocab', P_VOC, STYLE + " Une auto stationnée dans une case "
  "délimitée derrière un immeuble à logements, en hiver, avec un banc de neige au fond."),
 ('insonorise', 'vocab', P_VOC, STYLE + " Vue en contre-plongée du plafond d'un logement "
  "et du haut d'un mur mitoyen, dans une pièce vide et silencieuse, lumière rasante qui "
  "révèle la texture."),
 ('ensoleille', 'vocab', P_VOC, STYLE + " Une pièce vide où le soleil entre par une grande "
  "fenêtre et dessine un large rectangle de lumière sur le plancher de bois."),
 ('bois-franc', 'vocab', P_VOC, STYLE + " Gros plan en plongée sur des lames de plancher de "
  "bois franc verni, le grain du bois bien visible, lumière naturelle latérale."),
 ('remise', 'vocab', P_VOC, STYLE + " L'intérieur d'une petite remise de rangement ouverte : "
  "deux vélos appuyés au mur, des pneus empilés, une pelle à neige."),
 ('renouvellement', 'vocab', P_VOC, STYLE + " Un calendrier mural montrant la fin d'un mois "
  "et le début du suivant, accroché à un mur de cuisine, avec un trousseau de clés "
  "suspendu à un crochet à côté. Chiffres flous et illisibles."),
 ('sous-louer', 'vocab', P_VOC, PERS + " Une main qui remet un trousseau de clés dans la "
  "main d'une autre personne, devant la porte ouverte d'un logement. Les deux visages "
  "sont hors cadrage."),
 ('tribunal-logement', 'vocab', P_VOC, STYLE + " Un corridor administratif sobre avec des "
  "chaises alignées le long d'un mur et une porte fermée au fond, éclairage neutre. "
  "Aucune enseigne lisible."),
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
