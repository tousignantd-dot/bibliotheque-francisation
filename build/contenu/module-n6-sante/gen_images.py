#!/usr/bin/env python3
"""Les 18 images de module-n6-sante (niveau 6, activité 104).

Deux destinations :
  · `images/` — les six photos de l'exercice 4 de « Je découvre », réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les douze photos du banc de vocabulaire, réduites à 800 px
    qualité 82.

**Non exécuté au moment de la livraison du module** : les images coûtent de
l'argent réel et l'agent qui a produit le module n'était pas autorisé à les
générer. `node build/coherence.js module-n6-sante` sort donc 18 écarts
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

**Deux contraintes propres à ce module.**

1. *Aucune personne reconnaissable, et aucun corps montré.* Le sujet est un
   hôpital ; une photo de patient identifiable, même produite par un modèle,
   n'a pas sa place dans un matériel de classe. Les rares scènes habitées
   montrent des personnes de dos, de trois quarts arrière ou hors cadrage, et
   jamais un examen en cours.
2. *Aucun mot lisible.* Presque chaque image contient du papier imprimé — une
   convocation, un feuillet, une lettre — et un modèle d'image écrit volontiers
   de l'anglais dessus. Chaque prompt exige donc que toute ligne de texte soit
   réduite à un trait gris. Une image où l'on peut lire un mot est à refaire.

**Aucun nom d'établissement réel, aucun logo, aucune enseigne.** Un feuillet
ou une lettre qui porterait le nom d'un vrai hôpital serait un faux document ;
les scènes sont des lieux ordinaires et anonymes.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n6-sante/gen_images.py
  python3 build/contenu/module-n6-sante/gen_images.py salle-attente
  python3 build/contenu/module-n6-sante/gen_images.py vocab/prelevement
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n6-sante'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 4 — Les endroits d'une matinée à l'hôpital"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : un hôpital régional ordinaire d'une ville moyenne du
# Québec, lumière du matin, rien de spectaculaire et rien de dramatique.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle de fin "
         "d'avant-midi, faible profondeur de champ. Hôpital régional ordinaire "
         "d'une ville moyenne du Québec, intérieurs institutionnels sans luxe, "
         "palette sobre et froide. Aucun texte lisible, aucun mot "
         "déchiffrable, aucun logo, aucune marque, aucun filigrane, aucune "
         "personne identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène ordinaire dans un "
        "hôpital régional du Québec, avec une ou deux personnes vues de dos, "
        "de trois quarts arrière ou hors cadrage du visage. Lumière naturelle "
        "douce, faible profondeur de champ. Aucun visage reconnaissable, "
        "aucun corps dénudé, aucun soin en cours, aucun texte, aucun logo, "
        "aucun filigrane.")

# Le sujet du module oblige à cette phrase : presque toutes les images
# contiennent du papier imprimé, et un modèle d'image écrit volontiers de
# l'anglais dessus.
SANS_MOTS = (" Strictly no letters, no words, no readable characters anywhere "
             "in the image: every line of text, including any heading, label, "
             "sign or form field, must be an abstract grey stroke. Aucun mot "
             "d'anglais nulle part, aucun nom d'hôpital, aucune enseigne "
             "lisible.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 4 ────────────────────────────────────
 ('comptoir-clinique', 'images', P_EX, PERS + " Le comptoir d'accueil d'une "
  "clinique externe d'hôpital : un plan de travail stratifié, une vitre basse à "
  "deux postes, un petit lecteur de carte, un présentoir de dépliants aux "
  "couvertures unies, trois personnes qui attendent de dos, à distance l'une de "
  "l'autre. Mur institutionnel neutre." + SANS_MOTS),
 ('salle-attente', 'images', P_EX, PERS + " Une salle d'attente d'hôpital vue de "
  "l'entrée : des banquettes bleues alignées le long d'un mur, la moitié des "
  "places occupées par des adultes vus de dos, une horloge ronde au-dessus, un "
  "distributeur d'eau dans un coin. Éclairage au plafond, sol de tuiles pâles." + SANS_MOTS),
 ('bureau-consultation', 'images', P_EX, STYLE + " Un petit bureau de consultation "
  "vide : une table de travail avec un ordinateur, deux chaises face à face, une "
  "table d'examen recouverte de papier, un lavabo et un distributeur mural. "
  "Aucune personne, aucune affiche lisible au mur." + SANS_MOTS),
 ('poste-prelevement', 'images', P_EX, STYLE + " Un poste de prélèvement sanguin "
  "vide dans un laboratoire d'hôpital : un fauteuil à large accoudoir rabattable, "
  "un chariot à tiroirs, un support à tubes vides, une boîte de gants et des "
  "étiquettes vierges. Aucune personne, aucune aiguille visible, aucun sang." + SANS_MOTS),
 ('enveloppe-papiers', 'images', P_EX, STYLE + " Une enveloppe blanche ouverte et "
  "trois feuilles étalées sur une table de cuisine, en fin d'après-midi, à côté "
  "d'une tasse et d'un crayon. On distingue la disposition d'une lettre — en-tête, "
  "bloc d'adresse, paragraphes, liste à tirets, ligne de signature — mais chaque "
  "ligne est un trait gris entièrement illisible." + SANS_MOTS),
 ('corridor-liaison', 'images', P_EX, STYLE + " Un long corridor d'hôpital désert, "
  "sol de tuiles pâles, main courante le long du mur, portes numérotées sans "
  "chiffres lisibles, et tout au fond un petit bureau vitré éclairé. Perspective "
  "en fuite, aucune personne, aucune affiche lisible." + SANS_MOTS),

 # ── Les douze photos du banc de vocabulaire ───────────────────────────
 ('clinique-externe', 'vocab', P_VOC, STYLE + " L'entrée intérieure d'un service "
  "de clinique externe : une double porte vitrée, un banc vide, une plante. Le point "
  "de vue est bas, sous le panneau directionnel suspendu, qui est coupé par le bord "
  "supérieur du cadre : on n'en voit que la tranche et son support, jamais sa face "
  "écrite. Aucune personne." + SANS_MOTS),
 ('demande-de-consultation', 'vocab', P_VOC, STYLE + " Gros plan sur un formulaire "
  "imprimé posé sur un bureau, à moitié rempli à la main : des cases, deux "
  "colonnes et une signature manuscrite illisible. Toutes les lignes sont des "
  "traits gris entièrement illisibles. Un stylo repose à côté." + SANS_MOTS),
 ('medecine-interne', 'vocab', P_VOC, STYLE + " Un panneau directionnel suspendu "
  "dans un corridor d'hôpital, avec plusieurs lignes et des flèches, toutes les "
  "inscriptions étant des traits gris entièrement illisibles. Arrière-plan flou "
  "de couloir institutionnel." + SANS_MOTS),
 ('delai-attente', 'vocab', P_VOC, STYLE + " Une horloge murale ronde et blanche "
  "au-dessus d'une rangée de sièges vides, dans une salle d'attente d'hôpital. "
  "Lumière de fin d'avant-midi par une fenêtre latérale. Aucune personne, aucun "
  "chiffre lisible ailleurs que sur le cadran." + SANS_MOTS),
 ('dossier-medical', 'vocab', P_VOC, STYLE + " Gros plan sur un tiroir de classeur "
  "ouvert, rempli de chemises de carton beige aux onglets vierges, dans un bureau "
  "administratif d'hôpital. Une chemise est légèrement sortie. Aucune écriture "
  "lisible sur les onglets." + SANS_MOTS),
 ('malaise', 'vocab', P_VOC, PERS + " Une personne adulte assise seule au bord "
  "d'un lit, dans une chambre ordinaire, vue de dos et de loin, la tête baissée, "
  "les avant-bras sur les genoux, tôt le matin. Lumière grise par la fenêtre. Le "
  "visage est entièrement hors cadrage." + SANS_MOTS),
 ('fatigue-chronique', 'vocab', P_VOC, PERS + " Une personne adulte assise sur la "
  "dernière marche d'un escalier intérieur, vue de dos et de trois quarts "
  "arrière, un sac de travail posé à côté d'elle, une rampe de bois. Le visage "
  "est hors cadrage." + SANS_MOTS),
 ('proche-aidant', 'vocab', P_VOC, PERS + " Un homme âgé assis seul dans une "
  "salle d'attente d'hôpital, vu de trois quarts arrière, un manteau de femme "
  "plié sur ses genoux et un sac à main posé à côté de lui. Rangée de sièges "
  "vides autour. Le visage est hors cadrage." + SANS_MOTS),
 ('heures-de-visite', 'vocab', P_VOC, STYLE + " Gros plan sur un petit panneau "
  "rectangulaire fixé au mur à côté de portes battantes d'unité de soins : "
  "quatre lignes courtes et deux colonnes, toutes en traits gris entièrement "
  "illisibles. Un bouton-poussoir mural à côté." + SANS_MOTS),
 ('prelevement', 'vocab', P_VOC, STYLE + " Gros plan sur un support à tubes de "
  "laboratoire vides, aux bouchons de couleurs différentes, posé sur un comptoir "
  "blanc, avec une planche d'étiquettes vierges à côté. Aucune personne, aucune "
  "aiguille, aucun sang, aucune inscription lisible." + SANS_MOTS),
 ('effets-secondaires', 'vocab', P_VOC, STYLE + " Gros plan sur un feuillet "
  "imprimé plié en trois et posé à plat sur une table de cuisine, dont un "
  "paragraphe est entouré au crayon. Toutes les lignes sont des traits gris "
  "entièrement illisibles. Un verre d'eau au second plan, flou." + SANS_MOTS),
 ('feuillet-information', 'vocab', P_VOC, STYLE + " Une feuille imprimée de "
  "couleur bleu pâle, tenue par un aimant sur la porte d'un réfrigérateur de "
  "cuisine. On distingue des titres, une liste à tirets et un encadré, mais "
  "chaque ligne est un trait gris entièrement illisible." + SANS_MOTS),
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
    print('  ✓ %-28s %6.1f Ko  par %s' % (etiquette, len(data) / 1024, route),
          flush=True)

print()
print('%d produite(s), %d sautée(s), %d échec(s)'
      % (len(faits), len(sautes), len(echecs)))
for route, n in sorted(routes.items()):
    print('   · %-18s %d image(s)' % (route, n))
for e in echecs:
    print('   ✗ ' + e)
