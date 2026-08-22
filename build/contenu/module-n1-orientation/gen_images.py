#!/usr/bin/env python3
"""Les 20 images de module-n1-orientation.

Deux destinations :
  · `images/` — les six pictogrammes de l'exercice `prImg` « Le dessin dit
    quoi ? », réduits à 1200 px qualité 85 ;
  · `vocab/`  — les quatorze photos du banc de vocabulaire, réduites à 800 px
    qualité 82.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix mesuré le 21 août 2026 — Google direct,
puis fal.ai, puis WaveSpeed — et rend le nom de celle qui a servi, inscrit au
journal de chaque image. Le registre des appels compte les **tentatives**, pas
les fichiers : une image régénérée est payée chaque fois.

**La racine se déduit de `__file__`.** Ce fichier vit dans
`build/contenu/<slug>/` : `parents[2]` est `build/`, `parents[3]` le dépôt.
Aucun chemin absolu — un générateur qui en porte un ne tourne que sur le poste
où il a été écrit, et échoue en silence dans un worktree.

La contrainte propre à ce module, et elle est plus serrée qu'ailleurs
-------------------------------------------------------------------
Le sujet du module est **un mot écrit sur une porte**, et le générateur a
l'ordre de ne produire aucun texte lisible. La contradiction se règle par la
répartition :

- Les six images d'exercice sont des **pictogrammes seuls** — la silhouette
  d'homme et de femme, les couverts, l'adulte et l'enfant, la personne qui
  court vers une porte, la cigarette barrée, la flèche. Un pictogramme n'est
  pas du texte : c'est justement ce que l'exercice fait lire. Aucun mot ne
  doit apparaître dessus, sinon la réponse est donnée.
- Le **mot écrit**, lui, ne vient jamais d'une image : il vit dans les
  bandeaux noirs de `exos.js` et dans les exercices d'écriture, en HTML, où
  l'élève peut l'agrandir et où il ne dépend d'aucun rendu.
- Les quatorze photos du banc montrent **le lieu**, pas sa plaque : la salle à
  manger vide plutôt que le panneau CAFÉTÉRIA. Quand une photo doit montrer un
  panneau (poussez, tirez, défense de fumer), on demande la plaque de biais ou
  hors foyer, ou le geste plutôt que la plaque.

Aucune personne identifiable non plus : les silhouettes sont de dos, ou
cadrées aux mains.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée. Pour en
refaire une, effacer son fichier d'abord.

  python3 build/contenu/module-n1-orientation/gen_images.py
  python3 build/contenu/module-n1-orientation/gen_images.py picto-fleche
"""
import io, json, pathlib, sys, time

MODULE = 'module-n1-orientation'
ICI = pathlib.Path(__file__).resolve()
BUILD = ICI.parents[2]                      # …/build
RACINE = ICI.parents[3]                     # …/bibliotheque-francisation
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

# Trois décors, repris tels quels d'un prompt à l'autre pour que les vingt
# images se ressemblent assez pour tenir dans le même module.
SANS = ("Aucun texte lisible, aucun mot déchiffrable, aucune lettre, aucun "
        "chiffre, aucun logo, aucune marque, aucun filigrane, aucun visage, "
        "aucune personne identifiable — les personnes, s'il y en a, sont vues "
        "de dos ou cadrées sans le visage.")

# Le pictogramme lui-même : une plaque de signalisation, sans un seul mot.
PICTO = ("Illustration vectorielle nette, format paysage, une plaque de "
         "signalisation carrée photographiée de face et bien à plat sur un mur "
         "de blocs peints pâles. La plaque ne porte qu'un pictogramme : une "
         "silhouette blanche pleine sur fond uni, sans aucun mot, sans aucune "
         "lettre, sans aucun cadre de texte. Style de signalisation publique "
         "standard, lignes simples, contraste fort. " + SANS)

# Le décor du centre de formation, pour les photos du banc.
CENTRE = ("Photographie réaliste, format paysage, lumière de néons. Intérieur "
          "d'un centre de formation pour adultes au Québec : murs de blocs "
          "peints pâles, plancher de tuiles, portes de bois clair. Palette "
          "neutre et calme. " + SANS)

# Les endroits ouverts du rez-de-chaussée.
ENTREE = ("Photographie réaliste, format paysage, lumière du jour entrant par "
          "de grandes portes vitrées. Hall d'entrée d'un centre de formation "
          "pour adultes : sol de tuiles, mobilier simple, palette neutre. "
          + SANS)

