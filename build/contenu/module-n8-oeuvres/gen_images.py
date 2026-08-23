#!/usr/bin/env python3
"""Les douze images de module-n8-oeuvres (niveau 8, activité 123).

Une seule destination, `images/` : les six photos de `t1img` (les objets de
la dernière scène de la télésérie) et les six de `t2img` (les lieux de la
nouvelle et du poème), réduites à 1200 px qualité 85.

**Aucune carte de vocabulaire n'a d'image**, et c'est un choix documenté dans
`fccards.js` : les dix-sept mots de ce module sont abstraits — une
interprétation, l'implicite, un jugement de valeur, une métaphore, un
argument. Leur donner une photo aurait mis derrière chaque mot une vue
générique de bibliothèque, c'est-à-dire le thème du module à la place de ce
que dit la carte. C'est le quatrième défaut de la relecture du 22 août 2026 ;
`module-n7-oeuvres` (116) n'avait illustré que quatre cartes sur dix-neuf pour
la même raison, et `module-n8-recherche` (119) cinq sur seize.

**Aucune image ne montre une œuvre.** Une couverture de livre, une affiche de
spectacle, une page de journal, un écran de télévision : tous portent du
texte, et le texte d'une œuvre se compose en HTML — c'est ce que font les
trois exercices de type `texte` du module. Les photos ne montrent donc que la
**scène autour** : le quai, la chaloupe, la cafétéria, le stationnement. C'est
la règle que l'activité 115 a formulée pour la publicité et que l'activité
116 a confirmée pour la littérature ; ici elle vaut une troisième fois, et
elle explique pourquoi ce module ne comporte aucun piège à charabia.

**Les quatre règles de prompt sont appliquées ici** (`CLAUDE.md`, « Les images
d'un module ») :

1. aucun texte lisible ;
2. pas de mains ni de visages en gros plan ;
3. un décor québécois nommé — l'Estrie, Sherbrooke, un lac de la
   Haute-Mauricie ;
4. **l'image montre ce que dit son énoncé** — chaque prompt est écrit à partir
   de la phrase exacte de la rangée `ok`, recopiée en commentaire au-dessus.

**La parade au texte parasite est le cadrage, jamais la négation.** Quatre
scènes de ce module portent des inscriptions par nature : la cafétéria
d'usine (tableau du menu, affiches de sécurité), l'atelier de fenêtres
(étiquettes de lots collées sur les châssis), le stationnement (plaques
d'immatriculation, panneaux) et la vignette d'auto sur un pare-brise. Chaque
prompt les sort du champ : le mur du menu est coupé par le bord supérieur,
les châssis sont vus par la tranche, les plaques sont sous la neige, et la
vignette est du côté déjà gratté, hors cadre.

**Aucune image ne comporte de personne.** La règle « un prompt qui met plus
d'une personne doit dire qui elles sont » ne s'applique donc pas ici : les
douze énoncés décrivent des lieux et des objets vides, ce qui est aussi ce que
disent les deux œuvres — une femme seule sur un quai, une salle qui se vide.

Le contrôle avant livraison :

    node build/contexte_images.js module-n8-oeuvres

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix et inscrit chaque tentative au registre
`~/Claude/generations/journal_appels.py`.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu : ce fichier
vit dans `build/contenu/<slug>/`, donc trois niveaux sous la racine — sans
quoi il cesserait de fonctionner dans un worktree.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n8-oeuvres/gen_images.py
  python3 build/contenu/module-n8-oeuvres/gen_images.py quai-lumiere
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n8-oeuvres'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX1 = "Défi 1 · Exercice 6 — Les objets de la dernière scène"
P_EX2 = "Défi 2 · Exercice 6 — Les lieux des deux textes"

# Le style commun. Deux mondes dans ce module : un lac de la Haute-Mauricie à
# la fin de l'automne pour la télésérie, l'Estrie industrielle et enneigée
# pour la nouvelle et le poème. « Chalet moderne » et « usine lumineuse »
# sortent génériques américains : c'est exactement ce qu'on évite.
LAC = ("Photographie réaliste, format paysage, faible profondeur de champ. "
       "Un lac de la Haute-Mauricie à la fin de l'automne, avant la neige : "
       "épinettes noires et bouleaux dénudés, eau sombre et immobile, bois "
       "gris fendillé, tôle et aluminium ternis, feuilles mortes mouillées. "
       "Lumière de fin de jour, bleutée, sans soleil. Palette sourde. Aucune "
       "personne, aucun animal.")

ESTRIE = ("Photographie réaliste, format paysage, faible profondeur de champ. "
          "L'Estrie industrielle en janvier : brique rouge et tôle peinte, "
          "murs de blocs de béton peints en crème, planchers de béton scellé, "
          "châssis d'aluminium, mobilier ordinaire et un peu usé, restes de "
          "neige sale et de sel au bord de l'asphalte. Lumière de tubes "
          "fluorescents ou lumière grise d'hiver. Palette sobre. Aucune "
          "personne.")

# La négation seule ne tient pas devant un objet qui porte des inscriptions :
# elle sert de filet, pas de parade. La parade est dans chaque prompt, et
# c'est le cadrage.
SANS_MOTS = (" Strictly no letters, no words, no digits and no readable "
             "characters anywhere in the image: every piece of text — sign, "
             "menu board, safety placard, label, sticker, licence plate, "
             "book cover, poster, newspaper, screen or gauge marking — must "
             "fall outside the frame, be turned away, be buried under snow, "
             "or be an abstract grey stroke. Aucun mot d'anglais nulle part, "
             "aucune enseigne lisible, aucun logo, aucun filigrane.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── t1img · les objets de la dernière scène des « Eaux basses » ───────
 # « Un quai de bois sur un lac, à la nuit tombante, une lampe allumée au
 #   bout. »
 ('quai-lumiere', 'images', P_EX1, LAC + " Un quai de bois gris qui s'avance "
  "d'une quinzaine de pieds sur un lac parfaitement calme, photographié depuis "
  "la berge dans l'axe des planches. Au bout du quai, une petite lampe montée "
  "sur un poteau court est **allumée** et pose un halo jaune sur les planches "
  "mouillées et sur l'eau noire. Le ciel est bleu nuit, la ligne d'épinettes "
  "de l'autre rive n'est plus qu'une silhouette. Aucune embarcation amarrée, "
  "aucune personne, aucun panneau, aucun numéro sur le poteau." + SANS_MOTS),
 # « Une chaloupe d'aluminium retournée sur la berge, la coque vers le ciel. »
 ('chaloupe-retournee', 'images', P_EX1, LAC + " Une chaloupe d'aluminium "
  "ancienne, bosselée et ternie, **retournée quille en l'air** sur deux "
  "billots, à trois pas de l'eau, sur une berge de galets et de feuilles "
  "mortes. On voit toute la longueur de la coque en légère contre-plongée ; "
  "les bancs et l'intérieur ne sont pas visibles. Rivets apparents, traces "
  "d'algue séchée sur le bordé. Les numéros d'immatriculation de la coque sont "
  "hors du cadre, coupés par le bord gauche. Aucune personne, aucun moteur "
  "visible." + SANS_MOTS),
 # « Une paire de bottes de caoutchouc vertes posées à côté de bottes de
 #   ville, sur un plancher de bois. »
 ('bottes-caoutchouc', 'images', P_EX1, LAC + " Vue en plongée sur un plancher "
  "de bois franc usé, près d'une porte : **une paire de bottes de caoutchouc "
  "vert foncé**, hautes, éraflées, la semelle boueuse, posées côte à côte ; "
  "**à côté d'elles, une paire de bottillons de ville en cuir brun**, propres, "
  "bien alignés. Rien d'autre dans le cadre qu'un coin de tapis de caoutchouc "
  "et une plinthe. Les deux paires sont vides ; aucun pied, aucune main, "
  "aucune personne. Aucun logo, aucune marque sur les bottes." + SANS_MOTS),
 # « Une corde enroulée en huit autour d'un taquet de métal vissé sur un
 #   quai. »
 ('taquet-corde', 'images', P_EX1, LAC + " Cadrage rapproché, en plongée, sur "
  "un **taquet d'amarrage** en métal galvanisé vissé dans une planche de quai "
  "grise : une corde de nylon blanchie y est **enroulée en huit**, deux tours "
  "bien serrés, le brin libre pendant vers l'eau. Les planches sont mouillées "
  "et fendillées, quelques aiguilles d'épinette collées dessus. Le reste du "
  "quai est flou. Aucune main, aucune personne, aucune étiquette ni "
  "marquage sur le métal." + SANS_MOTS),
 # « La cuisine d'un chalet des Cantons-de-l'Est, une table de bois, une lampe
 #   allumée, personne. »
 ('cuisine-chalet', 'images', P_EX1, LAC + " L'intérieur de la cuisine d'un "
  "vieux chalet de bois : murs de planches verticales vernies, armoires de "
  "mélamine des années soixante-dix, un évier sous une fenêtre noire de nuit, "
  "une **table de bois massif** au centre avec quatre chaises dépareillées. "
  "Une **lampe suspendue est allumée** au-dessus de la table et laisse les "
  "coins de la pièce dans l'ombre. Une tasse et un torchon sur le comptoir. "
  "La pièce est **vide** : aucune personne. Le babillard et le calendrier "
  "habituels sont hors champ, coupés par le bord ; aucun papier, aucune "
  "étiquette visible." + SANS_MOTS),
 # « Un chemin de terre entre les épinettes, l'auto stationnée au bout,
 #   portière fermée. »
 ('chemin-chalet', 'images', P_EX1, LAC + " Un chemin de terre étroit et "
  "creusé d'ornières, entre deux murs d'épinettes noires, photographié dans "
  "son axe. Au bout, à une trentaine de mètres, **une berline ordinaire est "
  "stationnée de trois quarts arrière, toutes portières fermées**, éteinte. "
  "Feuilles mortes et flaques dans les ornières, fin de jour bleutée. La "
  "plaque d'immatriculation est hors du cadre, coupée par l'angle de la "
  "voiture ; aucun logo de marque discernable. Aucune personne." + SANS_MOTS),

 # ── t2img · les lieux de la nouvelle et du poème ──────────────────────
 # « Une cafétéria d'usine aux tables longues et aux chaises de plastique,
 #   vide, éclairée au néon. »
 # Refaite : la première version portait un tableau de menu en charabia et
 # deux affiches de sécurité sur le mur de gauche. « Coupé par le bord
 # supérieur » ne suffisait pas — le modèle a rempli les murs latéraux. Le
 # prompt refait **descend l'appareil au niveau des tables** et ne laisse
 # entrer aucun mur : il n'y a plus de surface où écrire quoi que ce soit.
 ('cafeteria-usine', 'images', P_EX2, ESTRIE + " La cafétéria d'une usine, "
  "**complètement vide**, photographiée **à hauteur de table**, l'appareil "
  "posé sur une table du premier plan et dirigé dans l'axe des rangées : "
  "quatre **longues tables rectangulaires** de mélamine claire qui fuient vers "
  "le fond, bordées de **chaises de plastique moulé** orange et gris, sur un "
  "plancher de tuiles de vinyle usées. Le cadre ne contient que des tables, "
  "des chaises, le plancher et, tout en haut, la rangée de tubes fluorescents "
  "du plafond. **Aucun mur n'entre dans l'image** — ni à gauche, ni à droite, "
  "ni au fond, qui se perd dans le flou : il n'y a donc ni tableau de menu, ni "
  "affiche, ni distributrice, ni porte, ni fenêtre. Aucune "
  "personne." + SANS_MOTS),
 # « Une table pliante contre un mur de bloc de béton, deux chaises
 #   dépareillées, tout au fond d'une salle. »
 ('table-du-fond', 'images', P_EX2, ESTRIE + " Le fond d'une grande salle de "
  "cafétéria, vu de loin : contre un **mur de blocs de béton peints en "
  "crème**, une **table pliante** en mélamine, plus petite et plus basse que "
  "les autres, avec **deux chaises dépareillées** — l'une de plastique orange, "
  "l'autre de bois. Rien dessus. Autour, le plancher est nu ; les autres "
  "tables sont hors champ ou floues au premier plan. Le mur est complètement "
  "nu, sans affiche ni prise de courant étiquetée. Aucune personne." + SANS_MOTS),
 # « Une nappe de papier blanche pliée en quatre, posée près d'un sac à main
 #   sur une table. »
 # Refaite : la première version rendait une feuille **dépliée**, marquée de
 # plis. L'énoncé dit « pliée en quatre », et l'exercice consiste justement à
 # reconnaître l'objet ; une feuille à plat le contredisait. Le prompt refait
 # décrit **l'épaisseur** — un rectangle de papier de quatre épaisseurs,
 # nettement plus petit qu'une feuille — plutôt que le pliage.
 ('nappe-papier', 'images', P_EX2, ESTRIE + " Cadrage rapproché sur le coin "
  "d'une table de cafétéria en mélamine : un **petit rectangle de papier "
  "blanc replié sur lui-même en quatre épaisseurs**, de la taille d'une main, "
  "compact, aux arêtes marquées, dont on voit distinctement la **tranche "
  "feuilletée** sur le côté — ce n'est pas une feuille à plat, c'est un paquet "
  "de papier plié. Il est posé contre **un sac à main de cuir brun usé**, "
  "fermé, couché sur le côté. Une miette ou deux sur la table. Lumière froide "
  "de fluorescent, arrière-plan flou. Le papier est **parfaitement vierge** : "
  "aucune impression, aucun motif, aucune écriture. Aucune main, aucune "
  "personne." + SANS_MOTS),
 # « Un atelier où des châssis de fenêtres attendent debout sur des chevalets
 #   de bois. »
 ('atelier-fenetres', 'images', P_EX2, ESTRIE + " L'intérieur d'un atelier de "
  "fabrication de portes et fenêtres : une rangée de **châssis de fenêtres en "
  "PVC blanc**, vitrés, **debout sur la tranche** dans des **chevalets de "
  "bois** à encoches, alignés en profondeur sur un plancher de béton scellé. "
  "Copeaux et poussière au sol, établi et serre-joints flous à droite, murs de "
  "tôle. Les châssis sont vus **par la tranche**, si bien que les étiquettes "
  "de lot collées sur les vitres ne sont pas dans le champ ; aucune affiche, "
  "aucun pictogramme sur les murs. Aucune personne." + SANS_MOTS),
 # « Un stationnement extérieur avant le lever du jour, les autos sous vingt
 #   centimètres de neige. »
 ('stationnement-neige', 'images', P_EX2, ESTRIE + " Un stationnement "
  "extérieur d'immeuble à logements, **avant le lever du jour** : une dizaine "
  "d'autos ordinaires **entièrement recouvertes d'une vingtaine de centimètres "
  "de neige fraîche**, dont on ne devine plus que les formes, alignées en épi. "
  "Deux lampadaires posent une lumière orange sur la neige ; le ciel est "
  "encore noir. Au fond, la façade de brique d'un triplex avec un escalier "
  "extérieur en colimaçon. Les plaques d'immatriculation et les numéros de "
  "case sont **sous la neige** ; aucun panneau de stationnement dans le cadre. "
  "Aucune personne." + SANS_MOTS),
 # « Un pare-brise couvert de givre, à moitié gratté du côté droit, vu de
 #   l'extérieur. »
 ('pare-brise-givre', 'images', P_EX2, ESTRIE + " Vue rapprochée, depuis "
  "l'extérieur et légèrement de côté, du **pare-brise d'une auto couvert de "
  "givre épais** : la **moitié droite est dégagée** en un rectangle net aux "
  "bords granuleux, la moitié gauche reste opaque et blanche. Sur le capot, "
  "un tas de neige repoussée. Un essuie-glace est **relevé**. L'habitacle "
  "derrière la partie dégagée est sombre et vide. Lumière bleue d'avant "
  "l'aube. La vignette d'immatriculation et tout autocollant sont hors du "
  "cadre. Aucune main, aucune gratte tenue, aucune personne." + SANS_MOTS),
]


def reduire(data, largeur, qualite):
    """L'image d'exercice occupe 223 x 132 px à l'écran.

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
        data = reduire(data, 1200, 85)
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
