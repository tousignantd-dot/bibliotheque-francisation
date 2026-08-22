#!/usr/bin/env python3
"""Génère les 20 images de module-n2-secretaire.

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer,
    telles que rendues ;
  · `vocab/`  — les quatorze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdait le tiers du haut et du bas. Voir
`docs/chantier-tous-niveaux.md`.

**L'appel réseau passe par `build/route_images.py`**, jamais par fal.ai en
dur : la route Google directe coûte 0,0336 $ et répond en 3,9 s, fal.ai
0,080 $ en 14,5 s, WaveSpeed 0,070 $ en 25,9 s — les trois revendent le même
modèle. `generer_image` les essaie dans l'ordre du prix et rend le nom de
celle qui a servi ; ce nom est écrit dans le journal .json adjacent, pour
qu'un repli ne passe jamais inaperçu.

**La racine du dépôt se déduit de `__file__`**, et non d'un chemin absolu
écrit en dur comme dans les générateurs plus anciens : ce module a été produit
dans un *worktree* git, où le chemin absolu aurait déposé les images dans une
autre copie du dépôt.

La difficulté propre à ce module est le **texte**. Un centre de formation est
couvert d'écriture : numéros de local, horaires, avis affichés, plaques de
porte. Or le générateur ne sait pas écrire, et un mot déformé sur une photo se
lit comme une faute. Tous les prompts demandent donc la même chose : les
papiers et les plaques restent **hors foyer**, l'écriture se lit comme des
traits gris. Les vrais mots, l'élève les lit dans les bandeaux noirs des
exercices — l'horaire du secrétariat et l'avis de la porte y sont écrits en
toutes lettres.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n2-secretaire/gen_images.py
  python3 build/contenu/module-n2-secretaire/gen_images.py lieu-couloir
"""
import io, json, pathlib, sys, time

MODULE = 'module-n2-secretaire'
RACINE = pathlib.Path(__file__).resolve().parents[3]
GEN  = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))  # build/
from route_images import generer_image, ESTIMATIONS

SANS = ("Aucun texte lisible, aucun mot déchiffrable, aucune écriture "
        "reconnaissable, aucun chiffre lisible, aucun nom, aucun logo, aucune "
        "marque, aucun filigrane, aucun visage, aucune personne identifiable — "
        "les personnes, s'il y en a, sont vues de dos ou cadrées sans le "
        "visage. L'écriture imprimée, les plaques et les affiches, quand il y "
        "en a, se lisent comme des traits gris flous, hors foyer.")

# Le décor principal : un centre de formation pour adultes, à Montréal.
CENTRE = ("Photographie réaliste, format paysage, lumière du jour par de "
          "grandes fenêtres. Un centre de formation pour adultes au Québec : "
          "murs clairs, sol de tuiles, portes de bois pâle, éclairage au "
          "plafond. Bâtiment public ordinaire, propre et sans luxe. Palette "
          "sobre et neutre. " + SANS)

# Ce qui se photographie de près, à hauteur de main.
PRES = ("Photographie réaliste, format paysage, vue rapprochée en lumière "
        "naturelle douce, faible profondeur de champ, palette neutre. " + SANS)

