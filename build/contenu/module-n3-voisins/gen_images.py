#!/usr/bin/env python3
"""Génère les 20 images de module-n3-voisins par `build/route_images.py`.

Deux destinations :
  · `images/` — les sept illustrations de l'exercice 3 de « Je découvre » ;
  · `vocab/`  — les treize photos du banc de vocabulaire, réduites à 800 px.

**Aucun appel réseau en dur ici.** `generer_image` essaie les routes dans
l'ordre du prix mesuré le 21 août 2026 — Google direct (0,0336 $, 3,9 s), puis
fal.ai, puis WaveSpeed — et rend le nom de celle qui a servi. C'est ce nom qui
est inscrit au journal de chaque image : une photo du banc produite chez un
repli n'est pas un détail, c'est une ligne de facture et parfois une
différence de style.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perdrait le tiers du haut et du bas.

**La difficulté propre à ce module est qu'il se passe entre gens.** Les
personnes ne peuvent pas être reconnaissables, et le générateur a l'ordre de
ne produire aucun texte lisible — or trois objets du module sont du papier :
le carton d'invitation, l'affiche du chat perdu, les boîtes aux lettres. Les
prompts demandent donc des papiers dont la *forme* se lit (un cadre, des
lignes, une photo au milieu) sans qu'aucun mot ne se déchiffre : l'élève
reconnaît l'objet, et c'est l'exercice qui en donne le contenu.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n3-voisins/gen_images.py
  python3 build/contenu/module-n3-voisins/gen_images.py remise-cour
"""
import io, json, pathlib, sys, time

MODULE = 'module-n3-voisins'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from route_images import generer_image                       # noqa: E402

IMMEUBLE = ("Photographie réaliste, format paysage, lumière naturelle douce, "
            "faible profondeur de champ. Un immeuble à logements ordinaire "
            "d'un quartier ouvrier de Montréal — brique rouge, escaliers de "
            "métal, ruelle en arrière. Palette sobre. Aucun texte lisible, "
            "aucune écriture, aucun numéro civique lisible, aucun logo, aucun "
            "filigrane, aucune personne identifiable.")

INTERIEUR = ("Photographie réaliste, format paysage, intérieur d'un logement "
             "québécois ordinaire, lumière naturelle douce, faible profondeur "
             "de champ. Aucun texte lisible, aucun logo, aucun filigrane, "
             "aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Les lieux qu'on partage"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les sept images de l'exercice 3 ───────────────────────────────────
 ('escalier-exterieur', 'images', P_EX, IMMEUBLE + " Un escalier extérieur de "
  "métal noir qui monte en tournant sur la façade de brique, vu d'en bas, "
  "rampe visible. Personne dans l'escalier."),
 ('palier-portes', 'images', P_EX, IMMEUBLE + " Le petit palier intérieur d'un "
  "étage : deux portes de logement côte à côte, un plancher de bois usé, une "
  "fenêtre au bout du corridor. Aucun numéro lisible sur les portes."),
 ('boites-aux-lettres', 'images', P_EX, IMMEUBLE + " Un mur de petites boîtes "
  "aux lettres métalliques dans l'entrée d'un immeuble, six cases alignées, "
  "vues de face. Les étiquettes sont des rectangles blancs vides."),
 ('remise-cour', 'images', P_EX, IMMEUBLE + " Une petite remise de bois au "
  "fond d'une cour arrière, porte entrouverte, un vélo appuyé contre le mur "
  "à côté. Herbe et clôture de bois autour."),
 ('corde-linge-cour', 'images', P_EX, IMMEUBLE + " Une corde à linge tendue "
  "entre un poteau et un balcon arrière, des draps blancs et des serviettes "
  "qui sèchent au soleil, vus de trois quarts."),
 ('ruelle-arriere', 'images', P_EX, IMMEUBLE + " Une ruelle étroite en arrière "
  "des immeubles, asphalte gris, clôtures de bois, garages de couleur, vue en "
  "enfilade vers le fond. Personne dans la ruelle."),
 ('affiche-entree', 'images', P_EX, IMMEUBLE + " Une feuille de papier blanche "
  "punaisée sur un mur, dans l'entrée d'un immeuble, à côté des boîtes aux "
  "lettres. On devine un cadre, une photo au milieu et des lignes grises, "
  "mais aucun mot ne se déchiffre."),

 # ── Les treize photos du banc de vocabulaire ──────────────────────────
 ('voisin', 'vocab', P_VOC, PERS + " Deux personnes qui se parlent brièvement "
  "sur le palier d'un immeuble, l'une sur le pas de sa porte, l'autre dans le "
  "corridor, vues de dos et de trois quarts."),
 ('immeuble', 'vocab', P_VOC, IMMEUBLE + " La façade complète d'un immeuble de "
  "six logements en brique rouge, escaliers de métal en avant, vue de la rue, "
  "ciel clair."),
 ('palier', 'vocab', P_VOC, IMMEUBLE + " Gros plan sur le petit espace plat "
  "d'un palier entre deux volées d'escalier intérieur, deux portes de "
  "logement, plancher de bois."),
 ('concierge', 'vocab', P_VOC, PERS + " Une personne en vêtements de travail, "
  "vue de dos, qui passe le balai dans l'entrée carrelée d'un immeuble, un "
  "trousseau de clés accroché à la ceinture."),
 ('remise', 'vocab', P_VOC, IMMEUBLE + " Une petite remise de bois peinte en "
  "gris au fond d'une cour, porte fermée, toit en pente, vue de face."),
 ('corde-a-linge', 'vocab', P_VOC, IMMEUBLE + " Gros plan sur une corde à "
  "linge avec des épingles de bois et deux draps blancs qui sèchent, cour "
  "arrière floue derrière."),
 ('invitation', 'vocab', P_VOC, INTERIEUR + " Une petite carte de papier "
  "blanche glissée sous une porte de logement, vue d'en haut sur un plancher "
  "de bois. On devine quelques lignes grises sur la carte, entièrement "
  "illisibles."),
 ('feter', 'vocab', P_VOC, INTERIEUR + " Une table de cuisine avec des tasses "
  "de café, une assiette de biscuits et une théière, quatre chaises autour, "
  "vue de trois quarts. Personne à table."),
 ('apporter', 'vocab', P_VOC, PERS + " Deux mains qui tiennent une assiette "
  "couverte d'un linge, devant une porte de logement entrouverte. Visage hors "
  "cadre."),
 ('compliment', 'vocab', P_VOC, PERS + " Deux personnes debout dans une "
  "cuisine, vues de dos, l'une montrant du doigt un gâteau posé sur le "
  "comptoir. Ambiance chaleureuse, aucun visage visible."),
 ('trousseau-de-cles', 'vocab', P_VOC, IMMEUBLE + " Gros plan sur un trousseau "
  "de trois clés avec un petit ourson en tissu usé accroché à l'anneau, posé "
  "sur une marche d'escalier de bois."),
 ('collier', 'vocab', P_VOC, INTERIEUR + " Gros plan sur un chat roux couché "
  "sur un fauteuil, portant un collier bleu uni sans médaille, vu de profil."),
 ('affiche', 'vocab', P_VOC, IMMEUBLE + " Gros plan sur une feuille de papier "
  "punaisée sur un babillard de bois dans l'entrée d'un immeuble. Un cadre, "
  "une photo carrée au milieu, des lignes grises au-dessus et en dessous — "
  "aucun mot déchiffrable."),
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
    if dossier == 'vocab':
        try:
            data = reduire(data)
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
