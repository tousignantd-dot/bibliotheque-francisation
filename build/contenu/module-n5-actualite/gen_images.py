#!/usr/bin/env python3
"""Génère les 22 images de module-n5-actualite par `build/route_images.py`.

Deux destinations :
  · `images/` — les six illustrations de l'exercice 3 de « Je découvre » ;
  · `vocab/`  — les seize photos du banc de vocabulaire, réduites à 800 px.

**Aucun appel réseau en dur ici.** `generer_image` essaie les routes dans
l'ordre du prix mesuré le 21 août 2026 — Google direct, puis fal.ai, puis
WaveSpeed — et rend le nom de celle qui a servi, inscrit au journal de chaque
image.

**La difficulté propre à ce module est qu'il parle de journaux.** Un fait
divers, un chapeau, un hebdomadaire : ce sont des objets faits de mots, et le
générateur a l'ordre de n'en produire aucun de lisible. Les prompts demandent
donc du papier dont la *forme* se lit — un titre plus gras, un bloc de lignes
serrées, une photo au milieu, des colonnes — sans qu'aucun mot ne se
déchiffre. L'élève reconnaît la page ; c'est l'exercice qui en donne le texte.

Deuxième difficulté : le module raconte des sinistres. Les images restent
sobres et jamais spectaculaires — le lendemain d'un feu plutôt que les
flammes, l'eau montée plutôt que le drame, personne d'identifiable nulle part.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-actualite/gen_images.py
  python3 build/contenu/module-n5-actualite/gen_images.py cabanon-ouvert
"""
import io, json, pathlib, sys, time

MODULE = 'module-n5-actualite'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from route_images import generer_image                       # noqa: E402

SANS = (" Aucun texte lisible, aucun mot déchiffrable, aucun logo, aucun "
        "filigrane, aucune personne identifiable, aucun visage reconnaissable.")

PAPIER = ("Photographie réaliste, format paysage, lumière naturelle douce, "
          "faible profondeur de champ. Du papier journal ordinaire : on "
          "distingue un titre plus gras, des colonnes de lignes grises "
          "serrées et parfois une photo carrée, mais l'écriture reste floue "
          "et illisible." + SANS)

RUE = ("Photographie réaliste, format paysage, rue ordinaire d'un quartier "
       "de Montréal, lumière naturelle, ciel couvert. Palette sobre, aucune "
       "scène spectaculaire." + SANS)

INT = ("Photographie réaliste, format paysage, intérieur ordinaire au Québec, "
       "lumière naturelle douce, faible profondeur de champ." + SANS)

PERS = ("Photographie réaliste, format paysage, une ou deux personnes vues de "
        "dos, de trois quarts ou hors cadrage du visage, lumière naturelle "
        "douce, faible profondeur de champ." + SANS)