P_EX  = "Je découvre · Exercice 3 — Où est-ce, dans le centre ?"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('lieu-secretariat', 'images', P_EX, CENTRE + " Le comptoir d'accueil du "
  "secrétariat, vu de trois quarts : un long comptoir de mélamine claire, une "
  "chaise derrière, un classeur et une plante verte, une petite cloche sur le "
  "dessus. Personne au premier plan."),
 ('lieu-couloir', 'images', P_EX, CENTRE + " Un couloir vu en enfilade, "
  "portes de classe fermées de chaque côté, plaques de numéro floues à côté "
  "de chaque porte, un banc contre le mur, le plafond éclairé au loin."),
 ('lieu-escalier', 'images', P_EX, CENTRE + " Une cage d'escalier intérieure "
  "vue d'en bas : marches de béton, rampe de métal, palier à mi-hauteur, "
  "lumière naturelle venant d'une fenêtre haute."),
 ('lieu-classe', 'images', P_EX, CENTRE + " Une salle de classe vide vue "
  "depuis la porte : rangées de tables et de chaises, un grand tableau blanc "
  "au fond, une horloge ronde au mur sans chiffres lisibles."),
 ('lieu-entree', 'images', P_EX, "Photographie réaliste, format paysage, "
  "lumière du jour. La porte d'entrée vitrée d'un bâtiment public de "
  "Montréal, vue de l'intérieur du hall : double porte de métal et de verre, "
  "un tapis d'entrée, la rue et les arbres visibles dehors, hors foyer. "
  + SANS),
 ('lieu-avis', 'images', P_EX, PRES + " Gros plan sur une feuille de papier "
  "blanche fixée avec du ruban adhésif sur une porte de bois pâle fermée, la "
  "feuille légèrement de biais, son texte entièrement flou et illisible, la "
  "poignée de porte visible en bas du cadre."),

 # ── Les quatorze photos du banc de vocabulaire ────────────────────────
 ('secretariat', 'vocab', P_VOC, CENTRE + " Le bureau du secrétariat vu "
  "depuis le couloir par une porte ouverte : un comptoir, deux classeurs, un "
  "écran d'ordinateur éteint, des tablettes de dossiers."),
 ('secretaire', 'vocab', P_VOC, CENTRE + " Une personne assise derrière un "
  "comptoir d'accueil, vue de dos et de trois quarts, cadrée aux épaules sans "
  "le visage, la main posée sur un clavier, des piles de papiers à côté."),
 ('concierge', 'vocab', P_VOC, CENTRE + " Une personne en vêtement de travail "
  "bleu, vue de dos dans un couloir, poussant un chariot d'entretien avec un "
  "balai et un seau, un trousseau de clés à la ceinture."),
 ('enseignante', 'vocab', P_VOC, CENTRE + " Une personne debout devant un "
  "grand tableau blanc dans une salle de classe, vue de dos, un marqueur à la "
  "main, des tables vides devant elle, le tableau couvert de traits gris "
  "illisibles."),
 ('couloir', 'vocab', P_VOC, CENTRE + " Un long couloir vide et lumineux, "
  "portes fermées de chaque côté, sol de tuiles brillant, perspective en "
  "fuite vers une fenêtre au fond."),
 ('rez-de-chaussee', 'vocab', P_VOC, CENTRE + " Le hall du rez-de-chaussée "
  "vu depuis le pied de l'escalier : la porte d'entrée vitrée d'un côté, le "
  "comptoir d'accueil de l'autre, un tapis, quelques chaises contre le mur."),
 ('etage', 'vocab', P_VOC, CENTRE + " Le palier d'un étage vu depuis "
  "l'escalier : la rampe de métal au premier plan, un couloir qui part vers "
  "la droite, une grande fenêtre au fond."),
 ('local', 'vocab', P_VOC, PRES + " Une porte de classe fermée, en bois pâle, "
  "vue de face, avec une petite plaque rectangulaire à côté du cadre — la "
  "plaque est nette comme objet mais son inscription reste entièrement floue "
  "et illisible."),
 ('comptoir', 'vocab', P_VOC, PRES + " Vue rapprochée du dessus d'un comptoir "
  "d'accueil de mélamine claire : une petite cloche métallique, un pot à "
  "crayons, un présentoir à feuillets vide, le bord du comptoir en diagonale."),
 ('attestation', 'vocab', P_VOC, PRES + " Une feuille de papier blanche posée "
  "à plat sur un comptoir clair, vue légèrement en plongée, son texte "
  "entièrement flou et illisible, un stylo posé en travers à côté."),
 ('horaire', 'vocab', P_VOC, PRES + " Une feuille imprimée en forme de "
  "tableau, fixée sur un mur clair, vue de face : on distingue nettement la "
  "grille de lignes et de colonnes, mais aucun mot ni aucun chiffre n'est "
  "lisible."),
 ('avis', 'vocab', P_VOC, PRES + " Une feuille blanche collée avec quatre "
  "morceaux de ruban adhésif sur une vitre de porte, photographiée de face, "
  "le texte flou et illisible, le hall du bâtiment visible derrière la vitre."),
 ('direction', 'vocab', P_VOC, CENTRE + " Un bureau fermé vu depuis le "
  "couloir : porte de bois avec une vitre dépolie, une plaque floue à côté, "
  "de la lumière allumée derrière la vitre."),
 ('porte-fermee', 'vocab', P_VOC, CENTRE + " Une porte fermée au bout d'un "
  "couloir sombre, l'éclairage éteint autour, une petite affiche floue collée "
  "à hauteur des yeux, l'ensemble donnant l'impression que le bureau est "
  "fermé."),
]


def reduire(data, largeur=800, qualite=82):
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien."""
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
faits, sautes, echecs, cout = [], [], [], 0.0

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
    if dossier == 'vocab':
        try:
            data = reduire(data)
        except Exception as e:
            echecs.append('%s : réduction impossible (%s) — image brute gardée'
                          % (etiquette, e))

    base = '%s_%s-%s_%s' % (MODULE, dossier, nom, horodatage)
    (GEN / (base + '.jpg')).write_bytes(brut)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "nano-banana-2",
        "prompt": prompt,
        "refs": [],
        "params": {"num_images": 1, "aspect_ratio": RATIO,
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": route,
        "cost_estimate_usd": ESTIMATIONS.get(route, 0.08),
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation",
        "module": MODULE,
        "page": page,
        "destination": "assets/interactive/%s/%s/%s.jpg" % (MODULE, dossier, nom),
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(etiquette)
    cout += ESTIMATIONS.get(route, 0.08)
    print('  ✓ %-28s %6.1f Ko   %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s) · environ %.2f $'
      % (len(faits), len(sautes), len(echecs), cout))
for e in echecs:
    print('  !! ' + e)
