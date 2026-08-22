#!/usr/bin/env python3
"""Les 17 images de module-n1-inscription.

Deux destinations, deux réductions :
  · `images/` — les six photos de l'exercice `prImg` « Ce qu'on voit le jour
    de l'inscription », réduites à **1200 px / qualité 85** ;
  · `vocab/`  — les onze photos du banc de vocabulaire, réduites à
    **800 px / qualité 82**.

Les deux se réduisent, et c'est le point. Un générateur qui ne réduisait que
le banc laissait les images d'exercice sortir brutes de la route Google —
quatre mégaoctets à charger pour six vignettes de 223 x 132 px, sur des
appareils de niveau 1 qui sont souvent les plus modestes de l'école.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle. Une
image carrée y perd le tiers du haut et du bas.

**La racine se déduit de `__file__`, jamais d'un chemin absolu.** Ce fichier
vit dans `build/contenu/<slug>/` ; le dépôt est trois niveaux au-dessus.
Un chemin absolu écrit en dur envoie les images dans le dépôt principal quand
le générateur tourne depuis un arbre de travail git — elles n'arrivent jamais
dans la branche qui les attend, et rien ne le dit.

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix — Google direct, puis fal.ai, puis
WaveSpeed — et rend le nom de celle qui a servi, inscrit au journal de chaque
image.

Trois contraintes propres à ce module :

- **Aucun texte lisible nulle part, et surtout aucun chiffre.** Tout le module
  porte sur ce qui est écrit dans une case : un formulaire lisible sur une
  photo donnerait la réponse d'un exercice, et un numéro de téléphone lisible
  serait celui de quelqu'un. Les prompts le redisent chaque fois.
- **Aucun visage reconnaissable.** Les scènes avec quelqu'un le montrent aux
  mains, de dos ou hors cadrage. Une inscription est un moment administratif :
  personne n'a envie d'y être photographié.
- **Aucune pièce d'identité réelle.** Pas de passeport, pas de carte
  d'assurance maladie, pas de logo de gouvernement — même flous. Une carte
  générique sans inscription, ou rien.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée. Pour
en refaire une, effacer son fichier d'abord.

  python3 build/contenu/module-n1-inscription/gen_images.py
  python3 build/contenu/module-n1-inscription/gen_images.py case fiche
"""
import io, json, pathlib, sys, time

MODULE = 'module-n1-inscription'
RATIO = "3:2"

# build/contenu/<slug>/gen_images.py → trois parents jusqu'à la racine du
# dépôt, quel que soit l'arbre de travail où ce fichier se trouve.
ICI = pathlib.Path(__file__).resolve()
BUILD = ICI.parent.parent.parent            # …/build
RACINE = BUILD.parent                       # …/bibliotheque-francisation (ou l'arbre)
BASE = RACINE / 'assets/interactive' / MODULE
GEN = pathlib.Path.home() / 'Claude/generations'

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

# Deux décors, repris tels quels d'un prompt à l'autre pour que les
# dix-sept images se ressemblent assez pour tenir dans le même module.
CENTRE = ("Photographie réaliste, format paysage, intérieur d'un centre de "
          "formation pour adultes au Québec : murs clairs, mobilier simple et "
          "un peu daté, lumière naturelle de fenêtre. Faible profondeur de "
          "champ. Aucun texte lisible, aucune affiche lisible, aucun "
          "formulaire lisible, aucun chiffre lisible, aucun logo, aucun "
          "visage reconnaissable.")

MAISON = ("Photographie réaliste, format paysage, coin d'un appartement ou "
          "d'un vestibule d'immeuble ordinaire à Montréal : bois peint, "
          "lumière douce de fin de journée. Faible profondeur de champ. "
          "Aucun texte lisible, aucun chiffre lisible, aucune adresse "
          "lisible, aucun logo, aucun visage reconnaissable.")

