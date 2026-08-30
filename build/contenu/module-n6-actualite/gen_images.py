#!/usr/bin/env python3
"""Les 15 images de module-n6-actualite (niveau 6, activité 99).

Deux destinations :
  · `images/` — les six photos de l'exercice 4 de « Je découvre », réduites à
    1200 px qualité 85 ;
  · `vocab/`  — les neuf photos du banc de vocabulaire, réduites à 800 px
    qualité 82.

**Non exécuté au moment de la livraison du module** : les images coûtent de
l'argent réel et l'agent qui a produit le module n'était pas autorisé à les
générer. `node build/coherence.js module-n6-actualite` sort donc 15 écarts
« image absente du disque », tous attendus, et aucun autre.

**Aucun appel réseau en dur ici.** `generer_image` de `build/route_images.py`
essaie les routes dans l'ordre du prix mesuré le 21 août 2026 — Google direct,
puis fal.ai, puis WaveSpeed — rend le nom de celle qui a servi, et inscrit
chaque tentative au registre `~/Claude/generations/journal_appels.py`. Un
fournisseur facture des **appels**, pas des fichiers présents : une image
régénérée est payée chaque fois.

**La racine se déduit de `__file__`**, jamais d'un chemin absolu écrit à la
main : ce fichier vit dans `build/contenu/<slug>/`, donc trois niveaux sous la
racine du dépôt. Les générateurs des modules précédents portaient le chemin en
dur et cessaient de fonctionner dès qu'on travaillait dans un worktree.

**Le sujet est l'information écrite et parlée** : presque chaque image contient
du papier, un écran ou un micro. Chaque prompt exige donc que toute ligne de
texte soit réduite à un trait gris. Une image où l'on peut lire un mot — un mot
d'anglais surtout — est à refaire.

Relançable : une image déjà présente est sautée. Pour en refaire une, effacer
son fichier d'abord.

  python3 build/contenu/module-n6-actualite/gen_images.py
  python3 build/contenu/module-n6-actualite/gen_images.py laveuse-brisee
  python3 build/contenu/module-n6-actualite/gen_images.py vocab/enquete
"""
import io
import json
import pathlib
import sys
import time

MODULE = 'module-n6-actualite'
RACINE = pathlib.Path(__file__).resolve().parents[3]   # …/bibliotheque-francisation
BUILD = pathlib.Path(__file__).resolve().parents[2]    # …/build
GEN = pathlib.Path.home() / 'Claude' / 'generations'
BASE = RACINE / 'assets' / 'interactive' / MODULE
RATIO = "3:2"

sys.path.insert(0, str(BUILD))
from route_images import generer_image                       # noqa: E402

P_EX = "Je découvre · Exercice 4 — Où l'information se fabrique et où elle se lit"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# Le style commun : Trois-Rivières ordinaire, lumière naturelle, rien de
# spectaculaire. Repris tel quel d'un module à l'autre, seule la palette change
# quand le thème l'exige.
STYLE = ("Photographie réaliste, format paysage, lumière naturelle, faible "
         "profondeur de champ. Ville moyenne du Québec, intérieurs et rues "
         "ordinaires, palette sobre. Aucun texte lisible, aucun mot "
         "déchiffrable, aucun logo, aucune marque, aucun filigrane, aucune "
         "personne identifiable, aucun visage reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie ordinaire au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts "
        "arrière ou hors cadrage du visage. Lumière naturelle douce, faible "
        "profondeur de champ. Aucun visage reconnaissable, aucun texte, aucun "
        "logo, aucun filigrane.")

