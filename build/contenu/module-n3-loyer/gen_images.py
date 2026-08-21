#!/usr/bin/env python3
"""Génère les 26 images de module-n3-loyer via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les treize illustrations des deux exercices `imgmatch`
    (« Les pièces du logement » et « Ce qu'on regarde pendant la visite ») ;
  · `vocab/`  — les treize photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdrait le tiers du haut et du bas.

**La difficulté propre à ce module est qu'il parle de logements vides.** Un
générateur d'images produit spontanément des intérieurs de magazine, meublés,
décorés, habités — ce qui contredit l'annonce (« non meublé ») et rend
l'exercice faux. Les prompts demandent donc partout des **pièces vides**, aux
murs nus, sans meubles ni objets personnels : c'est exactement ce que voit
quelqu'un qui visite un logement à louer.

Deuxième contrainte, la même que dans tout le dépôt : **aucun texte lisible**.
Une petite annonce, un bail, un avis de la Ville sont couverts d'écriture ; les
prompts demandent des papiers dont la *forme* se reconnaît — une colonne de
petits blocs gris dans un journal, un formulaire quadrillé — sans qu'un seul
mot ne se lise. L'élève reconnaît l'objet ; c'est l'exercice qui en donne le
contenu.

**Aucune adresse, aucune enseigne, aucun visage reconnaissable.** Les immeubles
sont des triplex montréalais ordinaires, sans numéro civique lisible.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée. Le
compte fal.ai se libère parfois par à-coups — une boucle de relances suffit,
il n'y a rien à réécrire :

    for i in $(seq 1 12); do \\
      python3 build/contenu/module-n3-loyer/gen_images.py && break; sleep 120; done

  python3 build/contenu/module-n3-loyer/gen_images.py
  python3 build/contenu/module-n3-loyer/gen_images.py buanderie
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n3-loyer'
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

VIDE = ("Photographie réaliste, format paysage, intérieur d'un appartement "
        "locatif **entièrement vide** dans un immeuble montréalais ordinaire : "
        "murs peints en blanc cassé, plancher de bois franc usé, plinthes de "
        "bois, lumière naturelle par la fenêtre. Aucun meuble, aucun objet, "
        "aucune décoration, aucune personne. Aucun texte lisible, aucune "
        "enseigne, aucun logo, aucun filigrane.")

OBJET = ("Photographie réaliste, format paysage, gros plan sur un objet posé "
         "sur une table de bois clair, lumière naturelle douce, faible "
         "profondeur de champ. Aucun texte lisible, aucun logo, aucune "
         "marque, aucun filigrane, aucune personne identifiable.")

DEHORS = ("Photographie réaliste, format paysage, rue résidentielle d'un "
          "quartier montréalais ordinaire par une journée claire : triplex de "
          "brique à deux étages, escaliers extérieurs en métal, arbres de "
          "rue. Aucun numéro civique lisible, aucune enseigne, aucune plaque "
          "d'immatriculation lisible, aucun visage reconnaissable, aucun "
          "texte, aucun logo.")

P_EX1 = "Je découvre · Exercice 3 — Les pièces du logement"
P_EX2 = "Défi 3 · Exercice 4 — Ce qu'on regarde pendant la visite"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les sept images de « Les pièces du logement » ────────────────────
 ('cuisine', 'images', P_EX1, VIDE + " Une cuisine vide : comptoir de "
  "stratifié clair, évier d'acier inoxydable, armoires de bois fermées, une "
  "fenêtre au-dessus de l'évier. Aucun appareil électroménager, aucune "
  "vaisselle."),
 ('salon', 'images', P_EX1, VIDE + " Un salon vide, grande pièce ouverte sans "
  "porte, deux fenêtres donnant sur la rue, un radiateur de fonte sous la "
  "fenêtre. Rien au mur."),
 ('chambre', 'images', P_EX1, VIDE + " Une chambre à coucher vide, plus "
  "petite, avec une porte ouverte sur le côté, une fenêtre au fond et une "
  "penderie sans portes. Aucun lit, aucun meuble."),
 ('salle-de-bain', 'images', P_EX1, "Photographie réaliste, format paysage, "
  "salle de bain vide d'un appartement locatif : baignoire blanche, lavabo "
  "sur colonne, toilette, carrelage clair au mur, petit miroir sans cadre. "
  "Aucun objet de toilette, aucune serviette, aucune personne, aucun texte."),
 ('balcon-arriere', 'images', P_EX1, "Photographie réaliste, format paysage, "
  "petit balcon arrière en bois d'un immeuble montréalais, vu depuis la porte "
  "de la cuisine : garde-corps de métal peint, escalier qui descend vers une "
  "cour, cordes à linge au loin. Balcon vide. Aucun texte, aucun logo, "
  "aucune personne."),
 ('couloir', 'images', P_EX1, VIDE + " Un couloir étroit et vide, vu depuis "
  "une extrémité : deux portes fermées à gauche, une porte ouverte au fond, "
  "un plafonnier simple. Rien au mur."),
 ('escalier-exterieur', 'images', P_EX1, DEHORS + " Un escalier extérieur en "
  "métal peint qui monte en tournant vers la porte du deuxième étage d'un "
  "triplex de brique. Vu du trottoir, de trois quarts."),

 # ── Les six images de « Ce qu'on regarde pendant la visite » ─────────
 ('buanderie', 'images', P_EX2, "Photographie réaliste, format paysage, "
  "petite buanderie commune au sous-sol d'un immeuble locatif : deux laveuses "
  "et deux sécheuses blanches alignées contre un mur de béton peint, un "
  "plafonnier, un plancher de ciment. Aucun texte lisible sur les appareils, "
  "aucun logo, aucune personne."),
 ('fenetres-neuves', 'images', P_EX2, VIDE + " Gros plan sur une fenêtre "
  "récente à cadre blanc dans un mur de plâtre, ouverte à moitié, avec une "
  "poignée de métal et un appui de bois peint. Lumière du jour. Rien d'autre "
  "dans le cadrage."),
 ('cour-arriere', 'images', P_EX2, "Photographie réaliste, format paysage, "
  "petite cour arrière de triplex montréalais : clôture de bois, un carré de "
  "gazon, une allée de dalles de béton, escaliers extérieurs de métal au "
  "fond. Aucune personne, aucun texte, aucun logo."),
 ('rue-stationnement', 'images', P_EX2, DEHORS + " Vue du trottoir vers une "
  "rangée d'autos stationnées le long du trottoir, devant des triplex de "
  "brique. Un panneau de stationnement de rue est visible mais son texte est "
  "flou et parfaitement illisible."),
 ('sous-sol-escalier', 'images', P_EX2, "Photographie réaliste, format "
  "paysage, escalier de bois qui descend vers un sous-sol d'immeuble, vu du "
  "haut des marches : rampe de métal, mur de béton peint, une ampoule qui "
  "éclaire le bas. Aucun texte, aucune personne."),
 ('immeuble-facade', 'images', P_EX2, DEHORS + " Façade complète d'un triplex "
  "de brique rouge à trois logements, vue de face depuis le trottoir d'en "
  "face : trois portes, escalier extérieur, fenêtres alignées. Aucun numéro "
  "civique lisible, aucune affiche."),

 # ── Les treize photos du banc de vocabulaire ─────────────────────────
 ('logement', 'vocab', P_VOC, DEHORS + " Un triplex de brique à deux étages "
  "vu de trois quarts, avec son escalier extérieur et son balcon avant. "
  "Journée claire, ciel dégagé."),
 ('quatre-et-demie', 'vocab', P_VOC, VIDE + " Vue d'ensemble d'un logement "
  "vide depuis l'entrée : on voit le salon au premier plan, l'ouverture de la "
  "cuisine à droite et un couloir qui part vers le fond. Pièces enfilées, "
  "plancher de bois, murs blancs."),
 ('chambre-a-coucher', 'vocab', P_VOC, VIDE + " Une chambre à coucher vide, "
  "carrée, avec une grande fenêtre à droite et une porte ouverte à gauche. "
  "Plancher de bois franc, plinthes blanches."),
 ('balcon', 'vocab', P_VOC, "Photographie réaliste, format paysage, balcon "
  "avant en bois d'un triplex montréalais, vu de la rue : garde-corps de "
  "métal ouvragé, deux marches, porte d'entrée au fond. Balcon vide. Aucun "
  "numéro civique lisible, aucun texte."),
 ('petite-annonce', 'vocab', P_VOC, OBJET + " Une page de journal ouverte à "
  "plat, montrant plusieurs colonnes de petites annonces encadrées. Le texte "
  "des annonces est réduit à des traits gris parfaitement illisibles. Aucun "
  "mot, aucun chiffre lisible."),
 ('meuble', 'vocab', P_VOC, "Photographie réaliste, format paysage, petite "
  "pièce meublée simplement d'un logement locatif : un lit simple fait, une "
  "table de bois et deux chaises, une commode. Murs blancs, plancher de bois, "
  "lumière du jour. Aucun objet personnel, aucune photo au mur, aucune "
  "personne, aucun texte."),
 ('chauffe', 'vocab', P_VOC, OBJET.replace('sur une table de bois clair',
  'contre un mur de plâtre blanc') + " Un radiateur de fonte peint en blanc, "
  "sous une fenêtre, dans une pièce vide. Lumière d'hiver, plancher de bois."),
 ('electricite-comprise', 'vocab', P_VOC, OBJET + " Un compteur électrique "
  "rond au cadran de verre, fixé sur un mur extérieur de brique. Les chiffres "
  "du cadran sont flous et illisibles. Aucun texte, aucun logo, aucune "
  "marque."),
 ('proprietaire', 'vocab', P_VOC, "Photographie réaliste, format paysage, "
  "une personne vue de dos, dans l'embrasure de la porte ouverte d'un "
  "logement vide, un trousseau de clés à la main, tournée vers l'intérieur de "
  "la pièce. Visage complètement hors champ. Lumière naturelle. Aucun texte, "
  "aucun logo, aucun visage reconnaissable."),
 ('bail', 'vocab', P_VOC, OBJET + " Deux feuilles de papier officiel posées "
  "côte à côte, quadrillées de cases et de lignes grises comme un formulaire, "
  "avec un stylo posé dessus. Les cases sont remplies de traits gris "
  "totalement illisibles. Aucun mot, aucun chiffre lisible, aucun logo."),
 ('sous-sol', 'vocab', P_VOC, "Photographie réaliste, format paysage, "
  "sous-sol vide d'un immeuble locatif : murs de béton peint, plafond bas "
  "avec des tuyaux apparents, plancher de ciment, une ampoule allumée. Aucun "
  "objet, aucune personne, aucun texte."),
 ('chauffage', 'vocab', P_VOC, "Photographie réaliste, format paysage, gros "
  "plan sur un thermostat rond et blanc fixé sur un mur de plâtre, avec un "
  "radiateur flou à l'arrière-plan. Le cadran du thermostat est uni et sans "
  "chiffres lisibles. Aucun texte, aucune marque."),
 ('stationnement', 'vocab', P_VOC, DEHORS + " Une entrée de stationnement "
  "asphaltée entre deux immeubles de brique, avec une seule place marquée au "
  "sol par des lignes blanches, vide. Vue depuis la rue. Aucun panneau "
  "lisible, aucune auto."),
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
if echecs:
    sys.exit(1)
