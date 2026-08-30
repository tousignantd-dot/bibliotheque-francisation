#!/usr/bin/env python3
"""Les 22 images de module-n5-actualite, telles qu'elles ont été produites.

Ce fichier n'a pas précédé les images : il les suit. Les vingt-deux photos ont
été générées le 21 août 2026 par un agent qui a été coupé net — sommeil de
l'ordinateur — avant d'avoir versé son générateur au dépôt. Les images, elles,
étaient commitées. Les prompts ci-dessous sont les **vrais**, relus un à un
dans les journaux .json de ~/Claude/generations : réécrire de mémoire des
prompts « équivalents » aurait donné un fichier qui ment sur ce qu'on voit à
l'écran, et la prochaine régénération aurait changé le module sans prévenir.

Les vingt-deux sont passées par la **route Google directe**, sans repli.

Deux destinations :
  · `images/` — les six photos de l'exercice 3 « Ce qu'on voit dans un fait
    divers » ;
  · `vocab/`  — les seize photos du banc, réduites à 800 px.

**Aucun appel réseau en dur ici.** `generer_image` essaie les routes dans
l'ordre du prix mesuré le 21 août 2026 — Google direct, puis fal.ai, puis
WaveSpeed — et rend le nom de celle qui a servi, inscrit au journal de chaque
image.

Relançable : une image déjà présente est sautée. Pour en refaire une, efface
son fichier d'abord.

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

P_EX  = "Je découvre · Exercice 3 — Ce qu'on voit dans un fait divers"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 3 ────────────────────────────────────
 ('cabanon-ouvert', 'images', P_EX,
  "Photographie réaliste, format paysage, rue ordinaire d'un "
   "quartier de Montréal, lumière naturelle, ciel couvert. Palette "
   "sobre, aucune scène spectaculaire. Aucun texte lisible, aucun "
   "mot déchiffrable, aucun logo, aucun filigrane, aucune personne "
   "identifiable, aucun visage reconnaissable. Une petite remise de "
   "bois peinte en gris au fond d'une cour arrière, la porte grande "
   "ouverte sur des tablettes à moitié vides, un cadenas brisé qui "
   "pend. Herbe et clôture de bois autour, personne dans la cour."),
 ('immeuble-incendie', 'images', P_EX,
  "Photographie réaliste, format paysage, rue ordinaire d'un "
   "quartier de Montréal, lumière naturelle, ciel couvert. Palette "
   "sobre, aucune scène spectaculaire. Aucun texte lisible, aucun "
   "mot déchiffrable, aucun logo, aucun filigrane, aucune personne "
   "identifiable, aucun visage reconnaissable. La façade de brique "
   "d'un immeuble à logements le lendemain d'un feu : trois fenêtres "
   "noircies au deuxième étage, des traces de suie au-dessus des "
   "cadres, un ruban de chantier tendu devant l'entrée. Aucune "
   "flamme, aucune fumée."),
 ('journal-cafeteria', 'images', P_EX,
  "Photographie réaliste, format paysage, lumière naturelle douce, "
   "faible profondeur de champ. Du papier journal ordinaire : on "
   "distingue un titre plus gras, des colonnes de lignes grises "
   "serrées et parfois une photo carrée, mais l'écriture reste floue "
   "et illisible. Aucun texte lisible, aucun mot déchiffrable, aucun "
   "logo, aucun filigrane, aucune personne identifiable, aucun "
   "visage reconnaissable. Un journal de quartier ouvert à plat sur "
   "une table de cafétéria en stratifié, à côté d'une tasse de café "
   "et d'un plateau. Vue de trois quarts, d'en haut."),
 ('pompiers-boyau', 'images', P_EX,
  "Photographie réaliste, format paysage, une ou deux personnes "
   "vues de dos, de trois quarts ou hors cadrage du visage, lumière "
   "naturelle douce, faible profondeur de champ. Aucun texte "
   "lisible, aucun mot déchiffrable, aucun logo, aucun filigrane, "
   "aucune personne identifiable, aucun visage reconnaissable. Deux "
   "pompiers en habit de combat et casque, vus de dos, qui tiennent "
   "un gros boyau devant la façade d'un immeuble. Camion rouge flou "
   "en arrière-plan, aucune flamme visible."),
 ('porte-parole-micros', 'images', P_EX,
  "Photographie réaliste, format paysage, une ou deux personnes "
   "vues de dos, de trois quarts ou hors cadrage du visage, lumière "
   "naturelle douce, faible profondeur de champ. Aucun texte "
   "lisible, aucun mot déchiffrable, aucun logo, aucun filigrane, "
   "aucune personne identifiable, aucun visage reconnaissable. Une "
   "femme en manteau debout dehors, vue de trois quarts arrière, "
   "devant quatre micros noirs tendus vers elle par des mains hors "
   "cadre. Aucun cube de station sur les micros."),
 ('sous-sol-inonde', 'images', P_EX,
  "Photographie réaliste, format paysage, intérieur ordinaire au "
   "Québec, lumière naturelle douce, faible profondeur de champ. "
   "Aucun texte lisible, aucun mot déchiffrable, aucun logo, aucun "
   "filigrane, aucune personne identifiable, aucun visage "
   "reconnaissable. Le sous-sol d'une maison où l'eau brune monte à "
   "trente centimètres, au-dessus du bas de boîtes de carton rangées "
   "contre le mur. Une chaudière, un escalier de bois, lumière crue "
   "d'une ampoule nue."),
 # ── Les seize photos du banc de vocabulaire ───────────────────────────
 ('avertissement', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, intérieur ordinaire au "
   "Québec, lumière naturelle douce, faible profondeur de champ. "
   "Aucun texte lisible, aucun mot déchiffrable, aucun logo, aucun "
   "filigrane, aucune personne identifiable, aucun visage "
   "reconnaissable. Gros plan sur un téléphone posé sur une table de "
   "cuisine, écran allumé montrant un bandeau d'alerte orange uni, "
   "sans aucun mot lisible dessus."),
 ('cabanon', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, rue ordinaire d'un "
   "quartier de Montréal, lumière naturelle, ciel couvert. Palette "
   "sobre, aucune scène spectaculaire. Aucun texte lisible, aucun "
   "mot déchiffrable, aucun logo, aucun filigrane, aucune personne "
   "identifiable, aucun visage reconnaissable. Une petite remise de "
   "bois à toit en pente au fond d'une cour, porte fermée, une pelle "
   "et un râteau appuyés contre le mur, vue de face."),
 ('chapeau', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, lumière naturelle douce, "
   "faible profondeur de champ. Du papier journal ordinaire : on "
   "distingue un titre plus gras, des colonnes de lignes grises "
   "serrées et parfois une photo carrée, mais l'écriture reste floue "
   "et illisible. Aucun texte lisible, aucun mot déchiffrable, aucun "
   "logo, aucun filigrane, aucune personne identifiable, aucun "
   "visage reconnaissable. Très gros plan rasant sur la jonction "
   "entre deux ou trois lignes plus grasses et le corps du texte en "
   "lignes fines, prise de vue à 30° pour que rien ne se déchiffre. "
   "Le titre est coupé par le bord supérieur de l'image, aucun gros "
   "caractère dans le champ."),
 ('declaration', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, une ou deux personnes "
   "vues de dos, de trois quarts ou hors cadrage du visage, lumière "
   "naturelle douce, faible profondeur de champ. Aucun texte "
   "lisible, aucun mot déchiffrable, aucun logo, aucun filigrane, "
   "aucune personne identifiable, aucun visage reconnaissable. Gros "
   "plan sur deux micros noirs tendus vers l'épaule d'une personne "
   "qui parle, visage entièrement hors cadre, fond extérieur flou."),
 ('enquete', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, rue ordinaire d'un "
   "quartier de Montréal, lumière naturelle, ciel couvert. Palette "
   "sobre, aucune scène spectaculaire. Aucun texte lisible, aucun "
   "mot déchiffrable, aucun logo, aucun filigrane, aucune personne "
   "identifiable, aucun visage reconnaissable. Un ruban de chantier "
   "jaune tendu entre deux poteaux devant l'entrée d'un bâtiment, "
   "cour vide derrière, fin de journée."),
 ('enqueteur', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, une ou deux personnes "
   "vues de dos, de trois quarts ou hors cadrage du visage, lumière "
   "naturelle douce, faible profondeur de champ. Aucun texte "
   "lisible, aucun mot déchiffrable, aucun logo, aucun filigrane, "
   "aucune personne identifiable, aucun visage reconnaissable. Une "
   "personne en manteau et gants, vue de dos, accroupie devant des "
   "débris noircis dans une pièce vide, une lampe de poche à la "
   "main."),
 ('evacuer', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, une ou deux personnes "
   "vues de dos, de trois quarts ou hors cadrage du visage, lumière "
   "naturelle douce, faible profondeur de champ. Aucun texte "
   "lisible, aucun mot déchiffrable, aucun logo, aucun filigrane, "
   "aucune personne identifiable, aucun visage reconnaissable. Trois "
   "personnes en manteau par-dessus des vêtements de nuit, vues de "
   "dos, sur un trottoir devant un immeuble, une couverture sur les "
   "épaules, la nuit, lumière orangée d'un lampadaire."),
 ('fait-divers', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, lumière naturelle douce, "
   "faible profondeur de champ. Du papier journal ordinaire : on "
   "distingue un titre plus gras, des colonnes de lignes grises "
   "serrées et parfois une photo carrée, mais l'écriture reste floue "
   "et illisible. Aucun texte lisible, aucun mot déchiffrable, aucun "
   "logo, aucun filigrane, aucune personne identifiable, aucun "
   "visage reconnaissable. Gros plan sur une page intérieure de "
   "journal : une colonne étroite surmontée d'un court titre gras et "
   "d'une petite photo carrée."),
 ('hebdomadaire', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, lumière naturelle douce, "
   "faible profondeur de champ. Du papier journal ordinaire : on "
   "distingue un titre plus gras, des colonnes de lignes grises "
   "serrées et parfois une photo carrée, mais l'écriture reste floue "
   "et illisible. Aucun texte lisible, aucun mot déchiffrable, aucun "
   "logo, aucun filigrane, aucune personne identifiable, aucun "
   "visage reconnaissable. Une pile de journaux pliés dans un "
   "présentoir de métal, vue du dessus et de trois quarts : la "
   "manchette est sous le pli, donc hors du champ. Le présentoir "
   "seul, aucune devanture de commerce, aucune enseigne, aucun "
   "panneau derrière."),
 ('incendie', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, rue ordinaire d'un "
   "quartier de Montréal, lumière naturelle, ciel couvert. Palette "
   "sobre, aucune scène spectaculaire. Aucun texte lisible, aucun "
   "mot déchiffrable, aucun logo, aucun filigrane, aucune personne "
   "identifiable, aucun visage reconnaissable. Une maison de bois "
   "dont le toit et une fenêtre sont noircis, vue de la rue le "
   "lendemain d'un feu, planches de contreplaqué clouées sur "
   "l'ouverture."),
 ('inondation', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, rue ordinaire d'un "
   "quartier de Montréal, lumière naturelle, ciel couvert. Palette "
   "sobre, aucune scène spectaculaire. Aucun texte lisible, aucun "
   "mot déchiffrable, aucun logo, aucun filigrane, aucune personne "
   "identifiable, aucun visage reconnaissable. Une rue résidentielle "
   "dont la chaussée est recouverte d'eau brune jusqu'au bas des "
   "portes de garage, reflets des arbres à la surface. Aucune "
   "voiture en mouvement."),
 ('prevention', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, intérieur ordinaire au "
   "Québec, lumière naturelle douce, faible profondeur de champ. "
   "Aucun texte lisible, aucun mot déchiffrable, aucun logo, aucun "
   "filigrane, aucune personne identifiable, aucun visage "
   "reconnaissable. Gros plan sur des mains qui notent au crayon "
   "dans un carnet quadrillé posé à côté d'un vélo renversé sur "
   "l'établi d'un garage. Les traits du carnet sont illisibles."),
 ('sinistre', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, une ou deux personnes "
   "vues de dos, de trois quarts ou hors cadrage du visage, lumière "
   "naturelle douce, faible profondeur de champ. Aucun texte "
   "lisible, aucun mot déchiffrable, aucun logo, aucun filigrane, "
   "aucune personne identifiable, aucun visage reconnaissable. Une "
   "personne assise de dos sur une chaise pliante dans un gymnase "
   "transformé en refuge, lits de camp alignés et sacs de vêtements "
   "autour."),
 ('suspect', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, rue ordinaire d'un "
   "quartier de Montréal, lumière naturelle, ciel couvert. Palette "
   "sobre, aucune scène spectaculaire. Aucun texte lisible, aucun "
   "mot déchiffrable, aucun logo, aucun filigrane, aucune personne "
   "identifiable, aucun visage reconnaissable. Une silhouette sombre "
   "et floue qui s'éloigne au fond d'une ruelle la nuit, vue de très "
   "loin et de dos, éclairée par un seul lampadaire. Aucun détail du "
   "visage ni des vêtements."),
 ('temoin', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, une ou deux personnes "
   "vues de dos, de trois quarts ou hors cadrage du visage, lumière "
   "naturelle douce, faible profondeur de champ. Aucun texte "
   "lisible, aucun mot déchiffrable, aucun logo, aucun filigrane, "
   "aucune personne identifiable, aucun visage reconnaissable. Une "
   "personne debout sur un trottoir, vue de dos, qui parle à "
   "quelqu'un dont on ne voit que l'épaule et un carnet ouvert dans "
   "la main."),
 ('vol', 'vocab', P_VOC,
  "Photographie réaliste, format paysage, rue ordinaire d'un "
   "quartier de Montréal, lumière naturelle, ciel couvert. Palette "
   "sobre, aucune scène spectaculaire. Aucun texte lisible, aucun "
   "mot déchiffrable, aucun logo, aucun filigrane, aucune personne "
   "identifiable, aucun visage reconnaissable. Gros plan sur un "
   "cadenas ouvert et une moraillon arraché sur la porte d'une "
   "remise de bois, éclats de peinture autour de la vis."),
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
    print('  \u2713 %-24s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('   \u2717 ' + e)
