#!/usr/bin/env python3
"""Génère les 18 images de module-n5-quebec via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice `prImg` ;
  · `vocab/`  — les douze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

Quatre contraintes propres à ce module :

- **Le paysage est celui du Bas-Saint-Laurent, pas d'une côte quelconque.**
  Le module se passe au parc national du Bic et dans le village du Bic : des
  caps de roche sombre, des baies, des anses, de l'herbe rase, des sapins
  courts, et le fleuve si large qu'on ne voit pas l'autre rive. Les prompts le
  redisent chaque fois, parce qu'une plage de sable ou une falaise de craie
  ferait mentir le module sur la région qu'il enseigne.
- **Aucun logo de transporteur, aucune destination lisible.** Le module cite
  Orléans Express et VIA Rail par leur nom dans le texte ; les photos, elles,
  montrent des autocars et des trains vus de loin, de biais ou de dos, sans
  livrée reconnaissable et sans girouette lisible. Un nom de ville lisible sur
  un autocar donnerait la réponse d'un exercice d'horaire.
- **Aucun visage reconnaissable.** Les vacanciers, les voyageurs et les gens
  du gîte sont vus de dos, de loin, ou à contre-jour.
- **Six des dix-huit images se recoupent par le sujet** — le phare, le
  sentier, le fleuve et le gîte existent en version « exercice » et en version
  « banc de mots ». Les prompts diffèrent volontairement par l'angle, l'heure
  et le cadrage, pour qu'on ne se retrouve pas deux fois avec la même photo
  dans le même module.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-quebec/gen_images.py
  python3 build/contenu/module-n5-quebec/gen_images.py phare
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n5-quebec'
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

# Les quatre décors du module. Chacun porte ses interdits, parce qu'un prompt
# qui ne les redit pas les perd.
COTE = ("Photographie réaliste, format paysage, littoral du Bas-Saint-Laurent "
        "au Québec : caps de roche sombre et feuilletée, baies et anses, herbe "
        "rase, épinettes courtes penchées par le vent, et le fleuve "
        "Saint-Laurent si large qu'on n'en voit pas l'autre rive. Lumière "
        "naturelle du matin ou de fin de jour. Aucun visage reconnaissable, "
        "aucune enseigne, aucun texte lisible, aucun logo.")

GARE = ("Photographie réaliste, format paysage, gare d'autocars interurbains "
        "en ville au Québec : hall de béton et de verre, quais numérotés, "
        "sol de terrazzo, éclairage au plafond. Prise de vue de loin ou de "
        "biais, faible profondeur de champ. Aucune livrée de transporteur "
        "reconnaissable, aucune girouette de destination lisible, aucun logo, "
        "aucun texte lisible, aucun visage reconnaissable.")

ROUTE = ("Photographie réaliste, format paysage, route de campagne du "
         "Bas-Saint-Laurent : asphalte étroit, champs, granges, clôtures de "
         "perches, le fleuve au loin sur la droite. Ciel largement dégagé de "
         "fin d'été. Aucune plaque d'immatriculation lisible, aucun logo de "
         "constructeur ou de transporteur, aucune enseigne, aucun texte, "
         "aucun visage.")

VILLAGE = ("Photographie réaliste, format paysage, village de bord de fleuve "
           "au Bas-Saint-Laurent : maisons de bois à toit à deux versants et "
           "à galerie, lilas et vivaces, clôtures basses, rue tranquille. "
           "Lumière douce de fin d'après-midi. Aucune enseigne lisible, aucun "
           "texte, aucun logo, aucun visage reconnaissable.")

P_EX = "Je découvre · Exercice — Ce qu'on voit quand on sort de la ville"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les six images de `prImg` ───────────────────────────
 # Chacune doit correspondre sans ambiguïté à sa phrase, et à elle seule :
 # l'exercice est un appariement, donc deux images voisines se répondraient.
 ('gare-autocars', 'images', P_EX, GARE + " Un grand hall vitré vu de "
  "l'intérieur, avec trois autocars gris stationnés en épi le long de quais "
  "numérotés, derrière une paroi de verre. Quelques voyageurs de dos, flous, "
  "au premier plan. Aucun nom de ville, aucun logo sur les autocars."),
 ('autocar-route', 'images', P_EX, ROUTE + " Un autocar interurbain gris vu "
  "de trois quarts arrière, roulant sur une route de campagne, le fleuve "
  "large et gris à droite de l'image et des champs moissonnés à gauche. Vue "
  "de loin, depuis le bord de la route. Aucune inscription lisible sur la "
  "carrosserie."),
 ('phare-cap', 'images', P_EX, COTE + " Une tour de phare blanche à toit "
  "rouge, dressée au bout d'une pointe de roche plate, face à l'eau, vue de "
  "trois quarts et de loin, ciel clair de fin d'après-midi. Aucune personne, "
  "aucun panneau."),
 ('sentier-bord-eau', 'images', P_EX, COTE + " Un petit sentier de terre "
  "battue serpentant entre des épinettes courtes, s'ouvrant au bout sur "
  "l'eau grise du fleuve. Vue prise depuis le sentier, à hauteur d'homme. "
  "Aucune personne, aucun panneau."),
 ('gite-galerie', 'images', P_EX, VILLAGE + " Une vieille maison de bois "
  "blanche à grande galerie couverte, avec quatre chaises de bois peintes et "
  "des pots de fleurs devant, vue de trois quarts depuis la rue. Aucune "
  "enseigne, aucun texte, aucune personne."),
 ('train-quai-soir', 'images', P_EX, "Photographie réaliste, format paysage, "
  "petite gare ferroviaire de région au Québec à la tombée du jour. Un train "
  "de voyageurs argenté arrêté le long d'un quai bas, vu de trois quarts "
  "avant et de loin, fenêtres éclairées, lampadaires allumés sur le quai. "
  "Aucun logo, aucune inscription lisible, aucun visage reconnaissable."),

 # ── Je retiens des mots · les douze photos du banc ────────────────────
 ('depliant', 'vocab', P_VOC, "Photographie réaliste, format paysage, gros "
  "plan en plongée sur un dépliant touristique de papier glacé ouvert en "
  "trois volets, posé sur une table de bois clair, à côté d'une tasse. Les "
  "volets montrent des photos de paysage et un plan schématique. Le texte "
  "imprimé est trop petit et trop flou pour être lu : aucun mot lisible, "
  "aucun logo, aucune main, aucun visage."),
 ('fleuve', 'vocab', P_VOC, COTE + " Le fleuve occupant les deux tiers de "
  "l'image, gris-bleu et parcouru de longues rides, sans aucune rive visible "
  "en face, vu depuis une plage de galets au premier plan. Aucun bateau, "
  "aucune personne."),
 ('phare', 'vocab', P_VOC, COTE + " Un phare blanc à toit rouge vu en "
  "contre-plongée serrée depuis sa base, dans une lumière de fin de jour, "
  "l'herbe rase au premier plan et le ciel derrière. Cadrage différent d'une "
  "vue de loin : la tour remplit l'image. Aucune personne, aucun texte."),
 ('horaire', 'vocab', P_VOC, GARE + " Gros plan de biais sur un tableau "
  "d'affichage d'horaires accroché au mur d'une gare : une grille de lignes "
  "et de colonnes régulières, avec des heures et des noms rendus illisibles "
  "par le flou et l'angle. Aucun mot déchiffrable, aucun logo."),
 ('soute', 'vocab', P_VOC, "Photographie réaliste, format paysage, flanc "
  "d'un autocar interurbain gris avec la trappe de soute ouverte au ras du "
  "sol, laissant voir des valises rangées à l'intérieur du compartiment. Vue "
  "de trois quarts, à hauteur de hanche, lumière grise de quai. Aucune "
  "inscription lisible sur la carrosserie, aucun logo, aucun visage."),
 ('gite', 'vocab', P_VOC, VILLAGE + " Une maison d'hôtes de deux étages en "
  "bardeaux bleu pâle, vue de face depuis le trottoir d'en face, par un "
  "matin clair, avec des rideaux aux fenêtres et un banc près de la porte. "
  "Cadrage frontal, différent de la vue de trois quarts. Aucune enseigne "
  "lisible, aucune personne."),
 ('sentier', 'vocab', P_VOC, COTE + " Un sentier de terre et de racines "
  "monté en pente douce dans un sous-bois d'épinettes, vu en plongée depuis "
  "le haut, sans eau visible. Cadrage forestier, différent de la vue qui "
  "s'ouvre sur le fleuve. Aucune personne, aucun panneau."),
 ('maree', 'vocab', P_VOC, COTE + " L'estran découvert à marée basse : une "
  "vaste étendue de roche plate et de vase luisante parcourue de flaques et "
  "de rubans d'algues brunes, la ligne d'eau très loin au fond. Aucune "
  "personne, aucune embarcation."),
 ('pret-a-camper', 'vocab', P_VOC, "Photographie réaliste, format paysage, "
  "hébergement de prêt-à-camper dans un camping de parc national du Québec : "
  "une tente de toile beige montée en dur sur une plateforme de bois, avec "
  "une petite galerie, deux chaises et une table à pique-nique, entourée "
  "d'épinettes. Fin d'après-midi. Aucun logo, aucun texte lisible, aucune "
  "personne."),
 ('vacancier', 'vocab', P_VOC, COTE + " Une personne seule vue de dos, en "
  "coupe-vent et sac à dos, arrêtée sur un cap de roche et regardant le "
  "fleuve, silhouette occupant le tiers droit de l'image. De dos et de loin : "
  "aucun visage, aucun logo de vêtement lisible."),
 ('belvedere', 'vocab', P_VOC, COTE + " Une plateforme d'observation en bois "
  "avec un garde-corps, aménagée en hauteur au bout d'un cap et donnant sur "
  "la baie et le fleuve, vue de trois quarts arrière et vide de monde. "
  "Aucun panneau lisible, aucune personne."),
 ('jaser', 'vocab', P_VOC, VILLAGE + " Deux personnes assises côte à côte "
  "dans des chaises de bois sur une galerie couverte, vues de dos et en "
  "légère contre-plongée, tournées l'une vers l'autre, tasses à la main, en "
  "fin d'après-midi. Aucun visage reconnaissable, aucun texte."),
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
print('%d générée(s) · %d déjà présente(s) · %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for e in echecs:
    print('  ✗', e)
if echecs:
    sys.exit(1)