# Le sujet du module oblige à cette phrase : la moitié des images contient du
# texte imprimé ou affiché, et un modèle d'image écrit volontiers de l'anglais.
SANS_MOTS = (" Strictly no letters, no words, no readable characters anywhere "
             "in the image: every line of text, including any headline or "
             "label, must be an abstract grey stroke. Aucun mot d'anglais "
             "nulle part.")

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice 4 ────────────────────────────────────
 ('comptoir-bibliotheque', 'images', P_EX, STYLE + " Le comptoir d'accueil d'une "
  "petite bibliothèque municipale : un plan de travail de bois clair, deux piles de "
  "livres refermés à replacer, un chariot à roulettes à côté, des rayonnages flous en "
  "arrière-plan. Aucune personne. Les couvertures des livres sont unies, sans aucun "
  "titre." + SANS_MOTS),
 ('laveuse-brisee', 'images', P_EX, STYLE + " Une laveuse à chargement frontal, porte "
  "ouverte, dans une petite salle de lavage de sous-sol au plancher de béton peint. Le "
  "panier contient encore quelques centimètres d'eau grise et du linge mouillé. Un "
  "panier à linge de plastique posé à côté. Aucune personne, aucune inscription lisible "
  "sur le panneau de commande." + SANS_MOTS),
 ('radio-cuisine', 'images', P_EX, STYLE + " Un petit poste de radio de table, en "
  "plastique, posé au bout du comptoir d'une cuisine ordinaire, tôt le matin. Une tasse "
  "de café fume à côté. Lumière basse d'hiver par la fenêtre. Aucune personne, aucune "
  "inscription lisible sur le poste." + SANS_MOTS),
 ('studio-entrevue', 'images', P_EX, STYLE + " L'intérieur d'un petit studio de radio "
  "vu de côté : deux places face à face de chaque côté d'une table, chacune devant un "
  "micro sur bras articulé, deux casques d'écoute posés. Mur de mousse acoustique. "
  "Aucune personne, aucune inscription sur les micros ni sur la console." + SANS_MOTS),
 ('page-courrier', 'images', P_EX, STYLE + " Une page de journal de papier, pliée en "
  "deux et posée bien à plat sur une table de salle des employés, à côté d'une tasse. "
  "Elle porte une colonne de six courts blocs de texte séparés par des filets fins, "
  "chacun terminé par un trait plus court en italique. Chaque ligne est un trait gris "
  "abstrait ; aucun caractère isolé nulle part." + SANS_MOTS),
 ('ecran-documentaire', 'images', P_EX, STYLE + " Un écran de télévision dans un salon "
  "obscur, le soir, qui montre une image d'archives en noir et blanc : l'intérieur d'une "
  "usine ancienne, des machines et des courroies. Le reste de la pièce est sombre. "
  "Aucun sous-titre, aucune écriture à l'écran." + SANS_MOTS),

 # ── Les neuf photos du banc de vocabulaire ────────────────────────────
 ('chronique-pratique', 'vocab', P_VOC, PERS + " Une personne vue de trois quarts "
  "arrière, casque d'écoute sur les oreilles, penchée vers un micro de studio, une "
  "feuille de notes à la main. Le visage est hors cadrage." + SANS_MOTS),
 ('documentaire', 'vocab', P_VOC, STYLE + " Gros plan sur un écran de télévision "
  "montrant une image d'archives en noir et blanc d'un atelier ancien, dans une pièce "
  "sombre. Aucun sous-titre." + SANS_MOTS),
 ('entrevue', 'vocab', P_VOC, PERS + " Deux personnes assises face à face de part et "
  "d'autre d'une table de studio, chacune devant un micro sur bras articulé, vues de "
  "loin et de côté, les visages hors cadrage." + SANS_MOTS),
 ('courrier-lecteurs', 'vocab', P_VOC, STYLE + " Gros plan sur une double page de "
  "journal ouverte, montrant une colonne de courtes lettres séparées par des filets, "
  "chacune terminée par une ligne de signature. Toutes les lignes de texte sont des "
  "traits gris illisibles." + SANS_MOTS),
 ('piece-rechange', 'vocab', P_VOC, STYLE + " Gros plan sur une pièce mécanique neuve "
  "d'électroménager — une pompe de vidange de plastique noir avec son raccord — posée "
  "sur un établi, encore à moitié dans son emballage de carton brun. Aucune étiquette "
  "lisible." + SANS_MOTS),
 ('mise-en-demeure', 'vocab', P_VOC, STYLE + " Gros plan sur une feuille de papier "
  "blanche imprimée, posée sur une table de cuisine à côté d'un stylo et d'une "
  "enveloppe. On distingue la disposition d'une lettre — bloc d'adresse en haut, trois "
  "paragraphes, une ligne de signature — mais chaque ligne est un trait gris "
  "entièrement illisible." + SANS_MOTS),
 ('enquete', 'vocab', P_VOC, STYLE + " Gros plan sur une table de travail : des "
  "chemises de carton ouvertes, des documents empilés, un carnet à spirale et une loupe "
  "posée dessus. Les lignes des documents et du carnet sont des traits gris "
  "illisibles." + SANS_MOTS),
 ('organisme-public', 'vocab', P_VOC, STYLE + " Le comptoir d'accueil d'un bureau de "
  "service public modeste : un guichet vitré, une chaise, un présentoir de dépliants "
  "aux couvertures unies, un mur neutre. Aucune personne, aucune affiche lisible, aucun "
  "logo." + SANS_MOTS),
 ('lettre-ouverte', 'vocab', P_VOC, PERS + " Une personne vue de dos, assise à une "
  "table de cuisine le soir, qui écrit à la main sur une feuille de papier, une tasse à "
  "côté. Le visage est hors cadrage et les lignes écrites sont des traits gris "
  "illisibles." + SANS_MOTS),
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
