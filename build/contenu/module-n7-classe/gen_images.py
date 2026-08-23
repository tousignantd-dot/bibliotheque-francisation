#!/usr/bin/env python3
"""Les 10 images de module-n7-classe (niveau 7, activité 117).

Deux destinations :
  · `images/` — les six photos de l'exercice d'association du défi 1
    (`t1img`, « Ce que l'équipe est allée voir dans le quartier »), réduites
    à 1200 px qualité 85 ;
  · `vocab/`  — les quatre photos du banc de vocabulaire, réduites à 800 px
    qualité 82. Seize des vingt cartes n'ont **pas** d'image, et c'est voulu :
    « un mandat », « la répartition des rôles », « un tour de parole », « un
    consensus », « un compte rendu », « un résumé » nomment des façons de
    travailler ou des documents. Un document, c'est du texte, et le texte ne
    va pas dans l'image.

**Les quatre règles de prompt du 22 août 2026 sont appliquées ici**
(`CLAUDE.md`, « Les images d'un module ») :

1. aucun texte lisible ;
2. pas de mains ni de visages en gros plan ;
3. un décor québécois nommé ;
4. **l'image montre ce que dit son énoncé** — chaque prompt d'exercice est
   écrit à partir de la phrase exacte de la rangée `ok`, recopiée en
   commentaire juste au-dessus.

**Les deux pièges de ce module-ci, et le cadrage qui les règle.** Une salle de
classe est pleine d'inscriptions — tableau, affiches, écran de projection,
babillard — et pleine de visages. La parade n'est pas de les interdire, c'est
de **ne pas les cadrer** : ce module ne montre aucune salle de classe. Les six
photos d'exercice montrent le **quartier** que l'équipe est allée observer, et
la seule image où des personnes paraissent (« personne-ressource ») est prise
depuis le fond de la salle, à contre-jour, les auditeurs vus de dos et
l'écran de projection coupé par le bord supérieur du cadre. Deuxième piège,
plus discret : la rue porte des panneaux, l'école porte un numéro civique, le
sac d'arrosage d'un jeune arbre porte une étiquette du fournisseur. Chaque
prompt les met hors champ nommément.

Le contrôle avant livraison :

    node build/contexte_images.js module-n7-classe

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix — Google direct, puis fal.ai, puis
WaveSpeed —, rend le nom de celle qui a servi et inscrit chaque tentative au
registre `~/Claude/generations/journal_appels.py`.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu : ce fichier
vit dans `build/contenu/<slug>/`, donc trois niveaux sous la racine — sans
quoi il cesserait de fonctionner dans un worktree.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n7-classe/gen_images.py
  python3 build/contenu/module-n7-classe/gen_images.py trottoir-racine
  python3 build/contenu/module-n7-classe/gen_images.py vocab/canopee
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n7-classe'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Défi 1 · Exercice 2 — Ce que l'équipe est allée voir dans le quartier"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : une ville moyenne du Centre-du-Québec au début de l'été,
# des rues ordinaires. Rien de « moderne », rien de publicitaire : c'est de là
# que vient le générique américain.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle de début "
         "d'été, faible profondeur de champ. Ville moyenne du "
         "Centre-du-Québec : bungalows et duplex de brique et de déclin de "
         "vinyle, poteaux de bois et fils aériens, trottoirs de béton "
         "fissurés, bordures de granit, entrées d'asphalte, hangars de bois "
         "à l'arrière des logements. Palette sobre, végétation ordinaire, "
         "rien de spectaculaire. Aucune personne identifiable, aucun visage "
         "reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire au Québec "
        "avec quelques personnes vues de loin et de dos, jamais en gros plan, "
        "jamais de visage, jamais de mains au premier plan. Lumière naturelle "
        "douce, faible profondeur de champ.")

# La négation seule ne tient pas devant un objet qui porte des inscriptions :
# elle sert de filet, pas de parade. La parade est dans chaque prompt, et
# c'est le cadrage.
SANS_MOTS = (" Strictly no letters, no words, no digits and no readable "
             "characters anywhere in the image: every street sign, house "
             "number, notice, poster, whiteboard, projection screen, tag or "
             "label must fall outside the frame, be turned away from the "
             "camera, or be completely out of focus. Aucun mot d'anglais "
             "nulle part, aucune enseigne lisible, aucun logo, aucun "
             "filigrane.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── t1img · les six lieux du quartier ─────────────────────────────────
 # « Un grand stationnement d'asphalte noir en plein soleil, sans un seul arbre, vu de loin. »
 ('stationnement-asphalte', 'images', P_EX, STYLE + " Un grand stationnement "
  "commercial vide, en plein soleil de midi : une étendue d'asphalte noir "
  "neuf, très sombre, quadrillée de lignes de peinture pâle presque effacées, "
  "sans un seul arbre ni un seul îlot de verdure. Vue de loin, depuis le "
  "trottoir d'en face, cadrage bas et large ; la chaleur fait légèrement "
  "vibrer l'air au-dessus du sol. Deux ou trois autos très éloignées au fond. "
  "Les façades des commerces sont coupées par le bord supérieur de l'image et "
  "aucun panneau, aucun mât, aucune affiche n'entre dans le cadre. Aucune "
  "personne." + SANS_MOTS),
 # « Une rue résidentielle bordée d'érables matures dont les branches se rejoignent au-dessus de la chaussée. »
 ('rue-erables', 'images', P_EX, STYLE + " Une rue résidentielle tranquille "
  "vue depuis le milieu de la chaussée, en enfilade : deux rangées d'érables "
  "matures plantés de chaque côté, dont les hautes branches se rejoignent "
  "au-dessus de la rue et forment une voûte continue de feuillage vert. "
  "Lumière tachetée sur l'asphalte, ombre presque partout, duplex de brique "
  "en retrait derrière les troncs. Aucun panneau de signalisation, aucune "
  "plaque de rue, aucun numéro civique visible ; aucune auto au premier plan. "
  "Aucune personne." + SANS_MOTS),
 # « Un jeune arbre planté depuis peu, tenu droit par deux tuteurs de bois, un sac d'arrosage à sa base. »
 ('jeune-arbre-tuteurs', 'images', P_EX, STYLE + " Un jeune arbre feuillu au "
  "tronc mince, à peine plus haut qu'une personne, planté dans une bande de "
  "terre entre le trottoir et la rue : il est tenu bien droit par deux tuteurs "
  "de bois plantés de part et d'autre et reliés au tronc par des sangles "
  "noires. À sa base, un sac d'arrosage vert foncé en toile, fermé, enroulé "
  "autour du tronc ; le sac est vu de trois quarts arrière, de sorte que sa "
  "face imprimée et toute étiquette du fournisseur sont hors du champ. Paillis "
  "brun autour, gazon coupé court derrière. Aucune personne." + SANS_MOTS),
 # « Une cour d'école entièrement asphaltée, vue d'un étage, avec une mince bande de gazon jauni le long de la clôture. »
 ('cour-ecole', 'images', P_EX, STYLE + " Une cour d'école entièrement "
  "asphaltée, vue de haut depuis une fenêtre du deuxième étage : une grande "
  "surface d'asphalte gris foncé et craquelé, vide, avec les restes très pâles "
  "de lignes de jeu peintes au sol, aucune ombre nulle part. Le long de la "
  "clôture à mailles losangées qui la ferme, une mince bande de gazon jauni et "
  "sec. Un panier de basketball sans filet, de dos. Aucun panneau, aucune "
  "affiche sur la clôture, aucun numéro sur le mur ; les fenêtres de l'école "
  "sont hors champ. Aucune personne, aucun enfant." + SANS_MOTS),
 # « Un trottoir de béton soulevé et fendu par la grosse racine de l'arbre planté à côté. »
 ('trottoir-racine', 'images', P_EX, STYLE + " Cadrage rapproché et en biais "
  "sur une section de trottoir de béton gris : une grosse racine d'arbre a "
  "soulevé deux dalles voisines, qui se chevauchent maintenant de plusieurs "
  "centimètres, avec une longue fissure entre les deux et de la mousse dans la "
  "cassure. À droite du cadre, la base d'un tronc épais et son écorce "
  "profondément crevassée. Herbe folle dans le joint. Le haut de l'arbre est "
  "hors champ. Aucune personne, aucune main, aucun pied." + SANS_MOTS),
 # « Une ruelle de gravier entièrement à l'ombre, entre deux rangées de hangars de bois et de gros arbres. »
 ('ruelle-ombragee', 'images', P_EX, STYLE + " Une ruelle résidentielle en "
  "gravier, vue en enfilade, entièrement à l'ombre en plein après-midi : de "
  "chaque côté, des hangars de bois peints et des clôtures de bois gris, et "
  "au-dessus, les cimes de gros arbres matures qui se referment presque "
  "complètement. Quelques taches de soleil sur le gravier, des poubelles "
  "roulantes rangées le long d'une clôture, un fil électrique qui traverse. "
  "Aucune affiche, aucun graffiti lisible, aucune plaque de ruelle. Aucune "
  "personne." + SANS_MOTS),

 # ── Les quatre photos du banc de vocabulaire ──────────────────────────
 # « Quelqu'un qui connaît bien un sujet et qu'on invite pour l'entendre et le
 #   questionner. »
 ('personne-ressource', 'vocab', P_VOC, PERS + " " + STYLE + " Une salle de cours "
  "d'un centre d'éducation des adultes, photographiée depuis la dernière "
  "rangée : au fond de l'image, une personne debout de dos ou de trois quarts "
  "arrière, en silhouette à contre-jour devant la fenêtre, s'adresse à une "
  "dizaine d'adultes assis, tous vus de dos, épaules et nuques seulement. "
  "L'avant de la salle — tableau, écran de projection, mur du fond — est coupé "
  "par le bord supérieur de l'image et n'apparaît pas. Aucun visage, aucune "
  "feuille lisible sur les tables, aucun texte." + SANS_MOTS),
 # « Un secteur dont la surface devient beaucoup plus chaude que celle des
 #   secteurs voisins. »
 # Refaite : la première version montrait un quartier résidentiel ordinaire,
 # pelouses vertes comprises — le contraire de ce que dit l'énoncé. Le prompt
 # refait **remplit le cadre de minéral** au lieu de décrire un secteur, et il
 # met le contraste dans l'image : le vert n'apparaît qu'au loin, au fond.
 ('ilot-de-chaleur', 'vocab', P_VOC, STYLE + " Vue en plongée depuis un toit, "
  "un jour de canicule, sur un secteur commercial où l'on ne voit **que du "
  "minéral** : au premier plan une immense toiture plate de gravier noir avec "
  "ses appareils de ventilation métalliques, derrière elle une mer d'asphalte "
  "de stationnement, sans un seul arbre et sans un seul brin d'herbe sur les "
  "quatre cinquièmes de l'image. Tout au fond, très loin et très petite, une "
  "bande verte d'arbres marque le quartier voisin. Air qui tremble de chaleur, "
  "ombres très courtes de midi, ciel blanc. Aucun bâtiment portant une "
  "enseigne, aucun mât, aucune personne." + SANS_MOTS),
 # « La couverture formée par la cime des arbres, vue d'en haut, mesurée en
 #   pourcentage du territoire. »
 ('canopee', 'vocab', P_VOC, STYLE + " Vue aérienne basse, à la verticale, d'un "
  "quartier résidentiel en été : on ne voit presque que les cimes rondes et "
  "vertes des grands arbres, serrées les unes contre les autres, entre "
  "lesquelles apparaissent seulement quelques bouts de toitures grises et un "
  "mince ruban d'asphalte. Fin d'après-midi, ombres longues des couronnes sur "
  "ce qu'on aperçoit de la rue. Aucun panneau, aucune inscription au sol, "
  "aucune personne." + SANS_MOTS),
 # « Un arbre planté dans le trottoir ou en bordure de la chaussée, dans une
 #   ouverture étroite. »
 ('arbre-de-rue', 'vocab', P_VOC, STYLE + " Un arbre de bonne taille planté "
  "dans une ouverture carrée découpée à même le trottoir de béton, en bordure "
  "d'une rue de quartier : la fosse est visiblement étroite, à peine plus "
  "large que le tronc, remplie de terre tassée et de quelques mauvaises "
  "herbes, et le béton est fendu sur un côté. Cadrage à hauteur de taille, "
  "l'arbre coupé au niveau des premières branches. Une bordure de granit et le "
  "bord de la chaussée à droite. Aucune plaque, aucune borne d'incendie "
  "portant une inscription, aucune personne." + SANS_MOTS),
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
