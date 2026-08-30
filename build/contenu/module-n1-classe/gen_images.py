#!/usr/bin/env python3
"""Génère les 19 images de module-n1-classe.

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer
    « La salle de classe », réduites à 1200 px, qualité 85 ;
  · `vocab/`  — les treize photos du banc de vocabulaire, réduites à 800 px,
    qualité 82.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdait le tiers du haut et du bas. Voir
`docs/chantier-tous-niveaux.md`.

**L'appel réseau passe par `build/route_images.py`**, jamais par fal.ai en
dur : le module essaie Google en direct, puis fal.ai, puis WaveSpeed — l'ordre
du prix, les trois revendant le même modèle. `generer_image` rend le nom de la
route qui a servi, et ce nom est écrit dans le journal .json adjacent pour
qu'un repli ne passe jamais inaperçu.

**La racine du dépôt se déduit de `__file__`**, jamais d'un chemin absolu
écrit en dur : ce module a été produit dans un *worktree* git, où un chemin
absolu déposerait les images dans une autre copie du dépôt.

La difficulté propre à ce module est le **texte**, comme pour tous les modules
qui se passent dans un centre de formation : un tableau, un horaire affiché,
une page de livre sont couverts d'écriture, et le générateur ne sait pas
écrire. Tous les prompts demandent donc la même chose — les mots restent hors
foyer, l'écriture se lit comme des traits gris. Les vrais mots, l'élève les
lit dans les bandeaux noirs des exercices, où l'horaire du groupe est écrit en
toutes lettres.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n1-classe/gen_images.py
  python3 build/contenu/module-n1-classe/gen_images.py horloge
"""
import io, json, pathlib, sys, time

MODULE = 'module-n1-classe'
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
        "visage. L'écriture imprimée ou manuscrite, quand il y en a, se lit "
        "comme des traits gris flous, hors foyer.")

# Le décor principal : une salle de classe d'adultes, dans un centre de
# formation du Québec.
CLASSE = ("Photographie réaliste, format paysage, lumière du jour par de "
          "grandes fenêtres. Une salle de classe pour adultes dans un centre "
          "de formation du Québec : murs clairs, sol de tuiles, tables "
          "individuelles, chaises de plastique et de métal, éclairage au "
          "plafond. Salle ordinaire, propre et sans luxe. Palette sobre et "
          "neutre. " + SANS)

# Ce qui se photographie de près, à hauteur de main.
PRES = ("Photographie réaliste, format paysage, vue rapprochée en lumière "
        "naturelle douce, faible profondeur de champ, palette neutre. " + SANS)

