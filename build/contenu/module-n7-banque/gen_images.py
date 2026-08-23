#!/usr/bin/env python3
"""Les 13 images de module-n7-banque (niveau 7, activité 114).

Deux destinations :
  · `images/` — les dix photos des deux exercices d'association (« Je
    découvre » exercice 4, et Défi 3 exercice 5), réduites à 1200 px
    qualité 85 ;
  · `vocab/`  — trois photos seulement du banc de vocabulaire, réduites à
    800 px qualité 82.

**Pourquoi si peu d'images de vocabulaire.** Le lexique de cette situation est
abstrait : un solde, un taux, une cote, un rendement, une protection, une
contestation ne se photographient pas. Leur donner une image reviendrait à
poser derrière chaque mot une vue générique de comptoir de caisse —
c'est-à-dire le thème du module à la place de ce que dit la carte, exactement
le quatrième défaut relevé le 22 août 2026. Les trois retenues montrent un
objet réel, décrit par la phrase d'exemple de leur carte, et distinct de ceux
que montrent déjà les dix images d'exercice.

**Ce module est le pire piège à texte du dépôt** : relevé, carte, écran,
calculatrice, affichage de taux — presque tout ce qui illustre une banque
porte des chiffres ou des mots. La leçon des quatre modules du 23 août 2026
est appliquée ici : **la parade n'est pas de répéter l'interdiction, c'est de
cadrer l'inscription hors champ**. L'afficheur de la calculatrice est coupé
par le bord de l'image, la carte de plastique est retournée face contre la
table, le relevé est vu par la tranche. Même mécanique pour les mains :
chaque prompt **impose le poste de l'appareil** au lieu d'écrire « pas de
mains ».

Les quatre règles de `CLAUDE.md` (« Les images d'un module ») :

1. aucun texte lisible — ici par le cadrage, pas par la négation seule ;
2. pas de mains ni de visages en gros plan — ici par le poste de l'appareil ;
3. un décor québécois nommé — mélamine, fromagerie, perron, neige fondue ;
4. **l'image montre ce que dit son énoncé.** Les dix prompts d'exercice sont
   écrits à partir de la phrase exacte de la rangée `ok`, recopiée en
   commentaire au-dessus de chacun. Le contrôle avant livraison :

       node build/contexte_images.js module-n7-banque

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix — Google direct, puis fal.ai, puis
WaveSpeed —, rend le nom de celle qui a servi et inscrit chaque tentative au
registre `~/Claude/generations/journal_appels.py`. Un fournisseur facture des
**appels**, pas des fichiers présents.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu : ce fichier
vit dans `build/contenu/<slug>/`, donc trois niveaux sous la racine — sans
quoi il cesserait de fonctionner dans un worktree.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n7-banque/gen_images.py
  python3 build/contenu/module-n7-banque/gen_images.py carte-coupee
  python3 build/contenu/module-n7-banque/gen_images.py vocab/hameconnage
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n7-banque'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX1 = "Je découvre · Exercice 4 — Les lieux et les objets du dossier de Marlène"
P_EX3 = "Défi 3 · Exercice 5 — Le soir de la contestation"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : Victoriaville et le Centre-du-Québec, des intérieurs
# ordinaires, une lumière franche mais basse. Rien de publicitaire, rien de
# « moderne » : le générique américain vient de là.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle de fin "
         "d'hiver ou de début de printemps, faible profondeur de champ. Ville "
         "moyenne du Centre-du-Québec : maisons de brique et de déclin de "
         "vinyle, perrons de béton, escaliers de métal peint, fenêtres à "
         "guillotine, comptoirs et tables de mélamine à l'intérieur, mobilier "
         "ordinaire un peu usé, palette sobre. Aucun texte lisible, aucun mot "
         "déchiffrable, aucun logo, aucune marque, aucun filigrane, aucune "
         "personne identifiable, aucun visage reconnaissable.")

# Le sujet de ce module est fait de chiffres : relevés, taux, afficheurs,
# cartes. Un modèle d'image écrit du charabia numérique ou de l'anglais sur
# tout objet qui, dans le monde, porte une inscription — et l'élève le lit.
# La négation ne suffit pas : chaque prompt sort l'inscription du cadre.
SANS_MOTS = (" Strictly no letters, no digits, no readable characters "
             "anywhere in the image: every line of text, every number, every "
             "display, label, sign, screen interface or form field must be an "
             "abstract grey stroke or be cropped out of frame entirely. Aucun "
             "mot d'anglais nulle part, aucun nom d'institution, aucune "
             "enseigne lisible, aucun chiffre déchiffrable.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les cinq images de « Je découvre », exercice 4 ────────────────────
 # « Une salle de repos d'usine, une longue table de mélamine et des chaises
 #   dépareillées. »
 # Refaite : la première version laissait dépasser du bord supérieur la moitié
 # d'un cadran d'horloge, avec ses chiffres. Le prompt disait déjà « hors
 # champ » ; ce qui manque à une négation, c'est de dire où va l'appareil.
 # Le mur du fond est donc nu, sans horloge du tout.
 ('salle-de-repos', 'images', P_EX1, STYLE + " Une salle de repos d'employés "
  "dans une petite usine agroalimentaire du Québec : une longue table de "
  "mélamine beige au centre, six ou sept chaises de plastique dépareillées "
  "autour, un mur de blocs de béton peints en crème, un babillard de liège "
  "entièrement vide au fond. Aucune horloge, aucun cadran, aucun panneau, "
  "aucun affichage nulle part sur les murs. Lumière de tubes fluorescents. "
  "Aucune personne." + SANS_MOTS),
 # « Une enveloppe déjà ouverte et une feuille pliée en trois, posées sur une
 #   nappe cirée. »
 ('enveloppe-du-releve', 'images', P_EX1, STYLE + " Une table de cuisine "
  "couverte d'une nappe de toile cirée à petits motifs : une enveloppe blanche "
  "déchirée sur le côté court, et à côté une feuille encore pliée en trois, "
  "posée de biais et vue presque par la tranche, de sorte qu'aucune de ses "
  "lignes n'est de face. Une tasse vide au bord du cadre. Lumière grise de fin "
  "d'après-midi par une fenêtre. Aucune personne, aucune main." + SANS_MOTS),
 # « Une calculatrice à gros boutons et un stylo, seuls sous une lampe de
 #   cuisine, tard le soir. »
 ('calculatrice-du-soir', 'images', P_EX1, STYLE + " Vue en légère plongée sur "
  "une calculatrice de bureau à gros boutons posée sur une table de cuisine "
  "sombre, un stylo à bille couché à côté. Le cadrage coupe l'appareil au ras "
  "de la première rangée de touches : **l'afficheur est entièrement hors "
  "champ**, au-dessus du bord supérieur de l'image. Une seule lampe suspendue "
  "éclaire la scène, le reste de la pièce est dans le noir. Aucune personne, "
  "aucune main dans le cadre." + SANS_MOTS),
 # « Un quai de réception où des caisses de plastique bleues attendent devant
 #   une porte relevée. »
 ('quai-de-la-fromagerie', 'images', P_EX1, STYLE + " Un quai de réception de "
  "petite usine alimentaire, porte de garage métallique relevée aux trois "
  "quarts : une vingtaine de caisses de plastique bleues empilées par colonnes "
  "sur le béton, un diable appuyé contre le mur, de la neige fondante dehors. "
  "Lumière du matin qui entre par l'ouverture. Aucune personne, aucune "
  "inscription sur les caisses." + SANS_MOTS),
 # « Une petite salle d'attente d'institution financière, quatre chaises en
 #   rang et un guéridon. »
 # Refaite deux fois : la première version rendait trois chaises au lieu de
 # quatre — l'énoncé de la rangée `ok` en dit quatre, et l'élève compte — et
 # surtout une porte vitrée au fond dont le panneau de sortie affichait
 # « EXIT » en rouge et en anglais. La parade est le cadrage : le mur du fond
 # est plein, il n'y a plus de porte dans le champ.
 ('salle-attente-caisse', 'images', P_EX1, STYLE + " Une petite salle "
  "d'attente d'institution financière de quartier, cadrée face à un mur "
  "plein : exactement quatre chaises rembourrées grises alignées côte à côte "
  "contre ce mur clair, et un guéridon rond au bout de la rangée avec une "
  "plante verte. Moquette à motif discret, éclairage encastré. Aucune porte, "
  "aucune fenêtre, aucun panneau lumineux dans le champ. Aucune personne, "
  "aucune affiche au mur, aucune revue sur le guéridon." + SANS_MOTS),

 # ── Les cinq images du Défi 3, exercice 5 ─────────────────────────────
 # « Un carnet à spirale ouvert sur une table, un stylo posé en travers de la
 #   page. »
 ('carnet-a-spirale', 'images', P_EX3, STYLE + " Un petit carnet à spirale "
  "ouvert à plat sur une table de mélamine, un stylo à bille posé en travers "
  "de la page de droite. La page porte quelques lignes manuscrites qui ne sont "
  "que des traits d'encre gris entièrement illisibles, et un chiffre entouré "
  "réduit à un simple cercle. Lumière de fin de soirée par la fenêtre. Aucune "
  "personne, aucune main dans le cadre." + SANS_MOTS),
 # « Un cellulaire posé à plat, écran contre le bois, à côté d'un trousseau de
 #   clés. »
 ('cellulaire-a-plat', 'images', P_EX3, STYLE + " Un téléphone cellulaire posé "
  "à plat sur un comptoir de bois, **écran contre le comptoir**, de sorte "
  "qu'on n'en voit que le dos lisse et l'îlot de caméra. Un trousseau de trois "
  "clés à côté, et un bol de céramique au bord du cadre. Lumière rasante de "
  "fin de journée. Aucune personne, aucune main, aucun écran visible." + SANS_MOTS),
 # « Une carte de plastique coupée en deux, les deux moitiés retournées dans un
 #   petit bol. »
 ('carte-coupee', 'images', P_EX3, STYLE + " Un petit bol de céramique blanche "
  "posé sur une table de mélamine, contenant les deux moitiés d'une carte de "
  "plastique coupée en diagonale, **posées face contre le fond du bol** : on "
  "n'en voit que le dos uni et la tranche du plastique. Une paire de ciseaux "
  "de cuisine posée à côté du bol. Lumière de plafonnier. Aucune personne, "
  "aucune main, aucune puce ni bande visible." + SANS_MOTS),
 # « Une boîte aux lettres de métal fixée près d'une porte, la neige fondue sur
 #   le perron. »
 ('boite-aux-lettres', 'images', P_EX3, STYLE + " Une boîte aux lettres de "
  "métal peint fixée au revêtement de vinyle, à droite d'une porte d'entrée de "
  "maison québécoise, sur un perron de béton où la neige fond en plaques. Son "
  "couvercle est légèrement entrouvert, rien n'en dépasse. Fin d'hiver, ciel "
  "couvert. Aucune personne, aucun numéro civique lisible, aucune "
  "inscription." + SANS_MOTS),
 # « Un poste de travail vu de loin, un casque d'écoute posé sur une cloison
 #   basse. »
 # Refaite : la première version montrait un téléphone de bureau et aucun
 # casque d'écoute — le thème du module (un centre d'appels) à la place de ce
 # que dit l'énoncé. C'est le quatrième défaut, et il ne s'est vu qu'avec la
 # phrase à côté de la photo. Le prompt refait fait du casque le sujet.
 ('poste-de-securite', 'images', P_EX3, STYLE + " Premier plan net sur un "
  "casque d'écoute noir à deux oreillettes, avec sa perche de micro, posé à "
  "cheval sur le rebord d'une cloison de bureau basse et grise. Derrière, "
  "flous, un fauteuil de bureau vide tourné de côté et un écran éteint vu de "
  "profil, dans une aire de travail ouverte. Éclairage de plafond uniforme. "
  "Aucune personne, aucun téléphone, aucune image ni interface sur "
  "l'écran." + SANS_MOTS),

 # ── Les trois photos du banc de vocabulaire ───────────────────────────
 # « un relevé de compte » — « Le relevé de compte est resté trois jours sur la
 #   table de la cuisine, plié en trois. »
 ('releve-de-compte', 'vocab', P_VOC, STYLE + " Une petite pile de trois ou "
  "quatre feuilles agrafées, posée debout **sur la tranche** contre un pot de "
  "céramique, sur une table de cuisine : on voit l'épaisseur du papier et "
  "l'agrafe, jamais la face imprimée. Une enveloppe ouverte à plat à côté. "
  "Lumière de fin de journée. Aucune personne, aucune ligne de texte "
  "visible." + SANS_MOTS),
 # « un prêt personnel » — « Le prêt personnel se termine au quatre-vingtième
 #   versement, et la date est au contrat. »
 ('pret-personnel', 'vocab', P_VOC, STYLE + " Un petit bureau fermé "
  "d'institution financière de quartier, vu depuis la porte : une table claire, "
  "un fauteuil vide derrière, une chaise visiteur devant, une chemise "
  "cartonnée fermée au centre de la table et un écran d'ordinateur **éteint, "
  "tourné de profil** vers la cloison. Cloison vitrée derrière, lumière du "
  "matin. Aucune personne, aucun papier ouvert, aucune affiche." + SANS_MOTS),
 # « l'hameçonnage » — « Le message annonçait une carte bloquée et demandait de
 #   cliquer : c'était de l'hameçonnage. »
 ('hameconnage', 'vocab', P_VOC, STYLE + " Un ordinateur portable ouvert sur "
  "une table de cuisine, **vu de dos** : on n'aperçoit que le dos de l'écran "
  "et le bord du clavier, l'affichage est entièrement hors champ. La lueur "
  "bleutée de l'écran éclaire le mur derrière. Une tasse froide et un "
  "trousseau de clés à côté. Pièce sombre, tard le soir. Aucune personne, "
  "aucune main, aucune interface visible." + SANS_MOTS),
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
