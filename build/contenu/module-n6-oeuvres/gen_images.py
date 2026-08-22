#!/usr/bin/env python3
"""Les 16 images de module-n6-oeuvres (niveau 6, activité 103).

Deux destinations :
  · `images/` — les six photos de l'exercice 5 de « Je découvre », réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les dix photos du banc de vocabulaire, réduites à 800 px
    qualité 82.

**Non exécuté au moment de la livraison du module** : les images coûtent de
l'argent réel et l'agent qui a produit le module n'était pas autorisé à les
générer. `node build/coherence.js module-n6-oeuvres` sort donc 16 écarts
« image absente du disque », tous attendus, et aucun autre.

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix mesuré le 21 août 2026 — Google direct,
puis fal.ai, puis WaveSpeed — rend le nom de celle qui a servi, et inscrit
chaque tentative au registre `~/Claude/generations/journal_appels.py`. Un
fournisseur facture des **appels**, pas des fichiers présents : une image
régénérée est payée chaque fois.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu écrit à la
main : ce fichier vit dans `build/contenu/<slug>/`, donc trois niveaux sous la
racine du dépôt. Les générateurs des modules les plus anciens portaient le
chemin en dur et cessaient de fonctionner dès qu'on travaillait dans un
worktree.

**Le sujet est le cinéma, donc l'écrit est partout** : affiches, génériques,
feuillets, pages de journal. Chaque prompt exige donc que toute ligne de texte
soit réduite à un trait gris. Une image où l'on peut lire un mot — un mot
d'anglais surtout — est à refaire. Deux interdits de plus, propres à ce
module : **aucune affiche de film reconnaissable et aucun titre d'œuvre
réelle**. Le film du module est inventé ; une image qui montrerait une vraie
affiche ferait entrer dans le module une œuvre que le texte n'a pas le droit
de citer.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n6-oeuvres/gen_images.py
  python3 build/contenu/module-n6-oeuvres/gen_images.py quai-novembre
  python3 build/contenu/module-n6-oeuvres/gen_images.py vocab/montage
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n6-oeuvres'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 5 — Le mercredi soir, salle Beauchemin"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : une ville moyenne du Québec en novembre, lumière basse,
# rien de spectaculaire. Repris tel quel d'un module à l'autre, seule la
# palette change quand le thème l'exige — ici, elle est volontairement froide.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle basse de "
         "fin d'automne, faible profondeur de champ. Ville moyenne du Québec, "
         "intérieurs et extérieurs ordinaires, palette sobre et froide. Aucun "
         "texte lisible, aucun mot déchiffrable, aucun logo, aucune marque, "
         "aucun filigrane, aucune personne identifiable, aucun visage "
         "reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie ordinaire au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts "
        "arrière ou hors cadrage du visage. Lumière naturelle douce, faible "
        "profondeur de champ. Aucun visage reconnaissable, aucun texte, aucun "
        "logo, aucun filigrane.")

# Le sujet du module oblige à ces deux phrases : la moitié des images contient
# du texte imprimé ou projeté, et un modèle d'image écrit volontiers de
# l'anglais. La seconde interdit toute affiche de film reconnaissable — le film
# du module est inventé, et le rester.
SANS_MOTS = (" Strictly no letters, no words, no readable characters anywhere "
             "in the image: every line of text, including any headline, title "
             "or label, must be an abstract grey stroke. Aucun mot d'anglais "
             "nulle part.")

SANS_AFFICHE = (" Aucune affiche de film reconnaissable, aucun titre d'œuvre, "
                "aucune jaquette identifiable : tout ce qui ressemblerait à "
                "une affiche est uni ou entièrement flou.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 5 ────────────────────────────────────
 ('salle-cineclub', 'images', P_EX, STYLE + " L'intérieur d'une petite salle de "
  "projection de quartier avant la séance : cinq ou six rangées de fauteuils de "
  "velours usé, un écran blanc éteint au fond, une allée centrale, les lumières de "
  "service encore allumées. Aucune personne, aucune inscription." + SANS_MOTS
  + SANS_AFFICHE),
 ('table-entree', 'images', P_EX, STYLE + " Une table pliante à l'entrée d'une salle "
  "communautaire : deux piles de feuilles imprimées, une petite boîte à monnaie de "
  "métal, un stylo, une chaise vide derrière. Les feuilles montrent une disposition de "
  "texte — un titre, des paragraphes — mais chaque ligne est un trait gris entièrement "
  "illisible." + SANS_MOTS + SANS_AFFICHE),
 ('maison-bord-eau', 'images', P_EX, STYLE + " Une maison de bois à un étage, volets "
  "fermés, au bord d'un fleuve gris, en novembre. Herbe jaunie, ciel bas, aucune "
  "lumière aux fenêtres. Aucune personne, aucune enseigne." + SANS_MOTS),
 ('quai-novembre', 'images', P_EX, STYLE + " Un quai de village en bois et en béton, "
  "battu par le vent, avec ses pneus d'amarrage noirs suspendus au bord et une corde "
  "enroulée sur un taquet. Eau grise agitée, ciel couvert. Aucune personne, aucun "
  "bateau nommé." + SANS_MOTS),
 ('salle-montage', 'images', P_EX, STYLE + " Une petite salle de montage vue de côté : "
  "deux écrans éteints ou montrant une image grise, une console avec des molettes, un "
  "casque d'écoute posé, et des boîtiers ronds de bobines empilés sur une étagère "
  "derrière. Aucune personne, aucune étiquette lisible." + SANS_MOTS + SANS_AFFICHE),
 ('journal-critique', 'images', P_EX, STYLE + " Un hebdomadaire local de papier, ouvert "
  "et posé à plat sur une table de cuisine à côté d'une tasse, à la page des "
  "spectacles : deux colonnes de texte séparées par un filet et une petite image carrée "
  "en haut à gauche. Toutes les lignes de texte sont des traits gris entièrement "
  "illisibles, et l'image carrée est un aplat gris." + SANS_MOTS + SANS_AFFICHE),

 # ── Les dix photos du banc de vocabulaire ─────────────────────────────
 ('cine-club', 'vocab', P_VOC, PERS + " Une dizaine de personnes assises en demi-cercle "
  "sur des chaises pliantes dans une petite salle, après une projection, vues de dos et "
  "de loin. L'écran est éteint au fond. Aucun visage cadré." + SANS_MOTS + SANS_AFFICHE),
 ('long-metrage', 'vocab', P_VOC, STYLE + " Un écran de projection blanc éclairé dans "
  "une salle obscure, vu depuis le fond, avec les silhouettes noires des dossiers de "
  "fauteuils au premier plan. L'écran ne montre qu'une lumière diffuse, aucune image "
  "identifiable." + SANS_MOTS + SANS_AFFICHE),
 ('bande-annonce', 'vocab', P_VOC, STYLE + " Gros plan sur un projecteur de cinéma "
  "ancien dans sa cabine, faisceau de lumière visible dans la poussière, bobine en "
  "place. Aucune personne, aucune inscription sur l'appareil." + SANS_MOTS),
 ('generique', 'vocab', P_VOC, STYLE + " Un écran de cinéma presque noir, à la toute "
  "fin d'une séance, sur lequel défilent des lignes claires très fines — chacune un "
  "simple trait clair, aucun caractère déchiffrable. Trois spectateurs de dos, en "
  "silhouette, au premier plan." + SANS_MOTS),
 ('scene', 'vocab', P_VOC, PERS + " Une cuisine ordinaire de maison ancienne, éclairée "
  "par une seule lampe, avec des boîtes de carton ouvertes sur le plancher et des "
  "armoires vidées. Une personne de dos, hors cadrage du visage, en train de plier du "
  "papier journal." + SANS_MOTS),
 ('retour-arriere', 'vocab', P_VOC, STYLE + " Une photographie ancienne en noir et blanc "
  "posée sur une table de bois à côté d'une enveloppe ouverte, la surface légèrement "
  "cornée. On distingue une silhouette floue sur la photographie, aucun visage net, "
  "aucune écriture lisible au dos." + SANS_MOTS),
 ('realisatrice', 'vocab', P_VOC, PERS + " Une personne vue de dos, debout dans une "
  "salle vide, en train de regarder un écran éteint, un carnet à la main. Le visage est "
  "hors cadrage et les pages du carnet sont couvertes de traits gris illisibles."
  + SANS_MOTS + SANS_AFFICHE),
 ('tournage', 'vocab', P_VOC, PERS + " Une petite équipe de tournage en extérieur au "
  "bord de l'eau, en novembre : une caméra sur trépied, un pied de projecteur, deux "
  "personnes de dos en manteau. Ciel gris, herbe jaunie. Aucun visage cadré, aucune "
  "inscription sur le matériel." + SANS_MOTS),
 ('montage', 'vocab', P_VOC, STYLE + " Gros plan sur une table de montage : des bandes "
  "de pellicule suspendues à des crochets, une paire de ciseaux, une loupe et un "
  "enrouleur métallique. Aucune personne, aucune étiquette lisible sur les boîtes."
  + SANS_MOTS),
 ('critique', 'vocab', P_VOC, STYLE + " Gros plan sur une page d'hebdomadaire local "
  "posée sur une table, montrant une colonne de texte surmontée d'un titre et suivie "
  "d'une ligne de signature. Toutes les lignes, titre compris, sont des traits gris "
  "entièrement illisibles. Un crayon posé en travers." + SANS_MOTS + SANS_AFFICHE),
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
    print('  ✓ %-24s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('   ✗ ' + e)