P_EX  = "Je découvre · Exercice 3 — La salle de classe"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 ('salle-vide', 'images', P_EX, CLASSE + " La salle vue depuis la porte du "
  "fond : quatre rangées de tables et de chaises vides, le devant de la classe "
  "au loin, la lumière venant des fenêtres de gauche."),
 ('tableau-blanc', 'images', P_EX, CLASSE + " Un grand tableau blanc au mur du "
  "devant, vu de trois quarts, couvert de traits gris flous et illisibles, un "
  "porte-marqueurs en dessous, une table de travail au premier plan."),
 ('fenetre-classe', 'images', P_EX, CLASSE + " Une grande fenêtre de salle de "
  "classe entrouverte, vue de l'intérieur : la poignée nette au premier plan, "
  "des arbres et un stationnement flous dehors, un radiateur bas sous la "
  "fenêtre."),
 ('sac-sous-chaise', 'images', P_EX, PRES + " Vue en plongée sur le pied d'une "
  "chaise de classe : un sac à dos de toile posé par terre, entièrement sous "
  "l'assise de la chaise, le sol de tuiles autour."),
 ('livre-ouvert', 'images', P_EX, PRES + " Un livre ouvert à plat sur une table "
  "claire, vu du dessus légèrement de biais, un stylo posé en travers dans le "
  "creux des pages — le texte des deux pages est entièrement flou et "
  "illisible."),
 ('horaire-mur', 'images', P_EX, PRES + " Une feuille imprimée en forme de "
  "grille, fixée avec du ruban adhésif sur un mur clair à côté d'une porte de "
  "classe : on distingue nettement les lignes et les colonnes du tableau, mais "
  "aucun mot ni aucun chiffre n'est lisible."),

 # ── Les treize photos du banc de vocabulaire ──────────────────────────
 ('livre', 'vocab', P_VOC, PRES + " Un livre épais fermé, posé à plat sur une "
  "table de bois clair, vu de trois quarts : on voit la tranche et la "
  "couverture unie, sans aucun titre ni motif lisible."),
 ('stylo', 'vocab', P_VOC, PRES + " Un stylo à bille bleu posé seul sur une "
  "feuille blanche vierge, sur une table claire, vu de très près, le capuchon "
  "à côté."),
 ('chaise', 'vocab', P_VOC, CLASSE + " Une seule chaise de classe, en "
  "plastique et métal, vue de trois quarts devant une table vide, le reste de "
  "la salle flou derrière."),
 ('sac', 'vocab', P_VOC, PRES + " Un sac à dos de toile posé debout sur une "
  "chaise, fermeture éclair entrouverte, vu de face, dans une salle claire "
  "floue derrière."),
 ('porte', 'vocab', P_VOC, CLASSE + " La porte de la salle de classe, en bois "
  "pâle avec une petite vitre rectangulaire, vue de l'intérieur de la salle, "
  "entrouverte sur un couloir clair et flou."),
 ('horloge', 'vocab', P_VOC, PRES + " Une horloge murale ronde et blanche, "
  "accrochée haut sur un mur clair, vue de face — le cadran est net comme "
  "objet, mais les chiffres et les aiguilles restent flous et indistincts."),
 ('ecouter', 'vocab', P_VOC, CLASSE + " Une personne adulte assise à une table "
  "de classe, vue de dos et de trois quarts, cadrée aux épaules sans le "
  "visage, la tête légèrement tournée vers le devant de la salle, une main "
  "près de l'oreille."),
 ('regarder', 'vocab', P_VOC, CLASSE + " Deux personnes adultes assises côte à "
  "côte à des tables de classe, vues de dos, la tête levée vers le devant de "
  "la salle et le tableau flou au loin."),
 ('ouvrir', 'vocab', P_VOC, PRES + " Deux mains adultes, cadrées aux poignets "
  "seulement, en train d'ouvrir un livre posé sur une table claire — le livre "
  "est à moitié ouvert, ses pages entièrement floues."),
 ('fermer', 'vocab', P_VOC, PRES + " Une main adulte, cadrée au poignet, en "
  "train de rabattre la couverture d'un livre presque fermé posé sur une "
  "table claire, un sac à dos flou au fond."),
 ('midi', 'vocab', P_VOC, "Photographie réaliste, format paysage. Un couloir "
  "vitré de bâtiment public en plein soleil de la mi-journée, la lumière "
  "tombant à la verticale sur le sol de tuiles, quelques silhouettes floues "
  "vues de dos au loin, l'heure du jour rendue par la lumière seule. " + SANS),
 ('semaine', 'vocab', P_VOC, PRES + " Gros plan sur la grille d'un calendrier "
  "mural de papier accroché à un mur clair, vu de face : l'en-tête du mois et "
  "la rangée des noms de jours sont coupés par le bord supérieur du cadre. On "
  "ne voit que les cases carrées et les filets qui les séparent ; aucun mot, "
  "aucun nom de jour, aucune case cochée dans le champ."),
 ('horaire', 'vocab', P_VOC, PRES + " Une feuille imprimée en forme de tableau "
  "à deux colonnes, posée à plat sur une table claire à côté d'un stylo, vue "
  "en plongée : les lignes du tableau sont nettes, aucun mot n'est lisible."),
]


def reduire(data, largeur=800, qualite=82):
    """Les images du module se voient petites : 1024 px n'y sert à rien.

    Deux formats, parce que les deux usages ne sont pas les mêmes : l'image
    d'exercice occupe 223 x 132 px dans la zone de glisser-déposer mais peut
    s'agrandir au clic (1200 px, qualité 85) ; la photo du banc de vocabulaire
    ne s'agrandit jamais (800 px, qualité 82).
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
    try:
        data = reduire(data, *((800, 82) if dossier == 'vocab' else (1200, 85)))
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
