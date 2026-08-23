#!/usr/bin/env python3
"""Les 16 images de module-n8-recherche (niveau 8, activité 119).

Deux destinations :
  · `images/` — les onze photos des deux exercices d'association (`prImg`,
    six lieux et moments du processus ; `t2img`, cinq choses que le profil
    d'entreprise décrit), réduites à 1200 px qualité 85 ;
  · `vocab/`  — les cinq photos du banc de vocabulaire, réduites à 800 px
    qualité 82. **Onze des seize cartes n'ont pas d'image**, et c'est un
    choix : le lexique d'un processus de sélection est abstrait — une
    présélection, un échelon, une contrepartie, un motif de discrimination,
    le service continu. Leur donner une photo aurait mis derrière chaque
    carte une vue générique de salle de réunion, c'est-à-dire le thème du
    module à la place de ce que dit la carte. C'est le quatrième défaut de
    la relecture du 22 août 2026, et `module-n7-banque` avait tranché dans
    le même sens la veille.

**Les quatre règles de prompt sont appliquées ici** (`CLAUDE.md`, « Les
images d'un module ») :

1. aucun texte lisible ;
2. pas de mains ni de visages en gros plan ;
3. un décor québécois nommé — ici Sherbrooke et l'Estrie ;
4. **l'image montre ce que dit son énoncé** — chaque prompt est écrit à
   partir de la phrase exacte de la rangée `ok`, recopiée en commentaire
   au-dessus de lui.

**La parade au texte parasite est le cadrage, jamais la négation.** Ce
module est plein d'objets qui *portent* des inscriptions : les feuilles d'un
examen écrit, les chemises d'un comité, la livrée d'un camion de livraison,
les étiquettes de casiers d'un vestiaire, l'écran d'une machine à l'arrêt,
la signalisation de sécurité d'une passerelle. Écrire « aucun texte » ne les
enlève pas — le modèle écrit du charabia à la place. Chaque prompt ci-dessous
sort donc l'inscription du champ : les feuilles sont franchement hors du plan
de netteté, la face du camion est coupée par le bord, les casiers sont vus
de biais et leurs porte-étiquettes sont vides, l'écran de la machine est
éteint et tourné, la signalisation est au-dessus du cadre.

**Les personnes sont vues de loin et de dos.** Deux images en comportent —
le contremaître et l'entrevue de groupe — parce que le mot les exige ; elles
sont cadrées de trois quarts arrière, à distance, sans aucun visage.

Le contrôle avant livraison :

    node build/contexte_images.js module-n8-recherche

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix — Google direct, puis fal.ai, puis
WaveSpeed —, rend le nom de celle qui a servi et inscrit chaque tentative au
registre `~/Claude/generations/journal_appels.py`.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu : ce fichier
vit dans `build/contenu/<slug>/`, donc trois niveaux sous la racine — sans
quoi il cesserait de fonctionner dans un worktree.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n8-recherche/gen_images.py
  python3 build/contenu/module-n8-recherche/gen_images.py salle-examen
  python3 build/contenu/module-n8-recherche/gen_images.py vocab/contremaitre
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n8-recherche'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX1 = "Je découvre · Exercice 4 — Les lieux et les moments du processus"
P_EX2 = "Défi 2 · Exercice 6 — Ce que le profil décrit, en images"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : Sherbrooke et l'Estrie à la fin de l'hiver. Une usine de
# quartier plutôt qu'un site industriel neuf, des locaux ordinaires et un peu
# usés. « Bureau moderne et lumineux » sort générique américain : c'est
# exactement ce qu'on évite.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle de fin "
         "d'hiver, faible profondeur de champ. Sherbrooke et l'Estrie : "
         "bâtiments industriels de brique rouge et de tôle peinte, fenêtres "
         "à châssis d'aluminium, murs de blocs de béton peints en crème, "
         "planchers de béton scellé, escaliers extérieurs en acier "
         "galvanisé, restes de neige sale et de sel au bord de l'asphalte. "
         "Palette sobre, mobilier ordinaire et un peu usé. Aucune personne "
         "identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire dans une "
        "usine de Sherbrooke avec une ou deux personnes vues de loin, de dos "
        "ou de trois quarts arrière, jamais en gros plan et jamais les mains "
        "seules au premier plan. Lumière naturelle douce, faible profondeur "
        "de champ. Aucun visage reconnaissable, aucun texte, aucun logo, "
        "aucun filigrane.")

# La négation seule ne tient pas devant un objet qui porte des inscriptions :
# elle sert de filet, pas de parade. La parade est dans chaque prompt, et
# c'est le cadrage.
SANS_MOTS = (" Strictly no letters, no words, no digits and no readable "
             "characters anywhere in the image: every line of text, "
             "including any headline, label, sign, safety placard, locker "
             "nameplate, truck livery, control-panel screen or gauge "
             "marking, must fall outside the frame, be switched off, or be "
             "an abstract grey stroke. Aucun mot d'anglais nulle part, aucun "
             "nom d'entreprise, aucune enseigne lisible, aucun logo.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── prImg · les six lieux et moments du processus ─────────────────────
 # « Une longue table où quatre candidats écrivent, chacun devant une feuille
 #   et rien d'autre. »
 # Refaite le 23 août 2026. La première version rendait quatre hommes blancs
 # d'une cinquantaine d'années : l'image passait les quatre règles, mais elle
 # ne montrait aucune des personnes qui suivent ce module — une classe de
 # francisation est faite d'adultes venus d'ailleurs, et la candidate du
 # scénario est une femme arrivée d'Iran. Le prompt refait **impose la
 # composition du groupe** plutôt que de la laisser au modèle, qui retombe
 # sinon sur son défaut.
 ('salle-examen', 'images', P_EX1, PERS + " " + STYLE + " Une longue table "
  "rectangulaire de mélamine claire dans une salle de formation d'usine aux "
  "murs de blocs de béton crème. **Quatre** personnes y sont assises très "
  "espacées, vues de trois quarts arrière depuis le fond de la salle, penchées "
  "sur leur feuille, un crayon à la main. Le groupe est **mixte et d'origines "
  "diverses** : deux femmes et deux hommes, d'âges et de teints de peau "
  "différents, l'une portant un foulard sur les cheveux. Rien d'autre devant "
  "elles — aucun "
  "ordinateur, aucune bouteille, aucun sac. Les feuilles sont franchement hors "
  "du plan de netteté, entièrement floues, aucun caractère n'y est "
  "discernable. Le mur du fond est nu et l'image est coupée juste au-dessus du "
  "tableau : aucune affiche, aucun panneau n'entre dans le cadre. Lumière de "
  "tubes fluorescents et d'une fenêtre latérale." + SANS_MOTS),
 # « Le plancher d'une usine vu de la passerelle, trois lignes parallèles en
 #   marche. »
 ('plancher-usine', 'images', P_EX1, STYLE + " Vue en plongée depuis une "
  "passerelle métallique, sur le plancher de béton scellé d'une usine "
  "d'emballage : trois chaînes de conditionnement parallèles en marche, "
  "convoyeurs à rouleaux et carters de tôle bleue, des contenants de plastique "
  "clair qui avancent sur les courroies, des bacs empilés entre les lignes. Le "
  "regard porte loin dans la profondeur du bâtiment. Les murs et les colonnes "
  "sont nus, sans aucune affiche ni pancarte, et les écrans de commande des "
  "machines sont éteints et vus de côté. Aucune personne au premier "
  "plan." + SANS_MOTS),
 # « Le stationnement d'une usine à la fin d'un quart de soir, sous la neige et
 #   les lampadaires. »
 ('stationnement-soir', 'images', P_EX1, STYLE + " Un stationnement d'employés "
  "d'usine tard le soir, en hiver : une vingtaine d'autos ordinaires couvertes "
  "de quelques centimètres de neige fraîche, alignées sur l'asphalte, sous "
  "trois lampadaires dont la lumière orange traverse les flocons. Au fond, la "
  "silhouette basse d'un bâtiment de brique rouge dont quelques fenêtres sont "
  "encore éclairées. Ciel noir. Les plaques d'immatriculation sont coupées par "
  "l'angle ou couvertes de neige, et aucun panneau de stationnement n'entre "
  "dans le cadre. Aucune personne." + SANS_MOTS),
 # « Deux chaises d'un côté d'une table, une seule de l'autre, dans une petite
 #   salle de réunion. »
 ('table-comite', 'images', P_EX1, STYLE + " Une petite salle de réunion "
  "d'usine, vide, vue de l'entrée : une table de bois clair au centre, **deux** "
  "chaises de bureau rembourrées côte à côte d'un côté, **une seule** chaise "
  "isolée de l'autre côté, face à elles. Deux chemises cartonnées beiges "
  "**fermées** et un verre d'eau devant les deux chaises ; rien du tout devant "
  "la chaise isolée. Cloison vitrée à gauche, mur de blocs crème à droite, "
  "moquette grise usée. Le mur du fond est nu et coupé par le bord supérieur : "
  "aucun tableau, aucune affiche. Aucune personne." + SANS_MOTS),
 # « Deux tasses vides sur une table de café, près d'une vitrine donnant sur
 #   une rue enneigée. »
 ('cafe-wellington', 'images', P_EX1, STYLE + " Une petite table ronde de café "
  "de quartier, en bois foncé, contre une grande vitrine : **deux tasses de "
  "céramique vides** avec leur soucoupe, une cuillère posée à côté, une "
  "serviette de papier froissée. Derrière la vitre, une rue commerçante de "
  "Sherbrooke en fin d'après-midi d'hiver, trottoir déneigé, bancs de neige "
  "grise, façades de brique et lumière déclinante. La vitrine est propre et "
  "n'a aucune inscription peinte ni autocollant ; les enseignes d'en face sont "
  "hors champ, coupées par le bord supérieur. Aucune personne "
  "attablée." + SANS_MOTS),
 # « Des palettes de caisses de plastique alignées devant un quai de
 #   chargement. »
 ('palettes-quai', 'images', P_EX1, STYLE + " Une dizaine de palettes de bois "
  "chargées de caisses de plastique gris et bleu emboîtées, filmées de "
  "polythène transparent, alignées en deux rangées sur le béton d'un entrepôt, "
  "devant une porte de quai de chargement relevée par laquelle entre la "
  "lumière grise du dehors. Les caisses n'ont aucune étiquette, aucun "
  "autocollant, aucun code imprimé — le film plastique les recouvre. Le mur "
  "porte des marques de chocs et des traces de pneus. Aucune personne, aucun "
  "chariot élévateur." + SANS_MOTS),

 # ── t2img · ce que le profil d'entreprise décrit ──────────────────────
 # « Des contenants de plastique alimentaire vides, empilés par centaines à la
 #   sortie d'une machine. »
 ('contenants-plastique', 'images', P_EX2, STYLE + " Cadrage rapproché sur la "
  "sortie d'une machine de thermoformage : des centaines de contenants de "
  "plastique translucide pour aliments, ronds et peu profonds, emboîtés en "
  "longues colonnes serrées qui s'accumulent dans un bac de réception. Le "
  "plastique est parfaitement lisse et **complètement vierge** : aucun "
  "couvercle imprimé, aucune étiquette, aucun sigle moulé. Reflets de "
  "l'éclairage industriel sur les colonnes. Le carter de la machine occupe le "
  "haut du cadre, son panneau de commande est hors champ. Aucune "
  "personne." + SANS_MOTS),
 # « Un camion reculé contre un quai de chargement, la porte relevée, le quai
 #   désert. »
 # Refaite le 23 août 2026. La première version montrait la remorque garée
 # **au milieu de la cour**, à trois mètres du quai, ouverte face à
 # l'objectif : l'énoncé dit « reculé **contre** un quai », et l'accostage
 # était précisément ce qui manquait. Le quatrième défaut sous sa forme la
 # moins visible, celle du degré — le sujet y est, la relation entre les
 # objets n'y est pas. Le prompt refait décrit **le joint** entre la remorque
 # et le quai plutôt que la scène : le plancher de la boîte à la hauteur du
 # béton, le bourrelet d'étanchéité écrasé, aucun jour entre les deux.
 ('quai-chargement', 'images', P_EX2, STYLE + " Vue de l'intérieur d'un "
  "entrepôt, à hauteur d'homme, dans l'axe d'une porte de quai : la boîte d'un "
  "camion de livraison est **accostée contre le quai**, son plancher "
  "exactement au niveau du béton et **sans aucun jour entre les deux** ; les "
  "bourrelets d'étanchéité noirs de l'encadrement sont écrasés contre ses "
  "flancs. Sa **porte arrière est relevée** et l'on voit dans la profondeur de "
  "la remorque, vide et sombre, jusqu'au fond. On ne voit **rien de "
  "l'extérieur** : la remorque bouche entièrement l'ouverture. Le quai est "
  "**désert** — aucune palette, aucun chariot, personne. Aucun flanc de "
  "remorque n'est visible, donc aucune livrée ni inscription. Béton marqué de "
  "traces de pneus et de sel." + SANS_MOTS),
 # « Une chaîne de conditionnement immobile, avec des contenants restés en
 #   travers du convoyeur. »
 ('ligne-arretee', 'images', P_EX2, STYLE + " Une chaîne de conditionnement "
  "**à l'arrêt**, vue de trois quarts à hauteur de taille : le convoyeur à "
  "courroie est immobile, et une dizaine de contenants de plastique clair sont "
  "**renversés et coincés en travers** de la bande, l'un d'eux tombé au sol à "
  "côté. Une colonne lumineuse de signalisation à trois étages est allumée en "
  "ambre au-dessus de la machine. L'écran de commande, sur le côté du carter, "
  "est **éteint et noir**, vu de biais. Le reste de l'atelier est flou en "
  "arrière-plan. Aucune personne." + SANS_MOTS),
 # « Une passerelle métallique d'où l'on surveille trois lignes parallèles. »
 ('passerelle-usine', 'images', P_EX2, STYLE + " Une passerelle industrielle en "
  "caillebotis d'acier galvanisé, vue dans sa longueur depuis son extrémité : "
  "garde-corps jaune écaillé de chaque côté, plinthes de tôle, éclairage "
  "suspendu au-dessus. Elle traverse le bâtiment à quatre mètres du sol, et "
  "l'on aperçoit à travers le caillebotis, en bas et flou, les trois lignes de "
  "production. La passerelle est vide. Les panneaux de sécurité habituels des "
  "garde-corps sont hors champ, au-dessus du bord supérieur de l'image ; les "
  "montants sont nus. Aucune personne." + SANS_MOTS),
 # « Un vestiaire d'usine aux casiers fermés, à l'heure où le quart de jour est
 #   déjà parti. »
 ('vestiaire-vide', 'images', P_EX2, STYLE + " Un vestiaire d'employés d'usine, "
  "**désert**, vu en enfilade : deux rangées de casiers métalliques bleus "
  "**tous fermés**, un banc de bois clair au milieu de l'allée, un plancher de "
  "tuiles grises luisantes, une paire de bottes de travail oubliée sous le "
  "banc. Les casiers sont vus **en fuite, de biais**, et leurs porte-étiquettes "
  "sont vides — aucun nom, aucun numéro lisible. Un seul plafonnier allumé au "
  "fond, le reste dans la pénombre : le quart de jour est parti. Aucune "
  "personne." + SANS_MOTS),

 # ── Les cinq photos du banc de vocabulaire ────────────────────────────
 # « La personne qui dirige une équipe directement sur le plancher d'une
 #   usine. »
 ('contremaitre', 'vocab', P_VOC, PERS + " " + STYLE + " Une personne en "
  "dossard de sécurité orange et casque blanc, vue **de dos et de loin**, "
  "debout au milieu du plancher d'une usine d'emballage, une planchette à "
  "pince baissée le long du corps. Elle regarde vers une chaîne de production "
  "qui occupe l'arrière-plan, légèrement floue. Le dossard n'a **aucune "
  "inscription** dans le dos. Deux autres silhouettes travaillent au loin, "
  "encore plus petites. Aucun visage visible, aucune main au premier "
  "plan." + SANS_MOTS),
 # « La période de travail qui commence en après-midi et se termine tard le
 #   soir. »
 ('quart-de-soir', 'vocab', P_VOC, STYLE + " La façade d'une usine de brique "
  "rouge à un étage, photographiée de l'extérieur au crépuscule d'hiver, "
  "depuis le trottoir d'en face : une longue rangée de fenêtres à châssis "
  "d'aluminium **toutes éclairées d'une lumière blanche**, se détachant sur un "
  "ciel bleu nuit. Une porte d'employés éclairée d'une applique, un banc de "
  "neige devant, quelques traces de pas. Aucune enseigne sur la façade, aucun "
  "panneau, aucun numéro civique visible. Aucune personne." + SANS_MOTS),
 # « La suite de machines et de postes où un produit se fabrique du début à la
 #   fin. »
 ('chaine-de-production', 'vocab', P_VOC, STYLE + " Une chaîne de "
  "conditionnement complète vue dans sa longueur, en perspective, depuis le "
  "bout de la ligne : convoyeur à courroie, carters de tôle bleue, bras "
  "mécaniques, une station de remplissage puis une station d'empilage, des "
  "contenants de plastique clair qui progressent d'un poste à l'autre jusqu'au "
  "fond de l'image. Éclairage industriel régulier. Les écrans de commande sont "
  "éteints et de profil ; aucune étiquette, aucun pictogramme lisible sur les "
  "carters. Aucune personne." + SANS_MOTS),
 # « Une rencontre où plusieurs candidats sont reçus et observés en même
 #   temps. »
 # Refaite le 23 août 2026, pour la même raison que `salle-examen` : la
 # première version montrait six hommes. Le prompt impose désormais la
 # composition, et il déplace les deux observateurs **derrière l'appareil**
 # plutôt que contre le mur du fond — c'est ce qui faisait apparaître deux
 # visages, même flous.
 ('entrevue-de-groupe', 'vocab', P_VOC, PERS + " " + STYLE + " Une table "
  "ronde dans une salle de réunion d'usine, vue **de haut et de loin**, depuis "
  "un coin de la pièce : **quatre** personnes assises autour, vues du dessus et "
  "de dos, **aucun visage visible**, chacune avec un bloc-notes fermé devant "
  "elle. Le groupe est **mixte et d'origines diverses** : deux femmes et deux "
  "hommes, d'âges et de teints de peau différents. Personne d'autre n'est dans "
  "le champ : les observateurs sont derrière l'appareil. "
  "Moquette grise, murs de blocs crème, lumière de tubes "
  "fluorescents. Les blocs-notes sont fermés et vierges ; aucun tableau, "
  "aucune affiche sur les murs." + SANS_MOTS),
 # « Le moment où une machine ne produit pas, prévu ou non. »
 ('temps-d-arret', 'vocab', P_VOC, STYLE + " Cadrage serré sur une colonne "
  "lumineuse de signalisation à trois étages, montée sur le carter d'une "
  "machine industrielle : l'étage **ambre est allumé**, le vert et le rouge "
  "sont éteints. Derrière, un convoyeur immobile et vide, complètement flou. "
  "La lueur ambre se reflète sur la tôle bleue du carter. Aucun écran, aucun "
  "bouton étiqueté, aucune plaque signalétique dans le champ. Aucune "
  "personne." + SANS_MOTS),
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
