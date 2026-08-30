#!/usr/bin/env python3
"""Génère les 29 images de module-n3-loisirs par `build/route_images.py`.

Trois destinations, deux dossiers :
  · `images/` — les huit illustrations de l'exercice 3 de « Je découvre »
    (le centre communautaire) et les huit de l'exercice 5 du Défi 3
    (les outils de la cuisine collective) ;
  · `vocab/`  — les treize photos du banc de vocabulaire, réduites à 800 px.
    Trois cartes sur seize n'en ont pas : « une session », « le tarif » et
    « gratuit » sont des idées, pas des objets — les photographier donnerait
    une image de calendrier ou de billet, c'est-à-dire un autre mot.

**Aucun appel réseau en dur ici.** `generer_image` essaie les routes dans
l'ordre du prix mesuré le 21 août 2026 — Google direct, puis fal.ai, puis
WaveSpeed — et rend le nom de celle qui a servi. C'est ce nom qui est inscrit
au journal de chaque image, et `route_images` tient de son côté le registre
des appels : le mur compte des appels, pas des fichiers présents.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perdrait le tiers du haut et du bas.

**La difficulté propre à ce module est que trois de ses objets sont du
papier** — le babillard, le feuillet d'automne, l'horaire au mur — alors que
le générateur a l'ordre de ne produire aucun texte lisible. Les prompts
demandent donc des papiers dont la *forme* se lit (un panneau couvert de
feuilles, un dépliant ouvert, une grille de colonnes et de lignes) sans
qu'aucun mot ne se déchiffre : l'élève reconnaît l'objet, et c'est l'exercice
qui en donne le contenu.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n3-loisirs/gen_images.py
  python3 build/contenu/module-n3-loisirs/gen_images.py chaudron-rond
"""
import io, json, pathlib, sys, time

MODULE = 'module-n3-loisirs'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from route_images import generer_image                       # noqa: E402

CENTRE = ("Photographie réaliste, format paysage, lumière naturelle douce, "
          "faible profondeur de champ. Intérieur d'un centre communautaire "
          "québécois ordinaire : murs clairs, plancher de tuiles ou de bois, "
          "mobilier simple et un peu usé, éclairage au plafond. Palette "
          "sobre. Aucun texte lisible, aucune écriture déchiffrable, aucun "
          "logo, aucun filigrane, aucune personne identifiable.")

CUISINE = ("Photographie réaliste, format paysage, gros plan sur un plan de "
           "travail de cuisine collective — comptoir d'acier ou de stratifié "
           "clair, lumière naturelle douce, faible profondeur de champ. "
           "Aucun texte lisible, aucune étiquette, aucun logo, aucun "
           "filigrane, aucune personne identifiable.")

PAPIER = ("Photographie réaliste, format paysage, gros plan sur un imprimé "
          "posé ou affiché, lumière naturelle douce, faible profondeur de "
          "champ. La mise en page se reconnaît — colonnes, lignes régulières, "
          "blocs de texte — mais le lettrage est flou et entièrement "
          "illisible. Aucun logo, aucun filigrane, aucune personne "
          "identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne "
        "au Québec avec une ou deux personnes vues de dos, de trois quarts ou "
        "hors cadrage du visage. Lumière naturelle douce, faible profondeur "
        "de champ. Aucun visage reconnaissable, aucun texte, aucun logo, "
        "aucun filigrane.")

