#!/usr/bin/env python3
"""Génère les 20 images de module-n3-horaire par `build/route_images.py`.

Deux destinations :
  · `images/` — les huit illustrations de l'exercice 3 de « Je découvre » ;
  · `vocab/`  — les douze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdrait le tiers du haut et du bas.

**La difficulté propre à ce module est l'écriture.** Son univers est fait
d'heures affichées : un horaire au mur, une poinçonneuse à chiffres, un carnet
de notes. Or le générateur a l'ordre de ne produire aucun texte lisible. Les
prompts demandent donc des objets dont la **forme** est reconnaissable sans
qu'un mot ne se lise : un grand tableau blanc quadrillé de lignes et de
colonnes floues, une petite machine murale à écran sombre, un carnet ouvert
couvert de traits gris. L'élève reconnaît l'objet ; c'est l'exercice qui en
donne le contenu.

**Aucune marque, aucun logo de résidence ou de traiteur, aucun visage
reconnaissable.** Les scènes de cuisine se prennent sans personne au premier
plan, ou de dos.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée. La
route dit toujours d'où vient l'image — un repli chez un revendeur n'est
jamais silencieux, et chaque tentative entre au registre des appels.

  python3 build/contenu/module-n3-horaire/gen_images.py
  python3 build/contenu/module-n3-horaire/gen_images.py tableau-horaire
"""
import io, json, pathlib, sys, time

MODULE = 'module-n3-horaire'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from route_images import generer_image                       # noqa: E402

CUISINE = ("Photographie réaliste, format paysage, lumière naturelle douce, "
           "faible profondeur de champ. La cuisine d'une cafétéria de "
           "résidence pour aînés au Québec : inox, chariots, plateaux, "
           "palette sobre. Aucun texte lisible, aucune écriture, aucun logo, "
           "aucun filigrane, aucune personne identifiable.")

PERSONNEL = ("Photographie réaliste, format paysage, lumière naturelle douce, "
             "faible profondeur de champ. La salle du personnel d'un lieu de "
             "travail ordinaire au Québec : murs clairs, casiers, mobilier "
             "simple. Aucun texte lisible, aucune écriture, aucun logo, aucun "
             "filigrane, aucune personne identifiable.")

OBJET = ("Photographie réaliste, format paysage, gros plan sur un objet posé "
         "sur une surface de travail claire, lumière naturelle douce, faible "
         "profondeur de champ. Aucun texte lisible, aucune écriture, aucun "
         "chiffre lisible, aucun logo, aucun filigrane.")

