#!/usr/bin/env python3
"""Génère les 22 images de module-n5-actualite par `build/route_images.py`.

Deux destinations :
  · `images/` — les six photos de l'exercice 3 « Ce qu'on voit dans un fait
    divers » ;
  · `vocab/`  — les seize photos du banc, réduites à 800 px.

**Aucun appel réseau en dur ici.** `generer_image` essaie les routes dans
l'ordre du prix mesuré le 21 août 2026 — Google direct, puis fal.ai, puis
WaveSpeed — et rend le nom de celle qui a servi, inscrit au journal de chaque
image.

**La difficulté propre à ce module est qu'il parle de journaux.** Cinq mots du
banc — le fait divers, l'hebdomadaire, le chapeau, la déclaration,
l'avertissement — désignent du papier ou de l'écrit, et le générateur a l'ordre
de ne produire aucun texte lisible. Les prompts demandent donc des imprimés
dont la *forme* se lit — colonnes, filets, un pavé plus gras sous le titre,
une photo carrée — sans qu'aucun mot ne se déchiffre : l'élève reconnaît
l'objet, et c'est la carte qui en donne le sens.

**Et il parle de malheurs.** Un incendie, une inondation, un vol : les scènes
montrent l'*après* et les choses, jamais la détresse de quelqu'un. Les
personnes — témoin, sinistré, enquêteur, suspect, porte-parole — sont vues de
dos, de trois quarts ou hors cadrage du visage. Personne n'est reconnaissable,
et aucune image ne met en scène un visage qui pleure.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-actualite/gen_images.py
  python3 build/contenu/module-n5-actualite/gen_images.py cabanon
"""
import io, json, pathlib, sys, time

MODULE = 'module-n5-actualite'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from route_images import generer_image                       # noqa: E402

SOCLE = ("Photographie réaliste, format paysage, lumière naturelle, faible "
         "profondeur de champ, palette sobre. Aucun texte lisible, aucune "
         "écriture déchiffrable, aucun logo, aucun filigrane, aucune personne "
         "identifiable.")

QUARTIER = (SOCLE + " Scène d'un quartier ordinaire de Montréal — brique "
            "rouge, escaliers de métal, ruelles, arbres de rue.")

PERS = (SOCLE + " Une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Aucun visage reconnaissable, aucune expression de "
        "détresse visible.")

PAPIER = (SOCLE + " Un imprimé dont on reconnaît la mise en page — colonnes, "
          "filets gris, un pavé plus gras, une photo carrée — mais dont aucun "
          "mot ne se déchiffre : les lignes sont de simples traits gris.")

