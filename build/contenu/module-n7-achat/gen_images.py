#!/usr/bin/env python3
"""Les 18 images de module-n7-achat (niveau 7, activité 113).

Deux destinations :
  · `images/` — les dix photos des deux exercices d'association (`prImg`,
    cinq lieux du dossier ; `t1img`, cinq choses remarquées), réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les huit photos du banc de vocabulaire, réduites à 800 px
    qualité 82. Huit des seize cartes n'ont **pas** d'image : « l'odomètre »,
    « les frais de crédit », « l'obligation totale », « un cognement »,
    « la garantie de bon fonctionnement », « une garantie prolongée »,
    « une réclamation » et « une mise en demeure » sont soit des
    abstractions, soit des documents — et un document, c'est du texte.

**Les quatre règles de prompt du 22 août 2026 sont appliquées ici**
(`CLAUDE.md`, « Les images d'un module ») :

1. aucun texte lisible ;
2. pas de mains ni de visages en gros plan ;
3. un décor québécois nommé ;
4. **l'image montre ce que dit son énoncé** — chaque prompt d'exercice est
   écrit à partir de la phrase exacte de la rangée `ok`, recopiée en
   commentaire au-dessus de lui.

**Ce module est celui du dépôt où les inscriptions sont les plus
tentantes**, et c'est pour cela que la parade retenue n'est pas la négation
mais le **cadrage**. La leçon des quatre modules du 23 août 2026 : devant un
objet dont le modèle *sait* qu'il porte des lettres — étiquette de prix,
plaque d'immatriculation, fenêtre des rapports d'un levier de vitesse,
tableau de bord, écran d'appareil de diagnostic, enseigne de concessionnaire
—, écrire « aucun texte » ne suffit pas. Il faut **sortir l'inscription du
cadre**. On le voit dans les prompts ci-dessous : la plaque est coupée par le
bord de l'image, la fenêtre des rapports est masquée par la console, les
cadrans du tableau de bord sont hors champ, les pare-brise de la rangée
d'autos sont au-dessus du cadre. Même chose pour les mains : plutôt que « pas
de mains », on impose le poste de l'appareil.

Le contrôle avant livraison :

    node build/contexte_images.js module-n7-achat

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix — Google direct, puis fal.ai, puis
WaveSpeed —, rend le nom de celle qui a servi et inscrit chaque tentative au
registre `~/Claude/generations/journal_appels.py`.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu : ce fichier
vit dans `build/contenu/<slug>/`, donc trois niveaux sous la racine — sans
quoi il cesserait de fonctionner dans un worktree.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n7-achat/gen_images.py
  python3 build/contenu/module-n7-achat/gen_images.py levier-de-vitesse
  python3 build/contenu/module-n7-achat/gen_images.py vocab/transmission
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n7-achat'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX1 = "Je découvre · Exercice 4 — Les lieux du dossier d'Ernestine"
P_EX2 = "Défi 1 · Exercice 2 — Ce qu'Ernestine a remarqué"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : Victoriaville au printemps, des lieux ordinaires du
# Centre-du-Québec. Rien de publicitaire, rien de « moderne » : le générique
# américain vient de là.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle de "
         "printemps, faible profondeur de champ. Ville moyenne du "
         "Centre-du-Québec : bungalows de brique et de déclin d'aluminium, "
         "entrées d'asphalte fissurées, poteaux de bois et fils aériens, "
         "restes de gravier d'hiver au bord du trottoir, garages de quartier "
         "en blocs de béton peints. Palette sobre, mobilier et outillage "
         "ordinaires, un peu usés. Aucune personne identifiable, aucun "
         "visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire au Québec "
        "avec une ou deux personnes vues de loin, de dos ou de trois quarts "
        "arrière, jamais en gros plan et jamais les mains seules au premier "
        "plan. Lumière naturelle douce, faible profondeur de champ. Aucun "
        "visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

# La négation seule ne tient pas devant un objet qui porte des inscriptions :
# elle sert de filet, pas de parade. La parade est dans chaque prompt, et
# c'est le cadrage.
SANS_MOTS = (" Strictly no letters, no words, no digits and no readable "
             "characters anywhere in the image: every line of text, "
             "including any headline, label, sign, price tag, licence plate, "
             "screen interface, dial or gauge marking, must fall outside the "
             "frame or be an abstract grey stroke. Aucun mot d'anglais nulle "
             "part, aucun nom d'organisme, aucune enseigne lisible, aucun "
             "logo de constructeur.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── prImg · les cinq lieux du dossier ─────────────────────────────────
 # « Un petit bureau vitré au fond d'une salle de montre, une table et deux chaises. »
 ('bureau-de-vente', 'images', P_EX1, STYLE + " Un petit bureau fermé par des "
  "cloisons vitrées, au fond d'une salle de montre de concessionnaire de "
  "quartier : une table de mélamine claire, deux chaises rembourrées vides "
  "face à face, une chemise cartonnée fermée posée à plat. À travers la vitre, "
  "on devine le plancher de béton poli de la salle et l'arrière d'une "
  "carrosserie. Le haut de l'image est coupé au-dessus des cloisons : aucun "
  "mur d'enseigne, aucun panneau suspendu n'entre dans le cadre. Aucune "
  "personne." + SANS_MOTS),
 # « Une berline grise stationnée dans une entrée d'asphalte, devant un bungalow. »
 ('berline-dans-l-entree', 'images', P_EX1, STYLE + " Une berline grise à "
  "quatre portes, propre et sans particularité, stationnée de trois quarts "
  "avant dans une entrée d'asphalte devant un bungalow de brique beige des "
  "années soixante-dix, avec une haie basse et un érable encore nu. Cadrage "
  "légèrement en hauteur, pris depuis le trottoir : le pare-chocs avant et la "
  "plaque d'immatriculation sont coupés par le bord inférieur de l'image et "
  "n'apparaissent pas. Aucun écusson de constructeur visible sur la calandre. "
  "Aucune personne." + SANS_MOTS),
 # « Un atelier de garage où une auto est levée sur un pont élévateur. »
 ('atelier-pont-elevateur', 'images', P_EX1, STYLE + " L'intérieur d'un atelier "
  "de garage indépendant en blocs de béton peints en blanc : une auto grise "
  "levée à hauteur de poitrine sur un pont élévateur à deux colonnes, un "
  "établi encombré d'outils le long du mur, un tuyau d'air enroulé au plafond, "
  "un bidon d'huile vide au sol. Les murs sont nus : aucune affiche, aucun "
  "calendrier, aucun panneau. Éclairage de tubes fluorescents. Aucune "
  "personne." + SANS_MOTS),
 # « Un comptoir de service à la clientèle, haut, avec deux tabourets vides devant. »
 ('comptoir-de-service', 'images', P_EX1, STYLE + " Un comptoir de service à la "
  "clientèle en stratifié gris, haut, avec un dessus de mélamine plus foncé, "
  "deux tabourets rembourrés vides poussés devant, un petit présentoir "
  "métallique vide et un pot à crayons. Derrière, une cloison basse et un "
  "classeur à tiroirs. Cadrage bas, à hauteur du comptoir : le mur du fond et "
  "tout ce qui pourrait y être accroché sont hors champ, coupés par le bord "
  "supérieur. Aucune personne." + SANS_MOTS),
 # « Une table de cuisine le soir, un ordinateur portable ouvert et une pile de papiers. »
 ('table-de-cuisine-le-soir', 'images', P_EX1, STYLE + " Une table de cuisine "
  "de bungalow le soir, éclairée par une seule lampe suspendue : un ordinateur "
  "portable ouvert, tourné de trois quarts de sorte que l'écran est vu presque "
  "de côté et paraît uniformément sombre, une pile de feuilles à côté et une "
  "tasse. Les feuilles sont nettement hors du plan de netteté, entièrement "
  "floues, aucun caractère n'y est discernable. Fenêtre noire derrière. Aucune "
  "personne, aucune main." + SANS_MOTS),

 # ── t1img · les cinq choses remarquées ────────────────────────────────
 # « Une flaque rouge sur l'asphalte, sous l'avant d'une auto stationnée. »
 ('flaque-rouge', 'images', P_EX2, STYLE + " Vue en plongée sur l'asphalte "
  "gris et fissuré d'une entrée résidentielle : une flaque de liquide rouge "
  "vif de la taille d'une main s'est formée sous l'avant d'une auto "
  "stationnée, dont on ne voit que le bas du pare-chocs et une roue avant, en "
  "haut du cadre. Lumière grise du matin, quelques grains de gravier autour. "
  "Aucune personne." + SANS_MOTS),
 # « Un pare-brise couvert de givre, tôt le matin, dans une entrée encore sombre. »
 ('pare-brise-givre', 'images', P_EX2, STYLE + " Un pare-brise entièrement "
  "couvert de givre blanc, vu de l'extérieur et de trois quarts, tôt le matin "
  "dans une entrée résidentielle encore bleutée. On devine à peine l'intérieur "
  "de l'habitacle derrière le givre. Le capot occupe le bas du cadre ; aucune "
  "vignette, aucun autocollant, aucune inscription sur la vitre. Aucune "
  "personne." + SANS_MOTS),
 # « Une petite montée de rue résidentielle, vue depuis l'intérieur d'une auto. »
 ('petite-montee', 'images', P_EX2, STYLE + " Vue depuis le siège du conducteur "
  "à travers un pare-brise propre : une rue résidentielle qui monte en pente "
  "douce entre deux rangées de bungalows, trottoirs mouillés, arbres nus, ciel "
  "clair de printemps. On voit le haut du tableau de bord en bas du cadre, "
  "sans aucun cadran ni aucun bouton visible. Aucun panneau de signalisation, "
  "aucune affiche, aucune personne dans la rue." + SANS_MOTS),
 # « Un levier de vitesse automatique, vu de trois quarts, entre les deux sièges. »
 ('levier-de-vitesse', 'images', P_EX2, STYLE + " Cadrage serré, de trois "
  "quarts arrière, sur le levier de vitesse d'une transmission automatique "
  "d'auto ordinaire : le pommeau de cuir noir usé et le haut de la tige, entre "
  "les deux sièges avant, avec la console de plastique gris autour. La "
  "plaquette des rapports, sur le côté de la console, est entièrement masquée "
  "par l'angle de prise de vue et n'apparaît pas dans l'image. Lumière "
  "naturelle par la vitre latérale. Aucune main, aucune personne." + SANS_MOTS),
 # « Le dessous d'une auto vu depuis la fosse d'un atelier de mécanique. »
 ('dessous-de-l-auto', 'images', P_EX2, STYLE + " Vue prise du bas vers le "
  "haut, depuis la fosse d'un atelier de mécanique, sur le dessous d'une auto : "
  "le carter, la traverse, les tuyaux d'échappement, une trace sombre "
  "d'écoulement le long d'une pièce, la rouille de surface habituelle des "
  "véhicules du Québec. Une lampe de travail éclaire de côté. Aucune "
  "inscription moulée lisible sur les pièces, aucune personne." + SANS_MOTS),

 # ── Les huit photos du banc de vocabulaire ────────────────────────────
 # « Un véhicule qui a déjà appartenu à quelqu'un et qu'on achète en deuxième
 #   ou en troisième main. »
 ('auto-d-occasion', 'vocab', P_VOC, STYLE + " Une rangée d'autos d'occasion "
  "propres, de couleurs sobres, stationnées serrées en épi sur un terrain "
  "d'asphalte, vues de trois quarts arrière et à hauteur de hanche, un matin "
  "de printemps. Le cadrage s'arrête à la hauteur des vitres arrière : les "
  "pare-brise, le toit et tout ce qui pourrait y être posé sont hors champ, "
  "au-dessus du bord supérieur de l'image. Aucun fanion, aucune banderole, "
  "aucune affichette, aucune plaque d'immatriculation visible, aucun mât. "
  "Aucune personne." + SANS_MOTS),
 # « La partie mécanique qui transmet la force du moteur aux roues et qui
 #   change les rapports. »
 ('transmission', 'vocab', P_VOC, STYLE + " Une boîte de transmission "
  "automatique d'automobile déposée sur un établi d'atelier, vue de trois "
  "quarts : carter d'aluminium terne, boulons apparents, un joint neuf posé à "
  "côté, un chiffon gras et une clé à douille. Aucune inscription moulée ni "
  "gravée lisible sur le carter, aucune étiquette collée. Éclairage de tube "
  "fluorescent. Aucune personne, aucune main." + SANS_MOTS),
 # « La petite lampe du tableau de bord qui s'allume pour signaler un problème
 #   au conducteur. »
 ('temoin-lumineux', 'vocab', P_VOC, STYLE + " Cadrage très serré sur une "
  "petite portion de tableau de bord d'auto dans la pénombre : un seul témoin "
  "ambre allumé, un pictogramme simple d'engrenage stylisé, sa lumière "
  "diffusant légèrement sur le plastique gris autour. Les cadrans, les "
  "chiffres et tous les autres témoins sont hors champ, coupés par les bords "
  "de l'image. Aucune personne, aucune main." + SANS_MOTS),
 # « Le résultat de l'examen par lequel un spécialiste établit d'où vient un
 #   problème. »
 ('diagnostic', 'vocab', P_VOC, STYLE + " Vue rapprochée, depuis le seuil de la "
  "portière ouverte du côté conducteur, sur le connecteur de diagnostic situé "
  "sous le tableau de bord d'une auto : un câble noir y est branché et descend "
  "hors du cadre vers la droite. L'appareil au bout du câble n'apparaît pas "
  "dans l'image, et aucun écran n'est visible. Le volant est coupé par le bord "
  "supérieur. Aucune personne, aucune main." + SANS_MOTS),
 # « La détérioration qu'un objet subit forcément à l'usage, et qu'aucune
 #   garantie ne répare. »
 ('usure-normale', 'vocab', P_VOC, STYLE + " Deux disques de frein d'auto posés "
  "côte à côte à plat sur un établi d'atelier : celui de gauche est très usé, "
  "rainuré, rouillé sur le pourtour ; celui de droite est neuf, lisse et clair. "
  "Un vernier posé à côté. Éclairage rasant qui fait ressortir les rainures. "
  "Aucune étiquette, aucune inscription gravée lisible, aucune personne." + SANS_MOTS),
 # « Un défaut grave qu'un acheteur attentif ne pouvait pas voir au moment de
 #   l'achat. »
 ('vice-cache', 'vocab', P_VOC, STYLE + " Le plancher du coffre d'une auto, "
  "vu de haut, coffre ouvert : le tapis de coffre a été soulevé et replié sur "
  "le côté, découvrant une plaque de tôle percée de rouille brune sur toute "
  "une bande, avec des écailles de peinture. La roue de secours apparaît au "
  "bord du cadre. Lumière du jour. Aucune personne, aucune main." + SANS_MOTS),
 # « Un papier qui prouve ce qu'on avance : une facture, un rapport, un
 #   contrat. »
 ('piece-justificative', 'vocab', P_VOC, STYLE + " Une chemise cartonnée beige "
  "ouverte sur une table de cuisine, contenant une pile de feuilles agrafées "
  "légèrement décalées les unes des autres, avec un trombone et un surligneur "
  "posés dessus. La mise au point est faite sur le trombone et sur le bord de "
  "la chemise ; les feuilles sont franchement hors du plan de netteté, floues, "
  "et aucun caractère n'y est discernable. Aucune personne, aucune main." + SANS_MOTS),
 # « Le tribunal où l'on réclame soi-même, sans avocat, une somme de quinze
 #   mille dollars ou moins. »
 ('petites-creances', 'vocab', P_VOC, STYLE + " Une petite salle d'audience "
  "vide de palais de justice de région, vue depuis le fond : quatre rangées de "
  "bancs de bois clair, une allée centrale, deux tables face à une estrade "
  "basse, boiseries sombres et lumière de fenêtres hautes sur la gauche. Le "
  "mur du fond derrière l'estrade est nu et l'image est coupée juste "
  "au-dessus : aucun écusson, aucun drapeau, aucune inscription n'entre dans "
  "le cadre. Aucune personne." + SANS_MOTS),
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
