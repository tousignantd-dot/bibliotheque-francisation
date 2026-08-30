#!/usr/bin/env python3
"""Génère les 24 images de module-n5-services via fal.ai (Nano Banana 2).

Deux destinations :
  · `images/` — les huit illustrations de l'exercice `prImg` ;
  · `vocab/`  — les seize photos du banc de vocabulaire, réduites à 800 px.

**Format 3:2 paysage** : la zone de glisser-déposer est un rectangle de
223 x 132 px. Une image carrée y perd le tiers du haut et du bas.

Le sujet impose la même contrainte que le module du logement, en plus dure :
ce module parle de brochures, de formulaires et de billets de file d'attente.
Or les prompts interdisent tout texte lisible. Les documents et les écrans sont
donc photographiés de biais ou en faible profondeur de champ, les lignes
réduites à des traits gris. C'est voulu : un élève ne doit pas lire un faux
formulaire approximatif sur une photo. Même chose pour les organismes : aucune
enseigne, aucun logo, aucune couleur de marque reconnaissable.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-n5-services/gen_images.py
  python3 build/contenu/module-n5-services/gen_images.py comptoir-guichet
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-n5-services'
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

DOC = ("Photographie réaliste, format paysage, vue rapprochée d'un document de "
       "papier posé à plat, éclairage doux et rasant, faible profondeur de "
       "champ. Les lignes de texte apparaissent comme des traits gris "
       "entièrement illisibles. Aucun mot déchiffrable, aucun logo, aucun "
       "filigrane, aucune personne.")

ECRAN = ("Photographie réaliste, format paysage, écran d'ordinateur portable "
         "vu de trois quarts sur une table de cuisine, éclairage doux du soir, "
         "faible profondeur de champ. Le contenu de l'écran est flou : des "
         "rectangles et des traits gris, aucun mot lisible, aucun logo, aucune "
         "couleur de marque reconnaissable.")

PERS = ("Photographie réaliste, format paysage, scène de la vie quotidienne au "
        "Québec avec une ou deux personnes vues de dos, de trois quarts ou hors "
        "cadrage du visage. Lumière naturelle douce, faible profondeur de champ. "
        "Aucun visage reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX1 = "Je découvre · Exercice 3 — Les mots des services publics"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Je découvre · les huit images de `prImg` ──────────────────────────
 ('brochure-ville', 'images', P_EX1, DOC + " Un dépliant de plusieurs volets ouvert sur "
  "une table de cuisine, à côté d'une enveloppe et de circulaires empilées. Les blocs de "
  "texte et les pictogrammes restent flous et illisibles."),
 ('bacs-trottoir', 'images', P_EX1, STYLE + " Trois bacs roulants de couleurs différentes "
  "— gris, vert et brun — alignés sur un trottoir devant un immeuble à logements, tôt le "
  "matin, lumière rasante. Aucune inscription lisible sur les bacs."),
 ('ecocentre-depot', 'images', P_EX1, STYLE + " Une aire de dépôt extérieure avec de grands "
  "conteneurs ouverts et une file d'autos qui attendent, un vieux réfrigérateur posé au "
  "sol près d'un conteneur. Vue d'ensemble, aucune enseigne lisible."),
 ('appel-telephone', 'images', P_EX1, PERS + " Une personne assise à une table de cuisine, "
  "téléphone contre l'oreille, un stylo à la main au-dessus d'un carnet ouvert. Vue de "
  "trois quarts arrière, visage hors cadrage."),
 ('formulaire-ecran', 'images', P_EX1, ECRAN + " Un formulaire à remplir : une colonne de "
  "champs rectangulaires vides et un bouton en bas de page, tout flou."),
 ('billet-file-attente', 'images', P_EX1, STYLE + " Gros plan sur un billet de papier "
  "numéroté tenu entre le pouce et l'index, remplissant le tiers du cadre. Des rangées de "
  "chaises de salle d'attente entièrement floues derrière. Aucune feuille, aucun document "
  "et aucune table dans le champ."),
 ('comptoir-guichet', 'images', P_EX1, PERS + " Un comptoir de service au public, vu depuis "
  "la salle d'attente : une vitre basse, un écran d'ordinateur de dos, une chaise vide "
  "devant le comptoir. Aucune enseigne, aucun logo."),
 ('preuve-residence', 'images', P_EX1, DOC + " Une facture d'une page et une enveloppe "
  "adressée posées côte à côte sur une table, en légère plongée. Aucune carte de plastique "
  "à logo dans le champ. Tous les caractères sont flous et illisibles."),

 # ── Les seize photos du banc de vocabulaire ───────────────────────────
 ('brochure', 'vocab', P_VOC, DOC + " Un dépliant de plusieurs volets, à demi ouvert, posé "
  "sur une table à côté d'une enveloppe."),
 ('matieres-residuelles', 'vocab', P_VOC, STYLE + " Un camion de collecte municipale arrêté "
  "dans une rue résidentielle, un bac roulant relevé sur le côté. Aucune inscription "
  "lisible sur le camion."),
 ('bac-brun', 'vocab', P_VOC, STYLE + " Un bac roulant brun ouvert au bord d'un trottoir, "
  "un petit seau de cuisine posé à côté, un matin d'automne."),
 ('ecocentre', 'vocab', P_VOC, STYLE + " De grands conteneurs métalliques ouverts alignés "
  "sur une aire asphaltée, avec des branches et de vieux meubles empilés à l'intérieur."),
 ('preuve-residence', 'vocab', P_VOC, DOC + " Une facture d'une page posée sur une table, "
  "et par-dessus, en travers, une carte de plastique bleu pâle sans en-tête ni drapeau, sa "
  "photo d'identité tournée vers le bord du cadre. En légère plongée."),
 ('prepose', 'vocab', P_VOC, PERS + " Une personne assise derrière un comptoir de service, "
  "casque téléphonique sur la tête, vue de trois quarts arrière devant un écran flou."),
 ('requete', 'vocab', P_VOC, ECRAN + " L'ordinateur portable est vu de trois quarts "
  "arrière, le bord inférieur de son écran sorti du cadre, aucun logo ni lettrage sur le "
  "châssis, aucun nom de fabricant. À l'écran, une fiche de suivi : un long numéro net en "
  "haut, puis des lignes grises."),
 ('jour-ouvrable', 'vocab', P_VOC, STYLE + " Un calendrier mural accroché près d'une porte "
  "de cuisine, vu de biais. Son titre et sa rangée de noms de jours sortent du cadre par le "
  "haut : seules la grille de cases et deux dates entourées au crayon restent visibles."),
 ('epeler', 'vocab', P_VOC, PERS + " Une main qui écrit des lettres majuscules espacées sur "
  "un bloc-notes posé près d'un téléphone, vue en plongée. L'écriture reste illisible."),
 ('formulaire', 'vocab', P_VOC, DOC + " Un formulaire de papier posé sur une table avec un "
  "stylo en travers : on distingue une grille de cases vides, sans un mot lisible."),
 ('en-vigueur', 'vocab', P_VOC, DOC + " Un avis d'une page affiché sur un babillard de "
  "liège, une punaise dans le coin, vu de biais. Texte entièrement flou."),
 ('matiere-refusee', 'vocab', P_VOC, STYLE + " Un vieux pneu et un bidon de plastique sans "
  "étiquette posés au sol devant un conteneur fermé, dans une aire de dépôt."),
 ('encadre', 'vocab', P_VOC, ECRAN + " Une page Web où un bloc rectangulaire gris se "
  "détache nettement du reste, en haut à droite. Tout le texte est flou."),
 ('guichet', 'vocab', P_VOC, PERS + " Un comptoir de service au public vu de côté, une "
  "personne debout devant, de dos, un dossier de papiers sous le bras."),
 ('billet-attente', 'vocab', P_VOC, STYLE + " Un seul petit billet de papier crème posé au "
  "centre de l'assise d'une chaise de salle d'attente, vu de près. Le numéro imprimé dessus "
  "est net. Aucun autre papier, aucune table et aucun document dans le cadre."),
 ('piece-identite', 'vocab', P_VOC, DOC + " Deux cartes de plastique posées côte à côte sur "
  "un comptoir clair, en légère plongée, aucun caractère lisible, aucun visage."),
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
