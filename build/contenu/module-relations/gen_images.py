#!/usr/bin/env python3
"""Génère les 21 images du module-relations via fal.ai (Nano Banana 2).

Deux destinations, deux formats :
  · `images/` — les illustrations d'exercice, 1024 px, telles que rendues ;
  · `vocab/`  — les photos du banc de vocabulaire, réduites à 800 px / q. 82.

Une image à la fois, journal .json adjacent dans ~/Claude/generations, puis
copie vers le module. Relançable : une image déjà présente est sautée.

  python3 build/contenu/module-relations/gen_images.py
  python3 build/contenu/module-relations/gen_images.py tournoi balcon
"""
import io, json, os, pathlib, sys, time, urllib.request, urllib.error

MODULE = 'module-relations'
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

STYLE = ("Photographie réaliste, format carré, lumière naturelle douce, faible "
         "profondeur de champ. Intérieur ou extérieur québécois ordinaire, palette "
         "sobre et chaleureuse. Aucun texte, aucune écriture, aucun logo, aucun "
         "filigrane, aucune personne identifiable.")

PERS = ("Photographie réaliste, format carré, scène de la vie quotidienne au Québec "
        "avec une ou deux personnes vues de dos, de trois quarts ou hors cadrage du "
        "visage. Lumière naturelle douce, faible profondeur de champ. Aucun visage "
        "reconnaissable, aucun texte, aucun logo, aucun filigrane.")

P_EX  = "Je découvre · Exercice 3 — Les gestes de la semaine"
P_VOC = "Je retiens des mots — banc de vocabulaire"