PERS = ("Photographie réaliste, format paysage, scène de travail ordinaire au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Les lieux et les objets du travail"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit images de l'exercice 3 ───────────────────────────────────
 ('tableau-horaire', 'images', P_EX, PERSONNEL + " Un grand tableau blanc "
  "accroché au mur, quadrillé au marqueur en lignes et en colonnes régulières. "
  "L'écriture dans les cases n'est qu'une suite de traits gris flous, "
  "entièrement illisibles."),
 ('poinconneuse', 'images', P_EX, PERSONNEL + " Une petite machine grise fixée "
  "au mur à hauteur d'épaule, à écran sombre et à fente horizontale, vue de "
  "trois quarts. L'écran reste éteint et illisible."),
 ('casiers-vestiaire', 'images', P_EX, PERSONNEL + " Une rangée de casiers "
  "métalliques étroits, gris clair, à portes fermées, dans un vestiaire "
  "d'employés. Un banc de bois devant. Aucun numéro lisible."),
 ('chariot-plateaux', 'images', P_EX, CUISINE + " Un chariot de service à "
  "roulettes, en inox, chargé de plateaux de cafétéria vides empilés sur ses "
  "tablettes, vu de trois quarts dans un corridor."),
 ('chambre-froide', 'images', P_EX, CUISINE + " L'intérieur d'une chambre "
  "froide de restaurant : tablettes d'inox, caisses de plastique, porte épaisse "
  "entrouverte, lumière froide. Personne dans la pièce."),
 ('four-cuisine', 'images', P_EX, CUISINE + " Un grand four professionnel en "
  "inox, portes fermées, boutons ronds sur le panneau, vu de face dans une "
  "cuisine de cafétéria. Aucun affichage lisible."),
 ('boites-livraison', 'images', P_EX, CUISINE + " Six boîtes de carton brun "
  "fermées au ruban adhésif, empilées contre un mur dans un corridor de "
  "service. Aucune inscription lisible sur le carton."),
 ('note-papier', 'images', P_EX, OBJET + " Un petit carnet à spirale ouvert et "
  "un crayon posés sur un bureau de bois clair. Trois lignes d'écriture "
  "manuscrite y paraissent comme des traits gris, entièrement illisibles."),

 # ── Les douze photos du banc de vocabulaire ───────────────────────────
 ('quart-de-travail', 'vocab', P_VOC, PERS + " Un employé de cuisine en "
  "uniforme, vu de dos, qui entre dans une cuisine de cafétéria au petit "
  "matin. Lumière encore basse aux fenêtres."),
 ('horaire', 'vocab', P_VOC, PERSONNEL + " Gros plan légèrement de biais sur un "
  "tableau blanc quadrillé au marqueur, lignes et colonnes régulières. Les "
  "cases contiennent des traits gris flous, illisibles."),
 ('chef-equipe', 'vocab', P_VOC, PERS + " Deux personnes en uniforme de "
  "cuisine, vues de trois quarts dos, debout devant un tableau mural ; l'une "
  "montre quelque chose du doigt. Aucun visage reconnaissable."),
 ('tache', 'vocab', P_VOC, CUISINE + " Deux mains gantées qui déposent des "
  "plateaux propres sur la tablette d'un chariot d'inox. Cadrage serré, aucun "
  "visage."),
 ('uniforme', 'vocab', P_VOC, OBJET + " Un uniforme de cuisine propre — "
  "chemise claire et tablier — suspendu à un cintre devant une porte de casier "
  "métallique. Aucune broderie lisible."),
 ('vestiaire', 'vocab', P_VOC, PERSONNEL + " Un vestiaire d'employés : deux "
  "rangées de casiers métalliques face à face, un banc de bois au centre, sol "
  "de tuiles claires. Personne dans la pièce."),
 ('poinconner', 'vocab', P_VOC, PERS + " Une main qui approche une carte "
  "rectangulaire de la fente d'un petit appareil mural gris. Cadrage serré sur "
  "la main et l'appareil. Aucun affichage lisible."),
 ('pause', 'vocab', P_VOC, PERSONNEL + " Une table de salle du personnel avec "
  "une tasse de café, un contenant de repas ouvert et une chaise reculée. "
  "Personne assise."),
 ('conge', 'vocab', P_VOC, OBJET + " Un calendrier mural de papier accroché à "
  "un mur clair, dont deux cases sont marquées d'un grand trait au crayon. Les "
  "chiffres et les mots restent flous et illisibles."),
 ('livraison', 'vocab', P_VOC, CUISINE + " Une pile de boîtes de carton brun "
  "posées sur un diable, dans le corridor de service d'une cuisine "
  "institutionnelle. Aucune inscription lisible."),
 ('eteindre', 'vocab', P_VOC, OBJET + " Gros plan sur une main qui tourne un "
  "bouton rond de commande sur le panneau d'inox d'un four professionnel. "
  "Aucun chiffre lisible autour du bouton."),
 ('ranger', 'vocab', P_VOC, PERS + " Une personne vue de dos qui dépose une "
  "caisse de plastique sur une tablette d'inox, dans une chambre froide de "
  "restaurant. Lumière froide, aucun visage."),
]


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
faits, sautes, echecs, routes = [], [], [], {}

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
        data, route = generer_image(prompt, ratio=RATIO, resolution="1K",
                                    module=MODULE, cible=etiquette)
    except Exception as e:
        echecs.append('%s : %s' % (etiquette, e)); continue

    brut = data
    # La route Google directe rend des JPEG bien plus lourds que fal.ai —
    # de 650 à 1000 Ko contre 350. À l'écran, l'image d'exercice occupe
    # 223 x 132 px et la photo du banc encore moins : les deux se réduisent,
    # seulement pas au même format.
    try:
        data = reduire(data, *((800, 82) if dossier == 'vocab' else (1200, 85)))
    except Exception as e:
        echecs.append('%s : réduction impossible (%s) — image brute gardée'
                      % (etiquette, e))

    base = '%s_%s-%s_%s' % (MODULE, dossier, nom, horodatage)
    (GEN / (base + '.jpg')).write_bytes(brut)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "nano-banana-2 (Gemini 3.1 Flash Image)",
        "prompt": prompt,
        "refs": [],
        "params": {"num_images": 1, "aspect_ratio": RATIO,
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": route,
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation",
        "module": MODULE,
        "page": page,
        "destination": "assets/interactive/%s/%s/%s.jpg" % (MODULE, dossier, nom),
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(etiquette)
    routes[route] = routes.get(route, 0) + 1
    print('  ✓ %-24s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('  !! ' + e)
