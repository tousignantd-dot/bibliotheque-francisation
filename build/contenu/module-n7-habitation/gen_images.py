#!/usr/bin/env python3
"""Les 15 images de module-n7-habitation (niveau 7, activité 112).

Deux destinations :
  · `images/` — les six photos de l'exercice 3 de « Je découvre », réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les neuf photos du banc de vocabulaire, réduites à 800 px
    qualité 82 (sept des seize cartes n'ont pas d'image : « un inconvénient
    normal », « une concession », « un reproche », « un témoin », « le
    règlement municipal », « un délai raisonnable » et « une diminution de
    loyer » sont des abstractions ou des documents qui ne s'illustrent pas
    sans texte).

**Les quatre règles de prompt du 22 août 2026 sont appliquées ici**, et elles
sont écrites dans `CLAUDE.md` (« Les images d'un module ») :

1. aucun texte lisible — d'où `SANS_MOTS`, exigé sur chaque image ;
2. pas de mains ni de visages en gros plan ;
3. un décor québécois nommé — triplex de brique, escalier extérieur en métal
   peint, rampe de bois, plinthes hautes — plutôt qu'« appartement moderne » ;
4. **l'image montre ce que dit son énoncé.** Les six prompts d'exercice sont
   écrits à partir de la phrase exacte de la rangée `ok` de `prImg`, recopiée
   en commentaire au-dessus de chacun ; les neuf prompts de vocabulaire, à
   partir de la définition de la carte. Le contrôle avant livraison :

       node build/contexte_images.js module-n7-habitation

**Ce que les quatre modules du 23 août ont appris, et qui est appliqué ici.**
La règle 1 ne suffit pas devant un objet qui *porte* des inscriptions : le
modèle les écrit quand même, en charabia ou en anglais (« PLAY », « STOP »,
« March », « 1:520 »). La parade est de **cadrer l'inscription hors champ**,
jamais de répéter l'interdiction. Cinq images de ce module sont concernées et
le disent dans leur prompt : la console du tapis roulant, les numéros de
porte du palier, les numéros de casier du vestiaire, le numéro civique du
triplex et le décalque du cadre de vélo sont tous **coupés par le bord de
l'image**. Même chose pour les mains : `arrangement-a-lamiable` impose le
poste de l'appareil (« depuis le bas de la volée d'escalier, à hauteur de
taille ») au lieu d'interdire les gros plans.

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix — Google direct, puis fal.ai, puis
WaveSpeed —, rend le nom de celle qui a servi et inscrit chaque tentative au
registre `~/Claude/generations/journal_appels.py`.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu : ce fichier
vit dans `build/contenu/<slug>/`, donc trois niveaux sous la racine — sans
quoi il cesserait de fonctionner dans un worktree.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n7-habitation/gen_images.py
  python3 build/contenu/module-n7-habitation/gen_images.py palier
  python3 build/contenu/module-n7-habitation/gen_images.py vocab/nuisance-sonore
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n7-habitation'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 3 — Les lieux du dossier de Ruslana"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : Limoilou, à Québec, à la fin de l'hiver. Des logements
# ordinaires de triplex, pas des intérieurs de catalogue.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle de fin "
         "d'hiver, faible profondeur de champ. Quartier ancien d'une ville du "
         "Québec : triplex de brique rouge ou beige, escaliers extérieurs en "
         "métal peint, fenêtres à guillotine, à l'intérieur plancher de bois "
         "franc usé, plinthes hautes peintes, plinthes électriques, mobilier "
         "ordinaire et un peu dépareillé, palette sobre. Aucun texte lisible, "
         "aucun mot déchiffrable, aucun logo, aucune marque, aucun filigrane, "
         "aucune personne identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire au Québec avec "
        "une ou deux personnes vues de loin, de dos ou de trois quarts "
        "arrière, jamais en gros plan et jamais les mains seules au premier "
        "plan. Lumière naturelle douce, faible profondeur de champ. Aucun "
        "visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

# Ce module est plein d'objets qui portent des inscriptions : une console de
# tapis roulant, des numéros de porte, des numéros de casier, un cadre de
# vélo, une lettre. La négation ne suffit pas ; le cadrage, oui.
SANS_MOTS = (" Strictly no letters, no words, no digits and no readable "
             "characters anywhere in the image: every line of text, including "
             "any headline, label, display, sign, door number or brand decal, "
             "must be either cropped out of frame or rendered as an abstract "
             "grey stroke. Aucun mot d'anglais nulle part, aucune enseigne "
             "lisible, aucun chiffre lisible.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 3 ────────────────────────────────────
 # « Un tapis roulant installé contre le mur d'un salon de logement, à côté
 #   d'une bibliothèque basse. »
 # La console de l'appareil porte toujours des chiffres et des mots : elle est
 # coupée par le bord haut du cadre, on ne voit que le tapis et les montants.
 ('tapis-roulant-logement', 'images', P_EX, STYLE + " Un tapis roulant "
  "domestique installé contre le mur d'un salon de logement de triplex, à côté "
  "d'une bibliothèque basse en bois. Vue de trois quarts arrière, en légère "
  "plongée depuis l'autre bout de la pièce : la console et le guidon de "
  "l'appareil sont entièrement hors champ, coupés par le bord supérieur de "
  "l'image, et l'on ne voit que la bande de roulement, les montants et le "
  "socle. Plancher de bois franc, plinthe haute peinte, fenêtre à guillotine "
  "sur la gauche. Aucune personne." + SANS_MOTS),
 # « Une chambre à coucher encore sombre, où seule la fenêtre commence à
 #   pâlir. »
 # Aucun réveil dans le cadre : un afficheur produirait des chiffres inventés.
 ('chambre-a-laube', 'images', P_EX, STYLE + " Une petite chambre à coucher de "
  "logement ancien, encore dans la pénombre : lit défait avec une couette "
  "froissée, table de chevet en bois, mur peint clair. Le seul éclairage vient "
  "de la fenêtre à guillotine, dont le store est à demi relevé et derrière "
  "laquelle le ciel commence à peine à pâlir en bleu très sombre. Aucun réveil, "
  "aucun écran, aucun afficheur dans le cadre. Aucune personne." + SANS_MOTS),
 # « Un escalier intérieur étroit à rampe de bois, entre deux étages d'un
 #   triplex. »
 ('escalier-interieur-triplex', 'images', P_EX, STYLE + " Un escalier intérieur "
  "étroit de triplex, vu du bas de la volée : marches de bois recouvertes d'un "
  "tapis usé, rampe de bois vernie fixée au mur, mur de plâtre peint beige, "
  "plafonnier simple sur le palier au-dessus. Lumière chaude et un peu faible. "
  "Aucune personne, aucune inscription, aucun numéro." + SANS_MOTS),
 # « Un vélo de route appuyé contre le mur d'une entrée de logement, près
 #   d'une porte. »
 # Les cadres de vélo portent un décalque de marque : cadre uni, et le tube
 # diagonal partiellement masqué par la rampe.
 # Refaite le 23 août 2026. La première version plaçait le vélo **dehors**,
 # appuyé contre l'escalier extérieur, avec la porte ouverte au fond : c'était
 # une belle photo de rue et ce n'était pas ce que dit l'énoncé, qui parle
 # d'une entrée de logement. Défaut n° 4 exactement — il ne se voit qu'avec la
 # phrase à côté. Le prompt refait **enferme la scène** : plus de rue, plus de
 # neige, plus d'escalier extérieur, seulement le vestibule.
 ('velo-dans-lentree', 'images', P_EX, STYLE + " Intérieur seulement : le "
  "vestibule d'entrée d'un logement de triplex, porte fermée. Un vélo de route "
  "est appuyé par la selle et le guidon contre le mur de plâtre peint, à un "
  "pas d'une porte de bois peinte foncée qui reste close. Le cadre du vélo est "
  "d'une seule couleur mate, entièrement uni, sans le moindre décalque ni la "
  "moindre inscription. Vue de trois quarts arrière, à hauteur de taille. "
  "Plancher de bois franc, tapis d'entrée mouillé, bottes rangées le long de "
  "la plinthe haute, patère de métal au mur avec un manteau. Aucune fenêtre "
  "sur la rue, aucune vue extérieure, aucune neige, aucun escalier extérieur. "
  "Aucune personne." + SANS_MOTS),
 # « Un vestiaire de personnel avec des casiers de métal et un banc de bois. »
 # Les portes de casier portent des numéros : le cadrage s'arrête à mi-hauteur.
 ('vestiaire-hopital', 'images', P_EX, STYLE + " Un vestiaire de personnel "
  "d'établissement de santé : une rangée de casiers de métal peint vert pâle et "
  "un long banc de bois devant eux. Cadrage en largeur qui s'arrête à "
  "mi-hauteur des casiers, de sorte que les plaques numérotées du haut des "
  "portes sont entièrement hors champ, coupées par le bord supérieur de "
  "l'image. Plancher de linoléum, éclairage de plafonniers. Aucune personne." + SANS_MOTS),
 # « Un triplex de brique avec un escalier extérieur en métal peint, au bout
 #   d'une rue enneigée. »
 # Le numéro civique est hors champ : la façade est prise en contre-plongée
 # depuis le trottoir opposé, et le bas du perron est coupé.
 ('triplex-8e-avenue', 'images', P_EX, STYLE + " Un triplex de brique rouge de "
  "trois étages avec un escalier extérieur en métal peint noir qui monte en "
  "biais vers le balcon du deuxième, dans une rue résidentielle enneigée d'un "
  "quartier ancien de Québec. Vue depuis le trottoir d'en face, en légère "
  "contre-plongée : le bas du perron et la plaque du numéro civique sont hors "
  "champ, coupés par le bord inférieur de l'image. Bancs de neige gris le long "
  "de la rue, ciel bas de fin d'hiver. Aucune personne, aucune enseigne, aucun "
  "numéro visible." + SANS_MOTS),

 # ── Les neuf photos du banc de vocabulaire ────────────────────────────
 # « un trouble de voisinage » — le dérangement qu'une personne fait subir à
 #   celle qui habite au-dessus ou à côté, dans l'usage normal de son logement.
 ('trouble-de-voisinage', 'vocab', P_VOC, STYLE + " Contre-plongée depuis un "
  "canapé vers le plafond d'un salon de logement ancien : un luminaire "
  "suspendu à une tige, très légèrement flou comme s'il oscillait, une moulure "
  "de plâtre au raccord du mur, une fissure fine dans la peinture. La pièce "
  "est dans une lumière grise de petit matin. Aucune personne, aucun texte." + SANS_MOTS),
 # « une nuisance sonore » — un bruit qui dépasse ce qu'une personne
 #   raisonnable accepterait, par son heure, sa force ou sa répétition.
 ('nuisance-sonore', 'vocab', P_VOC, STYLE + " Gros plan sur une table de "
  "chevet en bois dans une chambre sombre : une paire de bouchons d'oreille en "
  "mousse orange posés à côté d'un verre d'eau, un coin d'oreiller froissé au "
  "premier plan, hors du plan de netteté. Lumière très basse, bleutée. Aucune "
  "personne, aucune main, aucun écran, aucune inscription." + SANS_MOTS),
 # « la jouissance paisible » — le droit d'habiter son logement tranquille,
 #   sans être dérangé sans arrêt par quelqu'un d'autre.
 ('jouissance-paisible', 'vocab', P_VOC, STYLE + " Un salon de logement ancien "
  "rangé et silencieux un matin de congé : un fauteuil rembourré, une tasse de "
  "café fumante posée sur une table basse en bois, une couverture pliée sur "
  "l'accoudoir, et un large rayon de soleil qui traverse le plancher de bois "
  "franc depuis la fenêtre à guillotine. Aucune personne, aucun texte." + SANS_MOTS),
 # « un palier » — l'espace plat, devant les portes, où l'escalier s'arrête à
 #   chaque étage.
 ('palier', 'vocab', P_VOC, STYLE + " Le palier du dernier étage d'un triplex : "
  "un petit espace plat de plancher de bois où débouche une volée d'escalier, "
  "une rampe de bois vernie, deux portes de logement peintes côte à côte et un "
  "paillasson usé. Cadrage à hauteur de poitrine, de sorte que la moitié "
  "supérieure des portes, où seraient les plaques numérotées, est hors champ. "
  "Plafonnier simple, lumière chaude. Aucune personne." + SANS_MOTS),
 # « un arrangement à l'amiable » — une solution que deux personnes trouvent
 #   elles-mêmes, sans juge et sans papier officiel.
 # Le poste de l'appareil est imposé plutôt que les gros plans interdits :
 # c'est ce qui a marché du premier coup sur l'activité 109.
 ('arrangement-a-lamiable', 'vocab', P_VOC, PERS + " Deux personnes debout sur "
  "le palier d'un triplex, en train de se parler calmement : l'une dans "
  "l'embrasure de sa porte entrouverte, l'autre à un pas de là, une main sur la "
  "rampe. L'appareil est placé au bas de la volée d'escalier, à hauteur de "
  "taille, de sorte qu'on les voit de dos et de loin, en légère contre-plongée, "
  "sans aucun visage. Lumière chaude de plafonnier, fin de soirée. Aucune "
  "inscription, aucun numéro de porte visible." + SANS_MOTS),
 # « un registre des bruits » — le carnet où l'on note chaque jour l'heure, la
 #   durée et la nature de ce qu'on entend.
 ('registre-des-bruits', 'vocab', P_VOC, STYLE + " Un petit carnet à spirale "
  "ouvert à plat sur une table de chevet en bois, montrant deux pages de "
  "lignes manuscrites disposées en colonnes régulières, avec un crayon à mine "
  "posé en travers. Chaque ligne écrite est un trait d'encre grise entièrement "
  "illisible ; seule la structure en colonnes se distingue. Lumière de lampe de "
  "chevet. Aucune personne, aucune main dans le cadre." + SANS_MOTS),
 # « la médiation citoyenne » — un service gratuit où une personne neutre aide
 #   deux voisins à se parler jusqu'à ce qu'ils trouvent eux-mêmes une entente.
 ('mediation-citoyenne', 'vocab', P_VOC, STYLE + " Une petite salle de local "
  "communautaire de quartier : trois chaises de bois disposées autour d'une "
  "table ronde, une carafe d'eau et trois verres au centre, une boîte de "
  "mouchoirs. Mur de brique peint en blanc, plancher de tuiles, lumière du jour "
  "par une fenêtre à gauche. La salle est vide. Aucune personne, aucune "
  "affiche, aucun tableau écrit." + SANS_MOTS),
 # « une mise en demeure » — une lettre qui expose un problème, demande
 #   précisément quelque chose et donne un délai pour le faire.
 ('mise-en-demeure', 'vocab', P_VOC, STYLE + " Une feuille blanche pliée en "
  "trois puis rouverte, posée à plat sur une table de cuisine à côté d'une "
  "enveloppe blanche fermée. On distingue la disposition d'une lettre — un bloc "
  "d'adresse en haut à gauche, une courte ligne d'objet soulignée, trois "
  "paragraphes séparés par des blancs, une signature manuscrite en bas — mais "
  "chaque ligne écrite est un trait gris entièrement illisible. Un stylo posé "
  "en travers. Aucune personne, aucune main." + SANS_MOTS),
 # « un courrier recommandé » — un envoi postal dont on garde la preuve, parce
 #   que la personne doit signer pour le recevoir.
 # Le reçu est sorti du plan de netteté : c'est la consigne qui marche quand
 # « aucun texte » ne suffit pas.
 ('courrier-recommande', 'vocab', P_VOC, STYLE + " Une enveloppe blanche "
  "cachetée posée sur un comptoir de bois clair, avec une étiquette "
  "autocollante rectangulaire dans le coin supérieur droit dont les traits ne "
  "forment aucun caractère lisible. Derrière l'enveloppe, entièrement hors du "
  "plan de netteté, un petit reçu de papier et un tampon de caoutchouc. "
  "Lumière neutre de plafonnier. Aucune personne, aucune main, aucune enseigne, "
  "aucun logo." + SANS_MOTS),
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
