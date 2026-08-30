#!/usr/bin/env python3
"""Génère les 23 images de module-n3-secretariat par `build/route_images.py`.

Deux destinations :
  · `images/` — les huit illustrations de l'exercice 3 de « Je découvre » ;
  · `vocab/`  — les quinze photos du banc de vocabulaire, réduites à 800 px.

**Aucun appel réseau en dur ici.** `generer_image` essaie les routes dans
l'ordre du prix mesuré le 21 août 2026 — Google direct, puis fal.ai, puis
WaveSpeed — et rend le nom de celle qui a servi. C'est ce nom qui est inscrit
au journal de chaque image : une photo produite chez un repli n'est pas un
détail, c'est une ligne de facture et parfois une différence de style.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perdrait le tiers du haut et du bas.

**La difficulté propre à ce module est que sa matière est du papier et de
l'administration.** Un billet d'absence, une attestation, un formulaire, un
dossier : quatre objets dont tout le sens est écrit dessus — et le générateur
a l'ordre de ne produire aucun texte lisible. Les prompts demandent donc des
papiers dont la *forme* se reconnaît (un petit feuillet plié, une feuille à
en-tête, un formulaire à cases, une chemise cartonnée) sans qu'aucun mot ne se
déchiffre : l'élève reconnaît l'objet, et c'est l'exercice qui en donne le
contenu. Le reste du module se passe dans un centre de formation des adultes
ordinaire, et les personnes n'y sont jamais reconnaissables : un comptoir,
un corridor, une salle d'attente, une main qui signe.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n3-secretariat/gen_images.py
  python3 build/contenu/module-n3-secretariat/gen_images.py billet-clinique
"""
import io, json, pathlib, sys, time

MODULE = 'module-n3-secretariat'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from route_images import generer_image                       # noqa: E402

CENTRE = ("Photographie réaliste, format paysage, lumière naturelle douce, "
          "faible profondeur de champ. Intérieur d'un centre de formation des "
          "adultes québécois ordinaire : murs clairs, planchers de tuile, "
          "mobilier institutionnel simple. Palette sobre. Aucun texte "
          "lisible, aucune écriture déchiffrable, aucun logo, aucun "
          "filigrane, aucune personne identifiable.")

