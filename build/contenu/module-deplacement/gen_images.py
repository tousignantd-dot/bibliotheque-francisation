#!/usr/bin/env python3
"""Génère les 21 images du module-deplacement via fal.ai (Nano Banana 2).

Deux destinations, deux formats :
  · `images/` — les illustrations d'exercice, 1024 px, telles que rendues ;
  · `vocab/`  — les photos du banc de vocabulaire, réduites à 800 px / q. 82.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-deplacement/gen_images.py
  python3 build/contenu/module-deplacement/gen_images.py tournoi balcon
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-deplacement'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
ENV  = pathlib.Path('/Users/danieltousignant/Claude/.env')


def cle(nom):
    for ligne in ENV.read_text(encoding='utf-8').splitlines():
        ligne = ligne.strip()
        if ligne.startswith(nom + '='):
            return ligne.split('=', 1)[1].strip().strip('"\'')
    return ''


FAL = cle('FAL_KEY')
if not FAL:
    sys.exit('FAL_KEY absente de ~/Claude/.env')

STYLE = ("Photographie réaliste, format paysage 3:2, lumière naturelle de jour, faible "
         "profondeur de champ. Rue ou transport en commun d'une ville québécoise "
         "ordinaire, palette sobre. Aucun texte lisible, aucune écriture, aucun logo, "
         "aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage 3:2, scène de la vie quotidienne au Québec "
        "avec une ou deux personnes vues de dos, de trois quarts ou hors cadrage du "
        "visage. Lumière naturelle douce, faible profondeur de champ. Aucun visage "
        "reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Les repères de la rue"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit repères de la rue (exercice 3) ───────────────────────────
 ('feu', 'images', P_EX, STYLE + " Un feu de circulation vu du trottoir, au croisement de "
  "deux rues de quartier. Le feu est rouge. Poteaux gris, fils électriques au-dessus, "
  "maisons de brique en arrière-plan flou."),
 ('coin', 'images', P_EX, STYLE + " Le coin de deux rues résidentielles vu du trottoir : "
  "un passage piéton peint au sol, un poteau d'arrêt, et les deux rues qui se croisent en "
  "angle droit. Arbres et maisons de chaque côté."),
 ('arret-autobus', 'images', P_EX, PERS + " Un abribus vitré au bord d'une rue de "
  "quartier, avec un banc et un poteau de métal nu. Une personne attend, vue de dos. Le "
  "haut du poteau et son panneau sont coupés par le bord supérieur ; aucun pictogramme, "
  "aucun numéro de ligne, aucune plaque dans le champ. Fin d'après-midi."),
 ('quai-metro', 'images', P_EX, STYLE + " Un quai de station de métro vide : ligne de "
  "sécurité peinte au sol le long du bord, carrelage, bancs alignés contre le mur, "
  "éclairage au plafond. Tunnel sombre au bout."),
 ('parc-sentier', 'images', P_EX, STYLE + " Un sentier de terre battue traversant un petit "
  "parc de quartier, entre deux rangées d'arbres. Un module de jeux pour enfants visible "
  "à gauche, flou. Lumière du matin."),
 ('porte-vitree', 'images', P_EX, STYLE + " La façade d'un édifice de bureaux de trois "
  "étages en brique claire, avec une grande porte vitrée à double battant et quelques "
  "marches devant. Trottoir au premier plan."),
 ('panneau-quai', 'images', P_EX, STYLE + " Un panneau de signalisation suspendu au-dessus "
  "d'un escalier de station de métro, avec une flèche vers le bas. Le panneau est vu de "
  "biais et son inscription reste floue et illisible."),
 ('escalier', 'images', P_EX, STYLE + " Un escalier de béton descendant au bout d'un long "
  "corridor vitré, avec une rampe métallique. Lumière du jour entrant par les vitres du "
  "corridor. Aucune personne."),

 # ── Les treize mots du banc de vocabulaire ────────────────────────────
 ('coin-de-rue', 'vocab', P_VOC, STYLE + " Vue en plongée légère sur le croisement de deux "
  "rues résidentielles, avec les passages piétons peints en blanc sur l'asphalte et les "
  "quatre coins de trottoir visibles."),
 ('feu-circulation', 'vocab', P_VOC, STYLE + " Gros plan sur un feu de circulation pour "
  "véhicules, suspendu au-dessus d'un croisement de rues : un boîtier vertical à trois "
  "lentilles rondes, rouge en haut, jaune au centre, vert en bas, la lentille rouge "
  "allumée. Aucun signal pour piétons, aucune main lumineuse dans le champ. Ciel dégagé "
  "en arrière-plan."),
 ('trottoir', 'vocab', P_VOC, STYLE + " Un trottoir de béton bordé d'une bande de gazon et "
  "d'arbres, longeant une rue résidentielle. Vue à hauteur de piéton, perspective vers "
  "l'avant."),
 ('terminus', 'vocab', P_VOC, STYLE + " Un terminus d'autobus de banlieue : plusieurs "
  "autobus blancs stationnés en épi le long de quais couverts, marquises de métal, "
  "asphalte propre. Aucune inscription lisible."),
 ('quai', 'vocab', P_VOC, STYLE + " Un quai d'embarquement d'autobus sous une marquise "
  "vitrée, avec un banc et une poubelle. Le poteau d'arrêt est coupé à mi-hauteur par le "
  "bord droit du cadre, sa plaque entièrement hors champ ; aucun chiffre, aucun "
  "pictogramme, aucun panneau dans le champ. Sol de béton lisse."),
 ('correspondance', 'vocab', P_VOC, STYLE + " Un quai de métro vu depuis le fond : à gauche, une rame arrêtée "
  "portes ouvertes ; à droite, au-delà d'un court passage voûté, une "
  "seconde rame attend sur un autre quai. Deux voyageurs vus de dos "
  "marchent du premier quai vers le second. Une grande flèche blanche "
  "peinte au sol indique le passage. Aucun panneau, aucune plaque, "
  "aucun nom de station, aucun chiffre dans le champ."),
 ('direction', 'vocab', P_VOC, STYLE + " L'avant d'un autobus de ville arrêté à un arrêt, vu de trois quarts "
  "depuis le trottoir. Au-dessus du pare-brise, le panneau de "
  "destination est une bande lumineuse ambrée entièrement floue, où "
  "aucun caractère n'est formé. Au premier plan, une personne vue de "
  "dos lève la tête vers ce panneau. Aucun numéro, aucun mot, aucun "
  "sigle de société de transport nulle part."),
 ('sentier', 'vocab', P_VOC, STYLE + " Un sentier de terre serpentant dans un boisé de "
  "quartier, avec des arbres feuillus de chaque côté et de la lumière filtrant entre les "
  "branches."),
 ('enseigne', 'vocab', P_VOC, STYLE + " Une petite enseigne rectangulaire vierge, sans "
  "aucune inscription, fixée au-dessus de la porte d'entrée d'un commerce de quartier. "
  "Brique et cadre de bois autour."),
 ('edifice', 'vocab', P_VOC, STYLE + " Un édifice de bureaux de quatre étages en brique "
  "beige, vu depuis le trottoir d'en face, avec une entrée vitrée au centre et des "
  "fenêtres régulières. Ciel gris."),
 ('horaire', 'vocab', P_VOC, STYLE + " Un panneau d'horaire d'autobus vitré fixé à un "
  "abribus, montrant une grille de colonnes et de lignes. Les chiffres restent flous et "
  "illisibles. Reflet léger sur la vitre."),
 ('interruption', 'vocab', P_VOC, STYLE + " Une barrière de chantier orange et blanche "
  "vue de face, bloquant le haut d'un escalier qui descend sous le trottoir, avec des "
  "cônes orange devant. L'enseigne du métro reste hors cadre au-dessus ; aucun sigle, "
  "aucun pictogramme de transport, aucune plaque dans le champ."),
 ('plan-reseau', 'vocab', P_VOC, STYLE + " Un plan de réseau de transport affiché derrière "
  "une vitre dans une station : des lignes de couleur qui se croisent, des cercles blancs "
  "et noirs le long des lignes. Aucun nom lisible."),
]


def genere(prompt):
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": "3:2",
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + FAL, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.loads(r.read())
    with urllib.request.urlopen(d["images"][0]["url"], timeout=240) as r:
        return r.read()


def reduire(data, cote=800, qualite=82):
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien.

    En 3:2, comme le gabarit qui les affiche — `.imgzone`, `.imgtile` et
    `.vc-photo` sont tous en `aspect-ratio:3/2`. Redimensionner en carré
    faisait recadrer d'un tiers à l'affichage, et c'était le sujet qui
    partait."""
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert('RGB')
    im = im.resize((cote, round(cote * 2 / 3)), Image.LANCZOS)
    tampon = io.BytesIO()
    im.save(tampon, 'JPEG', quality=qualite, optimize=True)
    return tampon.getvalue()


voulus = set(sys.argv[1:])
GEN.mkdir(parents=True, exist_ok=True)
horodatage = time.strftime('%Y%m%d-%H%M%S')
faits, sautes, echecs = [], [], []

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
        data = genere(prompt)
    except urllib.error.HTTPError as e:
        echecs.append('%s : HTTP %s %s' % (etiquette, e.code, e.read()[:180])); continue
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
        "model": "fal-ai/nano-banana-2",
        "prompt": prompt,
        "refs": [],
        "params": {"num_images": 1, "aspect_ratio": "3:2",
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": "fal.ai",
        "cost_estimate_usd": 0.034,
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation",
        "module": MODULE,
        "page": page,
        "destination": "assets/interactive/%s/%s/%s.jpg" % (MODULE, dossier, nom),
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(etiquette)
    print('  ✓ %-28s %6.1f Ko' % (etiquette, len(data) / 1024), flush=True)

print('\n%d générées, %d déjà présentes, %d en échec'
      % (len(faits), len(sautes), len(echecs)))
for e in echecs:
    print('  ✗ ' + e)
print('coût estimé : %.2f $' % (len(faits) * 0.034))
