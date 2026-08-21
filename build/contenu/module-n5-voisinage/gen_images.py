#!/usr/bin/env python3
"""Génère les 19 images de module-n5-voisinage via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les six illustrations de l'exercice `prImg` ;
  · `vocab/`  — les treize photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

Trois contraintes propres à ce module :

- **Aucun visage, et c'est plus dur ici qu'ailleurs** : le module raconte des
  gens qui se parlent — un escalier, une fête de ruelle, une cérémonie de
  citoyenneté, un café entre voisines. Toutes les personnes sont donc vues de
  dos, de trois quarts arrière, ou hors cadrage. Plusieurs scènes sont
  simplement vides : la ruelle avant que les gens arrivent, deux tasses sur une
  table, un balcon.
- **Aucun texte lisible.** Le module parle de papiers laissés sur un frigo,
  d'un certificat de citoyenneté, d'une invitation. Tout document est
  photographié de biais ou en faible profondeur de champ, ses lignes réduites à
  des traits gris. Un mot lisible donnerait la réponse d'un exercice.
- **Rien qui ressemble à un document officiel identifiable.** Le certificat de
  citoyenneté est vu de très près et flou, sans armoiries ni sceau
  reconnaissable : on suggère un papier important, on n'imite pas une pièce
  d'identité.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-voisinage/gen_images.py
  python3 build/contenu/module-n5-voisinage/gen_images.py hangar
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n5-voisinage'
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
         "profondeur de champ. Scène québécoise ordinaire et contemporaine, "
         "ni luxueuse ni délabrée, palette sobre. Aucun texte lisible, aucune "
         "écriture, aucun logo, aucune enseigne, aucun filigrane, aucune "
         "personne identifiable.")

RUELLE = ("Photographie réaliste, format paysage, ruelle résidentielle d'un "
          "quartier ancien de Montréal en fin de printemps : immeubles de brique "
          "de trois étages, hangars de bois, clôtures, escaliers de métal. "
          "Lumière naturelle de fin d'après-midi, faible profondeur de champ. "
          "Aucun texte lisible, aucune plaque, aucun graffiti lisible, aucune "
          "personne identifiable.")

INTERIEUR = ("Photographie réaliste, format paysage, intérieur de logement "
             "montréalais modeste et propre, mobilier simple, lumière naturelle "
             "de fenêtre, faible profondeur de champ. Aucun texte lisible, aucun "
             "logo, aucune personne identifiable.")

PAPIER = ("Photographie réaliste, format paysage, cadrage serré et oblique sur un "
          "papier posé ou fixé, faible profondeur de champ. Les lignes du papier "
          "sont réduites à des traits gris : aucun mot, aucun chiffre, aucune "
          "signature n'est lisible. Aucun logo, aucun en-tête reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène de vie de quartier "
        "ordinaire au Québec avec une ou deux personnes vues de dos, de trois "
        "quarts arrière ou hors cadrage du visage. Lumière naturelle douce, "
        "faible profondeur de champ. Aucun visage reconnaissable, aucun texte, "
        "aucun logo, aucun filigrane.")

P_EX1 = "Je découvre · Exercice 3 — Les lieux de l'immeuble"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les six images de `prImg` ───────────────────────────
 ('ruelle-fete', 'images', P_EX1, RUELLE + " Deux tables à tréteaux montées au "
  "milieu de la ruelle, recouvertes de nappes de papier, avec des chaises "
  "dépareillées autour, avant l'arrivée des invités. Aucune personne, aucune "
  "banderole écrite."),
 ('escalier-exterieur', 'images', P_EX1, RUELLE + " Un escalier extérieur de métal "
  "en colimaçon, peint en noir, sur la façade de brique d'un immeuble de trois "
  "logements, vu de la rue en contre-plongée. Aucun numéro civique lisible, "
  "aucune personne."),
 ('balcon-arriere', 'images', P_EX1, RUELLE + " Un balcon de bois à l'arrière d'un "
  "immeuble, avec deux chaises de jardin et trois pots de fleurs, donnant sur la "
  "ruelle. Aucune personne, aucun texte."),
 ('boites-lettres', 'images', P_EX1, INTERIEUR + " Une rangée de six boîtes aux "
  "lettres de métal fixées au mur d'une petite entrée d'immeuble, vues de trois "
  "quarts, quelques circulaires de papier dépassant d'une fente. Aucun nom, aucun "
  "chiffre lisible."),
 ('mot-sur-frigo', 'images', P_EX1, PAPIER + " Une feuille de papier blanc couverte "
  "de quelques lignes manuscrites, retenue par un aimant rond sur la porte d'un "
  "réfrigérateur blanc. L'écriture est entièrement floue et illisible."),
 ('bac-brun', 'images', P_EX1, RUELLE + " Un bac roulant brun de collecte des "
  "résidus alimentaires, couvercle fermé, posé sur le trottoir devant une haie, un "
  "matin. Aucune inscription lisible sur le bac, aucune personne."),

 # ── Je retiens des mots · les treize photos du banc ───────────────────
 ('ruelle-verte', 'vocab', P_VOC, RUELLE + " Une ruelle verte aménagée : bandes de "
  "terre plantées le long des clôtures, vivaces et plants de tomates, quelques "
  "dalles de pierre remplaçant l'asphalte. Aucune personne, aucune affiche."),
 ('hangar', 'vocab', P_VOC, RUELLE + " Un hangar de bois peint en gris au fond "
  "d'une petite cour, porte fermée, une pelle et un vélo appuyés contre le mur. "
  "Aucune personne, aucun texte."),
 ('corvee', 'vocab', P_VOC, PERS + " Trois personnes vues de dos, en gants de "
  "jardinage, en train de ratisser et de planter le long d'une clôture de ruelle, "
  "avec des sacs de terre et une brouette. Aucun visage."),
 ('invitation', 'vocab', P_VOC, PAPIER + " Un carton d'invitation blanc glissé sous "
  "une porte de logement, sur un plancher de bois, vu en plongée oblique. "
  "L'écriture du carton est réduite à des traits gris illisibles."),
 ('plat-partager', 'vocab', P_VOC, INTERIEUR + " Un grand plat de service rempli de "
  "chaussons dorés faits maison, recouvert à moitié d'un linge à vaisselle, posé "
  "sur un comptoir de cuisine. Aucune personne, aucune marque."),
 ('reporter', 'vocab', P_VOC, RUELLE + " La même ruelle sous une pluie fine : les "
  "tables sont repliées contre un hangar, des flaques sur l'asphalte, un ciel gris. "
  "Aucune personne, aucun texte."),
 ('repondeur', 'vocab', P_VOC, INTERIEUR + " Cadrage serré et oblique sur un "
  "téléphone sans fil posé sur sa base, sur un meuble d'entrée, avec un petit "
  "voyant rouge de message allumé. Aucune marque, aucun chiffre lisible."),
 ('mot-papier', 'vocab', P_VOC, PAPIER + " Une feuille de bloc-notes couverte de "
  "quelques lignes manuscrites, posée bien en évidence au milieu d'une table de "
  "cuisine, à côté d'un stylo. L'écriture est floue et illisible."),
 ('arroser', 'vocab', P_VOC, INTERIEUR + " Un arrosoir de métal versant de l'eau "
  "dans un grand pot de plante verte, près d'une fenêtre lumineuse. Une main est "
  "visible au bord du cadre, aucun visage."),
 ('felicitations', 'vocab', P_VOC, PERS + " Deux personnes vues de dos, l'une "
  "posant la main sur l'épaule de l'autre, devant une porte d'entrée de logement, "
  "dans une lumière chaude de fin de journée. Aucun visage, aucun texte."),
 ('citoyennete', 'vocab', P_VOC, PAPIER + " Cadrage très serré et oblique sur un "
  "certificat de papier crème tenu à deux mains au-dessus d'une table, avec un "
  "petit drapeau canadien rouge et blanc posé à côté. Le certificat est flou : "
  "aucun mot, aucune armoirie, aucun sceau n'est lisible ou reconnaissable."),
 ('ceremonie', 'vocab', P_VOC, PERS + " Une grande salle communautaire vue du fond, "
  "rangées de chaises occupées par des personnes vues de dos, quelques petits "
  "drapeaux canadiens rouges et blancs, éclairage neutre de plafond. Aucun visage, "
  "aucune affiche lisible, aucune estrade identifiable."),
 ('feter', 'vocab', P_VOC, INTERIEUR + " Deux tasses de café fumantes et une "
  "assiette de biscuits sur une petite table de cuisine, près d'une fenêtre, deux "
  "chaises tirées. Aucune personne, aucune marque."),
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
