#!/usr/bin/env python3
"""Génère les 19 images de module-n5-transport via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice `prImg` ;
  · `vocab/`  — les treize photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

Quatre contraintes propres à ce module, toutes payées ailleurs :

- **Aucune plaque d'immatriculation, aucun logo de constructeur.** Le module
  est plein d'autos et de camions. Toutes les prises de vue sont donc de loin,
  de biais, de dos, ou en faible profondeur de champ, et les prompts le
  redisent chaque fois. Une plaque lisible ferait de l'image la photo d'un
  véhicule réel.
- **Aucun texte sur les panneaux.** Les panneaux de chantier du Québec portent
  des mots ; ici ils sont vus de biais, flous, ou réduits à leur forme et à
  leur couleur orange. Un mot lisible donnerait la réponse d'un exercice.
- **Aucun accident spectaculaire, aucun blessé, aucun sang.** Le module parle
  de carambolages et de véhicules d'urgence. Les scènes montrent le
  dégagement, pas le drame : une remorqueuse au travail, des gyrophares au
  loin, des cônes. C'est aussi ce qu'un élève verra vraiment de la route.
- **Six des dix-neuf images se recoupent par le sujet** — bouchon, accotement,
  remorqueuse, nid-de-poule, détour existent en version « exercice » et en
  version « banc de mots ». Les prompts diffèrent volontairement par l'angle,
  l'heure et le cadrage, pour qu'on ne se retrouve pas avec deux fois la même
  photo dans le même module.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-transport/gen_images.py
  python3 build/contenu/module-n5-transport/gen_images.py bretelle
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n5-transport'
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

ROUTE = ("Photographie réaliste, format paysage, route ou autoroute urbaine du "
         "Québec par temps couvert, béton et asphalte, glissières de sécurité, "
         "lampadaires. Prise de vue de loin ou de biais, faible profondeur de "
         "champ. Aucune plaque d'immatriculation lisible, aucun logo de "
         "constructeur, aucune enseigne, aucun texte, aucun visage.")

RUE = ("Photographie réaliste, format paysage, rue résidentielle d'un quartier "
       "ancien de Montréal, immeubles de brique, arbres, trottoirs. Lumière "
       "naturelle, faible profondeur de champ. Aucune plaque "
       "d'immatriculation lisible, aucune enseigne lisible, aucun texte, "
       "aucun visage.")

CHANTIER = ("Photographie réaliste, format paysage, chantier routier ordinaire "
            "au Québec : cônes orange, barrières de plastique, marquage au sol "
            "effacé. Lumière grise de matin, faible profondeur de champ. Les "
            "panneaux sont vus de biais ou flous : aucun mot, aucun chiffre "
            "n'est lisible. Aucun visage, aucun logo.")

AUTO = ("Photographie réaliste, format paysage, intérieur ou abord immédiat "
        "d'une automobile ordinaire, lumière naturelle du matin, faible "
        "profondeur de champ. Aucune plaque d'immatriculation, aucun logo de "
        "constructeur, aucun écran lisible, aucun visage reconnaissable.")

P_EX1 = "Je découvre · Exercice 3 — Ce qu'on voit sur la route"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les six images de `prImg` ───────────────────────────
 ('autoroute-bouchon', 'images', P_EX1, ROUTE + " Trois files d'automobiles "
  "immobilisées pare-chocs contre pare-chocs sur une autoroute urbaine, vues de "
  "haut et de loin depuis un viaduc, un matin gris. Feux arrière rouges alignés "
  "jusqu'à l'horizon. Aucun véhicule au premier plan."),
 ('accotement-panne', 'images', P_EX1, ROUTE + " Une automobile berline grise "
  "immobilisée sur l'accotement, en dehors des voies marquées, feux de détresse "
  "allumés, vue de trois quarts arrière et de loin. Les voies de circulation sont "
  "vides à côté d'elle. Aucune plaque lisible, aucune personne."),
 ('chantier-cones', 'images', P_EX1, CHANTIER + " Une longue rangée de cônes "
  "orange qui ferme la voie de droite d'un boulevard, vue au ras du sol, avec des "
  "barrières de plastique orange et blanc derrière. Aucun ouvrier, aucun panneau "
  "lisible."),
 ('remorqueuse-travail', 'images', P_EX1, ROUTE + " Une dépanneuse jaune en train "
  "de soulever l'avant d'une automobile accidentée au bord d'une autoroute, vue de "
  "loin et de trois quarts arrière, gyrophares allumés. Aucun dégât spectaculaire, "
  "aucune personne blessée, aucune plaque lisible."),
 ('nid-de-poule-rue', 'images', P_EX1, RUE + " Cadrage serré et en plongée sur un "
  "trou profond creusé dans l'asphalte d'une rue, bords irréguliers, eau de fonte "
  "au fond, au printemps. Aucun véhicule, aucune personne."),
 ('panneau-detour', 'images', P_EX1, CHANTIER + " Un panneau de chantier orange "
  "carré monté sur deux pieds au bord d'une rue, portant une grande flèche "
  "blanche coudée et aucun mot, vu de trois quarts dans une lumière grise. "
  "L'arrière-plan est flou. Aucun texte, aucun logo."),

 # ── Je retiens des mots · les treize photos du banc ───────────────────
 ('ralentissement', 'vocab', P_VOC, ROUTE + " Une file d'automobiles avançant "
  "lentement sur une autoroute urbaine, espacées de quelques mètres, vue de "
  "l'arrière depuis le niveau de la chaussée, en fin de journée. On sent que ça "
  "avance. Aucune plaque lisible."),
 ('bouchon', 'vocab', P_VOC, ROUTE + " Des automobiles complètement arrêtées sur "
  "toutes les voies d'une autoroute, vues au niveau du sol entre deux véhicules, "
  "un matin d'hiver gris. Aucune plaque lisible, aucun visage."),
 ('accotement', 'vocab', P_VOC, ROUTE + " Cadrage sur la bande d'asphalte et de "
  "gravier située à droite de la ligne blanche continue, avec la glissière de "
  "sécurité et l'herbe derrière. Aucun véhicule, aucune personne."),
 ('carambolage', 'vocab', P_VOC, ROUTE + " Trois automobiles arrêtées l'une "
  "derrière l'autre en accordéon sur une voie d'autoroute, tôles froissées à "
  "l'avant et à l'arrière, vues de très loin et de haut. Aucune personne, aucun "
  "sang, aucune scène dramatique, aucune plaque lisible."),
 ('remorqueuse', 'vocab', P_VOC, ROUTE + " Une dépanneuse jaune vue de profil au "
  "bord d'une route, bras hydraulique replié, gyrophares éteints, stationnée. "
  "Aucune inscription lisible sur la caisse, aucune personne."),
 ('voie', 'vocab', P_VOC, ROUTE + " Vue en plongée sur trois voies de circulation "
  "séparées par des lignes blanches pointillées, chaussée mouillée et vide, sans "
  "aucun véhicule. Le marquage est net et occupe toute l'image."),
 ('vehicule-urgence', 'vocab', P_VOC, RUE + " Une ambulance blanche et une "
  "voiture de police arrêtées en travers d'une rue, gyrophares bleus et rouges "
  "allumés, vues de dos et de loin dans une lumière de fin de jour. Aucun "
  "visage, aucune inscription lisible, aucun blessé."),
 ('chaussee', 'vocab', P_VOC, ROUTE + " Cadrage rasant sur l'asphalte mouillé "
  "d'une route, reflets de lampadaires, ligne jaune centrale, sans aucun "
  "véhicule. La texture de la chaussée occupe toute l'image."),
 ('nid-de-poule', 'vocab', P_VOC, RUE + " Un trou d'une trentaine de centimètres "
  "creusé dans l'asphalte au milieu d'une voie, vu de côté à hauteur de genou, "
  "morceaux d'asphalte cassé autour, ciel gris de mars. Aucun véhicule."),
 ('detour', 'vocab', P_VOC, CHANTIER + " Une rue barrée par des barrières "
  "orange et blanc, la circulation déviée vers une rue transversale sur la "
  "droite, vue de loin en plongée légère. Deux automobiles tournent. Aucun "
  "panneau lisible, aucune plaque."),
 ('bretelle', 'vocab', P_VOC, ROUTE + " Une bretelle d'autoroute courbée qui "
  "s'élève et rejoint une autoroute plus haute, vue de loin en contre-plongée, "
  "piliers de béton, ciel couvert. Peu de véhicules, aucun au premier plan."),
 ('covoiturage', 'vocab', P_VOC, AUTO + " Vue de l'arrière de l'habitacle d'une "
  "automobile, deux personnes assises à l'avant vues de dos, ceintures bouclées, "
  "pare-brise donnant sur une route dégagée au petit matin. Aucun visage, aucun "
  "écran lisible."),
 ('stationnement-incitatif', 'vocab', P_VOC, ROUTE + " Un grand stationnement "
  "extérieur presque plein, rangées d'automobiles vues de haut et de loin, un "
  "abribus vitré et un lampadaire au bord, ciel gris de matin. Aucune plaque "
  "lisible, aucune enseigne lisible, aucune personne reconnaissable."),
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