PAPIER = ("Photographie réaliste, format paysage, gros plan sur un document "
          "posé sur une surface claire, lumière naturelle rasante, faible "
          "profondeur de champ. Les lignes de texte apparaissent comme des "
          "traits gris entièrement illisibles : aucun mot, aucun chiffre, "
          "aucune signature déchiffrable, aucun logo, aucun filigrane.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne "
        "au Québec avec une ou deux personnes vues de dos, de trois quarts ou "
        "hors cadrage du visage. Lumière naturelle douce, faible profondeur "
        "de champ. Aucun visage reconnaissable, aucun texte, aucun logo, "
        "aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Une journée au centre"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit images d'exercice ────────────────────────────────────────
 ('comptoir-accueil', 'images', P_EX, CENTRE + " Le comptoir d'accueil d'un "
  "centre de formation, vu de face : plan de travail haut, écran d'ordinateur "
  "de dos, téléphone, porte-crayons. Personne au premier plan."),
 ('chaise-vide', 'images', P_EX, CENTRE + " Une chaise vide devant un pupitre "
  "d'adulte dans une salle de classe, cahier fermé posé dessus, les autres "
  "places floues à l'arrière-plan."),
 ('calendrier-mural', 'images', P_EX, CENTRE + " Un calendrier de papier "
  "accroché au mur d'un bureau, dont la grille de cases se voit nettement, "
  "mais dont aucun chiffre ni aucun mot n'est lisible."),
 ('billet-clinique', 'images', P_EX, PAPIER + " Un petit feuillet de papier "
  "plié une fois, de la taille d'une main, posé sur un comptoir de bureau à "
  "côté d'un stylo."),
 ('photocopieur', 'images', P_EX, CENTRE + " Un photocopieur de bureau, "
  "couvercle levé, une feuille blanche posée sur la vitre, vu de trois "
  "quarts."),
 ('salle-attente', 'images', P_EX, CENTRE + " La salle d'attente d'une "
  "clinique de quartier : une rangée de chaises vides alignées contre un mur, "
  "une petite table basse, lumière du matin."),
 ('main-signature', 'images', P_EX, PERS + " Très gros plan sur une seule main, "
  "un stylo et le bas d'une feuille libre posée sur un comptoir clair. Aucune "
  "personne dans le champ, aucun cahier relié, aucun décor de café : rien que "
  "le comptoir, la feuille et la main. Le trait de l'écriture reste flou et "
  "illisible."),
 ('horloge-corridor', 'images', P_EX, CENTRE + " Une horloge ronde "
  "institutionnelle accrochée au mur d'un corridor d'école, aiguilles un peu "
  "avant huit heures, casiers flous à l'arrière-plan."),

 # ── Les quinze photos du banc de vocabulaire ──────────────────────────
 ('secretariat', 'vocab', P_VOC, CENTRE + " Le bureau du secrétariat d'un "
  "centre de formation vu depuis le corridor, porte vitrée ouverte, comptoir "
  "au fond."),
 ('comptoir', 'vocab', P_VOC, CENTRE + " Un comptoir d'accueil haut, vu de "
  "trois quarts, avec un petit présentoir de dépliants et un stylo attaché."),
 ('secretaire', 'vocab', P_VOC, PERS + " Une personne assise derrière un "
  "comptoir d'accueil, vue de dos et de trois quarts, en train d'écrire dans "
  "un cahier. Aucun visage visible."),
 ('groupe', 'vocab', P_VOC, CENTRE + " Une salle de classe d'adultes vue "
  "depuis le fond : des rangées de pupitres, quelques personnes assises de "
  "dos, un tableau blanc vide au loin."),
 ('dossier', 'vocab', P_VOC, PAPIER + " Une chemise cartonnée beige ouverte "
  "sur un bureau, quelques feuilles à l'intérieur, une languette d'onglet sur "
  "le côté."),
 ('absence', 'vocab', P_VOC, CENTRE + " Un pupitre vide au milieu d'une "
  "rangée de pupitres occupés, chaise poussée de côté, le reste de la salle "
  "flou."),
 ('prevenir', 'vocab', P_VOC, PERS + " Une personne debout dans un corridor, "
  "vue de dos, un téléphone cellulaire à l'oreille, sac à l'épaule."),
 ('avant-midi', 'vocab', P_VOC, CENTRE + " Une horloge murale ronde indiquant "
  "un peu avant neuf heures, dans un corridor éclairé par une fenêtre du "
  "matin. Les chiffres du cadran restent flous."),
 ('rendez-vous', 'vocab', P_VOC, PAPIER + " Un agenda de papier ouvert sur "
  "une table, la grille des heures bien visible, une case marquée d'un trait "
  "de stylo. Aucun mot lisible."),
 ('billet-absence', 'vocab', P_VOC, PAPIER + " Un petit feuillet de papier "
  "tenu entre deux doigts devant un arrière-plan flou de comptoir de bureau."),
 ('photocopie', 'vocab', P_VOC, CENTRE + " Une feuille de papier qui sort du "
  "plateau de sortie d'un photocopieur de bureau, gros plan, aucun texte "
  "déchiffrable."),
 ('original', 'vocab', P_VOC, PAPIER + " Deux feuilles côte à côte sur un "
  "bureau : l'une un peu jaunie avec un pli, l'autre parfaitement blanche et "
  "plate. Aucun mot lisible sur l'une ni sur l'autre."),
 ('abandon', 'vocab', P_VOC, PERS + " Une personne vue de dos qui s'éloigne "
  "dans un corridor d'école en portant un sac, casiers de chaque côté, porte "
  "de sortie éclairée au fond."),
 ('attestation', 'vocab', P_VOC, PAPIER + " Une feuille de papier épais à "
  "en-tête posée sur un bureau, avec un cadre et un espace de signature en "
  "bas. Le texte est une suite de traits gris illisibles."),
 ('signer', 'vocab', P_VOC, PERS + " Gros plan sur une main qui signe le bas "
  "d'un formulaire posé sur un comptoir de bureau ou de guichet, un stylo bleu "
  "entre les doigts. Arrière-plan neutre et flou, aucun aliment, aucune "
  "viennoiserie, aucun terminal de paiement dans le champ. L'écriture reste "
  "illisible."),
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