# (nom, dossier, page, prompt)
IMAGES = [
 # ── Les huit gestes de la semaine (exercice 3) ────────────────────────
 ('brassee', 'images', P_EX, PERS + " Une personne accroupie devant une laveuse "
  "frontale dans une petite salle de lavage d'appartement, en train d'y enfourner "
  "une pile de linge. Panier de plastique posé à côté, boîte de savon sur la "
  "sécheuse."),
 ('balayeuse', 'images', P_EX, PERS + " Une personne passe l'aspirateur sur un "
  "tapis de salon, vue de dos, le tube incliné vers l'avant. Meubles simples, "
  "lumière de fin d'avant-midi par une fenêtre."),
 ('ordures', 'images', P_EX, PERS + " Une personne, de dos, pousse un bac roulant "
  "noir sur le trottoir devant une maison de quartier, tôt le matin. Neige fondante "
  "au sol, autres bacs alignés plus loin dans la rue."),
 ('chaudron', 'images', P_EX, STYLE + " Gros plan en plongée sur un grand chaudron "
  "en inox posé sur une cuisinière, rempli d'un ragoût qui mijote. À côté, six "
  "contenants de plastique alignés, prêts à être remplis et congelés."),
 ('reveil', 'images', P_EX, STYLE + " Gros plan sur un réveille-matin numérique posé "
  "sur une table de chevet, affichant une heure très matinale. La chambre est encore "
  "sombre, une faible lueur bleutée passe par la fenêtre."),
 ('gymnase', 'images', P_EX, STYLE + " Un gymnase de centre communautaire vu du bord "
  "du terrain : filet de volleyball tendu, plancher de bois verni marqué de lignes de "
  "couleur, quelques ballons au sol, gradins vides. Éclairage au plafond."),
 ('autobus', 'images', P_EX, PERS + " Une personne attend seule à un abribus vitré, "
  "le soir, en hiver. Un autobus de ville approche au loin, ses phares éclairant la "
  "neige. Rue de quartier, lampadaires allumés."),
 ('balcon', 'images', P_EX, STYLE + " Un petit balcon d'appartement montréalais en "
  "été, avec un escalier extérieur en métal, deux chaises pliantes et une petite "
  "table où sont posées deux assiettes. Fin de journée, lumière dorée."),

 # ── Les treize mots du banc de vocabulaire ────────────────────────────
 ('brassee', 'vocab', P_VOC, STYLE + " Gros plan sur l'intérieur d'une laveuse "
  "frontale ouverte, à moitié remplie de linge coloré, dans une salle de lavage "
  "d'appartement. Un panier de plastique attend par terre."),
 ('balayeuse', 'vocab', P_VOC, STYLE + " Un aspirateur-traîneau posé au milieu d'un "
  "salon, tube et brosse appuyés contre un fauteuil, fil déroulé jusqu'à la prise "
  "murale."),
 ('bac-recyclage', 'vocab', P_VOC, STYLE + " Un bac de recyclage bleu à roulettes, "
  "couvercle ouvert, rempli de boîtes de carton aplaties, de bouteilles de plastique "
  "et de journaux, posé au bord d'un trottoir de quartier résidentiel."),
 ('quart-travail', 'vocab', P_VOC, STYLE + " Une horloge murale ronde et blanche dans "
  "un corridor de service aux murs clairs, à côté d'un tableau d'affichage où sont "
  "épinglées des feuilles d'horaire vierges. Éclairage fluorescent."),
 ('covoiturage', 'vocab', P_VOC, PERS + " Vue depuis la banquette arrière d'une "
  "voiture : deux personnes assises à l'avant, de dos, sur une rue de banlieue en "
  "soirée d'hiver. Sacs de sport posés sur le siège arrière."),
 ('centre-communautaire', 'vocab', P_VOC, STYLE + " La façade d'un centre "
  "communautaire de quartier en brique claire, avec de grandes fenêtres éclairées, un "
  "escalier de béton et une rampe d'accès. Fin d'après-midi d'automne, feuilles au sol."),
 ('coequipiere', 'vocab', P_VOC, PERS + " Deux joueuses de volleyball en chandail "
  "d'équipe se tapent la main au filet, vues de côté, visages hors cadre. Gymnase "
  "éclairé, plancher de bois."),
 ('sentrainer', 'vocab', P_VOC, PERS + " Une personne s'exerce seule à faire des "
  "passes de volleyball contre un mur de gymnase, ballon en l'air, vue de dos. "
  "Plancher de bois, lignes de terrain visibles."),
 ('tournoi', 'vocab', P_VOC, STYLE + " Un gymnase pendant un tournoi : deux terrains "
  "de volleyball côte à côte séparés par des filets, gradins avec quelques spectateurs "
  "flous, sacs de sport alignés le long du mur."),
 ('demenagement', 'vocab', P_VOC, STYLE + " Le salon d'un logement à moitié vidé : "
  "une dizaine de boîtes de carton empilées, un matelas appuyé contre le mur, du ruban "
  "d'emballage sur le plancher de bois. Pluie visible par la fenêtre."),
 ('naissance', 'vocab', P_VOC, STYLE + " Un petit lit de bébé en bois clair dans une "
  "chambre calme, avec une couverture tricotée pliée sur le bord et un mobile suspendu "
  "au-dessus. Lumière douce de fin de journée. Aucun bébé visible."),
 ('carte-postale', 'vocab', P_VOC, STYLE + " Gros plan en plongée sur une carte "
  "postale vierge posée sur une table de bois, à côté d'un stylo et d'une tasse de "
  "café. Le côté visible est celui de l'adresse, séparé en deux par un trait, avec un "
  "rectangle vide pour le timbre. Aucune écriture."),
 ('carte-voeux', 'vocab', P_VOC, STYLE + " Gros plan sur une carte de souhaits ouverte "
  "posée debout sur une commode, à côté d'une enveloppe blanche. L'intérieur de la "
  "carte est vierge, sans aucun texte. Petit bouquet de fleurs séchées à côté."),
]


def genere(prompt):
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": "1:1",
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + FAL, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.loads(r.read())
    with urllib.request.urlopen(d["images"][0]["url"], timeout=240) as r:
        return r.read()


def reduire(data, cote=800, qualite=82):
    """Les photos du banc sont vues petites : 1024 px n'y sert à rien."""
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert('RGB')
    im = im.resize((cote, cote), Image.LANCZOS)
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
        "params": {"num_images": 1, "aspect_ratio": "1:1",
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
