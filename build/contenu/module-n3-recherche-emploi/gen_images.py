#!/usr/bin/env python3
"""Génère les 25 images de module-n3-recherche-emploi par `build/route_images.py`.

Deux destinations :
  · `images/` — les sept illustrations de l'exercice 3 de « Je découvre » ;
  · `vocab/`  — les dix-huit photos du banc de vocabulaire, réduites à 800 px.

**Aucun appel réseau en dur ici.** `generer_image` essaie les routes dans
l'ordre du prix mesuré le 21 août 2026 — Google direct (0,0336 $, 3,9 s), puis
fal.ai, puis WaveSpeed — et rend le nom de celle qui a servi. C'est ce nom qui
est inscrit au journal de chaque image, et `route_images` inscrit de son côté
chaque **tentative** au registre `journal_appels` : le mur compte des appels,
pas des fichiers, et une image reprise trois fois est payée trois fois.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perdrait le tiers du haut et du bas.

**La difficulté propre à ce module est qu'il est fait de papier.** Une affiche
d'embauche, une offre punaisée au babillard, un formulaire à cases, une petite
annonce écrite à la main : quatre des sept illustrations sont des documents, et
le générateur a l'ordre de ne produire aucun texte lisible. Les prompts
demandent donc des papiers dont la *forme* se lit — un grand mot en haut, des
lignes régulières, une grille de cases, un numéro en gros en bas — sans qu'un
seul mot ne se déchiffre. L'élève reconnaît l'objet ; c'est l'exercice qui en
donne le contenu, et c'est ce qu'on veut : sinon il lirait la réponse dans
l'image au lieu de la lire dans l'énoncé.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n3-recherche-emploi/gen_images.py
  python3 build/contenu/module-n3-recherche-emploi/gen_images.py affiche-vitrine
"""
import io, json, pathlib, sys, time

MODULE = 'module-n3-recherche-emploi'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from route_images import generer_image                       # noqa: E402

COMMERCE = ("Photographie réaliste, format paysage, lumière naturelle douce, "
            "faible profondeur de champ. Un petit commerce de quartier "
            "ordinaire à Montréal — boulangerie, épicerie de coin, centre "
            "communautaire. Palette sobre et chaleureuse. Aucun texte lisible, "
            "aucune écriture déchiffrable, aucune enseigne lisible, aucun "
            "logo, aucun filigrane, aucune personne identifiable.")

PAPIER = ("Photographie réaliste, format paysage, gros plan sur un document de "
          "papier, lumière naturelle douce, faible profondeur de champ. La "
          "MISE EN PAGE du document doit se reconnaître au premier coup d'œil, "
          "mais AUCUN mot ne doit être déchiffrable : les lignes de texte sont "
          "de simples traits gris flous. Aucun logo, aucun filigrane, aucune "
          "personne identifiable.")

