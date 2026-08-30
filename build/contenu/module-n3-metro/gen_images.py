#!/usr/bin/env python3
"""Génère les 24 images de module-n3-metro via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les treize illustrations des deux exercices `imgmatch`
    (« Ce qu'on voit dans la station » et « Les gestes de l'achat ») ;
  · `vocab/`  — les onze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdrait le tiers du haut et du bas.

**La difficulté propre à ce module est que tout son univers est couvert
d'écriture** — une grille de tarifs, une carte de transport, un écran de
borne, un reçu — alors que le générateur a l'ordre de ne produire aucun texte
lisible. Les prompts demandent donc des objets dont la *forme* est
reconnaissable sans qu'un seul mot ne se lise : une carte de plastique bleue
et blanche tenue à la main, un panneau quadrillé de lignes et de colonnes
grises, un petit ticket de papier aux traits illisibles. L'élève reconnaît
l'objet ; c'est l'exercice qui en donne le contenu.

**Aucune marque de société de transport n'est demandée** : pas de logo, pas de
sigle, pas de couleur de ligne identifiable. Les véhicules et les stations
sont génériques.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n3-metro/gen_images.py
  python3 build/contenu/module-n3-metro/gen_images.py tourniquets
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n3-metro'
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

STATION = ("Photographie réaliste, format paysage, lumière artificielle douce, "
           "faible profondeur de champ. Intérieur d'une station de transport "
           "collectif urbaine ordinaire en Amérique du Nord : carrelage clair, "
           "murs de céramique, éclairage au plafond, palette sobre de gris et "
           "de beige. Aucun texte lisible, aucune écriture, aucun sigle, aucun "
           "logo, aucun filigrane, aucune personne identifiable.")

OBJET = ("Photographie réaliste, format paysage, gros plan sur un objet posé "
         "sur un comptoir clair, lumière naturelle douce, faible profondeur "
         "de champ. Aucun texte lisible, aucun logo, aucune marque, aucun "
         "filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX1 = "Je découvre · Exercice 3 — Ce qu'on voit dans la station"
P_EX2 = "Défi 2 · Exercice 5 — Les gestes de l'achat"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les sept images de « Ce qu'on voit dans la station » ─────────────
 ('comptoir-station', 'images', P_EX1, STATION + " Un comptoir de service "
  "vitré encastré dans le mur d'une station, avec une petite ouverture "
  "arrondie au bas de la vitre et une tablette de métal devant. Le comptoir "
  "est vide et net, aucun panneau écrit."),
 ('tourniquets', 'images', P_EX1, STATION + " Une rangée de quatre portillons "
  "d'accès en métal brossé, alignés dans le hall d'une station, chacun avec "
  "un petit lecteur rond de couleur claire sur le dessus. Aucun panneau, "
  "aucune inscription."),
 ('carte-main', 'images', P_EX1, PERS + " Gros plan sur une main qui tient une "
  "carte de plastique rigide, bleu pâle et blanc, au-dessus d'un comptoir. "
  "La carte est parfaitement unie, sans aucune inscription ni photo."),
 ('grille-affichee', 'images', P_EX1, STATION + " Un grand panneau blanc fixé "
  "au mur d'une station, quadrillé de lignes et de colonnes grises régulières "
  "comme un tableau. Les cases sont remplies de traits gris flous, totalement "
  "illisibles. Aucun mot, aucun chiffre lisible."),
 ('borne-vente', 'images', P_EX1, STATION + " Une borne libre-service en métal "
  "gris posée contre un mur de station, avec un écran sombre éteint, un "
  "clavier de touches rondes et une fente à billets. Aucun texte, aucun "
  "symbole lisible sur l'appareil."),
 ('autobus-arret', 'images', P_EX1, PERS + " Un autobus urbain blanc et gris, "
  "générique et sans marque, arrêté au bord d'un trottoir, ses portes avant "
  "ouvertes. Vue de trois quarts avant. Le panneau de destination est éteint "
  "et vide. Aucun logo, aucun numéro lisible."),
 ('places-avant', 'images', P_EX1, "Photographie réaliste, format paysage, "
  "intérieur d'un autobus urbain vide, vue vers l'avant depuis le milieu de "
  "l'allée. Les deux premières rangées de sièges sont d'une couleur "
  "différente des autres, plus pâle. Lumière du jour par les fenêtres. Aucun "
  "texte lisible, aucun logo, aucune personne."),

 # ── Les six images de « Les gestes de l'achat » ──────────────────────
 ('recharge-comptoir', 'images', P_EX2, PERS + " Deux mains au-dessus d'un "
  "comptoir de service : l'une pose une carte de plastique bleu pâle sur un "
  "petit lecteur gris, l'autre attend. Vue en plongée, visages hors cadre. "
  "Aucune inscription sur la carte ni sur l'appareil."),
 ('validation-autobus', 'images', P_EX2, PERS + " Vue rapprochée, à l'entrée "
  "d'un autobus : une main approche une carte de plastique bleu pâle d'un "
  "petit boîtier lecteur fixé sur un poteau, près du chauffeur hors champ. "
  "Aucun texte, aucun logo."),
 ('paiement-carte', 'images', P_EX2, OBJET + " Un terminal de paiement noir "
  "tenu au-dessus d'un comptoir, une main y approchant une carte bancaire "
  "unie et sans inscription. L'écran du terminal est sombre et vide."),
 ('argent-comptant', 'images', P_EX2, OBJET + " Quelques billets de banque "
  "pliés et une petite pile de pièces de monnaie argentées posés sur un "
  "comptoir clair. Les billets sont d'une couleur unie, sans motif ni "
  "chiffre lisible."),
 ('photo-carte', 'images', P_EX2, PERS + " Une personne assise de dos devant "
  "un petit fond blanc mural, dans un local de service, pendant qu'on prend "
  "sa photo. Vue depuis l'arrière, visage complètement hors champ. Aucun "
  "texte, aucun appareil de marque reconnaissable."),
 ('recu-titre', 'images', P_EX2, OBJET + " Gros plan sur un petit ticket de "
  "papier blanc étroit, légèrement froissé, posé à côté d'une carte de "
  "plastique bleu pâle sur un comptoir. Les lignes du ticket sont des traits "
  "gris parfaitement illisibles."),

 # ── Les onze photos du banc de vocabulaire ───────────────────────────
 ('carte-opus', 'vocab', P_VOC, OBJET + " Une carte de plastique rigide, bleu "
  "pâle et blanche, posée seule au centre d'un comptoir clair, vue de dessus. "
  "La carte est entièrement unie : aucune inscription, aucun sigle, aucune "
  "photo, aucune puce visible."),
 ('point-de-service', 'vocab', P_VOC, STATION + " Un guichet de service vitré "
  "dans le mur d'une station, éclairé de l'intérieur, avec une tablette de "
  "métal et une petite ouverture au bas de la vitre. Aucun panneau écrit, "
  "aucune personne."),
 ('titre-mensuel', 'vocab', P_VOC, OBJET + " Une carte de plastique bleu pâle "
  "posée sur un calendrier mural ouvert dont les cases sont vides et sans "
  "chiffres. Vue en plongée, lumière douce. Aucun texte lisible."),
 ('recharger-carte', 'vocab', P_VOC, PERS + " Une main dépose une carte de "
  "plastique bleu pâle sur un petit lecteur gris posé sur un comptoir de "
  "service. Visage hors champ. Aucun texte, aucun logo."),
 ('valider-titre', 'vocab', P_VOC, PERS + " Gros plan sur une main qui "
  "approche une carte de plastique bleu pâle d'un boîtier lecteur gris fixé "
  "sur un poteau, à l'intérieur d'un autobus. Aucune inscription."),
 ('tourniquet', 'vocab', P_VOC, STATION + " Un seul portillon d'accès en "
  "métal brossé, vu de face et de près, avec un lecteur rond de couleur "
  "claire sur le dessus et deux battants vitrés fermés. Aucun panneau."),
 ('zone-tarifaire', 'vocab', P_VOC, "Photographie réaliste, format paysage, "
  "vue aérienne en fin de journée d'une grande ville nord-américaine traversée "
  "par une rivière, avec des ponts et des quartiers de densités différentes. "
  "Lumière chaude, ciel dégagé. Aucun texte, aucun repère identifiable, aucun "
  "monument reconnaissable."),
 ('place-reservee', 'vocab', P_VOC, "Photographie réaliste, format paysage, "
  "gros plan sur deux sièges vides d'un autobus urbain, d'une couleur plus "
  "pâle que les sièges voisins, avec une barre d'appui métallique devant. "
  "Lumière du jour par la fenêtre. Aucun texte lisible, aucun pictogramme "
  "lisible, aucune personne."),
 ('transport-adapte', 'vocab', P_VOC, PERS + " Un petit véhicule de transport "
  "blanc, générique et sans marque, stationné au bord d'un trottoir, sa porte "
  "latérale ouverte et une rampe d'accès abaissée jusqu'au sol. Vue de trois "
  "quarts. Aucun logo, aucune inscription."),
 ('correspondance', 'vocab', P_VOC, PERS + " Une personne vue de dos, sac au "
  "dos, descendant d'un autobus et marchant vers l'entrée d'une station, en "
  "fin d'après-midi. L'entrée de la station est vue de trois quarts, son "
  "bandeau lumineux sort du cadre par le haut ; seule la lueur portée sur le "
  "trottoir dit l'entrée. Visage hors champ. Aucun texte, aucun logo."),
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
