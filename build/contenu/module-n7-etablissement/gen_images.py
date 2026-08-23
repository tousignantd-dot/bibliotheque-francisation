#!/usr/bin/env python3
"""Les 13 images de module-n7-etablissement (niveau 7, activité 118).

Deux destinations :
  · `images/` — les dix photos des deux exercices d'association (« Je
    découvre » exercice 5, et Défi 2 exercice 5), réduites à 1200 px
    qualité 85 ;
  · `vocab/`  — trois photos seulement du banc de vocabulaire, réduites à
    800 px qualité 82.

**Pourquoi si peu d'images de vocabulaire.** Le lexique de l'admission est
administratif : un préalable, une aptitude, un rang, une reconnaissance des
acquis ne se photographient pas. Leur donner une image reviendrait à poser
derrière chaque mot une vue générique de secrétariat d'école — c'est-à-dire le
thème du module à la place de ce que dit la carte, le quatrième défaut relevé
le 22 août 2026 et commis volontairement treize fois par `module-n7-banque`.
Les trois retenues montrent un objet ou un lieu réel, décrit par la phrase
d'exemple de leur propre carte.

**Ce module est un piège à texte** : un centre de formation est fait
d'enseignes, de panneaux de porte, de numéros de casier, de formulaires et
d'abribus publicitaires. La parade appliquée ici est celle du 23 août 2026 —
**non pas répéter l'interdiction, mais cadrer l'inscription hors champ** :
l'enseigne du centre est au-dessus du bord supérieur, les casiers ont des
plaques lisses vues en enfilade, le caisson publicitaire de l'abribus est
derrière l'appareil, les panneaux de chambre du corridor sont hors du champ,
et les étiquettes du laboratoire sont coupées par le cadre.

Les quatre règles de `CLAUDE.md` (« Les images d'un module ») :

1. aucun texte lisible — ici par le cadrage, pas par la négation seule ;
2. pas de mains ni de visages en gros plan — ici en imposant le poste des
   objets : la chaise vide, la blouse au crochet, la table déjà dressée ;
3. un décor québécois nommé — brique brune, mélamine, tuiles de vinyle pâle,
   neige poussée en tas, déclin de vinyle, abribus de boulevard ;
4. **l'image montre ce que dit son énoncé.** Les dix prompts d'exercice sont
   écrits à partir de la phrase exacte de la rangée `ok`, recopiée en
   commentaire au-dessus de chacun. Le contrôle avant livraison :

       node build/contexte_images.js module-n7-etablissement

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix — Google direct, puis fal.ai, puis
WaveSpeed —, rend le nom de celle qui a servi et inscrit chaque tentative au
registre `~/Claude/generations/journal_appels.py`.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu : ce fichier
vit dans `build/contenu/<slug>/`, donc trois niveaux sous la racine — sans
quoi il écrirait dans le dépôt principal au lieu du worktree de l'agent, ce
qui est arrivé à l'activité 108.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n7-etablissement/gen_images.py
  python3 build/contenu/module-n7-etablissement/gen_images.py entree-du-centre
  python3 build/contenu/module-n7-etablissement/gen_images.py vocab/stage
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n7-etablissement'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX1 = "Je découvre · Exercice 5 — Les lieux du dossier de Rania"
P_EX2 = "Défi 2 · Exercice 5 — Le matin de l'entrevue"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : Granby et les Cantons-de-l'Est à la fin de l'hiver. Des
# intérieurs institutionnels ordinaires, une lumière franche et basse. Rien de
# publicitaire, rien de « moderne » : le générique américain vient de là.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle de fin "
         "d'hiver, faible profondeur de champ. Ville moyenne des "
         "Cantons-de-l'Est, au Québec : brique brune, déclin de vinyle, "
         "perrons de béton, stationnements d'asphalte fissuré, neige poussée "
         "en tas sale. À l'intérieur, mobilier institutionnel ordinaire et un "
         "peu usé : mélamine beige, tuiles de vinyle pâle, chaises "
         "rembourrées grises, éclairage de tubes fluorescents. Palette sobre. "
         "Aucun texte lisible, aucun mot déchiffrable, aucun logo, aucune "
         "marque, aucun filigrane, aucune personne identifiable, aucun visage "
         "reconnaissable.")

# Un centre de formation est couvert d'inscriptions : enseigne, panneaux de
# porte, numéros de casier, affiches de babillard, publicité d'abribus. Le
# modèle en écrit du charabia ou de l'anglais, et l'élève le lit. La négation
# ne suffit pas : chaque prompt sort l'inscription du cadre.
SANS_MOTS = (" Strictly no letters, no digits, no readable characters "
             "anywhere in the image: every sign, label, door plate, locker "
             "number, poster, screen interface or form field must be an "
             "abstract grey stroke, a blank surface, or be cropped out of "
             "frame entirely. Aucun mot d'anglais nulle part, aucune enseigne "
             "lisible, aucun numéro déchiffrable, aucune affiche.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les cinq images de « Je découvre », exercice 5 ────────────────────
 # « Une salle du personnel, une table longue de mélamine et un four à
 #   micro-ondes sur un comptoir. »
 ('salle-du-personnel', 'images', P_EX1, STYLE + " Une salle du personnel "
  "d'un centre d'hébergement pour personnes âgées : une longue table de "
  "mélamine beige au centre avec des chaises de plastique dépareillées, et le "
  "long du mur un comptoir bas sur lequel est posé un four à micro-ondes "
  "blanc un peu vieux, à côté d'une bouilloire. Mur de blocs de béton peints "
  "en crème, babillard de liège entièrement vide et sans une seule feuille. "
  "Aucune horloge, aucun panneau, aucun affichage nulle part. Aucune "
  "personne." + SANS_MOTS),
 # « L'entrée en brique brune d'un centre de formation, deux portes vitrées et
 #   un stationnement déneigé. »
 ('entree-du-centre', 'images', P_EX1, STYLE + " L'entrée d'un centre de "
  "formation professionnelle des années soixante-dix : façade de brique "
  "brune, deux portes vitrées à cadre d'aluminium au centre, quelques marches "
  "de béton et une rampe de métal noir. Le cadrage s'arrête **juste au-dessus "
  "du linteau des portes** : tout ce qui pourrait porter une enseigne, un nom "
  "ou un panneau est au-dessus du bord supérieur de l'image. Devant, un "
  "stationnement d'asphalte déneigé avec des bancs de neige sale au fond. "
  "Ciel couvert de mars. Aucune personne, aucune voiture au premier "
  "plan." + SANS_MOTS),
 # « Une table de cuisine tard le soir : un ordinateur portable ouvert, une
 #   tasse et une pile de feuilles. »
 ('table-de-cuisine-le-soir', 'images', P_EX1, STYLE + " Une table de cuisine "
  "vue en légère plongée, tard le soir, éclairée par une seule lampe "
  "suspendue : un ordinateur portable ouvert **vu de trois quarts arrière**, "
  "de sorte que son écran est tourné à l'opposé de l'appareil photo et "
  "entièrement invisible, une tasse de café à moitié pleine, et une pile de "
  "feuilles blanches posée à plat, la page du dessus complètement vierge. Le "
  "reste de la pièce est dans le noir. Aucune personne, aucune main dans le "
  "cadre." + SANS_MOTS),
 # « Un corridor d'unité de soins, un plancher de tuiles pâles et une main
 #   courante le long du mur. »
 ('corridor-du-chsld', 'images', P_EX1, STYLE + " Un corridor d'unité de "
  "soins de longue durée, vu dans l'axe : plancher de tuiles de vinyle pâles "
  "et cirées, murs peints en beige avec une main courante de bois clair fixée "
  "à mi-hauteur des deux côtés, portes de chambre entrouvertes en enfilade. "
  "Les plaques et les numéros de porte sont **hors du champ**, coupés par le "
  "bord de l'image ou remplacés par des surfaces lisses. Lumière de tubes "
  "fluorescents et fenêtre au fond du corridor. Aucune personne, aucun "
  "panneau, aucune affiche au mur." + SANS_MOTS),
 # « Un abribus au bord d'un boulevard, avant le lever du jour, avec de la
 #   neige fondante au sol. »
 ('arret-dautobus-au-petit-matin', 'images', P_EX1, STYLE + " Un abribus de "
  "boulevard québécois avant le lever du jour, photographié **de biais et par "
  "l'arrière**, de sorte que son caisson publicitaire latéral est derrière "
  "l'appareil et n'apparaît pas : on voit la structure de métal peint, les "
  "panneaux de verre embués et le banc vide à l'intérieur. Trottoir couvert "
  "de neige fondante et de gadoue, lampadaire orange encore allumé, ciel "
  "bleu-gris. Aucune personne, aucun panneau, aucun horaire affiché, aucune "
  "publicité." + SANS_MOTS),

 # ── Les cinq images du Défi 2, exercice 5 ─────────────────────────────
 # « Une petite salle d'attente : trois chaises contre un mur et une plante
 #   dans un pot de plastique. »
 ('salle-dattente-du-centre', 'images', P_EX2, STYLE + " Une petite salle "
  "d'attente de centre de formation, cadrée face à un mur plein : exactement "
  "trois chaises rembourrées grises alignées côte à côte contre ce mur clair, "
  "et à l'extrémité de la rangée une plante verte dans un pot de plastique "
  "noir posé au sol. Tuiles de vinyle pâles, éclairage encastré. Aucune "
  "porte, aucune fenêtre, aucun babillard dans le champ. Aucune personne, "
  "aucune affiche, aucune revue." + SANS_MOTS),
 # « Une table de réunion vide, deux chaises d'un côté et une seule de
 #   l'autre. »
 ('table-de-comite', 'images', P_EX2, STYLE + " Une petite salle de réunion "
  "de bureau institutionnel : une table rectangulaire de mélamine claire, "
  "vide, avec **exactement deux chaises de bureau du même côté** et **une "
  "seule chaise en face**, de l'autre côté de la table. Un pichet d'eau et "
  "deux verres au centre. Cloison vitrée derrière, store baissé. Lumière du "
  "matin. Aucune personne, aucun papier sur la table, aucun écran, aucun "
  "tableau au mur." + SANS_MOTS),
 # « Un laboratoire de soins d'école : un lit d'hôpital monté, une potence et
 #   un chariot métallique. »
 ('laboratoire-de-soins', 'images', P_EX2, STYLE + " Un laboratoire de "
  "pratique en soins, dans une école : un lit d'hôpital monté avec des draps "
  "blancs tirés au carré, une potence de soluté nue à côté du lit, et un "
  "chariot métallique à deux plateaux au pied du lit, avec quelques plateaux "
  "de métal vides. Les flacons, les boîtes et tout ce qui pourrait porter une "
  "étiquette sont **hors du champ**, coupés par le bord inférieur de l'image. "
  "Murs pâles, plancher de vinyle. Aucune personne, aucun mannequin, aucune "
  "étiquette, aucun écran." + SANS_MOTS),
 # « Un corridor d'école bordé de casiers de métal beige, tous fermés. »
 ('casiers-du-corridor', 'images', P_EX2, STYLE + " Un corridor d'école vu en "
  "enfilade, bordé des deux côtés de casiers de métal beige un peu bosselés, "
  "**tous fermés**, dont les plaques et les cadenas sont des surfaces lisses "
  "sans aucun chiffre ni aucune inscription. Plancher de terrazzo, lumière de "
  "tubes fluorescents et fenêtre au fond. Aucune personne, aucun panneau, "
  "aucune affiche." + SANS_MOTS),
 # « Un stationnement d'asphalte au petit matin, quelques voitures et de la
 #   neige poussée en tas au bout. »
 ('stationnement-au-petit-matin', 'images', P_EX2, STYLE + " Un stationnement "
  "d'asphalte fissuré au petit matin, vu de niveau : cinq ou six voitures "
  "garées en rangée, couvertes de givre, et au bout du terrain un gros tas de "
  "neige sale poussée par la déneigeuse. Les plaques d'immatriculation sont "
  "**coupées par le bord inférieur de l'image** ou masquées par l'angle de "
  "prise de vue. Lampadaire encore allumé, ciel qui pâlit. Aucune personne, "
  "aucun panneau de stationnement, aucune enseigne." + SANS_MOTS),

 # ── Les trois photos du banc de vocabulaire ───────────────────────────
 # « une entrevue de sélection » — « Son entrevue de sélection est fixée au
 #   mardi matin, à neuf heures quinze. »
 ('entrevue-de-selection', 'vocab', P_VOC, STYLE + " Une seule chaise "
  "rembourrée grise posée dans un corridor de bureau institutionnel, contre "
  "un mur clair, juste à côté d'une porte de bureau fermée en bois pâle. La "
  "plaque de la porte est une petite surface de métal lisse, entièrement "
  "vide. Tuiles de vinyle pâles, lumière de plafond. Aucune personne, aucun "
  "panneau, aucune inscription." + SANS_MOTS),
 # « une pièce justificative » — « L'attestation de son employeur est la pièce
 #   justificative qui manquait au dossier. »
 ('piece-justificative', 'vocab', P_VOC, STYLE + " Une chemise cartonnée "
  "beige fermée, posée à plat sur une table de mélamine, avec deux ou trois "
  "feuilles qui dépassent légèrement d'un côté et qu'on ne voit que **par la "
  "tranche** : aucune face imprimée n'est visible. Un trombone posé à côté. "
  "Lumière rasante de fin de journée par une fenêtre. Aucune personne, aucune "
  "main, aucune ligne de texte." + SANS_MOTS),
 # « un stage » — « Le stage se fait dans un établissement de la région, à
 #   raison de quatre jours par semaine. »
 ('stage', 'vocab', P_VOC, STYLE + " Un vestiaire d'employés dans un "
  "établissement de soins : une blouse d'uniforme bleu pâle suspendue à un "
  "crochet de métal contre un mur de blocs peints, et au sol, juste en "
  "dessous, une paire de sabots de travail blancs posés côte à côte. Un banc "
  "de bois au premier plan, flou. Lumière de plafonnier. Aucune personne, "
  "aucun visage, aucune étiquette sur la blouse." + SANS_MOTS),
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
    print('  ✓ %-30s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('   ✗ ' + e)
