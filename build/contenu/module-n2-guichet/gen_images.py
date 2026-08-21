#!/usr/bin/env python3
"""Génère les 17 images de module-n2-guichet.

Deux destinations :
  · `images/` — les six illustrations de l'exercice de glisser-déposer,
    telles que rendues ;
  · `vocab/`  — les onze photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdait le tiers du haut et du bas. Voir
`docs/chantier-tous-niveaux.md`.

**L'appel réseau passe par `build/route_images.py`**, jamais par fal.ai en
dur : la route Google directe coûte 0,0336 $ et répond en 3,9 s, fal.ai
0,080 $ en 14,5 s, WaveSpeed 0,070 $ en 25,9 s — les trois revendent le même
modèle. `generer_image` les essaie dans l'ordre du prix et rend le nom de
celle qui a servi ; ce nom est écrit dans le journal .json adjacent, pour
qu'un repli ne passe jamais inaperçu.

Le module se passe dans un hall de guichets et à un comptoir d'accueil. Les
six photos de l'exercice doivent rester **reconnaissables du premier coup
d'œil** — un élève de niveau 2 les associe à une phrase de cinq mots, sans
lire de légende. Aucun texte lisible nulle part : ni montant, ni logo de
caisse, ni nom de banque.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n2-guichet/gen_images.py
  python3 build/contenu/module-n2-guichet/gen_images.py etape-nip
"""
import io, json, pathlib, sys, time

MODULE = 'module-n2-guichet'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
RATIO = "3:2"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))  # build/
from route_images import generer_image, ESTIMATIONS

# Le décor commun : le hall des guichets d'une caisse populaire de quartier.
HALL = ("Photographie réaliste, format paysage, lumière intérieure douce. "
        "Le hall des guichets automatiques d'une caisse populaire de quartier "
        "au Québec : murs clairs, sol de tuiles, plantes vertes. Palette "
        "sobre. Aucun texte lisible, aucun chiffre lisible, aucun logo, "
        "aucune marque, aucun filigrane, aucune personne identifiable.")

# Quand des mains sont nécessaires, on ne voit qu'elles.
MAINS = ("Photographie réaliste, format paysage, gros plan sur des mains "
         "seules, sans visage ni buste dans le cadre. Lumière intérieure "
         "douce, faible profondeur de champ. Aucun texte lisible, aucun "
         "chiffre lisible, aucun logo, aucun filigrane.")

# Les objets du banc, photographiés seuls.
OBJET = ("Photographie réaliste, format paysage, un seul objet net au centre "
         "du cadre sur un fond intérieur flou et neutre. Lumière naturelle "
         "douce. Aucun texte lisible, aucun chiffre lisible, aucun logo, "
         "aucun nom de banque, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Qu'est-ce qu'on fait sur la photo ?"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les six images de l'exercice de glisser-déposer ───────────────────
 # Chacune doit se lire seule : c'est l'objet même de l'exercice.
 ('etape-carte', 'images', P_EX, MAINS + " Une main glisse une carte de "
  "plastique bleue dans la fente d'un guichet automatique. La fente et la "
  "carte sont nettes et bien au centre. Aucune écriture sur la carte."),
 ('etape-nip', 'images', P_EX, MAINS + " Une main tape sur le clavier de "
  "métal d'un guichet automatique pendant que l'autre main, posée au-dessus, "
  "cache le clavier. Les touches restent floues et sans chiffres lisibles."),
 ('etape-choix', 'images', P_EX, MAINS + " Un index appuie sur un bouton "
  "rectangulaire situé à côté de l'écran d'un guichet automatique. L'écran "
  "est allumé mais complètement flou : aucun mot, aucun chiffre."),
 ('etape-billets', 'images', P_EX, MAINS + " Deux mains prennent des billets "
  "de banque qui sortent de la fente d'un guichet automatique. Les billets "
  "sont nets mais leurs inscriptions restent illisibles."),
 ('etape-releve', 'images', P_EX, MAINS + " Une main tient un petit reçu de "
  "papier blanc étroit qui vient de sortir d'un guichet automatique. Le "
  "papier est net, l'impression dessus reste floue et illisible."),
 ('etape-comptoir', 'images', P_EX, HALL + " Le comptoir d'accueil d'une "
  "caisse populaire vu de trois quarts : une employée derrière le comptoir "
  "et une personne devant, toutes deux vues de dos ou de profil perdu, "
  "visages hors cadrage."),

 # ── Les onze photos du banc de vocabulaire ────────────────────────────
 ('argent', 'vocab', P_VOC, OBJET + " Des billets de banque et quelques "
  "pièces de monnaie posés à plat sur une table de bois clair, vus d'en "
  "haut. Les inscriptions restent illisibles."),
 ('billet', 'vocab', P_VOC, OBJET + " Un seul billet de banque coloré tenu "
  "entre deux doigts, devant un fond intérieur flou. Aucun chiffre lisible."),
 ('piece', 'vocab', P_VOC, OBJET + " Trois pièces de monnaie de métal posées "
  "côte à côte sur une table claire, vues de très près. Aucune inscription "
  "lisible."),
 ('carte-debit', 'vocab', P_VOC, OBJET + " Une carte de plastique bleue à "
  "puce dorée, posée en biais sur une table claire. Aucun nom, aucun chiffre, "
  "aucun logo dessus."),
 ('guichet-automatique', 'vocab', P_VOC, HALL + " Un guichet automatique "
  "encastré dans un mur, vu de face, personne devant. L'écran est allumé mais "
  "flou : aucun mot lisible."),
 ('depot', 'vocab', P_VOC, MAINS + " Une main glisse une enveloppe de papier "
  "dans la fente d'un guichet automatique. L'enveloppe est blanche et vierge."),
 ('releve', 'vocab', P_VOC, OBJET + " Un petit reçu de papier étroit posé sur "
  "une table claire, légèrement enroulé au bout. L'impression dessus reste "
  "floue et illisible."),
 ('cheque', 'vocab', P_VOC, OBJET + " Un chèque de papier vierge, de couleur "
  "pâle, posé à plat sur une table de bois avec un stylo à côté. Les lignes "
  "du chèque sont visibles, mais aucun mot n'est lisible."),
 ('signature', 'vocab', P_VOC, MAINS + " Une main tient un stylo et signe le "
  "bas d'un papier posé sur une table de bois. Le trait de la signature est "
  "net, mais illisible : ce n'est qu'une boucle d'encre."),
 ('paiement-direct', 'vocab', P_VOC, MAINS + " Une main approche une carte de "
  "plastique du petit terminal de paiement d'un commerce, posé sur un "
  "comptoir. L'écran du terminal est allumé mais flou."),
 ('comptant', 'vocab', P_VOC, MAINS + " Une main tend des billets de banque "
  "au-dessus du comptoir d'un commerce. Les billets sont nets, leurs "
  "inscriptions illisibles."),
]


def reduire(data, largeur=800, qualite=82):
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien.

    La hauteur suit le rapport de l'image reçue, au lieu d'être forcée à un
    carré — c'est tout l'objet du passage au 3:2.
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
