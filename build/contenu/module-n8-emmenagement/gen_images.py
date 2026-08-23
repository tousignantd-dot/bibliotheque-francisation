#!/usr/bin/env python3
"""Les 16 images de module-n8-emmenagement (niveau 8, activité 120).

Deux destinations :
  · `images/` — les douze photos des deux exercices d'association (`prImg`,
    six traces laissées par le déménagement ; `t1img`, six sinistres et la
    protection qui les vise), réduites à 1200 px qualité 85 ;
  · `vocab/`  — les quatre photos du banc de vocabulaire, réduites à 800 px
    qualité 82. **Douze des seize cartes n'ont pas d'image**, et c'est un
    choix, pas un oubli : le lexique de l'assurance est un lexique de
    clauses — une franchise, un avenant, une exclusion, la responsabilité
    civile, la dépréciation, la subrogation ne se photographient pas. Leur
    donner une photo aurait mis derrière chaque carte une vue générique de
    bureau ou de boîtes de carton, c'est-à-dire le thème du module à la
    place de ce que dit la carte. C'est le quatrième défaut de la relecture
    du 22 août 2026, et `module-n7-oeuvres` puis `module-n8-recherche` ont
    tranché dans le même sens.

**Les quatre règles de prompt sont appliquées ici** (`CLAUDE.md`, « Les
images d'un module ») :

1. aucun texte lisible ;
2. pas de mains ni de visages en gros plan ;
3. un décor québécois nommé — ici Trois-Rivières et la Mauricie ;
4. **l'image montre ce que dit son énoncé** — chaque prompt est écrit à
   partir de la phrase exacte de la rangée `ok`, recopiée en commentaire
   au-dessus de lui.

**La parade au texte parasite est le cadrage, jamais la négation.** Ce
module est un piège à inscriptions : un connaissement est un formulaire, un
inventaire est une liste, une boîte de déménagement porte le nom d'une pièce
au marqueur, un camion porte une livrée, un cabanon porte une plaque. Écrire
« aucun texte » ne les enlève pas — le modèle écrit du charabia à la place.
Chaque prompt ci-dessous sort donc l'inscription du champ : la liasse du
connaissement est vue **par la tranche**, à plat sur un hayon, la moitié
écrite retournée dessous ; les boîtes de l'inventaire portent des **numéros
au ruban de couleur** et non des mots ; le flanc du camion est coupé par le
mur de la ruelle ; la plaque du cabanon est hors cadre.

**Aucune personne dans aucune des seize images.** Elles montrent toutes des
lieux, des objets et des dommages, jamais une scène de conversation — et la
règle des mains ne se pose donc pas. Là où le journal de l'activité 119
recommande de **dire qui elles sont** dès qu'une image porte plus d'une
personne, la question ne se pose pas ici : il n'y en a aucune, et c'est ce
que les énoncés demandent.

Le contrôle avant livraison :

    node build/contexte_images.js module-n8-emmenagement

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix — Google direct, puis fal.ai, puis
WaveSpeed —, rend le nom de celle qui a servi et inscrit chaque tentative au
registre `~/Claude/generations/journal_appels.py`.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu : ce fichier
vit dans `build/contenu/<slug>/`, donc trois niveaux sous la racine — sans
quoi il cesserait de fonctionner dans un worktree.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n8-emmenagement/gen_images.py
  python3 build/contenu/module-n8-emmenagement/gen_images.py rampe-tordue
  python3 build/contenu/module-n8-emmenagement/gen_images.py vocab/inventaire
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n8-emmenagement'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX1 = "Je découvre · Exercice 4 — Ce que le camion a laissé derrière lui"
P_EX2 = "Défi 1 · Exercice 6 — Un sinistre, une protection"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : Trois-Rivières, un quartier de triplex de brique rouge
# des années trente, escaliers extérieurs en colimaçon, ruelles étroites.
# « Appartement moderne » sortirait générique américain : c'est exactement
# ce qu'on évite. La lumière est celle d'une journée de pluie de fin d'été
# pour les six premières — c'est le jour du déménagement — et d'un hiver
# ordinaire pour celles du défi 1 qui le demandent.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle, faible "
         "profondeur de champ. Trois-Rivières, Québec : triplex et duplex de "
         "brique rouge des années trente, escaliers extérieurs en colimaçon "
         "à limon d'acier peint, balcons de bois à garde-corps tourné, "
         "fenêtres à guillotine, ruelles étroites asphaltées, plinthes "
         "électriques, planchers de bois franc anciens, murs de plâtre peints "
         "en teintes sourdes. Palette sobre et un peu délavée, matériaux usés "
         "par l'hiver. Aucune personne dans le cadre, aucun visage, aucune "
         "main.")

# La négation seule ne tient pas devant un objet qui porte des inscriptions :
# elle sert de filet, pas de parade. La parade est dans chaque prompt, et
# c'est le cadrage.
SANS_MOTS = (" Strictly no letters, no words, no digits and no readable "
             "characters anywhere in the image: every line of text, "
             "including any form, invoice, checklist, shipping label, "
             "marker writing on a cardboard box, truck livery, street sign, "
             "civic number, appliance nameplate or warning placard, must "
             "fall outside the frame, be turned face down, or be an abstract "
             "grey stroke well out of focus. Aucun mot d'anglais nulle part, "
             "aucun nom d'entreprise, aucune enseigne lisible, aucun logo.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── prImg · les six traces du déménagement ────────────────────────────
 # « La rampe d'un escalier extérieur en colimaçon, tordue vers l'intérieur à
 #   hauteur du deuxième palier. »
 ('rampe-tordue', 'images', P_EX1, STYLE + " Gros plan moyen sur la **main "
  "courante d'acier d'un escalier extérieur en colimaçon** de triplex, prise "
  "d'en bas et de trois quarts : à hauteur du deuxième palier, le tube de la "
  "rampe est **visiblement plié vers l'intérieur sur environ un mètre**, la "
  "peinture noire craquelée et écaillée à l'endroit du choc, un barreau voisin "
  "déformé et son point de soudure tiré. Le reste de la rampe, au-dessus et "
  "au-dessous, est parfaitement droit — la déformation est le sujet de "
  "l'image et doit sauter aux yeux. Derrière, le mur de brique rouge et une "
  "fenêtre. Ciel gris de pluie, marches mouillées." + SANS_MOTS),
 # « Deux boîtes de carton affaissées et gonflées d'eau, posées sur les
 #   planches mouillées d'un balcon. »
 ('boites-mouillees', 'images', P_EX1, STYLE + " Deux boîtes de déménagement "
  "en carton brun posées sur les **planches de bois gris et détrempées** d'un "
  "balcon arrière de triplex, vues de trois quarts et d'assez près : le carton "
  "est **gonflé, gondolé et foncé par l'eau**, les coins sont ramollis, le fond "
  "de l'une s'est ouvert et un angle s'affaisse vers le plancher. Des flaques "
  "autour, des gouttes qui tombent encore du garde-corps de bois. Le carton "
  "est **entièrement vierge** : aucune écriture au marqueur, aucune étiquette, "
  "aucun ruban imprimé. Lumière grise d'après-averse." + SANS_MOTS),
 # « Un vaisselier de bois foncé couché sur une couverture grise, une longue
 #   fente le long du panneau de côté. »
 # Refaite le 23 août 2026. La première version rendait le meuble **debout**
 # sur la couverture, alors que l'énoncé le dit **couché**. Le quatrième
 # défaut sous la forme que l'activité 119 a nommée : le sujet y est, la
 # position ne l'est pas. Le prompt refait décrit **la vue** (en plongée,
 # depuis le dessus) plutôt que la posture — « couché » se laisse ignorer,
 # un point de vue non.
 ('vaisselier-fendu', 'images', P_EX1, STYLE + " **Vue en plongée, prise "
  "debout au-dessus du meuble**, sur un **vaisselier ancien en bois foncé "
  "renversé à l'horizontale, à plat sur le plancher**, entièrement posé sur "
  "une **couverture de déménagement grise matelassée** dans un salon vide au "
  "plancher de bois franc. Le meuble est **couché sur le dos, ses deux portes "
  "tournées vers le ciel** et fermées ; **aucune partie n'est debout**, sa "
  "plus grande dimension est allongée horizontalement à travers l'image. Une "
  "**longue fente nette court sur toute la longueur du panneau de côté**, "
  "maintenant tourné vers l'objectif, le bois légèrement soulevé de part et "
  "d'autre du trait et une écharde claire au milieu du bois sombre : c'est le "
  "sujet de l'image. Sangles de déménagement enroulées sur le plancher à "
  "côté. Lumière de fenêtre sans rideau." + SANS_MOTS),
 # « Une remorque de déménagement blanche reculée dans une ruelle étroite,
 #   entre deux murs de brique rouge. »
 ('camion-ruelle', 'images', P_EX1, STYLE + " Une **remorque de déménagement "
  "blanche** vue **de l'arrière, dans l'axe**, reculée dans une **ruelle "
  "étroite** entre deux murs de brique rouge qui la serrent de très près des "
  "deux côtés. Ses portes arrière sont grandes ouvertes et sa rampe d'accès "
  "est descendue sur l'asphalte mouillé. On ne voit **que la face arrière et "
  "les portes** : les deux flancs sont entièrement masqués par les murs de la "
  "ruelle, donc aucune livrée, aucun nom d'entreprise n'entre dans le cadre. "
  "Escaliers extérieurs en colimaçon sur le mur de gauche, fils électriques "
  "en travers du ciel gris. Aucune personne." + SANS_MOTS),
 # « Un salon entièrement vide où il ne reste qu'une pile de chaises au milieu
 #   du plancher. »
 # L'énoncé disait d'abord « quatre chaises empilées ». Deux tirages ont rendu
 # une pile de deux, puis de trois : le modèle ne compte pas, et le nombre
 # n'était de toute façon pas vérifiable dans une vignette de 223 px. C'est
 # l'énoncé qui a cédé, parce que le nombre n'était pas ce qui distinguait
 # cette photo des cinq autres — « entièrement vide » l'est.
 ('salon-vide', 'images', P_EX1, STYLE + " Un **salon entièrement vide** de "
  "logement ancien, vu depuis l'embrasure de la porte : plancher de bois franc "
  "rayé et marqué, murs de plâtre pâle où l'on devine les rectangles plus "
  "clairs laissés par des cadres décrochés, plinthes de bois peintes, deux "
  "grandes fenêtres à guillotine sans rideau. Au **milieu exact du plancher**, "
  "**une pile haute de quatre chaises de bois identiques emboîtées les unes "
  "sur les autres**, dont on distingue nettement **les quatre sièges étagés "
  "et les quatre dossiers décalés**, la pile montant presque à hauteur de "
  "fenêtre ; et rien d'autre dans la pièce — aucune boîte, aucun meuble, "
  "aucun objet. La pièce paraît plus grande qu'elle n'est. Lumière du jour "
  "grise et égale." + SANS_MOTS),
 # « Un plancher de bois franc gondolé et soulevé le long d'une plinthe
 #   électrique. »
 ('plancher-gondole', 'images', P_EX1, STYLE + " Cadrage rapproché et rasant "
  "sur la **jonction entre un plancher de bois franc et une plinthe "
  "électrique** de logement québécois : les lames de bois sont **gondolées et "
  "soulevées** sur une trentaine de centimètres le long du mur, leurs bords "
  "relevés et écartés les uns des autres, le vernis blanchi et cloqué par "
  "l'humidité. Une auréole plus foncée s'étend sur le bois vers le centre de "
  "la pièce. La plinthe électrique est vue de biais et ses grilles sont "
  "poussiéreuses ; sa plaque signalétique est hors cadre. Lumière latérale "
  "rasante qui accuse le relief." + SANS_MOTS),

 # ── t1img · six sinistres, et la protection qui les vise ──────────────
 # « Le tapis d'un sous-sol fini, trempé sur deux mètres tout autour d'un
 #   drain de plancher. »
 ('soussol-trempe', 'images', P_EX2, STYLE + " Un **sous-sol fini** de maison "
  "québécoise, vu de la dernière marche de l'escalier : moquette rase de "
  "couleur beige, murs de gypse peints, plafond bas à luminaires encastrés. "
  "Autour d'un **drain de plancher rond en fonte**, au centre de l'image, la "
  "moquette est **visiblement trempée et foncée sur environ deux mètres de "
  "rayon**, la limite de l'auréole nettement dessinée, et une mince pellicule "
  "d'eau reflète la lumière tout près du drain. Un divan et une table basse "
  "sont poussés en périphérie, leurs pieds dans l'eau. Aucune personne." + SANS_MOTS),
 # « Le cadre d'une porte d'entrée fendu à hauteur de la serrure, le bois
 #   éclaté vers l'intérieur. »
 ('porte-forcee', 'images', P_EX2, STYLE + " Cadrage rapproché sur le **cadre "
  "d'une porte d'entrée de logement**, à **hauteur de serrure**, vu de "
  "l'intérieur : le montant de bois peint est **fendu et éclaté vers "
  "l'intérieur**, des échardes claires hérissées autour de la gâche métallique "
  "à demi arrachée, deux vis pendantes, de la peinture tombée en écailles sur "
  "le plancher juste en dessous. La porte est entrouverte et l'on aperçoit la "
  "lumière du palier. Aucune plaque, aucun numéro civique, aucun autocollant "
  "dans le cadre. Aucune personne, aucune main." + SANS_MOTS),
 # « Le plafond d'une salle de bain marqué d'une large auréole brune, la
 #   peinture cloquée au centre. »
 ('plafond-aureole', 'images', P_EX2, STYLE + " Vue en contre-plongée du "
  "**plafond d'une petite salle de bain** de logement ancien : une **large "
  "auréole brune irrégulière** s'étale sur le plâtre blanc, ses bords plus "
  "foncés que son centre, et **la peinture est cloquée et écaillée au milieu**, "
  "un morceau prêt à tomber. Le coin supérieur du carrelage mural et le haut "
  "d'un cadre de porte entrent dans le bas du cadre. Éclairage d'un plafonnier "
  "simple, un peu jaune. Aucun objet portant d'inscription, aucune personne." + SANS_MOTS),
 # « Un balcon de bois dont deux planches se sont défoncées, sous une mince
 #   couche de neige. »
 ('balcon-defonce', 'images', P_EX2, STYLE + " Un **balcon arrière de bois** de "
  "triplex, vu d'en haut et de trois quarts, sous une **mince couche de neige "
  "fraîche** : **deux planches du plancher se sont défoncées** côte à côte, "
  "cassées vers le bas, et l'on voit par le trou la structure de solives et le "
  "sol de la cour en dessous. Le bois autour de la cassure est gris, fendillé "
  "et pourri par endroits. Garde-corps de bois tourné, escalier en colimaçon "
  "au fond, cour enneigée. Hiver, ciel blanc. Aucune personne." + SANS_MOTS),
 # « Un cabanon de tôle au fond d'une cour, la porte arrachée d'un gond et
 #   pendante. »
 ('cabanon-arrache', 'images', P_EX2, STYLE + " Un petit **cabanon de tôle "
  "ondulée** beige, au fond d'une cour arrière de quartier ouvrier, vu de "
  "face à quelques mètres : **une de ses deux portes est arrachée de son gond "
  "supérieur et pend de travers**, le coin inférieur posé sur le gravier, le "
  "métal tordu autour de la charnière. L'intérieur sombre se devine par "
  "l'ouverture. Herbe haute et jaunie autour, clôture de mailles derrière, "
  "hangar de brique du voisin. La plaque du fabricant et toute étiquette sont "
  "hors du cadre. Lumière de fin d'après-midi. Aucune personne." + SANS_MOTS),
 # « Le tuyau de renvoi sous un évier de cuisine, un seau posé dessous et une
 #   flaque tout autour. »
 ('tuyau-evier', 'images', P_EX2, STYLE + " Vue à hauteur du sol dans le "
  "**caisson ouvert sous un évier de cuisine** de logement ancien : le "
  "**tuyau de renvoi en plastique blanc** et son siphon en col de cygne "
  "occupent le centre du cadre, une **goutte suspendue** au raccord, et un "
  "**seau de plastique gris posé juste en dessous** recueille l'eau. Une "
  "**flaque s'est étalée tout autour du seau** sur le fond du caisson, dont le "
  "panneau d'aggloméré est gonflé et foncé par l'humidité. Les produits "
  "d'entretien ont été sortis et sont hors du cadre : rien ne porte "
  "d'étiquette. Lumière crue d'une lampe de poche posée à côté." + SANS_MOTS),

 # ── Les quatre photos du banc de vocabulaire ──────────────────────────
 # « L'événement qui cause le dommage et qui déclenche le contrat. »
 ('sinistre', 'vocab', P_VOC, STYLE + " Un **salon de logement ancien dont une "
  "partie du plafond de plâtre s'est effondrée** : un pan de plâtre est tombé "
  "sur le plancher de bois franc en gros morceaux blancs et en poussière, on "
  "voit au-dessus les **lattes et les solives mises à nu**, noircies par "
  "l'humidité, et l'eau a coulé le long du mur en une longue traînée. Un "
  "fauteuil poussé en hâte contre le mur du fond est couvert de débris. La "
  "pièce est autrement intacte, ce qui rend le dégât plus frappant. Lumière du "
  "jour par une fenêtre à guillotine. Aucune personne." + SANS_MOTS),
 # « Le papier que le transporteur fait signer et qui dit ce qu'il prend en
 #   charge. »
 # C'est l'image la plus exposée du module : un connaissement EST un
 # formulaire. On ne montre donc pas ce qu'il dit, on montre l'objet — une
 # liasse vue par la tranche, à plat, la face écrite retournée dessous.
 ('connaissement', 'vocab', P_VOC, STYLE + " Cadrage rapproché et **très "
  "rasant, à hauteur de la table**, sur une **liasse de trois feuilles de "
  "papier autocopiant** — une blanche, une jaune, une rose — posée **à plat, "
  "face écrite retournée contre le bois**, sur le hayon abaissé d'une remorque "
  "de déménagement. On ne voit d'elle que **la tranche et les bords colorés** "
  "des trois feuillets décalés, et le **dos parfaitement vierge** de celui du "
  "dessus. Une planchette à pince de plastique noir et un stylo à bille sont "
  "posés à côté. Arrière-plan : le plancher de contreplaqué de la remorque, "
  "flou. Aucune écriture, aucune case, aucune ligne imprimée visible nulle "
  "part. Aucune main." + SANS_MOTS),
 # « La liste écrite de tout ce qui est transporté ou de tout ce qui a été
 #   abîmé. »
 # Une liste est du texte. On montre donc ce que l'inventaire compte : des
 # boîtes numérotées — et les numéros sont des BANDES DE RUBAN DE COULEUR,
 # pas des chiffres.
 ('inventaire', 'vocab', P_VOC, STYLE + " Une **pile de huit à dix boîtes de "
  "déménagement en carton brun**, empilées sur trois colonnes contre le mur "
  "d'un salon vide au plancher de bois franc, vues de face à deux mètres. "
  "Chaque boîte porte, sur sa face avant, **une ou plusieurs bandes de ruban "
  "adhésif de couleur** — rouge, bleu, jaune, vert — collées côte à côte comme "
  "un code : c'est ainsi qu'elles sont comptées. **Aucun mot, aucun chiffre "
  "n'est écrit sur le carton**, ni au marqueur ni sur une étiquette. Une "
  "couverture de déménagement grise est pliée au sol devant la pile. Lumière "
  "de fenêtre." + SANS_MOTS),
 # « Le dommage causé par l'eau qui entre là où elle ne devrait pas. »
 ('degat-eau', 'vocab', P_VOC, STYLE + " Cadrage moyen sur un **mur de plâtre "
  "de logement ancien, marqué par l'eau** : une **grande auréole brune** part "
  "du plafond et descend en s'élargissant sur près d'un mètre, la peinture "
  "**cloque et se décolle en larges plaques** au bas de la coulée, et le "
  "plâtre à nu est plus foncé dessous. Au sol, le long de la plinthe de bois, "
  "les lames du plancher de bois franc sont **gondolées et écartées**. Un "
  "linge posé au pied du mur. Éclairage naturel latéral qui accuse le relief "
  "des cloques. Aucun objet portant d'inscription, aucune personne." + SANS_MOTS),
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
