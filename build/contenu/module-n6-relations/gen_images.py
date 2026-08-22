#!/usr/bin/env python3
"""Les 22 images de module-n6-relations (niveau 6, activité 101).

Deux destinations :
  · `images/` — les douze photos des deux exercices à glisser-déposer (les
    six lieux de « Je découvre », les six détails du Défi 2), réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les dix photos du banc de vocabulaire, réduites à 800 px
    qualité 82.

**Non exécuté au moment de la livraison du module** : les images coûtent de
l'argent réel et l'agent qui a produit le module n'était pas autorisé à les
générer. `node build/coherence.js module-n6-relations` sort donc 22 écarts
« image absente du disque », tous attendus, et aucun autre.

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix mesuré le 21 août 2026 — Google direct,
puis fal.ai, puis WaveSpeed — rend le nom de celle qui a servi, et inscrit
chaque tentative au registre `~/Claude/generations/journal_appels.py`. Un
fournisseur facture des **appels**, pas des fichiers présents : une image
régénérée est payée chaque fois.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu écrit à la
main : ce fichier vit dans `build/contenu/<slug>/`, donc trois niveaux sous la
racine du dépôt. Les générateurs des premiers modules portaient le chemin en
dur et cessaient de fonctionner dès qu'on travaillait dans un worktree.

**La contrainte propre à ce module : personne n'est reconnaissable, alors que
le Défi 2 porte sur la description physique.** C'est voulu, et c'est ce qui
rend l'exercice juste : on ne montre jamais un visage, on montre ce qui se
voit de loin dans un terminus — une silhouette à contre-jour, un chignon vu de
dos, des lunettes posées, un foulard sur une épaule, une valise, une
casquette. L'élève apprend ainsi à décrire des repères, pas des traits.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n6-relations/gen_images.py
  python3 build/contenu/module-n6-relations/gen_images.py terminus-autobus
  python3 build/contenu/module-n6-relations/gen_images.py vocab/jumelage
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n6-relations'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_LIEUX = "Je découvre · Exercice 4 — Les lieux de cette histoire"
P_DESC = "Défi 2 · Exercice 2 — Ce qui se voit de loin dans un terminus"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : Saint-Hyacinthe ordinaire, lumière naturelle, rien de
# spectaculaire. Repris tel quel d'un module à l'autre, seule la palette change
# quand le thème l'exige.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle, faible "
         "profondeur de champ. Ville moyenne du Québec, intérieurs et rues "
         "ordinaires, palette sobre. Aucun texte lisible, aucun mot "
         "déchiffrable, aucun logo, aucune marque, aucun filigrane, aucune "
         "personne identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie ordinaire au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts "
        "arrière ou hors cadrage du visage. Lumière naturelle douce, faible "
        "profondeur de champ. Aucun visage reconnaissable, aucun texte, aucun "
        "logo, aucun filigrane.")

# La moitié des images de ce module contient du papier ou un écran — un
# courriel, un journal, une feuille imprimée — et un modèle d'image écrit
# volontiers de l'anglais dessus.
SANS_MOTS = (" Strictly no letters, no words, no readable characters anywhere "
             "in the image: every line of text, including any headline or "
             "label, must be an abstract grey stroke. Aucun mot d'anglais "
             "nulle part.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six lieux de « Je découvre » ──────────────────────────────────
 ('comptoir-boulangerie', 'images', P_LIEUX, STYLE + " Le comptoir d'une petite "
  "boulangerie de quartier, tôt le matin : un plan de travail de bois clair, des "
  "plateaux de pains et de croissants derrière une vitrine, une caisse ancienne au "
  "bout. Aucune personne. Aucune étiquette de prix lisible." + SANS_MOTS),
 ('ecran-courriel', 'images', P_LIEUX, STYLE + " Un écran d'ordinateur portable posé "
  "sur une table de cuisine, qui affiche un courriel long : quatre blocs de "
  "paragraphes séparés par des blancs, une ligne d'objet en haut. Toutes les lignes "
  "de texte sont des traits gris entièrement illisibles. Aucune personne." + SANS_MOTS),
 ('table-cuisine-lecture', 'images', P_LIEUX, STYLE + " Une table de cuisine vue de "
  "haut : une feuille imprimée posée à plat, un crayon de bois en travers, une tasse "
  "de thé à moitié pleine, des lunettes de lecture repliées. Les lignes de la feuille "
  "sont des traits gris illisibles. Aucune personne." + SANS_MOTS),
 ('terminus-autobus', 'images', P_LIEUX, STYLE + " Le quai d'un petit terminus "
  "d'autobus régional en fin d'après-midi : un abri vitré, un banc de métal, un "
  "guichet fermé, un autobus interurbain stationné en arrière-plan. Aucune personne, "
  "aucune destination lisible sur l'autobus." + SANS_MOTS),
 ('salle-communautaire', 'images', P_LIEUX, STYLE + " Une salle communautaire au "
  "sous-sol d'une église : plafond bas, tuiles acoustiques, une quinzaine de chaises "
  "pliantes disposées en cercle sur un plancher de tuiles, une table à café le long du "
  "mur. Aucune personne, aucune affiche lisible." + SANS_MOTS),
 ('journal-quartier', 'images', P_LIEUX, STYLE + " Un journal de quartier en papier, "
  "plié en deux et posé sur une table de cuisine, ouvert sur une page à trois colonnes "
  "avec une photo carrée en haut. Toutes les lignes de texte sont des traits gris "
  "entièrement illisibles." + SANS_MOTS),

 # ── Les six détails du Défi 2 ─────────────────────────────────────────
 # Aucun visage : c'est la contrainte du dossier, et c'est aussi ce que
 # l'exercice enseigne — on décrit ce qui se voit de loin.
 ('silhouette-quai', 'images', P_DESC, PERS + " Une seule personne vue de dos et à "
  "contre-jour sur le quai d'un terminus d'autobus, debout, une valise à côté d'elle. "
  "On ne distingue que la silhouette : la taille, la carrure, la longueur du manteau. "
  "Le visage est hors cadrage." + SANS_MOTS),
 ('chignon-nuque', 'images', P_DESC, PERS + " Gros plan sur la nuque d'une personne "
  "vue de dos : des cheveux ondulés bruns relevés en chignon bas, quelques mèches "
  "libres, le col d'une veste grise. Le visage n'est pas visible du tout." + SANS_MOTS),
 ('lunettes-rondes', 'images', P_DESC, STYLE + " Gros plan sur une paire de lunettes "
  "rondes à monture fine et dorée, repliées et posées sur une table de bois clair à "
  "côté d'un carnet fermé. Aucune personne." + SANS_MOTS),
 ('foulard-vert', 'images', P_DESC, PERS + " Détail d'un foulard de laine vert posé "
  "sur l'épaule d'un manteau gris, vu de trois quarts arrière. Le cadrage s'arrête à "
  "la hauteur du menton : aucun visage." + SANS_MOTS),
 ('valise-rouge', 'images', P_DESC, STYLE + " Une grosse valise rouge rigide à "
  "roulettes, debout, poignée télescopique sortie, à côté d'un banc de métal dans une "
  "salle d'attente de terminus. Aucune personne, aucune étiquette lisible." + SANS_MOTS),
 ('casquette-bleue', 'images', P_DESC, STYLE + " Une casquette de coton bleu marine "
  "usée, posée sur un vieux manteau de laine brun plié, sur une chaise de cuisine. "
  "Aucune personne, aucune inscription sur la casquette." + SANS_MOTS),

 # ── Les dix photos du banc de vocabulaire ─────────────────────────────
 ('demenagement', 'vocab', P_VOC, PERS + " Une pièce à moitié vidée : des boîtes de "
  "carton fermées empilées, un ruban à emballer sur le dessus, un cadre décroché posé "
  "contre le mur. Une personne de dos porte une boîte, hors cadrage du visage."
  + SANS_MOTS),
 ('faire-part', 'vocab', P_VOC, STYLE + " Gros plan sur une petite carte de papier "
  "épais crème, à bord doré, posée sur une table à côté de son enveloppe ouverte. Les "
  "quelques lignes imprimées sont des traits gris illisibles." + SANS_MOTS),
 ('accident-travail', 'vocab', P_VOC, STYLE + " Un atelier de garage : une plateforme "
  "de travail métallique à mi-hauteur, une échelle repliée à côté, des outils posés au "
  "sol, un cône orange de signalisation. Aucune personne, aucune blessure montrée."
  + SANS_MOTS),
 ('readaptation', 'vocab', P_VOC, PERS + " Une salle de réadaptation claire : une "
  "personne vue de dos marche entre deux barres parallèles basses, un physiothérapeute "
  "à côté d'elle, également de dos. Une paire de béquilles appuyée au mur." + SANS_MOTS),
 ('retrouvailles', 'vocab', P_VOC, PERS + " Deux personnes qui s'étreignent dans le "
  "hall d'un petit terminus d'autobus, vues de loin et de dos, une valise posée à côté "
  "d'elles. Aucun visage visible." + SANS_MOTS),
 ('silhouette', 'vocab', P_VOC, PERS + " Une personne seule à contre-jour devant une "
  "grande fenêtre de salle d'attente, vue de dos : seule la forme générale se "
  "distingue." + SANS_MOTS),
 ('visage-allonge', 'vocab', P_VOC, STYLE + " Un miroir ovale ancien accroché à un mur "
  "clair, qui ne reflète que la pièce vide et une fenêtre. Aucune personne, aucun "
  "reflet de visage." + SANS_MOTS),
 ('cheveux-ondules', 'vocab', P_VOC, PERS + " Gros plan sur des cheveux bruns ondulés "
  "détachés tombant sur les épaules, vus de dos, lumière naturelle de fenêtre. Le "
  "visage n'apparaît pas." + SANS_MOTS),
 ('jumelage', 'vocab', P_VOC, PERS + " Deux familles marchent ensemble sur un trottoir "
  "de quartier résidentiel en automne, vues de dos, à distance. Aucun visage "
  "reconnaissable." + SANS_MOTS),
 ('organisme-communautaire', 'vocab', P_VOC, STYLE + " L'entrée d'un local "
  "communautaire au sous-sol d'un immeuble : une porte vitrée, un présentoir de "
  "dépliants aux couvertures unies, un tableau d'affichage en liège couvert de "
  "feuillets. Aucune personne, aucune affiche lisible, aucun logo." + SANS_MOTS),
]


def reduire(data, largeur, qualite):
    """L'image d'exercice occupe 223 x 132 px à l'écran, la photo du banc moins.

    La route Google directe rend des JPEG bien plus lourds que fal.ai ; les
    deux se réduisent, seulement pas au même format. La hauteur suit le rapport
    de l'image reçue au lieu d'être forcée à un carré — c'est tout l'objet du
    passage au 3:2.
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
