#!/usr/bin/env python3
"""Génère les 21 images du module-activite via fal.ai (Nano Banana 2).

Deux destinations, deux formats :
  · `images/` — les illustrations d'exercice, 1024 px, telles que rendues ;
  · `vocab/`  — les photos du banc de vocabulaire, réduites à 800 px / q. 82.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-activite/gen_images.py
  python3 build/contenu/module-activite/gen_images.py tournoi balcon
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-activite'
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

# Le décor est celui de CE module. La phrase « Rue ou transport en commun »
# qui tenait ici venait de module-deplacement, recopiée par erreur : le
# générateur la prenait au mot et servait les assiettes dans un autobus.
STYLE = ("Photographie réaliste, format paysage 3:2, lumière naturelle de jour, faible "
         "profondeur de champ. Centre de loisirs ou local communautaire "
         "ordinaire au Québec, palette sobre. "
         "Aucun texte lisible, aucune écriture, aucun logo, "
         "aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage 3:2, scène de la vie quotidienne au Québec "
        "avec une ou deux personnes vues de dos, de trois quarts ou hors cadrage du "
        "visage. Lumière naturelle douce, faible profondeur de champ. Aucun visage "
        "reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Ce qu'on apporte, ce qu'on trouve"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit lieux et objets (exercice 3) ─────────────────────────────
 ('comptoir', 'images', P_EX, STYLE + " Le comptoir d'accueil d'un centre sportif "
  "municipal : un long comptoir de mélamine claire, un écran d'ordinateur de dos, un "
  "présentoir à dépliants vide, et un tabouret derrière. Personne visible."),
 ('piscine', 'images', P_EX, STYLE + " Une piscine intérieure de quartier vue du bord : "
  "eau turquoise, lignes de couloir flottantes, carrelage clair autour du bassin, "
  "grandes fenêtres au fond. Aucune personne dans l'eau."),
 ('vestiaire', 'images', P_EX, STYLE + " Un vestiaire de centre sportif : deux rangées de "
  "casiers métalliques bleus, un banc de bois au milieu, crochets au mur. Éclairage au "
  "plafond, sol de céramique."),
 ('sac-piscine', 'images', P_EX, STYLE + " Un sac de sport ouvert posé sur un banc de "
  "vestiaire, d'où sortent une serviette pliée, un maillot de bain et une paire de "
  "sandales de plastique. Un bonnet de bain posé à côté."),
 ('planches', 'images', P_EX, STYLE + " Une pile de planches de natation en mousse de "
  "couleur, empilées dans un bac à roulettes au bord d'une piscine. Carrelage humide "
  "au premier plan."),
 ('gymnase-cours', 'images', P_EX, STYLE + " Un gymnase de centre communautaire préparé "
  "pour un cours de groupe : une dizaine de tapis d'exercice disposés en demi-cercle sur "
  "un plancher de bois, ballons rangés le long du mur. Aucune personne."),
 ('salle-chorale', 'images', P_EX, STYLE + " Une salle polyvalente de centre "
  "communautaire disposée pour une chorale : trois rangées de chaises pliantes en arc de "
  "cercle, un piano droit au fond, des lutrins pliés dans un coin."),
 ('formulaire', 'images', P_EX, STYLE + " Gros plan en plongée sur un formulaire de "
  "papier vierge, sans aucune inscription, posé sur un comptoir à côté d'un stylo et "
  "d'une carte plastifiée retournée. Lignes et cases vides uniquement."),

 # ── Les treize mots du banc de vocabulaire ────────────────────────────
 ('inscription', 'vocab', P_VOC, STYLE + " Un comptoir de service avec un formulaire "
  "vierge, un stylo posé dessus et une petite pile de feuilles à côté. Vue de face, "
  "hauteur de comptoir. Aucune écriture visible."),
 ('depliant', 'vocab', P_VOC, STYLE + " Un dépliant de papier plié en trois, ouvert à "
  "plat sur une table de bois. Les pages montrent des colonnes et des blocs de couleur, "
  "mais aucun texte lisible."),
 ('tarif', 'vocab', P_VOC, STYLE + " Gros plan sur un terminal de paiement posé sur un "
  "comptoir, écran allumé mais illisible, à côté d'un petit panier de reçus. Éclairage "
  "d'intérieur doux."),
 ('preuve-residence', 'vocab', P_VOC, STYLE + " Une enveloppe blanche ouverte et une "
  "feuille pliée posées sur une table de cuisine, à côté d'un trousseau de clés. Le "
  "papier ne porte aucun texte lisible."),
 ('moniteur', 'vocab', P_VOC, PERS + " Une personne en short et chandail de sport, "
  "accroupie au bord d'une piscine, un sifflet autour du cou, vue de dos. Elle tend le "
  "bras vers l'eau. Visage hors cadre."),
 ('maillot', 'vocab', P_VOC, STYLE + " Un maillot de bain une pièce bleu marine plié sur "
  "un banc de vestiaire, à côté d'une serviette blanche roulée."),
 ('bonnet', 'vocab', P_VOC, STYLE + " Gros plan sur un bonnet de bain en silicone bleu "
  "posé sur le rebord carrelé d'une piscine, à côté d'une paire de lunettes de natation."),
 ('vestiaire', 'vocab', P_VOC, STYLE + " Une rangée de casiers métalliques verts avec "
  "leurs cadenas, dans un vestiaire de centre sportif. Banc de bois devant, sol de "
  "céramique claire."),
 ('planche', 'vocab', P_VOC, STYLE + " Une seule planche de natation en mousse bleue "
  "posée à plat sur le rebord d'une piscine, gouttes d'eau autour. Gros plan."),
 ('benevole', 'vocab', P_VOC, PERS + " Deux personnes en chandail uni, vues de dos, "
  "installent des chaises pliantes dans une salle communautaire. Lumière naturelle par "
  "de grandes fenêtres."),
 ('chorale', 'vocab', P_VOC, STYLE + " Des chaises pliantes disposées en demi-cercle "
  "dans une salle claire, un piano droit au fond, quelques lutrins. Aucune personne."),
 ('places', 'vocab', P_VOC, STYLE + " Une rangée de chaises pliantes vides dans une "
  "salle communautaire, dont trois se détachent au premier plan. Plancher de bois, mur "
  "clair."),
 ('legende', 'vocab', P_VOC, STYLE + " Gros plan sur le bas d'une page de dépliant "
  "imprimé, où de petits symboles — une étoile, un astérisque, un carré — sont alignés "
  "les uns sous les autres. Le texte à côté reste flou et illisible."),
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
