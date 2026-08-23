#!/usr/bin/env python3
"""Les 17 images de module-n8-actualite (niveau 8, activité 122).

Deux destinations :
  · `images/` — les douze photos des deux exercices d'association (`prImg`,
    six lieux du dossier ; `t3img`, six moments de la soirée de
    consultation), réduites à 1200 px qualité 85 ;
  · `vocab/`  — les cinq photos du banc de vocabulaire, réduites à 800 px
    qualité 82. **Onze des seize cartes n'ont pas d'image**, et c'est un
    choix : le lexique de cette situation est presque entièrement abstrait —
    une thèse, une concession, une nuance, un parti pris, une manchette.
    Leur donner une photo aurait mis derrière chaque carte une vue générique
    de salle de rédaction, c'est-à-dire le thème du module à la place de ce
    que dit la carte. C'est le quatrième défaut de la relecture du 22 août
    2026.

**Les quatre règles de prompt sont appliquées ici** (`CLAUDE.md`, « Les
images d'un module ») :

1. aucun texte lisible ;
2. pas de mains ni de visages en gros plan ;
3. un décor québécois nommé — ici une petite ville de l'Estrie, en automne ;
4. **l'image montre ce que dit son énoncé** — chaque prompt est écrit à
   partir de la phrase exacte de la rangée `ok`, recopiée en commentaire
   au-dessus de lui.

**La parade au texte parasite est le cadrage, jamais la négation.** Ce module
est le pire du dépôt de ce point de vue : son sujet *est* de l'écrit. Un
hôtel de ville porte une plaque, un studio de radio porte des étiquettes de
console, un comptoir de bibliothèque porte le dos des livres, un registre
référendaire est un cahier qu'on remplit, un tract est une feuille imprimée.
Chaque prompt ci-dessous sort donc l'inscription du champ plutôt que de
l'interdire : la façade est coupée sous le fronton, la console est vue de
trois quarts arrière et éteinte, les livres sont sur la tranche et hors du
plan de netteté, le cahier est ouvert sur des pages **vierges et lignées**,
et le tract est **plié, verso vers l'objectif**.

**Là où le texte est vraiment le sujet — l'éditorial, les deux dépêches, la
lettre au journal — il n'y a aucune image :** il est composé en HTML, dans
les trois exercices de type `texte`. C'est la règle de `CLAUDE.md`, et elle
est ce qui rend ce module possible.

**Les personnes sont vues de loin et de dos**, et quand une image en porte
plus d'une, sa composition est **imposée** plutôt que laissée au modèle, qui
retombe sinon sur un groupe d'hommes d'une même origine — deux images le
demandaient ici (l'assemblée de consultation, la salle avant l'assemblée).

Le contrôle avant livraison :

    node build/contexte_images.js module-n8-actualite

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix — Google direct, puis fal.ai, puis
WaveSpeed —, rend le nom de celle qui a servi et inscrit chaque tentative au
registre `~/Claude/generations/journal_appels.py`.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu : ce fichier
vit dans `build/contenu/<slug>/`, donc trois niveaux sous la racine — sans
quoi il cesserait de fonctionner dans un worktree.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n8-actualite/gen_images.py
  python3 build/contenu/module-n8-actualite/gen_images.py hotel-de-ville
  python3 build/contenu/module-n8-actualite/gen_images.py vocab/registre
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n8-actualite'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX1 = "Je découvre · Exercice 4 — Les lieux du dossier"
P_EX2 = "Défi 3 · Exercice 6 — La soirée de consultation"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : une petite ville de l'Estrie en octobre. Pas une banlieue
# neuve, pas un centre-ville de métropole — une ville de vingt-quatre mille
# habitants avec ses duplex de brique, ses galeries de bois et ses érables.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle d'un "
         "après-midi d'octobre couvert, faible profondeur de champ. Une "
         "petite ville de l'Estrie, au Québec : duplex et maisons de brique "
         "rouge à galerie de bois peinte, toits de tôle à baguettes, "
         "escaliers de béton, érables aux feuilles rousses, fils "
         "électriques en travers des rues, asphalte fatigué. Palette sobre "
         "et automnale, bâtiments ordinaires et un peu usés. Aucune "
         "personne identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire dans une "
        "petite ville du Québec avec des personnes vues de loin, de dos ou "
        "de trois quarts arrière, jamais en gros plan et jamais les mains "
        "seules au premier plan. Lumière naturelle douce, faible profondeur "
        "de champ. Aucun visage reconnaissable, aucun texte, aucun logo, "
        "aucun filigrane.")

# La négation seule ne tient pas devant un objet qui porte des inscriptions :
# elle sert de filet, pas de parade. La parade est dans chaque prompt, et
# c'est le cadrage.
SANS_MOTS = (" Strictly no letters, no words, no digits and no readable "
             "characters anywhere in the image: every line of text, "
             "including any headline, nameplate, street sign, municipal "
             "plaque, book spine, console label, poster, notice board, "
             "banner or printed sheet, must fall outside the frame, be "
             "switched off, be turned away from the camera, or be an "
             "abstract grey stroke well outside the plane of focus. Aucun "
             "mot d'anglais nulle part, aucun nom de ville, aucune enseigne "
             "lisible, aucun logo.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── prImg · les six lieux du dossier ──────────────────────────────────
 # « De grands érables serrés en lisière, avec les toits d'un quartier
 #   résidentiel juste derrière. »
 ('erables-lisiere', 'images', P_EX1, STYLE + " La lisière d'un boisé "
  "d'érables matures photographiée depuis un champ herbeux : une trentaine de "
  "troncs gris et droits, serrés, de gros diamètre, dont les frondaisons "
  "rousses et jaunes occupent tout le haut de l'image. **Juste derrière la "
  "cime des arbres, on aperçoit les toits de tôle et les cheminées de brique "
  "d'un quartier résidentiel**, très proches, ce qui montre que le boisé "
  "touche la ville. Feuilles mortes au sol, herbe haute jaunie au premier "
  "plan. Aucune clôture, aucun panneau, aucune personne." + SANS_MOTS),
 # « Une étendue plate de gravier et de terre compactée, quelques herbes
 #   éparses, une clôture de mailles. »
 ('remblai-voirie', 'images', P_EX1, STYLE + " Un terrain **plat et nu** de "
  "gravier gris et de terre compactée, photographié à hauteur d'homme depuis "
  "son bord : la surface est dure, marquée d'ornières de camion et de "
  "quelques flaques d'eau, avec seulement des **touffes d'herbe éparses** qui "
  "percent çà et là. Une **clôture de mailles losangées** grise court sur la "
  "droite du cadre et s'éloigne vers le fond. À l'horizon, une ligne d'arbres "
  "roux et un ciel bas et gris. Aucun bâtiment, aucun panneau accroché à la "
  "clôture, aucune personne." + SANS_MOTS),
 # « Un petit hôtel de ville en brique rouge, escalier de béton et lampadaire,
 #   un soir d'automne. »
 # Piège à texte : un hôtel de ville porte toujours une plaque et un drapeau.
 # Le cadre s'arrête sous le fronton et le mât est hors champ.
 ('hotel-de-ville', 'images', P_EX1, STYLE + " Un petit édifice municipal de "
  "deux étages en brique rouge foncé, photographié depuis le trottoir d'en "
  "face au crépuscule : fenêtres à guillotine à cadre blanc, quelques-unes "
  "éclairées d'une lumière chaude, un large **escalier de béton** à "
  "garde-corps de fer noir montant vers une porte à double battant, et un "
  "**lampadaire de fonte allumé** au bas des marches. Le cadre est **coupé "
  "juste au-dessus du linteau de la porte** : le fronton, la plaque du "
  "bâtiment et le mât de drapeau sont entièrement hors champ. Feuilles mortes "
  "sur les marches, ciel bleu sombre. Aucune personne." + SANS_MOTS),
 # « Un studio de radio minuscule : un micro sur bras, un casque posé, des
 #   panneaux de mousse au mur. »
 ('studio-radio', 'images', P_EX1, STYLE + " L'intérieur d'un très petit "
  "studio de radio, vide, vu depuis la porte : un **microphone sur bras "
  "articulé** avec sa bonnette noire, penché au-dessus d'une table de bois "
  "clair, un **casque d'écoute posé à plat** à côté, et des **panneaux de "
  "mousse acoustique gris anthracite** en damier sur le mur du fond. Une "
  "console de mixage occupe le coin droit, vue **de trois quarts arrière et "
  "éteinte** : on n'en voit que le flanc et l'arrière des potentiomètres, "
  "aucune étiquette, aucun afficheur. Chaise de bureau vide, tapis usé, "
  "lumière chaude d'une lampe d'appoint. Aucune personne." + SANS_MOTS),
 # « Un comptoir de retour de bibliothèque, avec un chariot de livres à côté et
 #   une lampe allumée. »
 # Piège à texte : les dos des livres. Ils sont sur la tranche, franchement
 # hors du plan de netteté.
 ('comptoir-bibliotheque', 'images', P_EX1, STYLE + " Un comptoir de "
  "bibliothèque municipale, **derrière lequel il n'y a personne** : plan de "
  "travail de mélamine claire, une **lampe de bureau à abat-jour vert "
  "allumée** posée dessus, un tampon encreur et un pot à crayons. À côté du "
  "comptoir, un **chariot de bibliothèque à deux tablettes** chargé de livres "
  "rangés **sur la tranche**, entièrement **flous** — aucun titre, aucune "
  "couleur de dos discernable. Derrière, des rayonnages de bois hors du plan "
  "de netteté. Aucune affiche au mur, aucun écriteau sur le comptoir, aucune "
  "personne." + SANS_MOTS),
 # « Un grand terrain herbeux et vide derrière un aréna de tôle, sous un ciel
 #   gris. »
 ('terrain-arena', 'images', P_EX1, STYLE + " Un **grand terrain herbeux "
  "entièrement vide**, plat, à l'herbe jaunie et fauchée, occupant les deux "
  "tiers de l'image, sous un **ciel gris uniforme**. Sur la gauche, à "
  "distance, le flanc aveugle d'un **aréna de tôle ondulée beige** à toit "
  "arrondi, avec ses conduits de ventilation sur le toit et une porte de "
  "service métallique. Aucune enseigne, aucun panneau, aucune ligne de jeu "
  "tracée au sol. Quelques arbres roux au fond. Aucune "
  "personne." + SANS_MOTS),

 # ── t3img · les six moments de la soirée de consultation ──────────────
 # « Une salle communautaire remplie de chaises pliantes en rangées, avant que
 #   le monde arrive. »
 ('salle-communautaire', 'images', P_EX2, STYLE + " L'intérieur d'une salle "
  "communautaire de sous-sol d'église, **entièrement vide de gens**, "
  "photographiée depuis le fond : une centaine de **chaises pliantes "
  "métalliques grises alignées en rangées régulières** avec une allée "
  "centrale, faisant face à une petite estrade et à une table pliante. "
  "Plancher de tuiles de vinyle beige, murs de gypse crème, plafond de tuiles "
  "acoustiques et tubes fluorescents allumés. Le mur du fond est **nu** et le "
  "cadre est coupé sous le tableau : aucune affiche, aucune banderole. Aucune "
  "personne." + SANS_MOTS),
 # « Un micro sur pied, seul au milieu de l'allée centrale, devant les
 #   premières rangées. »
 ('micro-allee', 'images', P_EX2, STYLE + " Un **microphone sur pied "
  "télescopique noir**, seul et bien droit, planté au milieu de l'**allée "
  "centrale** d'une salle communautaire, son câble serpentant au sol vers "
  "l'avant. Il est photographié de face, à hauteur de poitrine, avec de part "
  "et d'autre les **premières rangées de chaises pliantes grises**, vides, "
  "qui s'éloignent floues vers l'arrière-plan. Plancher de tuiles beige, "
  "lumière de tubes fluorescents. Aucune personne, aucune affiche, aucun "
  "écriteau." + SANS_MOTS),
 # « Une table pliante dans un hall, un gros cahier relié ouvert dessus et un
 #   stylo posé à côté. »
 # Piège à texte : le cahier. Ses pages sont vierges, lignées, et vues en
 # oblique.
 ('table-registre', 'images', P_EX2, STYLE + " Le hall d'entrée d'un édifice "
  "municipal, plancher de terrazzo et murs de brique claire, avec une "
  "**table pliante rectangulaire** dressée contre un mur : dessus, un **gros "
  "cahier relié ouvert bien à plat**, ses **pages entièrement vierges et "
  "simplement lignées**, vues **en oblique** de sorte qu'aucune écriture ne "
  "serait lisible, et un **stylo à bille posé à côté**, en travers. Une "
  "chaise vide derrière la table. Grande porte vitrée à l'arrière-plan, "
  "floue, laissant entrer la lumière grise du dehors. Aucun panneau, aucune "
  "affiche, aucune personne." + SANS_MOTS),
 # « Une feuille pliée coincée dans la poignée d'une porte de maison, sur une
 #   galerie de bois. »
 # Piège à texte : le tract. Il est plié, verso vers l'objectif.
 ('tract-porte', 'images', P_EX2, STYLE + " La porte d'entrée d'une maison "
  "québécoise, vue depuis la **galerie de bois peinte en gris** : porte de "
  "bois foncé à petite fenêtre, poignée de laiton, et une **feuille de papier "
  "blanc pliée en deux coincée dans la poignée**, qui pend légèrement. La "
  "feuille est **pliée verso vers l'objectif** : sa face imprimée est cachée "
  "contre la porte, et le côté visible est **entièrement blanc et vierge**. "
  "Autour : le garde-corps de bois de la galerie, un paillasson usé, quelques "
  "feuilles mortes, un pot de fleurs fanées. Aucune personne." + SANS_MOTS),
 # « Le stationnement presque vide d'un aréna de tôle, un soir d'automne
 #   pluvieux. »
 ('stationnement-arena', 'images', P_EX2, STYLE + " Un grand stationnement "
  "d'asphalte **presque vide** devant un aréna de tôle ondulée beige à toit "
  "arrondi, un soir d'automne **pluvieux** : cinq ou six autos ordinaires "
  "seulement, éparpillées loin les unes des autres, l'asphalte mouillé et "
  "luisant reflétant la lumière orange de deux lampadaires, des flaques dans "
  "les creux. Ciel gris foncé, presque nuit. Les plaques d'immatriculation "
  "sont coupées par l'angle de vue, et aucun panneau de stationnement n'entre "
  "dans le cadre. Aucune enseigne sur le bâtiment. Aucune "
  "personne." + SANS_MOTS),
 # « Une rue résidentielle bordée de duplex de brique, les arbres du boisé au
 #   bout de la rue. »
 ('rue-des-cedres', 'images', P_EX2, STYLE + " Une rue résidentielle "
  "tranquille photographiée dans son axe, depuis le milieu de la chaussée : "
  "de chaque côté, des **duplex de brique rouge à deux étages avec galeries "
  "de bois et escaliers extérieurs**, de petites cours avant clôturées, "
  "quelques autos stationnées le long du trottoir. **Au bout de la rue, "
  "fermant la perspective, la masse rousse et dense des grands arbres d'un "
  "boisé.** Feuilles mortes dans le caniveau, fils électriques en travers, "
  "ciel gris. Aucun panneau de rue, aucun numéro civique lisible, aucune "
  "personne." + SANS_MOTS),

 # ── Les cinq photos du banc de vocabulaire ────────────────────────────
 # « Une petite station locale sans but lucratif, animée en partie par des
 #   bénévoles. »
 # Distincte de `studio-radio`, qui montre l'intérieur : ici, la façade.
 ('radio-communautaire', 'vocab', P_VOC, STYLE + " La façade d'un **petit "
  "local commercial** au rez-de-chaussée d'un immeuble de brique d'une rue "
  "principale de village, photographiée du trottoir d'en face : une vitrine "
  "et une porte vitrée, des stores vénitiens à mi-hauteur, un intérieur "
  "modestement éclairé qu'on devine à peine. Sur le **toit plat**, bien "
  "visible contre le ciel gris, une **antenne d'émission métallique haubanée** "
  "et deux petites paraboles. La vitrine est **entièrement nue** : aucune "
  "affiche, aucun lettrage, aucune enseigne au-dessus de la porte. Aucune "
  "personne." + SANS_MOTS),
 # « Un petit terrain couvert d'arbres, souvent en ville ou juste à côté. »
 # Distincte de `erables-lisiere`, qui montre la lisière : ici, l'intérieur.
 ('boise', 'vocab', P_VOC, STYLE + " L'**intérieur** d'un boisé d'érables en "
  "automne : un **sentier de terre battue** serpente entre de gros troncs "
  "gris, le sol est entièrement couvert de feuilles mortes rousses et jaunes, "
  "et la lumière filtre à travers les frondaisons. Quelques jeunes arbres et "
  "des fougères sèches en sous-bois. Le sentier est étroit et bordé de "
  "racines. Aucun banc, aucune borne, aucun panneau d'interprétation, aucune "
  "personne." + SANS_MOTS),
 # « Un terrain rempli de terre et de gravier rapportés, où presque rien ne
 #   pousse. »
 # Distincte de `remblai-voirie`, vue large : ici, le sol de près.
 ('remblai', 'vocab', P_VOC, STYLE + " Le sol d'un ancien terrain de voirie, "
  "photographié de près et en oblique : un **remblai de gravier concassé et "
  "de terre grise compactée**, dur et inégal, mêlé de morceaux de béton "
  "cassé et de vieilles briques, avec seulement **trois ou quatre touffes "
  "d'herbe rase** qui survivent dans les creux. Une **bordure de béton "
  "fissurée** traverse le bas du cadre. Au fond, flou, un tas de gravier et "
  "une ligne d'arbres. Aucun engin, aucun panneau, aucune "
  "personne." + SANS_MOTS),
 # « La rencontre publique où une ville explique un projet et écoute les
 #   gens. »
 # Composition imposée : sans cela le modèle rend un groupe d'hommes d'une
 # seule origine, ce que ne montre aucune classe de francisation.
 ('assemblee-consultation', 'vocab', P_VOC, PERS + " " + STYLE + " Une salle "
  "communautaire **pleine de monde**, photographiée **du fond de la salle, en "
  "légère plongée** : une quarantaine de personnes assises sur des chaises "
  "pliantes grises, **toutes vues de dos**, aucun visage visible, tournées "
  "vers une petite estrade éclairée au fond où l'on distingue une table et "
  "deux silhouettes assises, minuscules et floues. Une personne debout dans "
  "l'allée centrale, de dos, devant un micro sur pied. L'assistance est "
  "**visiblement mixte et d'origines diverses** : hommes et femmes de tous "
  "âges, cheveux de couleurs et de coiffures variées, quelques foulards, "
  "manteaux d'automne sur les dossiers. Aucune banderole, aucun écran de "
  "projection, aucune affiche au mur." + SANS_MOTS),
 # « Le cahier qu'on ouvre une journée pour compter ceux qui demandent un
 #   référendum. »
 ('registre', 'vocab', P_VOC, STYLE + " Un **gros cahier relié à couverture "
  "de toile sombre, ouvert à plat** sur une table de bois, photographié en "
  "**plongée oblique** depuis le coin de la table : ses deux pages sont "
  "**entièrement vierges**, simplement **rayées de lignes horizontales "
  "pâles** et d'une marge verticale, sans une seule inscription. Un **stylo "
  "à bille noir posé en travers** de la page de droite, et un ruban signet "
  "qui dépasse. Lumière latérale rasante d'une fenêtre, le reste de la table "
  "flou. Aucune main, aucune personne, aucun formulaire, aucun "
  "en-tête." + SANS_MOTS),
]


def reduire(data, largeur, qualite):
    """L'image d'exercice occupe 223 x 132 px à l'écran, la photo du banc moins.

    La hauteur suit le rapport de l'image reçue plutôt que d'être forcée à un
    carré — c'est l'objet du passage au 3:2.
    """
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
    print('  ✓ %-26s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('   ✗ ' + e)