P_EX  = "Je découvre · Exercice 3 — Ce qu'on voit dans un fait divers"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 3 ────────────────────────────────────
 ('journal-cafeteria', 'images', P_EX, PAPIER + " Un journal de quartier "
  "ouvert à plat sur une table de cafétéria, vu de trois quarts d'en haut, à "
  "côté d'une tasse de café et d'un plateau. Deux pages visibles, colonnes et "
  "une photo carrée. Personne à la table."),
 ('immeuble-incendie', 'images', P_EX, QUARTIER + " La façade d'un immeuble à "
  "logements le lendemain d'un feu : trois fenêtres noircies, la brique "
  "marquée de suie au-dessus des cadres, un ruban de plastique tendu devant "
  "l'entrée. Ciel gris, aucune flamme, aucune personne."),
 ('sous-sol-inonde', 'images', P_EX, SOCLE + " Un sous-sol de maison où l'eau "
  "brune monte à mi-hauteur de boîtes de carton empilées contre le mur. "
  "Escalier de bois au fond, une ampoule allumée. Personne dans la pièce."),
 ('cabanon-ouvert', 'images', P_EX, QUARTIER + " Une petite remise de bois "
  "peinte en gris au fond d'une cour arrière, la porte grande ouverte sur "
  "l'intérieur sombre et vide, un cadenas brisé qui pend. Herbe et clôture de "
  "bois autour, personne dans la cour."),
 ('pompiers-boyau', 'images', P_EX, PERS + " Deux pompiers en habit de combat "
  "et casque, vus de dos, qui tiennent ensemble un boyau d'incendie dirigé "
  "vers la façade d'un bâtiment. Camion rouge flou en arrière-plan, aucune "
  "inscription lisible sur les habits."),
 ('porte-parole-micros', 'images', P_EX, PERS + " Une femme en veste sombre "
  "vue de trois quarts arrière, debout devant quatre micros noirs tendus vers "
  "elle sur des perches. Les micros sont nus, sans cube ni écusson. "
  "Arrière-plan flou d'extérieur."),

 # ── Les seize photos du banc de vocabulaire ───────────────────────────
 ('fait-divers', 'vocab', P_VOC, PAPIER + " Gros plan sur une page intérieure "
  "de journal, une colonne courte encadrée d'un filet, une petite photo carrée "
  "en haut. Le papier est posé sur une table de bois."),
 ('hebdomadaire', 'vocab', P_VOC, PAPIER + " Une pile de journaux de format "
  "tabloïd pliés en deux dans un présentoir de métal, à l'entrée d'une "
  "épicerie de quartier. On voit la tranche et la une du dessus, illisible."),
 ('chapeau', 'vocab', P_VOC, PAPIER + " Très gros plan sur le haut d'un "
  "article : une grosse ligne noire épaisse, puis deux ou trois lignes plus "
  "grasses que le reste, puis les colonnes de texte fin. Tout est en traits "
  "gris, aucun mot lisible. Faible profondeur de champ."),
 ('temoin', 'vocab', P_VOC, PERS + " Une personne debout sur un trottoir, vue "
  "de dos, qui pointe du doigt vers le fond d'une ruelle en parlant à "
  "quelqu'un hors champ. Fin d'après-midi."),
 ('incendie', 'vocab', P_VOC, QUARTIER + " Une fenêtre d'immeuble noircie par "
  "le feu, le cadre de bois carbonisé et la brique marquée de suie au-dessus. "
  "Gros plan de trois quarts, aucune flamme."),
 ('evacuer', 'vocab', P_VOC, PERS + " Trois personnes en manteau par-dessus "
  "des vêtements de nuit, vues de dos, qui s'éloignent de l'entrée d'un "
  "immeuble sur le trottoir, la nuit. Gyrophares flous en arrière-plan."),
 ('sinistre', 'vocab', P_VOC, PERS + " Une personne assise de dos sur une "
  "chaise pliante dans un gymnase transformé en refuge, une couverture grise "
  "sur les épaules, un sac de sport à ses pieds. Lits de camp alignés au fond."),
 ('inondation', 'vocab', P_VOC, QUARTIER + " Une rue résidentielle dont la "
  "chaussée est recouverte d'eau brune jusqu'au bas des portes de garage, un "
  "panneau de rue dont la base trempe. Personne dans la rue."),
 ('declaration', 'vocab', P_VOC, PERS + " Gros plan sur un micro noir tendu "
  "vers l'épaule d'une personne en veste, vue de trois quarts arrière, tête "
  "hors cadre. Arrière-plan flou d'extérieur."),
 ('enquete', 'vocab', P_VOC, SOCLE + " Un ruban de plastique tendu en travers "
  "d'une entrée de cour, noué à une clôture de bois, vu de près. Le ruban est "
  "uni, sans aucune inscription. Cour floue derrière."),
 ('enqueteur', 'vocab', P_VOC, PERS + " Une personne en manteau, vue de dos, "
  "accroupie devant une porte forcée, un calepin ouvert dans une main et un "
  "crayon dans l'autre. Les pages du calepin sont vides."),
 ('avertissement', 'vocab', P_VOC, SOCLE + " Un téléphone cellulaire tenu à "
  "deux mains, écran allumé sur un bandeau de couleur ambre occupant le haut "
  "de l'écran, avec des lignes grises en dessous — aucun mot déchiffrable. "
  "Fenêtre pluvieuse floue derrière."),
 ('vol', 'vocab', P_VOC, SOCLE + " Gros plan sur une porte de remise de bois "
  "entrouverte, le moraillon arraché et le cadenas brisé qui pend au bout de "
  "son anneau. Éclats de bois clair autour des vis."),
 ('suspect', 'vocab', P_VOC, PERS + " Une silhouette en capuchon vue de dos et "
  "de loin, qui s'éloigne au fond d'une ruelle mal éclairée, la nuit. Image "
  "volontairement peu contrastée, aucun détail du visage ni des vêtements."),
 ('cabanon', 'vocab', P_VOC, QUARTIER + " Une petite remise de bois au fond "
  "d'une cour arrière, porte fermée, toit en pente, une pelle et un râteau "
  "appuyés contre le mur à côté. Vue de face, plein jour."),
 ('prevention', 'vocab', P_VOC, SOCLE + " Deux mains qui posent un cadenas "
  "neuf à anse épaisse sur le moraillon d'une porte de remise de bois. Gros "
  "plan, visage hors cadre, plein jour."),
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
    # La route Google directe rend des JPEG bien plus lourds que fal.ai. À
    # l'écran, l'image d'exercice occupe 223 x 132 px et la photo du banc
    # encore moins : les deux se réduisent, seulement pas au même format.
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
    print('   ✗ ' + e)