P_EX  = "Je découvre · Exercice 3 — Ce qu'on voit dans un fait divers"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 3 ────────────────────────────────────
 ('journal-cafeteria', 'images', P_EX, PAPIER + " Un journal de quartier "
  "ouvert à plat sur une table de cafétéria en stratifié, à côté d'une tasse "
  "de café et d'un plateau. Vue de trois quarts, d'en haut."),
 ('immeuble-incendie', 'images', P_EX, RUE + " La façade de brique d'un "
  "immeuble à logements le lendemain d'un feu : trois fenêtres noircies au "
  "deuxième étage, des traces de suie au-dessus des cadres, un ruban de "
  "chantier tendu devant l'entrée. Aucune flamme, aucune fumée."),
 ('sous-sol-inonde', 'images', P_EX, INT + " Le sous-sol d'une maison où l'eau "
  "brune monte à trente centimètres, au-dessus du bas de boîtes de carton "
  "rangées contre le mur. Une chaudière, un escalier de bois, lumière crue "
  "d'une ampoule nue."),
 ('cabanon-ouvert', 'images', P_EX, RUE + " Une petite remise de bois peinte "
  "en gris au fond d'une cour arrière, la porte grande ouverte sur des "
  "tablettes à moitié vides, un cadenas brisé qui pend. Herbe et clôture de "
  "bois autour, personne dans la cour."),
 ('pompiers-boyau', 'images', P_EX, PERS + " Deux pompiers en habit de combat "
  "et casque, vus de dos, qui tiennent un gros boyau devant la façade d'un "
  "immeuble. Camion rouge flou en arrière-plan, aucune flamme visible."),
 ('porte-parole-micros', 'images', P_EX, PERS + " Une femme en manteau debout "
  "dehors, vue de trois quarts arrière, devant quatre micros noirs tendus "
  "vers elle par des mains hors cadre. Aucun cube de station sur les micros."),

 # ── Les seize photos du banc de vocabulaire ───────────────────────────
 ('fait-divers', 'vocab', P_VOC, PAPIER + " Gros plan sur une page intérieure "
  "de journal : une colonne étroite surmontée d'un court titre gras et d'une "
  "petite photo carrée."),
 ('hebdomadaire', 'vocab', P_VOC, PAPIER + " Une pile de journaux gratuits "
  "pliés dans un présentoir de métal, à l'entrée d'une épicerie de quartier."),
 ('chapeau', 'vocab', P_VOC, PAPIER + " Très gros plan sur le haut d'un "
  "article : un titre en gros caractères, puis deux ou trois lignes plus "
  "grasses que le reste du texte, puis le corps en lignes fines."),
 ('temoin', 'vocab', P_VOC, PERS + " Une personne debout sur un trottoir, vue "
  "de dos, qui parle à quelqu'un dont on ne voit que l'épaule et un carnet "
  "ouvert dans la main."),
 ('incendie', 'vocab', P_VOC, RUE + " Une maison de bois dont le toit et une "
  "fenêtre sont noircis, vue de la rue le lendemain d'un feu, planches de "
  "contreplaqué clouées sur l'ouverture."),
 ('evacuer', 'vocab', P_VOC, PERS + " Trois personnes en manteau par-dessus "
  "des vêtements de nuit, vues de dos, sur un trottoir devant un immeuble, "
  "une couverture sur les épaules, la nuit, lumière orangée d'un lampadaire."),
 ('sinistre', 'vocab', P_VOC, PERS + " Une personne assise de dos sur une "
  "chaise pliante dans un gymnase transformé en refuge, lits de camp alignés "
  "et sacs de vêtements autour."),
 ('inondation', 'vocab', P_VOC, RUE + " Une rue résidentielle dont la "
  "chaussée est recouverte d'eau brune jusqu'au bas des portes de garage, "
  "reflets des arbres à la surface. Aucune voiture en mouvement."),
 ('declaration', 'vocab', P_VOC, PERS + " Gros plan sur deux micros noirs "
  "tendus vers l'épaule d'une personne qui parle, visage entièrement hors "
  "cadre, fond extérieur flou."),
 ('enquete', 'vocab', P_VOC, RUE + " Un ruban de chantier jaune tendu entre "
  "deux poteaux devant l'entrée d'un bâtiment, cour vide derrière, fin de "
  "journée."),
 ('enqueteur', 'vocab', P_VOC, PERS + " Une personne en manteau et gants, vue "
  "de dos, accroupie devant des débris noircis dans une pièce vide, une "
  "lampe de poche à la main."),
 ('avertissement', 'vocab', P_VOC, INT + " Gros plan sur un téléphone posé "
  "sur une table de cuisine, écran allumé montrant un bandeau d'alerte "
  "orange uni, sans aucun mot lisible dessus."),
 ('vol', 'vocab', P_VOC, RUE + " Gros plan sur un cadenas ouvert et une "
  "moraillon arraché sur la porte d'une remise de bois, éclats de peinture "
  "autour de la vis."),
 ('suspect', 'vocab', P_VOC, RUE + " Une silhouette sombre et floue qui "
  "s'éloigne au fond d'une ruelle la nuit, vue de très loin et de dos, "
  "éclairée par un seul lampadaire. Aucun détail du visage ni des vêtements."),
 ('cabanon', 'vocab', P_VOC, RUE + " Une petite remise de bois à toit en "
  "pente au fond d'une cour, porte fermée, une pelle et un râteau appuyés "
  "contre le mur, vue de face."),
 ('prevention', 'vocab', P_VOC, INT + " Gros plan sur des mains qui notent au "
  "crayon dans un carnet quadrillé posé à côté d'un vélo renversé sur "
  "l'établi d'un garage. Les traits du carnet sont illisibles."),
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
    print('   ✗ %s' % e)
sys.exit(1 if echecs else 0)
