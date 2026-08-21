#!/usr/bin/env python3
"""Génère les 23 images de module-n3-poste via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les sept illustrations de l'exercice 3 de « Je découvre » ;
  · `vocab/`  — les seize photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer mesure 223 x 132 px, un
rapport de 1,7. Une image carrée y perdrait le tiers du haut et du bas.

**La difficulté propre à ce module est que tout son univers est couvert
d'écriture** — un timbre, une adresse, un carton d'avis, un reçu, un
mandat-poste —, alors que le générateur a l'ordre de ne produire aucun texte
lisible. Les prompts demandent donc des objets dont la **forme** est
reconnaissable sans qu'un mot ne se lise : un carton rectangulaire dans une
fente de boîte aux lettres, une planchette de petits carrés dentelés, une
boîte de carton brun fermée au ruban. L'élève reconnaît l'objet ; c'est
l'exercice qui en donne le contenu.

**Aucune marque, aucun sigle, aucun logo de société postale** — ni le nom, ni
l'oiseau stylisé, ni la couleur d'uniforme reconnaissable. Vérifier à la
réception qu'aucun sigle n'est apparu : c'est le seul défaut que ces prompts
peuvent produire, et il ne se voit qu'en regardant.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n3-poste/gen_images.py
  python3 build/contenu/module-n3-poste/gen_images.py carton-avis
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n3-poste'
GEN  = pathlib.Path('/Users/danieltousignant/Claude/generations')
BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation'
                    '/assets/interactive/' + MODULE)
ENV  = pathlib.Path('/Users/danieltousignant/Claude/.env')
RATIO = "3:2"


def cle(nom):
    for ligne in ENV.read_text(encoding='utf-8').splitlines():
        ligne = ligne.strip()
        if ligne.startswith(nom + '='):
            return ligne.split('=', 1)[1].strip().strip('"\'')
    return ''


FAL = cle('FAL_KEY')
if not FAL:
    sys.exit('FAL_KEY absente de ~/Claude/.env')

STYLE = ("Photographie réaliste, format paysage, lumière naturelle, faible "
         "profondeur de champ. Intérieur d'un petit bureau de poste de "
         "quartier au Québec : comptoir de stratifié clair, sol pâle, "
         "tablettes sobres, palette neutre. Aucun texte lisible, aucune "
         "écriture, aucun logo, aucun sigle, aucune marque de société "
         "postale, aucun filigrane, aucune personne identifiable.")

OBJET = ("Photographie réaliste, format paysage, gros plan sur un objet posé "
         "sur un comptoir clair, lumière naturelle douce, faible profondeur "
         "de champ. Aucun texte lisible, aucun logo, aucun sigle, aucune "
         "marque, aucun filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun sigle, "
        "aucun filigrane.")

RUE = ("Photographie réaliste, format paysage, rue résidentielle d'un quartier "
       "de Québec, lumière naturelle d'après-midi, faible profondeur de champ. "
       "Aucun texte lisible, aucun logo, aucun sigle, aucune marque, aucune "
       "personne identifiable.")

P_EX  = "Je découvre · Exercice 3 — Dans le bureau de poste"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les sept images d'exercice ────────────────────────────────────────
 ('comptoir-poste', 'images', P_EX, STYLE + " Un comptoir de service vu de "
  "trois quarts, avec un petit terminal de paiement sombre de côté et un mur "
  "de casiers de bois derrière. Le comptoir est vide et net."),
 ('boite-rouge-rue', 'images', P_EX, RUE + " Une boîte aux lettres publique en métal "
  "rouge vif, montée sur un pied, au coin d'un trottoir, devant des arbres. "
  "Sa fente horizontale est bien visible. Aucune inscription sur le métal."),
 ('balance-colis', 'images', P_EX, OBJET + " Une boîte de carton brun fermée au "
  "ruban, posée sur le plateau plat d'une balance de comptoir, dont le petit "
  "afficheur est éteint et vide."),
 ('carnet-timbres', 'images', P_EX, OBJET + " Une planchette de petits carrés de "
  "papier aux bords dentelés, toutes de la même couleur unie, disposées en "
  "grille régulière. Les carrés sont vierges, sans dessin ni chiffre."),
 ('carton-avis', 'images', P_EX, OBJET + " Un petit carton rectangulaire de couleur "
  "pâle qui dépasse d'une fente de boîte aux lettres métallique. Les lignes "
  "d'impression du carton sont des traits gris entièrement illisibles."),
 ('cases-postales', 'images', P_EX, STYLE + " Un mur de petits casiers de métal "
  "carrés et identiques, fermés, alignés du sol au plafond, chacun avec une "
  "petite serrure ronde. Aucun numéro lisible."),
 ('ruban-boite', 'images', P_EX, OBJET + " Une boîte de carton brun de taille "
  "moyenne, fermée par une bande de ruban d'emballage transparent bien "
  "tendue, posée sur un comptoir clair. Le carton est vierge."),

 # ── Les seize photos du banc de vocabulaire ───────────────────────────
 ('bureau-de-poste', 'vocab', P_VOC, STYLE + " Vue d'ensemble d'un petit "
  "bureau de poste : un comptoir au fond, deux personnes en file vues de dos, "
  "un mur de casiers sur le côté. Aucun visage, aucune enseigne lisible."),
 ('timbre', 'vocab', P_VOC, OBJET + " Gros plan très rapproché sur un seul "
  "petit carré de papier aux bords dentelés, de couleur unie, posé de biais "
  "sur une enveloppe blanche. Le carré est vierge."),
 ('affranchir', 'vocab', P_VOC, PERS + " Gros plan sur une main qui presse du "
  "pouce un petit carré de papier dans le coin supérieur droit d'une "
  "enveloppe blanche unie, sur une table de bois clair."),
 ('envoi', 'vocab', P_VOC, OBJET + " Trois objets alignés sur un comptoir "
  "clair : une enveloppe blanche, une petite boîte de carton brun et une "
  "enveloppe matelassée beige. Tous vierges, sans inscription."),
 ('prepose', 'vocab', P_VOC, PERS + " Une personne en chemise unie, vue de "
  "trois quarts arrière derrière un comptoir de service, penchée sur une "
  "boîte de carton. Aucun visage reconnaissable, aucun insigne lisible."),
 ('colis', 'vocab', P_VOC, OBJET + " Une boîte de carton brun fermée au ruban, "
  "posée seule au centre d'un comptoir clair, vue de trois quarts. Le carton "
  "est entièrement vierge."),
 ('expediteur', 'vocab', P_VOC, OBJET + " Gros plan sur le coin supérieur "
  "gauche d'une boîte de carton brun, où une petite étiquette blanche est "
  "collée. Les lignes d'écriture de l'étiquette sont des traits bleus "
  "entièrement illisibles."),
 ('destinataire', 'vocab', P_VOC, OBJET + " Gros plan sur le centre d'une "
  "boîte de carton brun, où une grande étiquette blanche est collée bien "
  "droit. Les lignes d'écriture sont des traits noirs plus gros, entièrement "
  "illisibles."),
 ('code-postal', 'vocab', P_VOC, PERS + " Gros plan sur une main qui écrit au "
  "stylo noir sur la dernière ligne d'une étiquette blanche collée sur du "
  "carton brun. Les traits tracés sont illisibles."),
 ('reperage', 'vocab', P_VOC, OBJET + " Gros plan sur un téléphone cellulaire "
  "tenu au-dessus d'une boîte de carton brun. L'écran du téléphone affiche "
  "des barres grises et une ligne horizontale, sans aucun mot lisible."),
 ('balance', 'vocab', P_VOC, OBJET + " Une balance de comptoir à plateau "
  "plat, vue de côté, avec un petit afficheur noir éteint. Le plateau est "
  "vide et propre."),
 ('fragile', 'vocab', P_VOC, OBJET + " Une boîte de carton brun ouverte sur "
  "un comptoir, remplie de papier bulle froissé d'où dépasse le bord d'une "
  "assiette blanche. Aucune inscription sur le carton."),
 ('recu', 'vocab', P_VOC, OBJET + " Un petit ruban de papier blanc de caisse, "
  "légèrement enroulé au bout, posé à côté d'un terminal de paiement sombre "
  "sur un comptoir. Les lignes du papier sont des traits gris illisibles."),
 ('avis-de-livraison', 'vocab', P_VOC, OBJET + " Un petit carton rectangulaire "
  "de couleur pâle tenu à plat sur une paume ouverte, au-dessus d'une table "
  "de cuisine. Ses lignes d'impression sont des traits gris illisibles."),
 ('courrier-recommande', 'vocab', P_VOC, PERS + " Gros plan sur une main qui "
  "signe au stylo sur une petite tablette électronique tendue au-dessus d'un "
  "comptoir. L'écran ne montre qu'un trait de signature, sans aucun mot."),
 ('mandat-poste', 'vocab', P_VOC, OBJET + " Un rectangle de papier épais de "
  "couleur pâle, un peu plus grand qu'un chèque, posé à plat sur un comptoir "
  "clair à côté d'un stylo. Les lignes imprimées sont des traits gris "
  "parfaitement illisibles, et aucun chiffre ne se lit."),
]


def genere(prompt):
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": RATIO,
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + FAL, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.loads(r.read())
    with urllib.request.urlopen(d["images"][0]["url"], timeout=240) as r:
        return r.read()


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
        "params": {"num_images": 1, "aspect_ratio": RATIO,
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

print()
print('%d produite(s), %d sautée(s), %d échec(s) · environ %.2f $'
      % (len(faits), len(sautes), len(echecs), 0.034 * len(faits)))
for e in echecs:
    print('  !! ' + e)
