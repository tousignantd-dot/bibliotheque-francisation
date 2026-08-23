#!/usr/bin/env python3
"""Les 10 images de module-n8-habitation (niveau 8, activité 121).

Deux destinations :
  · `images/` — les six photos de l'exercice d'association `prImg` (le
    sous-sol deux jours après), réduites à 1200 px qualité 85 ;
  · `vocab/`  — les quatre photos du banc de vocabulaire, réduites à 800 px
    qualité 82.

**Douze des seize cartes n'ont pas d'image**, et c'est un choix. Le lexique
d'un dossier d'assurance refusé est en grande partie abstrait — une
exclusion, une franchise, un motif, une révision, un transfert de dossier.
Leur donner une photo aurait mis derrière chaque carte une vue générique de
sous-sol inondé, c'est-à-dire le thème du module à la place de ce que dit la
carte : c'est le quatrième défaut de la relecture du 22 août 2026.

Deux cartes ont perdu leur image en cours de route, et la raison mérite d'être
écrite : « une facture acquittée » et « une décision motivée » sont des
**documents**, c'est-à-dire des objets dont le texte *est* le sujet. La parade
au texte parasite — cadrer l'inscription hors du champ — ne s'applique pas :
sortir le texte du cadre d'une facture, c'est ne plus montrer de facture. La
règle de `CLAUDE.md` le dit autrement : quand le texte est le sujet, il se
compose en HTML, jamais dans l'image. Ces deux mots-là vivent donc dans le
troisième exercice `texte` du défi 3, où ils sont lisibles et corrects.

**Les quatre règles de prompt sont appliquées ici** (`CLAUDE.md`, « Les
images d'un module ») :

1. aucun texte lisible ;
2. pas de mains ni de visages en gros plan ;
3. un décor québécois nommé — ici Trois-Rivières et la Mauricie, un duplex de
   brique d'après-guerre, son sous-sol fini et sa ruelle ;
4. **l'image montre ce que dit son énoncé** — chaque prompt est écrit à partir
   de la phrase exacte de la rangée `ok`, recopiée en commentaire au-dessus de
   lui.

**La parade au texte parasite est le cadrage, jamais la négation.** Ce module
est plein d'objets qui portent des inscriptions : le couvercle de fonte d'un
regard d'égout, la plaque d'un clapet antiretour, le boîtier d'un ventilateur
de séchage, le dossard d'un expert, le flanc d'un touret de câble. Écrire
« aucun texte » ne les enlève pas — le modèle écrit du charabia à la place.
Chaque prompt ci-dessous sort donc l'inscription du champ : la fonte est vue
sous l'eau et dans le reflet, la plaque du clapet est tournée vers le mur, le
boîtier du ventilateur est hors du plan de netteté, le dossard est vu de dos
et nu, le flanc du touret est coupé par le bord.

**Les personnes sont vues de loin et de dos.** Une seule image en comporte —
l'expert en sinistre — parce que le mot désigne une personne ; elle est cadrée
de trois quarts arrière, à distance, sans visage ni mains au premier plan.

Le contrôle avant livraison :

    node build/contexte_images.js module-n8-habitation

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix — Google direct, puis fal.ai, puis
WaveSpeed —, rend le nom de celle qui a servi et inscrit chaque tentative au
registre `~/Claude/generations/journal_appels.py`.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu : ce fichier
vit dans `build/contenu/<slug>/`, donc trois niveaux sous la racine — sans
quoi il cesserait de fonctionner dans un worktree.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n8-habitation/gen_images.py
  python3 build/contenu/module-n8-habitation/gen_images.py regard-ruelle
  python3 build/contenu/module-n8-habitation/gen_images.py vocab/clapet-antiretour
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n8-habitation'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 4 — Le sous-sol, deux jours après"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : Trois-Rivières au début de l'automne, un duplex de brique
# d'après-guerre. Pas « appartement moderne » — c'est exactement ce qu'on
# évite, et ça sort générique américain.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle grise de "
         "début d'automne, faible profondeur de champ. Trois-Rivières, "
         "Mauricie : duplex de brique rouge d'après-guerre, escalier "
         "extérieur en acier, ruelle asphaltée, sous-sol fini aux murs de "
         "gypse peints en beige et au plancher flottant imitation chêne, "
         "plafond suspendu à tuiles, calorifères électriques bas le long des "
         "murs, fenêtres à guillotine étroites au ras du sol. Palette sobre, "
         "mobilier ordinaire et un peu usé. Aucune personne identifiable, "
         "aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire dans un "
        "sous-sol de duplex de Trois-Rivières avec une personne vue de loin, "
        "de dos ou de trois quarts arrière, jamais en gros plan et jamais les "
        "mains seules au premier plan. Lumière naturelle douce, faible "
        "profondeur de champ. Aucun visage reconnaissable, aucun texte, aucun "
        "logo, aucun filigrane.")

# La négation seule ne tient pas devant un objet qui porte des inscriptions :
# elle sert de filet, pas de parade. La parade est dans chaque prompt, et
# c'est le cadrage.
SANS_MOTS = (" Strictly no letters, no words, no digits and no readable "
             "characters anywhere in the image: every line of text, "
             "including any cast lettering on a manhole cover, valve "
             "nameplate, appliance label, safety placard, invoice, warning "
             "sticker or cable-reel marking, must fall outside the frame, be "
             "turned away from the camera, be submerged, or be an abstract "
             "grey stroke. Aucun mot d'anglais nulle part, aucun nom "
             "d'entreprise, aucune enseigne lisible, aucun logo.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── prImg · le sous-sol, deux jours après ─────────────────────────────
 # « Un sous-sol fini où l'eau brune arrive à mi-mollet, entre un divan et une
 #   bibliothèque basse. »
 ('sous-sol-inonde', 'images', P_EX, STYLE + " Un sous-sol fini de duplex "
  "**inondé** : une nappe d'eau brunâtre et opaque couvre tout le plancher et "
  "monte à une quinzaine de centimètres, jusqu'au bas des meubles. Au premier "
  "plan à gauche, un divan de tissu gris dont les pieds et le bas des coussins "
  "trempent ; à droite, une bibliothèque basse en mélamine blanche dont la "
  "tablette du bas est sous l'eau. La surface de l'eau reflète le plafond "
  "suspendu et une fenêtre étroite au ras du sol. Les tranches des livres de "
  "la bibliothèque sont floues et illisibles ; aucune couverture n'est "
  "lisible, aucune affiche au mur. Aucune personne." + SANS_MOTS),
 # « Le drain rond au centre d'une dalle de béton, sa grille de fonte soulevée
 #   et posée à côté. »
 ('drain-de-plancher', 'images', P_EX, STYLE + " Vue en plongée serrée sur une "
  "dalle de béton gris nu, propre et sèche, dans un local technique de "
  "sous-sol. Au centre, l'ouverture ronde d'un drain de plancher, environ dix "
  "centimètres de diamètre, sombre à l'intérieur ; sa **grille de fonte ronde "
  "est soulevée et posée à plat juste à côté**, à quelques centimètres, "
  "montrant sa **face inférieure rugueuse et rouillée**, sans aucune lettre "
  "moulée. Un léger cerne brunâtre auréole le pourtour de l'ouverture. Rien "
  "d'autre dans le champ, aucune personne, aucun outil." + SANS_MOTS),
 # « Des lés de plancher flottant gondolés et des bacs de plastique empilés au
 #   bord d'un trottoir, un matin d'automne. »
 ('bord-de-trottoir', 'images', P_EX, STYLE + " Le bord d'un trottoir de "
  "béton devant un duplex de brique rouge, un matin d'automne gris. Sur le "
  "gazon jauni, un tas de déchets de sinistre : des **lés de plancher "
  "flottant imitation chêne, visiblement gondolés et gonflés**, empilés en "
  "vrac et appuyés les uns sur les autres, et à côté une pile de **bacs de "
  "rangement en plastique translucide**, certains sans couvercle. Feuilles "
  "mortes mouillées sur l'asphalte, ciel bas. Les bacs n'ont **aucune "
  "étiquette collée** et aucune inscription moulée visible : leurs faces "
  "portant des marques sont tournées vers l'intérieur du tas. Aucune "
  "personne." + SANS_MOTS),
 # « Deux ventilateurs de séchage posés au pied d'un mur dont le gypse a été
 #   coupé à mi-hauteur. »
 ('ventilateurs-sechage', 'images', P_EX, STYLE + " Un mur de sous-sol dont le "
  "**gypse a été découpé horizontalement à mi-hauteur**, laissant voir, sur "
  "toute la longueur de la coupe, les montants de bois et l'isolant rose mis à "
  "nu au bas du mur. Au pied de ce mur, **deux ventilateurs de séchage "
  "professionnels de forme trapézoïdale**, l'un rouge et l'autre bleu, posés "
  "au sol et orientés vers la cavité, leurs câbles électriques orange courant "
  "sur le béton. Les panneaux de commande des ventilateurs sont **hors du plan "
  "de netteté**, complètement flous, et aucune plaque n'est lisible. Plancher "
  "de béton nu, plinthes arrachées et empilées au fond. Aucune "
  "personne." + SANS_MOTS),
 # « Un regard d'égout dans une ruelle de brique, l'eau qui affleure au ras de
 #   la fonte sous une averse. »
 ('regard-ruelle', 'images', P_EX, STYLE + " Une ruelle asphaltée étroite "
  "entre deux murs de brique rouge, sous une **averse battante**. Au centre de "
  "la chaussée, un **regard d'égout circulaire en fonte** dont le couvercle "
  "**disparaît sous une pellicule d'eau qui affleure et déborde légèrement**, "
  "formant des rides concentriques. Le relief moulé du couvercle est effacé "
  "par l'eau et par le reflet du ciel : **aucune lettre n'est discernable**. "
  "Gouttes qui rebondissent, flaques, murs de brique sombres et mouillés de "
  "chaque côté. Aucune personne, aucun véhicule." + SANS_MOTS),
 # « Un touret de câble de caméra déroulé sur le béton, devant l'ouverture d'un
 #   drain de fondation. »
 # Refaite le 23 août 2026. La première version cadrait le touret **en
 # entier**, roues comprises, et le modèle a couvert son flanc
 # d'autocollants blancs et orange parfaitement lisibles — la première règle,
 # prise en défaut par l'objet le plus banal de la scène. Écrire « flanc coupé
 # par le bord droit » ne suffisait pas : tant que l'objet est le sujet, le
 # modèle le montre en entier. Le prompt refait change de **sujet** : ce n'est
 # plus le touret, c'est le **câble et l'ouverture du drain**, et le touret
 # n'entre plus dans le champ que par sa moitié inférieure, de dos.
 ('camera-de-drain', 'images', P_EX, STYLE + " Vue basse, presque au ras du "
  "plancher de béton nu d'un sous-sol, cadrée sur l'**ouverture d'un tuyau de "
  "drain** qui sort du mur de fondation au ras de la dalle. Un **câble noir "
  "souple** s'engage dans cette ouverture et se déroule vers l'appareil en "
  "**larges boucles posées à plat sur le béton**, occupant tout le premier "
  "plan ; la petite tête de caméra est visible juste avant l'ouverture, sa "
  "diode allumée. Le touret d'où vient le câble n'apparaît qu'**au bord "
  "gauche du cadre, de dos et coupé à mi-hauteur** : on n'en voit que la "
  "tranche du bâti et le bas de deux roues, aucune surface plane tournée vers "
  "l'appareil. Aucun écran dans le champ. Lumière rasante d'une baladeuse "
  "posée au sol, hors cadre. Aucune personne." + SANS_MOTS),

 # ── Les quatre photos du banc de vocabulaire ──────────────────────────
 # « La remontée des eaux usées par les drains d'un bâtiment, souvent pendant
 #   une grosse pluie. »
 ('refoulement-egout', 'vocab', P_VOC, STYLE + " Cadrage serré en plongée sur "
  "un drain de plancher de béton d'où **l'eau brunâtre remonte activement** : "
  "un bouillonnement trouble s'échappe de la grille de fonte et s'étale en "
  "nappe autour d'elle, gagnant déjà quelques mètres carrés de la dalle. "
  "Quelques bulles et un écume grisâtre à la surface. La grille est vue de "
  "trois quarts et son relief est noyé sous l'eau : **aucune lettre moulée "
  "n'est discernable**. Au fond, flou, le bas d'un mur de gypse beige et une "
  "plinthe qui commence à foncer. Aucune personne." + SANS_MOTS),
 # « Un petit dispositif installé sur un drain, qui laisse l'eau sortir mais
 #   l'empêche de revenir. »
 ('clapet-antiretour', 'vocab', P_VOC, STYLE + " Cadrage serré sur un "
  "**boîtier de clapet antiretour encastré dans une dalle de béton** : un "
  "corps cylindrique de fonte et de plastique noir d'une trentaine de "
  "centimètres, **son couvercle rond dévissé et posé de champ contre le "
  "boîtier**, laissant voir à l'intérieur le volet articulé qui bascule sur sa "
  "charnière. Le béton fraîchement scié tout autour montre la reprise de "
  "coulée. La **plaque signalétique du couvercle est tournée vers le mur**, "
  "hors de vue ; aucune inscription n'est lisible sur le corps. Lumière crue "
  "d'une lampe de chantier. Aucune personne." + SANS_MOTS),
 # « La personne qui examine les dommages, en cherche la cause et évalue ce
 #   qu'ils coûtent. »
 ('expert-en-sinistre', 'vocab', P_VOC, PERS + " " + STYLE + " Une personne "
  "en veste de travail et bottes de caoutchouc, vue **de dos et de loin**, "
  "accroupie à trois mètres de l'appareil devant un mur de sous-sol dont le "
  "gypse a été ouvert au bas. Elle éclaire l'intérieur de la cavité avec une "
  "lampe de poche tenue basse ; un appareil photo pend à son épaule. Le dos de "
  "sa veste est **uni, sans aucune inscription ni écusson**. Le reste du "
  "sous-sol est flou : plancher de béton nu, ventilateur de séchage éteint au "
  "fond. Aucun visage visible, aucune main au premier plan." + SANS_MOTS),
 # « Le tuyau perforé posé au pied des murs d'un bâtiment pour évacuer l'eau du
 #   sol. »
 ('drain-de-fondation', 'vocab', P_VOC, STYLE + " Une **tranchée ouverte le "
  "long d'un mur de fondation de béton**, à l'extérieur d'un duplex de brique, "
  "vue dans sa longueur en perspective. Au fond de la tranchée, sur un lit de "
  "pierre nette grise, court un **tuyau de drain noir ondulé et perforé**, "
  "partiellement recouvert d'une membrane géotextile blanche déroulée. La "
  "terre remuée forme un talus d'un côté ; on aperçoit en haut du cadre le bas "
  "du mur de brique et une fenêtre de sous-sol. Aucun panneau de chantier, "
  "aucun ruban imprimé, aucun véhicule. Aucune personne." + SANS_MOTS),
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