BUREAU = ("Photographie réaliste, format paysage, intérieur d'un bureau de "
          "quartier ou d'un local communautaire québécois ordinaire, lumière "
          "naturelle douce, faible profondeur de champ. Aucun texte lisible, "
          "aucun logo, aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Où on cherche du travail"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les sept images de l'exercice 3 ───────────────────────────────────
 ('affiche-vitrine', 'images', P_EX, COMMERCE + " Une feuille de papier rouge "
  "vif entièrement vierge, scotchée de l'intérieur dans la vitrine d'une "
  "boulangerie, vue de la rue : aucune écriture, aucune trace de marqueur, "
  "aucune impression sur la feuille. La devanture est cadrée sous le niveau "
  "de l'enseigne, qui reste hors champ. Reflets doux sur la vitre."),
 ('babillard-epicerie', 'images', P_EX, COMMERCE + " Un grand babillard de "
  "liège près de l'entrée d'une épicerie de quartier, couvert de petites "
  "feuilles et de cartons punaisés à des hauteurs différentes, certains avec "
  "des languettes découpées en bas. Aucun mot déchiffrable sur aucun papier."),
 ('comptoir-boulangerie', 'images', P_EX, COMMERCE + " Le comptoir vitré d'une "
  "boulangerie de quartier, vu de trois quarts : pains et viennoiseries "
  "alignés derrière la vitre, tablettes de bois au mur du fond, caisse "
  "enregistreuse au bout. Personne derrière le comptoir."),
 ('formulaire-demande', 'images', P_EX, PAPIER + " Un formulaire d'une page "
  "posé à plat sur un comptoir de bois, avec un stylo bleu à côté. On "
  "reconnaît une grille de petites cases carrées en haut, deux carrés à "
  "cocher au milieu et une longue ligne de signature en bas. Aucun mot "
  "déchiffrable."),
 ('centre-emploi', 'images', P_EX, BUREAU + " Un petit bureau d'aide à "
  "l'emploi de quartier : deux chaises devant un pupitre, un ordinateur "
  "éteint, un présentoir de dépliants au mur, une fenêtre qui donne sur la "
  "rue. Personne dans la pièce."),
 ('cuisine-centre', 'images', P_EX, BUREAU + " La cuisine d'un centre "
  "communautaire : grandes tables de travail en acier inoxydable, gros "
  "chaudrons sur une cuisinière, étagères de vaisselle, éviers doubles au "
  "fond. Propre et vide."),
 ('petite-annonce', 'images', P_EX, PAPIER + " Un petit carton blanc manuscrit "
  "en alphabet latin uniquement, punaisé sur un babillard de liège, sans "
  "titre en haut : seulement trois lignes de traits gris au milieu et une "
  "rangée de languettes découpées au bas — dont deux déjà arrachées. Aucun "
  "caractère d'un autre alphabet, aucun numéro de téléphone."),

 # ── Les dix-huit photos du banc de vocabulaire ────────────────────────
 ('emploi', 'vocab', P_VOC, PERS + " Une personne vue de dos, en tablier, qui "
  "range des produits sur les tablettes d'un petit commerce, tôt le matin."),
 ('embaucher', 'vocab', P_VOC, PERS + " Deux personnes debout de part et "
  "d'autre d'un comptoir, vues de trois quarts, l'une tendant une feuille de "
  "papier à l'autre. Aucun visage visible, aucun mot lisible sur la feuille."),
 ('metier', 'vocab', P_VOC, PERS + " Gros plan sur des mains qui pétrissent de "
  "la pâte sur un plan de travail fariné, dans une boulangerie de quartier, "
  "tôt le matin."),
 ('patron', 'vocab', P_VOC, PERS + " Une personne vue de dos derrière le "
  "comptoir d'un petit commerce, en tablier, en train de vérifier une liste "
  "sur un carnet. Aucun mot lisible."),
 ('affiche', 'vocab', P_VOC, PAPIER + " Une feuille de papier rouge vierge, "
  "sans une seule marque d'encre, scotchée à l'intérieur d'une vitrine de "
  "commerce, vue de près et de biais. Le papier est uni d'un bord à l'autre, "
  "aucun mot, aucun trait, aucune impression."),
 ('offrir-ses-services', 'vocab', P_VOC, PERS + " Une personne vue de dos qui "
  "pousse la porte vitrée d'un petit commerce, une main sur la poignée, "
  "clochette au-dessus de la porte."),
 ('commis', 'vocab', P_VOC, PERS + " Une personne en tablier, vue de dos, qui "
  "sert un client au comptoir d'une boulangerie, un sac de papier à la main."),
 ('experience', 'vocab', P_VOC, PERS + " Gros plan sur des mains "
  "expérimentées qui plient du linge propre en pile bien droite sur une "
  "table, dans une pièce claire."),
 ('disponibilites', 'vocab', P_VOC, PAPIER + " Un calendrier de semaine "
  "affiché sur un réfrigérateur avec des aimants : sept colonnes, des cases "
  "vides et quelques cases coloriées au surligneur. Aucun mot déchiffrable."),
 ('offre-emploi', 'vocab', P_VOC, PAPIER + " Une feuille blanche punaisée "
  "seule sur un babillard de liège : un titre en gras, six lignes courtes "
  "en dessous, une ligne de chiffres en bas. Rien n'est déchiffrable."),
 ('babillard', 'vocab', P_VOC, COMMERCE + " Gros plan sur un babillard de "
  "liège encadré de bois, dans l'entrée d'une épicerie, couvert de papiers "
  "punaisés de toutes tailles. Aucun mot déchiffrable."),
 ('salaire', 'vocab', P_VOC, PAPIER + " Un talon de paie posé sur une table de "
  "cuisine à côté d'une tasse de café : deux colonnes de chiffres alignées, "
  "un total encadré en bas. Les chiffres sont flous et illisibles."),
 ('horaire', 'vocab', P_VOC, PAPIER + " Un horaire de travail affiché au mur "
  "d'un arrière-boutique : une grille de sept colonnes et de plusieurs "
  "rangées, des cases remplies au crayon. Aucun mot ni chiffre déchiffrable."),
 ('temps-partiel', 'vocab', P_VOC, PERS + " Une personne vue de dos qui "
  "accroche son tablier à un crochet près d'une porte de service, sac à "
  "l'épaule, fin de quart de travail, lumière de fin de matinée."),
 ('formulaire', 'vocab', P_VOC, PAPIER + " Gros plan en plongée sur un "
  "formulaire d'une page et un stylo, posés sur un comptoir : rangées de "
  "petites cases carrées, deux carrés à cocher, une ligne de signature. "
  "Aucun mot déchiffrable."),
 ('lettres-moulees', 'vocab', P_VOC, PAPIER + " Très gros plan sur une main "
  "qui écrit une lettre majuscule au stylo dans une grille de petites cases "
  "carrées d'un formulaire. Les cases voisines sont vides ; aucun mot ne se "
  "forme."),
 ('petite-annonce', 'vocab', P_VOC, PAPIER + " Un carton punaisé sur un "
  "babillard, dont le contenu se réduit à un titre en gros traits illisibles, "
  "trois lignes de traits gris et des languettes découpées au bas dont une "
  "est arrachée. Aucune date, aucune heure, aucun montant, aucun symbole de "
  "devise."),
 ('curriculum-vitae', 'vocab', P_VOC, PAPIER + " Une feuille blanche unique "
  "posée sur une table de bois, tenue par une main au coin : un bloc de "
  "lignes en haut, deux blocs de lignes plus bas, marges larges. Aucun mot "
  "déchiffrable."),
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
    # La route Google directe rend des JPEG bien plus lourds que fal.ai —
    # de 650 à 1000 Ko contre 350. À l'écran, l'image d'exercice occupe
    # 223 x 132 px et la photo du banc encore moins : les deux se réduisent,
    # seulement pas au même format.
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
    print('  !! ' + e)