P_EX = "Je découvre · Exercice 3 — Ce qu'on voit le jour de l'inscription"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les six photos de l'exercice ────────────────────────
 ('table-inscription', 'images', P_EX, CENTRE + " Une longue table pliante "
  "installée dans un couloir, avec deux chaises vides d'un côté, une pile de "
  "feuilles blanches et un pot de stylos. Vue de trois quarts, un matin. "
  "Personne à la table. Les feuilles sont vierges."),
 ('fiche-cases', 'images', P_EX, CENTRE + " Gros plan en plongée sur une "
  "feuille de papier blanche posée sur une table de bois clair, quadrillée de "
  "rectangles vides tracés au trait fin. Les cases sont entièrement vides et "
  "aucune étiquette n'est lisible."),
 ('main-stylo', 'images', P_EX, CENTRE + " Gros plan sur une main qui tient un "
  "stylo bleu au-dessus d'une feuille quadrillée de cases, prête à écrire. On "
  "ne voit que la main et l'avant-bras. La feuille reste vierge et illisible."),
 ('boite-lettres', 'images', P_EX, MAISON + " Une rangée de petites boîtes aux "
  "lettres métalliques dans l'entrée d'un immeuble, portes fermées, serrures "
  "rondes. Les numéros sont flous et illisibles. Aucune personne."),
 ('telephone-papier', 'images', P_EX, MAISON + " Un téléphone à écran noir posé face "
  "vers le bas à côté d'un carnet ouvert et d'un crayon, sur une table de "
  "cuisine. L'écran est éteint, la page du carnet est vierge."),
 ('ecran-courriel', 'images', P_EX, MAISON + " Un ordinateur portable ouvert sur une "
  "table, vu de biais et de loin, l'écran allumé mais entièrement flou et "
  "illisible, une tasse à côté. Aucune interface reconnaissable, aucun texte."),

 # ── Je retiens des mots · les onze photos du banc ───────────────────
 ('inscription', 'vocab', P_VOC, CENTRE + " Une file de trois personnes vues "
  "de dos, de loin, qui attendent devant une table d'accueil dans un couloir "
  "de centre de formation. Aucun visage visible, aucune affiche lisible."),
 ('fiche', 'vocab', P_VOC, CENTRE + " Une seule feuille de papier blanche "
  "posée seule au centre d'une table de bois clair, légèrement de biais, avec "
  "un stylo à côté. La feuille porte des lignes fines mais aucun mot lisible."),
 ('case', 'vocab', P_VOC, CENTRE + " Très gros plan sur un unique rectangle "
  "vide tracé au trait noir sur du papier blanc, occupant presque toute "
  "l'image. Rien n'est écrit dedans."),
 ('remplir', 'vocab', P_VOC, CENTRE + " Gros plan sur une main qui écrit au "
  "stylo dans un formulaire papier, vue de haut. On ne voit ni visage ni "
  "épaules, et l'écriture reste floue et indéchiffrable."),
 ('date-de-naissance', 'vocab', P_VOC, MAISON + " Un calendrier mural de papier "
  "vu de face, page ouverte sur une grille de jours, entièrement flou sauf le "
  "grain du papier. Aucun chiffre ni nom de mois lisible."),
 ('annee', 'vocab', P_VOC, MAISON + " Douze petits calendriers de bureau "
  "identiques alignés en rangée sur une étagère, vus de trois quarts. Aucun "
  "chiffre lisible, aucune inscription."),
 ('adresse', 'vocab', P_VOC, MAISON + " Une porte d'entrée de maison de "
  "briques avec une plaque de métal vissée à côté, la plaque volontairement "
  "hors de mise au point et illisible. Escalier extérieur au premier plan."),
 ('appartement', 'vocab', P_VOC, MAISON + " Un couloir d'immeuble avec quatre "
  "portes d'appartement identiques de chaque côté, moquette usée, éclairage "
  "jaune. Les numéros des portes sont flous. Aucune personne."),
 ('code-postal', 'vocab', P_VOC, MAISON + " Une enveloppe blanche posée seule "
  "sur une table de bois, vue en plongée, avec un timbre dans le coin. "
  "L'adresse écrite dessus est entièrement floue et illisible."),
 ('telephone', 'vocab', P_VOC, MAISON + " Un téléphone tenu à plat dans une "
  "main ouverte, écran éteint et noir, sur fond de table de cuisine. On ne "
  "voit que la main. Aucune marque, aucun logo, aucune interface."),
 ('courriel', 'vocab', P_VOC, MAISON + " Un clavier d'ordinateur portable vu "
  "de très près en plongée, touches grises, l'écran flou en haut de l'image. "
  "Aucune lettre lisible sur les touches, aucun texte à l'écran."),
]


def reduire(data, largeur, qualite):
    """Réduit l'image à la largeur voulue, en gardant ses proportions.

    Les deux dossiers y passent, avec deux réglages : l'image d'exercice
    occupe 223 x 132 px à l'écran et la photo du banc encore moins. La route
    Google directe rend des JPEG bien plus lourds que fal.ai — sans cette
    étape, six vignettes pèsent plusieurs mégaoctets.
    """
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert('RGB')
    hauteur = max(1, round(largeur * im.height / im.width))
    im = im.resize((largeur, hauteur), Image.LANCZOS)
    tampon = io.BytesIO()
    im.save(tampon, 'JPEG', quality=qualite, optimize=True)
    return tampon.getvalue()


# images/ 1200 px q. 85 · vocab/ 800 px q. 82
FORMATS = {'images': (1200, 85), 'vocab': (800, 82)}

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
        data = reduire(data, *FORMATS[dossier])
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
