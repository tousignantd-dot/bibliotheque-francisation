#!/usr/bin/env python3
"""Les 22 images de module-n5-ecole — « Régler une affaire au centre ».

Deux destinations :
  · `images/` — les six photos de l'exercice 3 « Ce qu'on voit dans un
    centre » (1200 px, qualité 85) ;
  · `vocab/`  — les seize photos du banc de vocabulaire (800 px, qualité 82).

**Aucun appel réseau en dur ici.** Le module importe `build/route_images.py`,
qui essaie les routes dans l'ordre du prix mesuré le 21 août 2026 — Google
direct, puis fal.ai, puis WaveSpeed — et rend le nom de celle qui a servi.
C'est aussi lui qui inscrit chaque tentative, réussie ou non, au registre
d'appels de `~/Claude/generations/journal_appels.py` : le mur compte des
appels, pas des fichiers présents.

**La difficulté propre à ce module : tout y est du papier.** Un formulaire, un
avis, un babillard, une attestation — et un modèle d'image qui voit du papier
écrit du faux texte dessus, illisible et laid. Les prompts demandent donc
partout des lignes grises floues plutôt que des mots, et la consigne « aucun
texte lisible, aucun mot déchiffrable » est répétée dans chacun d'eux. C'est
volontairement redondant : elle saute au premier prompt qui l'oublie.

Deuxième difficulté : un centre d'éducation des adultes est plein de monde, et
le module ne doit montrer personne d'identifiable. Toutes les scènes avec
présence humaine la cadrent de dos, de trois quarts arrière, ou aux mains
seules.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n5-ecole/gen_images.py
  python3 build/contenu/module-n5-ecole/gen_images.py avis formulaire

**Non exécuté au moment de la livraison du module** : les images coûtent de
l'argent réel et l'agent qui a produit le module n'était pas autorisé à les
générer. `node build/coherence.js module-n5-ecole` sort donc 22 écarts
« image absente du disque », tous attendus, et aucun autre.
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n5-ecole'
GEN = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 3 — Ce qu'on voit dans un centre"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Trois décors, repris tels quels d'un prompt à l'autre pour que les
# vingt-deux images se ressemblent. Le module est intérieur, institutionnel et
# banal : ni école privée lumineuse, ni bureau d'entreprise.
S_LIEU = ("Photographie réaliste, format paysage, intérieur d'un centre "
          "d'éducation des adultes ordinaire au Québec : murs pâles, "
          "plancher de tuiles, éclairage fluorescent doux, mobilier usé mais "
          "propre. Palette sobre, aucune scène spectaculaire. Aucun texte "
          "lisible, aucun mot déchiffrable, aucun logo, aucun filigrane, "
          "aucune personne identifiable, aucun visage reconnaissable. ")
S_PAPIER = ("Photographie réaliste, format paysage, lumière naturelle douce, "
            "faible profondeur de champ. Du papier de bureau ordinaire : on "
            "distingue des lignes grises, des cases et parfois un titre plus "
            "gras, mais l'écriture reste floue et illisible. Aucun texte "
            "lisible, aucun mot déchiffrable, aucun logo, aucun filigrane, "
            "aucune personne identifiable, aucun visage reconnaissable. ")
S_GENS = ("Photographie réaliste, format paysage, une ou deux personnes vues "
          "de dos, de trois quarts arrière ou hors cadrage du visage, "
          "intérieur institutionnel ordinaire au Québec, lumière douce, "
          "faible profondeur de champ. Aucun texte lisible, aucun mot "
          "déchiffrable, aucun logo, aucun filigrane, aucune personne "
          "identifiable, aucun visage reconnaissable. ")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 3 ────────────────────────────────────
 ('comptoir-secretariat', 'images', P_EX, S_GENS +
  "Un comptoir d'accueil vitré au fond d'un hall, avec une vitre coulissante "
  "et un petit passe-papiers. Deux personnes attendent de dos, à distance, "
  "derrière une ligne d'attente collée au sol. Plantes vertes fatiguées dans "
  "un coin."),
 ('porte-local-numero', 'images', P_EX, S_LIEU +
  "La porte fermée d'une salle de classe, vue de face dans un corridor : "
  "bois pâle, petite fenêtre rectangulaire à hauteur d'œil, et une plaque de "
  "métal vissée à côté du cadre. La plaque est nette mais unie, sans aucun "
  "caractère dessus."),
 ('formulaire-comptoir', 'images', P_EX, S_PAPIER +
  "Une feuille à cases posée à plat sur un comptoir de stratifié gris, un "
  "stylo bleu couché en travers, une agrafeuse noire à côté. Vue d'en haut, "
  "légèrement de trois quarts. Les cases sont visibles, les lignes de "
  "l'écriture sont de simples traits gris."),
 ('bureau-conseiller', 'images', P_EX, S_LIEU +
  "Un petit bureau fermé, vide de monde : une table de travail contre un mur, "
  "un écran d'ordinateur éteint, deux chaises droites placées devant la table "
  "pour des visiteurs, une fenêtre à store vénitien à moitié baissé. Un "
  "classeur de métal à quatre tiroirs dans le coin."),
 ('babillard-avis', 'images', P_EX, S_PAPIER +
  "Un grand babillard de liège dans un corridor, couvert de feuilles blanches "
  "épinglées de travers, plusieurs se chevauchant. Chaque feuille ne montre "
  "que des blocs de lignes grises floues. Vue de face, légèrement de biais."),
 ('telephone-message', 'images', P_EX, S_GENS +
  "Une personne debout dans une cage d'escalier vide, vue de dos, un "
  "téléphone tenu contre l'oreille droite, l'autre main dans la poche d'un "
  "manteau d'hiver. Marches de béton, rampe de métal, lumière froide."),

 # ── Les seize photos du banc de vocabulaire ───────────────────────────
 ('secretariat', 'vocab', P_VOC, S_LIEU +
  "Un comptoir d'accueil de bureau scolaire, vu de face à hauteur d'épaule : "
  "surface de stratifié, une clochette de service, un présentoir de "
  "brochures vide, une vitre à moitié ouverte. Personne derrière."),
 ('conseillere', 'vocab', P_VOC, S_GENS +
  "Une personne assise de trois quarts arrière à une table de travail, dans "
  "un petit bureau, la main posée sur un dossier ouvert. Deux chaises vides "
  "devant elle. Le visage est entièrement hors cadre."),
 ('local', 'vocab', P_VOC, S_LIEU +
  "L'intérieur vide d'une salle de classe d'adultes : rangées de tables "
  "individuelles, chaises de plastique, un tableau blanc effacé au fond, une "
  "fenêtre à droite. Aucune écriture sur le tableau."),
 ('session', 'vocab', P_VOC, S_LIEU +
  "Un calendrier mural de grand format accroché près d'une porte, montrant "
  "une grille de cases vides ; quelques cases sont marquées d'un trait de "
  "crayon rouge. Aucun chiffre ni mot lisible."),
 ('absence', 'vocab', P_VOC, S_LIEU +
  "Une chaise vide devant une table individuelle dans une salle de classe "
  "occupée, vue de derrière : les autres tables portent des cahiers fermés, "
  "celle du premier plan est nue. Aucune personne visible."),
 ('motif', 'vocab', P_VOC, S_PAPIER +
  "Gros plan sur une case rectangulaire d'un formulaire, plus haute que les "
  "autres, entourée d'un cadre net et restée vide. La pointe d'un stylo "
  "s'approche du coin gauche de la case."),
 ('piece-justificative', 'vocab', P_VOC, S_PAPIER +
  "Deux petits papiers de tailles différentes posés l'un sur l'autre sur une "
  "table de bois, l'un froissé, l'autre net avec un tampon rond encré au "
  "coin. Le tampon est un simple cercle d'encre, sans aucun caractère."),
 ('rattrapage', 'vocab', P_VOC, S_LIEU +
  "Une petite salle avec quatre tables rapprochées et deux chaises "
  "seulement, un cahier ouvert et un crayon sur l'une d'elles, la lumière du "
  "midi qui entre par une fenêtre. Aucune personne."),
 ('avis', 'vocab', P_VOC, S_PAPIER +
  "Une feuille officielle unique posée sur une table de cuisine, avec un "
  "bandeau plus foncé en haut, un bloc de lignes grises floues, et un espace "
  "vide en bas pour une signature. Une tasse au bord du cadre."),
 ('echeance', 'vocab', P_VOC, S_PAPIER +
  "Gros plan sur une feuille où une seule ligne, plus grasse que les autres, "
  "a été soulignée deux fois au crayon rouge. Le reste de la page est en "
  "lignes grises floues. Aucun mot n'est déchiffrable."),
 ('formulaire', 'vocab', P_VOC, S_PAPIER +
  "Une feuille à cases vue de face, à plat, occupant tout le cadre : une "
  "grille de rectangles vides séparés par des filets fins, avec un stylo "
  "posé en diagonale dans le coin inférieur droit."),
 ('prolongation', 'vocab', P_VOC, S_PAPIER +
  "Un calendrier de bureau ouvert sur une double page, deux cases éloignées "
  "reliées par une flèche tracée au crayon, et une flèche plus longue qui "
  "continue vers la droite hors de la page. Aucun chiffre lisible."),
 ('transfert', 'vocab', P_VOC, S_LIEU +
  "Un corridor où deux portes de salles de classe se font face, l'une "
  "ouverte sur une pièce éclairée, l'autre fermée. Vue centrée dans l'axe du "
  "corridor, personne dedans."),
 ('attestation', 'vocab', P_VOC, S_PAPIER +
  "Une feuille seule, à moitié sortie d'une fente sombre au bord gauche de "
  "l'image, posée sur un comptoir clair : aucun appareil, aucune façade, "
  "aucun panneau de commande, aucun nom de fabricant visible. On voit des "
  "blocs de lignes grises et un espace de signature en bas."),
 ('releve', 'vocab', P_VOC, S_PAPIER +
  "Une feuille tenue à deux mains devant une table, montrant un tableau à "
  "colonnes régulières avec des cases remplies de traits gris courts. Les "
  "mains sont vues de dessus, aucun visage dans le cadre."),
 ('delai', 'vocab', P_VOC, S_LIEU +
  "Une horloge murale ronde et blanche accrochée haut sur un mur de couloir "
  "beige, à côté d'une porte fermée. Le cadran est net mais sans chiffre, "
  "seulement des traits d'heures et deux aiguilles."),
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
    # La route Google directe rend des JPEG bien plus lourds que fal.ai. À
    # l'écran, l'image d'exercice occupe 223 x 132 px et la photo du banc
    # encore moins : les deux se réduisent, seulement pas au même format.
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