P_EX = "Je découvre · Exercice 3 — Le dessin dit quoi ?"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les six pictogrammes de `prImg` ─────────────────────
 ('picto-toilettes', 'images', P_EX, PICTO + " Le pictogramme montre deux "
  "silhouettes debout côte à côte, l'une en pantalon et l'une en robe "
  "triangulaire, blanches sur fond bleu foncé."),
 ('picto-cafeteria', 'images', P_EX, PICTO + " Le pictogramme montre une "
  "fourchette et un couteau croisés, blancs sur fond bleu foncé."),
 ('picto-enfant', 'images', P_EX, PICTO + " Le pictogramme montre une grande "
  "silhouette d'adulte tenant par la main une petite silhouette d'enfant, "
  "blanches sur fond bleu foncé."),
 ('picto-sortie', 'images', P_EX, PICTO + " Le pictogramme montre une "
  "silhouette qui court vers l'ouverture rectangulaire d'une porte, avec une "
  "flèche, blanches sur fond vert franc."),
 ('picto-cigarette', 'images', P_EX, PICTO + " Le pictogramme montre une "
  "cigarette allumée dans un gros anneau rouge barré d'une large diagonale "
  "rouge, sur fond blanc."),
 ('picto-fleche', 'images', P_EX, PICTO + " Le pictogramme montre une seule "
  "flèche épaisse pointant vers la droite, blanche sur fond bleu foncé, rien "
  "d'autre sur la plaque."),

 # ── Je retiens des mots · les quatorze photos du banc ─────────────────
 ('panneau', 'vocab', P_VOC, CENTRE + " Une plaque de signalisation carrée "
  "vue de trois quarts, fixée au mur au-dessus d'une porte fermée, un peu "
  "hors foyer : on voit la forme de la plaque et sa fixation, pas ce qu'elle "
  "porte."),
 ('dessin', 'vocab', P_VOC, CENTRE + " Gros plan sur un pictogramme blanc "
  "sur fond bleu, une silhouette simple, occupant tout le cadre, sans aucun "
  "mot ni aucune lettre autour."),
 ('toilettes', 'vocab', P_VOC, CENTRE + " Une porte de toilettes publiques "
  "entrouverte au bout d'un corridor, laissant voir un mur de tuiles pâles et "
  "un lavabo, la plaque de porte floue."),
 ('cafeteria', 'vocab', P_VOC, ENTREE + " Une salle à manger de centre de "
  "formation vue du fond : tables rectangulaires et chaises légères, grandes "
  "fenêtres à gauche, salle vide."),
 ('fleche', 'vocab', P_VOC, CENTRE + " Une flèche directionnelle blanche "
  "peinte sur une plaque bleue fixée en hauteur dans un corridor, vue de "
  "légèrement en dessous, rien d'écrit à côté."),
 ('accueil', 'vocab', P_VOC, ENTREE + " Le hall d'entrée vu de la porte : "
  "comptoir d'accueil à droite, dessus dégagé, quelques chaises contre le "
  "mur, sol de tuiles clair."),
 ('service-de-garde', 'vocab', P_VOC, CENTRE + " Une petite salle de jeu "
  "pour enfants dans un bâtiment public : tapis de mousse aux couleurs "
  "douces, petites chaises basses, bacs de rangement, salle vide, aucune "
  "personne."),
 ('entree', 'vocab', P_VOC, ENTREE + " Les portes vitrées d'entrée vues de "
  "l'extérieur, une marche de béton devant, la lumière du jour sur le verre, "
  "personne dans le cadre."),
 ('sortie', 'vocab', P_VOC, ENTREE + " Des portes vitrées vues de "
  "l'intérieur, la lumière du jour derrière, barre horizontale d'ouverture au "
  "premier plan."),
 ('vestiaire', 'vocab', P_VOC, CENTRE + " Une rangée de crochets muraux avec "
  "trois manteaux d'hiver suspendus et des bottes alignées en dessous sur un "
  "tapis de caoutchouc, vue de trois quarts."),
 ('poussez', 'vocab', P_VOC, CENTRE + " Cadrage serré sur une main posée à "
  "plat sur la large plaque de métal brossé d'une porte, en train de pousser. "
  "On ne voit que la main et la porte, aucun visage."),
 ('tirez', 'vocab', P_VOC, CENTRE + " Cadrage serré sur une main qui saisit "
  "la poignée verticale de métal d'une porte de bois et la ramène vers elle. "
  "On ne voit que la main et la poignée, aucun visage."),
 ('defense-de-fumer', 'vocab', P_VOC, ENTREE + " Un cendrier de métal sur "
  "pied posé dehors, très loin des portes vitrées floues à l'arrière-plan, "
  "sous un ciel gris. Aucune cigarette allumée, aucune personne."),
 ('sortie-de-secours', 'vocab', P_VOC, CENTRE + " Une porte de métal peinte "
  "en vert avec une longue barre horizontale d'ouverture en travers, au bout "
  "d'un corridor, vue de face. Rien d'écrit dessus."),
]


def reduire(data, largeur, qualite):
    """L'image d'exercice occupe 223 x 132 px à l'écran, la photo du banc
    encore moins : la route Google rend des JPEG bien plus lourds que ça."""
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