P_EX1 = "Je découvre · Exercice 3 — Dans le centre communautaire"
P_EX3 = "Défi 3 · Exercice 5 — Les outils de la cuisine collective"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Exercice 3 de « Je découvre » — le centre communautaire ───────────
 ('babillard-entree', 'images', P_EX1, PAPIER + " Un grand panneau de liège "
  "accroché dans une entrée d'immeuble, couvert d'une vingtaine de feuilles "
  "de couleurs différentes retenues par des punaises, un peu de travers."),
 ('feuillet-automne', 'images', P_EX1, PAPIER + " Un petit dépliant de "
  "quelques pages, ouvert à plat sur une table de bois, à côté d'une tasse. "
  "On distingue des colonnes et une liste de lignes courtes."),
 ('gymnase-badminton', 'images', P_EX1, CENTRE + " Un gymnase d'école vide au "
  "plancher de bois verni, lignes de jeu peintes au sol, un filet de "
  "badminton tendu au milieu, gradins repliés contre le mur du fond."),
 ('comptoir-accueil', 'images', P_EX1, CENTRE + " Un comptoir d'accueil de "
  "hauteur moyenne, avec un ordinateur, un téléphone et un présentoir de "
  "métal rempli de dépliants, dans un hall clair."),
 ('salle-cuisine', 'images', P_EX1, CENTRE + " Une grande cuisine "
  "communautaire vide : deux longues tables de travail en acier, une "
  "cuisinière au fond, des armoires ouvertes montrant des chaudrons empilés."),
 ('salle-projection', 'images', P_EX1, CENTRE + " Une salle polyvalente "
  "préparée pour une projection : quatre rangées de chaises pliantes "
  "alignées face à un écran blanc, lumière tamisée, projecteur au fond."),
 ('espadrilles-bouteille', 'images', P_EX1, CUISINE.replace('cuisine collective',
  'banc de vestiaire') + " Une paire d'espadrilles de sport blanches et "
  "propres posées sur un banc de bois, une bouteille d'eau réutilisable "
  "debout à côté. Les chaussures sont unies, sans marque visible."),
 ('horaire-mur', 'images', P_EX1, PAPIER + " Une grande feuille quadrillée "
  "affichée au mur d'un corridor, sept colonnes et une douzaine de rangées. "
  "La première rangée d'en-têtes porte les sept jours de la semaine en "
  "français écrits à la main, lisibles : lundi, mardi, mercredi, jeudi, "
  "vendredi, samedi, dimanche. Les cases du corps ne contiennent que des "
  "traits et des blocs de surligneur, aucun mot. Aucun titre au-dessus du "
  "tableau."),

 # ── Exercice 5 du Défi 3 — les outils de la cuisine collective ────────
 ('bol', 'images', P_EX3, CUISINE + " Un grand bol de métal creux posé seul "
  "sur un comptoir, vu de trois quarts, légèrement incliné."),
 ('tasse-mesurer-lait', 'images', P_EX3, CUISINE + " Une tasse à mesurer de "
  "verre transparent remplie de lait jusqu'au tiers, vue de face à hauteur "
  "des yeux. Les graduations sont des traits gravés, sans chiffre lisible."),
 ('poele', 'images', P_EX3, CUISINE + " Une poêle ronde et plate à long "
  "manche, posée sur un rond de cuisinière, vue de trois quarts."),
 ('casserole', 'images', P_EX3, CUISINE + " Une casserole de métal à un seul "
  "manche, couvercle posé à côté, sur un comptoir clair."),
 ('econome', 'images', P_EX3, CUISINE + " Gros plan sur un économe à lame "
  "pivotante posé sur une planche de bois, à côté de deux pommes de terre "
  "dont l'une est à demi pelée, avec des épluchures."),
 ('cuillere-de-bois', 'images', P_EX3, CUISINE + " Une grande cuillère de "
  "bois appuyée en travers d'un chaudron, vue de trois quarts."),
 ('chaudron-rond', 'images', P_EX3, CUISINE + " Un gros chaudron de métal à "
  "deux poignées, posé sur le rond arrière d'une cuisinière, un peu de vapeur "
  "au-dessus."),
 ('tablier', 'images', P_EX3, CUISINE + " Un tablier de coton uni accroché à "
  "un crochet de mur, cordons pendants, à côté d'un linge à vaisselle plié."),

 # ── Les treize photos du banc de vocabulaire ──────────────────────────
 ('centre-communautaire', 'vocab', P_VOC, CENTRE.replace('Intérieur', 'Extérieur')
  + " Un bâtiment de quartier d'un étage, en brique claire, avec une porte "
  "vitrée à double battant et un large trottoir devant."),
 ('babillard', 'vocab', P_VOC, PAPIER + " Un panneau de liège encadré de bois, "
  "sur un mur clair, portant une douzaine de feuilles retenues par des "
  "punaises de couleur."),
 ('loisirs', 'vocab', P_VOC, PERS + " Quatre personnes vues de dos dans un "
  "gymnase, raquettes à la main, en train de bavarder avant de commencer à "
  "jouer."),
 ('gymnase', 'vocab', P_VOC, CENTRE + " Un gymnase au plancher de bois verni "
  "vu du fond, lignes de jeu peintes, paniers de basketball relevés, grandes "
  "fenêtres en haut du mur."),
 ('espadrilles', 'vocab', P_VOC, CUISINE.replace('cuisine collective',
  'vestiaire') + " Gros plan sur une paire d'espadrilles de sport propres, "
  "semelle de caoutchouc bien visible, posées côte à côte sur un banc."),
 ('cine-club', 'vocab', P_VOC, CENTRE + " Une petite salle de projection de "
  "quartier, chaises pliantes en rangées, écran blanc éclairé, lumière "
  "basse."),
 ('seance', 'vocab', P_VOC, PERS + " Une dizaine de personnes assises de dos "
  "dans une petite salle sombre, face à un écran lumineux."),
 ('telehoraire', 'vocab', P_VOC, PAPIER + " Un petit journal ouvert sur une "
  "table, deux colonnes de courts paragraphes séparés par des filets, avec "
  "des chiffres alignés à gauche de chaque bloc."),
 ('documentaire', 'vocab', P_VOC, CENTRE + " Un écran de projection montrant "
  "un paysage de rivière et de forêt du Québec, dans une salle sombre, deux "
  "rangées de chaises vides au premier plan."),
 ('cuisine-collective', 'vocab', P_VOC, PERS + " Trois personnes vues de dos "
  "autour d'une longue table de travail en acier, tabliers noués, en train "
  "de couper des légumes ensemble."),
 ('recette', 'vocab', P_VOC, PAPIER + " Une feuille imprimée posée à plat sur "
  "un comptoir de cuisine, entre une planche à découper et un bol. On "
  "distingue une courte liste en haut et des paragraphes numérotés en bas."),
 ('tasse-a-mesurer', 'vocab', P_VOC, CUISINE + " Une tasse à mesurer de verre "
  "transparent vide, vue de face, graduations gravées sur le côté, posée "
  "seule sur un comptoir clair."),
 ('chaudron', 'vocab', P_VOC, CUISINE + " Un gros chaudron de métal à deux "
  "poignées rempli d'eau, posé sur une cuisinière, vu de trois quarts."),
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
    print('  ✓ %-26s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('  !! ' + e)
